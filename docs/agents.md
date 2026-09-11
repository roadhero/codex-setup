# Native agents

These roles use the current standalone TOML format. Model and reasoning inherit
from the parent; no model or reasoning overrides are imposed.
Read-only roles set `sandbox_mode = "read-only"`. Runtime permission overrides
can still take precedence. QA/debugging inherit workspace permissions for test
artifacts; their instructions limit changes to the assigned task.

- `architect`: Plan substantial changes from repository evidence.
- `senior-swe`: Implement scoped changes and verify the outcome.
- `code-reviewer`: Review a concrete diff for actionable defects.
- `qa`: Verify changes with repository tests and realistic error cases.
- `security-reviewer`: Investigate a requested security review or a concrete security concern.
- `performance-engineer`: Investigate measured latency, throughput, or memory problems.
- `db-migration-specialist`: Design or implement explicitly requested data migrations.
- `debugger`: Reproduce failures and isolate root causes.
- `devops-sre`: Prepare CI, infrastructure, and operational changes.
- `docs-reconciler`: Find drift between documentation and implemented behavior.
- `release-engineer`: Prepare version changes, release notes, and release validation.
- `product-designer`: Specify or evaluate product flows and interaction behavior.
- `tech-writer`: Write accurate product and engineering documentation.
- `technical-program-manager`: Turn a delivery goal into a scoped sequence with dependencies.
- `scrum-master`: Assess an explicitly requested team cadence or delivery process.

Use a direct delegation request, such as: “Ask architect to inspect the design
and code-reviewer to review the diff; wait for both.” Agent availability alone
does not require delegation. Keep ownership explicit for concurrent writers.

Platform specialization is supplied by four focused skills and project context
rather than duplicate Android/iOS agents. Compute skills retain numerical, GPU,
build, inference-boundary, and profiling concerns without assuming a workstation.

## Compute specialists

- `build-engineer`: Diagnose and implement native build, linking, toolchain, and packaging changes.
- `cuda-engineer`: Design or optimize CUDA kernels with correctness evidence.
- `inference-engineer`: Investigate model-serving memory, latency, and throughput constraints.
- `memory-debugger`: Isolate native memory corruption, leaks, races, and device memory faults.
- `numerics-engineer`: Review numerical accuracy, precision changes, and reproducibility.
- `parallelism-engineer`: Design or diagnose CPU concurrency, multiprocessing, and NUMA behavior.
- `python-engineer`: Implement numerical Python and Python/native integration changes.
- `systems-engineer`: Prepare compute-host configuration and operational diagnostics.
