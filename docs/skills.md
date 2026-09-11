# Skills

The installer adds eight local skills under `~/.agents/skills`. Each has native
name/description frontmatter and a focused body. Codex can select them by task,
or you can invoke them by name. They contain no mandatory external integrations.

| Skill | Use |
| --- | --- |
| `$engineering-web` | Application/service boundaries, persistence, API compatibility, UI behavior |
| `$engineering-android` | Lifecycle/state, coroutines, variants, persistence, device/release verification |
| `$engineering-ios` | State/actors, Swift/Xcode toolchain, persistence, signing/device verification |
| `$engineering-compute` | Native ownership, CUDA, numerics, parallelism, benchmarks, hardware constraints |
| `$codex-new-repo` | Inspect and create project instructions and requested scaffolding |
| `$codex-quality-gate` | Run actual repository formatting, lint, type, test, and build commands |
| `$codex-release-prep` | Prepare versions, notes, artifacts, and relevant release validation |
| `$codex-reconcile-docs` | Identify or fix evidence-backed documentation drift |

Descriptions are available during discovery; the body loads when the skill is
used. Keep project-only skills in `.agents/skills` within that repository. Avoid
copying every platform's detailed rules into global AGENTS.md. Explicit user
instructions take precedence over these workflow defaults.
