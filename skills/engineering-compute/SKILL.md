---
name: engineering-compute
description: Build or review C++, CUDA, numerical Python, and CPU/GPU compute code.
---

# Compute engineering

Explicit user instructions take precedence over these guidelines. Apply only the relevant checks to the requested change.

Record actual CPU/GPU, OS, compiler, CUDA toolkit/driver, memory budget, precision, and workload. Derive workstation constraints from actual hardware. CUDA checks require a compatible NVIDIA host; macOS checks cannot establish GPU correctness.

For native code examine ownership/RAII, integer overflow, undefined behavior, ABI boundaries, error propagation, and sanitizer coverage. For device code examine bounds, launch/error checks, synchronization, stream lifetimes, transfers, and CPU/GPU equivalence.

For numerical changes specify tolerances and compare with a trusted reference, including edge values, reduction order, precision, and determinism. Separate numerical equivalence from bitwise reproducibility. For parallel Python examine GIL/native boundaries, multiprocessing start methods, copying, and oversubscription.

Derive CMake presets, build/test commands, Python environment commands, and GPU tooling from the project. Benchmark representative workloads before/after on the same hardware; report warmup and variability. Mark GPU, NUMA, or multi-device verification unavailable when the target hardware is absent.
