#!/usr/bin/env python3
"""Preview/apply a personal setup; retain exact originals for guarded restoration."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
import sys
import tempfile
import tomllib

ROOT = Path(__file__).resolve().parents[1]
BEGIN = '<!-- codex-setup:begin -->'
END = '<!-- codex-setup:end -->'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked(path):
    path = Path(os.path.abspath(path))
    for part in (path, *path.parents):
        if part.is_symlink():
            raise ValueError(f'Refusing symlink destination: {part}')
    if path.exists() and not path.is_file():
        raise ValueError(f'Not a regular file: {path}')
    return path


def guidance(original, body):
    block = BEGIN + '\n' + body.strip() + '\n' + END
    if BEGIN in original or END in original:
        if original.count(BEGIN) != 1 or original.count(END) != 1:
            raise ValueError('Malformed managed instruction markers')
        start, stop = original.index(BEGIN), original.index(END)
        if stop < start:
            raise ValueError('Reversed managed instruction markers')
        return original[:start] + block + original[stop + len(END):]
    return original + ('\n\n' if original else '') + block + '\n'


def config_defaults(original, defaults):
    """Add absent scalars/tables only; never reserialize existing user TOML."""
    current = tomllib.loads(original)
    additions = []
    tables = []
    for key, value in defaults.items():
        if key in ('sandbox_mode', 'approval_policy') and 'default_permissions' in current:
            continue  # Preserve the user's modern named permission profile.
        if isinstance(value, dict):
            if key in current:
                continue  # Existing table is owned by the user.
            tables.append('\n[' + key + ']\n' + '\n'.join(
                f'{k} = {json.dumps(v)}' for k, v in value.items()))
        elif key not in current:
            additions.append(f'{key} = {json.dumps(value)}')
    result = ('\n'.join(additions) + '\n\n' if additions else '') + original
    if tables:
        result = result.rstrip() + '\n' + '\n'.join(tables) + '\n'
    tomllib.loads(result)
    return result


def plan(home, codex_home, project=None, stack=None, hooks=False):
    changes = {}

    def add(path, data):
        path = checked(path)
        data = data.encode() if isinstance(data, str) else data
        old = path.read_bytes() if path.exists() else None
        if old != data:
            changes[path] = (old, data)

    def merge(path, body):
        path = checked(path)
        old = path.read_text() if path.exists() else ''
        add(path, guidance(old, body))

    merge(codex_home / 'AGENTS.md', (ROOT / 'global/AGENTS.md').read_text())
    config = checked(codex_home / 'config.toml')
    original = config.read_text() if config.exists() else ''
    defaults = tomllib.loads((ROOT / 'global/config.toml').read_text())
    add(config, config_defaults(original, defaults))
    for folder, target in [('agents', codex_home / 'agents'),
                           ('profiles', codex_home),
                           ('skills', home / '.agents/skills')]:
        for source in sorted((ROOT / folder).rglob('*')):
            if source.is_file():
                destination = checked(target / source.relative_to(ROOT / folder))
                if destination.exists() and destination.read_bytes() != source.read_bytes():
                    raise ValueError(f'Existing asset differs; review/merge manually: {destination}')
                add(destination, source.read_bytes())
    if hooks:
        script = codex_home / 'hooks/codex-setup-post-edit.py'
        add(script, (ROOT / 'hooks/post-edit.py').read_bytes())
        hook_path = checked(codex_home / 'hooks.json')
        old_hooks = json.loads(hook_path.read_text()) if hook_path.exists() else {}
        group = {'matcher': '^apply_patch$', 'hooks': [{
            'type': 'command', 'command': shlex.join([sys.executable, str(script)]),
            'timeout': 10, 'statusMessage': 'Checking patch whitespace'}]}
        groups = old_hooks.setdefault('hooks', {}).setdefault('PostToolUse', [])
        if group not in groups:
            if any('codex-setup-post-edit.py' in json.dumps(g) for g in groups):
                raise ValueError('Existing setup hook differs; merge its definition manually')
            groups.append(group)
        add(hook_path, json.dumps(old_hooks, indent=2) + '\n')
    if project:
        project = Path(os.path.abspath(project))
        override = project / 'AGENTS.override.md'
        if override.exists() and override.read_text().strip():
            raise ValueError(f'{override} shadows project AGENTS.md; merge it before installation')
        body = (ROOT / 'templates/AGENTS.project.md').read_text()
        if stack:
            body += '\n' + (ROOT / f'templates/stacks/AGENTS.{stack}.md').read_text()
        merge(project / 'AGENTS.md', body)
        config = checked(project / '.codex/config.toml')
        if not config.exists():
            add(config, (ROOT / 'templates/config.project.toml').read_bytes())
    override = codex_home / 'AGENTS.override.md'
    if override.exists() and override.read_text().strip():
        raise ValueError(f'{override} shadows global AGENTS.md; merge it before installation')
    return changes


def atomic_write(path, data, mode=0o600):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix='.codex-setup-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data)
        os.chmod(name, mode)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def apply(changes, backup_root):
    # Verify the full preview is still current before changing any destination.
    for path, (old, _) in changes.items():
        checked(path)
        if (path.read_bytes() if path.exists() else None) != old:
            raise ValueError(f'Destination changed after preview: {path}')
    if not changes:
        return None
    backup_root.mkdir(parents=True, exist_ok=True)
    backup = Path(tempfile.mkdtemp(prefix='install-', dir=backup_root))
    os.chmod(backup, 0o700)
    records = []
    for i, (path, (old, new)) in enumerate(changes.items()):
        mode = path.stat().st_mode & 0o777 if old is not None else 0o600
        record = {'path': str(path), 'before': f'{i}.bin' if old is not None else None,
                  'after_sha256': digest(new), 'mode': mode}
        if old is not None:
            atomic_write(backup / f'{i}.bin', old)
        records.append(record)
    manifest = backup / 'manifest.json'
    atomic_write(manifest, (json.dumps(records, indent=2) + '\n').encode())
    completed = []
    try:
        for record, (path, (old, new)) in zip(records, changes.items()):
            atomic_write(path, new, record['mode'])
            completed.append((path, old, record['mode']))
    except OSError:
        for path, old, mode in reversed(completed):
            if old is None:
                path.unlink()
            else:
                atomic_write(path, old, mode)
        raise
    return manifest


def restore(manifest, execute=False):
    records = json.loads(manifest.read_text())
    prepared = []
    for record in records:
        path = checked(record['path'])
        if not path.exists() or digest(path.read_bytes()) != record['after_sha256']:
            raise ValueError(f'Refusing to overwrite a post-install change: {path}')
        before = record['before']
        if before is not None and (Path(before).name != before or before in {'.', '..'}):
            raise ValueError('Invalid backup filename')
        data = (manifest.parent / before).read_bytes() if before is not None else None
        prepared.append((path, data, record['mode'], path.read_bytes(), path.stat().st_mode & 0o777))
    completed = []
    try:
        for path, data, mode, installed, installed_mode in prepared:
            print('RESTORE' if data is not None else 'REMOVE CREATED FILE', path)
            if execute:
                if data is None:
                    path.unlink()
                else:
                    atomic_write(path, data, mode)
                completed.append((path, installed, installed_mode))
    except OSError:
        for path, installed, installed_mode in reversed(completed):
            atomic_write(path, installed, installed_mode)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--home', type=Path, default=Path.home())
    parser.add_argument('--codex-home', type=Path)
    parser.add_argument('--project', type=Path)
    parser.add_argument('--stack', choices=['web', 'android', 'ios', 'compute'])
    parser.add_argument('--hooks', action='store_true', help='Add advisory post-edit hook (requires /hooks trust)')
    parser.add_argument('--apply', action='store_true', help='Write changes; otherwise preview only')
    parser.add_argument('--restore', type=Path, help='Preview/restore one private backup manifest')
    args = parser.parse_args()
    if args.restore:
        restore(args.restore, args.apply)
        return
    if args.stack and not args.project:
        parser.error('--stack requires --project')
    home = Path(os.path.abspath(args.home.expanduser()))
    codex_home = args.codex_home or (Path(os.environ['CODEX_HOME']) if 'CODEX_HOME' in os.environ else home / '.codex')
    codex_home = Path(os.path.abspath(codex_home.expanduser()))
    changes = plan(home, codex_home, args.project, args.stack, args.hooks)
    for path, (old, _) in changes.items():
        print('UPDATE' if old is not None else 'CREATE', path)
    print(f'{len(changes)} file(s); ' + ('applying' if args.apply else 'preview only'))
    if args.apply:
        result = apply(changes, codex_home / 'setup-backups')
        if result:
            print('Backup manifest:', result)


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, TypeError) as exc:
        sys.exit(str(exc))
