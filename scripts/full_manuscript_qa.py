#!/usr/bin/env python3
"""Reproducible full-manuscript mechanical audit, not a semantic editorial signoff.

All 300-token sliding windows are checked, with exact comparison on hash matches.
Body words exclude Markdown headings, dividers and comments like audit_chapter_length.py.
Usage: python3 scripts/full_manuscript_qa.py --json editorial/audits/latest-qa.json
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r"^(\d{3})-.*\.md$")
WINDOW = 300
MASK = (1 << 64) - 1
BASE = 257
AGE_RE = re.compile(
    r"\b(?:Percy|Annabeth|Thalia|Clarisse|Silena|Rhys|Jason)\b.{0,90}"
    r"\b(?:was|is|turned|turning|already)\s+(?:twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|\d{1,2})\b",
    re.IGNORECASE,
)
DISCLOSURE_RE = re.compile(
    r"(?:Amphitrite|Thalia|Clarisse|Silena).{0,90}"
    r"(?:erased future|previous life|life you remember|years you cannot remember|missing years)"
    r"|(?:erased future|previous life|life you remember|years you cannot remember|missing years)"
    r".{0,90}(?:Amphitrite|Thalia|Clarisse|Silena)",
    re.IGNORECASE,
)


def body_lines(text: str) -> list[tuple[int, str]]:
    result = []
    inside_comment = False
    for n, line in enumerate(text.splitlines(), 1):
        trimmed = line.strip()
        # Count only text outside HTML comments; this agrees with the length audit
        # for the manuscript's full-line comments.
        if "<!--" in trimmed:
            inside_comment = True
        if not inside_comment and not trimmed.startswith("#") and trimmed not in ("---", "***"):
            result.append((n, line))
        if "-->" in trimmed:
            inside_comment = False
    return result


def audit(root: Path, minimum: int = 10000) -> dict:
    chapter_dir = root / "chapters"
    files = sorted((p for p in chapter_dir.glob("*.md") if PATTERN.fullmatch(p.name)),
                   key=lambda p: int(PATTERN.fullmatch(p.name).group(1)))
    chapters = {}
    highest_chapter = max(
        (int(PATTERN.fullmatch(path.name).group(1)) for path in files), default=0
    )
    report = {
        "scope": f"Chapters 001–{highest_chapter:03d}; bonus interludes excluded",
        "threshold": minimum, "expected_chapters": highest_chapter,
        "count_method": "whitespace-separated body tokens; headings/dividers/comments excluded",
        "duplicate_method": "all consecutive 300-token windows, rolling 64-bit hash + exact token comparison",
        "chapter_count": len(files),
        "missing_chapters": [],
        "errors": [],
        "chapters": [],
        "300_word_cross_chapter_matches": [],
        "matched_window_count": 0,
        "window_comparisons": 0,
        "human_only_gates": ["character-local witnessed knowledge", "POV stability",
            "chronology and cause-effect", "semantic scene repetition", "dialogue authenticity",
            "prose pacing", "no padding", "prior/following chapter handoff"],
    }
    for path in files:
        number = int(PATTERN.fullmatch(path.name).group(1))
        if number in chapters:
            report["errors"].append("Repeated chapter number: " + str(number))
            continue
        try:
            text = path.read_text(encoding="utf-8-sig")
        except UnicodeError as exc:
            report["errors"].append(f"{path.name}: invalid UTF-8: {exc}")
            continue
        if "\ufffd" in text:
            report["errors"].append(f"{path.name}: replacement character found")
        lines = body_lines(text)
        words = [w for _, line in lines for w in line.split()]
        chapters[number] = (path, words)
        age_cues = [
            {"line": lineno, "text": line.strip()[:250]}
            for lineno, line in lines if AGE_RE.search(line)
        ][:25]
        secret_cues = [
            {"line": lineno, "text": line.strip()[:250]}
            for lineno, line in lines if DISCLOSURE_RE.search(line)
        ][:25]
        prose_paragraphs = [len(line.split()) for _, line in lines if line.strip()
                             and not line.lstrip().startswith((">", "|"))]
        report["chapters"].append({
            "chapter": number, "path": str(path.relative_to(root)),
            "body_words": len(words), "shortfall": max(0, minimum - len(words)),
            "passes_length": len(words) >= minimum,
            "age_review_cues": age_cues, "possible_knowledge_leak_cues": secret_cues,
            "dialogue_line_ratio": round(
                sum(bool(re.match(r"\s*[\"“']", line)) for _, line in lines) / max(1, len(lines)), 3),
            "median_paragraph_words": sorted(prose_paragraphs)[len(prose_paragraphs)//2] if prose_paragraphs else 0,
        })
        if not words:
            report["errors"].append(f"{path.name}: empty body")

    report["missing_chapters"] = [n for n in range(1, highest_chapter + 1) if n not in chapters]
    report["passing"] = sum(x["passes_length"] for x in report["chapters"])
    report["failing"] = sum(not x["passes_length"] for x in report["chapters"])
    report["total_shortfall"] = sum(x["shortfall"] for x in report["chapters"])

    # Complete cross-chapter exact match check; every offset is considered.
    # A hash is a candidate selector only. Tokens are compared exactly before reporting.
    cache = {}
    def token_hash(token: str) -> int:
        if token not in cache:
            cache[token] = int.from_bytes(hashlib.blake2b(token.encode("utf-8"), digest_size=8).digest(), "big")
        return cache[token]

    previous = {}
    power = pow(BASE, WINDOW - 1, 1 << 64)
    for number in sorted(chapters):
        path, words = chapters[number]
        if len(words) < WINDOW:
            continue
        hashes = [token_hash(t) for t in words]
        rolling = 0
        for v in hashes[:WINDOW]:
            rolling = (rolling * BASE + v) & MASK
        for offset in range(len(words) - WINDOW + 1):
            report["window_comparisons"] += 1
            if offset:
                rolling = ((rolling - hashes[offset-1] * power) * BASE
                           + hashes[offset+WINDOW-1]) & MASK
            prior = previous.get(rolling)
            if prior:
                prior_num, prior_offset = prior
                if prior_num != number:
                    earlier = chapters[prior_num][1]
                    if earlier[prior_offset:prior_offset+WINDOW] == words[offset:offset+WINDOW]:
                        report["matched_window_count"] += 1
                        if len(report["300_word_cross_chapter_matches"]) < 100:
                            report["300_word_cross_chapter_matches"].append({
                                "first_chapter": prior_num, "first_token_offset": prior_offset,
                                "later_chapter": number, "later_token_offset": offset,
                                "first_24_words": " ".join(words[offset:offset+24]),
                            })
                # Within-chapter reuse is not a cross-chapter match. Continue scanning.
            else:
                previous[rolling] = (number, offset)
    report["exact_duplicate_status"] = (
        "REVIEW_REQUIRED" if report["matched_window_count"] else "NO_CROSS_CHAPTER_300_WORD_MATCHES"
    )
    report["editorial_status"] = "NOT_SEMANTICALLY_CERTIFIED"
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", type=Path)
    ap.add_argument("--markdown", type=Path)
    ap.add_argument("--minimum", type=int, default=10000)
    ap.add_argument("--strict-length", action="store_true")
    ap.add_argument("--strict-duplicates", action="store_true")
    args = ap.parse_args()
    result = audit(ROOT, args.minimum)
    print("Chapters: {}/{}; length passing: {}; short: {}; missing body words: {:,}".format(
        result["chapter_count"], result["expected_chapters"], result["passing"],
        result["failing"], result["total_shortfall"]))
    print("300-token windows checked: {:,}; exact cross-chapter matched windows: {:,}".format(
        result["window_comparisons"], result["matched_window_count"]))
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        out = [
            "# Full manuscript mechanical QA",
            "",
            "Machine-generated. Not an editorial certificate; source branch must be recorded by the CI job.",
            "",
            f"- Chapters: {result['chapter_count']} / {result['expected_chapters']}",
            f"- At least {args.minimum:,} body words: {result['passing']} chapters",
            f"- Below minimum: {result['failing']} chapters",
            f"- Total body-word shortfall: {result['total_shortfall']:,}",
            f"- Exact 300-word windows checked: {result['window_comparisons']:,}",
            f"- Cross-chapter matching windows: {result['matched_window_count']:,}",
            f"- Structural errors: {len(result['errors'])}",
            "",
            "| Chapter | Body words | Missing |",
            "|---|---:|---:|",
        ]
        out += [f"| {row['chapter']:03d} | {row['body_words']:,} | {row['shortfall']:,} |"
                for row in result["chapters"]]
        out.extend(["", "## Limits", ""])
        out.extend("- Not verified: " + item for item in result["human_only_gates"])
        args.markdown.write_text("\n".join(out) + "\n", encoding="utf-8")
    for err in result["errors"]:
        print("STRUCTURAL ERROR:", err, file=sys.stderr)
    if result["errors"] or result["missing_chapters"]:
        return 1
    if args.strict_length and result["failing"]:
        return 2
    if args.strict_duplicates and result["matched_window_count"]:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
