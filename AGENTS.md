# codex-setup maintenance

This is a personal Codex configuration kit, targeting Codex CLI 0.154.0 or newer.
The current documentation baseline was checked on 2026-09-11. Consult
docs/sources.md before changing configuration shapes. Preserve existing user
configuration, MCP connections, skills, Git state, and credentials on installation.

Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`.
Use Python 3.11+ (stdlib only). Test installation and restoration in temporary
homes, never against real user settings. Avoid network access in unit tests.

Global files live under global/, native agents under agents/, local skills under
skills/, profile files under profiles/, and project examples under templates/.
Global deployment is an explicit installer operation, not part of validation.
Do not automatically trust hooks or projects, change Git identity, initialize a
remote, commit, push, publish, or replace unrelated configuration.

Release preparation uses VERSION, CHANGELOG.md, and docs/releases/vX.Y.Z.md.
Publish only within explicit user authorization. Follow docs/releases.md and
verify that archives, tag, notes, and release target describe the same commit.
Do not commit machine-specific installation reports or private backup paths.
