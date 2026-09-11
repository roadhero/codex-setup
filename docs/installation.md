# Installation, upgrades, and restoration

Install Python 3.11+, Git, and a compatible Codex CLI first. Use the
[official Codex quickstart](https://learn.chatgpt.com/docs/quickstart) for the client.
Run this kit from its checkout or an extracted release archive.

## Verify a release archive

Download a matching archive and SHA256SUMS from the release page. From the download
directory, compare the checksum for the archive you selected:

```sh
shasum -a 256 codex-setup-v1.0.0.tar.gz   # macOS
sha256sum codex-setup-v1.0.0.tar.gz      # Linux
```

It must equal that file's line in SHA256SUMS. Extract the archive, enter its
`codex-setup-v1.0.0` directory, and preview installation:

```sh
python3 scripts/install.py
python3 scripts/install.py --apply
```

Preview output lists paths only. Existing config values/tables and unrelated files
are preserved. Global AGENTS.md receives a replaceable marked block. A nonempty
AGENTS.override.md causes an explicit conflict because it would shadow the new
instructions. Customized agent/profile/skill files also cause a conflict before
any write. Review and merge them deliberately; there is no force-overwrite flag.

The optional `--hooks` flag adds the advisory hook. Restart Codex and use `/hooks`
to review/trust the exact definition. Project settings similarly need project
trust. The installer never grants either form of trust.

## Destination options

`CODEX_HOME` is honored; otherwise configuration goes to `~/.codex`. Skills go to
`~/.agents/skills`. `--home` and `--codex-home` allow explicit test destinations.
When testing, specify both so an existing CODEX_HOME cannot select your real home:

```sh
python3 scripts/install.py --home /tmp/test-user --codex-home /tmp/test-user/.codex
```

Do not point CODEX_HOME at a project's `.codex/` layer: it represents the full user
home, including runtime/authentication state. Symlink destinations are refused.

## Upgrades

Read the target release notes, check out/download that version, and preview again.
An unchanged install reports zero files. Existing custom assets require a deliberate
merge; the installer never guesses how to reconcile edited skills or agents.
It does not delete files removed in a later release. If moving between versions,
restore the preceding install first when practical, then install the new version.

## Backups and rollback

Each nonempty application prints a private manifest under
`CODEX_HOME/setup-backups/install-*/manifest.json`. Backup files preserve exact
original bytes and modes; newly created files are recorded separately. Writes are
atomic per file, with best-effort rollback of completed writes on ordinary I/O
failure. This is not a filesystem-wide power-failure transaction.

```sh
python3 scripts/install.py --restore /absolute/path/to/manifest.json
python3 scripts/install.py --restore /absolute/path/to/manifest.json --apply
```

The first command previews; the second restores originals and removes files created
by that installation. Restore validates all current hashes before writing and
refuses post-install edits. Restore multiple installs newest first. Empty directories
and backups remain. Keep backups private and use only trusted manifests.
