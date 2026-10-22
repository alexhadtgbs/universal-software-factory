# Documentation and Evidence Standard

## Purpose
USF treats documentation as part of the product and engineering work—not as a cleanup task performed after implementation. Every material activity must leave enough durable, reviewable evidence for another qualified person to understand what changed, why it changed, how it was validated, and what remains unresolved.

## Operating rules
1. **Record work as it happens.** Update the relevant artifact in the same task or pull request. Do not reconstruct the project history from memory at the end.
2. **Link, do not duplicate.** Use stable IDs and links between goals, requirements, decisions, backlog items, pull requests, commits, tests, defects, security findings, releases, and incidents.
3. **Record decisions and rationale.** Document alternatives considered, constraints, evidence, trade-offs, approver, date, and reconsideration triggers for material decisions.
4. **Make claims auditable.** “Tested”, “secure”, “accessible”, “done”, and “ready” require evidence and a stated scope. Distinguish observed facts from assumptions, estimates, and recommendations.
5. **Keep records current.** Mark superseded decisions, outdated documents, and unresolved questions explicitly; do not silently delete history.
6. **Automate consistency checks.** CI should check required files, links/IDs where practical, formatting, generated artifacts, and policy gates. Automation supplements human review.
7. **Protect sensitive information.** Never place credentials, tokens, private keys, personal data, or exploitable secret material in logs, issues, screenshots, or committed docs. Redact safely and follow the incident process if a secret is exposed.
8. **Document exceptions.** Every waived gate or deviation needs a rationale, named accountable approver, scope, compensating controls, expiry/review date, and remediation owner. Agents cannot approve their own material risk exceptions.
9. **Use lightweight, proportional records.** Tiny changes can use concise records; high-risk, regulated, security-sensitive, or externally visible changes need stronger evidence. Avoid ceremonial documents that do not aid a decision or operation.
10. **Preserve traceability across tools.** If work occurs in an IDE agent, issue tracker, Git provider, CI system, or release platform, link the authoritative record from the project’s index.

## Minimum record for every work item
- Unique work-item ID, title, owner, status, and priority.
- Parent epic/requirement and acceptance criteria.
- Relevant PDR/ADR/TDR IDs, or an explicit “none required” rationale.
- Implementation references: branch/PR/commit, changed areas, and migration/configuration impact.
- Validation evidence: test commands/jobs and results, test report links, and known gaps.
- Security/privacy/accessibility impact and reviews when applicable.
- Reviewer/approver, decision, date, and follow-up actions.
- Release/rollback/monitoring notes when the change can affect operation.

## Required lifecycle records
| Lifecycle stage | Minimum evidence |
|---|---|
| Discovery | Problem statement, target users, evidence sources, assumptions, constraints, open questions |
| PRD/backlog | Approved requirements, IDs, acceptance criteria, priorities, dependencies, traceability |
| Product form factor | Options, hard constraints, evaluation, rationale, PDR and approval |
| Architecture | Context and component views as needed, quality attributes, risks, ADRs, threat-model impact |
| Technology assessment | Candidate comparison, current sources, proof-of-concept results when needed, TDR |
| UX/UI | User flows, states, prototypes/specifications, accessibility notes, validation findings |
| Engineering planning | Tasks, estimates/uncertainty, dependencies, test strategy, deployment and rollback approach |
| Implementation | PR/commit, review, test evidence, dependency/configuration changes, docs updated |
| Verification | Automated and manual test reports, defects, coverage scope, accessibility/security evidence as relevant |
| Release | Version, changelog, included work IDs, build provenance, approvals, deployment result, rollback and monitoring |
| Operations | Monitoring/alerts, incident records, postmortems, follow-up work and reassessment triggers |

## Source of truth and retention
At project start, define where each record lives (repository, issue tracker, design system, CI provider, artifact registry, observability platform) and who owns it. Keep a repository index linking to external canonical records. Follow organizational retention, privacy, legal, and regulatory requirements; do not invent a universal retention period.

## Definition of documentation completeness
A work item is not complete if a material decision is undocumented, acceptance evidence is missing, traceability is broken, or operational instructions are stale. “Not applicable” is acceptable when accompanied by a brief reason.
