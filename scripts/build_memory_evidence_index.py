#!/usr/bin/env python3
"""Build a chapter-by-chapter *candidate evidence index* for human continuity review.

Do not treat character name occurrences as witnessed meetings or transferred knowledge.
Facts become CONFIRMED only when an editor reads the full surrounding scene and
records witnesses, source, and knowledge boundary in CHARACTER_MEMORY_LEDGER.md.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CHARACTERS = ("Percy", "Annabeth", "Thalia", "Clarisse", "Silena", "Amphitrite",
              "Poseidon", "Triton", "Tyson", "Jason", "Rhys", "Sally", "Beryl",
              "Chiron", "Grover", "Nico", "Luke", "Zeus", "Beckendorf", "Ella", "Leandros", "Ianthe")
EVENT = re.compile(
    r"\b(?:said|asked|told|remembered|promised|gave|handed|read|wrote|"
    r"kissed|hugged|held|met|recognized|admitted|confessed|learned|"
    r"discovered|forgot|warned|whispered|answered|replied|arrived|left|"
    r"returned|knew|understood)\b", re.IGNORECASE
)
SECRECY = re.compile(
    r"\b(?:secret|memory|remember|timeline|past life|previous life|"
    r"missing years|never told|didn't tell|couldn't remember|"
    r"did not know|birth mother|promise)\b", re.IGNORECASE
)


def build() -> list[dict]:
    records = []
    for path in sorted((ROOT / "chapters").glob("[0-9][0-9][0-9]-*.md")):
        num = int(path.name[:3])
        text = path.read_text(encoding="utf-8-sig")
        lines = text.splitlines()
        title = next((line.lstrip("# ").strip() for line in lines if line.startswith("#")), path.stem)
        counts = {name: len(re.findall(r"\b" + re.escape(name) + r"\b", text)) for name in CHARACTERS}
        cue_candidates = []
        disclosure_candidates = []
        for lineno, line in enumerate(lines, 1):
            if line.lstrip().startswith("#") or not line.strip():
                continue
            present = [name for name in CHARACTERS if re.search(r"\b" + re.escape(name) + r"\b", line)]
            if present and EVENT.search(line):
                cue_candidates.append({"line": lineno, "named": present, "excerpt": line.strip()[:240].rstrip()})
            if SECRECY.search(line) and present:
                disclosure_candidates.append({"line": lineno, "named": present, "excerpt": line.strip()[:240].rstrip()})
        # Limited representative anchors per chapter. These are a queue, not a
        # substitute for reading the surrounding paragraphs or entire scene.
        records.append({
            "chapter": num, "path": path.relative_to(ROOT).as_posix(),
            "title": title,
            "name_mentions": {k: v for k, v in counts.items() if v},
            "event_cues_for_manual_review": cue_candidates[:8],
            "possible_secret_and_memory_cues": disclosure_candidates[:4],
            "event_witnesses_verified": False,
            "secrets_verified": False,
            "relationship_changes_verified": False,
            "chronology_verified": False,
            "prior_and_next_scene_verified": False,
            "semantic_status": "UNVERIFIED",
        })
    return records


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", type=Path, required=True)
    ap.add_argument("--markdown", type=Path, required=True)
    args = ap.parse_args()
    data = build()
    chapter_numbers = [row["chapter"] for row in data]
    last_chapter = max([193, *chapter_numbers])
    if chapter_numbers != list(range(1, last_chapter + 1)):
        raise ValueError(f"Expected consecutive chapters 001-{last_chapter:03d}")
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps({
        "warning": "Cues only. No witnessed events, secrets, relationships or chronology are certified.",
        "chapters": data
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    out = [f"# Chapters 001–{last_chapter:03d}: candidate continuity evidence index",
           "",
           "**Machine-generated source locators, not a semantic continuity ledger.** "
           f"All {len(data)} entries are UNVERIFIED pending scene reading. "
           "A named character in a line may be absent or discussed by someone else.",
           "",
           "For actual, confirmed witnessed events, relationship stages and separate "
           "knowledge states, use [CHARACTER_MEMORY_LEDGER.md](../CHARACTER_MEMORY_LEDGER.md) "
           "and the handoff template. Never assign one person's memory to another.",
           ""]
    for row in data:
        out += [
            f"## {row['chapter']:03d}: {row['title']}",
            "",
            f"- [Source](../../{row['path']})",
            f"- **Status:** UNVERIFIED for scene, witnesses, first/secondhand knowledge, "
            "secrets, chronology, relationships and downstream handoff",
            "- Name appearances (not proof of presence): " +
                ", ".join(f"{k} {v}" for k, v in sorted(
                    row["name_mentions"].items(), key=lambda kv: -kv[1])[:10]),
        ]
        if row["event_cues_for_manual_review"]:
            out.append("- Event/action candidates to inspect in context:")
            for cue in row["event_cues_for_manual_review"][:5]:
                out.append(f"  - Line {cue['line']}: " + cue["excerpt"].replace("|", "\\|"))
        if row["possible_secret_and_memory_cues"]:
            out.append("- Memory/disclosure candidates to inspect:")
            for cue in row["possible_secret_and_memory_cues"][:3]:
                out.append(f"  - Line {cue['line']}: " + cue["excerpt"].replace("|", "\\|"))
        out.append("")
    args.markdown.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {len(data)} unverified chapter cue records and review locators.")


if __name__ == "__main__":
    main()
