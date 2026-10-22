---
name: universal-software-factory
version: 0.8.0
description: Portable workflows for product discovery, requirements, architecture decisions, implementation, and software quality.
---

# Universal Software Factory (USF)

## Mission
Turn a product idea into a traceable, tested, maintainable software release through explicit product decisions, architecture decisions, engineering tasks, and quality evidence.

## Non-negotiable principles
1. **Requirements before implementation:** clarify the problem and constraints before generating substantial code.
2. **No architecture by fashion:** never assume native, web, monolith, microservices, serverless, or cloud is the default for every project.
3. **Separate product form factor from system architecture:** a native macOS client can use a local core, a monolith backend, or microservices. These are different dimensions.
4. **Collaborative accountability:** Product Manager owns product goals and requirements; Solution Architect owns technical architecture quality. They collaborate on recommendations.
5. **Make uncertainty visible:** distinguish user-approved facts, inferred assumptions, and open questions. Ask targeted questions when a missing answer could materially change the decision.
6. **Present consequential choices:** explain viable options, trade-offs, risks, and confidence. Obtain user approval where a decision materially affects cost, privacy, deployment, lock-in, or scope.
7. **Traceability:** link goals → requirements → epics → stories → tasks → code changes → tests → release evidence.
8. **Small reversible steps:** prefer the simplest architecture that satisfies validated requirements, while preserving sensible extension points.
9. **Quality is part of delivery:** testing, security, documentation, accessibility where relevant, and operational readiness are not optional afterthoughts.
10. **Tool neutrality:** use adapters for different coding agents; never assume all agents expose the same capabilities or permissions.

## Standard lifecycle
Idea → Product Discovery → PRD → Product-form-factor Assessment → Architecture Assessment → Product Decision Record / ADR → Epics & Stories → Engineering Plan → Implementation → Tests & Review → Release.

Per approved work item, Implementation → Tests & Review can run as the agentic delivery loop (workflow 09): spec → build → parallel reviews → approval gate → merge or human escalation.

The sequence can iterate. A material requirement change may reopen a product or architecture decision.

## Role boundaries
- Product Manager (PM): user problem, target market/personas, outcomes, scope, priorities, product requirements, success measures, and product decision records.
- Business Analyst: detailed workflows, business rules, edge cases, and requirement clarification.
- UX/UI Designer: journeys, interaction model, accessibility, and interface specifications.
- Solution Architect (SA): technical alternatives, system boundaries, integration, data, security, reliability, deployment, architecture records.
- Technical Lead: task decomposition, dependencies, coding conventions, implementation sequence.
- Engineers: implement approved tasks and add tests.
- QA: independent verification against acceptance criteria and risk-based test plans.
- Security: threat modeling, least privilege, secrets handling, security verification.
- Reviewer: review code and evidence against project standards.
- Human owner: approves consequential product/architecture choices and risky actions according to project policy.

Roles may be implemented as prompts, skills, or separate agents; separate always-on agents are not required.

## Required behavior for a new project
1. Read available project context and identify missing information.
2. Run product discovery; label assumptions and open questions.
3. Draft a PRD with measurable outcomes, scope, functional requirements, and nonfunctional requirements.
4. Assess product form factor independently from backend/system architecture.
5. Generate viable alternatives and evaluate hard constraints before scoring preferences.
6. Recommend an option with rationale, trade-offs, risks, confidence, and reversibility.
7. Create a Product Decision Record and one or more ADRs as appropriate.
8. Obtain approval for decisions marked as approval-required.
9. Generate epics, stories, acceptance criteria, and a traceable implementation plan.
10. Implement only against approved requirements and task scope.
11. Verify acceptance criteria and quality gates; report gaps honestly.

## Architecture decision rule
USF MUST NOT prescribe a product form factor or software architecture before evaluating the product requirements, constraints, and viable alternatives. The PM and SA MUST collaborate on a recommendation, document rationale and trade-offs, and identify decisions requiring user approval.

Consider, where relevant:
- Product form factor: native desktop, web, mobile, cross-platform desktop, CLI, API/service, hybrid.
- Architecture: local-first, modular monolith, client-server, microservices, serverless, event-driven, hybrid.
- Drivers: offline behavior, OS integration, collaboration, data sensitivity/residency, scale, latency, availability, deployment, integrations, maintainability, team capabilities, budget, observability, disaster recovery.
- Hard constraints must be checked before weighted preferences.
- Microservices require a positive justification such as independent scaling/deployment, bounded service ownership, or demonstrated operational needs; they are not the default for growth.
- Prefer a modular monolith when it meets requirements and reduces unnecessary distributed-systems complexity.
- Record triggers that would justify revisiting the decision.

## Output conventions
- Use concise Markdown artifacts in the project's agreed documentation directory.
- Include IDs and status for requirements, epics, stories, tasks, decisions, and tests when feasible.
- Label status: `draft`, `proposed`, `approved`, `superseded`, or `rejected`.
- Do not claim tests, builds, integrations, or platform behavior were verified unless they actually were.

## Technology Stack Advisor

The Technology Stack Advisor is responsible for helping the team choose, validate, and periodically reassess technologies for the current project. This role may be performed by a dedicated agent or as a workflow capability.

### Mandatory technology-selection policy

USF MUST evaluate the suitability of the technology stack for each project based on its validated requirements, product form factor, architecture, constraints, and lifecycle needs. It MUST NOT assume that technologies used in previous projects are optimal for the current project.

The Technology Stack Advisor MUST collaborate with the Product Manager, Solution Architect, Technical Lead, Security Engineer, and delivery stakeholders as appropriate. The advisor MUST:
- identify hard constraints before scoring options;
- compare credible alternatives, including retaining existing technology or choosing not to add a dependency;
- use current, attributable evidence for material claims about support, compatibility, security, licensing, pricing, and ecosystem health;
- distinguish verified facts from assumptions, estimates, and opinions;
- document the recommendation, alternatives, trade-offs, evidence, assumptions, risks, confidence, and approval requirements in a Technology Decision Record (TDR);
- recommend a proof of concept when material uncertainty cannot be resolved adequately through research or stakeholder clarification;
- avoid irreversible commitments until material uncertainties and required approvals are addressed.

USF MUST optimize for project suitability and lifecycle value, not popularity, novelty, or consistency with previous projects. A familiar stack may be selected when evidence supports it; familiarity alone is not sufficient justification.

### Evaluation criteria

Apply project-specific criteria and weights. Treat hard constraints as pass/fail gates, not as scores that can be outweighed by strengths elsewhere. Consider, where relevant:
- functional and platform fit;
- compatibility with the selected product form factor and architecture;
- security, privacy, compliance, and data residency;
- maintainability, operability, and team capability;
- delivery speed and migration effort;
- performance, reliability, accessibility, and scalability;
- total cost of ownership over a stated time horizon;
- ecosystem maturity, documentation, community and vendor support;
- licensing and legal constraints;
- interoperability, portability, lock-in, and reversibility;
- testing, observability, deployment, and upgrade paths.

Weights MUST be tailored to the project and justified. Scores are decision aids, not substitutes for engineering judgment. Do not invent precision where evidence is weak; record confidence and evidence quality.

### Technology lifecycle and reassessment

A selected stack is not permanent. Reassess when requirements or platform targets change, dependencies become unsupported or materially vulnerable, compatibility breaks, quality goals are not met, costs or license terms materially change, operational burden becomes unacceptable, or a credible alternative offers a compelling lifecycle benefit.

Reassessment MUST NOT automatically trigger migration. Compare the expected benefits against migration cost, transition risk, retraining, compatibility, and opportunity cost. Preserve accepted decision records; create a new record that supersedes the old one when a material decision changes.

## Security Is a Non-Negotiable Requirement

Security MUST be considered throughout discovery, design, implementation, testing, release, and maintenance. It is not an optional final checklist or a feature that can be deferred without an explicit, documented risk decision.

### Security Reviewer / Ethical Hacker

USF MUST include a Security Reviewer capability that operates with the mindset and methods of an ethical hacker. The role may be performed by a dedicated agent or workflow, but it MUST be explicitly invoked at the security gates described below. It must independently challenge assumptions and attempt to identify realistic ways the system could be abused.

The reviewer MUST:
- model threats based on assets, trust boundaries, attackers, entry points, privileges, and likely abuse cases;
- inspect requirements, architecture, dependencies, source code, configuration, build/release processes, and deployment assumptions as relevant;
- look for vulnerabilities such as broken authentication or authorization, privilege escalation, injection, insecure deserialization, path traversal, SSRF, unsafe file handling, secrets exposure, insecure cryptography, data leakage, race conditions, unsafe update mechanisms, supply-chain compromise, and denial-of-service risks;
- review privacy, least privilege, secure defaults, error handling, logging, data retention, and recovery behavior;
- use proportionate defensive methods such as code review, static analysis, dependency and secret scanning, configuration checks, fuzzing, and authorized dynamic testing where available;
- report findings with affected component, reproducible evidence, severity, exploitability, impact, remediation guidance, and verification steps;
- validate fixes and check for regressions rather than treating a proposed patch as proof of resolution;
- identify limitations in tools, test coverage, environment, and evidence; never claim a system is secure merely because a scan is clean;
- preserve useful audit evidence without copying secrets or unnecessary personal data into reports.

### Authorization and safe testing boundaries

All active security testing MUST be explicitly authorized and limited to systems, accounts, environments, data, and techniques within the approved scope. Prefer isolated test environments and synthetic data. Do not attack third-party systems, evade monitoring, persist unauthorized access, exfiltrate real data, or disrupt production. If scope or authorization is unclear, stop active testing and ask the accountable human owner. Any production testing requires explicit authorization, a defined window, rollback/stop conditions, and an impact plan.

### Security gates

1. **Discovery and requirements:** identify sensitive assets, data classification, compliance obligations, abuse cases, and security/privacy requirements.
2. **Product and architecture decisions:** threat-model trust boundaries and evaluate security consequences of alternatives; document material risks in PDRs/ADRs/TDRs.
3. **Implementation planning:** define security acceptance criteria, test cases, dependency policies, secret handling, and review ownership.
4. **During implementation:** use secure coding practices, review risky changes, scan dependencies and secrets, and test authorization boundaries.
5. **Pre-release:** require a risk-based security review of the release candidate, relevant test evidence, remediation status, and explicit disposition of residual risks.
6. **After release:** monitor advisories and security signals, patch dependencies, respond to incidents, and revisit threat models after material changes.

### Findings and release decisions

Security findings MUST be prioritized using severity, exploitability, exposure, impact, and context. As a default release policy:
- Critical and High findings MUST block release until fixed and verified, or until a formally authorized exception is approved under a documented risk-acceptance process. An exception must include compensating controls, owner, expiry/review date, and mitigation plan.
- Medium and Low findings MUST have a documented disposition, owner, and target date or rationale for acceptance.
- Any suspected active compromise, exposed credential, or safety-critical vulnerability MUST trigger the relevant incident/credential-rotation process immediately.

An agent MUST NOT silently waive a security gate, approve its own high-risk exception, or represent an untested mitigation as verified. Final acceptance of material residual risk belongs to an accountable human, not solely to an AI agent.

### Security evidence
Maintain a traceable record of threat models, security requirements, review scope, tools and versions, test results, findings, remediation commits, retest results, exceptions, and approvals. Security testing complements—not replaces—design review, operational controls, and independent human judgment.

## UX/UI Design: Best Practices and Purposeful Innovation

USF MUST treat UX/UI as a core product discipline, not decoration applied after implementation. The UX/UI Designer MUST ground design in user goals, product requirements, chosen platform conventions, accessibility, privacy, and technical constraints.

The designer MUST:
- distinguish user evidence from assumptions and identify validation needs;
- define critical journeys, task flows, content hierarchy, interaction states, and usability success criteria;
- use familiar, platform-appropriate patterns when they improve clarity and learnability;
- treat accessibility and inclusive design as requirements from the beginning;
- explore purposeful alternatives for important journeys when appropriate, explaining the user benefit and trade-offs;
- prototype and validate novel interactions rather than assuming novelty improves usability;
- account for errors, recovery, empty/loading states, permissions, text scaling, keyboard use, and assistive technology;
- collaborate with Product, Engineering, Security, and Privacy roles;
- provide implementation-ready specifications and review the shipped experience.

USF MUST NOT equate innovation with visual novelty. A design is only an improvement when it creates meaningful user value without unacceptable regressions in clarity, accessibility, trust, or task success. Where user research is unavailable, assumptions MUST be labelled and a proportionate validation plan proposed.


## Continuous documentation and delivery evidence
- Document work as it happens; do not defer records to the end of a project.
- Keep requirement → decision → work item → PR/commit → test evidence → build/release traceability.
- Follow `docs/documentation-and-evidence-standard.md` and `workflows/07-delivery-ci-cd-and-release.md`.
- Plan CI/CD early, keep pipeline configuration under review/version control, publish actionable evidence, and define release gates, rollback/recovery, and post-release verification.
- Tailor pipeline stages to the selected product form factor, stack, risks, and distribution model. Do not assume a cloud deployment or universal coverage threshold.
- Record pipeline failures, release decisions, exceptions, and incidents with owners, dates, and follow-up actions.


## Quality assurance and documentation validation
- Treat documentation as a product deliverable and release gate, not optional polish.
- Maintain a documentation inventory appropriate to end users, operators, developers, and API/CLI users.
- Follow `docs/quality-assurance-and-documentation-acceptance.md` and `workflows/08-quality-assurance-and-documentation-validation.md`.
- Have an independent reviewer follow critical instructions literally from a clean/reset environment where practical; compare observed outcomes with documented outcomes.
- The AI reviewer must never fabricate execution, infer a pass from code inspection alone, or silently use undocumented steps. Mark unavailable checks Blocked/Not Verified and explain the limitation.
- Attach reproducible evidence and defect IDs; retest corrections and link the QA/documentation validation report to the release record.


## Agentic delivery loop
When implementing an approved backlog item with multiple agents, follow `workflows/09-agentic-delivery-loop.md`:
- Run only items whose requirements and governing PDR/ADR/TDRs are approved; route anything needing a new decision back to workflows 01–04.
- Hand off through files, not conversation: spec → build report → one review per lens (security, code/QA, UX/UI, documentation) → approval decision. Each agent writes exactly one file; reviewers and the approval gate never edit code; one orchestrator owns job state.
- Start every gate file with its fixed token (`STATUS: READY|BLOCKED`, `VERDICT: PASS|CHANGES`, `APPROVE|ESCALATE`) so gates are machine-checkable; treat anything else as a protocol failure.
- Wait for all reviews before rework, and bound rework (default 3 rounds) before escalating to a human.
- Isolate each job on its own branch and worktree (or sandbox), ports, and browser sessions; never push, deploy, or release from the loop.
- Escalate instead of auto-merging for auth/identity/payments/data-access, CI/deploy/build config, migrations or external messages, dependency changes, departures from approved decisions, residual security risk, product/business assumptions, and Not Verified critical checks.
- Templates: `templates/job-spec.md`, `templates/build-report.md`, `templates/review-report.md`, `templates/approval-decision.md`. Validate job folders with `scripts/validate_job.py`. A Claude Code implementation is in `adapters/claude-code/`.
