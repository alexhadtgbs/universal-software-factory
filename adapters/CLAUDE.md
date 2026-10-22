# USF Instructions

Read `skills/universal-software-factory/SKILL.md` before working on substantial product or engineering tasks.

For new projects, complete discovery, PRD/backlog, and product/architecture/technology decision workflows before substantial implementation. Do not assume native macOS, web, monolith, or microservices. Treat product form factor and system architecture as separate decisions. Record assumptions, alternatives, trade-offs, confidence, and approval needs in PDRs/ADRs/TDRs.

Apply the security, UX/UI, documentation-and-evidence, and QA/documentation-acceptance gates throughout, not at the end. Preserve requirement-to-test traceability, never push or release without the required approvals, and report verification honestly: anything not actually run is Not Verified.

To implement approved backlog items with agents, use the delivery loop in `adapters/claude-code/` (`/usf-loop`, workflow 09).
