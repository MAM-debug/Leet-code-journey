from __future__ import annotations

import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
SOLUTIONS_ROOT = ROOT / "solutions"
VALID_EXTENSIONS = {".cpp": "C++"}


def parse_metadata(text: str) -> Dict[str, str]:
    metadata: Dict[str, str] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("@") or ":" not in line:
            continue
        key, value = line[1:].split(":", 1)
        metadata[key.strip().lower()] = value.strip()
    return metadata


def extract_solutions() -> List[Dict[str, str]]:
    items: List[Dict[str, str]] = []
    if not SOLUTIONS_ROOT.exists():
        return items

    # Check root solutions folder for files (flat structure)
    for file_path in SOLUTIONS_ROOT.glob("*.cpp"):
        if file_path.is_file():
            text = file_path.read_text(encoding="utf-8")
            md = parse_metadata(text)

            if "date" not in md or "problem" not in md or "leetcode" not in md:
                continue

            language = md.get("language", VALID_EXTENSIONS[file_path.suffix.lower()])
            difficulty = md.get("difficulty", "Unknown")
            tags = md.get("tags", "")

            items.append(
                {
                    "date": md["date"],
                    "problem": md["problem"],
                    "difficulty": difficulty,
                    "language": language,
                    "leetcode": md["leetcode"],
                    "tags": tags,
                    "path": str(file_path.relative_to(ROOT)).replace("\\", "/"),
                }
            )

    # Check year subdirectories (nested structure)
    for year_dir in sorted(SOLUTIONS_ROOT.glob("[0-9][0-9][0-9][0-9]")):
        if not year_dir.is_dir():
            continue
        for file_path in year_dir.rglob("*"):
            if not file_path.is_file() or file_path.suffix.lower() not in VALID_EXTENSIONS:
                continue

            text = file_path.read_text(encoding="utf-8")
            md = parse_metadata(text)

            if "date" not in md or "problem" not in md or "leetcode" not in md:
                continue

            language = md.get("language", VALID_EXTENSIONS[file_path.suffix.lower()])
            difficulty = md.get("difficulty", "Unknown")
            tags = md.get("tags", "")

            items.append(
                {
                    "date": md["date"],
                    "problem": md["problem"],
                    "difficulty": difficulty,
                    "language": language,
                    "leetcode": md["leetcode"],
                    "tags": tags,
                    "path": str(file_path.relative_to(ROOT)).replace("\\", "/"),
                }
            )

    def sort_key(item: Dict[str, str]) -> str:
        return item["date"]

    return sorted(items, key=sort_key, reverse=True)


def replace_section(content: str, start: str, end: str, new_body: str) -> str:
    pattern = re.compile(
        rf"({re.escape(start)}\r?\n)(.*?)(\r?\n{re.escape(end)})",
        re.DOTALL,
    )
    replacement = rf"\1{new_body}\3"
    updated, count = pattern.subn(replacement, content)
    if count == 0:
        raise RuntimeError(f"Missing marker section: {start} ... {end}")
    return updated


def build_table_rows(solutions: List[Dict[str, str]]) -> str:
    if not solutions:
        return ""

    rows = []
    for item in solutions:
        rows.append(
            "| {date} | {problem} | {difficulty} | {language} | [LeetCode]({leetcode}) |".format(
                date=item["date"],
                problem=item["problem"],
                difficulty=item["difficulty"],
                language=item["language"],
                leetcode=item["leetcode"],
            )
        )
    return "\n".join(rows)


def build_stats(solutions: List[Dict[str, str]]) -> str:
    total = len(solutions)
    difficulty_counter = Counter(item["difficulty"].title() for item in solutions)

    tag_counter: Counter[str] = Counter()
    for item in solutions:
        for tag in [t.strip() for t in item["tags"].split(",") if t.strip()]:
            tag_counter[tag] += 1

    top_tags = ", ".join(f"{tag} ({count})" for tag, count in tag_counter.most_common(6))
    if not top_tags:
        top_tags = "None"

    now_utc = "N/A" if total == 0 else datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")

    lines = [
        f"- Total Solved: {total}",
        f"- Easy: {difficulty_counter.get('Easy', 0)}",
        f"- Medium: {difficulty_counter.get('Medium', 0)}",
        f"- Hard: {difficulty_counter.get('Hard', 0)}",
        f"- Top Tags: {top_tags}",
        f"- Last Updated (UTC): {now_utc}",
    ]
    return "\n".join(lines)


def build_badge(total: int) -> str:
    return (
        '<img src="https://img.shields.io/badge/Total%20Solved-'
        f'{total}-blue?style=flat-square" alt="Total Solved" />'
    )


def main() -> None:
    solutions = extract_solutions()
    readme = README_PATH.read_text(encoding="utf-8")

    readme = replace_section(
        readme,
        "<!-- PROBLEM_TABLE_START -->",
        "<!-- PROBLEM_TABLE_END -->",
        build_table_rows(solutions),
    )
    readme = replace_section(
        readme,
        "<!-- STATS_START -->",
        "<!-- STATS_END -->",
        build_stats(solutions),
    )
    readme = replace_section(
        readme,
        "<!-- TOTAL_SOLVED_BADGE_START -->",
        "<!-- TOTAL_SOLVED_BADGE_END -->",
        build_badge(len(solutions)),
    )

    README_PATH.write_text(readme, encoding="utf-8")
    print(f"README updated with {len(solutions)} solutions.")


if __name__ == "__main__":
    main()
