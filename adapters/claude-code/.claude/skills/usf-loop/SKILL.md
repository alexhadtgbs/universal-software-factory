---
name: usf-loop
description: Run the USF agentic delivery loop (workflow 09) for one work item. Use when the user types /usf-loop <item>, /usf-loop next, /usf-loop approve <job-id>, /usf-loop rework <job-id> <note>, or /usf-loop status. The session that runs it becomes the orchestrator of the spec → build → review → approval loop.
---

# USF delivery loop

You orchestrate one job. You spawn every agent, move the job between stages, and are the only writer of the job's `job.json`. You never write code, specs, reviews, or decisions yourself (the one exception is the round-limit escalation below). The standard is `workflows/09-agentic-delivery-loop.md` of USF; the core USF rules live in `.claude/skills/universal-software-factory/SKILL.md`.

## Preconditions

Before creating a job, check and stop with a clear message if any fails:
- The repo is a git repository and `AGENTS.md` or `CLAUDE.md` says how to set up a fresh checkout, start the app on a given port, and run tests, build, and lint.
- The integration branch exists. It is `main` unless `AGENTS.md` names another; below, `<base>` means that branch.
- The item is traceable to an approved requirement, or the user confirms it is a defect/chore that does not need one. If it would need a new product, architecture, or technology decision, say so and stop: that work belongs in workflows 01–04.

## Agents

| Step     | `subagent_type`         | Writes                                 |
| -------- | ----------------------- | -------------------------------------- |
| spec     | `usf-spec-writer`       | `spec.md`                              |
| build    | `usf-builder`           | `build.md` + commits on `usf/<job-id>` |
| review   | `usf-reviewer-security` | `round-N/review-security.md`           |
|          | `usf-reviewer-code`     | `round-N/review-code.md`               |
|          | `usf-reviewer-ux-ui`    | `round-N/review-ux-ui.md`              |
|          | `usf-reviewer-docs`     | `round-N/review-docs.md`               |
| approval | `usf-approver`          | `decision.md`                          |

`MAX_ROUNDS = 3` review rounds per run (the builder is resumed at most twice).

## Files

`<repo>` is `git rev-parse --show-toplevel` from your session; `<name>` is its folder name. `usf/jobs/` is gitignored runtime state.

```
<repo>/usf/backlog.md                         queue for /usf-loop next
<repo>/usf/dashboard.html                     live board (reads usf/jobs/)
<repo>/usf/jobs/<job-id>/job.json             state; only you write it
<repo>/usf/jobs/<job-id>/spec.md
<repo>/usf/jobs/<job-id>/build.md
<repo>/usf/jobs/<job-id>/rework-<k>.md        human feedback, written by you verbatim
<repo>/usf/jobs/<job-id>/round-<N>/review-{security,code,ux-ui,docs}.md
<repo>/usf/jobs/<job-id>/decision.md
<repo>/../<name>-usf/<job-id>/                the job's worktree on branch usf/<job-id>
```

`job.json` follows the schema in workflow 09. Rewrite the whole file on every transition and set `updated` to the current UTC time. `worktree` is always an absolute path.

## Prompts

Every agent prompt starts with:
`Job folder: <repo>/usf/jobs/<job-id>/. Worktree: <worktree>. Branch: usf/<job-id>. Base: <base>.`
Below, `<paths>` stands for that sentence.

Agents that run the app get a port. With `n` the job number (`007` → 7): builder `5100 + 10n`, `usf-reviewer-ux-ui` `5101 + 10n`, `usf-reviewer-docs` `5102 + 10n`. Append ` Port: <port>.`

## /usf-loop <item>

1. **Create the job.** `mkdir -p usf/jobs`. Pick the next 3-digit number after the highest folder in `usf/jobs/` (`001` if none) and a 2–4 word kebab-case slug. Claim it with `mkdir usf/jobs/<job-id>` (no `-p`); if that fails, another session took it, so take the next number. Ask the user for the requirement IDs if the item does not name them. Write `job.json` with `stage: "spec"`, `round: 0`, `max_rounds: 3`, all reviews `pending`.
2. **Worktree.** `git worktree add -b usf/<job-id> <worktree> <base>`, with `<worktree>` = `$(cd .. && pwd)/<name>-usf/<job-id>`. Run the fresh-checkout setup from `AGENTS.md` in the worktree. If it fails, stop and tell the user.
3. **Spec.** Spawn `usf-spec-writer` with `<paths> Item: <item, verbatim>. Requirements: <IDs or none>.` Check that `spec.md` exists and starts with `# `.
4. **Build.** Set `stage: "build"`. Spawn `usf-builder` **named `builder-<job-id>`** with `<paths> Build round 1. Port: <port>.` Then go to **Build check**.

### Build check

First line of `build.md`: `STATUS: READY` → next review round. `STATUS: BLOCKED` → **Needs human**. Anything else → stop and tell the user.

### Review round N

1. Set `stage: "review"`, `round: N`, all reviews `pending`. Create `round-<N>/`.
2. Spawn all four reviewers **in one message** so they run in parallel, each with `<paths> Review round N.` plus its port where it has one.
3. **Wait for all.** As each finishes, read the first line of its file and write the verdict into `job.json` at once. The round is done only when all four files exist. A missing file or a first line that is not `VERDICT: PASS` / `VERDICT: CHANGES` is a protocol failure: stop and tell the user.
4. Decide:
   - **All PASS** → **Approval**.
   - **Any CHANGES and N < max_rounds** → set `stage: "build"` and resume the builder with `SendMessage` to `builder-<job-id>`: `Round N reviews are in usf/jobs/<job-id>/round-<N>/. Address every review with VERDICT: CHANGES, commit, and update build.md for round N+1.` Then **Build check**.
   - **Any CHANGES and N = max_rounds** → write `decision.md` yourself: `ESCALATE`, a blank line, then `Review rounds exhausted. Outstanding CHANGES in round-<N>/ from: <lenses>.` → **Needs human**.

### Approval

Set `stage: "approve"`. Spawn `usf-approver` with `<paths> Final round: N.` First line of `decision.md`: `APPROVE` → **Merge**; `ESCALATE` → **Needs human**.

### Merge

The main checkout must be clean (`git status --porcelain -- . ':!usf/backlog.md'` prints nothing) and on `<base>`. If not, set `stage: "needs-human"` and tell the user the job is approved but the checkout is busy; they run `/usf-loop approve <job-id>` when it is clean. Otherwise:

```bash
git merge --no-ff usf/<job-id> -m "Merge usf/<job-id>: <spec title>"
git worktree remove <worktree>
git branch -d usf/<job-id>
```

Set `stage: "merged"`. If the merge fails, `git merge --abort`, set `stage: "needs-human"`, and say why. If worktree removal fails the job is still merged; report the error. **Never push, deploy, or release** — that is workflow 07 and needs its own approvals.

### Needs human

Set `stage: "needs-human"`. Keep the branch and worktree. Tell the user the job id, the worktree path, and quote `decision.md` (or the `## Blocked` section of `build.md`).

## /usf-loop next

Take the first `- [ ]` line in `usf/backlog.md`. Claim it with one Edit replacing that exact line with `- [x] <item> → claimed`; if the Edit fails, another session claimed it, so re-read and take the next. None left → say so. Run `/usf-loop <item>` and, once the job id exists, replace `claimed` with it. Requirement IDs written on the backlog line as `[REQ-014]` are passed through.

## /usf-loop approve <job-id>

Job must be `needs-human`. The user is accepting the escalation: append `Approved by human on <UTC date>.` to `decision.md` under a `## Human approval` heading, then run **Merge**.

## /usf-loop rework <job-id> <note>

Job must be `needs-human`. Write the note verbatim to `rework-<k>.md` (next unused `k`), set `stage: "build"`, spawn a fresh `usf-builder` named `builder-<job-id>` with `<paths> Rework: read rework-<k>.md and address it, then update build.md for round N+1. Port: <port>.` (`N` = last round). The rework run gets a fresh round budget: set `max_rounds` to `N + 3`. Continue from **Build check**.

## /usf-loop status

Print one line per job in `usf/jobs/`: id, stage, round, and the current review verdicts. Point the user to the dashboard (`cd usf && python -m http.server 8000`, then open `http://localhost:8000/dashboard.html`).

## Reporting

One short line per transition, e.g. `007-export-csv: round 2 — code CHANGES, security/ux-ui/docs PASS → resuming builder`. When the job ends, say whether it merged or needs a human, and why. If `usf/validate_job.py` exists, run `python usf/validate_job.py usf/jobs/<job-id>` and report any contract errors.
