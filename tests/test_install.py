import importlib.util
import contextlib
import io
from pathlib import Path
import tempfile
import tomllib
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', ROOT / 'scripts/install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name).resolve()
        self.codex = self.home / '.codex'

    def test_install_idempotent_and_restore_exact_existing_state(self):
        self.codex.mkdir()
        original = '# Keep this comment\nmodel = "personal-model"\n[mcp_servers.private]\ncommand = "private-tool"\n'
        (self.codex / 'config.toml').write_text(original)
        (self.codex / 'AGENTS.md').write_text('Personal instructions\n')
        (self.codex / 'auth.json').write_text('DO NOT TOUCH')
        changes = installer.plan(self.home, self.codex, hooks=True)
        self.assertEqual((self.codex / 'config.toml').read_text(), original)
        manifest = installer.apply(changes, self.codex / 'setup-backups')
        merged = tomllib.loads((self.codex / 'config.toml').read_text())
        self.assertEqual(merged['model'], 'personal-model')
        self.assertEqual(merged['mcp_servers']['private']['command'], 'private-tool')
        self.assertEqual(installer.plan(self.home, self.codex, hooks=True), {})
        with contextlib.redirect_stdout(io.StringIO()):
            installer.restore(manifest, execute=True)
        self.assertEqual((self.codex / 'config.toml').read_text(), original)
        self.assertEqual((self.codex / 'AGENTS.md').read_text(), 'Personal instructions\n')
        self.assertEqual((self.codex / 'auth.json').read_text(), 'DO NOT TOUCH')
        self.assertFalse((self.codex / 'agents/architect.toml').exists())

    def test_existing_permissions_and_agent_settings_are_preserved(self):
        original = 'sandbox_mode = "read-only"\n[agents]\nenabled = false\n'
        new = installer.config_defaults(original, {'sandbox_mode': 'workspace-write', 'agents': {'enabled': True}})
        self.assertEqual(new, original)
        original = 'default_permissions = ":read-only"\n'
        new = installer.config_defaults(original, {'sandbox_mode': 'workspace-write', 'approval_policy': 'on-request'})
        self.assertEqual(new, original)

    def test_post_install_changes_block_entire_restore(self):
        manifest = installer.apply(installer.plan(self.home, self.codex), self.codex / 'setup-backups')
        changed = self.codex / 'agents/architect.toml'
        changed.write_text('User edit')
        original = (self.codex / 'AGENTS.md').read_bytes()
        with self.assertRaises(ValueError):
            installer.restore(manifest, execute=True)
        self.assertEqual((self.codex / 'AGENTS.md').read_bytes(), original)
        self.assertEqual(changed.read_text(), 'User edit')

    def test_refuse_existing_assets_without_writes(self):
        folder = self.codex / 'agents'
        folder.mkdir(parents=True)
        (folder / 'architect.toml').write_text('existing custom agent')
        with self.assertRaises(ValueError):
            installer.plan(self.home, self.codex)
        self.assertFalse((self.codex / 'AGENTS.md').exists())

    def test_refuse_symlink_destination(self):
        external = self.home / 'external'
        external.mkdir()
        self.codex.symlink_to(external, target_is_directory=True)
        with self.assertRaises(ValueError):
            installer.plan(self.home, self.codex)
        self.assertEqual(list(external.iterdir()), [])

    def test_override_file_blocks_ineffective_install(self):
        self.codex.mkdir()
        (self.codex / 'AGENTS.override.md').write_text('Overrides')
        with self.assertRaises(ValueError):
            installer.plan(self.home, self.codex)
        (self.codex / 'AGENTS.override.md').unlink()
        project = self.home / 'project'
        project.mkdir()
        (project / 'AGENTS.override.md').write_text('Project overrides')
        with self.assertRaises(ValueError):
            installer.plan(self.home, self.codex, project)

    def test_malformed_markers_refused(self):
        for text in [installer.BEGIN, installer.END, installer.END + installer.BEGIN]:
            with self.assertRaises(ValueError):
                installer.guidance(text, 'new')

    def test_project_context_and_config_preserved(self):
        project = self.home / 'project with spaces'
        (project / '.codex').mkdir(parents=True)
        (project / 'AGENTS.md').write_text('Existing project commands\n')
        (project / '.codex/config.toml').write_text('model = "project-model"\n')
        changes = installer.plan(self.home, self.codex, project, 'ios')
        installer.apply(changes, self.codex / 'setup-backups')
        self.assertTrue((project / 'AGENTS.md').read_text().startswith('Existing project commands'))
        self.assertEqual((project / '.codex/config.toml').read_text(), 'model = "project-model"\n')
        self.assertEqual(installer.plan(self.home, self.codex, project, 'ios'), {})

    def test_changed_preview_refused(self):
        changes = installer.plan(self.home, self.codex)
        self.codex.mkdir()
        (self.codex / 'config.toml').write_text('model = "new"\n')
        with self.assertRaises(ValueError):
            installer.apply(changes, self.codex / 'setup-backups')
        self.assertFalse((self.codex / 'AGENTS.md').exists())

    def test_write_failure_rolls_back_completed_files(self):
        changes = installer.plan(self.home, self.codex)
        real_write = installer.atomic_write

        def write(path, data, mode=0o600):
            if path == self.codex / 'config.toml':
                raise OSError('simulated disk error')
            real_write(path, data, mode)

        with patch.object(installer, 'atomic_write', side_effect=write):
            with self.assertRaises(OSError):
                installer.apply(changes, self.codex / 'setup-backups')
        self.assertFalse((self.codex / 'AGENTS.md').exists())


if __name__ == '__main__':
    unittest.main()
