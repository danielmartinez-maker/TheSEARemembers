# Four-phase manuscript improvement: verified execution record

**Local date:** October 14, 2026 (Monterrey; GitHub run timestamps may show October 14 UTC)
**Repository:** `danielmartinez-maker/TheSEARemembers`  
**Source base:** `main` at `63ae90bb6aad31753fcabfd057a1771359594dca` contains the previous quality-pass merge (#100). The historical `rewrite/chapters-10k-quality-pass` branch is one commit behind main, with no unmerged commits.  
**This change branch:** `audit/four-phase-continuity-2026-10-13`, started from the open draft PR #102 head `1a3d83d528973e94c6d6c0e1a91ef606b45c71db` to preserve its unmerged continuity fixes. **Do not directly merge the old quality-pass branch.**  
**Do not confuse an audited chapter with a completed literary revision.**

## Phase 1: Cumulative memory, relationships, witnesses, secrets, chronology

**PARTIAL, NOT 193/193 SEMANTICALLY CERTIFIED.**

- Inherits the explicit witnessed-knowledge and relationship state ledger from PR #102: [Character memory ledger](../../continuity/CHARACTER_MEMORY_LEDGER.md) and [handoff schema](../../continuity/CHAPTER_MEMORY_HANDOFF.md).
- Added [chapter ledger 001–048](../../continuity/chapter-ledgers/001-048.md): Chapters 001–024 are now full-scene verified with adjacent boundary checks; 025–048 remain explicit TODO placeholders. Added [chapter ledger 049–060](../../continuity/chapter-ledgers/049-060.md), which records its partial-reading limits and does **not** certify every scene in that range. Added [chapter ledger 061–068](../../continuity/chapter-ledgers/061-068.md), whose full assigned chapters and adjacent boundary scenes were read. See also the new [Chapter 118 handoff](../../continuity/ch118.yaml).
- Added source-checked details from Chapters 011, 012, 017, 023, 066, 067, 068, 112, 132 and 133. Chapter 011 recalls Amphitrite's bag preparation; Chapter 012 tells Thalia limited earlier-life information (secondhand to Thalia, never her own future memory) and distinguishes Bianca hearing about a dream from witnessing a remembered Atlantean childhood scene. Chapters 017/023 record a bounded but incompletely specified report to Percy's sisters, the kitchen group's limited Sally information, and Annabeth's private clarification. Chapter 112 distinguishes writing/sending a letter from Amphitrite's unverified receipt.
- The evidence index generator now reads **all 193 chapter files** and writes [193 provisional chapter source locators](../../continuity/evidence/generated-ch001-193.md) and [structured JSON](../../continuity/evidence/generated-ch001-193.json). Every entry explicitly marks witnesses, relationships, personal knowledge, chronology and secrets as **UNVERIFIED** until a human scene-level review.
- Unreviewed appearances or dialogue cues are **not** promoted into a character's memory. The index is a queue, not a substitute for reconstructing each character's actual experiences.

**Additional source-confirmed handoffs:** Chapters [066](../../continuity/ch066.yaml), [067](../../continuity/ch067.yaml), [068](../../continuity/ch068.yaml), [069](../handoffs/ch069-silenas-song.md), [118](../../continuity/ch118.yaml), [132](../../continuity/ch132.yaml) and [133](../../continuity/ch133.yaml) now have scene-scoped handoffs. Ch. 067's private reciprocal Atlantis/Olympus promise is **Percy/Annabeth-only** knowledge, not a confirmed itinerary. Ch. 068 distinguishes Bryce's public apology from Annabeth's own forgiveness and the dangerous assumption that Percy can act as an electrical ground. Ch. 118 leaves the Atlantis trip unbooked, the map unsigned, and Amphitrite uninformed of Percy's private memory predicament. Ch. 132 separates an actual Poseidon invitation from a still-undelivered note addressed to Triton.

**Still required:** full scene-by-scene review of all 193 chapters, verified per-person event/knowledge transitions, first-vs-secondhand records, and resolved relationship/departure/prop/injury handoffs. The 061–068 ledger also records open items such as unknown exact dates, unconfirmed correspondence receipt, and an unplaced training morning rather than inventing answers.

## Phase 2: Substantive continuity repairs

**PARTIAL.**

The branch incorporates PR #102's 21 reported localized corrections across Chapters 030, 086, 099, 118, 120, 123, 126 and 127. The source-anchored memory regression script passed nine checks on the first full-manuscript CI run. Important corrected anchors: Amphitrite remembers prior meetings with Clarisse, Silena and Annabeth; Percy remembers calling Amphitrite Mother (Ch. 099), then Mom (Ch. 118); Amphitrite does not know the erased future or Percy's altered-childhood memory gap (Ch. 126–127); Triton recognizes his siblings from Ch. 032.

This pass adds **four exact localized prose replacements**:
1. Ch. 020, Silena's appeal is explicitly Silena's own charisma, not an apparent implication that she belongs to the Aphrodite cabin.
2. Ch. 020, Clarisse and Silena are at **Cabin Three's** craft table, not presented as working in their own Ares cabin.
3. Ch. 028, Thalia is **sixteen**, consistent with Ch. 016, 020 and 024, not inexplicably fifteen after Ch. 020.
4. Ch. 028, Clarisse calls Annabeth **Grace**, not **Chase**, in a current-life training scene.

Added regression guards for these two files, expanding targeted chapter checks from 9 to 11. No unnamed scene was mass-rewritten; all four replacements matched their original source span exactly once.

The bounded age/chronology review is recorded in [the source-cited age report](age-chronology-pass-2026-10-13.md). It supports the Chapter 028 age repair, verifies several earlier reported age candidates as non-reproducing on current source, resolves Chapter 063's “twelve again” as figurative in its full scene context, and leaves exact birthdays and unreviewed chronology explicitly unresolved.

**Chapter 126/127 secrecy re-review:** the Chapter 126 training-stage scene still had Percy tell Amphitrite “I wish I remembered,” followed by her “I know,” directly disclosing that he cannot recall an altered-childhood incident. The exchange is now a discussion of the repair and his determination as a child; the scene preserves the recollection as Amphitrite's and the ledger as the record. Percy tells Triton and Tyson about specific missing childhood memories in separate conversations, but Amphitrite is absent. Chapter 127's “we can learn who you are now” remains a present-focused reassurance, with no stated awareness of Percy's private memory gap. The regression guard now checks that the direct disclosure does not return.

**Additional continuation corrections on the PR #103 branch:** Chapter 149 no longer attributes Thalia's erased tree/Hunter history to Clarisse's memories. Chapter 176 dates the storm to Wednesday; Chapter 177's Tuesday postmark now correctly describes the day before it. The October 23 bonus scenes now place Rhys and Thalia's relationship at a little over two weeks since his announced Friday return in Chapter 175, and label Thalia's next-day visit with Chiron as a follow-up to the Sunday examination in Chapter 193.

**Known boundary:** Percy, Annabeth alone retain previous-life first-person memories. Thalia may remember a *report* Percy told her in Ch. 012 but never experiences that life herself. Amphitrite is not told the secret. Poseidon siblings Percy, Clarisse, Silena and Zeus/Grace siblings Thalia, Annabeth, Jason remain locked. No broader whole-novel contradiction-free claim is supported.

**Still required:** semantic inspection of every character-return scene, relationship carry-over, age transition, all other potential contradictions and their downstream chapters, and independent review of the inherited PR #102 prose changes.

## Phase 3: Expand all sub-10,000 full chapters

**PARTIAL: Chapters 066, 067, 068, 069, 118, 132 and 133 expanded to 10,000+ body words; 48 chapters still below threshold on the current local snapshot. Independent prose signoff remains open.**

The latest local count covers all 193 numbered Markdown chapters, excluding headings, scene separators and comments from whitespace-separated narrative body words. **145 pass** the 10,000-word floor; **48 remain short**; the combined deficit is **243,056 actual body words**. Both GitHub Actions workflows passed on the then-pushed narrative head `5edf61f5b41aca80170955941457292c7310b188`; later local changes in this report snapshot add only continuity/audit documents, so a fresh workflow run is still required after those documents are pushed. The earlier pre-expansion baseline was 138 passing / 55 short / 267,533 missing.

| Range | Short chapters | Words needed to 10,000 |
|---|---:|---:|
| 066–090 | 21 | 83,630 |
| 091–110 | 20 | 119,269 |
| 114–120 | 6 | 35,790 |
| 131–133 | 1 | 4,367 |
| **Total** | **48** | **243,056** |

**Verified continuation edits:** [Chapter 066](../../chapters/066-jason-s-letter.md) increased from **8,314 to 10,572 body words** after a shore-safety signaling scene; [Chapter 067](../../chapters/067-fishing.md) from **5,758 to 10,292** after dock safety, harvest choices and a supervised lesson; [Chapter 068](../../chapters/068-the-storm-small.md) from **5,529 to 10,328** after a consent-based follow-up scene; [Chapter 069](../../chapters/069-silena-s-song.md) from **6,001 to 10,118** after Silena chooses how to sing at a public event; [Chapter 118](../../chapters/118-a-message-from-amphitrite.md) from **4,921 to 10,464** after reply drafting, a security-aware camp portrait map and a real coverage check; [Chapter 132](../../chapters/132-a-month-beneath-the-sea.md) from **6,296 to 10,243**; and [Chapter 133](../../chapters/133-annabeth-s-birthday.md) from **8,704 to 10,656**. These seven expansions added **27,150 net body words**. Current local QA finds **145 length-passing chapters, 48 short and 243,056 words still needed** after Chapters 118 and 069 but before the next expansion batches are merged. Per-chapter handoffs record the narrative changes and open questions.

See [the original expansion tracker and writing queue](../handoffs/55-short-chapters-execution-queue.md). A packet is **not** a drafted chapter. The remaining 243,056 missing words require actual scenes with purpose and consequences, not indiscriminate padding.

**Still required:** expand the remaining 48 short chapters, inspect their adjacent scenes, recount and QA every revision, and attach its own continuity handoff. Chapters 066 and 133 also warrant independent prose-level and developmental review.

## Phase 4: Whole-manuscript QA and handoffs

**MECHANICAL QA PASSES ON THE CURRENT LOCAL SNAPSHOT; SEMANTIC/STYLE REVIEW INCOMPLETE.**

The latest local full-manuscript run screened **193/193** numbered files and **1,687,246** overlapping 300-body-word windows at every offset, with rolling-hash candidates confirmed by exact token comparison. It found **zero exact cross-chapter matches**, **zero missing numbered chapters**, **145 length passes**, **48 short chapters** and **243,056 body words still needed**. A second pass across all **196** chapter and bonus Markdown files checked **1,837,798** 300-word windows (**1,896,103** body words) and also found zero exact matches. Chapter-order/structure/UTF-8 checks reported **193 indexed and 193 numbered files, in order**, with no errors. The **16 source-anchored character-memory regression checks** passed. GitHub Actions workflows [38588840375](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38588840375) and [38588840979](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38588840979) passed on pushed head `5edf61f5b41aca80170955941457292c7310b188`. The only later local changes at this report snapshot are continuity/audit docs; run the workflows again after pushing them. Earlier Actions runs [38508276354](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38508276354) and [38508604807](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38508604807) apply to older content, not these numbers.

The added scenes were read against the preceding chapter closing scenes and next chapter openings, with character-specific sidecar handoffs. Neither these checks nor the generated cue index certifies a complete novel-wide semantic reading.

**Not assessed or not certified:** semantic paraphrase duplicates, repeated story beats under different wording, stylistic sameness, dialogue authenticity, character psychology, full scene coherence, hidden knowledge leaks, every gift/prop/injury carryover, and newly added narrative word quality. Textual absence of a 300-word repeat is not proof of absence of semantic repetition.

**Permanent tools and outputs:**
- [Full-manuscript QA script](../../scripts/full_manuscript_qa.py)
- [193-chapter evidence index script](../../scripts/build_memory_evidence_index.py)
- [Source-anchored memory regression script](../../scripts/check_character_memory.py)
- [Chapter structure and index audit](../../scripts/audit_chapter_structure.py)
- [Bonus-inclusive exact-window audit](../../scripts/audit_duplicate_windows.py)
- [Generated JSON word counts and flagged cues](generated-full-qa.json)
- [Generated readable word counts](generated-full-qa.md)
- [Generated chapter structure report](generated-chapter-structure.json)
- [Generated all-Markdown 300-word report](generated-all-text-300-word-qa.json)
- [Generated per-chapter evidence queue](../../continuity/evidence/generated-ch001-193.md)
- [GitHub Actions full-manuscript workflow](../../.github/workflows/full-manuscript-audit.yml)

## Open editorial signoff

- **Do not merge as a final literary 10k manuscript release.** This PR can be reviewed as continuity fixes plus verified audit infrastructure.
- The PR is a draft, allowing previously unmerged PR #102 edits to be considered together with the new corrections without rewriting `main` by surprise.
- Additional expansion and semantic editing work must be sequenced through the 12 handoff packets and submitted with original scene changes, individual word counts, and evidence-based relationship updates.
- Historical PDF editions and designated local working chapters have not been reconciled byte-for-byte to this GitHub snapshot. This PR changes GitHub sources only; it does not certify published reader editions.

**Completion verdict:** Phase 1 partial (193 provisional locators; scene-verified ranges 001–024 and 061–068, partial 049–060, other ranges still unverified); Phase 2 partial (confirmed specific corrections, not all contradictions); Phase 3 partially implemented (7 length passes, 48 short); Phase 4 mechanical checks passed on pushed narrative head, full semantic/style and all-character continuity signoff still incomplete.
