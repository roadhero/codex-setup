import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('post_edit', ROOT / 'hooks/post-edit.py')
hook = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook)


class HookTests(unittest.TestCase):
    def test_advisory_reports_without_modifying_or_exposing_diff(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            subprocess.run(['git', 'init', '-q', str(root)], check=True)
            source = root / 'file.txt'
            source.write_text('original\n')
            subprocess.run(['git', '-C', folder, 'add', 'file.txt'], check=True)
            source.write_text('private-value  \n')
            event = {'cwd': folder, 'tool_name': 'apply_patch'}
            result = hook.inspect(event)
            self.assertEqual(result['hookSpecificOutput']['hookEventName'], 'PostToolUse')
            self.assertNotIn('private-value', json.dumps(result))
            self.assertEqual(source.read_text(), 'private-value  \n')
            source.write_text('clean\n')
            self.assertIsNone(hook.inspect(event))

    def test_unrelated_or_malformed_event_is_ignored(self):
        for event in [None, [], {}, {'tool_name': 'Bash'}, {'tool_name': 'apply_patch', 'cwd': 12}]:
            self.assertIsNone(hook.inspect(event))

    def test_non_repository_is_ignored(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertIsNone(hook.inspect({'tool_name': 'apply_patch', 'cwd': folder}))
