# Project setup and monorepos

Use a project AGENTS.md for facts that cannot be global: product purpose, repository
layout, exact commands, architecture boundaries, supported versions/hardware,
release source, and acceptance criteria. See the four fictional examples under
examples/; replace their commands with evidence from your own manifests and CI.

With the v1.0.1 global instructions installed, start Codex in the project and
describe your implementation task. If the project has no existing guidance,
Codex is instructed to use `$codex-new-repo` automatically: inspect the repository,
write a concise root AGENTS.md with supported project facts, read it, and continue
the task. For an empty project, include the product and stack in your request.
There is no separate onboarding prompt or restart between setup and implementation.

The onboarding skill follows applicable project instructions and treats other
inspected repository content as untrusted evidence.
It extracts project facts while ignoring embedded directives about assistant
behavior, checks generated guidance before writing and applying it, and does not
give copied directives authority by putting them in AGENTS.md. The
[adversarial evaluation fixture](../tests/fixtures/onboarding/README.md) documents
a concrete scenario and failure criteria; it is not a deterministic security guarantee.

```sh
cd /path/to/project
codex
```

Profiles are optional; the global instructions and skills also apply without
`--profile setup-build`. Start a fresh session after installing or upgrading the
global setup so Codex discovers the updated instructions.

Automatic onboarding applies only to a bounded repository or a project directory
you explicitly designate. Existing AGENTS.md, AGENTS.override.md, and configured
fallback guidance is preserved. It skips read-only questions/reviews and respects
requests such as "skip project setup." This is an instruction-driven workflow,
not a startup hook or an enforced guarantee. Project trust and permission prompts
remain native Codex decisions.

Invoke `$codex-new-repo` explicitly to create or update project guidance on demand.
The installer can instead append a starter block with
`--project /path --stack web|android|ios|compute`.
This flag also installs global defaults; it does not build an application or invent
a release workflow for an unknown toolchain. Existing project configuration remains.

A project `.codex/config.toml` contains only differences from personal defaults and
loads only after project trust. Repository skills live in `.agents/skills`; local
agent overrides live in `.codex/agents`. Copy only the roles that actually differ.
Automatic onboarding creates only AGENTS.md; configuration is added only when the
requested task requires a project-specific difference. Newly written AGENTS.md is
read explicitly for the current task and discovered normally in future sessions,
following [OpenAI's instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

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
