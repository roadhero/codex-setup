# Example: CPU reference with optional CUDA backend

Fictional CMake project with Python analysis tooling. The example defines `dev`
configure/build/test presets; verify actual presets before using these commands.

## Architecture

CPU reference calculations define numerical expectations. Native ownership uses
RAII; CUDA paths check bounds, launch errors, synchronization, and resource
lifetimes. Python/native boundaries document dtype, shape, ownership, and copying.
Use engineering-compute and the relevant compute specialist when requested.

## Commands

```sh
cmake --preset dev
cmake --build --preset dev
ctest --preset dev --output-on-failure
```

Record actual compiler, OS, CPU, GPU model, driver/toolkit, precision, and memory
budget. GPU tests require a compatible NVIDIA host. Do not describe CPU-only
macOS checks as CUDA validation. Record numerical tolerances and compare against
the reference implementation. Benchmarks report workload, warmup, and variability.

## Delivery

Version source is the top-level CMake project declaration. Test artifact ABI and
supported targets before packaging. Driver/system tuning is a separate authorized
operation with a recovery plan.
