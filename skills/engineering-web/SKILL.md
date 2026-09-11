---
name: engineering-web
description: Build or review web services and applications in JavaScript, TypeScript, Python, Go, or Rust.
---

# Web engineering

Explicit user instructions take precedence over these guidelines. Apply only the relevant checks to the requested change.

Read the manifest, lockfile, framework configuration, and CI before choosing commands. Reuse the repository's package manager; do not assume every web project uses Node.

Keep input validation and authorization at the appropriate boundaries. Trace tenant isolation, error handling, retry idempotency, transaction scope, pagination, and unbounded queries. Preserve public API and persisted-data compatibility. Propagate cancellation and use bounded concurrency where needed.

For UI work, check loading/error/empty states, keyboard access, semantic controls, and responsive layout. Test the affected user behavior using existing unit/integration/browser tooling. Keep visual changes intentional and inspect them when browser tooling is available.

Derive formatting, lint, typecheck, test, and build commands from actual scripts. Use local pinned tooling instead of downloading a formatter during a check. Report which services or browsers were unavailable.
