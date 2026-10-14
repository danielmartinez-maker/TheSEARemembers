#!/usr/bin/env python3
"""Regression guard for source-anchored character memory in The Sea Remembers.

This catches specific, previously confirmed resets and lists other likely
first-meeting dialogue for *human* review. It cannot prove semantic continuity.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

# Anchors correspond to confirmed scenes in continuity/CHARACTER_MEMORY_LEDGER.md.
# If an author intentionally changes one, revise the ledger and this check together.
CHECKS = {
    "chapters/014-letters-from-under-the-sea.md": {
        "present": ("I'm Annabeth. Daughter of Zeus.",),
        "absent": (),
    },
    "chapters/020-cake-and-lightning.md": {
        "present": ("Thalia's already sixteen", "followed Silena into battle",
                    "Cabin Three's cleared-off craft table"),
        "absent": ("followed Aphrodite kids into battle",
                   "Ares cabin's borrowed craft corner"),
    },
    "chapters/028-sparring.md": {
        "present": ("Thalia Grace called. She was sixteen",
                    '"Bring your knife, Grace.'),
        "absent": ("Thalia Grace called. She was fifteen",
                   '"Bring your knife, Chase.'),
    },
    "chapters/030-amphitrite-visits.md": {
        "present": ("without a rainbow between us", "meet you in person"),
        "absent": ("And you must be Annabeth",),
    },
    "chapters/066-jason-s-letter.md": {
        "present": ("One person doesn't get to decide everyone's ready",
                    "Then remember it for the next letter",
                    "The courier has a destination and a receipt"),
        "absent": ("Jason already answered Thalia's new flag question",),
    },
    "chapters/133-annabeth-s-birthday.md": {
        "present": ("Don't display any of my drawings unless you ask me first",
                    "Annabeth couldn't tell whether she'd heard the exchange",
                    "The line of stars moved well above everyone's heads"),
        "absent": ("Thalia promised not to move Annabeth's map",),
    },
    "chapters/067-fishing.md": {
        "present": ("come to Atlantis with me", "come to Olympus with me",
                    "pinky promise", "Ella did, on the back of the page",
                    "bucket still empty, with a notebook full of questions"),
        "absent": ("Amphitrite now knows about the other timeline",),
    },
    "chapters/068-the-storm-small.md": {
        "present": ("But you can stay without making yourself the place the lightning goes",
                    "Percy had learned from the fishing day",
                    "made a note to take the brazier out of service",),
        "absent": ("Let Percy’s sea take it",),
    },
    "chapters/132-a-month-beneath-the-sea.md": {
        "present": ("Then ask him, not your imagination",
                    "The note was written, not delivered",
                    "A good map saves people work"),
        "absent": ("Silena whisked the photograph clear of the sand before they took positions",),
    },
    "chapters/086-the-summons-to-atlantis.md": {
        "present": ("haven't softened since you tried to knock me", "I still like her"),
        "absent": ("You must be Clarisse", "you must be the sweet one"),
    },
    "chapters/099-mothers.md": {
        "present": ("Thank you — Mother", "I never met Sally Jackson"),
        "absent": ("the life you remember", "years you cannot remember"),
    },
    "chapters/118-a-message-from-amphitrite.md": {
        "present": ("Hi, Mom", "remember our lunch at camp"),
        "absent": ("Glad to meet you properly",),
    },
    "chapters/120-a-letter-from-the-sea.md": {
        "present": ("I remember that visit", "gave me a bracelet"),
        "absent": ("You’ve never met her",),
    },
    "chapters/123-the-garden-under-the-sea.md": {
        "present": ("glad to see you again", "ordinary family anecdote"),
        "absent": ("And you are Annabeth", "He knew she understood that"),
    },
    "chapters/126-the-palace-below.md": {
        "present": ("Not in person", "He had drawn the blue house"),
        "absent": ("telling Amphitrite about Sally’s kitchen in the life I remember",
                   "We wrote to one another before she died",
                   "I kept that letter for a long time"),
    },
    "chapters/127-guest-and-beloved.md": {
        "present": ("We can learn who you are now", "wish being here felt easier"),
        "absent": ("missing years are not a debt you owe me",),
    },
}

FIRST_MEETING_HINT = re.compile(
    r"nice to meet you|pleasure to meet you|you've never met (?:him|her|them)"
    r"|you’ve never met (?:him|her|them)"
    r"|you must be (?:annabeth|clarisse|silena|percy|thalia|triton|amphitrite)",
    re.IGNORECASE,
)


def main() -> int:
    errors = []
    for rel in (
        "FIC_CONTEXT.md",
        "continuity/CHARACTER_MEMORY_LEDGER.md",
        "continuity/CHAPTER_MEMORY_HANDOFF.md",
        "CHAPTER_INDEX.md",
    ):
        if not (ROOT / rel).is_file():
            errors.append(f"Required continuity source missing: {rel}")

    for rel, rules in CHECKS.items():
        target = ROOT / rel
        if not target.is_file():
            errors.append(f"Required chapter missing: {rel}")
            continue
        body = target.read_text(encoding="utf-8")
        for snippet in rules["present"]:
            if snippet not in body:
                errors.append(f"Memory regression or changed canon anchor: {rel} (missing {snippet!r})")
        for snippet in rules["absent"]:
            if snippet in body:
                errors.append(f"Previously corrected reset reappeared: {rel} ({snippet!r})")

    index = ROOT / "CHAPTER_INDEX.md"
    candidates = []
    if index.is_file():
        relpaths = re.findall(r"\]\((chapters/[^)]+\.md)\)", index.read_text(encoding="utf-8"))
        if len(relpaths) < 193:
            errors.append(f"Chapter index unexpectedly short: {len(relpaths)} entries")
        for rel in relpaths:
            target = ROOT / rel
            if not target.is_file():
                errors.append(f"Indexed chapter missing: {rel}")
                continue
            for number, line in enumerate(target.read_text(encoding="utf-8").splitlines(), 1):
                if FIRST_MEETING_HINT.search(line):
                    candidates.append((rel, number, line.strip()[:125]))

    # These are review cues, not failures. First meetings with *new* people are valid.
    print(f"Screened {len(candidates)} potential introduction lines for human review.")
    for rel, number, line in candidates[:40]:
        print(f"REVIEW {rel}:{number}: {line}")
    if len(candidates) > 40:
        print(f"... {len(candidates) - 40} further candidate lines")

    if errors:
        for err in errors:
            print("FAIL:", err, file=sys.stderr)
        return 1
    print(f"PASS: {len(CHECKS)} source-anchored chapter memory regression checks.")
    print("Note: a lexical pass does not certify all characters' narrative memories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
