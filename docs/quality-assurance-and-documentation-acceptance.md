# Quality Assurance and Documentation Acceptance Standard

## Purpose
Every product delivered by USF must be understandable, usable, testable, operable, and supportable by its intended users and maintainers. Documentation is an acceptance deliverable, not optional polish. A reviewer must verify documentation against the actual product and demonstrate that its instructions work in a clean, representative environment.

## Core principles
1. **Documentation follows the product truth.** Instructions must match the shipped version, supported platforms, UI, configuration, permissions, and behavior.
2. **Test the instructions, not just the prose.** A qualified reviewer who did not author the documentation must follow it step by step wherever practical.
3. **Test from a clean starting point.** Use a clean machine/VM/container/profile or a reset test account appropriate to the product. Do not rely on undocumented local state, cached credentials, developer-only tools, or unstated assumptions.
4. **Write for the intended audience.** Separate end-user, administrator/operator, developer/contributor, and API/reference documentation. Explain prerequisites and terminology.
5. **Make success observable.** Each procedure states expected outcomes and how the user can tell whether it succeeded.
6. **Cover failure and recovery.** Include common errors, troubleshooting, recovery, backup/restore where relevant, safe retry behavior, and support/escalation paths.
7. **Be accessible and maintainable.** Use clear structure, descriptive headings, readable examples, accessible images/diagrams, versioning, and links. Avoid relying on color alone or screenshots as the only explanation.
8. **No fabricated proof.** Mark unverified steps and known limitations explicitly. Do not claim a guide was tested unless there is a dated test record with environment and results.
9. **Proportionate rigor.** A simple tool may need a concise guide; a complex or safety-/security-critical product needs deeper task-based, operational, and recovery documentation. All products must meet the applicable checklist.

## Documentation set: minimum required by product type
Create and tailor a documentation plan during discovery. Explain which documents are required, not applicable, or intentionally deferred and why.

### End-user documentation
- Product purpose, intended users, supported platforms/versions, and limitations.
- Getting started: prerequisites, installation or access, first-run setup, and first successful task.
- Task-based guides for every important user journey and major feature.
- UI/navigation and key concepts, including permissions and account/data handling where relevant.
- Configuration and customization.
- Troubleshooting: recognizable symptoms, likely causes, safe diagnostic steps, remedies, and when to seek help.
- FAQ/glossary where it materially helps the audience.
- Accessibility and supported input methods where relevant.
- Upgrade/update, export/import, data backup/restore, uninstall/removal, and data deletion where applicable.
- Clear support/contact/escalation route or a statement of support limitations.

### Administrator/operator documentation
- Deployment/distribution and environment prerequisites.
- Configuration reference and secret-management guidance (never publish secret values).
- Identity, permissions, access control, network/data boundaries, and audit logging.
- Monitoring, health checks, alerts, maintenance, backup/restore, recovery, upgrades, rollback, and incident response.
- Capacity, limits, dependencies, service ownership, support boundaries, and known operational risks, as applicable.

### Developer/contributor documentation
- Architecture overview, component boundaries, key flows, and decision records.
- Supported toolchain and exact setup steps for a clean checkout.
- Build, test, lint, static analysis, and local run commands with expected outcomes.
- Repository structure, contribution process, code review, branching/versioning, and Definition of Done.
- CI/CD pipeline, environments, release procedure, artifact provenance, and rollback/recovery.
- Configuration, migrations, dependency update process, generated files, and troubleshooting.
- How to add/change features safely, including test and documentation expectations.

### API/SDK/CLI/library documentation (when applicable)
- Complete reference for public interfaces, arguments, flags, types, responses, errors, exit codes, compatibility, and deprecations.
- Authentication/authorization and rate/usage limits, if relevant.
- Copyable examples that are tested against the supported version.
- Installation/package integrity and version support.
- Migration and compatibility guidance.

## Documentation inventory and ownership
Maintain a documentation index with:
- Document title and audience.
- Product/version or scope covered.
- Owner and last verified date.
- Canonical location.
- Required/optional/not-applicable status with rationale.
- Automated and manual validation method.
- Related requirements/features and test evidence.
- Known gaps and planned correction, owner, and due date.

Every major requirement and feature must link to relevant user guidance and, where relevant, operational/developer references. Avoid duplicated instructions: designate a canonical source and link to it.

## Documentation acceptance gate
Documentation is acceptable only when:
- Required document set is complete for the product type and audience.
- Steps match the current build and all prerequisites are explicit.
- Critical user tasks have clear step-by-step guidance and expected outcomes.
- Commands, configuration examples, code snippets, API examples, links, screenshots, and diagrams have been checked; examples are executed where practical.
- A non-author reviewer successfully follows critical instructions in a clean environment or records a concrete blocker.
- Error recovery, security/privacy cautions, data loss warnings, and permissions are clear where applicable.
- Terminology, version numbers, feature names, and UI labels are consistent with the product.
- Accessibility and readability have been reviewed.
- All known gaps are transparent and have owners; release-blocking gaps are fixed or handled by authorized exception.
- Documentation is versioned with the product or clearly identifies which versions it applies to.

A document that merely exists does not pass this gate. Its accuracy and practical usability must be demonstrated.

## AI reviewer capability standard
An AI agent reviewer should act as an independent acceptance tester, not assume the documentation is correct. For every testable documented capability:
1. Identify the claim/procedure and its prerequisites.
2. Map it to a requirement, feature, command/API/UI flow, or operational procedure.
3. Prepare a safe, representative test environment with least privilege and synthetic/non-sensitive data.
4. Follow the instructions exactly as written, without undocumented interventions.
5. Record actual actions, outputs, screenshots/log references where safe, and pass/fail/blocked status.
6. Compare observed behavior with documented expected outcomes.
7. Report ambiguity, missing prerequisites, stale instructions, undocumented behavior, security issues, and differences between documentation and implementation.
8. Re-run after correction and attach evidence.

The reviewer must not silently infer missing steps, patch the environment to make a guide work, or claim a capability works based only on code inspection. If the reviewer lacks a tool, permission, platform, account, or environment needed to test a claim, it must mark the claim **Not Verified** or **Blocked**, explain why, and request an appropriate test path. It must never fabricate execution results.

## Independence and risk
- The documentation author and acceptance reviewer should be different agents/people when practical for critical paths.
- The reviewer should receive the release candidate, documentation, and declared test setup—not undocumented author knowledge.
- Critical install, upgrade, data migration/export/restore, authentication/authorization, recovery, and core user journeys require direct verification appropriate to the product risk.
- Security-sensitive or destructive actions must be tested only with explicit authorization, scoped environments, and synthetic data.
- Human approval remains required where the product risk, policy, or release process calls for it.

## Release gate and ongoing maintenance
Documentation must be reviewed for every user-visible behavior, interface, configuration, supported-platform, security, or operational change. Release records must link the documentation acceptance report. Revalidate after significant UI changes, dependency/runtime changes, migrations, support-policy changes, and incidents. Remove or mark obsolete guidance instead of leaving conflicting instructions published.
