import hashlib
import importlib.util
from pathlib import Path
import subprocess
import tarfile
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('release', ROOT / 'scripts/release.py')
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.repo = self.base / 'repo'
        self.repo.mkdir()
        self.git('init', '-q')
        (self.repo / 'VERSION').write_text('1.0.0\n')
        (self.repo / 'docs/releases').mkdir(parents=True)
        (self.repo / 'docs/releases/v1.0.0.md').write_text('# v1.0.0\n\nFirst release.\n')
        (self.repo / 'hello.txt').write_text('hello\n')
        self.git('add', '.')
        self.git('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
                 '-c', 'core.hooksPath=/dev/null', 'commit', '--no-gpg-sign', '-qm', 'Initial fixture')
        self.git('tag', 'v1.0.0')

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.repo), *args], stderr=subprocess.STDOUT)

    def test_archives_checksums_and_reproducibility(self):
        first = release.package(self.repo, self.base / 'first', 'v1.0.0')
        second = release.package(self.repo, self.base / 'second', 'v1.0.0')
        for a, b in zip(first, second, strict=True):
            self.assertEqual(a.read_bytes(), b.read_bytes())
        with tarfile.open(first[0]) as archive:
            self.assertEqual(archive.extractfile('codex-setup-v1.0.0/hello.txt').read(), b'hello\n')
            self.assertTrue(all(m.name.startswith('codex-setup-v1.0.0/') for m in archive.getmembers()))
        with zipfile.ZipFile(first[1]) as archive:
            self.assertEqual(archive.read('codex-setup-v1.0.0/VERSION'), b'1.0.0\n')
        for line in first[2].read_text().splitlines():
            sha, name = line.split('  ')
            self.assertEqual(sha, hashlib.sha256((first[2].parent / name).read_bytes()).hexdigest())

    def test_dirty_tree_refused_without_output(self):
        (self.repo / 'hello.txt').write_text('changed\n')
        with self.assertRaisesRegex(ValueError, 'clean'):
            release.package(self.repo, self.base / 'output')
        self.assertFalse((self.base / 'output').exists())

    def test_mismatched_tag_refused(self):
        with self.assertRaisesRegex(ValueError, 'Tag'):
            release.package(self.repo, self.base / 'output', 'v2.0.0')

    def test_tag_must_reference_packaged_commit(self):
        (self.repo / 'hello.txt').write_text('new revision\n')
        self.git('add', '.')
        self.git('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
                 '-c', 'core.hooksPath=/dev/null', 'commit', '--no-gpg-sign', '-qm', 'Another fixture')
        with self.assertRaisesRegex(ValueError, 'HEAD'):
            release.package(self.repo, self.base / 'output', 'v1.0.0')
