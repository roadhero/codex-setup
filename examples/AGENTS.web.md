# Example: task-board web service

Fictional TypeScript service with a browser client. These commands describe an
example repository, not this configuration kit; replace them with verified facts.

## Layout and architecture

`apps/api` owns HTTP validation/authentication and calls domain services.
`apps/web` owns UI behavior. PostgreSQL persistence stays behind repository APIs.
Tenant authorization is checked server-side for every task-board operation.

## Commands

The example uses pnpm and scripts defined in its package.json:

```sh
pnpm install --frozen-lockfile
pnpm format:check
pnpm lint
pnpm typecheck
pnpm test
pnpm build
```

Integration tests require a disposable PostgreSQL service and a test DATABASE_URL.
Never run fixtures against production. Use the engineering-web skill and inspect
loading, empty, error, and keyboard interaction states when UI behavior changes.

## Delivery

package.json is the version source. Required CI matches the commands above plus
integration checks. Releases are reviewed before package/container publishing.
