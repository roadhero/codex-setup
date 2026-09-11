# Example: Swift package with an iOS app

Fictional project with a domain Swift package and a Notebook app scheme. Replace
scheme/workspace names and destinations with values from the actual repository.

## Architecture

The domain package is independent of UI. App state has explicit ownership and
actor isolation. Persistence changes include old-data validation. Use the
engineering-ios skill and the existing Swift concurrency language mode.

## Commands

```sh
swift build
swift test
xcodebuild -list
xcodebuild -showdestinations -scheme Notebook
```

Choose an available simulator destination, then run the repository's documented
xcodebuild test command. Simulator checks do not prove physical-device, signing,
archive/export, entitlement, or store-submission behavior.

## Delivery

Marketing/build versions follow the Xcode project's existing source. Signing uses
configured team credentials. Archive/export and device verification are explicit
release tasks, with upload only when authorized.
