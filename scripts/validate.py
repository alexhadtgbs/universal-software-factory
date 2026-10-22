"""Validate the USF package structure and version consistency."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = "skills/universal-software-factory/SKILL.md"

# Artifacts introduced by each release; later releases must still ship them.
ARTIFACTS = {
    "0.1.0": [
        "VERSION",
        "README.md",
        SKILL,
        "adapters/AGENTS.md",
        "adapters/CLAUDE.md",
        "adapters/cursor-usf-core.mdc",
        "adapters/generic.md",
        "workflows/04-engineering-plan.md",
        "workflows/05-implementation-and-quality.md",
        "quality/definition-of-done.md",
        "docs/system-overview.md",
        "docs/version-history.md",
    ],
    "0.2.0": [
        "workflows/01-product-discovery.md",
        "workflows/02-prd-and-backlog.md",
        "workflows/03-product-and-architecture-decisions.md",
        "templates/product-brief.md",
        "templates/prd.md",
        "templates/product-decision-record.md",
        "templates/architecture-decision-record.md",
        "templates/traceability-matrix.md",
        "docs/roles-and-responsibilities.md",
        "docs/usf-product-roadmap.md",
    ],
    "0.3.0": [
        "workflows/04-technology-stack-assessment.md",
        "templates/technology-decision-record.md",
        "docs/technology-research-standards.md",
    ],
    "0.4.0": [
        "workflows/05-security-review-and-ethical-hacking.md",
        "templates/security-review-report.md",
        "docs/security-baseline.md",
    ],
    "0.5.0": [
        "workflows/06-ux-ui-design-and-validation.md",
        "templates/ux-ui-design-brief.md",
        "docs/ux-ui-design-principles.md",
    ],
    "0.6.0": [
        "workflows/07-delivery-ci-cd-and-release.md",
        "docs/documentation-and-evidence-standard.md",
        "docs/ci-cd-pipeline-template.md",
        "templates/engineering-activity-log.md",
        "templates/test-plan-and-report.md",
        "templates/release-record.md",
        "templates/incident-postmortem.md",
    ],
    "0.7.0": [
        "workflows/08-quality-assurance-and-documentation-validation.md",
        "docs/quality-assurance-and-documentation-acceptance.md",
        "templates/documentation-inventory.md",
        "templates/documentation-validation-report.md",
    ],
    "0.8.0": [
        "workflows/09-agentic-delivery-loop.md",
        "templates/job-spec.md",
        "templates/build-report.md",
        "templates/review-report.md",
        "templates/approval-decision.md",
        "scripts/validate_job.py",
        "adapters/claude-code/README.md",
        "adapters/claude-code/.claude/skills/usf-loop/SKILL.md",
        "adapters/claude-code/.claude/agents/usf-spec-writer.md",
        "adapters/claude-code/.claude/agents/usf-builder.md",
        "adapters/claude-code/.claude/agents/usf-reviewer-security.md",
        "adapters/claude-code/.claude/agents/usf-reviewer-code.md",
        "adapters/claude-code/.claude/agents/usf-reviewer-ux-ui.md",
        "adapters/claude-code/.claude/agents/usf-reviewer-docs.md",
        "adapters/claude-code/.claude/agents/usf-approver.md",
        "adapters/claude-code/usf/backlog.md",
        "adapters/claude-code/usf/dashboard.html",
    ],
    "0.8.1": [
        "adapters/claude-code/README.md",
    ],
    "0.8.2": [
        "adapters/claude-code/usf/dashboard.html",
    ],
}

# Key policy statements the skill must keep.
SKILL_PHRASES = [
    "MUST NOT prescribe a product form factor",
    "microservices",
    "Technology Stack Advisor",
    "Security Reviewer / Ethical Hacker",
    "UX/UI Design",
    "Continuous documentation and delivery evidence",
    "Quality assurance and documentation validation",
    "Agentic delivery loop",
]


def vkey(v):
    return tuple(int(x) for x in v.split("."))


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def main():
    errors = []

    if not (ROOT / "VERSION").is_file():
        print("FAIL: VERSION file is missing")
        return 1
    version = read("VERSION").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        print(f"FAIL: VERSION is not semantic (x.y.z): {version!r}")
        return 1
    if version not in ARTIFACTS:
        errors.append(f"VERSION {version} has no artifact list in validate.py")

    # Required files for this and all earlier releases.
    for release, paths in ARTIFACTS.items():
        if vkey(release) > vkey(version):
            continue
        missing = [p for p in paths if not (ROOT / p).is_file()]
        if missing:
            errors.append(f"Missing {release} artifacts: " + ", ".join(missing))
        else:
            print(f"OK  {release} artifacts ({len(paths)} files)")

    # Version labels must agree with VERSION.
    if (ROOT / "README.md").is_file():
        m = re.search(r"\bv(\d+\.\d+\.\d+)", read("README.md").splitlines()[0])
        if not m or m.group(1) != version:
            errors.append(f"README.md title version must be v{version}")
    if (ROOT / SKILL).is_file():
        skill = read(SKILL)
        m = re.search(r"^---\s*\n(.*?)\n---", skill, re.S)
        sv = re.search(r"^version:\s*(\S+)\s*$", m.group(1) if m else "", re.M)
        if not sv or sv.group(1) != version:
            errors.append(f"{SKILL} frontmatter version must be {version}")
        for phrase in SKILL_PHRASES:
            if phrase not in skill:
                errors.append(f"{SKILL} is missing required text: {phrase!r}")
    if (ROOT / "docs/version-history.md").is_file():
        entries = re.findall(r"^## (\d+\.\d+\.\d+)", read("docs/version-history.md"), re.M)
        if not entries or entries[0] != version:
            errors.append(f"docs/version-history.md must list {version} first")
        if entries != sorted(entries, key=vkey, reverse=True):
            errors.append("docs/version-history.md entries must be newest first")

    if errors:
        print("\nValidation FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"\nUSF {version} validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
