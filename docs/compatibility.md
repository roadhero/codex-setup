# Compatibility

| Component | Requirement / baseline |
| --- | --- |
| Codex CLI | 0.154.0 tested; use this version or a newer version that retains these interfaces |
| Python | 3.11+; standard library only |
| Platforms | macOS and Linux; CI checks both |
| Git | Needed for repository checks and release packaging |
| Windows | Not tested; install paths and shell examples target macOS/Linux |
| Authentication | Existing Codex sign-in; the kit neither provisions accounts nor copies credentials |

Separate profile files and standalone agent TOML depend on current Codex behavior.
Do not convert them to legacy nested profile tables. Consult current official docs
and `codex --help` when upgrading. No model, provider, reasoning, or service tier is
pinned. Availability depends on the selected account and client.

CLI and IDE share local configuration. Hosted/cloud work needs repository guidance
and its own environment setup; local installation does not configure cloud workers.
Managed settings and live runtime overrides retain their documented precedence.
