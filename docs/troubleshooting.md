# Troubleshooting

| Symptom | Check |
| --- | --- |
| Instructions missing | Start a fresh session; inspect CODEX_HOME and any AGENTS.override.md |
| Project config ignored | Open/trust the intended project; check the starting directory |
| Nested guidance missing | Start in the component or read the linked component file explicitly |
| Profile rejected | Use a separate `<name>.config.toml`; check client version and CLI help |
| Skill not listed | Check its SKILL.md under the discovered user/project location; restart |
| Hook not running | Use `/hooks` to inspect source, enabled state, and trust hash |
| Installer asset conflict | Compare the file with the release; merge deliberately or restore the prior install |
| Restore refused | A file changed after installation; preserve/merge that change before restoring |
| Permission setting unchanged | Existing user values and modern permission profiles are intentionally retained |
| GPU tests unavailable | Use a compatible NVIDIA host; macOS tests cannot establish CUDA correctness |

Use `codex --help` and current official documentation for client-specific commands.
`--strict-config` works for interactive Codex, exec, and app-server startup, not
for `codex features`. Never print authentication stores or raw private diagnostics
in an issue. Provide version numbers, redacted errors, and a minimal reproduction.
