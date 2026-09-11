# Hooks and quality checks

`python3 scripts/install.py --hooks --apply` installs a native `PostToolUse` hook
matching `^apply_patch$`. Its JSON definition lives in Codex home's hooks.json;
existing unrelated definitions are preserved. The exact command uses the installer
Python executable and an absolute script path. Replacing that interpreter may
require updating the definition and reviewing trust again.

After installation, restart Codex and inspect `/hooks`. Codex skips untrusted
non-managed hooks until their exact definitions are reviewed. Do not bypass trust.

The handler reads the documented JSON stdin fields, checks the Git working tree
with `git diff --no-ext-diff --check`, and emits advisory context when whitespace
errors are found. It never prints the diff, changes files, or blocks an operation.
Malformed inputs, non-repositories, missing Git, and timeouts are harmless no-ops.

Limits: the check sees tracked working-tree changes, not every untracked file. It
can notice pre-existing errors and says to fix only authorized changes. It observes
apply_patch, not every possible filesystem tool. It does not replace a formatter,
commit guard, secret scanner, required CI, or remote branch protection.

For formatting, use `$codex-quality-gate`: it discovers the repository's pinned
commands, scopes edits, and reports failures. Keep mandatory formatting checks and
secret scanning in project CI/Git hooks. No universal shell parser or broad command
allowlist is installed. See the [official hook contract](https://learn.chatgpt.com/docs/hooks).
