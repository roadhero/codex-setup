# Engineering workflow

For substantial changes, establish the outcome and inspect existing patterns,
implement the smallest coherent change, review the diff, and verify behavior.
One agent can perform all steps. Delegate bounded independent work when requested;
assign clear file ownership and use separate worktrees for branch isolation.

Broad, independent file-location and call-path searches can use `repo-explorer`
under the global delegation instruction. Return concise evidence to the main
thread, preserve useful parallel work, and leave simple lookups local. See
[repository exploration](exploration.md). Design, correctness, and implementation
remain with the appropriate reasoning role.

Scale the process to the change. A wording correction does not need a design
ceremony; a persistence migration needs realistic old-data and recovery checks.
Continue already authorized work without demanding repeated approval. Surface
material assumptions and ask when a missing fact or permission actually blocks it.

## Evidence and tests

Use project-pinned formatters, lint/type checks, tests, and builds. Test a meaningful
regression rather than mirroring implementation. For performance work record the
baseline, workload, hardware, variability, and resulting change. Distinguish bugs
from missing services, tools, credentials, or target devices.

A failed check is investigated, not disabled. Review findings include a reachable
trigger, impact, and a precise location. Confirm agent reports against repository
evidence. Report unavailable checks rather than claiming a green gate.

## Git and delivery

Preserve unrelated edits and configured Git identity. Use the repository's branch
and review policy. Keep commits coherent and PR descriptions about the problem,
resulting behavior, and validation. Do not skip hooks to conceal a failure, or
amend an earlier commit after a new commit attempt failed.

For stacked work, rebase each remaining branch onto the actual merged base after
its prerequisite lands; verify conflicts and tests before publishing updates.
Use draft PRs when useful, and check required CI at the final pushed commit.
Publishing and history rewrites must stay within the user's authorization.

## Continuity

Save durable decisions in the project's established docs when useful. Keep working
notes scoped and free of credentials. Reconcile documentation after relevant changes
or when requested. Do not create speculative tickets or recurring tasks after the
requested outcome is complete.
