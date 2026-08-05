#!/usr/bin/env python3
"""Builds powerbi-onboarding-coach-single.md: the whole skill as one Markdown
file for AI tools without skill support (M365 Copilot agents, ChatGPT projects,
corporate chatbots, or any chat that accepts a file attachment).

Run from the repo root:  python scripts/build_single_file.py
Re-run after every change to SKILL.md, references/ or assets/.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "powerbi-onboarding-coach-single.md"

ORDER = [
    "references/data-profiling.md",
    "references/module-1-foundations.md",
    "references/module-2-modeling-dax.md",
    "references/module-3-visualization-ibcs.md",
    "references/module-4-service-sharing.md",
    "references/progress-and-gamification.md",
    "references/resources.md",
]

PREAMBLE = """\
# Power BI Onboarding Coach · single-file edition

This is the all-in-one edition of
https://github.com/Losveratos/powerbi-onboarding-coach for AI tools without
skill support: Microsoft 365 Copilot agents, ChatGPT projects, corporate
chatbots, or any chat where you can attach or paste a file.

**How to use (human):** start a new chat, attach this file together with a
CSV or Excel file from your own work, and write:
*"Act as my Power BI coach. Follow the instructions in this file."*

**Note for the AI reading this:** this document bundles a multi-file skill.
Wherever the instructions below say to read a file from `references/` or
`assets/`, use the matching `FILE:` section of this document instead. If you
cannot write files to disk, follow the chat-only fallbacks described in the
instructions: keep progress in the conversation and offer the progress file
and HTML tracker as downloadable files or copy-paste blocks at milestones.

---
"""


def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.DOTALL)


def section(path: str, body: str) -> str:
    return f"\n\n---\n\n**FILE: `{path}`**\n\n{body.strip()}\n"


def main() -> None:
    parts = [PREAMBLE]
    skill = strip_frontmatter((ROOT / "SKILL.md").read_text(encoding="utf-8"))
    parts.append(skill.strip() + "\n")
    for rel in ORDER:
        parts.append(section(rel, (ROOT / rel).read_text(encoding="utf-8")))

    tracker = (ROOT / "assets/progress-tracker.html").read_text(encoding="utf-8")
    parts.append(
        "\n\n---\n\n**FILE: `assets/progress-tracker.html`** (template for the"
        " progress page; replace `/*PROGRESS_DATA*/null` with the current"
        " progress JSON and hand the result to the user as"
        " `my-powerbi-progress.html`)\n\n"
        "```html\n" + tracker.strip() + "\n```\n"
    )

    OUT.write_text("".join(parts), encoding="utf-8", newline="\n")
    print(f"OK {OUT.name}: {OUT.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
