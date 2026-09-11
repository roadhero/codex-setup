#!/usr/bin/env python3
"""Advisory whitespace check after apply_patch; never edits or exposes diff content."""
import json
from pathlib import Path
import subprocess
import sys


def inspect(event):
    if not isinstance(event, dict) or event.get('tool_name') != 'apply_patch':
        return None
    cwd = event.get('cwd')
    if not isinstance(cwd, str) or not Path(cwd).is_dir():
        return None
    # --no-ext-diff avoids executing a repository's external diff helper.
    root = subprocess.run(['git', '-C', cwd, 'rev-parse', '--show-toplevel'],
                          capture_output=True, timeout=3)
    if root.returncode:
        return None
    result = subprocess.run(['git', '-C', cwd, 'diff', '--no-ext-diff', '--check'],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                            timeout=5)
    if result.returncode == 2:
        return {'hookSpecificOutput': {'hookEventName': 'PostToolUse',
                'additionalContext': 'git diff --check found whitespace errors in the working tree. Inspect the affected diff; fix only errors within your authorized changes. Run the project formatter/checks as appropriate. This advisory does not cover untracked files or prove tests passed.'}}
    return None


def main():
    try:
        result = inspect(json.load(sys.stdin))
        if result:
            print(json.dumps(result))
    except (ValueError, OSError, subprocess.TimeoutExpired):
        # Advisory only: missing git, bad input, or a slow repository must not block work.
        pass


if __name__ == '__main__':
    main()
