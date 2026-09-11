---
name: engineering-android
description: Build or review Android Kotlin, Compose, Gradle, and persistence changes.
---

# Android engineering

Explicit user instructions take precedence over these guidelines. Apply only the relevant checks to the requested change.

Read the Gradle wrapper, module graph, version catalog, manifest, and existing architecture. Use the actual module and variant names; do not assume Hilt, Room, or Roborazzi are installed.

Keep UI state ownership explicit and lifecycle-aware. Propagate coroutine cancellation, handle upstream flow failures, avoid blocking the main thread, and test navigation/effect delivery across lifecycle changes. Match existing dependency injection boundaries.

When persistence changes, test migration from supported old schemas. Check debug-only dependencies against release compilation. For visual changes, use existing snapshot/UI tests with deterministic clocks and fixtures; update goldens only for intentional differences.

Record the actual unit/lint/build commands and relevant instrumented or physical-device checks. For releases verify versionCode/versionName from their real source, signing configuration without exposing keys, shrinker behavior, and target-device startup. Do not invent SDK versions or submit store releases from a preparation request.
