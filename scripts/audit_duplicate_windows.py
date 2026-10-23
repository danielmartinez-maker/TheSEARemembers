#!/usr/bin/env python3
"""Find exact repeated body windows of N whitespace-delimited words.

The scan checks every starting offset across numbered chapters and optional
bonus files. Rolling hashes are only an index; every reported match is verified
against the original token IDs.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

MASK = (1 << 64) - 1
BASES = (1_000_003, 1_000_033)


def body_tokens(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8-sig")
    tokens: list[str] = []
    inside_comment = False
    for line in text.splitlines():
        trimmed = line.strip()
        if "<!--" in trimmed:
            inside_comment = True
        if not inside_comment and not trimmed.startswith("#") and trimmed not in ("---", "***"):
            tokens.extend(line.split())
        if "-->" in trimmed:
            inside_comment = False
    return tokens


def rolling_hashes(values: list[int], width: int):
    if len(values) < width:
        return
    powers = tuple(pow(base, width - 1, 1 << 64) for base in BASES)
    hashes = [0, 0]
    for value in values[:width]:
        item = value + 1
        hashes[0] = (hashes[0] * BASES[0] + item) & MASK
        hashes[1] = (hashes[1] * BASES[1] + item) & MASK
    yield 0, (hashes[0], hashes[1])
    for start in range(1, len(values) - width + 1):
        old = values[start - 1] + 1
        new = values[start + width - 1] + 1
        hashes[0] = ((hashes[0] - old * powers[0]) * BASES[0] + new) & MASK
        hashes[1] = ((hashes[1] - old * powers[1]) * BASES[1] + new) & MASK
        yield start, (hashes[0], hashes[1])


def audit(paths: list[Path], width: int) -> dict:
    token_ids: dict[str, int] = {}
    files: list[dict] = []
    for path in paths:
        words = body_tokens(path)
        ids = []
        for word in words:
            ids.append(token_ids.setdefault(word, len(token_ids)))
        files.append({"path": path.as_posix(), "words": words, "ids": ids})

    # Hash -> exact-token representatives. Repeated windows are recorded as
    # offset pairs; any hash collision gets a separate representative.
    seen: dict[tuple[int, int], list[tuple[int, int]]] = {}
    matches: set[tuple[int, int, int, int]] = set()
    windows = 0
    for file_index, record in enumerate(files):
        ids = record["ids"]
        for start, key in rolling_hashes(ids, width):
            windows += 1
            candidates = seen.setdefault(key, [])
            exact = False
            for prior_file, prior_start in candidates:
                prior_ids = files[prior_file]["ids"]
                if ids[start:start + width] == prior_ids[prior_start:prior_start + width]:
                    if (prior_file, prior_start) != (file_index, start):
                        matches.add((prior_file, prior_start, file_index, start))
                    exact = True
                    break
            if not exact:
                candidates.append((file_index, start))

    summaries = []
    for earlier_file, earlier_start, later_file, later_start in sorted(matches):
        summaries.append({
            "earlier": files[earlier_file]["path"],
            "earlier_word_offset": earlier_start,
            "later": files[later_file]["path"],
            "later_word_offset": later_start,
        })
    return {
        "window_words": width,
        "files": len(files),
        "body_words": sum(len(record["words"]) for record in files),
        "windows_checked": windows,
        "exact_matching_windows": len(matches),
        "matches": summaries,
        "method": "dual 64-bit rolling hashes, followed by exact token-ID comparison",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chapters", type=Path, default=Path("chapters"))
    parser.add_argument("--bonus", type=Path, default=Path("bonus"))
    parser.add_argument("--words", type=int, default=300)
    parser.add_argument("--json", type=Path)
    parser.add_argument("--strict-duplicates", action="store_true",
                        help="exit nonzero when any exact matching window is found")
    args = parser.parse_args()
    if args.words <= 0:
        parser.error("--words must be positive")
    paths = sorted(args.chapters.glob("[0-9][0-9][0-9]-*.md"))
    if args.bonus.is_dir():
        paths.extend(sorted(args.bonus.glob("*.md")))
    result = audit(paths, args.words)
    rendered = json.dumps(result, indent=2, ensure_ascii=False)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered + "\n", encoding="utf-8")
    print(f"Files: {result['files']}; body words: {result['body_words']:,}")
    print(f"{result['windows_checked']:,} windows of {args.words} words checked")
    print(f"Exact matching windows: {result['exact_matching_windows']:,}")
    for match in result["matches"]:
        print(json.dumps(match, ensure_ascii=False))
    return 2 if args.strict_duplicates and result["exact_matching_windows"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
