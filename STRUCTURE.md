# Repository and installed layout

```text
codex-setup/
├── VERSION                     # Release source of truth
├── README.md, CHANGELOG.md      # Product overview and release history
├── AGENTS.md                   # Instructions for maintaining this repository
├── .codex/config.toml          # This repository's project layer
├── .github/workflows/          # Cross-platform gate and tagged release automation
├── agents/                     # 23 standalone native TOML agents
├── global/                     # Personal AGENTS.md and config defaults
├── profiles/                   # Build/review/compute profile files
├── skills/                     # Eight scoped SKILL.md workflows
├── hooks/                      # Advisory PostToolUse handler
├── rules/                      # Command-policy guide and opt-in example
├── templates/                  # Project/context/PR/decision templates
├── examples/                   # Four worked project examples
├── docs/                       # Installation, behavior, support, and release docs
├── scripts/                    # Install/restore, validation, release packaging
└── tests/                      # Isolated behavioral tests
```

The installer writes personal instructions, configuration, agents, profiles, and
optional hooks under `CODEX_HOME` (default `~/.codex`). User skills go under
`~/.agents/skills`. Private original-file backups remain under
`CODEX_HOME/setup-backups/`; they are never part of release archives.

Project instructions and optional `.codex/config.toml` go only to the project
explicitly supplied with `--project`. Additional templates are opt-in references;
`examples/` are fictional and are not copied by the installer. The `.rules` example
is not automatically installed. Existing unrelated files remain user-owned.
