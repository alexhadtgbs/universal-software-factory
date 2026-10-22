# Workflow 09: Agentic Delivery Loop

Turns one approved backlog item into a reviewed, merged change (or a precise question for a human) using cooperating agents. It operationalizes workflows 05–08 for a single work item. It does not replace discovery, PRD, or decision workflows: run it only for items whose requirements and governing decisions are already approved.

## When to use
- The item is traceable to an approved requirement (or is a defect/chore the project policy allows without one).
- The product form factor, architecture, and technology decisions it depends on are approved.
- The repository's agent instructions (`AGENTS.md` / `CLAUDE.md`) say how to set up a fresh checkout, run the app, and run tests, build, and lint.

If any of these is missing, stop and route the item back to the relevant earlier workflow.

## The loop

```
item → spec → build → [security, code, ux-ui, docs] reviews → WAIT FOR ALL
                ▲                                                  │
                └────── any CHANGES and rounds left: rework ◄──────┤
                                                                   ▼ all PASS
                                   merge ◄─ APPROVE ─ approval gate ─ ESCALATE → needs-human
```

| Step     | Role (USF)                         | Writes                         |
| -------- | ---------------------------------- | ------------------------------ |
| spec     | Product Manager / Business Analyst | `spec.md`                      |
| build    | Engineer                           | `build.md` + commits on branch |
| review   | Security Reviewer                  | `round-N/review-security.md`   |
|          | Reviewer / QA                      | `round-N/review-code.md`       |
|          | UX/UI Designer                     | `round-N/review-ux-ui.md`      |
|          | Documentation reviewer             | `round-N/review-docs.md`       |
| approval | Approval gate (Reviewer)           | `decision.md`                  |
| state    | Orchestrator                       | `job.json`                     |

## Operating rules
1. **Context comes from files, not conversation.** Each agent reads the project instructions, the job folder, and the change itself. Nothing depends on what another agent "remembers".
2. **One writer per file.** Each agent writes exactly one job file. Only the orchestrator writes `job.json`. Reviewers and the approval gate never edit code.
3. **Machine-readable first lines.** Every job file starts with a fixed token so gates can be checked without interpretation (see *Artifact contract*). Anything else on the first line is a protocol failure: stop and tell the human.
4. **Wait for all reviews.** A round ends only when every review file exists. Never start rework mid-round.
5. **Bounded rework.** Default maximum: 3 review rounds per run. When exhausted, escalate with the outstanding findings; do not loop indefinitely.
6. **Isolation.** Each job runs on its own branch in its own worktree (or equivalent sandbox), with its own ports and browser sessions. The human's main checkout is touched only by the merge step.
7. **Evidence, not assertion.** Every acceptance criterion needs recorded evidence (command + result, or observed page state). A check that was not run is `Not Verified`, never inferred as passed.
8. **Never push, deploy, or release from the loop.** Merging to the integration branch is the furthest the loop goes; delivery follows workflow 07.

## Artifact contract

| File                       | First line                                  | Meaning                                         |
| -------------------------- | ------------------------------------------- | ----------------------------------------------- |
| `spec.md`                  | `# <title>`                                 | Spec exists; see `templates/job-spec.md`        |
| `build.md`                 | `STATUS: READY` or `STATUS: BLOCKED`        | Ready for review, or needs a human              |
| `round-N/review-<lens>.md` | `VERDICT: PASS` or `VERDICT: CHANGES`       | Lens accepts, or blocking findings listed       |
| `decision.md`              | `APPROVE` or `ESCALATE`                     | Merge automatically, or hand to a human         |
| `rework-K.md`              | free text                                   | Human feedback for a rework run                 |

### job.json

```json
{
  "id": "007-export-csv",
  "item": "Export the report table as CSV",
  "requirements": ["REQ-014"],
  "branch": "usf/007-export-csv",
  "worktree": "/abs/path/to/repo-usf/007-export-csv",
  "stage": "review",
  "round": 2,
  "max_rounds": 3,
  "reviews": { "security": "PASS", "code": "CHANGES", "ux-ui": "PASS", "docs": "pending" },
  "updated": "2026-10-22T14:03:00Z"
}
```

- `stage`: `spec`, `build`, `review`, `approve`, `merged`, or `needs-human`.
- `round`: current review round; `0` before the first round.
- `reviews`: current round only; each value `pending`, `PASS`, or `CHANGES`. Earlier rounds stay in their `round-N/` folders.
- Rewrite the whole file on every transition. `scripts/validate_job.py` checks a job folder against this contract.

## Escalation policy (approval gate)

The approval gate APPROVES only when every acceptance criterion is met with convincing evidence (and it spot-checks at least one itself), all final-round reviews are PASS with no real problem hidden in their notes, the branch merges cleanly, and the Definition of Done is satisfied.

It ESCALATES, regardless of review results, when the change:
- touches authentication, authorization, identity, payments, or data-access rules;
- changes CI/CD, build, deploy, hosting, release, or update-mechanism configuration;
- migrates a schema, writes production data, sends email or other external messages;
- adds, removes, or upgrades a dependency (a TDR may be required — workflow 04);
- departs from an approved PDR/ADR/TDR or implies a new consequential decision;
- carries a security finding of any severity whose acceptance is a residual-risk decision (USF reserves that for an accountable human);
- rests on a spec assumption that is really a product or business decision (pricing, public claims, scope, privacy, what is free vs paid);
- leaves any critical check `Not Verified` or `Blocked`.

`decision.md` for an escalation must state the exact decision or check needed from the human and the files to inspect.

## Human commands
- **Approve:** human accepts an escalated job → run the merge step.
- **Rework:** human writes feedback → saved verbatim as `rework-K.md`; a fresh build run starts with a fresh round budget.
- **Abandon:** human closes the job; branch and worktree are removed only on explicit instruction.

## Merge step
Merge only when the main checkout is clean and on the integration branch. Use a non-fast-forward merge so the job is visible in history, then remove the worktree and branch. If the merge fails, abort it and move the job to `needs-human`. Record the merge commit in the job's traceability links.

## Outputs
- Job folder with spec, build report, review rounds, decision, and `job.json`.
- Commits on the job branch, merged or awaiting a human.
- Updated traceability (requirement → job → commits → evidence).

## Tool adapters
- Claude Code: `adapters/claude-code/` provides a ready-to-copy orchestrator skill (`/usf-loop`), agents, backlog, and dashboard.
- Other agents: implement the same roles and artifact contract; the contract, not the tool, is the standard.
