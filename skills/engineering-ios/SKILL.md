---
name: engineering-ios
description: Build or review Swift, SwiftUI, Xcode, and Apple-platform changes.
---

# Ios engineering

Explicit user instructions take precedence over these guidelines. Apply only the relevant checks to the requested change.

Inspect the workspace/project or Package.swift, supported deployment targets, schemes, dependency resolution, and CI. Discover simulator destinations before constructing xcodebuild commands.

Track state ownership, actor isolation, task cancellation, main-thread work, retain cycles, and persistence compatibility. Match the project's concurrency language mode; do not apply compiler-version assumptions from another project.

Use existing Swift testing or XCTest tooling for logic, snapshot/UI checks for relevant interfaces, and Instruments when investigating measured performance issues. Keep fixtures deterministic. Distinguish simulator verification from signing/device/App Store validation.

For release preparation identify the real marketing/build version source, bundle identity, entitlements, privacy manifest, signing strategy, and archive/export commands. Do not change signing identities or upload a build without applicable authorization.
