# CI/CD Pipeline Blueprint (Technology-Neutral)

This is a pipeline design checklist, not a drop-in executable workflow. USF must generate provider- and stack-specific pipeline configuration only after the repository, build tooling, distribution target, and trust boundaries are known.

## Pull request pipeline
- [ ] Checkout a pinned/verified source revision.
- [ ] Validate work-item links and required documentation.
- [ ] Install dependencies using lockfiles and trusted registries.
- [ ] Run formatter/linter/type checks.
- [ ] Run secret, dependency, license, and static security checks as applicable.
- [ ] Build and run unit tests.
- [ ] Run integration/contract/UI tests appropriate to changed areas.
- [ ] Produce test, coverage, and scan reports.
- [ ] Enforce branch protection and independent review.
- [ ] Publish a concise pass/fail summary linked to the PR and work items.

## Main-branch pipeline
- [ ] Repeat required verification on the exact merged commit.
- [ ] Build an immutable versioned artifact.
- [ ] Record commit, toolchain, dependency state, build ID, and artifact digest.
- [ ] Attach provenance/attestation when supported.
- [ ] Publish to a controlled artifact store.
- [ ] Deploy to a safe environment or create a release candidate.
- [ ] Run smoke and environment-specific checks.
- [ ] Require protected-environment approval where risk policy demands it.

## Release pipeline
- [ ] Promote the same verified artifact.
- [ ] Verify release record and all release gates.
- [ ] Apply least-privilege deployment identity.
- [ ] Deploy progressively where supported.
- [ ] Verify health and critical user journeys.
- [ ] Stop promotion and roll back/forward if defined thresholds fail.
- [ ] Publish release notes and deployment result.
- [ ] Link operational telemetry and any incidents to the release.

## Tailoring by product form factor
- **Native desktop/mobile:** build per target platform; test signing, notarization/store packaging, update mechanism, migration, and supported OS/device matrix as relevant.
- **Web/API/service:** validate deployment configuration, migrations, health checks, secrets, network boundaries, and rollback.
- **CLI/library/SDK:** validate supported OS/runtime matrix, package metadata, API compatibility, signatures/checksums, and registry publication.
- **Local-first/offline software:** verify offline behavior, local data safety, update/recovery path, and telemetry/privacy constraints.

## Security constraints
Never expose production secrets to untrusted code or untrusted pull requests. Do not deploy production from an unreviewed branch. Limit artifact/log access. Scope dynamic security tests to authorized environments. A pipeline passing its checks does not establish that the product is free of vulnerabilities.
