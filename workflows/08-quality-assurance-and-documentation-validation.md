# Workflow 08 — Product Quality Assurance and Documentation Validation

## Objective
Independently verify that the product and its documentation meet acceptance criteria, that documented procedures work in practice, and that users can complete important tasks without relying on hidden knowledge.

## Phase 1: Establish the quality plan
During discovery/planning:
- Identify user audiences and skill levels.
- Identify supported platforms, configurations, environments, and distribution methods.
- Identify critical user journeys, quality attributes, and high-risk procedures.
- Build a requirements-to-test-to-documentation traceability matrix.
- Define the documentation inventory, owners, reviewers, and validation methods.
- Define risk-based test scope, entry/exit criteria, environments, data, and release-blocking defects.
- Identify what cannot be tested automatically and who will test it.

## Phase 2: Define measurable acceptance criteria
For each requirement/feature, define:
- Expected behavior and observable success signal.
- Negative/error cases and recovery expectations.
- Supported platform/configuration coverage.
- Applicable security, privacy, accessibility, performance, compatibility, and reliability checks.
- Required user documentation and operational/developer documentation.
- Evidence needed to mark the requirement verified.

Avoid vague criteria such as “works well” or “documentation is complete” without observable checks.

## Phase 3: Verify implementation
Use risk-appropriate layers:
- Static checks, linting, type checks, and dependency/license/security scanning.
- Unit, integration, contract, UI/end-to-end, and regression tests.
- Manual exploratory testing for usability and unexpected behavior.
- Accessibility checks, including keyboard and assistive-technology checks for critical flows where practical.
- Performance, compatibility, resilience, migration, backup/restore, and recovery tests where relevant.
- Authorized security review and testing under the security workflow.
Record the exact build/commit, environment, test data characteristics, commands/jobs, outcomes, defects, and limitations.

## Phase 4: Validate documentation in practice
For each required guide:
1. Verify its target product version and audience.
2. Review prerequisites, permissions, environment, and expected outcomes.
3. Start from a clean or reset environment suitable to the guide.
4. Have a reviewer who did not author the guide follow it exactly.
5. Execute commands and code/API examples when practical; verify links and references.
6. For visual instructions, compare screenshots/labels with the actual build and check alternative text.
7. Test troubleshooting steps against safe, reproducible failure cases where practical.
8. Capture a documentation test report and file defects for discrepancies.
9. Correct the source document and rerun failed steps.
10. Mark untestable procedures Not Verified/Blocked with reason and an owner—not Passed.

## Phase 5: AI agent reviewer protocol
The reviewer must:
- Use the designated tools and authorized test environment; disclose tool/platform limitations.
- Work from the same release candidate and documented prerequisites that a real user receives.
- Avoid relying on prior conversation context or private knowledge not available to the intended user.
- Follow procedures literally first. If a step fails, record the failure before attempting diagnosis.
- Distinguish product defect, documentation defect, environment issue, and inconclusive test.
- Preserve reproducible evidence while redacting secrets and personal data.
- Verify fixes on a new run or reset state.
- Never claim to have executed commands, opened UI, tested a platform, or verified a link unless that action actually occurred.
- Never bypass authorization, release gates, or safety controls to make the test pass.

## Phase 6: Defect triage
Each defect includes:
- Unique ID, summary, severity/priority, affected version, and reproduction steps.
- Expected versus actual behavior.
- Requirement/documentation references.
- Evidence, environment, and reproducibility.
- Impact and workaround, if safe.
- Owner, target date, fix reference, and retest result.

Treat documentation defects that block installation, core tasks, safe data handling, recovery, security, or correct operation as potentially release-blocking. Severity depends on user impact and risk, not whether the defect is in prose or code.

## Phase 7: Exit criteria and release recommendation
The QA reviewer issues one of:
- **Pass:** applicable acceptance criteria met with evidence.
- **Pass with documented limitations:** only when policy permits and limitations are explicit, owned, and non-blocking.
- **Fail:** a release-blocking defect or missing evidence remains.
- **Blocked / Not Verified:** environment, permission, hardware, tool, or access constraints prevent a valid conclusion.

Before release, ensure:
- Requirements and critical journeys map to test results.
- Documentation inventory is complete or justified exceptions are approved.
- Critical guides have passed independent, clean-environment walkthroughs.
- Known defects and gaps have documented dispositions.
- Security, privacy, accessibility, and release gates are satisfied as applicable.
- Release record links QA report, documentation validation report, CI artifacts, and approvals.

## Phase 8: Post-release feedback
Monitor support questions, failed onboarding, task failures, crashes/errors, incidents, and documentation feedback. Convert recurring issues into product or documentation improvements. Revalidate affected documentation after fixes and meaningful behavior changes.
