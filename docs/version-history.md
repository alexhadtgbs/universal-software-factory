# Version History

## 0.8.0 — Agentic delivery loop
- Added workflow 09: an executable spec → build → parallel review → approval-gate loop for approved backlog items, with a file-based artifact contract, `job.json` state schema, bounded rework, per-job isolation, and an escalation policy aligned with USF's human-approval and residual-risk rules.
- Added job spec, build report, review report, and approval decision templates.
- Added `scripts/validate_job.py` to check job folders against the contract.
- Added the Claude Code adapter (`adapters/claude-code/`): `/usf-loop` orchestrator, spec-writer, builder, security, code/QA, UX/UI, and documentation reviewers, approver, backlog, and dashboard.
- Brought the CLAUDE.md, AGENTS.md, Cursor, and generic adapters up to date with the security, UX/UI, evidence, and QA gates.
- Extended the Definition of Done for jobs delivered through the loop.

## 0.7.0 — Quality assurance and executable documentation validation
- Added a product-wide QA standard and documentation acceptance gate.
- Defined user, operator, developer, and API/reference documentation expectations.
- Added an independent reviewer protocol that tests documented procedures from clean/reset environments where practical.
- Added documentation inventory and validation report templates.
- Added explicit Pass / Pass with documented limitations / Fail / Blocked / Not Verified outcomes and anti-fabrication requirements for AI reviewers.
- Aligned version labels in README, SKILL.md, and VERSION; rewrote `scripts/validate.py` to check all release artifacts against `VERSION`.

## 0.6.0 — Continuous documentation and CI/CD
- Added a documentation/evidence standard requiring contemporaneous, traceable, auditable records across the lifecycle.
- Added delivery, CI/CD, release, operations, and incident-learning workflow.
- Added engineering activity, test plan/results, release, and incident postmortem templates.
- Added a technology-neutral pipeline blueprint tailored to native desktop, web/service, CLI/library, and local-first products.
- Clarified that CI/CD configuration must follow validated product and technology decisions rather than assume a specific provider or deployment model.

## 0.5.0 — UX/UI design excellence
- Added UX/UI design principles and a design/validation workflow.
- Added UX/UI design brief template.
- Established accessibility-first, platform-aware, evidence-driven design and purposeful innovation requirements.

## 0.4.0 — Security-first review
- Made security a mandatory lifecycle requirement.
- Added Security Reviewer / Ethical Hacker role and authorized security review workflow.
- Added security review report template and baseline checklist.
- Added release gates, finding retest requirements, AI-agent security checks, and human residual-risk acceptance.

## 0.3.0 — Technology stack assessment
- Added Technology Stack Advisor responsibilities and project-specific technology selection policy.
- Added technology stack assessment workflow, TDR template, and research standards.
- Added lifecycle reassessment triggers, evidence quality requirements, and proof-of-concept guidance.

## 0.2.0 — Product management and architecture decisions
- Added product management and product discovery workflow.
- Added explicit product-form-factor assessment distinct from system architecture selection.
- Added Product Decision Record and Architecture Decision Record templates.
- Added traceability from goals and requirements to tests.
- Added decision approval, uncertainty, and reassessment rules.
- Added provisional roadmap for the USF desktop application and optional future platform services.

## 0.1.0
- Portable core skill, generic workflows, templates, and adapters.
