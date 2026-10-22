# Workflow 03 — Product Form Factor and Architecture Decisions

## Goal
Select a product form factor and technical architecture based on requirements and explicit trade-offs.

## Keep two decisions separate
A. **Product form factor:** native macOS, native Windows, web, mobile, cross-platform desktop, CLI, API/service, or hybrid.
B. **System architecture:** local-first, modular monolith, client-server, microservices, serverless, event-driven, or hybrid.

They interact but are not mutually exclusive. For example, native macOS can pair with a modular local core or a remote backend.

## Procedure
1. Read the approved brief and PRD.
2. Extract architecture drivers and constraints. Label each as hard constraint, preference, or assumption.
3. Identify unknowns that could change the decision; ask the user if necessary.
4. Generate at least two plausible options unless constraints leave only one viable option.
5. Eliminate options that violate hard constraints.
6. Compare remaining options on user fit, delivery speed, complexity, security/privacy, reliability, performance, operating cost, maintainability, team skills, portability, and reversibility.
7. Explain the recommendation, rejected alternatives, trade-offs, confidence, and assumptions.
8. Identify which decisions require explicit human approval.
9. Create a Product Decision Record for product direction and ADR(s) for technical choices.
10. Define triggers for reassessment and continue to implementation planning only when required approvals are present.

## Decision safeguards
- Do not choose microservices merely because a product may grow. Identify concrete service boundaries and why independent deployment/scaling/ownership is worth the operational cost.
- Do not choose native macOS solely because USF itself may start as a Mac app. Projects created with USF must receive project-specific recommendations.
- Do not assume cloud is acceptable for sensitive data or that local-only is acceptable for collaboration needs.
- Distinguish present requirements from speculative future requirements.
- State confidence and what evidence would change the recommendation.
