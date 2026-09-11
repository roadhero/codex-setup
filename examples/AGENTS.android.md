# Example: offline Android notebook

Fictional Kotlin/Compose application with an `app` Gradle module and Room storage.
Commands depend on these example modules/plugins and must be verified before use.

## Architecture

ViewModels own screen state; UI owns navigation/system interactions. Coroutines
are lifecycle-aware and propagate cancellation. Room migrations retain existing
notes. Use the engineering-android skill for platform-specific checks.

## Commands

```sh
./gradlew :app:testDebugUnitTest :app:lintDebug :app:assembleDebug
./gradlew :app:compileReleaseKotlin :app:assembleDebugAndroidTest
```

Instrumented tests require a configured emulator or device. Test supported schema
upgrades and release-variant behavior. Record actual SDK/JDK/Gradle versions from
the wrapper, version catalog, manifest, and CI instead of assuming defaults.

## Delivery

Read versionCode/versionName from the existing Gradle configuration. Signed
release artifacts require the team's credential store and physical-device smoke
checks; do not copy keystores into the repository or publish from a prep request.
