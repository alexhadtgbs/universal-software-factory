# USF Roles and Responsibilities

Roles are capabilities, not a requirement to run a separate agent for each task. A single agent or person may perform multiple roles when appropriate, but security review must be explicit and sufficiently independent for the risk involved. High-risk changes should receive independent review rather than relying only on the implementer's self-review.

- **Product Manager:** problem, users, outcomes, scope, requirements, priorities, and roadmap.
- **Business Analyst:** elicitation, clarification, acceptance criteria, process and domain modeling.
- **Solution Architect:** system boundaries, architecture alternatives, quality attributes, integration, and architecture decisions.
- **Technology Stack Advisor:** technology candidates, current evidence, compatibility, licensing, security/support lifecycle, total cost, trade-offs, and TDR.
- **UX/UI Designer:** user research synthesis, journeys, information architecture, interaction and visual design, accessibility, usability validation, and purposeful innovation.
- **Technical Lead:** implementation strategy, engineering standards, decomposition, and technical coordination.
- **Engineers:** implementation, maintainability, tests, and technical documentation.
- **QA/Test Engineer:** verification strategy, risk-based testing, regression, and release evidence.
- **Security Reviewer / Ethical Hacker:** independently threat-models and challenges the product; reviews architecture and code; performs authorized security testing; verifies fixes; reports vulnerabilities and residual risk.
- **Security/Privacy Owner:** ensures privacy, compliance, and security requirements are identified; coordinates response and risk acceptance. This can be the same human as a reviewer in small projects, but high-risk findings should receive independent verification where practical.
- **DevOps/Release Engineer:** build, packaging, deployment, observability, recovery, and release operations.
- **Code Reviewer:** independent review of correctness, security, maintainability, and adherence to decisions.

## Security independence and authority
- Security is mandatory across the lifecycle, not just before release.
- The Security Reviewer / Ethical Hacker must be able to raise blockers and escalate unresolved findings.
- The implementer must not be the sole verifier of a high-risk security fix.
- AI agents can analyze, test, and recommend, but cannot independently accept material residual risk on behalf of the organization.
- Testing must be authorized and scoped. If authorization is unclear, active testing stops until the accountable owner clarifies it.
- A clean scanner result is not proof of security; review conclusions must state coverage and limitations.

## Decision collaboration
Product Manager and Solution Architect jointly ensure that product form factor and architecture fit validated needs. The Technology Stack Advisor collaborates with the Solution Architect and Technical Lead on stack fit, and involves Security/Privacy reviewers where relevant. The Security Reviewer should be involved in threat modeling, material architecture and technology decisions, risky implementation changes, and pre-release review. The accountable human owner approves consequential product, architecture, technology, and residual-risk decisions.


## UX/UI Designer operating standard
The UX/UI Designer must use platform conventions and accessibility best practices as the foundation, then explore purposeful differentiation where it can improve a real user outcome. The role must distinguish evidence from assumptions, prototype risky interactions, test important tasks, consider all meaningful UI states, and document trade-offs. Novelty alone is not a success criterion; clarity, accessibility, user control, and measurable usefulness must not be sacrificed for visual novelty.
