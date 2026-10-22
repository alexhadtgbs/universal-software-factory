# System Overview

USF separates portable process guidance from any one application or agent.

- **Shared skill:** roles, rules, lifecycle, decision standards.
- **Workflows:** repeatable procedures for discovery, requirements, architecture, planning, implementation, and quality.
- **Templates:** versioned product and engineering artifacts.
- **Adapters:** entry points and instructions for different agent environments.
- **Future desktop application:** an interface and orchestration layer that invokes workflows and tracks artifacts. This package does not yet implement that app.

## Suggested artifact layout in a project
```text
product/
  product-brief.md
  prd.md
  backlog.md
decisions/
  PDR-001-product-direction.md
  ADR-001-system-architecture.md
engineering/
  plan.md
quality/
  traceability-matrix.md
  test-plan.md
```

The exact layout can be configured per project. Artifacts should remain readable and portable.
