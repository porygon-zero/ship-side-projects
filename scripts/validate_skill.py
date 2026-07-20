#!/usr/bin/env python3
"""Validate the distributable Ship Side Projects skill using the standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "ship-side-projects"
SKILL_FILE = SKILL_DIR / "SKILL.md"
LOCAL_LINK = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def validate_frontmatter(errors: list[str]) -> None:
    if not SKILL_FILE.is_file():
        fail(f"Missing required file: {SKILL_FILE.relative_to(ROOT)}", errors)
        return

    text = SKILL_FILE.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter", errors)
        return

    frontmatter = match.group(1)
    keys = [line.split(":", 1)[0].strip() for line in frontmatter.splitlines() if ":" in line]
    if keys != ["name", "description"]:
        fail("SKILL.md frontmatter must contain only name and description", errors)

    name_match = re.search(r"^name:\s*['\"]?([^'\"\n]+)", frontmatter, re.MULTILINE)
    if not name_match:
        fail("SKILL.md frontmatter is missing name", errors)
    else:
        name = name_match.group(1).strip()
        if name != SKILL_DIR.name:
            fail(f"Skill name '{name}' must match directory '{SKILL_DIR.name}'", errors)
        if not re.fullmatch(r"[a-z0-9-]{1,63}", name):
            fail(f"Invalid skill name: {name}", errors)

    description_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    if not description_match or not description_match.group(1).strip(" '\""):
        fail("SKILL.md frontmatter is missing a non-empty description", errors)


def validate_links(errors: list[str]) -> None:
    for markdown in sorted(SKILL_DIR.rglob("*.md")):
        text = markdown.read_text(encoding="utf-8")
        for target in LOCAL_LINK.findall(text):
            clean_target = target.split("#", 1)[0]
            if clean_target and not (markdown.parent / clean_target).resolve().exists():
                fail(
                    f"Broken local link in {markdown.relative_to(ROOT)}: {target}",
                    errors,
                )


def validate_interface(errors: list[str]) -> None:
    interface = SKILL_DIR / "agents" / "openai.yaml"
    if not interface.is_file():
        fail("Missing recommended agents/openai.yaml", errors)
        return
    text = interface.read_text(encoding="utf-8")
    for key in ("display_name", "short_description", "default_prompt"):
        if not re.search(rf"^\s+{key}:\s+\".+\"$", text, re.MULTILINE):
            fail(f"agents/openai.yaml is missing quoted {key}", errors)
    if "$ship-side-projects" not in text:
        fail("agents/openai.yaml default_prompt must mention $ship-side-projects", errors)


def main() -> int:
    errors: list[str] = []
    validate_frontmatter(errors)
    validate_links(errors)
    validate_interface(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Skill validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

