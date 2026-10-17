# The Sea Remembers, the Sky Forgets

*Percy Jackson and the Olympians fanfiction · Time travel · Canon divergence · Percabeth*

**Work in progress.** This repository organizes 193 chapters and two bonus interludes into individual Markdown files. The PR branch includes scoped continuity and prose revisions; manifest.json retains the checksum for the original imported manuscript. Chapter filenames begin with three-digit numbers to keep them ordered.

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

## Current PR candidate and local QA (October 17, 2026)

- [Evidence-backed four-phase execution record](editorial/audits/FOUR-PHASE-EXECUTION-2026-10-13.md): what passed, what was revised and what remains incomplete.
- [Per-chapter machine-generated continuity cue index](continuity/evidence/generated-ch001-193.md): 193 chapter locators; witnesses, relationships and secret knowledge explicitly **unverified** until human scene review.
- [Full-manuscript QA report](editorial/audits/generated-full-qa.md) and [structured data](editorial/audits/generated-full-qa.json): on the current local continuation of PR #103 head `284b8cc`, strict QA reports **193/193** ordered chapters at or above 10,000 body words, zero shortfall, and zero exact cross-chapter matches across **1,941,481** every-offset windows. The chapter-plus-bonus scan covers **196 files**, **2,150,338 body words** and **2,092,033 windows**, also with zero exact matches. **36** source-anchored memory regressions pass. Hosted validation for this continuation is pending; these mechanical checks do not certify every scene's continuity or prose quality.
- [Continuity coverage map](continuity/character-states/README.md): ledger-backed full-scene review covers **193/193** chapters. All **49** character-state profiles now contain selected, source-linked cumulative timelines spanning Chapters 001–193; they are not exhaustive person-by-chapter matrices. The full cross-character semantic reconciliation and independent whole-novel style review remain incomplete.
- [Expansion handoff queue](editorial/handoffs/55-short-chapters-execution-queue.md): the mechanical shortfall is now zero. All 193 chapters pass the 10k body-word threshold; independent whole-novel literary and semantic review remains open.
- [Auditing scripts](scripts/full_manuscript_qa.py) and [CI workflow](.github/workflows/full-manuscript-audit.yml). Mechanical QA does not certify every scene's continuity or prose quality.

## Editorial audit progress

- [Chapter 1 audit](editorial/audits/chapter-001.md) and [Issue #1](https://github.com/danielmartinez-maker/TheSEARemembers/issues/1)
- [Chapters 2–6 batch overview](editorial/audits/BATCH-002-006.md)
- [Chapters 7–26 batch overview](editorial/audits/BATCH-007-026.md): 20 individual chapter reports and revision issues
- [Chapters 27–66 batch overview](editorial/audits/BATCH-027-066.md): 40 individual source-referenced audits and GitHub revision issues
- [Chapters 67–193 batch overview](editorial/audits/BATCH-067-193.md): all 127 chapter screenings, exact-duplication results and [priority backlog issue #97](https://github.com/danielmartinez-maker/TheSEARemembers/issues/97)

Audit records distinguish completed scoped revisions from proposed fixes and screenings. Whole-novel scene review, semantic repetition review and independent literary signoff remain incomplete.
