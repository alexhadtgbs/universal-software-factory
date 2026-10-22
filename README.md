# Universal Software Factory (USF) — v0.8.0

USF is a portable, AI-assisted software production system. It combines product discovery, requirements, architecture decisions, engineering workflows, quality gates, and tool adapters. The long-term product direction is a native macOS workspace that can evolve into a broader platform; this is a roadmap, not a requirement imposed on every project USF helps build.

## Core principle

**USF MUST NOT prescribe a product form factor or software architecture before evaluating the product requirements, constraints, and viable alternatives.** The AI Product Manager and Solution Architect collaborate on a recommendation, document rationale and trade-offs, and identify decisions requiring user approval.

## Product management and architecture decisions (v0.2.0)

- Product Manager role and discovery-to-PRD workflow.
- Product-form-factor and architecture assessment as separate but related decisions.
- Solution Architect role and explicit architecture alternatives.
- Product Decision Record (PDR) and Architecture Decision Record (ADR) templates.
- Requirements-to-epics/stories/tasks/tests traceability guidance.
- Human approval and uncertainty rules for consequential decisions.
- A provisional roadmap for USF itself: native macOS first, modular local core, optional backend later, subject to validation.

## Technology stack assessment (v0.3.0)

- Technology Stack Advisor responsibilities and a project-specific technology selection policy.
- `workflows/04-technology-stack-assessment.md`, `templates/technology-decision-record.md`, and `docs/technology-research-standards.md`.
- Lifecycle reassessment triggers, evidence quality requirements, and proof-of-concept guidance.

## Quick start

1. Copy `skills/universal-software-factory/` into your preferred agent's skill/instructions location.
2. Add the appropriate adapter from `adapters/` to the project root.
3. For a new product, follow `workflows/01-product-discovery.md`, then `02-prd-and-backlog.md`, then `03-product-and-architecture-decisions.md`.
4. Validate the project outputs against `quality/definition-of-done.md`.

See `docs/` for the system overview and USF's provisional product roadmap. This package provides instructions and templates; it does not itself execute agents or build a macOS app.

## What's new in v0.4.0 — security-first review

- Makes security a mandatory lifecycle requirement rather than an optional final checklist.
- Adds the **Security Reviewer / Ethical Hacker** role, with independent challenge, threat modeling, authorized testing, finding triage, remediation verification, and release-gate authority.
- Adds `workflows/05-security-review-and-ethical-hacking.md`.
- Adds `templates/security-review-report.md` and `docs/security-baseline.md`.
- Defines explicit authorization boundaries for active testing and human approval for material residual-risk acceptance.
- Establishes a default release block for Critical/High findings unless a formally authorized exception is documented.
- Adds AI-agent-specific security concerns such as prompt injection, unsafe tool invocation, over-privileged agents, and accidental secret exposure.

Security reviews use authorized, scoped, defensive testing only. A clean scan is not proof that a system is secure.

## What's new in v0.5.0 — UX/UI design excellence

- Defines the UX/UI Designer as a product capability from discovery through post-implementation review.
- Adds `workflows/06-ux-ui-design-and-validation.md`.
- Adds `templates/ux-ui-design-brief.md` and `docs/ux-ui-design-principles.md`.
- Balances platform conventions and accessibility with purposeful, evidence-driven innovation.
- Requires validation of novel interactions and coverage of important UI states, including errors and recovery.


## Documentation, CI/CD, and operational evidence (v0.6.0)

USF now treats documentation and evidence as continuous engineering outputs. Work items, decisions, code reviews, tests, security and accessibility reviews, builds, releases, deployments, and incidents must be traceable through linked records. See:

- `docs/documentation-and-evidence-standard.md`
- `workflows/07-delivery-ci-cd-and-release.md`
- `docs/ci-cd-pipeline-template.md`
- `templates/engineering-activity-log.md`
- `templates/test-plan-and-report.md`
- `templates/release-record.md`
- `templates/incident-postmortem.md`

CI/CD must be adapted to the validated product form factor and chosen technology stack. USF does not assume that every product is a cloud service or that one pipeline fits all projects.


## Quality assurance and documentation acceptance (v0.7.0)

Every product must have audience-appropriate, versioned documentation and evidence that critical instructions work in practice. The documentation acceptance gate requires an independent reviewer to follow important procedures from a clean or reset environment where practical. The AI reviewer must report only actions it actually performed and mark unsupported or inaccessible checks as Blocked/Not Verified.

- `docs/quality-assurance-and-documentation-acceptance.md`
- `workflows/08-quality-assurance-and-documentation-validation.md`
- `templates/documentation-inventory.md`
- `templates/documentation-validation-report.md`


## Agentic delivery loop (v0.8.0)

USF can now *run* its gates, not only describe them. For each approved backlog item, cooperating agents go spec → build → four parallel reviews (security, code/QA, UX/UI, documentation) → approval gate, then merge or escalate to a human with a precise question. Handoffs are files with machine-checkable first lines, rework is bounded, each job is isolated in its own worktree, and the loop never pushes or releases.

- `workflows/09-agentic-delivery-loop.md` — the tool-neutral standard, artifact contract, `job.json` schema, and escalation policy
- `templates/job-spec.md`, `templates/build-report.md`, `templates/review-report.md`, `templates/approval-decision.md`
- `scripts/validate_job.py` — checks a job folder against the contract
- `adapters/claude-code/` — ready-to-copy Claude Code implementation: `/usf-loop` orchestrator skill, seven agents, backlog, and a live dashboard
