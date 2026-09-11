# Official documentation and compatibility

Verified 2026-09-11 against the official Codex manual and local codex-cli 0.154.0.
OpenAI's older developers.openai.com/codex URLs now redirect to these pages.

| Surface | Official source | Choice in this kit |
| --- | --- | --- |
| Personal/project layers | https://learn.chatgpt.com/docs/config-file/config-basic | Merge global defaults, optional trusted project config |
| Profiles | https://learn.chatgpt.com/docs/config-file/config-advanced | Separate `<name>.config.toml` files; legacy `[profiles]` is obsolete since 0.134.0 |
| Config schema | https://learn.chatgpt.com/docs/config-file/config-reference | Validate with the installed CLI's `--strict-config` |
| Instructions | https://learn.chatgpt.com/docs/agent-configuration/agents-md | Global then root-to-working-directory instructions; override file wins within a directory; default 32 KiB budget |
| Agents | https://learn.chatgpt.com/docs/agent-configuration/subagents | Standalone TOML files with name, description, developer_instructions |
| Skills | https://learn.chatgpt.com/docs/build-skills | User `~/.agents/skills`, project `.agents/skills`; name/description discovery, body on invocation |
| Hooks | https://learn.chatgpt.com/docs/hooks | Native JSON input/output; exact definitions need trust review via `/hooks` |
| Command rules | https://learn.chatgpt.com/docs/agent-configuration/rules | Experimental prefix rules control commands outside sandbox; not a complete Git policy |
| Permissions | https://learn.chatgpt.com/docs/agent-approvals-security | Workspace sandbox with on-request approvals; managed restrictions still apply |
| MCP | https://learn.chatgpt.com/docs/extend/mcp | Preserve existing servers; credentials remain outside this kit |
| CLI | https://learn.chatgpt.com/docs/developer-commands?surface=cli | Verify installed command flags before use |

Local CLI help confirms file-based profiles, `--strict-config`, both supported
approval values, and the full bypass flag. No model is pinned: model availability
and reasoning support depend on the account and selected model. API model names
are not used to infer Codex account access. No experimental flags are enabled.

CLI and IDE share local configuration. Hosted Codex needs repository instructions
and its own environment setup; copying files into this Mac's home does not
configure cloud jobs. Application/runtime overrides and managed requirements can
take precedence over these personal defaults. Start a new session after installing.
