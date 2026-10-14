# The Sea Remembers, the Sky Forgets

*Percy Jackson and the Olympians fanfiction · Time travel · Canon divergence · Percabeth*

**Work in progress.** This repository organizes 193 chapters and two bonus interludes into individual Markdown files, preserving the original manuscript text. Chapter filenames begin with three-digit numbers to keep them ordered.

- [Chapters](chapters/)
- [Bonus interludes](bonus/)
- [Chapter index](CHAPTER_INDEX.md)
- [Manifest and integrity checks](manifest.json)

Edit chapters independently using pull requests or direct commits. This is an unofficial, noncommercial fan work set in Rick Riordan's Percy Jackson universe.

## Canon and editing

- [FIC_CONTEXT.md](FIC_CONTEXT.md): governing story bible, author decisions, continuity requirements, and chapter handoff template.
- [Character memory ledger](continuity/CHARACTER_MEMORY_LEDGER.md): source-anchored relationships, past encounters, what each character remembers, and knowledge boundaries.
- [Chapter memory handoff](continuity/CHAPTER_MEMORY_HANDOFF.md): mandatory per-chapter checklist for first meetings, earned intimacy, promises, objects, injuries and disclosure.
- [Character-memory audit](editorial/audits/CHARACTER-MEMORY-2026-10-13.md): targeted confirmed repairs, with explicit limits on what has been reviewed.
- [Character-memory regression check](scripts/check_character_memory.py): tests source-anchored relationship facts and lists possible first-introduction dialogue for manual review; also runs in GitHub Actions.

## Coordinated 193-chapter audit (October 13, 2026)

- [Evidence-backed four-phase execution record](editorial/audits/FOUR-PHASE-EXECUTION-2026-10-13.md): what passed, what was revised and what remains incomplete.
- [Per-chapter machine-generated continuity cue index](continuity/evidence/generated-ch001-193.md): 193 chapter locators; witnesses, relationships and secret knowledge explicitly **unverified** until human scene review.
- [Full-manuscript QA report](editorial/audits/generated-full-qa.md) and [structured data](editorial/audits/generated-full-qa.json): latest verified CI recount **143/193** length-passing, **50 short**, **252,134** body words missing; **1,677,515** consecutive 300-word windows with zero exact cross-chapter matches. **16/16** character-memory regressions. [Passing run](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38511481429).
- [Expansion handoff queue](editorial/handoffs/55-short-chapters-execution-queue.md): originally 55 short chapters, **50** still short. Chapters [066](chapters/066-jason-s-letter.md), [067](chapters/067-fishing.md), [068](chapters/068-the-storm-small.md), [132](chapters/132-a-month-beneath-the-sea.md) and [133](chapters/133-annabeth-s-birthday.md) now meet the 10k body-word threshold, with [per-chapter continuity handoffs](continuity/) and outstanding independent literary review.
- [Auditing scripts](scripts/full_manuscript_qa.py) and [CI workflow](.github/workflows/full-manuscript-audit.yml). Mechanical QA does not certify every scene's continuity or prose quality.

## Editorial audit progress

- [Chapter 1 audit](editorial/audits/chapter-001.md) and [Issue #1](https://github.com/danielmartinez-maker/TheSEARemembers/issues/1)
- [Chapters 2–6 batch overview](editorial/audits/BATCH-002-006.md)
- [Chapters 7–26 batch overview](editorial/audits/BATCH-007-026.md): 20 individual chapter reports and revision issues
- [Chapters 27–66 batch overview](editorial/audits/BATCH-027-066.md): 40 individual source-referenced audits and GitHub revision issues
- [Chapters 67–193 batch overview](editorial/audits/BATCH-067-193.md): all 127 chapter screenings, exact-duplication results and [priority backlog issue #97](https://github.com/danielmartinez-maker/TheSEARemembers/issues/97)

Audits document proposed fixes. The chapter prose remains unchanged until edits are separately made and reviewed.
