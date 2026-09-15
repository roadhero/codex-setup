# Release process

VERSION is the source of truth. A stable release needs matching CHANGELOG.md and
`docs/releases/vX.Y.Z.md` entries, with install/upgrade guidance and real validation.
Never include machine-specific reports, credentials, or private backup manifests.

1. Prepare and review the version, changelog, notes, and relevant documentation.
2. Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`.
3. Commit the complete change on a release branch and open a pull request against
   main. Review the diff and resolve relevant findings; require successful checks
   at the final PR revision before merging through the repository's normal policy.
4. Update the local main checkout to the merged commit and run
   `python3 scripts/release.py` for a local archive/checksum preview. Packaging
   refuses a dirty working tree. Confirm VERSION and notes still match the release.
5. After publication is authorized, create an annotated `vX.Y.Z` tag on that merged
   commit and push the tag. The release workflow runs the cross-platform gate,
   verifies tag/VERSION/HEAD parity, creates the archives, and publishes matching notes.
6. Verify the GitHub release target, assets, and downloaded checksums.

The workflow does not overwrite an existing release. If publishing failed after a
release was created, inspect its state and upload missing verified assets explicitly;
do not move a published tag or silently replace changed artifacts. Use a new patch
release for changed content.

Manual recovery after verifying a clean tagged checkout:

```sh
python3 scripts/release.py --tag v1.1.0
gh release create v1.1.0 --verify-tag \
  --title 'v1.1.0 — Codex engineering setup' \
  --notes-file docs/releases/v1.1.0.md \
  dist/codex-setup-v1.1.0.tar.gz dist/codex-setup-v1.1.0.zip dist/SHA256SUMS
```

Archives come from Git blobs at HEAD, not loose working files. File order, ownership,
timestamps, and compression inputs are normalized for repeatable output in the same
toolchain. SHA256SUMS covers both archives. Checksums are integrity checks, not
independent publisher signatures. GitHub's automatic source archives are separate
from these generated assets.
