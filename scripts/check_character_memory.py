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
    "chapters/023-sally-s-blue.md": {
        "present": ("Amphitrite had visited the camp and tried to be kind to Percy.",
                    "what she would want to hear in a letter."),
        "absent": ("Amphitrite knew Percy had arrived with memories that didn't match his life in Atlantis",),
    },
    "chapters/032-triton-visits.md": {
        "present": ("I left our old routines out of the report.",
                    "This is enough for now.",
                    "He could choose which stories traveled home, one at a time."),
        "absent": ("I also mentioned that you don't always recall the routines we used to practice together.",),
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
                    "That was the one I agreed to",
                    "No more from the notebook today",
                    "The only safe mounting points",
                    "Once Beckendorf repaired the brace"),
        "absent": ("I'm not moving until story time happens",
                   "Every Aphrodite instinct in the arena had perked up",
                   "He would arrive in about ten minutes"),
    },
    "chapters/074-tyson-s-visit.md": {
        "present": ("Now I know! I can tell them yes when I go home.",
                    "I wanted to be sure before I tell them,"),
        "absent": ("I knew! I told them yes!", "You — you already told them yes?"),
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
                    "You were very determined about your lessons",
                    "I could love you without asking to be loved in her place."),
        "absent": ("telling Amphitrite about Sally’s kitchen in the life I remember",
                   "We wrote to one another before she died",
                   "I kept that letter for a long time",
                   "I wish I remembered.",
                   "Percy told Amphitrite that he remembered another life",
                   "Percy told Amphitrite that he could not remember his childhood in Atlantis"),
    },
    "chapters/127-guest-and-beloved.md": {
        "present": ("We can take each visit as it comes",
                    "I don't want every visit to feel like a test I have to pass",
                    "wish being here felt easier",
                    "Why would I want them all to belong to me in the same way?"),
        "absent": ("missing years are not a debt you owe me",
                   "We can learn who you are now",
                   "Not because I have to make up for those years",
                   "Percy told Amphitrite that he remembered another life",
                   "Percy told Amphitrite that he could not remember his childhood in Atlantis"),
    },
    "chapters/095-annabeth-sick.md": {
        "present": ("Will had cleared Percy to return to ordinary drills after a full day without fever",
                    "No one needs to guess where the weak post is.",
                    "I don't want to talk about it while I'm sick.",
                    "Tell him the fever is down and I'm staying in Cabin Three today."),
        "absent": ("Fevers needed to breathe.",
                   "Tartarus dreams",
                   "Will says fevers fight harder when the body knows it's safe.",
                   "Clarisse and Silena ran cold spring water all day"),
    },
    "chapters/096-training-together.md": {
        "present": ("At dawn, after Annabeth's temperature had registered lower overnight",
                    "Thalia told me what she sent Grover",
                    "The water is not a wire",
                    "Anybody can call stop",
                    "She waited until the arch path was clear, then gave Grover a small nod.",
                    "No one asked what Annabeth had dreamed",
                    "I want my own bunk tonight"),
        "absent": ("as well as any child of Athena",
                   "the tail at the lake",
                   "the base steady where it met the lake",
                   "Holding a water bridge that far",
                   "Only after the sisters were out of earshot",
                   "The morning after Annabeth's fever breaks"),
    },
    "chapters/097-the-map.md": {
        "present": ("You didn't erase what we remember. You just stopped the map from claiming it was here.",
                    "third board flexes; do not step on it until repaired",
                    "Forge entrance; keep clear of vent while forge is operating.",
                    "The door is public. What happens inside can change, and it isn't for the map.",
                    "Wide shot only"),
        "absent": ("Percy's thinking rock",
                   "Best at sunrise. Ask Percy before bringing friends.",
                   "third board flexed and should be stepped over until it was repaired",
                   "the north trail is open",
                   "Amphitrite knows the time rewrite"),
    },
    "chapters/098-fathers-day-gods.md": {
        "present": ("You remember the visit when I was eight?",
                    "I cried in the kitchen after you were gone.",
                    "We're together,",
                    "Every time you visit, you come with another face.",
                    "The north trail was still marked closed"),
        "absent": ("through the change",
                   "memories you carry together",
                   "Virginia orchard",
                   "Triton keeps me updated with pictures",
                   "A bald eagle named Kevin",
                   "Amphitrite knows the time rewrite"),
    },
    "chapters/099-mothers.md": {
        "present": ("She died when you were two; that doesn’t mean you cannot miss her",
                    "60 days sober today. They gave me a chip.",
                    "She asked for you. She said you can come too",
                    "A letter came from Mom. I'm keeping it for now.",
                    "Don't put somebody's name on a thing they didn't choose.",
                    "The dock's third board still flexed; nobody was to use it.",
                    "I've been rude to you and Percy. I'm sorry."),
        "absent": ("Ares thinks it's stupid",
                   "cheetah-print coat and no shoes",
                   "set the house on fire when I was seven",
                   "told my principal she was Hera",
                   "forgot Jason's birthday three years running",
                   "Beryl was at the Big House",
                   "Thalia was whittling",
                   "GABE got crossed out and replaced with PAUL",
                   "Amphitrite knows the time rewrite"),
    },
    "chapters/100-the-thousandth-campfire.md": {
        "present": ("That's not how I arrived here.",
                    "If you write it down, mark where you heard it.",
                    "the Minotaur belonged to the other life he remembered",
                    "Amphitrite watched the story circle quietly",
                    "Beryl was not at the campfire.",
                    "Thalia had made no visit arrangement",
                    "the right palm was still wrapped",
                    "The rest is still mine.",
                    "There was no Minotaur panel.",
                    "Would you want a print of the dance?",
                    "Triton nodded. “If you ask.”"),
        "absent": ("That was from the life I remember.",
                   "In the other life. In this one,",
                   "I didn't surf it in either life.",
                   "Beryl was at the campfire.",
                   "Clarisse fought a Minotaur with him.",
                   "Amphitrite knows the time rewrite",
                   "The Minotaur belonged to the camp's own record of his arrival."),
    },
    "chapters/101-a-name-for-it.md": {
        "present": ("I want to be your girlfriend.",
                    "Favorite person can be ours.",
                    "I don't remember the blocks,",
                    "The bandage on her right palm was clean",
                    "I'm Noah. I wanted to ask about the shield rack.",
                    "I'll bring you one tomorrow."),
        "absent": ("Thalia's right palm was healed.",
                   "Annabeth remembered the blocks.",
                   "Amphitrite knows the time rewrite",
                   "Beryl was at the shrine."),
    },
    "chapters/177-the-one-who-came-back.md": {
        "present": ("Percy had the familiar talent for being entirely present in a room",),
        "absent": ("the twelve-year-old's talent", "the twelve-year-old’s talent"),
    },
    "chapters/136-percy-s-birthday.md": {
        "present": ('Percy felt the old unease, soft and familiar. "It\'s a good place for it."',
                    "To her, it was an ordinary family anecdote from the childhood she knew he had lived.",
                    "He kept that distinction private.",
                    "Silena had heard him say that Sally took pictures in the life he remembered",
                    "it wasn't a memory she could carry for him."),
        "absent": ('Percy felt the old unease, soft and familiar. "Did I?"',
                   "not expecting him to supply an answering memory",
                   "Both truths could live in him without being explained to her tonight.",
                   "neither did his sisters"),
    },
    "chapters/145-the-lake-keeps-what-it-takes.md": {
        "present": ("You are my boyfriend.", "I know I love you. I know I chose this life with you."),
        "absent": ("You are not my boyfriend.",
                   "whether I'm still in love with you or just still kind of haunted by the idea of you"),
    },
    "chapters/146-the-long-way-back.md": {
        "present": ("After we talked about the tree, I started thinking about this.",),
        "absent": ("When I was a tree, I used to think about this.",),
    },
    "chapters/187-silver-on-the-rings.md": {
        "present": ("The sight brought back the memory he carried from the future that had been erased",
                    "a blade slipping in a boathouse, in a month this life had not reached"),
        "absent": ("from a blade that had slipped in a boathouse in a month neither of them had lived yet",),
    },
    "chapters/038-brothers-and-sisters.md": {
        "present": ("a fourteen-year-old girl told him where he'd missed a spot",),
        "absent": ("a thirteen-year-old girl told him where he'd missed a spot",),
    },
    "chapters/175-salt-and-steam.md": {
        "present": ("The association offered no room or event, only an ache of wanting he could not quite place.",
                    "It gave him no age, room, or person on the other side of a wall.",
                    "The gesture felt familiar in the muscles of his palm, but it gave him no scene to set it in."),
        "absent": ("the exact smell of the corridor outside my mother's rooms in the deep palace",
                   "in a room where he was nine, when somebody he loved was awake on the other side of it",
                   "which was a thing he had done in the deep palace, exactly this"),
    },
    "chapters/190-thursday-twice.md": {
        "present": ("Percy had told her only that the warm mineral smell pulled him toward Atlantis; the corridor was her guess, not something he could remember.",
                    "The association belonged to him, not her."),
        "absent": ("That was Percy's memory, not hers.",),
    },
    "chapters/181-whoever-wants-to-come.md": {
        "present": ("It brought with it a deep-palace association he couldn't fasten to a corridor, a pool, or a voice.",
                    "the hall was not the palace, and an association was not a scene he remembered."),
        "absent": (),
    },
    "chapters/194-a-place-at-the-table.md": {
        "present": ("I’m sorry I put you on the spot at the shooting line.",
                    "That's private.", "The sign of Poseidon.",
                    "I don't take orders from girls."),
        "absent": ("Because of the time thing?", "I remember the future"),
    },
    "chapters/195-the-rules-of-cabin-three.md": {
        "present": ("But this is the first time we’ve met.",
                    "I had people who took care of me."),
        "absent": ("Because of the time thing?", "I remember the future"),
    },
    "chapters/196-what-a-map-leaves-out.md": {
        "present": ("I’m not going to explain your sister for you.",
                    "I don’t want you to stop worrying."),
        "absent": ("Because of the time thing?", "I remember the future"),
    },
    "chapters/197-the-room-we-keep.md": {
        "present": ("I promised you one",
                    "not a gift I promised you on my behalf",
                    "I thought if she saw us in the picture, that would make the table less strange."),
        "absent": ("Because of the time thing?", "I remember the future"),
    },
}

FIRST_MEETING_HINT = re.compile(
    r"nice to meet you|pleasure to meet you|you've never met (?:him|her|them)"
    r"|you’ve never met (?:him|her|them)|first time (?:we|i)['’]ve met|this is (?:leandros|ianthe)"
    r"|you must be (?:annabeth|clarisse|silena|percy|thalia|triton|amphitrite|leandros|ianthe)",
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
