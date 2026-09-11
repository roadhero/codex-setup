# Security policy

The latest published release is the supported version. Security fixes are released
as patches; older releases do not have a separate maintenance branch.

Report vulnerabilities privately through
[GitHub security advisories](https://github.com/roadhero/codex-setup/security/advisories/new).
Include the affected version, a minimal reproduction using synthetic data, expected
behavior, and observed impact. Do not include real credentials or private backups.
If private reporting is unavailable, open an issue requesting a private reporting
channel without publishing exploit details or secrets.

## Trust boundaries

Review configuration and scripts before installing. The installer does not create
trust for projects or hooks. User-level instructions and hooks are not managed
administrator policy. Runtime overrides can affect agent sandbox defaults.

The optional hook is advisory, checks tracked working-tree whitespace only, and is
not a secret scanner or a universal interception boundary. Use repository branch
protection, required checks, and a dedicated secret scanner where appropriate.

Backups may contain pre-existing private configuration. They are stored outside
the repository with restrictive file permissions. Restore only trusted manifests:
they contain absolute write destinations. Restore checks installed-file hashes
before replacing files, but a maliciously edited manifest is not trusted input.

Release SHA256SUMS detects accidental archive corruption; it is not an independent
signature or proof of publisher identity. Obtain archives and checksums from the
same authenticated project release page.
