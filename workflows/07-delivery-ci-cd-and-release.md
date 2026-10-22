# Workflow 07 — Delivery, CI/CD, Release, and Operations

## Objective
Deliver changes through a repeatable, observable, secure pipeline with traceable evidence from requirement to production. CI/CD is the default delivery model where the project's risk, platform, and operating constraints support it. For products that cannot deploy continuously (for example, native desktop distribution), automate build, verification, signing/notarization where applicable, packaging, release candidate generation, and staged rollout as appropriate.

## 1. Define delivery strategy before implementation
For each deployable component, document:
- Environments and their purpose (local, CI, ephemeral review, test/staging, production, or platform-specific equivalents).
- Branching and merge strategy, review requirements, versioning, artifact naming, and release cadence.
- Pipeline triggers and required checks.
- Secrets and identity model; prefer short-lived, least-privilege credentials and managed secret stores.
- Test data policy, dependency/source controls, artifact storage, signing, provenance, and retention.
- Deployment method, feature flags where useful, health checks, rollback/roll-forward plan, and responsible owner.
- Monitoring, alerting, support ownership, and incident escalation.
Record significant choices in ADRs and link them from the engineering plan.

## 2. Standard pipeline stages
Adapt these stages to the selected stack and hosting/distribution model; do not assume a particular language, framework, cloud, or Git provider.

1. **Change intake:** validate issue/requirement IDs, scope, and acceptance criteria.
2. **Static checks:** formatting, linting, type checking, policy checks, secret scanning, and static analysis where supported.
3. **Dependency and supply-chain checks:** lockfile consistency, dependency vulnerability/license review, provenance controls, and permitted-source checks as appropriate.
4. **Build/package:** reproducible or repeatable build where practical; record toolchain and artifact identity.
5. **Unit tests:** run fast deterministic tests and publish machine-readable results.
6. **Integration/contract tests:** validate interfaces and dependency boundaries.
7. **UI/end-to-end tests:** cover critical user journeys and important state/error paths where applicable.
8. **Security checks:** threat-model-linked checks, SAST/SCA/secrets/IaC/container scans as applicable, plus authorized dynamic testing in a scoped environment. A clean scanner result is not proof of security.
9. **Quality gates:** enforce project-specific thresholds and release-blocking findings; publish exceptions with approver and expiry.
10. **Artifact publication:** store immutable build artifacts and reports; attach version, commit, build ID, and provenance/attestation when available.
11. **Pre-release validation:** deploy to a safe environment or prepare a signed release candidate; run smoke, migration, accessibility, performance, privacy, and manual checks as required by risk.
12. **Approval and release:** require human approval for production or other high-impact actions according to the project's risk policy. Automated promotion is permitted only after explicit policy design.
13. **Post-release verification:** verify health, key journeys, crash/error rates, security signals, and service-level indicators; record outcome.
14. **Rollback or recovery:** execute the rehearsed rollback/roll-forward procedure if release criteria fail. Preserve evidence and open follow-up work.

## 3. Pull request / change review contract
Every material change must include:
- What and why, linked work-item IDs, and acceptance criteria.
- Risk/impact assessment including data migrations, compatibility, privacy, security, UX/accessibility, and operations.
- Tests added/changed and actual CI results (not just “tests pass”).
- Documentation, configuration, observability, and runbook updates.
- Deployment and rollback considerations.
- Screenshots/video or design links for material UI changes when helpful, without exposing sensitive data.
- Known limitations and follow-up items.

Required checks must pass before merge. Any exception follows the documented exception policy. Reviews must be performed by an appropriate reviewer; authors/agents must not self-approve changes where independent approval is required.

## 4. Release readiness gate
Do not release until the release record is complete and:
- Scope, version, change log, and included work items are known.
- Required CI jobs and manual acceptance checks have passed.
- Critical/High security findings are resolved or handled only through a formally authorized exception permitted by the security policy.
- Data migration, backup/recovery, compatibility, privacy, accessibility, and operational impacts have been assessed as relevant.
- Release artifact and provenance are identifiable.
- Rollback/roll-forward plan and post-release checks are ready.
- Required human approvals are recorded.
- Open Medium/Low findings and known issues have an owner, disposition, and target date or rationale.
- Support/operations notes and user-facing release notes are ready where applicable.

## 5. Production deployment and operations
- Prefer progressive delivery (canary, phased rollout, rings, feature flags) when supported and proportionate.
- Use health checks and stop/rollback thresholds tied to observable signals.
- Do not log secrets or sensitive user content. Limit access to logs, traces, artifacts, and production data.
- Verify migrations and backward compatibility; use expand/contract patterns where appropriate.
- Record deployment start/end, artifact digest/version, environment, actor/automation identity, result, approvals, and any intervention.
- Link alerts, incidents, customer impact, and remediation items to the release.
- Define ownership and operational targets appropriate to the product; do not invent SLOs without product/service context.

## 6. Failure, incident, and learning loop
When a pipeline or release fails:
1. Stop unsafe promotion; preserve logs and artifact identifiers.
2. Communicate status and assign an owner.
3. Restore service safely where needed.
4. Record the timeline, impact, detection, response, root/contributing factors, and what went well/poorly.
5. Create prioritized, owned corrective actions with due dates.
6. Feed lessons into tests, architecture, threat models, runbooks, monitoring, and planning.
Use blameless analysis focused on system improvements, not blame.

## 7. CI/CD implementation rules for USF
- Keep pipeline definitions in version control and review them like production code.
- Provide a minimal pipeline early, then extend it as risks and requirements become clear.
- Store test outputs, coverage, scan results, build metadata, and deployment logs as CI artifacts with appropriate access controls.
- Use environment protection and least privilege; untrusted pull requests must not receive production secrets.
- Pin or constrain critical actions/tools according to platform best practices and monitor updates.
- Separate build from deployment where feasible; promote the same immutable artifact rather than rebuilding different binaries per environment.
- Ensure pipeline failures are visible, actionable, and linked to work items.
- Define and test recovery paths; backups that have never been restored are not proven recovery.
- Tailor gates to product risk and platform realities. Do not impose meaningless universal coverage percentages or require cloud deployment for a local desktop application.

## 8. Required output
Maintain a delivery strategy, pipeline map, required-check list, environment/configuration inventory, release record for every release candidate, operational runbook, and incident/postmortem records when incidents occur. Use `templates/release-record.md`, `templates/test-plan-and-report.md`, and `templates/incident-postmortem.md`.
