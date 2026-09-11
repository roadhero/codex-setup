#!/usr/bin/env python3
"""Build deterministic release archives from a clean, committed Git tree."""
import argparse
import gzip
import hashlib
import io
from pathlib import Path
import re
import subprocess
import tarfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args])


def package(root, output, tag=None):
    root = root.resolve()
    output = output.resolve()
    if git(root, 'status', '--porcelain').strip():
        raise ValueError('Release packaging requires a clean committed tree')
    version = git(root, 'show', 'HEAD:VERSION').decode().strip()
    if not re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+', version):
        raise ValueError('VERSION must be a stable semantic version')
    expected = 'v' + version
    if tag is not None:
        if tag != expected:
            raise ValueError('Tag does not match VERSION')
        if git(root, 'rev-parse', tag + '^{commit}') != git(root, 'rev-parse', 'HEAD'):
            raise ValueError('Release tag must point to HEAD')
    notes = git(root, 'show', f'HEAD:docs/releases/{expected}.md')
    if not notes.startswith(f'# {expected}'.encode()):
        raise ValueError('Release notes heading must match VERSION')
    files = []
    for entry in git(root, 'ls-tree', '-rz', 'HEAD').split(b'\0'):
        if not entry:
            continue
        metadata, name = entry.split(b'\t', 1)
        mode, kind, oid = metadata.split()
        path = name.decode('utf-8')
        if kind != b'blob' or mode not in (b'100644', b'100755'):
            raise ValueError(f'Unsupported release entry: {path}')
        if Path(path).is_absolute() or '..' in Path(path).parts:
            raise ValueError('Unsafe archive path')
        if path == 'dist' or path.startswith('dist/'):
            raise ValueError('Generated dist artifacts must not be tracked')
        destination = output / path
        if destination == root / path:
            raise ValueError('Output must not overwrite source files')
        files.append((path, int(mode, 8) & 0o777, git(root, 'cat-file', 'blob', oid.decode())))
    files.sort()
    output.mkdir(parents=True, exist_ok=True)
    prefix = 'codex-setup-' + expected
    tar_path = output / (prefix + '.tar.gz')
    zip_path = output / (prefix + '.zip')
    with tar_path.open('wb') as raw:
        with gzip.GzipFile(filename='', fileobj=raw, mode='wb', mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode='w', format=tarfile.USTAR_FORMAT) as archive:
                for name, mode, data in files:
                    info = tarfile.TarInfo(prefix + '/' + name)
                    info.size, info.mode, info.mtime = len(data), mode, 0
                    info.uid = info.gid = 0
                    info.uname = info.gname = ''
                    archive.addfile(info, io.BytesIO(data))
    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, mode, data in files:
            info = zipfile.ZipInfo(prefix + '/' + name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = (0o100000 | mode) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, data)
    checksums = ''.join(hashlib.sha256(path.read_bytes()).hexdigest() + '  ' + path.name + '\n'
                        for path in (tar_path, zip_path))
    (output / 'SHA256SUMS').write_text(checksums)
    return tar_path, zip_path, output / 'SHA256SUMS'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist')
    parser.add_argument('--tag', help='Verify a release tag matches VERSION and HEAD')
    args = parser.parse_args()
    for path in package(ROOT, args.output, args.tag):
        print(path)


if __name__ == '__main__':
    main()
