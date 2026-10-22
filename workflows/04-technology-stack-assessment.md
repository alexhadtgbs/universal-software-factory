# Workflow: Technology Stack Assessment

## Purpose
Recommend a technology stack that fits this project's validated needs. This workflow follows product-form-factor and architecture assessment; it does not assume a universal preferred stack.

## Inputs
- Approved or sufficiently validated product brief and PRD
- Product Form-Factor Decision and Architecture Decision Record, where available
- Functional and non-functional requirements
- Platform, security, privacy, regulatory, budget, schedule, team, and operating constraints
- Existing codebase and dependency inventory for brownfield projects

## Procedure

1. **Set the decision boundary**
   - Identify the components/layers requiring a decision and what is out of scope.
   - Identify decision owner, approvers, deadline, and consequences of delay.
   - Separate mandatory constraints from preferences.

2. **Inventory the needs**
   - Map requirements and quality attributes to technology capabilities.
   - Identify existing technologies, integration contracts, migration constraints, team skills, and operational expectations.
   - Avoid adding layers or dependencies that do not serve a stated need.

3. **Generate credible alternatives**
   - Include the status quo where applicable.
   - Consider build, buy, reuse, and defer options where relevant.
   - Exclude alternatives that fail hard constraints, recording the reason.
   - Avoid presenting a single option as a comparison.

4. **Research current evidence**
   - Prefer official documentation, release/support policies, security advisories, license texts, compatibility matrices, and published pricing.
   - Record source URLs, access/review date, relevant version, and what the source actually establishes.
   - Use independent evidence for material claims when practical.
   - Verify active maintenance, upgrade path, known vulnerabilities, platform support, licensing, and exit/migration options.
   - Clearly label estimates, uncertain claims, and unavailable evidence. Never fabricate research or sources.

5. **Evaluate options**
   - Apply project-specific criteria and weights.
   - Treat hard constraints as pass/fail gates.
   - Record evidence and rationale behind scores; use “unknown” rather than false precision.
   - Evaluate the complete stack as well as important interactions between layers.
   - Consider total lifecycle cost, including hosting, licenses, support, upgrades, migration, training, and operations.

6. **Resolve uncertainty**
   - Ask stakeholders for missing business or operational constraints.
   - Research unresolved factual claims.
   - Design a time-boxed proof of concept for high-risk unknowns, with hypotheses, success criteria, owner, and stop conditions.
   - Do not treat a proof of concept as production readiness.

7. **Recommend and review**
   - Produce a Technology Decision Record using `templates/technology-decision-record.md`.
   - State the recommendation, rejected alternatives, trade-offs, risks, assumptions, confidence, and review triggers.
   - Obtain required human approvals before material or hard-to-reverse commitments.
   - Link the TDR to requirements, ADRs/PDRs, epics, implementation tasks, and verification evidence.

8. **Validate during delivery**
   - Check selected versions and integrations against the decision.
   - Capture evidence from prototypes, builds, tests, security scans, and deployment experiments.
   - Raise a decision review if evidence invalidates a key assumption.

9. **Reassess when triggered**
   - Revisit the decision when platform targets, requirements, risk, support, costs, licenses, or maintenance conditions materially change.
   - Compare staying, upgrading, replacing, and reducing dependencies.
   - If the decision changes, create a new TDR that supersedes the previous record; do not rewrite history.

## Outputs
- Completed Technology Decision Record
- Research/evidence list
- Explicit unresolved questions and proof-of-concept plan, if needed
- Approval status and traceability links
- Reassessment triggers and review date

## Exit criteria
- Hard constraints have been checked.
- Alternatives and evidence are documented.
- Material uncertainties have been resolved or explicitly accepted by an authorized owner.
- The decision has the required approvals.
- Downstream work can trace back to the decision and requirements.
