# Command policy

This kit does not install broad command allowlists. Codex already runs permitted
work inside its sandbox. Rules control commands outside that boundary, so allowing
`python3`, `bash`, `git`, or a package manager wholesale grants far more than a
specific read or build operation.

If a repeated command needs approval, accept a narrowly scoped prefix only after
reviewing it. Native rules are experimental. Test a proposed rule with:

```sh
codex execpolicy check --pretty --rules /path/to/file.rules -- gh pr view 123
```

Protect shared branches with remote branch protection and use the project's Git
hooks and secret scanner for commit hygiene. This setup does not install or
override `core.hooksPath`, Git identity, or branch policy. A prefix rule or shell
regex is not a universal prohibition on force pushes or secret commits.
