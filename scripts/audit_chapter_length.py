#!/usr/bin/env python3
"""Report per-chapter narrative body word counts without modifying source files.

Usage:
    python scripts/audit_chapter_length.py
    python scripts/audit_chapter_length.py --min-words 10000 --json editorial/length-report.json

Counts whitespace-delimited body words and excludes chapter headings, scene
separators and Markdown comments. This is a mechanical gate, NOT prose QA.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

CHAPTER_PATTERN = re.compile(r"^(\d{3})-.*\.md$")


def body_word_count(path: Path) -> int:
    text = path.read_text(encoding="utf-8-sig")
    body_lines: list[str] = []
    inside_comment = False
    for line in text.splitlines():
        trimmed = line.strip()
        if "<!--" in trimmed:
            inside_comment = True
        if not inside_comment and not trimmed.startswith("#") and trimmed not in ("---", "***"):
            body_lines.append(line)
        if "-->" in trimmed:
            inside_comment = False
    return len(" ".join(body_lines).split())


def audit(directory: Path, min_words: int) -> dict:
    if not directory.is_dir():
        raise FileNotFoundError(f"Chapter directory not found: {directory}")
    records = []
    for path in sorted(directory.glob("*.md")):
        match = CHAPTER_PATTERN.match(path.name)
        if match is None:
            continue
        number = int(match.group(1))
        count = body_word_count(path)
        records.append(
            {
                "chapter": number,
                "path": str(path.as_posix()),
                "body_words": count,
                "words_missing": max(0, min_words - count),
                "passes": count >= min_words,
            }
        )
    present = {row["chapter"] for row in records}
    holes = [n for n in range(1, max(present, default=0) + 1) if n not in present]
    return {
        "minimum": min_words,
        "chapter_count": len(records),
        "passing": sum(row["passes"] for row in records),
        "failing": sum(not row["passes"] for row in records),
        "total_words_missing": sum(row["words_missing"] for row in records),
        "missing_chapter_numbers": holes,
        "chapters": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, default=Path(__file__).resolve().parents[1] / "chapters")
    parser.add_argument("--min-words", type=int, default=10_000)
    parser.add_argument("--json", dest="json_path", type=Path)
    args = parser.parse_args()
    if args.min_words <= 0:
        parser.error("--min-words must be positive")
    result = audit(args.directory, args.min_words)
    print(f"Chapter length audit: {result['passing']}/{result['chapter_count']} pass {args.min_words:,} body words")
    print(f"Shortfall across failing chapters: {result['total_words_missing']:,} words")
    for row in result["chapters"]:
        shortfall = f" ({row['words_missing']:,} short)" if not row["passes"] else ""
        verdict = "PASS" if row["passes"] else "FAIL"
        print(f"{row['chapter']:03d}  {row['body_words']:>7,} words  {verdict}{shortfall}")
    if result["missing_chapter_numbers"]:
        print("Missing chapters:", result["missing_chapter_numbers"])
    if args.json_path:
        args.json_path.parent.mkdir(parents=True, exist_ok=True)
        args.json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return 0 if result["failing"] == 0 and not result["missing_chapter_numbers"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
