#!/usr/bin/env python3
"""Check chapter file numbering, index order, title headings and UTF-8 text."""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

INDEX_ENTRY = re.compile(r"^- \*\*(\d{3})\.\*\* \[([^\]]+)\]\((chapters/[^)]+\.md)\)$", re.MULTILINE)
CHAPTER_HEADING = re.compile(r"^## Chapter\s+0*(\d+):\s*(.+?)\s*$", re.MULTILINE)
CHAPTER_FILE = re.compile(r"^(\d{3})-.+\.md$")


def audit(root: Path) -> dict:
    index_text = (root / "CHAPTER_INDEX.md").read_text(encoding="utf-8")
    indexed = [
        {"number": int(number), "title": title, "path": rel}
        for number, title, rel in INDEX_ENTRY.findall(index_text)
    ]
    actual = sorted((root / "chapters").glob("*.md"))
    by_number: dict[int, list[Path]] = defaultdict(list)
    for path in actual:
        match = CHAPTER_FILE.match(path.name)
        if match:
            by_number[int(match.group(1))].append(path)

    indexed_numbers = [row["number"] for row in indexed]
    actual_numbers = [number for number, paths in by_number.items() for _ in paths]
    highest_number = max([193, *indexed_numbers, *actual_numbers])
    expected = list(range(1, highest_number + 1))
    indexed_paths = {row["path"] for row in indexed}
    actual_paths = {path.relative_to(root).as_posix() for path in actual if CHAPTER_FILE.match(path.name)}
    headings = []
    decode_errors = []
    replacement_glyphs = []
    pov_headers = []
    for row in indexed:
        path = root / row["path"]
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as error:
            decode_errors.append({"path": row["path"], "error": str(error)})
            continue
        if "\ufffd" in text:
            replacement_glyphs.append(row["path"])
        matches = CHAPTER_HEADING.findall(text)
        headings.append({
            "number": row["number"],
            "path": row["path"],
            "expected_title": row["title"],
            "headings": [{"number": int(number), "title": title} for number, title in matches],
        })
        for line_number, line in enumerate(text.splitlines(), 1):
            if re.match(r"^#{2,6}\s*POV\s*:", line, re.IGNORECASE):
                pov_headers.append({"path": row["path"], "line": line_number, "text": line.strip()})

    mismatches = []
    for item in headings:
        if len(item["headings"]) != 1:
            mismatches.append({"path": item["path"], "issue": f"expected one chapter heading, found {len(item['headings'])}"})
            continue
        heading = item["headings"][0]
        if heading["number"] != item["number"] or heading["title"] != item["expected_title"]:
            mismatches.append({"path": item["path"], "index_title": item["expected_title"], "heading": heading})

    return {
        "indexed_chapters": len(indexed),
        "actual_numbered_chapter_files": len(actual_paths),
        "expected_chapters": highest_number,
        "index_sequence_is_contiguous": indexed_numbers == expected,
        "missing_index_numbers": sorted(set(expected) - set(indexed_numbers)),
        "duplicate_index_numbers": sorted(number for number in set(indexed_numbers) if indexed_numbers.count(number) > 1),
        "duplicate_file_numbers": {str(number): [path.name for path in paths] for number, paths in by_number.items() if len(paths) > 1},
        "unindexed_chapter_files": sorted(actual_paths - indexed_paths),
        "indexed_paths_missing_on_disk": sorted(row["path"] for row in indexed if not (root / row["path"]).is_file()),
        "heading_mismatches": mismatches,
        "utf8_decode_errors": decode_errors,
        "replacement_glyph_files": replacement_glyphs,
        "pov_heading_candidates": pov_headers,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = audit(args.root)
    rendered = json.dumps(result, indent=2, ensure_ascii=False)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered + "\n", encoding="utf-8")
    print(f"Index entries: {result['indexed_chapters']}; numbered files: {result['actual_numbered_chapter_files']}")
    print(f"Ordered 001–{result['expected_chapters']:03d}: {result['index_sequence_is_contiguous']}")
    for key in (
        "missing_index_numbers", "duplicate_index_numbers", "duplicate_file_numbers",
        "unindexed_chapter_files", "indexed_paths_missing_on_disk", "heading_mismatches",
        "utf8_decode_errors", "replacement_glyph_files", "pov_heading_candidates",
    ):
        value = result[key]
        if value:
            print(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    return 0 if (
        result["indexed_chapters"] == result["expected_chapters"]
        and result["actual_numbered_chapter_files"] == result["expected_chapters"]
        and result["index_sequence_is_contiguous"]
        and not any(result[key] for key in (
            "missing_index_numbers", "duplicate_index_numbers", "duplicate_file_numbers",
            "unindexed_chapter_files", "indexed_paths_missing_on_disk", "heading_mismatches",
            "utf8_decode_errors", "replacement_glyph_files",
        ))
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())
