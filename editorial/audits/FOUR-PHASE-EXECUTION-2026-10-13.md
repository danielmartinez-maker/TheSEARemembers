# Four-phase manuscript improvement: verified execution record

**Local date:** October 13, 2026 (Monterrey; GitHub run timestamps may show October 14 UTC)  
**Repository:** `danielmartinez-maker/TheSEARemembers`  
**Source base:** `main` at `63ae90bb6aad31753fcabfd057a1771359594dca` contains the previous quality-pass merge (#100). The historical `rewrite/chapters-10k-quality-pass` branch is one commit behind main, with no unmerged commits.  
**This change branch:** `audit/four-phase-continuity-2026-10-13`, started from the open draft PR #102 head `1a3d83d528973e94c6d6c0e1a91ef606b45c71db` to preserve its unmerged continuity fixes. **Do not directly merge the old quality-pass branch.**  
**Do not confuse an audited chapter with a completed literary revision.**

## Phase 1: Cumulative memory, relationships, witnesses, secrets, chronology

**PARTIAL, NOT 193/193 SEMANTICALLY CERTIFIED.**

- Inherits the explicit witnessed-knowledge and relationship state ledger from PR #102: [Character memory ledger](../../continuity/CHARACTER_MEMORY_LEDGER.md) and [handoff schema](../../continuity/CHAPTER_MEMORY_HANDOFF.md).
- Added source-checked details from Chapters 011, 012 and 112. Chapter 011 recalls Amphitrite's bag preparation, Chapter 012 tells Thalia limited earlier-life information (secondhand to Thalia, never her own future memory), Chapter 112 distinguishes writing/sending a letter from Amphitrite's unverified receipt. Chapter 012 also distinguishes Bianca hearing about a dream from witnessing a remembered Atlantean childhood scene.
- The evidence index generator now reads **all 193 chapter files** and writes [193 provisional chapter source locators](../../continuity/evidence/generated-ch001-193.md) and [structured JSON](../../continuity/evidence/generated-ch001-193.json). Every entry explicitly marks witnesses, relationships, personal knowledge, chronology and secrets as **UNVERIFIED** until a human scene-level review.
- Unreviewed appearances or dialogue cues are **not** promoted into a character's memory. The index is a queue, not a substitute for reconstructing each character's actual experiences.

**Still required:** full scene-by-scene review of all 193 chapters, verified per-person event/knowledge transitions, first-vs-secondhand records, and resolved relationship/departure/prop/injury handoffs.

## Phase 2: Substantive continuity repairs

**PARTIAL.**

The branch incorporates PR #102's 21 reported localized corrections across Chapters 030, 086, 099, 118, 120, 123, 126 and 127. The source-anchored memory regression script passed nine checks on the first full-manuscript CI run. Important corrected anchors: Amphitrite remembers prior meetings with Clarisse, Silena and Annabeth; Percy remembers calling Amphitrite Mother (Ch. 099), then Mom (Ch. 118); Amphitrite does not know the erased future or Percy's altered-childhood memory gap (Ch. 126–127); Triton recognizes his siblings from Ch. 032.

This pass adds **four exact localized prose replacements**:
1. Ch. 020, Silena's appeal is explicitly Silena's own charisma, not an apparent implication that she belongs to the Aphrodite cabin.
2. Ch. 020, Clarisse and Silena are at **Cabin Three's** craft table, not presented as working in their own Ares cabin.
3. Ch. 028, Thalia is **sixteen**, consistent with Ch. 016, 020 and 024, not inexplicably fifteen after Ch. 020.
4. Ch. 028, Clarisse calls Annabeth **Grace**, not **Chase**, in a current-life training scene.

Added regression guards for these two files, expanding targeted chapter checks from 9 to 11. No unnamed scene was mass-rewritten; all four replacements matched their original source span exactly once.

**Known boundary:** Percy, Annabeth alone retain previous-life first-person memories. Thalia may remember a *report* Percy told her in Ch. 012 but never experiences that life herself. Amphitrite is not told the secret. Poseidon siblings Percy, Clarisse, Silena and Zeus/Grace siblings Thalia, Annabeth, Jason remain locked. No broader whole-novel contradiction-free claim is supported.

**Still required:** semantic inspection of every character-return scene, relationship carry-over, age transition, all other potential contradictions and their downstream chapters, and independent review of the inherited PR #102 prose changes.

## Phase 3: Expand all sub-10,000 full chapters

**PARTIAL: Chapters 066 and 133 expanded to 10,000+ body words; 53 chapters still below threshold. Independent prose signoff remains open.**

New code reran a count of each of 193 numbered Markdown chapters, excluding Markdown headings, scene separators and comments from whitespace-separated narrative body words. **140 passed** the 10,000-word floor; **53 remain short**; the current combined deficit is **264,551 actual body words**. The earlier baseline was 138 passing / 55 short / 267,533 missing.

| Range | Short chapters | Words needed to 10,000 |
|---|---:|---:|
| 066–090 | 24 | 96,342 |
| 091–110 | 20 | 119,269 |
| 114–120 | 7 | 40,869 |
| 131–133 | 2 | 8,071 |
| **Total** | **53** | **264,551** |

**Verified continuation edits:** [Chapter 066](../../chapters/066-jason-s-letter.md) increased from **8,314 to 10,572 body words** after an added shore-safety signaling scene grounded in Chapters 065–067 and Jason's correspondence. [Chapter 133](../../chapters/133-annabeth-s-birthday.md) increased from **8,704 to 10,656** after a new pavilion-preparation scene that carries forward Annabeth's boundaries and the later map misunderstanding. New prose added **4,210 body words** in total, and the minimum-length deficit declined by **2,982** words. Per-character handoffs: [066](../../continuity/ch066.yaml) and [133](../../continuity/ch133.yaml).

See [the original 55-chapter tracker, now 53 still short, with 12 dependency-safe writing packets](../handoffs/55-short-chapters-execution-queue.md). A packet is **not** a drafted chapter. The remaining 264,551 missing words require actual scenes with purpose and consequences, not indiscriminate padding.

**Still required:** expand the other 53 short chapters, inspect their adjacent scenes, recount and QA every revision, and attach its own continuity handoff. Chapters 066 and 133 also warrant independent prose-level and developmental review.

## Phase 4: Whole-manuscript QA and handoffs

**MECHANICAL QA COMPLETED; SEMANTIC/STYLE REVIEW INCOMPLETE.**

The continuation audit [run 38507799236](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38507799236) **passed** after both expansion edits. It screened **193/193** numbered files and **1,664,234** overlapping 300-body-word windows at **every offset**, with rolling-hash candidate selection and exact token confirmation. **Zero cross-chapter 300-word matches**, **zero missing numbered chapters** and **zero structural/UTF-8 errors** were found. The recount yielded **140 length-passing chapters**, **53 short** and **264,551 body words still needed**. The **11 source-anchored character-memory regression checks** also passed. The earlier initial run [38505151582](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38505151582) recorded the historical 138/55 baseline, and must not be cited as current status.

The added scenes were read against the preceding chapter closing scenes and next chapter openings, with character-specific sidecar handoffs. Neither these checks nor the generated cue index certifies a complete novel-wide semantic reading.

**Not assessed or not certified:** semantic paraphrase duplicates, repeated story beats under different wording, stylistic sameness, dialogue authenticity, character psychology, full scene coherence, hidden knowledge leaks, every gift/prop/injury carryover, and newly added narrative word quality. Textual absence of a 300-word repeat is not proof of absence of semantic repetition.

**Permanent tools and outputs:**
- [Full-manuscript QA script](../../scripts/full_manuscript_qa.py)
- [193-chapter evidence index script](../../scripts/build_memory_evidence_index.py)
- [Source-anchored memory regression script](../../scripts/check_character_memory.py)
- [Generated JSON word counts and flagged cues](generated-full-qa.json)
- [Generated readable word counts](generated-full-qa.md)
- [Generated per-chapter evidence queue](../../continuity/evidence/generated-ch001-193.md)
- [GitHub Actions full-manuscript workflow](../../.github/workflows/full-manuscript-audit.yml)

## Open editorial signoff

- **Do not merge as a final literary 10k manuscript release.** This PR can be reviewed as continuity fixes plus verified audit infrastructure.
- The PR is a draft, allowing previously unmerged PR #102 edits to be considered together with the new corrections without rewriting `main` by surprise.
- Additional expansion and semantic editing work must be sequenced through the 12 handoff packets and submitted with original scene changes, individual word counts, and evidence-based relationship updates.
- Historical PDF editions and designated local working chapters have not been reconciled byte-for-byte to this GitHub snapshot. This PR changes GitHub sources only; it does not certify published reader editions.

**Completion verdict:** Phase 1 partial with new verified event entries; Phase 2 partial; Phase 3 partially implemented (2 additional chapters length-pass, 53 short); Phase 4 mechanical checks passed on the edited manuscript, semantic/style signoff still incomplete.
