# Validation

The v1.0.0 baseline was verified with Codex CLI 0.154.0 on macOS on 2026-09-11.
Native app-server startup accepted the installed configuration with
`--strict-config`. Local prompt rendering discovered global guidance, this
repository's project instructions, and installed workflow/platform skills.

Automated tests exercise configuration preservation, installation idempotency,
backup/restoration, conflicting files, symlink refusal, instruction overrides,
write failures, documented hook output, release archives, and integrity checks.
Run the same suite locally:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

See the [CI runs](https://github.com/roadhero/codex-setup/actions/workflows/gate.yml)
for platform-specific results on each commit. Local validation is not a promise
that every future Codex version retains the same behavior.

No remote model task is needed for these tests. Hook fixture tests do not replace
reviewing/trusting a hook and checking it in an actual session. Third-party MCP
connectivity, account/model access, hosted-cloud setup, signing, and target-device
behavior are outside these tests. GPU validation requires a compatible GPU host.
