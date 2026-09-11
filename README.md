# Codex setup

[![Gate](https://github.com/roadhero/codex-setup/actions/workflows/gate.yml/badge.svg)](https://github.com/roadhero/codex-setup/actions/workflows/gate.yml)
[![Release](https://img.shields.io/github/v/release/roadhero/codex-setup)](https://github.com/roadhero/codex-setup/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A complete engineering workspace for OpenAI Codex: personal and project
instructions, 23 native specialist agents, eight focused skills, named profiles,
project templates, an advisory edit hook, and a tested installer with backups.

Keep reusable preferences global. Put concrete commands, architecture, hardware,
and delivery constraints in the project. Install only what belongs at each level.
The configuration follows [official OpenAI documentation](docs/sources.md), uses
Codex's native formats, and inherits your selected model and reasoning settings.

## Quick start

Requires macOS or Linux, Python 3.11+, Git, and Codex CLI 0.154.0 or newer.
See [compatibility](docs/compatibility.md) for the tested baseline.

```sh
git clone https://github.com/roadhero/codex-setup.git
cd codex-setup
git checkout v1.0.0
python3 scripts/install.py             # preview
python3 scripts/install.py --apply     # install with backups
```

Alternatively, download a versioned archive and SHA256SUMS from
[Releases](https://github.com/roadhero/codex-setup/releases), verify it as described
in [installation](docs/installation.md), and run the same installer from the
extracted directory. No remote script is piped into a shell.

Start a fresh Codex session after installation:

```sh
codex --profile setup-build
codex --profile setup-review
codex --profile setup-compute
```

The installer preserves existing configuration, MCP connections, authentication,
plugins, and unrelated skills. It adds missing defaults, appends a marked guidance
block, and refuses conflicting custom assets. See [installation and rollback](docs/installation.md).

## Included

| Component | What it provides |
| --- | --- |
| [Global instructions](global/AGENTS.md) | Focused engineering agreements, task completion, Git hygiene, and verification |
| [Configuration](global/config.toml) | Workspace sandbox, on-request approvals, live web search, bounded subagents |
| [23 native agents](docs/agents.md) | Planning, implementation, review, QA, security, operations, delivery, and compute specialists |
| [Eight skills](docs/skills.md) | Web, Android, iOS, compute, onboarding, quality gates, release preparation, and documentation reconciliation |
| [Profiles](profiles/) | Separate build, review, and compute configuration files |
| [Project templates](templates/) | Root/component instructions and trusted-project configuration |
| [Worked examples](examples/) | Web, Android, iOS, and compute project context |
| [Edit hook](docs/hooks.md) | Optional native post-edit whitespace feedback; no file mutation |
| [Command policy](rules/README.md) | Narrow native-rule guidance and a testable example |
| [Installation](scripts/install.py) | Preview, backup, idempotent install, conflict refusal, and guarded restoration |
| [Release tooling](docs/releases.md) | Version/tag parity, tested archives, checksums, and GitHub release automation |

A root `AGENTS.md` and `.codex/config.toml` configure this repository itself.
Other repositories inherit the personal setup and add local context as needed.
Read [STRUCTURE.md](STRUCTURE.md) for the complete layout.

## Project setup

Ask Codex to use `$codex-new-repo` to inspect a repository and write actual project
commands. For a static starter:

```sh
python3 scripts/install.py --project /absolute/path/to/repo --stack android
python3 scripts/install.py --project /absolute/path/to/repo --stack android --apply
```

The project option also performs global installation. Existing instructions are
preserved; replace starter guidance with real project facts. Supported stacks are
`web`, `android`, `ios`, and `compute`. It never initializes Git, publishes a
project, or grants project trust. See [project setup](docs/projects.md).

## Skills and agents

Use `$codex-quality-gate` for the project's actual formatter and verification
commands, `$codex-release-prep` for release work, and `$codex-reconcile-docs` for
documentation drift. Platform skills are selected by task or invoked explicitly.

Request specialist work when useful: “Have architect inspect the design and
code-reviewer review the diff independently, then combine the findings.” No global
instruction forces delegation. Read [workflow](docs/workflow.md) and
[agent responsibilities](docs/agents.md).

## Optional hook

```sh
python3 scripts/install.py --hooks
python3 scripts/install.py --hooks --apply
```

Restart Codex and review/trust the definition in `/hooks`. The hook provides
whitespace feedback after `apply_patch`; it never rewrites files and is not a
commit guard or secret scanner. Use project Git hooks and CI for mandatory gates.
[Hook behavior and limitations](docs/hooks.md).

## Verification

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

CI runs the same checks on macOS and Linux. Tests use temporary destinations and
never install into your real home. Native startup/discovery checks and the limits
of verification are documented in [validation](docs/installation-verification.md).

## Documentation

- [Installation, upgrades, and rollback](docs/installation.md)
- [Configuration and permissions](docs/configuration.md)
- [Project setup and monorepos](docs/projects.md)
- [Workflow and Git practices](docs/workflow.md)
- [Hooks](docs/hooks.md), [skills](docs/skills.md), and [agents](docs/agents.md)
- [Troubleshooting](docs/troubleshooting.md) and [compatibility](docs/compatibility.md)
- [Design decisions](docs/review.md) and [official sources](docs/sources.md)
- [Release process](docs/releases.md), [changelog](CHANGELOG.md), and [v1.0.0 notes](docs/releases/v1.0.0.md)
- [Contributing](CONTRIBUTING.md) and [security policy](SECURITY.md)

MIT licensed. This is a community project, not an official OpenAI product.
