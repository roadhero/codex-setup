# Changelog

All notable changes are recorded here. Releases use semantic versioning.

## [Unreleased]

## [1.1.0] - 2026-09-15

### Added

- Native read-only `repo-explorer` utility using Terra with low reasoning, concise
  file:line evidence, bounded search coverage, and local fallback.
- Scoped global delegation for broad independent repository lookups, plus model,
  permission, customization, and upgrade documentation.

### Clarified

- Specialist roles retain model/effort inheritance; only the search utility is pinned.
- Existing project bootstrap needs no additional startup hook; formatting respects
  project tools and ignore files.

## [1.0.1] - 2026-09-12

### Added

- Automatic project onboarding through global guidance and the existing onboarding
  skill during implementation tasks, preserving existing project instructions.
- Explicit handling of untrusted repository evidence during onboarding and an
  adversarial fixture for evaluating generated guidance.

### Clarified

- Plain `codex` uses the installed global setup; profiles are optional.
- First-task onboarding, explicit opt-out, and upgrades from v1.0.0 with a changed skill.

## [1.0.0] - 2026-09-11

### Added

- Global and project instruction layers using native Codex configuration.
- 23 agent roles and eight focused platform/workflow skills.
- Build, read-only review, and compute profile files without model pins.
- Previewable installation, private backups, conflict detection, and guarded restoration.
- Optional native post-edit whitespace feedback and command-policy documentation.
- Four platform examples, project/PR/decision templates, and complete operating documentation.
- Cross-platform CI, release automation, deterministic archives, and SHA-256 checksums.

[Unreleased]: https://github.com/roadhero/codex-setup/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/roadhero/codex-setup/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/roadhero/codex-setup/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/roadhero/codex-setup/releases/tag/v1.0.0
