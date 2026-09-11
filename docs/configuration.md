# Configuration and permissions

The personal baseline adds `approval_policy = "on-request"`,
`sandbox_mode = "workspace-write"`, and `web_search = "live"` when absent. It adds
agent defaults only when no agents table exists. Existing values and tables win.
A modern `default_permissions` setting suppresses addition of the legacy sandbox
and approval keys, preserving the user's selected permission profile.

No model is pinned. Agents inherit the selected model and reasoning effort, except
for any explicit overrides you add. The built-in read-only review profile sets a
sandbox default; project and command-line settings may override it.

Profiles are separate files under Codex home:

- `setup-build.config.toml`: workspace writes, approvals on request.
- `setup-review.config.toml`: read-only sandbox, approvals on request.
- `setup-compute.config.toml`: workspace writes, approvals on request.

Build/compute have identical permissions intentionally; their separate files allow
later personal specialization. Domain behavior comes from skills and project facts.

## Approval choices

- `codex --approve-for-me`: automatic approval review with a workspace sandbox.
- `codex --ask-for-approval never`: do not prompt; operations needing new approval fail.
- `codex --dangerously-bypass-approvals-and-sandbox`: disable approvals and sandboxing.

The full bypass flag is a one-off option, never installed as an alias or default.
Managed policy can still constrain behavior. Choose a mode for the actual task.

## Integrations

Existing MCP servers and plugins are preserved. Use `codex mcp --help` and the
[official MCP documentation](https://learn.chatgpt.com/docs/extend/mcp) when adding
an integration. Keep credentials in the integration's supported authentication
store, never in this repository. This kit does not add third-party connections.

See [official config precedence](https://learn.chatgpt.com/docs/config-file/config-basic)
and [permissions](https://learn.chatgpt.com/docs/agent-approvals-security).
