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
    "chapters/070-clarisse-s-poems.md": {
        "present": ("You said no", "I haven't read it",
                    "I'm correcting my own mistake",
                    "The only safe mounting points",
                    "Once Beckendorf repaired the brace"),
        "absent": ("I'm not moving until story time happens",
                   "Every Aphrodite instinct in the arena had perked up",
                   "He would arrive in about ten minutes"),
    },
    "chapters/076-the-promise-ii.md": {
        "present": ("The older shrine was tucked",
                    "not claim a life she has not lived",
                    "That board still required an inspected fence repair",
                    "I'm not asking you to be her",
                    "After dinner Percy returned to the canoe dock"),
        "absent": ("grabbed Clarisse's hand and forced her pinky up",
                   "The rope would survive.",
                   "Ella will remember for them"),
    },
    "chapters/077-beach-day-atlantis-style.md": {
        "present": ("sheltered Atlantean pools",
                    "Mara and Lucy went off to tell the other children",
                    "The living sand lost its magical shine",
                    "a place for him when he visits Cabin Three"),
        "absent": ("with a nectar bottle",
                   "Tyson finally has a cabin that feels like home",
                   "The war with Kronos is coming"),
    },
    "chapters/078-nico-s-birthday.md": {
        "present": ("Friday's your birthday",
                    "Chiron placed a provisional approval",
                    "Chiron had inspected the fort at dawn",
                    "Nico put his letter into the hidden shelf",
                    "He went back to Cabin Thirteen"),
        "absent": ("Stygian iron", "Styx promise",
                   "I swear on the Styx",
                   "blindfolded with her own jacket"),
    },
    "chapters/079-elena-s-tale.md": {
        "present": ("Things Mom has liked before",
                    "Marisol asked for tea without lemon",
                    "She erased it",
                    "Nico had a ring with a skull on it",
                    "Until he approves it",
                    "Elena looked at the notebook in her lap"),
        "absent": ("Elena could quote it back word for word",
                   "You gave me your notebook from the whole week",
                   "hugged Elena hard enough to lift her"),
    },
    "chapters/080-the-second-dance.md": {
        "present": ("Tyson returned from meeting an approved Atlantean messenger",
                    "The silver wristband from the first dance had stayed with Annabeth",
                    "Grover danced with Ella for the first slow song",
                    "The side path is clear",
                    "Beckendorf unplugged the speaker"),
        "absent": ("lake portal", "He had knocked over nectar",
                   "Annabeth says triangles only hurt when people compete"),
    },
    "chapters/090-storm-and-sea.md": {
        "present": ("the shanty she'd taught them during the cove drills",
                    "a raised yellow flag meant irregular wind and an automatic hold",
                    "the Sound had never entered the canoe lake",
                    "That would be a morning check",
                    "no strike on a single dropped flag",
                    "We do not yet know what called it"),
        "absent": ("Three months ago,", "faint white scar on his left palm",
                   "their dad had taught them in dreams",
                   "nearly collapsed doing that last week",
                   "Annabeth, are you seeing this?", "No real injuries.", "Mjolnir"),
    },
    "chapters/091-tide-pools.md": {
        "present": ("No touching, no finish line, no cheating.",
                    "The boyfriend part is accurate.",
                    "The diagram was useful.",
                    "The lower route stays closed while the tide rises",
                    "Sally made blue food on purpose, in the life I remember"),
        "absent": ("Do not pick up anything with blue rings.",
                   "Grover snored softly with cookie crumbs on his shirt.",
                   "Grover dozing again",
                   "Clarisse with a crab on her palm",
                   "We are not—"),
    },
    "chapters/092-jealousy-ii.md": {
        "present": ("Nobody had stopped him from joining; the decision was his.",
                    "Clarisse can tell him no.",
                    "shared her bread with him when his own burned.",
                    "Tomorrow's practice will use the wider marks."),
        "absent": ("By lunch, Evan and Clarisse were inseparable.",
                   "Evan clapped Clarisse on the shoulder, hard enough to rock her forward"),
    },
    "chapters/093-movie-night.md": {
        "present": ("when Jason had saved a place for his family on the fireworks hill",
                    "Camp Jupiter T-shirt he had borrowed from Frank at dinner",
                    "Frank checked the fabric and took it from him.",
                    "Austin shut down the projector and waited for the lamp to cool.",
                    "The counselors gathered their cabin groups before walking them back from the green.",
                    "No one had left the marked green during the night."),
        "absent": ("he'd stolen from Frank",
                   "photos his friend Frank had sent him",
                   "Austin left the projector running so the white sheet glowed like a nightlight.",
                   "The projector clicked off, and the sheet went dark.",
                   "Sweet and steady, the way they had learned to be."),
    },
    "chapters/094-sick-day.md": {
        "present": ("This looks consistent with an ordinary viral cold.",
                    "Sleeping outside doesn't prove that's where it began.",
                    "That memory was his alone.",
                    "I remember the shell bucket you told us about",
                    "You still need the full twenty-four hours without fever",
                    "her hand rested on the blanket near his shoulder"),
        "absent": ("October weather",
                   "Always, completely",
                   "Percy remembered her singing this song across the Poseidon cabin on his first homesick night",
                   "the thermometer was a monster"),
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
        "present": ("Not in person", "He had drawn the blue house",
                    "You were very determined about your lessons"),
        "absent": ("telling Amphitrite about Sally’s kitchen in the life I remember",
                   "We wrote to one another before she died",
                   "I kept that letter for a long time",
                   "I wish I remembered."),
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
