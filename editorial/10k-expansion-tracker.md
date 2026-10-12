# Full-manuscript 10,000-word expansion tracker

**Scope:** Chapters 001–193 (two bonus interludes are excluded from the 10k narrative-chapter rule).
**Working source:** `rewrite/chapters-10k-quality-pass` branched from `edit/chapters-001-036-unified` on 2026-10-12.
**Rule:** Each chapter must reach **10,000 body words**, preferably 10,200–11,200, *without filler*. A mechanical pass is not editorial approval.

## Verified length status on the first 36 chapters

- Passing the length gate: **8 / 36** (001–008).
- Still short: **28 / 36** (009–036).
- Remaining body words to reach 10k for the short chapters in this verified range: **96,277**.
- **Chapters 037–193 are not recounted in this tracker yet**. The manuscript's older reader-edition word counts are not reliable substitutes for current branch counts. Run `python scripts/audit_chapter_length.py --json editorial/latest-length-report.json` in a checkout to obtain the exact current all-chapter status; this will currently exit nonzero because many chapters are short.

| Chapter | Verified body words | Length status |
| --- | ---: | --- |
| 001 | 11,077 | Length pass |
| 002 | 10,834 | Length pass |
| 003 | 10,335 | Length pass |
| 004 | 10,928 | Length pass |
| 005 | 10,966 | Length pass |
| 006 | 10,639 | Length pass |
| 007 | 10,385 | Length pass |
| 008 | 10,292 | Length pass |
| 009 | 1,743 | 8,257 short |
| 010 | 2,154 | 7,846 short |
| 011 | 2,348 | 7,652 short |
| 012 | 7,149 | 2,851 short |
| 013 | 6,257 | 3,743 short |
| 014 | 8,182 | 1,818 short |
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
- Chapters 002–008 were expanded and line-edited with **new story scenes**, attention to dialogue rhythm, distinct character agency, scene causality, and the established Percabeth, Grace-sister and Poseidon-sibling relationships. See dedicated handoffs and `editorial/prose-dialogue-acceptance.md`.
- Chapters 009–193 **have not been expanded to the 10k floor** on this branch. No quality or length certification is being claimed for them.
- Before the Chapter 008 revision, an all-offset 300-word cross-chapter check of Chapters 001–012 reported 86,857 windows and no exact overlaps. After the latest Chapter 008 revision, a new all-offset check specifically across Chapters 007–009 examined **21,523 windows, zero cross-chapter matches**. A fresh entire-manuscript check is still required.

## Editorial release gate

For each chapter: read preceding final scene and following opening; map POV, ages, date, powers, props, injuries, secrets and promises; draft scenes with a concrete objective, opposition, choice and lasting consequence; preserve the existing character-specific voice; review for exposition loops and formulaic resolutions; count body words; run 300-word verbatim overlap check; update a dedicated continuity handoff; and review actual diff.

Prioritize **009–011**, then **012–036**, then perform an exact length inventory and ordered review for **037–193**. Expansion should not resolve the unknown time-rewrite architect, rewrite the memory rules, or disclose Percy's prior life to Amphitrite without explicit author instruction.

**Not merged:** This branch is an editing proposal; the parent 36-chapter branch remains unchanged.

## Editorial status as of 2026-10-12

The opening eight chapters pass **the length gate only**. The new text has received targeted dialogue and prose revision, including removal of many clipped, alternating one-line exchanges. Chapter 008 now includes a camp supply accountability sequence and a public safety meeting giving Annabeth an independent role after the storm, while preserving Thalia's continuing anxiety. The scene/developmental and line/dialogue acceptance review remains open. This is **not** a claim that all six edited chapters have passed a complete independent developmental or copyediting read. Long-form style consistency for Chapters 006–193 remains pending.
