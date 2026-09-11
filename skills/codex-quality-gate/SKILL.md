---
name: codex-quality-gate
description: Run a repository quality gate or format changed files using its established tools.
---

Explicit user instructions take precedence over these guidelines.

Read project instructions and CI/manifests to identify exact checks. Inspect git status before running tools. Run appropriate formatting/lint/type/test/build checks for the requested scope. Formatting writes must target intended files; do not reformat unrelated user edits.

Prefer repository-pinned formatters and existing check commands. Do not auto-download tools, silently ignore formatter failures, or weaken checks. Use failure output to distinguish actual defects from unavailable dependencies/services/devices. Fix failures within the authorized task and rerun affected checks.

Review the resulting diff and report commands, outcomes, and meaningful coverage gaps. Never claim checks passed if they were skipped. No external code-review service is required by this workflow.
