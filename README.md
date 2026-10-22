# The Sea Remembers, the Sky Forgets

*Percy Jackson and the Olympians fanfiction · Time travel · Canon divergence · Percabeth*

**Work in progress.** This repository organizes 198 chapters and two bonus interludes into individual Markdown files. The PR branch includes scoped continuity and prose revisions; manifest.json retains the checksum for the original imported manuscript. Chapter filenames begin with three-digit numbers to keep them ordered.

- [Chapters](chapters/)
- [Bonus interludes](bonus/)
- [Chapter index](CHAPTER_INDEX.md)
- [Manifest and integrity checks](manifest.json)

Edit chapters independently using pull requests or direct commits. This is an unofficial, noncommercial fan work set in Rick Riordan's Percy Jackson universe.

## Active family-first arc (October 22, 2026)

PR #103 is drafting Chapters 194–218. Chapters 194–198 contain 51,876 body words across five installments; Chapter 198 measures 10,051 body words by the repository's whitespace-token method. The arc remains in implementation, with Chapter 199 next. Hosted validation is tracked on the PR.

## Canon and editing

- [FIC_CONTEXT.md](FIC_CONTEXT.md): governing story bible, author decisions, continuity requirements, and chapter handoff template.
- [Character memory ledger](continuity/CHARACTER_MEMORY_LEDGER.md): source-anchored relationships, past encounters, what each character remembers, and knowledge boundaries.
- [Chapter memory handoff](continuity/CHAPTER_MEMORY_HANDOFF.md): mandatory per-chapter checklist for first meetings, earned intimacy, promises, objects, injuries and disclosure.
- [Character-memory audit](editorial/audits/CHARACTER-MEMORY-2026-10-13.md): targeted confirmed repairs, with explicit limits on what has been reviewed.
- [Character-memory regression check](scripts/check_character_memory.py): tests source-anchored relationship facts and lists possible first-introduction dialogue for manual review; also runs in GitHub Actions.

## Historical PR candidate and local QA (October 17, 2026)

- [Evidence-backed four-phase execution record](editorial/audits/FOUR-PHASE-EXECUTION-2026-10-13.md): what passed, what was revised and what remains incomplete.
- [Per-chapter machine-generated continuity cue index](continuity/evidence/generated-ch001-193.md): 193 chapter locators; witnesses, relationships and secret knowledge explicitly **unverified** until human scene review.
- [Full-manuscript QA report](editorial/audits/generated-full-manuscript-qa.md) and [structured data](editorial/audits/generated-full-manuscript-qa.json): the current candidate has **193/193** ordered chapters at or above 10,000 body words, **2,000,370** chapter body words and zero shortfall. Chapter-only exact-duplicate QA checked **1,942,663** every-offset 300-word windows; the chapter-plus-bonus scan covered **196 files / 2,151,520 body words / 2,093,215 windows**. Both scans found zero exact matches; all **45** source-anchored memory regressions pass, and structure and the 193-entry evidence index rebuild. Current source commit `0eb5229` passed hosted full QA [run 546](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/39093793372) and character-memory checks [run 269](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/39093793381). Mechanical checks do not certify every scene's continuity or prose quality.
- [Continuity coverage map](continuity/character-states/README.md): ledger-backed full-scene review covers **193/193** chapters. All **50** character-state profiles contain selected, source-linked timelines and now include exact-name candidate locator sweeps with explicit review limits. A locator hit is not proof of presence or knowledge, and candidate scenes not covered by a cited event remain unverified; these profiles are not exhaustive person-by-person, chapter-by-chapter matrices. Bounded scene checks corrected Annabeth's premature age label in Chapter 128 and Silena's Chapter 038 wording to fourteen, matching the opening baseline and Chapter 041; her exact birthday/date remains unknown. The full cross-character semantic reconciliation and independent whole-novel style review remain incomplete.
- [Expansion handoff queue](editorial/handoffs/55-short-chapters-execution-queue.md): the mechanical shortfall is now zero. All 193 chapters pass the 10k body-word threshold; independent whole-novel literary and semantic review remains open.
- [Auditing scripts](scripts/full_manuscript_qa.py) and [CI workflow](.github/workflows/full-manuscript-audit.yml). Mechanical QA does not certify every scene's continuity or prose quality.

## Editorial audit progress

- [Chapter 1 audit](editorial/audits/chapter-001.md) and [Issue #1](https://github.com/danielmartinez-maker/TheSEARemembers/issues/1)
- [Chapters 2–6 batch overview](editorial/audits/BATCH-002-006.md)
- [Chapters 7–26 batch overview](editorial/audits/BATCH-007-026.md): 20 individual chapter reports and revision issues
- [Chapters 27–66 batch overview](editorial/audits/BATCH-027-066.md): 40 individual source-referenced audits and GitHub revision issues
- [Chapters 67–193 batch overview](editorial/audits/BATCH-067-193.md): all 127 chapter screenings, exact-duplication results and [priority backlog issue #97](https://github.com/danielmartinez-maker/TheSEARemembers/issues/97)

Audit records distinguish completed scoped revisions from proposed fixes and screenings. Whole-novel scene review, semantic repetition review and independent literary signoff remain incomplete.
