# Project setup and monorepos

Use a project AGENTS.md for facts that cannot be global: product purpose, repository
layout, exact commands, architecture boundaries, supported versions/hardware,
release source, and acceptance criteria. See the four fictional examples under
examples/; replace their commands with evidence from your own manifests and CI.

`$codex-new-repo` inspects existing files before writing context. The installer can
instead append a starter block with `--project /path --stack web|android|ios|compute`.
This flag also installs global defaults; it does not build an application or invent
a release workflow for an unknown toolchain. Existing project configuration remains.

A project `.codex/config.toml` contains only differences from personal defaults and
loads only after project trust. Repository skills live in `.agents/skills`; local
agent overrides live in `.codex/agents`. Copy only the roles that actually differ.

## Nested guidance

Codex discovers AGENTS.md from the project root down to its starting directory.
At each directory a nonempty AGENTS.override.md takes priority over AGENTS.md.
Start Codex in the component directory to load its nested instructions directly.
For sessions spanning components, link component guidance from the root and ask
Codex to read it before touching those paths. Discovery is not extension-glob based.

Keep the combined instructions within the configured byte budget (32 KiB by
default). Skills provide detailed procedures on demand. Avoid global fallback
filenames that accidentally load instructions meant for a different tool.

When adding CI or releases, derive real checks from manifests and working commands.
Keep protected branch rules on the remote host; local guidance cannot enforce them.
Use templates/PULL_REQUEST_TEMPLATE.md and templates/decision.md when appropriate.
