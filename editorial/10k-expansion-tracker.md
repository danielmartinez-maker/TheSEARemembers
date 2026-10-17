# Full-manuscript 10,000-word expansion tracker

**Scope:** Chapters 001–193 (two bonus interludes are excluded from the 10k narrative-chapter rule).
**Current working source:** PR #103 head branch `audit/four-phase-continuity-2026-10-13`, updated from local continuation branch `audit/pr103-live-continuation`. Earlier audit tables farther down document historical branches and checkpoints.
**Rule:** Each chapter must reach **10,000 body words**, preferably 10,200–11,200, *without filler*. A mechanical pass is not editorial approval.

## Latest local continuation candidate: all 193 chapters meet the length gate (2026-10-17)

**Source:** Current manuscript content on PR #103 head `a88e710`, followed by a continuity-ledger wording clarification. Fresh strict QA after the Chapter 054 dream-conversation callback reports **193/193 chapters at or above 10,000 body words**, with zero shortfall. Chapter 109 has **10,128** words; Chapter 110 has **11,739** after a review-driven trim. These are mechanical word counts, not editorial approval. Hosted [full-manuscript QA, run 514](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/39071817916) and [character-memory run 253](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/39071817913) passed on exact PR head `a88e710`; subsequent edits change continuity/audit documentation only, and current PR-head validation is tracked on PR #103.

| Scope | Latest local result |
|---|---:|
| Ordered narrative chapters | **193/193** |
| At or above 10,000 body words | **193** |
| Below 10,000 / missing words | **0 / 0** |
| Chapter-only every-offset 300-word windows | **1,942,117; 0 exact cross-chapter matches** |
| All chapter and bonus Markdown files | **196 files / 2,150,974 body words / 2,092,669 windows; 0 exact matches** |
| Source-anchored memory regression groups | **45 passed** |
| Structure audit | **193/193 ordered; no reported errors** |
| Full-scene chapter-ledger coverage | **193/193; 50 selected character timelines with exact-name candidate maps; exhaustive per-character matrix remains incomplete** |

The lexical screen flags an introduction line in Chapter 014, but scene context confirms this is the first in-person meeting after the earlier Iris contact. The Chapter 038/041 Silena age wording remains unresolved because no birthday/date is established between the statements. Full semantic continuity and style/developmental review remain open. The 50 profile locator maps are candidate indexes, not all-scene reviews. Refreshed reports: `editorial/audits/generated-full-manuscript-qa.json`, `generated-full-manuscript-qa.md`, `generated-all-text-300-word-qa.json`, and `generated-chapter-structure.json`.

## Earlier local checkpoint: privacy-boundary repairs before expansion completion (2026-10-17)

**Source:** Working branch `audit/pr103-live-continuation`, based on live PR #103 head `e9d86c2`. Chapter 023 now preserves Amphitrite’s ignorance of Percy’s mismatched memories. Chapter 032 keeps Percy’s missing routines out of Triton’s report; Percy reviews the ordinary training-and-sisters summary and approves what is sent. Chapter 023 recounts at **10,011** body words and Chapter 032 at **10,159**.

| Scope | Latest local result |
|---|---:|
| Ordered narrative chapters | **193/193** |
| At or above 10,000 body words | **177** |
| Below 10,000 / missing words | **16 / 116,854** |
| Chapter-only every-offset 300-token windows | **1,821,169; 0 exact cross-chapter matches** |
| All chapter and bonus Markdown files | **196 files / 2,030,026 body words / 1,971,721 windows; 0 exact matches** |
| Source-anchored memory regression groups | **35 passed** |

One lexical first-introduction cue remains for human review in Chapter 014. This is mechanical QA plus two focused scene repairs; it does not certify whole-novel semantic continuity or literary quality. Refreshed local outputs: `editorial/audits/generated-full-qa.json`, `generated-all-text-300-word-qa.json`, and `generated-structure-qa.json`.

## Previous current-branch checkpoint: Chapter 101 (2026-10-15; superseded by the Oct. 17 local continuation)

**Source:** PR #103 branch `audit/four-phase-continuity-2026-10-13`, based on published head `50b57891de5482399f2c6a050ebbf2885513958c`. Chapter 101's local QA is being recorded against this candidate; hosted workflow results attach to the pushed PR head.

| Scope | Candidate-tree result |
|---|---:|
| Numbered narrative chapters present and ordered | **193/193** |
| At or above 10,000 actual body words | **177** |
| Below 10,000 actual body words | **16** |
| Required additional body words to clear minimum | **116,854** |
| Chapter-only every-offset 300-word windows | **1,821,045; 0 exact cross-chapter matches** |
| All chapter and bonus files | **196 files; 2,029,902 body words; 1,971,597 windows; 0 exact cross-file matches** |
| Source-anchored character-memory checks | **33 passed at this historical checkpoint** |

**Chapter 101, A Name for It:** **2,093 → 10,321 body words (+8,228 net).** The Percy-limited revision keeps the existing relationship intact while grounding the present choice, distinguishes Thalia's remembered blocks from Annabeth's missing memory, preserves Thalia's wrapped palm, and adds an earned shelf build, an orange boundary and Clarisse's shield-rack lesson with Noah. See the [Chapter 101 handoff](handoffs/ch101-a-name-for-it.md) and [structured continuity record](../continuity/ch101.yaml).

- **Phase 1:** Adds scene-scoped witnessed/reported/unknown facts and cumulative state entries for Percy, Annabeth, Thalia, Clarisse, Silena and Noah; records next-morning boundaries with Chapters 100 and 102.
- **Phase 2:** Preserves the exclusive Percy/Annabeth erased-life memory boundary, family relationships, Thalia's injury and schedule status, and the difference between Noah's shield lesson and Chapter 102's spear practice.
- **Phase 3:** Expands through the present-day relationship choice, measured shelf work and accessibility check, shield-rack repair and coached lesson. Removes repeated reassurance and duplicate book-category debate; replaces a generic line with a specific measurement.
- **Phase 4:** 193/193 indexed and ordered; 33 memory checks passed at that Chapter 101 checkpoint; chapter-only and bonus-inclusive strict duplicate scans found zero matches. The evidence index writes 193 provisional chapter locators, and the introduction screen leaves one review cue in Chapter 014. Both hosted Actions passed on revision commit `a6b53d8`: [full manuscript QA, run 468](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38794911797) and [character memory consistency, run 230](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38794911680). This remains a scoped chapter review, not whole-novel semantic or literary signoff.

**Next chronological underlength chapter:** [102 Not a Competition](../chapters/102-not-a-competition.md), **1,538 body words**, needs **8,462**. Preserve the morning-after relationship state and continue the Noah shield/spear lessons as distinct events.

## Superseded candidate checkpoint: Chapter 100 (2026-10-15 local candidate)

**Source:** PR #103 branch `audit/four-phase-continuity-2026-10-13`, based on published head `acb4a8b997e663bb4bce698d5f3bd8ff4cc70f8c`. Local QA passes; hosted workflow results are available on the PR's pushed head.

| Scope | Candidate-tree result |
|---|---:|
| Numbered narrative chapters present and ordered | **193/193** |
| At or above 10,000 actual body words | **176** |
| Below 10,000 actual body words | **17** |
| Required additional body words to clear minimum | **124,761** |
| Chapter-only every-offset 300-word windows | **1,812,817; 0 exact cross-chapter matches** |
| All chapter and bonus files | **196 files; 2,021,674 body words; 1,963,369 windows; 0 exact cross-file matches** |
| Source-anchored character-memory checks | **32 passed** |

**Chapter 100, The Thousandth Campfire:** **6,707 → 10,190 body words** (+3,483 net). The Percy-limited revision corrects the public Minotaur rumor without exposing Percy or Annabeth's private old-life memories; preserves Beryl's absence, Thalia's uncleared palm, Tyson's forge leave, Annabeth's illness privacy, and the consent limits around the dance photo; and records the campfire count as a count of surviving entries rather than every fire. The feast duplication is removed. See the [Chapter 100 handoff](handoffs/ch100-thousandth-campfire.md) and [structured continuity record](../continuity/ch100.yaml).

- **Phase 1:** Adds witnessed/reported/unknown handoff and scoped cumulative state updates for 18 characters, with the Chapter 099 close and Chapter 101 opening checked. The date links and Tyson leave continuity remain explicitly unknown.
- **Phase 2:** Keeps the Minotaur memory private while Amphitrite attends, labels the camp rumor as unverified, and preserves sibling parentage, injury, letter and illness boundaries.
- **Phase 3:** Expands the source from 6,707 to 10,190 through event choices, a fire-stack problem and earned family scenes; removes duplicated feast prose and avoids length padding.
- **Phase 4:** 193/193 structure; 32 memory checks pass; chapter-only and bonus-inclusive strict duplicate scans find zero matches. The evidence index writes 193 unverified source-cue records. The introduction scan leaves one review cue in Chapter 014. These are mechanical checks and a Chapter 100 scene review, not whole-novel literary certification.

**Next chronological underlength chapter:** [101 A Name for It](../chapters/101-a-name-for-it.md), **2,093 body words**, needs **7,907**. Keep Percy and Annabeth's established relationship intact; Chapter 101's opening asks what label feels right in their current life, without resetting their remembered bond.

## Superseded checkpoint: Chapter 098 (2026-10-15 candidate checkpoint)

**Source revision:** PR commit `1243faf14ef57c0cfa2591b11bfd32488372840`, based on published head `c9ff34393533642b667355c2212cdfadf99af0e3`. Both hosted workflows pass: [full manuscript QA](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38775006429) and [character memory consistency](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38775006398).

| Scope | Candidate-tree result |
|---|---:|
| Numbered narrative chapters present and ordered | **193/193** |
| At or above 10,000 actual body words | **174** |
| Below 10,000 actual body words | **19** |
| Required additional body words to clear minimum | **132,170** |
| Chapter-only every-offset 300-word windows | **1,805,052; 0 exact cross-chapter matches** |
| All chapter and bonus files | **196 files; 2,013,909 body words; 1,955,604 windows; 0 exact cross-file matches** |
| Source-anchored memory regression checks | **31 passed** |

**Chapter 098, Fathers' Day (Gods):** **6,261 → 10,121 body words** (**+3,860 net**). The Percy-limited revision keeps the survey public and on trial, preserves the dock and north-trail hazards, lets Clarisse tell Poseidon her firsthand memory of his brief visit, gives Silena and Thalia separate boundaries, and keeps Tyson's hinge work his own. Their fathers' apologies do not resolve long-term neglect. See the [Chapter 098 handoff](handoffs/ch098-fathers-day-gods.md) and [structured continuity record](../continuity/ch098.yaml).

- **Phase 1:** Added a scene-specific handoff and structured continuity record, appended witnessed/reported/unknown facts to the cumulative ledger, and updated ten per-character state files. Chapter 097's map status, Chapter 099's late-August opening, injuries, promises and private memory boundaries remain explicit.
- **Phase 2:** Corrected unsupported old-life details and private map leakage, kept Zeus unaware of erased-life memories, and did not infer that the approved Amphitrite photo was sent. Clarisse and Silena choose their own contact; Thalia's palm remains wrapped; the map, dock and north-trail issues stay open.
- **Phase 3:** Added Friday logistics, the public-survey review, Saturday's shared meal and distinct father-child conversations. Scene-level review covers Chapters 098 and adjacent 097/099 boundaries. The expansion is source-specific rather than repeated praise or padding.
- **Phase 4:** Local and hosted manuscript QA pass: 193/193 indexed and ordered; 174 pass / 19 short; 132,170 words remain; 1,805,052 chapter-only and 1,955,604 bonus-inclusive every-offset 300-word windows found zero exact matches; all 31 source-anchored memory checks pass; the evidence index rebuilds for all 193 chapters. The lexical introduction scan leaves one human-review cue in Chapter 014. These checks do not certify whole-novel semantic or literary consistency.

**Next chronological underlength chapter:** [099 Mothers](../chapters/099-mothers.md), **5,884 body words**, needs **4,116**. Chapter 098 closes after the Saturday meal; Chapter 099 opens in late August, and the exact elapsed time and whether Tyson's forge leave is the same visit remain unknown.

## Latest current-branch continuation: Chapter 099 (2026-10-15 candidate checkpoint)

**Chapter source revision:** PR commit `8b927088fc9c5e6793bec431a7cc0299f7224344`, based on published head `1243faf14ef57c0cfa2591b11bfd32488372840`. Both hosted workflows pass: [full manuscript QA](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38778701870) and [character memory consistency](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38778701784). The follow-up checkpoint below only records these results and does not change the chapter source.

| Scope | Candidate-tree result |
|---|---:|
| Numbered narrative chapters present and ordered | **193/193** |
| At or above 10,000 actual body words | **175** |
| Below 10,000 actual body words | **18** |
| Required additional body words to clear minimum | **128,054** |
| Chapter-only every-offset 300-word windows | **1,809,334; 0 exact cross-chapter matches** |
| All chapter and bonus files | **196 files; 2,018,191 body words; 1,959,886 windows; 0 exact cross-file matches** |
| Source-anchored memory regression checks | **31 passed** |

**Chapter 099, Mothers:** **5,884 → 10,166 body words** (**+4,282 net**). The Percy-limited revision preserves the unresolved dock hazard, attributes Beryl's claims to her letter, leaves Thalia's palm wrapped and uncleared, and records Amphitrite's gifts and Percy/Annabeth's temporary shawl loan. See the [Chapter 099 handoff](handoffs/ch099-mothers.md) and [structured continuity record](../continuity/ch099.yaml).

- **Phase 1:** Added the scene-level handoff, structured record, cumulative ledger entry, and 15 scoped character-state updates. Recorded witnessed, reported and unknown information separately, including Thalia's letter, the palm injury, gift ownership and the 098/099/100 timeline gaps.
- **Phase 2:** Removed the Ares parent reference, unsupported Beryl incidents and omniscient claims about Maria. Kept Beryl absent and her letter claims unverified; protected Amphitrite's knowledge boundary; kept the unsafe dock unused; preserved Thalia's unresolved injury.
- **Phase 3:** Added earned scenes around Percy's Sally memories, Amphitrite's visit, Thalia's decision, Tyson's tool test, Silena's direct report, and the optional lantern gathering. The revised scenes maintain Percy-limited narration and do not make him resolve his siblings' relationships.
- **Phase 4:** Local and hosted manuscript QA pass: 193/193 indexed and ordered; 175 pass / 18 short; 128,054 words remain; chapter-only and bonus-inclusive scans found zero exact 300-word matches; all 31 memory regression groups pass; the evidence index rebuilds for 193 chapters. Both hosted workflows passed on the Chapter 099 source commit. The lexical introduction scan leaves one human-review cue in Chapter 014. These checks do not certify whole-novel semantic or literary quality.

**Next chronological underlength chapter:** [100 The Thousandth Campfire](../chapters/100-the-thousandth-campfire.md), **6,707 body words**, needs **3,293**. Chapter 099 ends after an evening lantern gathering and beach bonfire. Chapter 100 opens on the morning of the thousandth campfire; the calendar gap and relation between the two events remain unknown. Tyson is on forge leave in both chapters, but whether it is the same leave is not established.

## Superseded checkpoint: Chapter 097 (2026-10-15)

**Source revision:** Chapter 097 is published in PR commit 577ec2a3e93ad2b960d5688e44381ebf77c3e0e9, based on previously verified head 88355d5edcbf525ffb2718ef535d6fc302c497f1. Both hosted workflows pass: [full manuscript QA](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38770657606) and [character memory consistency](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38770657790).

| Scope | Candidate-tree result |
|---|---:|
| Numbered narrative chapters present and ordered | **193/193** |
| At or above 10,000 actual body words | **173** |
| Below 10,000 actual body words | **20** |
| Required additional body words to clear minimum | **135,909** |
| Chapter-only every-offset 300-word windows | **1,801,192; 0 exact cross-chapter matches** |
| All chapter and bonus files | **196 files; 2,010,049 body words; 1,951,744 windows; 0 exact cross-file matches** |
| Source-anchored memory regression checks | **30 passed** |

**Chapter 097, The Map:** **6,862 → 10,185 body words** (**+3,323 net**). The revision keeps erased-life map memories private between Percy and Annabeth, corrects an unsafe dock instruction, tests the ramp route with Chiron, and adds forge/infirmary review, a new-camper legend test, participant-approved labels and a one-week display trial. The first edition logs an unresolved north-trail inspection, flexing dock board, wet-furrow alternate path and missing Cabin Six window. See the [Chapter 097 handoff](handoffs/ch097-the-map.md) and [structured continuity record](../continuity/ch097.yaml).

- **Chapter 095, Annabeth Sick:** **6,977 → 10,129 body words** (**+3,152 net**). The Percy-limited revision preserves Annabeth's independent choices during a fever, keeps the fever's cause and relationship to Percy's earlier illness unknown, follows Will's no-training and escalation instructions, and protects her private dream details. See the [Chapter 095 handoff](handoffs/ch095-annabeth-sick.md) and [structured continuity record](../continuity/ch095.yaml).
- **Chapter 096, Training Together:** **6,878 → 10,144 body words** (**+3,266 net**). The revision adds a signal rehearsal after the surf masks Grover's whistle, clarifies distinct water and air-strike routes, preserves Thalia's tender palm and Annabeth's recovery limits, and resolves her Cabin One choice before Chapter 097. See the [Chapter 096 handoff](handoffs/ch096-training-together.md) and [structured continuity record](../continuity/ch096.yaml).

- **Phase 1:** Added Chapter 097 handoff, structured continuity record and witnessed/reported/unknown state updates for 18 named participants and the offstage sender. Adjacent boundaries preserve the beacon, Thalia's last-known palm restriction, the pending north-trail inspection, and the distinction between Chiron's exercise map and Annabeth's survey.
- **Phase 2:** Keeps old-life map memories exclusive; preserves Poseidon and Zeus/Grace sibling relationships; removes private routines; corrects the dock instruction; keeps the north trail closed; does not imply a repair, health clearance, photo delivery or new route inspection.
- **Phase 3:** Chapter 097 reaches **10,185** words with consequential field checks, consent choices, the legend usability test and a first-edition trial rather than repeated praise or padding. Scene-level continuity review covers Chapter 097 and the Chapter 096/098 boundaries, plus the Chapter 148 map callback.
- **Phase 4:** Local checks pass on this candidate: 193/193 ordered; 173 pass / 20 short; 135,909 words remain; 1,801,192 chapter-only and 1,951,744 bonus-inclusive every-offset 300-word windows found zero exact matches; all 30 source-anchored memory checks pass; the five QA scripts compile; the evidence index rebuilds for 193 chapters. The lexical introduction scan leaves one human-review cue in Chapter 014. These checks do not certify whole-novel semantic or literary consistency. Hosted GitHub Actions pass on commit 577ec2a: [full manuscript QA](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38770657606), [character memory consistency](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38770657790).

**Next chronological underlength chapter:** [098 Fathers' Day (Gods)](../chapters/098-fathers-day-gods.md), **6,261 body words**, needs **3,739**. Chapter 097 ends with the first map edition in a one-week rec-room trial; the north trail and third dock board remain unresolved. Preserve the approval boundary for the photo to Amphitrite and do not imply it has been sent.

## Superseded checkpoint: Chapter 091 (2026-10-14)

**Branch base:** The candidate tree is built on remote commit `4c592e0fdd04e66a13485e44f60b4e46d8fcfaf1`. The figures below are exact-source local checks on that tree; GitHub Actions results for the published commit are tracked separately in PR #103.

| Scope | Candidate-tree result |
|---|---:|
| Numbered narrative chapters present and ordered | **193/193** |
| At or above 10,000 actual body words | **167** |
| Below 10,000 actual body words | **26** |
| Required additional body words to clear minimum | **156,214** |
| Chapter-only every-offset 300-word windows | **1,780,163; 0 exact cross-chapter matches** |
| All chapter and bonus files | **196 files; 1,930,715 windows; 0 exact cross-file matches** |
| Source-anchored memory regression checks | **24 passed** |

**Chapter 091, *Tide Pools*:** **6,788 → 10,050 body words** (+3,262 net). The morning now accounts for the storm's pending lake, ward, anchor, field and signal checks before departure; Grover supervises with a route and count protocol. The tide-pool scenes preserve wildlife, keep the changing route safe, and correct the relationship and reported-memory boundaries. Percy and Thalia receive Will's follow-up, and the chapter keeps every gift and Amphitrite-letter promise in its actual status. See the [Chapter 091 handoff](handoffs/ch091-tide-pools.md).

- **Phase 1:** Added a source-anchored Chapter 091 handoff and cumulative event entries for Percy, Annabeth, Clarisse, Silena, Thalia, Grover, Chiron, Will, Malcolm and Katie; added [a structured ledger](../continuity/ch091.yaml). The earlier gap in systematic Chapters 037–089 memory coverage remains disclosed.
- **Phase 2:** Repaired the unsafe/inaccurate blue-ring advice and crab handling; clarified Clarisse's separate mother history, the established Percy/Annabeth relationship, the limited Sally/Frederick reports, shell provenance, storm-check status, and Thalia/Percy aftercare.
- **Phase 3:** Expanded the chapter through a purposeful morning status check, observed intertidal activity, Annabeth's revised field notes, family conversation, and a conditional return plan. The chapter meets the 10,000-word floor; independent prose/developmental signoff remains open.
- **Phase 4:** Local exact-source checks pass: 193/193 ordered, 167 pass / 26 short, 156,214 words remaining; 1,780,163 chapter-only and 1,930,715 bonus-inclusive every-offset 300-word windows with zero exact matches; 24 anchored memory groups. These are mechanical results, not full-semantic or literary certification.

**Next chronological underlength chapter:** [092 Jealousy II](../chapters/092-jealousy-ii.md), at **6,375** words, needs **3,625** meaningful body words. Preserve Chapter 091's shell, sketch ownership, Thalia's morning injury check, Percy’s cleared symptom report without diagnosis, and the pending storm inspections.

## Superseded checkpoint: Chapter 090

Chapter 090, *Storm and Sea*, was committed at `4c592e0fdd04e66a13485e44f60b4e46d8fcfaf1` after growing **6,822 → 10,346 body words** (+3,524 net). The added scenes give Silena a shelter-count role, make the flag protocol fail in crosswind and get corrected, distinguish freshwater runoff from Sound saltwater, and track Thalia's right-palm burn and Percy's temporary hand tingling through Will's care. The [Chapter 090 handoff](handoffs/ch090-storm-and-sea.md) leaves the lake, ward, anchor and field checks pending for Chapter 091.

## Superseded checkpoint after Chapter 080 (2026-10-14)

**Source:** [GitHub Actions full-manuscript QA run 38611034708](https://github.com/danielmartinez-maker/TheSEARemembers/actions/runs/38611034708), after the Chapter 080 expansion and handoff. The additional Chapter 080 guard is separately checked at its script-head run. Earlier tables lower in this file are historical and superseded for current totals.

| Scope | Current verified result |
|---|---:|
| Numbered narrative chapters audited | **193** |
| At or above 10,000 actual body words | **156** (CI-verified) |
| Below 10,000 actual body words | **37** (CI-verified) |
| Required additional body words to clear minimum | **195,840** (CI-verified) |
| Exact cross-chapter 300-word duplicates | **0 exact cross-chapter matches across 1,737,367 every-offset 300-word windows** |
| Source-anchored memory regression checks | **21 checks passed** on corpus-validation head; **22 configured** after adding Chapter 080 guard, with newest guard-head run tracked separately |

**Eighteen chapter expansion results since the 138/55 baseline**:

- [066, Jason's Letter](../chapters/066-jason-s-letter.md): **8,314 → 10,572** words; [memory handoff](../continuity/ch066.yaml).
- [067, Fishing](../chapters/067-fishing.md): **5,758 → 10,292** words; [memory handoff](../continuity/ch067.yaml).
- [068, The Storm (Small)](../chapters/068-the-storm-small.md): **5,529 → 10,328** words; [memory handoff](../continuity/ch068.yaml).
- [070, Clarisse's Poems](../chapters/070-clarisse-s-poems.md): **6,072 → 10,543** body words (**+4,471 net**); [character, prop and permission handoff](handoffs/ch070-clarisses-poems.md). Chapter length passes, but independent semantic/prose signoff is open.
- [069, Silena's Song](../chapters/069-silena-s-song.md): **6,001 → 10,118** words; [scene handoff](handoffs/ch069-silenas-song.md).
- [071, Anniversary](../chapters/071-anniversary.md): **5,995 → 10,145** body words; [continuity handoff](handoffs/ch071-anniversary.md).
- [072, New Kids](../chapters/072-new-kids.md): **5,751 → 10,093** body words; [continuity handoff](handoffs/ch072-new-kids.md).
- [073, The Play](../chapters/073-the-play.md): **5,604 → 10,245** body words; [continuity handoff](handoffs/ch073-the-play.md).
- [074, Tyson's Visit](../chapters/074-tyson-s-visit.md): **5,845 → 10,158** body words; [continuity handoff](handoffs/ch074-tysons-visit.md).
- [075, Zoe's Story](../chapters/075-zoe-s-story.md): **5,558 → 10,087** body words; [continuity handoff](handoffs/ch075-zoes-story.md).
- [076, The Promise (II)](../chapters/076-the-promise-ii.md): **5,228 → 10,350** body words; [continuity handoff](handoffs/ch076-the-promise-ii.md).
- [077, Beach Day (Atlantis Style)](../chapters/077-beach-day-atlantis-style.md): **5,706 → 10,236** body words; [continuity handoff](handoffs/ch077-beach-day-atlantis-style.md).
- [078, Nico's Birthday](../chapters/078-nico-s-birthday.md): **5,987 → 10,471** body words; [memory handoff](handoffs/ch078-nicos-birthday.md).
- [079, Elena's Tale](../chapters/079-elena-s-tale.md): **5,336 → 10,116** body words; [memory handoff](handoffs/ch079-elenas-tale.md).
- [080, The Second Dance](../chapters/080-the-second-dance.md): **5,702 → 10,440** body words; [memory handoff](handoffs/ch080-the-second-dance.md).
- [118, A Message from Amphitrite](../chapters/118-a-message-from-amphitrite.md): **10,320 current body words** by the strict repository counter (an earlier tracker recorded 10,464); [memory handoff](../continuity/ch118.yaml).
- [132, A Month Beneath the Sea](../chapters/132-a-month-beneath-the-sea.md): **6,296 → 10,243** words; [memory handoff](../continuity/ch132.yaml).
- [133, Annabeth's Birthday](../chapters/133-annabeth-s-birthday.md): **8,704 → 10,656** words; [memory handoff](../continuity/ch133.yaml).

The first eight changes added **27,150 net body words** and eliminated **21,495 previously required shortfall words**. The seven additional 071–077 expansions remove **30,313 required shortfall words**, giving the previously CI-verified 40-chapter/208,815-word remainder. Chapters 078–079 then removed **8,677 additional required words**, giving the **previously verified 38 chapters / 200,138 words** outstanding. Chapter 080 then removed **4,298 mandatory shortfall words**, giving the **37 chapters / 195,840 words** remaining at that checkpoint. Length overages are not counted toward another short chapter's deficit. At this historical checkpoint, the [expansion queue](handoffs/55-short-chapters-execution-queue.md) started at **081** and also included **131**; the current queue is updated above. A mechanical length pass and absence of exact duplication are not a substitute for independent full semantic, dialogue, character-memory, plot and style review.

## Historical Chapters 121–160 checkpoint (2026-10-12; superseded by current all-chapter count)

**22 / 40 chapters** in this range have at least **10,000 body words**, as of the targeted revisions through commit `b278fc6615e9cc4193dc4c36709e08a95fa5ed9b`. **Every chapter 140–160 (21/21)** meets the mechanical minimum, as does **121 (10,632)**. The **18 remaining short chapters are 122–139**, collectively **94,887 words short** of their individual floors. Do not call the full range finished.

Revised passing counts beyond the existing baseline: **140 10,163; 141 10,030; 142 10,087; 143 10,136; 146 10,089; 147 10,143; 148 10,293; 149 10,387; 157 10,134; 158 10,149; 159 10,133**. Chapter 151, already over 10k, was canon-corrected to **10,823**. Chapters 122–123 were also corrected for inaccessible altered-childhood memory and saltwater versus freshwater geography, but remain short.

Chapters 147, 149 and 151 required additional memory-boundary repairs: Clarisse and Thalia cannot remember the erased Ares/Hunter/tree events, and only Percy and Annabeth remember the former timeline. No universal manuscript clearance should be inferred.

Source-specific prose changes, chapter-by-chapter counts and QA limits at that date: [full 121–160 inventory](audits/ch121-160-inventory-2026-10-12.md) and [continuity handoff](handoffs/ch121-160-2026-10-12.md). The stated shortfall and “continue at 122” instruction are historical and superseded: the current repository count reports all 193 chapters above the floor. This section does not claim independent full-chapter literary or cross-range semantic review.

## Chapters 014–044 current 10k-length verification (2026-10-12)

**31 / 31 Chapters 014–044 meet the 10,000-body-word minimum**, each freshly fetched and recounted on this branch. The "first 36 chapters" table farther below records an earlier baseline and is **superseded** for Chapters 014–036. Do not use its old figures to plan subsequent work.

The final 13-chapter closeout (body words): **018 10,001; 019 10,003; 021 10,000; 023 10,011; 027 10,000; 029 10,005; 031 10,005; 032 10,001; 033 10,001; 040 10,005; 041 10,019; 042 10,133; 043 10,052**. The other 18 chapters in 014–044 were also individually fetched and verified at or above 10,000.

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
