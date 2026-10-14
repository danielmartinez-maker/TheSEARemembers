# Bounded age and chronology pass — 2026-10-13

## Authority and scope

Reviewed the isolated `codex/age-continuity` worktree at `4da559a`, based on GitHub `main` commit `63ae90bb6aad31753fcabfd057a1771359594dca` plus the approved plan and previously verified continuity changes. The current chapter files and [FIC_CONTEXT.md §6](../../FIC_CONTEXT.md#L191) govern this pass; the deprecated computer manuscript was not used. The opening ages are Percy 12, Annabeth 12, Thalia 16, Clarisse 13, and Silena 14. Explicit birthday and elapsed-time evidence controls later ages; unknown dates remain unknown.

This pass reviews the reported age candidates in Chapters 028, 048, and 062, their immediately preceding final and following opening scenes, and supporting passages in Chapters 005, 020, 060, 061, and 065. It is not a complete age ledger or a full literary reread of those chapters or the whole manuscript. Searches supplied candidate locations; the scene reads listed below supplied the context for the decisions.

## Finding and exact repair

**Confirmed — Chapter 028 calls Thalia fifteen after her sixteenth celebration.**

- [Chapter 020, lines 15–19](../../chapters/020-cake-and-lightning.md#L15) now explicitly says she is already sixteen and never had a proper sixteenth party. This is a belated celebration, not a new birthday at which she first turns sixteen. [Line 789](../../chapters/020-cake-and-lightning.md#L789) calls it her “belated sixteenth party”; [lines 1009–1019](../../chapters/020-cake-and-lightning.md#L1009) distinguish the cake on the actual day and wish her “Happy belated sixteen.” The planning exchange, Annabeth's gift scene, the bonfire/candle passage, and the walk home were read in context.
- [Chapter 028, line 147](../../chapters/028-sparring.md#L147) described the present-day Thalia arriving for Monday dawn drills as “She was fifteen.” The entire scene at lines 69–179 was read, along with the preceding Saturday scene and following Tuesday opening. It contains no flashback, age reversal, or intervening birthday that could justify fifteen.
- [Chapter 029, line 505](../../chapters/029-rainy-day.md#L505) describes Thalia's present face as looking “older than sixteen,” in a sister/card-game argument. The argument and repair passage around that reference was read to distinguish present age from a recollection.

**Change:** In Chapter 028 line 147, replace only `She was fifteen,` with `She was sixteen,`. No date, birthday, dialogue, event, POV, or relationship fact is added. The one-word replacement preserves the file's existing encoding and line endings.

## Previously reported candidates that do not reproduce

| Candidate | Current evidence and decision |
|---|---|
| Chapter 048: Thalia sixteen versus “Fifteen and twelve” during Zeus's visit | [Line 124](../../chapters/048-accused.md#L124) says Thalia sixteen and Annabeth twelve; [line 238](../../chapters/048-accused.md#L238) already says “Sixteen and twelve.” The gathering and visit through breakfast departure, lines 104–571, were read. Both references describe the same visit consistently. No edit. |
| Chapter 062: Annabeth twelve after being thirteen in Chapter 061 | [Chapter 061 line 15](../../chapters/061-fall.md#L15) says Annabeth thirteen like Percy and expressly places her birthday in July. Its closing scene [line 935](../../chapters/061-fall.md#L935) again calls them two thirteen-year-olds. [Chapter 062 line 105](../../chapters/062-snow-day.md#L105) already says “Thirteen now, like Percy.” The Snow Day opening and arrival scene, lines 3–149, were read. No edit. |
| Chapter 065: later Annabeth-thirteen reference from the previous audit | The current chapter contains no explicit `thirteen` or `twelve` Annabeth age reference. The opening arrival scene, early-April training introduction [line 75](../../chapters/065-triton-s-lesson.md#L75), and the equipment scene containing the former line-433 location were read. It does not supply the historical quoted age anchor; do not cite that old quotation as current evidence. No edit. |
| Chapter 005: sisters arrived at five and had been at camp seven years | The current chapter no longer contains the paired age-five/seven-years arrival claim. Its opening patrol scene was read; whole-file searches for the old ages, elapsed years, arrival, and `since` references did not reproduce it. [Chapter 028 line 5](../../chapters/028-sparring.md#L5) now separately says Clarisse has been at camp since eight. The reviewed passages do not establish Silena's exact arrival age or the intended historical elapsed years. No edit and no invented arrival dates. |

## Scene handoffs and chronology markers

| Boundary or supporting passage | Confirmed handoff | Inferred or unknown |
|---|---|---|
| 027 final → 028 opening | Chapter 027 closes with Nico's completed archive exhibition and dinner; Chapter 028 opens in Clarisse's perspective at a Saturday arena spar, arranging Monday dawn training. Thalia's corrected arrival is in the subsequent Monday scene, and the next scene advances to Tuesday. | The calendar date and gap from the exhibition to Saturday are unknown. |
| 028 final → 029 opening | Chapter 028 closes after Sunday's final dawn spar: the five campers go to breakfast and agree to continue training next week. Chapter 029 opens with Tuesday sword practice interrupted by rain. These scenes were read in full; the age edit changes no training or next-week promise. | A following Tuesday is implied; no numbered date is assigned. |
| 047 final → 048 opening → 049 opening | Chapter 047 closes on a snowy night with fear about the stolen bolt. Chapter 048 expressly opens in early June, with winter behind them, then Zeus visits. Chapter 049 opens before dawn with the siblings summoned to the Big House for Rachel's preparation. The boundary scenes were read in full. | The precise elapsed interval from the winter ending to early June remains unspecified; Chapter 049 does not supply a numbered day or a new age-changing birthday. |
| 060 final → 061 opening and ending | Chapter 060 closes at the final summer campfire; Chapter 061 opens on the second Saturday in September with Annabeth thirteen after her July birthday. Chapter 061 closes on the day before December, with Percy and Annabeth thirteen. These boundary scenes were read in full. | Annabeth's exact July birthday day and Percy's birthday date are not established by these reviewed passages. |
| 061 final → 062 opening → 063 opening | Chapter 062 looks back on a long November, brings the winter-break visitors together, and keeps Annabeth thirteen. Chapter 063 opens on the first warm March morning with spring cleaning. These opening scenes and Chapter 061's final scene were read in full. | No exact Snow Day date or year is stated here. The timing of “winter break” relative to November/December remains under-evidenced; no date was inserted. |

The Chapter 028 scene uses the sea-fed saltwater Tempest Hall pool, not the freshwater canoe lake. The repair leaves its location, dawn sequence, weapons, bruises, towels, muffins, training rules, and all five characters' arrival/departure behavior intact. Percy and Annabeth remain established romantic partners. Thalia is Annabeth's older sister; Clarisse and Silena remain Percy's Poseidon half-sisters. No autobiographical memory is added by changing the present age.

## Counts and manuscript QA

Counts use the repository's `scripts/audit_chapter_length.py` `body_word_count` function: whitespace-delimited body words, excluding headings, dividers, and Markdown comments. Metadata is not counted. Only Chapter 028 is edited; Chapters 048 and 062 were recounted as assigned comparison checks.

| Chapter | Before | After | Result |
|---|---:|---:|---|
| 028 | 10,049 | 10,049 | Pass ≥10,000 |
| 048 | 10,119 | 10,119 | Pass; unchanged |
| 062 | 10,010 | 10,010 | Pass; unchanged |

QA: reviewed the changed scene with its immediately preceding scene and following opening; reviewed Chapter 027's last scene, Chapter 028's last scene, and Chapter 029's first scene; checked the comparison boundaries stated above; inspected the one-word source diff; confirmed UTF-8 decoding and retained Chapter 028 line endings; recounted all three assigned chapters; and ran `git diff --check`. No software tests were expected or run. This task does not certify whole-manuscript duplicate coverage; the coordinated pass handles that separately.

## Remaining questions and limits

- Exact birthday/calendar dates not present in the reviewed passages remain unknown. Thalia is sixteen at the corrected Chapter 028 scene; this does not set later ages without later birthday evidence.
- The old Chapter 005 paired arrival claim has been removed from current source. Silena's exact arrival age and the historical intended elapsed years are not reconstructed or resolved here.
- Chapter 065 no longer carries the previous audit's Annabeth-thirteen quote. Chapter 061's July birthday and Chapter 062's explicit thirteen provide the current bounded age evidence; no exhaustive 063–065 age or chronology audit is claimed.
- The winter/early-June transition at 047→048 and winter-break timing in 062 have only broad seasonal anchors. Their precise elapsed dates are not resolved by this pass.
- Chapter 063's [line 755](../../chapters/063-spring-cleaning.md#L755) says Percy and Annabeth grin “twelve again.” Reading the complete shrine scene in context resolves this as figurative: the preceding paragraph says everyone is finding “the kid they used to be,” and nothing in the scene changes the explicit thirteen-year-old ages from Chapters 061–062. It is not an evidenced age-reset contradiction, so no manuscript repair is warranted. The wording remains a figurative age reference, not a new birthday or chronological fact.
- Other chapter ages, birthdays, school years, and late-arc adulthood require their own source-grounded reviews. The central continuity ledger and expansion tracker were not changed by this task.
