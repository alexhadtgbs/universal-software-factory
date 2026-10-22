# Workflow 02 — PRD and Backlog

## Goal
Translate an approved product brief into testable requirements and a prioritized backlog.

## PRD sections
1. Summary and product vision
2. Problem, target users, and personas
3. Goals, success metrics, and non-goals
4. User journeys and functional requirements
5. Nonfunctional requirements (performance, availability, privacy, security, accessibility, offline use, scale, maintainability)
6. Data classification, retention, and ownership
7. Integrations and external dependencies
8. Constraints, assumptions, risks, and open questions
9. Release scope and deferred capabilities
10. Acceptance criteria and measurement plan

## Backlog rules
- Use stable IDs such as `REQ-001`, `EPIC-001`, `STORY-001`, `TASK-001`, `TEST-001`.
- Each story describes a user/value outcome and includes observable acceptance criteria.
- Keep stories small enough to estimate and verify.
- Link every story to one or more requirements; link tasks to stories and tests to acceptance criteria.
- Mark priorities and dependencies; do not treat every request as P0.
- Do not make technology-specific stories a substitute for user outcomes. Technical enablers are allowed when their purpose is explained.

## User story template
**ID / Title:** STORY-###
**As a:** [persona]
**I want:** [capability]
**So that:** [user value]
**Linked requirements:** REQ-###
**Priority:** P0/P1/P2/P3
**Dependencies:** [...]
**Acceptance criteria:** Given / When / Then
**Telemetry or success measure:** [...]
**Risks / notes:** [...]
