# Workflow: Security Review and Ethical Hacking

## Purpose
Find, explain, prioritize, remediate, and retest security weaknesses using authorized, defensive security review. This workflow is mandatory and risk-based; the depth of testing scales with the assets, exposure, and consequences.

## Inputs
- Product brief, PRD, architecture and technology decisions
- Data classification, trust boundaries, deployment model, threat assumptions
- Source code, dependency manifests, build configuration, infrastructure configuration, and test environment as available
- Written scope and authorization for active testing
- Prior findings, incidents, exceptions, and remediation history

## 1. Establish scope and authority
- Identify the system owner, assets, environments, accounts, allowed test methods, excluded systems, time window, and stop conditions.
- Confirm authorization before active testing. If unclear, limit work to passive review and request clarification.
- Prefer isolated environments and synthetic data. Never use production data unnecessarily.
- Record assumptions and limitations.

## 2. Build the threat model
- Identify sensitive data, credentials, keys, intellectual property, user safety, and critical operations.
- Map entry points, trust boundaries, privileged operations, external integrations, update paths, and supply-chain dependencies.
- Consider attacker capabilities and abuse cases, including malicious or compromised dependencies and prompt/content injection where AI features or tool-using agents exist.
- Rank threats by plausible exploitability and impact.
- Define security requirements and testable acceptance criteria.

## 3. Review design and architecture
Check authentication, authorization, session/token lifecycle, least privilege, data flow, encryption, key management, tenant/user isolation where applicable, safe file/process/network access, logging, backups, updates, recovery, and failure modes.
Review whether security depends on client-side checks alone or other assumptions that an attacker can bypass. Record design findings in the relevant PDR/ADR/TDR and assign owners.

## 4. Inspect implementation and supply chain
Use suitable methods available for the stack:
- manual source and configuration review;
- static analysis and secure coding checks;
- dependency and known-vulnerability scanning;
- secret scanning and repository history checks where authorized;
- license and provenance review;
- infrastructure/build/update configuration review;
- fuzzing or targeted tests for parsers, input boundaries, and complex protocols where proportionate.

Prioritize likely attack paths over checklist completion. Avoid exposing secret values in logs or reports.

## 5. Perform authorized dynamic testing
When in scope and safe, test authentication and authorization boundaries, input validation, session handling, file handling, API behavior, data leakage, rate limits, and relevant abuse cases. Use controlled test identities and non-production data. Do not expand scope or perform disruptive exploitation without explicit authorization.

## 6. Record findings
Create a finding for each distinct issue. Include:
- unique ID and date;
- affected component/version and environment;
- concise title and description;
- preconditions and attack path;
- reproducible, minimal evidence that avoids secrets or personal data;
- severity and rationale, including likelihood/exploitability and impact;
- remediation guidance and owner;
- retest steps and status;
- disclosure/escalation requirements if applicable.

Use a recognized severity framework where appropriate (for example, CVSS) but explain contextual adjustments. Do not inflate or downplay severity to meet release targets.

## 7. Remediate and retest
- Assign an owner and target date.
- Fix root causes where practical, not just symptoms.
- Add regression tests for the vulnerability and relevant neighboring cases.
- Retest the fix independently for Critical/High findings where practical.
- Reopen findings if the fix is incomplete or creates a new weakness.
- Document accepted residual risk and compensating controls.

## 8. Make the release recommendation
The reviewer provides a clear recommendation: **Block**, **Conditional**, or **Ready from the reviewed scope**, with evidence and limitations.
- Critical/High findings block release by default unless an authorized, documented exception exists.
- Medium/Low findings require documented disposition, owner, and target date or acceptance rationale.
- Required security tests must not be marked complete when they were skipped or inconclusive.
- The accountable human owner—not the AI agent alone—accepts material residual risk.

## 9. Maintain security over time
Track dependency advisories, patch status, security incidents, secrets rotation, supported versions, and material changes to trust boundaries. Repeat the review after significant architectural changes, new external integrations, privilege changes, major dependency updates, or a security incident.

## Outputs
- Threat model and security acceptance criteria
- Security review scope and evidence
- Prioritized findings register
- Fix and retest evidence
- Release security recommendation and residual-risk approvals
- Reassessment triggers

## Exit criteria
- Scope and authorization are recorded.
- Threat model and relevant attack surfaces have been reviewed.
- Risk-appropriate checks have been run, with limitations disclosed.
- Findings have owners, dispositions, and retest status.
- Release recommendation and any residual-risk approvals are recorded.
