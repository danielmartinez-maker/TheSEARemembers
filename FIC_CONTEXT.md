# The Sea Remembers, the Sky Forgets
## Canon bible and editorial operating rules

**Status:** Work in progress  
**Updated:** 2026-10-17
**Scope:** Drafting, editing, continuity review, chapter handoffs, and reader-edition assembly  
**Fandom:** *Percy Jackson and the Olympians*  
**Primary pairing:** Percy Jackson / Annabeth Grace (established Percabeth)

> **Core promise:** Percy and Annabeth remember a future together, but return to a changed earlier point in their own history. They must keep their established bond while learning to live with families who know childhoods that they themselves do not remember. Family intimacy, romance, camp life, and ordinary shared experiences are the story's center. Mystery, quests, and divine politics should complicate those relationships, not replace them.

This document describes **intended canon and writing requirements**, not a certification that every existing chapter complies. Do not treat a contradiction in an older draft as new lore. Identify it, document it, and revise it deliberately.

---

## 1. Source authority and current state

### 1.1 Decision hierarchy

When two sources disagree, use this order:

1. **The user's explicit decisions**, with later direct changes superseding earlier instructions on the same point.
2. **Locked canon in this bible**, insofar as it accurately records those decisions. If it conflicts with a direct user instruction, flag and update it.
3. **The chapter files in `danielmartinez-maker/TheSEARemembers` on GitHub**, which the user explicitly designated as the source for the 2026-10-13 manuscript pass. Use the pinned `main` commit as the comparison baseline and keep proposed edits on the named review branch.
4. **Compiled Markdown, DOCX, and PDF reader editions**, which are outputs, not sources of truth; historical editions may be outdated.

**Never resolve a contradiction by silently changing parentage, inventing a memory rule, creating a new time-rewrite event, or treating assistant improvisation as an approved plot decision.** Log the discrepancy and make the smallest coherent proposed fix.

### 1.2 Working files, as of 2026-10-14

- **GitHub source for this pass:** [`danielmartinez-maker/TheSEARemembers`](https://github.com/danielmartinez-maker/TheSEARemembers), with `main` pinned at `63ae90bb6aad31753fcabfd057a1771359594dca` before edits. It contains numbered Markdown files for **chapters 1–193** and **two bonus interludes**, plus an index, manifest, and assembly script.
- **GitHub filename convention:** `chapters/001-the-weight-of-salt-and-sky.md` through `chapters/193-the-heel.md`. Use the actual filenames in `CHAPTER_INDEX.md`; do not assume the older `chapters/ch02.md` convention still applies in this repository.
- **Authority update:** The user's 2026-10-13 direction to work from the latest GitHub repository supersedes the earlier local-copy precedence for this pass. Historical/deprecated local manuscript copies were not used or reconciled; do not treat them as competing authorities unless the user explicitly re-designates one.
- **Arc continuity:** The originally planned fourth-arc range was chapters **140–164**, but the story continued through **165–193** without a new declared arc boundary. Treat chapters 140 onward as one continuous developing stretch until the user sets a new boundary.
- **Exports:** Existing PDF/DOCX volumes are historical until rebuilt from selected, corrected sources. Preserve old versions.

### 1.3 Length status: targets are not completion claims

**User requirement (2026-10-11):** A newly drafted full chapter must have **at least 10,000 body words**, with **10,200–11,200** as the normal working range, and more if its scenes earn the extra length. That floor is not a license for filler.

**Previous PR #103 continuation checkpoint (October 17, 2026):** source commit `27a41c8ed4ce91c11c97ec9c642aabc473d495bc` continues from fetched PR head `e6ea84f104a5502dbdfc756689ed345f4c271531`. It adds source-grounded repairs in Chapters 004, 038, 102, 118, 132, 133, 136, 145, 146, 167, 177, and 187, refreshes continuity notes, and generates current QA reports. Strict local QA reports **193/193 chapters at or above 10,000 body words**, zero shortfall; the chapter-only scan checked **1,941,320** every-offset 300-token windows with zero exact matches, and the chapter-plus-bonus scan checked **196 files / 2,150,177 body words / 2,091,872 windows**, also with zero exact matches. **42** source-anchored memory regressions pass; all 193 chapter files are ordered. Chapter 004 now uses Annabeth's current name/parentage, retains Percy POV, and treats prophecy-copy provenance as uncertain; Chapter 038's Silena age is fourteen, matching the opening baseline and Chapter 041, without an invented birthday. Chapters 136/145/146 preserve Amphitrite's privacy boundary, Annabeth and Percy's established relationship, and Thalia's lack of erased-tree memory. Chapters 102 and 118 received scoped repetition edits; Chapter 132's pre-dinner consultation now precedes its evening dock scene; Chapter 133's plan discussion no longer implies a physical corridor survey. Chapter 167's autumn wording now matches the late-September sequence, and Chapter 187 explicitly frames the boathouse detail as Percy's remembered-future association. Hosted [manuscript audit](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/39066126303) and [character-memory](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/39066126334) checks passed on `27a41c8`. Mechanical checks do not certify every scene's continuity or prose quality.

**Follow-on PR #103 checkpoint (October 17, 2026; started from `697741f`):** Chapter 142 now shows Clarisse reporting the outer-buoy overrun to Chiron; the location remains unknown pending image review. Chapters 175/181/190 now keep Percy's Atlantis response within sensory/bodily association and mark the corridor as Annabeth's inference. Chapter 175 attendance totals remain unresolved. Local QA after these edits reports 193/193 chapters above 10,000 body words, no shortfall, 1,942,016 chapter-only 300-word windows, and no exact matches; the 196-file bonus-inclusive scan reports 2,150,873 body words, 2,092,568 windows, and no exact matches. All 45 source-anchored character-memory regression checks pass. Hosted [full manuscript QA, run 510](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/39070769176) and [character-memory checks, run 251](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/39070769240) passed on commit 33fc2d0. These results do not certify full prose quality or all-scene continuity.

The four-phase request explicitly authorized substantive expansion of the chapters below 10,000 words. The current PR source meets that numeric floor; any later discovery of a short chapter should still be expanded with meaningful scenes and verified by body count. The completed mechanical gate does not certify that every expansion has literary approval.

---

## 2. The story's fixed premises

| Element | Locked rule |
|---|---|
| Timeline | Percy and Annabeth return to an **earlier point in their own timeline**; this is not an unrelated parallel-universe adventure. |
| Opening | Approximately **five months before *The Lightning Thief***. |
| Memory holders | **Only Percy and Annabeth** retain their remembered future under the original governing rule. Others may detect changes but do not automatically remember the erased history. |
| Their previous life | They were **seventeen**, had survived the Titan War, Giant War, and Tartarus, were in a relationship, and were planning a future together. |
| Altered history | Their childhoods, family relationships, parentage, and social world have already been rewritten before they arrive. |
| Mystery | The architect of the rewrite remains **unknown**. **Kronos is not the architect.** His possible role in a recognizable canon quest does not change this. |
| Powers | No automatic fate rewriting, omniscient record-reading, instant mastery, or spontaneous full memories of an altered childhood. |
| Primary lenses | Third-person limited, generally through **Percy, Annabeth, or Thalia**. |
| Tone and genre | Romance, found family, sibling bonds, camp slice-of-life, adventure, mystery, and divine politics. **Warmth and romance have priority** when they compete with plot spectacle. |

### 2.1 Memory boundaries

**Remembered life:** Percy grew up with **Sally alive** in Manhattan. Annabeth was **Athena's daughter**. Percy and Annabeth recall their relationship, friends, quests, Tartarus, and New Rome plans, including Percy's three recommendation letters. They were together before displacement.

**Altered history:** Sally died when Percy was **two** and Poseidon brought him into the Atlantean household, where Amphitrite helped raise him. Annabeth is a **daughter of Zeus and Beryl Grace**, Thalia's younger biological sister. These new lives are real to their surrounding families, but Percy and Annabeth do **not** inherit complete first-person autobiographical memories of those years.

**What may carry over:** Physical habits, bodily familiarity, trained reflexes, emotional associations, and skills can surface in bounded ways. None grants reliable knowledge of specific conversations, private memories, or events experienced only by the altered-history child. Percy and Annabeth's knowledge of canon events is imperfect predictive evidence, not a script that must repeat.

**Chapter 1 disclosure boundary (author directive, 2026-10-12):** **Amphitrite is not told and does not discover Percy's predicament.** She knows the ordinary altered-history facts that Sally died when Percy was two and that she has raised Percy since then. She does **not** know Percy remembers another life with Sally alive, cannot recall his Atlantean childhood autobiographically, or has awakened with the consciousness/memories of his seventeen-year-old self. She can interpret his nerves, distraction, and questions as ordinary pre-camp uncertainty or curiosity about his birth mother, but must not infer the timeline alteration. Percy deliberately conceals the secret from her. Do not reveal it to Amphitrite in later chapters without explicit author authorization. At the end of Chapter 1, Percy and Annabeth have privately recognized one another as the two memory holders; neither has explained the rewrite to their families.

**Forbidden shortcut:** Do not make Annabeth forget Percy or their romance merely to create a second courtship. Do not reveal Thalia as a hidden time architect or give her complete future memories without a fresh, explicit user decision revising the original premise.

### 2.2 Persistent, character-specific memory (author directive, 2026-10-13)

**Everyone retains a cumulative memory of what they personally experienced in this manuscript.** Chapters cannot quietly reset a friendship, first meeting, chosen family title, romantic milestone, conversation, skill, promise, injury, gift, disagreement, or earned trust just to replay the same emotional beat. A person who met another character in Chapter 30 must not introduce themselves to that person in Chapter 123. Percy's spoken **Mom** for Amphitrite in Chapters 99, 127, and 132 is an earned part of their relationship: he may still use her name or **Mother** in formal writing and other contextually formal uses, but must not subsequently treat her as a stranger. Affection can wax and wane; factual acquaintance does not.

Distinguish four separate categories for each character:

1. **Firsthand current-timeline knowledge:** witnessed events, personal conversations, gifts, promises, names used and repeated interactions. These persist unless a **specific, approved** forgetting mechanism occurs on the page.
2. **Secondhand current-timeline knowledge:** information received in a letter, retelling, overheard exchange, or report. Record who supplied it, what was said, and whether it was trusted. Do not write the recipient as if they witnessed the event.
3. **Remembered prior-life knowledge:** Percy and Annabeth alone possess autobiographical memories from their original future. Others can learn selected facts if explicitly told; being told is not the same as sharing those memories.
4. **Altered-childhood history without autobiographical recall:** people like Amphitrite, Thalia and Triton have firsthand memories of raising or knowing the altered-history Percy and Annabeth. Percy and Annabeth do not automatically gain those memories. They can learn family stories, accumulate **new** memories of these people, and form genuine affection without suddenly recalling an unexperienced childhood.

**Knowledge is per character, not global.** Verify whether a character was present, what they actually heard, and whether a secret was shared before writing informed dialogue. In particular, Amphitrite remembers raising Percy but does **not** know he remembers a different timeline or cannot recall his Atlantean childhood. His affection for her and his chosen address "Mom" never, by themselves, authorize such a revelation.

Use **continuity/CHARACTER_MEMORY_LEDGER.md** as a source-anchored index and **continuity/CHAPTER_MEMORY_HANDOFF.md** for each chapter's new facts. Before repeating a first meeting, name, nickname, emotional disclosure, family argument, gift, or callback, locate the original scene and check what each person knows. Add a new ledger event when a chapter changes a relationship; do not erase earlier events. If an established fact conflicts with a later passage, flag it as an error and make a bounded scene-level repair, not a global retcon.

---

## 3. Locked families and households

### 3.1 Poseidon's household: PCS

**PCS = Percy, Clarisse, Silena**; Percy is the youngest of these three half-siblings. The altered-history cabin is **Cabin Three**.

| Person | Canon relationship | Story consequences |
|---|---|---|
| **Percy Jackson** | Son of Poseidon and Sally Jackson; younger half-brother of Clarisse and Silena. | Raised in Atlantis in the changed past, but lacks that childhood's full memories. Has a particular relationship with royal status and privilege. |
| **Clarisse La Rue** | Daughter of **Poseidon**, not Ares in the present altered timeline; Percy's and Silena's half-sister. | Competitive, blunt, formidable, loyal; do not turn her into a duplicate of Thalia or transfer Thalia's history to her. |
| **Silena Beauregard** | Daughter of **Poseidon**, not Aphrodite in the present altered timeline; Percy's and Clarisse's half-sister. | Socially perceptive, creative, warm, and capable of dissent; she needs her own desires and limits beyond caretaking. |
| **Amphitrite** | Poseidon's wife and Percy's mother in practice after Sally's death in the altered history. | Percy can love her without replacing Sally. She is **unaware of Percy's remembered prior life or missing altered-childhood memories**, as explicitly directed for Chapter 1, and his unusual behavior reads to her as ordinary anxiety about leaving home. Her relationship with Clarisse and Silena grows on separate paths; do not presume a maternal bond or demand a title before they choose it. Their future chosen-mother arc is recorded below. |
| **Triton** | Son of Poseidon and Amphitrite; Percy's older half-brother. | Older Atlantean family member, mentor, and teasing rival, not an ordinary camp teenager. |
| **Tyson** | Poseidon's Cyclops son, where present. | His visits need established logistics. Do not relocate him permanently to camp by implication. |
| **Poseidon** | Shared divine father of the above acknowledged children. | A more present father to Percy in the altered history, but unequal childhood experiences and privilege may strain sibling relationships. |

**Planned chosen-mother arc (future work after Chapter 193):** Amphitrite's relationship with Silena and Clarisse develops gradually into a maternal bond through sustained care for each as an individual. Silena chooses to call her “Mom” first, in a private, earned moment; Clarisse makes that choice later, after Amphitrite has repeatedly respected her boundaries and her hurt about Poseidon's unequal involvement. Their milestones happen in separate scenes and have not occurred in Chapters 001–193. Amphitrite never asks for the title. This bond does not replace either sister's own mother, resolve Silena's relationship with Maria, or forgive Poseidon on Clarisse's behalf.

No invented replacement Poseidon sisters, including Marina, Coral, Tess, or Delphine. Any new child of Poseidon needs explicit approval and a deliberate role. Do not say Triton or Tyson is biologically unrelated to other children sharing Poseidon as father; distinguish their mothers, ages, and households instead.

### 3.2 Grace household

| Person | Canon relationship | Story consequences |
|---|---|---|
| **Thalia Grace** | Daughter of Zeus and Beryl; Annabeth's older biological sister and Jason's older sister; Cabin One. | Helped raise Annabeth. In this altered history she did **not** become a pine tree or join the Hunters. |
| **Annabeth Grace** | Daughter of Zeus and Beryl; Thalia's younger sister, Jason's older sister; Cabin One. | **Grace, not Jackson.** Her intelligence and architecture interests survive the parentage change. She loves Percy romantically, not as family. |
| **Jason Grace** | Younger brother of Thalia and Annabeth. | Raised at Camp Jupiter after being taken away young. Any presence at Camp Half-Blood needs a specific, plausible visit or communication arrangement. |
| **Zeus** | Father of the three Grace siblings. | Absent, inconsistent, volatile. Uses a different appearance at every visit to his daughters. See §4. |
| **Beryl Grace** | Mortal mother of the Grace siblings. | Addiction, instability, and childhood fear affect Thalia and Annabeth's altered history. Establish and track her current address and contact pattern. |

**Cross-family boundaries:** Clarisse and Silena are Annabeth's friends, not her biological sisters. Thalia is Percy's friend and his girlfriend's older sister, not PCS. Chosen-family terms can be affectionate but must not falsify biological relationships or cabin assignments. Percy and Annabeth are **never siblings**; do not introduce distracting incest/cousin framing to explain divine genealogy.

---

## 4. Character psychology and relationship friction

### Percy

Funny, loyal, observant of others' discomfort, brave, impulsive, and occasionally stubbornly wrong. His original experience gives him judgment and technique, but his younger body still limits speed, strength, endurance, and reach. He has to learn altered-history etiquette, Atlantean language, and family routines as a displaced consciousness; others can reasonably expect him to know things he cannot remember.

His grief for Sally is **new to him** and old to everyone else. Accepting Amphitrite must not erase that contradiction. Percy may offer comfort but should not become everyone's therapist, mediator, or infallible moral authority.

### Annabeth

Strategic, proud, ambitious, intelligent, curious, exacting, interested in architecture, and capable of resentment when her independence is discounted. Her Zeus powers (electricity, wind, pressure, storms) require practice, mistakes, and limits. She remembers loving Percy but struggles to respond naturally when Thalia recalls years of sisterhood she herself cannot remember.

Her arc is not a reset of her intelligence or romance. It is an attempt to build belonging in this life while refusing to remain permanently the protected little sister. Do not reduce her to a walking power hazard or an emotional support character for Percy.

### Thalia

Protective, combative, quick-witted, competitive, loving, sometimes overbearing, and worn down by having taken responsibility too young. Her identity has been organized around keeping Annabeth safe. She wants Annabeth to become independent, but is genuinely frightened by what that will mean for their relationship and her own purpose.

Show her routines, jokes, friendships, interests, resentments, tenderness, and ordinary bad days. Protectiveness should have costs and blind spots. Never frame either total control or instant selflessness as the correct answer.

### Clarisse and Silena

They must not become interchangeable. Clarisse's aggression and competence can coexist with embarrassing, concrete gestures of love. Silena can help others but should also say no, make mistakes, want things for herself, and pursue work or romance on her own terms. Their shared father does not imply identical powers, social experiences, childhood privilege, or temperaments. **Do not make an inequality disappear after one apology.**

### Zeus

Unpredictably attentive. He can be charming, absent, neglectful, frightening, or briefly considerate. **He never wears the same face twice when visiting the girls.** Recognition comes through divine presence, static, speech patterns, and their reaction, not a consistent appearance. He may praise Annabeth for compliance while denigrating Thalia's defiance, using comparison to divide them. He often treats a daughter's criticism of her father as disobedience to a king.

A heartfelt confrontation does not cure this history. Any improvement must be limited, uneven, and demonstrated through repeated choices; his volatility remains meaningful.

---

## 5. Emotional priorities and romance boundaries

**Story-wide priority:** Established Percabeth, Grace sisterhood, PCS solidarity, and other forms of chosen and biological family. Quiet domestic scenes are not filler merely because nobody fights a monster. A scene earns its place when it changes what people know, want, fear, choose, or can do together.

### 5.1 Recurring chapter ingredients

Every full chapter is intended to include:

1. **A warm centerpiece** with its own mini-arc: a meal, campfire, baking day, game, lake outing, date, craft project, performance, repair, or shared routine.
2. **A distinctive Percabeth beat**: mutual attention, affectionate teasing, hand-holding, a kiss, a cuddle, a disagreement, or care conveyed through a real choice.
3. **A meaningful sibling beat**: Thalia and Annabeth, Percy with Clarisse or Silena, or the households in interaction.

These are **requirements of emphasis, not instructions to paste in three formulaic scenes**. Let one activity carry multiple beats when that is natural. Give each chapter a different emotional movement and concrete consequence. Tender scenes may take time on the page; they should not keep describing the same sensation or restating the same reassurance.

### 5.2 Percabeth: established, younger, nonsexual

Percy and Annabeth remember their established relationship. They are not strangers, and no love triangle or amnesia-based second courtship is needed. Their bodies are younger, and they must work out what affection and independence mean now among new families and public expectations.

Age-appropriate kisses, hugging, leaning together, holding hands, cuddling, sleepiness, notes, dates, gentle jealousy, and ordinary disagreements are welcome. **No sexual content involving the younger Percy and Annabeth.** Mutuality and the ability to decline affection matter, but do not turn every scene into a formal consent speech or repeatedly label it “chaste.” Each partner must also have friendships and time separate from the other.

### 5.3 Silena / Charlie Beckendorf

A **slow-burn** between Silena (working late-arc age sixteen) and Charlie Beckendorf, a reserved, practically minded child of Hephaestus. The original context sheet points to a crush seed around chapter 25; verify the scene in the selected chapter source before citing it as established fact. Build the arc through projects, mistakes, awkward attention, friendship, and gradually chosen intimacy. Do not skip milestones or make Silena only a blushing spectator.

### 5.4 Thalia / Rhys Calder

Rhys is a **nineteen-year-old son of Apollo** who returns for winter; Thalia is **eighteen** in the late-arc working baseline. He appears in the late manuscript, rather than emerging from nowhere in a bonus interlude. Their relationship should grow through compatible competence, competitive friction, inconvenient attention, and ordinary choices. Rhys needs personal loyalties, obligations, defects, and goals independent of being attentive to Thalia.

The user's mature-romance instruction applies **only to these adult characters**. When an adult intimacy scene is called for, the direction is **not to fade to black automatically** or default to a saccharine register. Keep mutual agreement unambiguous, stay with the adult characters' specific reactions and voices, and avoid mechanical inventories or generic romantic language. Maintain the established timing of their relationship. This direction does **not** extend to Percabeth's nonsexual arc.

### 5.5 Sibling interactions

Favor **specific, reciprocal** teasing over recurring stock jokes: shared chores, competitions, borrowing clothes, sabotaged breakfast plans, sneaking snacks, private rituals, stubbornness, gifts, and practical help. A genuine conflict should have a consequence. Not every argument should end in the same hot drink, apology, or group hug.

---

## 6. Time, ages, and geography

| Character | Opening age | Working baseline from chapter 140 onward |
|---|---:|---:|
| Percy | 12, remembering life through 17 | 14 (birthday drafted in ch. 136) |
| Annabeth | 12, remembering life through 17 | 14 (birthday drafted in ch. 133) |
| Thalia | 16 | 18 |
| Clarisse | 13 | 15 |
| Silena | 14 | 16 |
| Rhys | Not yet introduced | 19 in his late-arc appearances |

**Source-verified early age cross-check:** Thalia is sixteen by Chapters 16, 20 and 24, and is still sixteen in the revised Chapter 28 (not fifteen). Chapter 133 portrays her as eighteen. Preserve intermediate birthdays only where the intervening narrative actually supports them.

**Working baseline, not an automatic age override:** Track explicit birthdays and elapsed time. From chapter 140, Percy and Annabeth should be fourteen unless a **later dated birthday** justifies a change. Do not silently revert them to thirteen. Check Thalia's legal adulthood and Rhys's nineteen-year-old status at the point of every mature interlude.

Before writing a chapter, make a timeline row with its date or season, elapsed days since prior chapter, ages, locations, arrivals/departures, current injuries, objects or gifts in use, and commitments due next. If the source does not establish the month or day, mark **unknown** rather than inventing one.

**Location constraints:** Atlantis is underwater and operates with its own etiquette. Camp's canoe lake is freshwater; do not make it salty by default. Camp weather, temperature, daylight, clothing, sleeping arrangements, and transport need to agree. Visits by Jason, Triton, Tyson, gods, or others require travel logistics and follow-through rather than spontaneous unexplained relocation.

---

## 7. Plot priorities and pending threads

- **Early camp material:** Family adjustment, warmth, training, changed household dynamics, and an established romantic bond. The time-rewrite mystery remains present but does not crowd out camp life.
- **Lightning Thief divergence:** The master-bolt theft, suspicion of Poseidon, the solstice deadline, and an adapted quest belong in the work. Percy and Annabeth may know what happened before but must test assumptions against changed circumstances. A familiar event is not proof that the time-rewrite antagonist is the same person.
- **Extended chapter 140+ progression:** Continued sibling bonding, lake scenes, projects, camp duties, adult slow-burn developments, and daily routines. There is **no newly declared arc break** at 164, 172, 178, or 193.
- **Outstanding mythology/mystery seeds:** Track Poseidon's early warnings about old gods and sacred sites, the actual mechanism of the altered history, and the architect's identity. Do not pay them off or discard them without a user-approved outline decision.

**Novel-scale principle:** Emotional continuity matters more than incident count. A chapter may remain gentle, but something from it should carry into the next chapter: a choice, obligation, worry, developing attraction, earned competence, new trust, unresolved resentment, changed schedule, or physical reminder.

---

## 8. Prose and scene rules

- Write **original third-person limited prose**. Do not reproduce Rick Riordan's distinctive wording or copy passages. A mythological setting, humor, and camaraderie do not require stylistic imitation.
- One focal character per scene, usually Percy, Annabeth, or Thalia. Shift perspective only after a `---` break and immediately establish whose perceptions govern the new scene. No unexplained omniscience or mind-reading.
- Use natural, character-specific dialogue. **Percy** should not speak exactly like **Annabeth**, and **Thalia** should not use the same therapy-fluent language as everyone else. Let emotion emerge through action, evasion, bad timing, interruption, and subtext as well as honest conversation.
- No `POV:` labels, bracketed drafting headers, game-rule/debug output, author commentary, or text about word counts embedded inside narrative scenes.
- Select details that change a reader's understanding of action or character. The smell of a forge can matter when Silena recognizes Charlie's work; another inventory of air, skin, fabric, and heartbeat does not automatically improve romance.
- Establish outfits once, then change their description when clothing becomes wet, torn, borrowed, too warm, too small, or otherwise relevant. Keep objects and injuries consistent within and across chapters.
- Vary sentence lengths naturally. **The old “at most one *and* per sentence” rule is retired.** Do not imitate its clipped fragments, but avoid uncontrolled run-ons. Let syntax serve the scene.
- Watch for repeated narrative formulas: “the weight of,” “we'll figure it out,” “done being afraid,” automatic emotional interpretations after a telling gesture, and repeated sensory tags. These are editing prompts, not prohibited word lists.
- Expand scenes through changed behavior, obstacles, reaction, setting interaction, and aftermath, **not** synonym substitutions, padded inventories, or additional reconciliations that repeat an earlier one.

### What a well-developed scene does

A scene should generally have a **present objective**, **a source of friction or uncertainty** (even mild), **specific behavior**, and **an outcome that matters afterward**. Fluff can satisfy all four: trying to bake a birthday cake while keeping it secret is an objective; jealousy over help, burnt batter, or a sibling with the wrong timing supplies friction; the resulting private joke or hurt feeling becomes a later callback.

---

## 9. Drafting workflow and quality gates

**Default scope:** Work in **five-chapter batches** unless the user changes it. For a revision, modify only the approved chapter(s), not neighboring chapters as a side effect. Keep backups or a focused Git branch/PR before substantive edits.

### 9.1 Required input for a chapter writer

Provide all of these:

- This bible, plus explicit overrides or unresolved questions.
- The **actual final scene** of the preceding canonical chapter, not only a plot summary.
- Current chapter number, title (if fixed), date/season, POV, and intended scene sequence.
- A compact continuity handoff: ages, households, injuries, active gifts/props, romantic status, unfinished arguments, arrivals, promises, and mystery threads, **plus the last confirmed shared scene, existing forms of address, and knowledge provenance for every major character in the next scene**.
- Body-word minimum and the requested emotional centerpiece, Percabeth beat, and sibling beat.

Subagents may help, but they receive the same bounded sources and must not invent changes to locked canon.

### 9.2 Acceptance checklist

| Gate | What to verify | Pass condition |
|---|---|---|
| **Canon** | Names, parentage, siblings, cabins, memory rules, ages, power ownership | No unexplained conflicts with locked rules |
| **Continuity** | Date, elapsed time, weather, travel, props, clothing, injuries, known facts, promises | Events follow coherently from preceding chapters |
| **Character memory** | Prior meetings, titles/nicknames, disclosures, promises, objects, trust changes and who personally witnessed each event | No relationship reset or knowledge leak; a callback follows the character-specific ledger |
| **POV** | Knowledge and perception within each scene | One clearly identifiable focal character per scene |
| **Character** | Voice, desires, mistakes, realistic boundaries, unforced resolutions | Conflict and affection are specific, not interchangeable |
| **Scene purpose** | Unique centerpiece, Percabeth development, sibling development | Beats are earned and change something |
| **Prose** | Pronouns, grammatical contractions, exposition, repetitious sensory phrases | Correct, natural, clear and varied |
| **Duplication** | All consecutive **300-word** sequences compared across every chapter, at every word offset | No unapproved verbatim reused scene of this length |
| **Length** | Chapter body only, titles, dividers, metadata, and notes removed | At least 10,000 body words for a newly drafted full chapter (or a documented user exception) |
| **Build** | Numeric ordering, UTF-8, markdown separation, export legibility | Successfully reassembled and inspected |

**Duplication method matters:** Run a full sliding-token window or equivalent rolling-hash check over every consecutive 300-word sequence. Do **not** inspect only the start of paragraphs, sample every hundred words, or use a global replace/delete operation on repeated fragments. If a duplicated scene is found, rewrite the *later occurrence* coherently and confirm its surrounding narrative still works.

### 9.3 Word-count method

For consistency, count whitespace-separated words from **chapter body text**, excluding chapter heading lines, `---` dividers, standalone planning notes, and non-narrative metadata. Note that tokenization conventions can differ slightly; use one script or manifest method consistently, not hand estimates. A chapter above 10,000 words still fails if it lacks coherent scene development.

### 9.4 Revision and release protocol

1. Record the problem, evidence (chapter and excerpt), locked rule implicated, and proposed change. Mark **confirmed**, **suspected**, or **requires author decision**.
2. Preserve the original; make the smallest scene-level coherent revision in its own file or branch.
3. Re-read the previous chapter's closing scene, the edited chapter, and the next chapter's opening to catch handoff errors.
4. Check newly introduced facts against other affected chapters; record necessary follow-up edits instead of silently changing distant chapters.
5. Run word count, canon checks, and duplicate checks; rebuild in numeric order.
6. Inspect compiled reader output, including beginning, middle, ending, chapter order, and visible text quality.
7. Commit with a clear scope and an editorial change summary. Update the continuity ledger and unresolved-issues log.

**Do not declare a batch complete solely because files exist or a PDF opens.** Report actual checks performed and what remains incomplete.

---

## 10. Known historical deviations and open checks

**These are documented risks from earlier versions, not automatic claims that the newest GitHub import still contains each error. Confirm against selected source files before fixing.**

| Issue | Required direction | Disposition |
|---|---|---|
| Thalia becomes the rewrite architect or an eclipse restores Athena parentage | Maintain unknown architect and Annabeth's Zeus parentage unless user changes canon | **Audit** historical material and current relevant chapters |
| Thalia gains complete memories of the erased life | Only Percy and Annabeth retain firsthand erased-life memories; other characters retain only what they explicitly heard or witnessed | **Audit** and flag deliberate exceptions for approval |
| Annabeth loses Percy, their romance, or Tartarus memories | She retains them from the opening | **Audit** early and mid-story scenes |
| Clarisse/Silena revert to Ares/Aphrodite, or new Poseidon sisters appear | PCS parentage and membership remain fixed | **Audit** names and cabin affiliations |
| Annabeth is called Jackson or related to Percy as a sibling | Annabeth Grace, Zeus daughter, Percy's partner | **Audit** and correct only proven mistakes |
| Sally's death appears in Percy's remembered original childhood | Sally died at age two **only in altered history** | **Audit** recalled memories and grief scenes |
| Ages, seasons, returning visitors, gifts, injuries, and powers jump | Maintain a dated continuity ledger | **Audit** transitions and new drafts |
| Reused long passages and mismatched chapter handoffs | Whole-manuscript 300-word window check; scene-level repair | **October 17 PR #103 follow-up after starting from 697741f:** 1,942,016 chapter-only and 2,092,568 bonus-inclusive every-offset 300-word windows across 196 chapter/bonus files; 0 exact matches in either scan. Scene ledgers cover all 193 chapters; cumulative semantic reconciliation remains in progress |
| Per-chapter word minimum | User requested 10,000 body words each | **October 17 PR #103 follow-up:** 193/193 chapters meet the minimum, with zero shortfall. This does not certify prose quality or literary approval. Hosted checks passed on commit `33fc2d0` |
| Older PDFs or root chapter files differ from corrected sources | Respect the GitHub source selected for this pass and rebuild exports from the reviewed branch | **Not reconciled**; do not claim historical editions match this source |

**Historical export note:** A chapter 20–21 sibling/cabin correction was reportedly made to `Vol1_CampArc_250k_SiblingFix.pdf` and source files on 2026-10-09. That was a bounded correction, **not** evidence of a complete all-chapter sibling audit. Chapter 20 has now received scoped Cabin Three/identity clarification on the 2026-10-13 audit branch; Chapter 28's erroneous fifteen-year-old Thalia and incorrect 'Chase' address were also corrected. The old PDF's exact text still has not been reconciled.

**PDF production:** Retain UTF-8; repair mojibake from a verified source rather than deleting replacement glyphs. Use clear chapter starts, readable spacing, page numbering, correct markdown conversion, and text inspection of actual rendered pages, not just file size or the `%PDF-` header. The user's prior export destination was `C:\Users\dmcfu\OneDrive\Documents\Default Project\TheSeaRemembers\`; access to this path depends on the user's connected machine.

---

## 11. Reusable chapter assignment

> **Assignment:** Draft or revise Chapter **[NUMBER]**, **[TITLE]**, of *The Sea Remembers, the Sky Forgets*. Use this bible, the authorized chapter source, the immediately preceding canonical chapter's final scene, and the supplied continuity handoff. Preserve Percy/Clarisse/Silena as Poseidon's children; Thalia/Annabeth Grace as Zeus's daughters and biological sisters; Percy/Annabeth as established romantic partners who remember their prior life. Keep the timeline architect unknown, and do not use discarded draft deviations as canon. Write original third-person limited prose with one focal character per scene and `---` scene breaks. Prioritize a distinct, developed cozy centerpiece, a meaningful and age-appropriate nonsexual Percabeth moment, and reciprocal sibling interaction. Use natural, differentiated dialogue and purposeful sensory detail; let conflict and repair feel earned. Meet the approved body-word minimum, without padding. Before delivery, check continuity, count words, and screen for 300-word verbatim overlaps. Deliver only the assigned file(s), the actual count, changed facts, unresolved questions, and a concise handoff for the next chapter.

### Handoff fields (complete every time)

```yaml
chapter: 000
status: draft | revised | approved
date_or_season: unknown
point_of_view: Percy | Annabeth | Thalia
body_word_count: 0
opening_location: unknown
ending_location: unknown
characters_and_ages: []
active_relationship_tensions: []
last_shared_scenes_and_chapters: []
forms_of_address_and_existing_intimacy: []
firsthand_events_remembered: []
secondhand_knowledge_and_source: []
secrets_unknown_to_each_character: []
prior_life_memories_percy_annabeth_only: []
injuries_and_care: []
objects_gifts_and_projects: []
new_knowledge_or_promises: []
ongoing_plot_threads: []
next_chapter_dependencies: []
unresolved_canon_questions: []
```

**Editing principle:** Preserve what the characters have earned; fix contradictions without erasing their emotional histories. Do not write the next chapter as if everyone has forgotten the last one.
