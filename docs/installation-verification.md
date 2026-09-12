# Validation

The v1.0.0 baseline was verified with Codex CLI 0.154.0 on macOS on 2026-09-11.
Native app-server startup accepted the installed configuration with
`--strict-config`. Local prompt rendering discovered global guidance, this
repository's project instructions, and installed workflow/platform skills.

For v1.0.1 on 2026-09-12, native `codex debug prompt-input` inspection in an empty
temporary directory confirmed discovery of the automatic-onboarding instructions
and updated skill description without a profile. This verifies loaded context,
not that every model task will follow the workflow. Structural validation, skill
validation, and all 18 behavioral tests passed locally.

The [adversarial onboarding fixture](../tests/fixtures/onboarding/README.md) provides
inputs and evaluation criteria for checking whether repository text is promoted
into persistent guidance. It is a manual model evaluation, not one of the 18
deterministic tests; those tests do not establish prompt-injection resistance.

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
