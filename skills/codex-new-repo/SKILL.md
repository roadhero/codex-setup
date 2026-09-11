---
name: codex-new-repo
description: Add Codex project instructions to a new or existing repository when the user requests scaffolding or onboarding.
---

Explicit user instructions take precedence over these guidelines.

Inspect the destination and existing AGENTS.md, .codex/config.toml, manifests, and CI first. Preserve existing files and unrelated Git state.

Use the project's existing layout and toolchain. Create or merge a short root AGENTS.md describing verified product context, commands, boundaries, and acceptance criteria. Add nested guidance only for components that need it, and link it from the root so it is read when working across components. For a genuinely new project, identify the language/runtime from the user's request; ask only for decisions that cannot safely be inferred.

Use the matching engineering platform skill when available. Project configuration should contain only differences from personal defaults. A new .codex/config.toml needs project trust before Codex loads it; do not silently trust a whole parent directory. Local skills belong under .agents/skills.

Build runnable CI from actual project commands if CI scaffolding was requested. Do not install a placeholder release workflow, invent signing credentials, create a remote, stage, commit, or publish merely to add instructions. Report created/merged/skipped files and unresolved product-specific decisions.
