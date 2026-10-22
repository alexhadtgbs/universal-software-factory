"""Validate USF delivery-loop job folders against the workflow 09 artifact contract.

Usage:
    python validate_job.py <job-folder> [<job-folder> ...]
    python validate_job.py <jobs-dir>          # validates every job folder inside
"""
from pathlib import Path
import json
import re
import sys

STAGES = {"spec", "build", "review", "approve", "merged", "needs-human"}
LENSES = ("security", "code", "ux-ui", "docs")
REVIEW_VALUES = {"pending", "PASS", "CHANGES"}
REQUIRED_KEYS = {"id", "item", "branch", "worktree", "stage", "round", "max_rounds", "reviews"}
# Files that must exist once a job has reached a stage.
STAGE_ORDER = ["spec", "build", "review", "approve"]


def first_line(path):
    with path.open(encoding="utf-8") as f:
        return f.readline().rstrip("\r\n")


def check_job(folder):
    errors = []
    job_file = folder / "job.json"
    if not job_file.is_file():
        return ["job.json is missing"]
    try:
        job = json.loads(job_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"job.json is not valid JSON: {e}"]

    missing = REQUIRED_KEYS - job.keys()
    if missing:
        errors.append("job.json missing keys: " + ", ".join(sorted(missing)))
    if job.get("id") != folder.name:
        errors.append(f"job.json id {job.get('id')!r} does not match folder {folder.name!r}")
    stage = job.get("stage")
    if stage not in STAGES:
        errors.append(f"unknown stage {stage!r}")
    rnd, max_rounds = job.get("round"), job.get("max_rounds")
    if not isinstance(rnd, int) or rnd < 0:
        errors.append(f"round must be a non-negative integer, got {rnd!r}")
        rnd = None
    if not isinstance(max_rounds, int) or max_rounds < 1:
        errors.append(f"max_rounds must be a positive integer, got {max_rounds!r}")
    elif rnd is not None and rnd > max_rounds:
        errors.append(f"round {rnd} exceeds max_rounds {max_rounds}")
    reviews = job.get("reviews", {})
    if not isinstance(reviews, dict) or set(reviews) != set(LENSES):
        errors.append(f"reviews must have exactly the lenses {', '.join(LENSES)}")
        reviews = {}
    for lens, value in reviews.items():
        if value not in REVIEW_VALUES:
            errors.append(f"reviews.{lens} has invalid value {value!r}")
    worktree = job.get("worktree", "")
    if worktree and not (worktree.startswith("/") or re.match(r"^[A-Za-z]:[\\/]", worktree)):
        errors.append("worktree must be an absolute path")

    # Artifacts implied by the stage.
    reached = STAGE_ORDER.index(stage) if stage in STAGE_ORDER else len(STAGE_ORDER)
    spec = folder / "spec.md"
    if spec.is_file():
        if not first_line(spec).startswith("# "):
            errors.append("spec.md must start with '# <title>'")
    elif reached >= 1:
        errors.append(f"spec.md is missing at stage {stage!r}")

    build = folder / "build.md"
    if build.is_file():
        if first_line(build) not in ("STATUS: READY", "STATUS: BLOCKED"):
            errors.append("build.md first line must be 'STATUS: READY' or 'STATUS: BLOCKED'")
    elif reached >= 2:
        errors.append(f"build.md is missing at stage {stage!r}")

    # Review rounds.
    for n in range(1, (rnd or 0) + 1):
        rdir = folder / f"round-{n}"
        current = n == rnd
        for lens in LENSES:
            f = rdir / f"review-{lens}.md"
            if not f.is_file():
                if not (current and stage == "review" and reviews.get(lens) == "pending"):
                    errors.append(f"round-{n}/review-{lens}.md is missing")
                continue
            line = first_line(f)
            if line not in ("VERDICT: PASS", "VERDICT: CHANGES"):
                errors.append(f"round-{n}/review-{lens}.md first line must be a VERDICT")
            elif current and reviews.get(lens) not in ("pending", line.split(": ")[1]):
                errors.append(f"job.json reviews.{lens} disagrees with round-{n}/review-{lens}.md")

    # Terminal stages.
    decision = folder / "decision.md"
    verdict = first_line(decision) if decision.is_file() else None
    if verdict is not None and verdict not in ("APPROVE", "ESCALATE"):
        errors.append("decision.md first line must be 'APPROVE' or 'ESCALATE'")
    if stage == "merged":
        human_ok = decision.is_file() and "## Human approval" in decision.read_text(encoding="utf-8")
        if verdict != "APPROVE" and not human_ok:
            errors.append("merged job needs decision.md APPROVE or a '## Human approval' section")
        if rnd and any(v != "PASS" for v in reviews.values()) and not human_ok:
            errors.append("merged without human approval but final reviews are not all PASS")
    if stage == "needs-human":
        blocked = build.is_file() and first_line(build) == "STATUS: BLOCKED"
        if verdict is None and not blocked:
            errors.append("needs-human job needs decision.md or a BLOCKED build.md")
    return errors


def job_folders(paths):
    for p in paths:
        p = Path(p)
        if (p / "job.json").is_file():
            yield p
        elif p.is_dir():
            yield from sorted(c for c in p.iterdir() if c.is_dir())
        else:
            yield p


def main(argv):
    if not argv:
        print(__doc__.strip())
        return 2
    failed = 0
    for folder in job_folders(argv):
        errors = check_job(folder) if folder.is_dir() else ["not a directory"]
        if errors:
            failed += 1
            print(f"FAIL {folder}")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"OK   {folder}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
