# Design decisions

## Keep personal and project context separate

Global guidance contains durable preferences. A project's commands, supported
platforms, versions, and delivery rules live in its AGENTS.md. The installer
never copies this repository's own project context into personal guidance.

## Use native extension surfaces

Instructions use AGENTS.md discovery, agent roles use standalone TOML, skills use
SKILL.md, profiles use separate configuration files, and lifecycle hooks use the
native event contract. No hidden marker claims to control prompt caching.

## Preserve user configuration

Installation adds missing configuration keys and leaves existing tables intact.
It does not rewrite a user's TOML, replace MCP connections, copy credentials,
change Git identity, or grant trust. Customized assets cause a visible conflict.
Each update has a private backup; restore refuses post-install edits.

## Be precise about enforcement

Read-only agents set a sandbox default, while parent runtime settings and managed
policy retain their precedence. The optional hook is advisory. Command rules
control execution outside the sandbox; they are not complete Git policy.
Mandatory repository checks belong in project CI and Git controls.

## Specialize without duplicating instructions

General roles share platform skills. Compute specialists cover build systems,
CUDA, numerics, memory, Python/native integration, parallelism, inference, and
workstation operations. Models and reasoning inherit from the calling session.
The setup does not presume a particular GPU, framework, or deployment service.

## Make distribution verifiable

VERSION is the release source of truth. Tags and release notes must agree.
Archives are generated from a clean committed Git tree, contain a single versioned
root, and have deterministic metadata and SHA-256 checksums. CI exercises packaging
and installation without touching a real user home.
