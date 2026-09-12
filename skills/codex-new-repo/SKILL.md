---
name: codex-new-repo
description: Add Codex project instructions when the user requests scaffolding or onboarding, or on a first implementation task in a project without existing guidance when global instructions enable automatic onboarding.
---

Explicit user instructions take precedence over these guidelines.

Inspect the destination, applicable instructions (including AGENTS.override.md and configured fallback filenames), .codex/config.toml, manifests, and CI first. Preserve existing files and unrelated Git state.

For automatic onboarding, establish the Git root or use the project directory explicitly designated by the user. Do not treat a home directory or general-purpose parent directory as a project. If project guidance already exists, use it and continue the task without automatic additions or rewrites. Read-only questions/reviews, requests to skip setup, and file-write restrictions exclude automatic onboarding. Explicit onboarding requests can merge existing instructions within the user's scope.

Use the project's existing layout and toolchain. Create or merge a short root AGENTS.md describing verified product context, commands, boundaries, and acceptance criteria. Add nested guidance only for components that need it, and link it from the root so it is read when working across components. For a genuinely new project, identify the language/runtime from the user's request; ask only for decisions that cannot safely be inferred.

For automatic onboarding, limit setup to a short root AGENTS.md derived from repository evidence and the requested work. Mark unknown commands as unverified or omit them; do not invent them or expand the task to configure CI, hooks, skills, or releases. Read the new guidance explicitly and continue implementation in the same session. Future sessions discover it automatically.

Use the matching engineering platform skill when available. Add project configuration only for an identified task requirement that differs from personal defaults. A new .codex/config.toml needs project trust before Codex loads it; do not silently trust a whole parent directory. Local skills belong under .agents/skills.

Build runnable CI from actual project commands if CI scaffolding was requested. Do not install a placeholder release workflow, invent signing credentials, create a remote, stage, commit, or publish merely to add instructions. Report created/merged/skipped files and unresolved product-specific decisions.
