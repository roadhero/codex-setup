# Contributing

Open an issue describing a concrete problem or send a focused pull request.
Keep behavior changes small enough to review, and preserve compatibility with
Python 3.11+ and the documented Codex baseline. No Python packages are required.

1. Read AGENTS.md and the relevant official source in docs/sources.md.
2. Add a meaningful regression test for installer, hook, or release behavior.
3. Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`.
4. Update user documentation and CHANGELOG.md under Unreleased.
5. Explain the behavior change and validation in the pull request.

Never test against a real user's authentication directory. Use temporary homes
and repositories. Do not commit credentials, local diagnostic reports, generated
archives, or private install backups. Keep dependencies at zero unless a concrete
need justifies one. Read SECURITY.md for private vulnerability reporting.

The maintainer handles version changes and tagged releases using docs/releases.md.
