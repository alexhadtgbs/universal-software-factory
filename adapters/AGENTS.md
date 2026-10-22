# USF Instructions

Use `skills/universal-software-factory/SKILL.md` as the shared operating standard.

For new projects, follow the product discovery, PRD/backlog, and product/architecture/technology decision workflows before substantial implementation. Do not assume native macOS, web, monolith, or microservices. Keep product form factor and system architecture as separate decisions. Document assumptions, alternatives, trade-offs, confidence, and required approvals in PDRs/ADRs/TDRs.

Apply the security, UX/UI, documentation-and-evidence, and QA/documentation-acceptance gates throughout, not at the end. Maintain traceability from requirements to tests, never push or release without the required approvals, and report verification honestly: anything not actually run is Not Verified.

When several agents implement an approved item, follow `workflows/09-agentic-delivery-loop.md` and its artifact contract.
