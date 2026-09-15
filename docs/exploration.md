# Repository exploration

Use `repo-explorer` for a concrete location or factual tracing question that needs
several searches and file reads: find request validation, map configuration loading,
or identify callers of a public function. The utility reads in its own context and
returns a short evidence report to the caller. It is a native custom agent under
`agents/repo-explorer.toml`; the installer places it under Codex home.

## Delegation and result

Global guidance requests one bounded delegation when the lookup is broad and can
run independently alongside useful local work. Simple known-file lookups stay in
the current thread. Higher-priority restrictions and requests not to delegate take
precedence. If the utility is unavailable or cannot start, continue locally.

You can request it explicitly:

> Ask repo-explorer to locate configuration loading and its direct callers under
> src/. Return the relevant files and lines, the load order, and any coverage gaps.
> While it searches, inspect the existing configuration tests.

Give the agent the question, repository, search boundaries, and any exclusions.
Expect a concise answer, verified file:line references, and a coverage statement.
The caller checks decisive evidence before changing code or making a judgment.
Do not duplicate the entire scan or request raw file dumps. An empty result from a
limited search is not proof that the code does not exist.

## Model and permissions

The utility uses `gpt-5.6-terra` with `model_reasoning_effort = "low"`. OpenAI's
[subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents)
recommends Terra for efficient read-heavy work and supports model/effort settings in
native agent files. The other 23 agents inherit the caller's model and effort.

Delegation moves tool-reading work into the selected agent's session; it does not
route an individual `rg` command to a different model. Additional threads consume
tokens, and a cheaper worker does not guarantee a cheaper overall task. Use a
bounded question, a concise result, and direct local reads for simple lookups.

The read-only sandbox is a default, not an absolute tool allowlist: live runtime
permission overrides can take precedence, and external tools have their own access
controls. The utility's instructions prohibit file/service mutations, executing
project scripts, tests/builds, dependency installation, and credential inspection.
It follows valid project instructions while treating other repository text as data.

Model availability depends on the account and client. If Terra is unavailable,
continue the lookup in the main agent. To customize persistently, edit the installed
agent's `model` and `model_reasoning_effort` together. Remove both to inherit model
selection from normal spawn/default/parent configuration. A task prompt cannot
override a model pinned inside a custom agent file. For a project-specific variant,
copy the complete agent file into `.codex/agents/` and customize it under project
trust. Keep all required agent fields and the inspection-only contract. Customized
assets trigger the installer's normal conflict protection on later installations.
