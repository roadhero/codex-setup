#!/usr/bin/env python3
"""Offline structural validation of the kit, not an account/runtime smoke test."""
from pathlib import Path
import re
import tomllib
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def main():
    version = (ROOT / 'VERSION').read_text().strip()
    assert re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+', version), 'Invalid VERSION'
    required = ['README.md', 'CHANGELOG.md', 'LICENSE', 'SECURITY.md', 'CONTRIBUTING.md',
                'STRUCTURE.md', '.github/workflows/gate.yml', '.github/workflows/release.yml',
                f'docs/releases/v{version}.md']
    for name in required:
        assert (ROOT / name).is_file(), f'Missing release file: {name}'
    assert f'## [{version}]' in (ROOT / 'CHANGELOG.md').read_text(), 'Missing changelog entry'
    assert (ROOT / f'docs/releases/v{version}.md').read_text().startswith(f'# v{version} ')
    tomls = list(ROOT.rglob('*.toml'))
    for path in tomls:
        value = tomllib.loads(path.read_text())
        if path.parent.name == 'agents':
            for field in ('name', 'description', 'developer_instructions'):
                assert isinstance(value.get(field), str) and value[field].strip(), path
            assert value['name'] == path.stem, path
    skills = list((ROOT / 'skills').glob('*/SKILL.md'))
    for path in skills:
        text = path.read_text()
        assert text.startswith('---\n'), path
        frontmatter = text.split('---', 2)[1]
        assert re.search(r'^name: ' + re.escape(path.parent.name) + r'$', frontmatter, re.M), path
        assert re.search(r'^description: \S.+$', frontmatter, re.M), path
        assert len(text.encode()) < 32768, path
        assert not re.search(r'\bTODO\b|\[INSERT', text), path
    assert (ROOT / 'global/AGENTS.md').stat().st_size < 8192
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts or 'dist' in path.parts:
            continue
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            target = target.split(' "', 1)[0].strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or not parsed.path:
                continue
            assert (path.parent / unquote(parsed.path)).exists(), f'Broken link in {path}: {target}'
    print(f'Validated release {version}, {len(tomls)} TOML files, {len(skills)} skills, and local documentation links.')


if __name__ == '__main__':
    main()
