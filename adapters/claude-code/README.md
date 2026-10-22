# USF adapter for Claude Code

A ready-to-copy implementation of `workflows/09-agentic-delivery-loop.md`. One orchestrator skill and seven subagents take an approved backlog item through spec → build → four parallel reviews → approval gate, then merge it or hand it to a human with a precise question.

```
item → usf-spec-writer → usf-builder → [security, code, ux-ui, docs] → WAIT FOR ALL
                              ▲                                          │
                              └──── any CHANGES (≤ 3 rounds): resume ◄───┤
                                                                         ▼ all PASS
                                    merge ◄─ APPROVE ─ usf-approver ─ ESCALATE → needs-human
```

## Contents

```
.claude/skills/usf-loop/SKILL.md        orchestrator: runs the loop, sole writer of job.json
.claude/agents/
  usf-spec-writer.md        opus    spec.md (traceable to REQ-IDs)
  usf-builder.md            opus    commits on usf/<job-id>, build.md with evidence
  usf-reviewer-security.md  opus    round-N/review-security.md (severity-rated)
  usf-reviewer-code.md      sonnet  round-N/review-code.md (correctness, tests, evidence)
  usf-reviewer-ux-ui.md     sonnet  round-N/review-ux-ui.md (flows, states, a11y, visuals)
  usf-reviewer-docs.md      sonnet  round-N/review-docs.md (follows procedures literally)
  usf-approver.md           opus    decision.md under USF's escalation policy
usf/
  backlog.md                queue for /usf-loop next
  dashboard.html            live board, no dependencies
```

## Install into a project

1. Copy `.claude/` and `usf/` into the repo root.
2. Copy the USF core skill: `skills/universal-software-factory/` → `.claude/skills/universal-software-factory/`. The agents read its security, UX, and QA rules.
3. Copy `scripts/validate_job.py` → `usf/validate_job.py` (optional; the orchestrator runs it at the end of each job when present).
4. Add `/usf/jobs/` to `.gitignore` — job folders are runtime state.
5. Make sure `AGENTS.md` (or `CLAUDE.md`) states: fresh-checkout setup, how to start the app on a given port, test/build/lint commands, the integration branch if not `main`, the browser automation tool agents should use (if the product has UI), and any extra always-escalate areas.
6. Commit on the integration branch, then run `/usf-loop <item>` or `/usf-loop next`.

## Commands

```
/usf-loop <item>                  run a new job
/usf-loop next                    run the first unchecked backlog item
/usf-loop approve <job-id>        human accepts an escalated job and merges it
/usf-loop rework <job-id> <note>  send an escalated job back with feedback
/usf-loop status                  one line per job
```

Run several jobs in parallel by starting `/usf-loop` in separate Claude Code sessions: each job has its own worktree (`../<repo>-usf/<job-id>/`), branch, ports, and browser sessions.

## Dashboard

```bash
cd usf && python -m http.server 8000
```

Open `http://localhost:8000/dashboard.html`. Cards move through stages, review chips fill in as verdicts land, escalated jobs are highlighted, and clicking a card shows its files.

## Checking a job

```bash
python usf/validate_job.py usf/jobs            # every job
python usf/validate_job.py usf/jobs/007-export-csv
```

## What stays with workflows 01–08

The loop implements one approved item. Discovery, PRDs, product/architecture/technology decisions, release, deployment, and residual-risk acceptance remain human-approved activities. The loop never pushes, deploys, or releases.

## Attribution

The loop shape (file-based handoffs, first-line verdicts, parallel review lenses, bounded rework, worktree-per-job, escalation gate, polling board) was inspired by the "software factory for Claude Code" example in the zazencodes-season-3 repository. This adapter is an independent implementation written for USF.
