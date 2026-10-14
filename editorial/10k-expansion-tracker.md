# Full-manuscript 10,000-word expansion tracker

**Scope:** Chapters 001–193 (two bonus interludes are excluded from the 10k narrative-chapter rule).
**Working source:** `rewrite/chapters-10k-quality-pass` branched from `edit/chapters-001-036-unified` on 2026-10-12.
**Rule:** Each chapter must reach **10,000 body words**, preferably 10,200–11,200, *without filler*. A mechanical pass is not editorial approval.

## Latest current-branch continuation (2026-10-14 local snapshot)

**Source:** `audit/four-phase-continuity-2026-10-13`, latest Chapter 070 edit recount and arithmetic from the previous 193-chapter audit checkpoint. Subsequent historical sections below may refer to older snapshots. The complete newest-head CI run, rather than this arithmetic, is authoritative for corpus-wide results.

| Scope | Current verified result |
|---|---:|
| Numbered narrative chapters audited | **193** |
| At or above 10,000 actual body words | **146** (expected; pending new full-corpus CI) |
| Below 10,000 actual body words | **47** (expected; pending new full-corpus CI) |
| Required additional body words to clear minimum | **239,128** (expected; pending new full-corpus CI) |
| Exact cross-chapter 300-word duplicates | **0 across 1,687,246 windows on the preceding 145-pass snapshot**; newest-head scan pending |
| Source-anchored memory regression checks | **17 checks configured**; new Chapter 070 anchor set passed 8 direct comparisons; newest-head full run pending |

**Eight chapter expansion results since the 138/55 baseline**:

- [066, Jason's Letter](../chapters/066-jason-s-letter.md): **8,314 → 10,572** words; [memory handoff](../continuity/ch066.yaml).
- [067, Fishing](../chapters/067-fishing.md): **5,758 → 10,292** words; [memory handoff](../continuity/ch067.yaml).
- [068, The Storm (Small)](../chapters/068-the-storm-small.md): **5,529 → 10,328** words; [memory handoff](../continuity/ch068.yaml).
- [070, Clarisse's Poems](../chapters/070-clarisse-s-poems.md): **6,072 → 10,543** body words (**+4,471 net**); [character, prop and permission handoff](handoffs/ch070-clarisses-poems.md). Chapter length passes, but independent semantic/prose signoff is open.
- [069, Silena's Song](../chapters/069-silena-s-song.md): **6,001 → 10,118** words; [scene handoff](handoffs/ch069-silenas-song.md).
- [118, A Message from Amphitrite](../chapters/118-a-message-from-amphitrite.md): **4,921 → 10,464** words; [memory handoff](../continuity/ch118.yaml).
- [132, A Month Beneath the Sea](../chapters/132-a-month-beneath-the-sea.md): **6,296 → 10,243** words; [memory handoff](../continuity/ch132.yaml).
- [133, Annabeth's Birthday](../chapters/133-annabeth-s-birthday.md): **8,704 → 10,656** words; [memory handoff](../continuity/ch133.yaml).

These changes added **27,150 net body words** and eliminated **21,495 words of previously required shortfall**; over-threshold margins explain the difference. The [remaining expansion queue](handoffs/55-short-chapters-execution-queue.md) now starts in manuscript order at **070**, and also includes **131**. A mechanical length pass and absence of exact duplication are not a substitute for independent full semantic, dialogue, character-memory, plot and style review.

## Chapters 121–160 scoped length and quality checkpoint (2026-10-12)

**22 / 40 chapters** in this range have at least **10,000 body words**, as of the targeted revisions through commit `b278fc6615e9cc4193dc4c36709e08a95fa5ed9b`. **Every chapter 140–160 (21/21)** meets the mechanical minimum, as does **121 (10,632)**. The **18 remaining short chapters are 122–139**, collectively **94,887 words short** of their individual floors. Do not call the full range finished.

Revised passing counts beyond the existing baseline: **140 10,163; 141 10,030; 142 10,087; 143 10,136; 146 10,089; 147 10,143; 148 10,293; 149 10,387; 157 10,134; 158 10,149; 159 10,133**. Chapter 151, already over 10k, was canon-corrected to **10,823**. Chapters 122–123 were also corrected for inaccessible altered-childhood memory and saltwater versus freshwater geography, but remain short.

Chapters 147, 149 and 151 required additional memory-boundary repairs: Clarisse and Thalia cannot remember the erased Ares/Hunter/tree events, and only Percy and Annabeth remember the former timeline. No universal manuscript clearance should be inferred.

Source-specific prose changes, chapter-by-chapter counts, QA limits and open acceptance gates: [full 121–160 inventory](audits/ch121-160-inventory-2026-10-12.md) and [continuity handoff](handoffs/ch121-160-2026-10-12.md). These chapters pass **word count only**, not independent full-chapter literary or cross-range 300-word QA. Continue in order at **122**.

## Chapters 014–044 current 10k-length verification (2026-10-12)

**31 / 31 Chapters 014–044 meet the 10,000-body-word minimum**, each freshly fetched and recounted on this branch. The "first 36 chapters" table farther below records an earlier baseline and is **superseded** for Chapters 014–036. Do not use its old figures to plan subsequent work.

The final 13-chapter closeout (body words): **018 10,001; 019 10,003; 021 10,000; 023 10,014; 027 10,000; 029 10,005; 031 10,005; 032 10,001; 033 10,001; 040 10,005; 041 10,019; 042 10,133; 043 10,052**. The other 18 chapters in 014–044 were also individually fetched and verified at or above 10,000.

Check: **126,352 overlapping 300-word windows** across those final 13 chapters, with zero exact cross-chapter matching sequences, plus single heading and UTF-8 replacement-character checks. This was **not** a full 31-chapter repeat check, a semantic similarity review, a CI run, or a final editorial signoff. Chapters exactly at 10,000 words have no deletion margin.

Full counts, canon corrections and the Chapter 044 continuity handoff: [Chapters 014–044 final 13 editorial handoff](handoffs/ch014-044-final-13-length-qa-2026-10-12.md).

**Follow-up:** Chapter 036 now has **10,085 words** after removing an unapproved disclosure of Percy and Annabeth's erased history to Thalia. Chapter 043 now has **10,052 words** after a related correction to its Thalia/Silena dialogue. Rechecked a 300-word exact-repeat scan across the 13 targeted chapters **and Chapter 036**: **136,138 windows**, zero exact cross-chapter repeats (13-only subset: 126,352).

## Historical baseline length status on the first 36 chapters (superseded)

- Passing the length gate: **13 / 36** (001–013).
- Still short: **23 / 36** (014–036).
- Remaining body words to reach 10k for the short chapters in this verified range: **65,910**.
- **This table recounts Chapters 001–036; a separate dated inventory covers Chapters 045–090**. The manuscript's older reader-edition word counts are not reliable substitutes for current branch counts. Run `python scripts/audit_chapter_length.py --json editorial/latest-length-report.json` in a checkout to obtain the exact current all-chapter status; this will currently exit nonzero because many chapters are short.

| Chapter | Verified body words | Length status |
| --- | ---: | --- |
| 001 | 11,077 | Length pass |
| 002 | 10,834 | Length pass |
| 003 | 10,335 | Length pass |
| 004 | 10,928 | Length pass |
| 005 | 10,966 | Length pass |
| 006 | 10,639 | Length pass |
| 007 | 10,385 | Length pass |
| 008 | 10,650 | Length pass |
| 009 | 10,109 | Length pass |
| 010 | 10,087 | Length pass |
| 011 | 10,049 | Length pass |
| 012 | 10,035 | Length pass |
| 013 | 10,056 | Length pass |
| 014 | 8,200 | 1,800 short (recounted as adjacent chapter) |
| 015 | 6,543 | 3,457 short |
| 016 | 8,944 | 1,056 short |
| 017 | 6,168 | 3,832 short |
| 018 | 6,669 | 3,331 short |
| 019 | 6,185 | 3,815 short |
| 020 | 7,949 | 2,051 short |
| 021 | 7,165 | 2,835 short |
| 022 | 7,739 | 2,261 short |
| 023 | 5,171 | 4,829 short |
| 024 | 7,797 | 2,203 short |
| 025 | 7,637 | 2,363 short |
| 026 | 7,538 | 2,462 short |
| 027 | 5,182 | 4,818 short |
| 028 | 8,380 | 1,620 short |
| 029 | 6,365 | 3,635 short |
| 030 | 8,684 | 1,316 short |
| 031 | 5,806 | 4,194 short |
| 032 | 6,955 | 3,045 short |
| 033 | 6,590 | 3,410 short |
| 034 | 8,901 | 1,099 short |
| 035 | 7,275 | 2,725 short |
| 036 | 6,247 | 3,753 short |

## What is and isn't done

- Chapter 001's revised branch text already exceeded 10k.
- Chapters 002–013 were expanded and line-edited with **new story scenes**, attention to dialogue rhythm, distinct character agency, scene causality, and the established Percabeth, Grace-sister and Poseidon-sibling relationships. See dedicated handoffs and `editorial/prose-dialogue-acceptance.md`.
- Chapters 045–049 were later expanded above 10,000 body words as tracked in the separate 045–090 workstream. Other chapters outside the currently certified ranges must be verified independently; no blanket quality approval is claimed.
- After the Chapter 009–013 revisions, an exhaustive at-every-offset rolling-hash check with exact candidate verification scanned **140,164 consecutive 300-word windows** across current Chapters **001–014** and found **zero exact cross-chapter matches**. This is not a semantic originality review or a full 193-chapter certification. Chapter 014 was also recounted as an adjacent handoff chapter; Chapters 015–036 retain their previous tracker counts.

## Editorial release gate

For each chapter: read preceding final scene and following opening; map POV, ages, date, powers, props, injuries, secrets and promises; draft scenes with a concrete objective, opposition, choice and lasting consequence; preserve the existing character-specific voice; review for exposition loops and formulaic resolutions; count body words; run 300-word verbatim overlap check; update a dedicated continuity handoff; and review actual diff.

Prioritize **014–018**, then **019–036**, then perform an exact length inventory and ordered review for **037–193**. Expansion should not resolve the unknown time-rewrite architect, rewrite the memory rules, or disclose Percy's prior life to Amphitrite without explicit author instruction.

**Not merged:** This branch is an editing proposal; the parent 36-chapter branch remains unchanged.

## Editorial status as of 2026-10-12 (after Chapters 009–013)

The opening thirteen chapters pass **the length gate only**. Chapters 009–013 have completed a 10k expansion pass with targeted developmental, canon and dialogue revisions. Chapter 009 gives the illicit Oracle visits specific consequences; Chapter 010 establishes Zoe's independent ward evidence and training limits; Chapter 011 replaces an unsafe water-as-electrical-route sequence with a contained ward intervention and evacuation accountability; Chapter 012 repairs the prior chapter's structural and injury continuity; Chapter 013 preserves Zeus's volatility and refusal to provide reliable paternal support. Dedicated chapter handoffs 009–013 document remaining dependencies. **These are mechanical length passes and targeted editing passes, not independent line/copyedit or full developmental approval.** Verify the canonical working copies before using this branch as sole source of truth; full 193-chapter semantic-reuse checks and reader-edition build remain pending.

## Parallel Chapters 045–090 workstream (2026-10-12)

On this same branch, **Chapters 045–049** have now passed the **10,000-body-word length gate** with source-specific expansions and chapter handoffs. They are **not independently approved by developmental/line/copyedit reviewers**. Chapter counts: **045: 10,133; 046: 10,214; 047: 10,181; 048: 10,119; 049: 10,024**. The baseline audit of 046–090 had **46/46 below 10k** before this workstream; current **045–090** status is **5/46 passing**, with **41 chapters (050–090)** collectively missing **171,013** body words to reach the individual minimums.

Detailed baseline, rolling updates and scope caveats: [editorial/audits/ch045-090-inventory-2026-10-12.md](audits/ch045-090-inventory-2026-10-12.md). Handoffs: [045](handoffs/ch045-revision.md), [046](handoffs/ch046-revision.md), [047](handoffs/ch047-revision.md), [048](handoffs/ch048-revision.md), [049](handoffs/ch049-revision.md). These checks cover adjacent 300-word exact repetition but **not** a whole-manuscript scan. Other chapters may be changing concurrently; avoid claiming their baseline counts remain current without fetching them again.

## Quest arc 050–059 length pass (2026-10-12)

The **ten chapters from 050 Half-Blood Hill through 059 Homecoming** each now meet the 10,000 body-word threshold: **10,003; 10,009; 10,010; 10,027; 10,009; 10,014; 10,000; 10,080; 10,039; 10,097**. The ten-chapter body-word sum is **100,288**. Current **045–090** length tally is **15/46 passing** (045–059); **060–090** are **31** short chapters with **126,047** combined missing words, independently recalculated from all 31 current files.

QA: an all-offset exact 300-word scan across **045–060** found **no verbatim matching 300-word windows**. Chapter-specific narrative continuity and limitations are in [quest-arc handoff](handoffs/ch050-059-quest-quality-pass.md). Rolling inventory and baseline distinction: [chapters 45–90 audit](audits/ch045-090-inventory-2026-10-12.md). **These are mechanical length and exact-repeat passes only, not proof of final literary quality, semantic uniqueness or canonical-copy reconciliation.** Chapters 055/056 meet the floor with very little margin, so any future editing requires a recount. The next chapter is `chapters/060-summer-s-end.md`, currently **6,016** body words.

## Chapters 161–193: second-pass targeted prose revisions (2026-10-12)

The entire **33-chapter range now passes the per-chapter 10,000-body-word length gate**, verified by retrieving current branch files and recounting the narrative body: **362,416 total body words**. In the first pass, **162, 191 and 193** were expanded or structurally repaired; **191** also received a later repair of triplicate transitions, preemptive heel dialogue and Friday path chronology. In the second pass, the **30 remaining chapter files** (161, 163–190, and 192) received individual closing-scene revisions addressing recurring generalized endings, character agency, logistical obligations and continuity. Chapter 183 received a follow-up correction that preserves the mail sack's preexisting count of forty letters and two parcels. Chapter 192's deferred pine butt and damaged fence now hand off to the supervised Sunday work in 193.

**This is a verified length pass and targeted prose revision, not final literary approval**. All chapters still require an independent whole-chapter developmental and line edit. Exact 100-word repeated windows were checked at every offset **within** and **between** chapters in four adjacent blocks (161–169, 170–177, 178–185, 186–193): **0 exact matches in those blocks**. A later exhaustive within-chapter **50-word** repeat scan found and led to correction of repeated material in 191; final results were **zero exact nonoverlapping 50-word repeats within any of the 33 individual chapters**. Cross-block exact overlap, semantic scene duplication, canonical-copy reconciliation, and full manuscript assembly were not checked.

Full counts, QA scope, specific chapter revisions, and continuity handoffs: [Chapters 161–193 quality-pass report](ch161-193-quality-pass.md).
