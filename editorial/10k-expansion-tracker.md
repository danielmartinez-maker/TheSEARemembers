# Full-manuscript 10,000-word expansion tracker

**Scope:** Chapters 001–193 (two bonus interludes are excluded from the 10k narrative-chapter rule).
**Working source:** `rewrite/chapters-10k-quality-pass` branched from `edit/chapters-001-036-unified` on 2026-10-12.
**Rule:** Each chapter must reach **10,000 body words**, preferably 10,200–11,200, *without filler*. A mechanical pass is not editorial approval.

## Verified length status on the first 36 chapters

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
