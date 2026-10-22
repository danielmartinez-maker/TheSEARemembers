# Amphitrite's Chosen-Mother Arc Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Record Amphitrite’s gradual chosen-mother arc for Silena and Clarisse, and make Percy use “Mom” in his dialogue.

**Architecture:** Keep the existing Chapters 125–132 as the source-grounded setup, then record Silena’s earlier and Clarisse’s later title milestones as future work beyond Chapter 193. Make only the targeted Percy dialogue changes already identified and update the canon/profile documents so they distinguish current events from planned future development.

**Tech Stack:** Markdown manuscript, GitHub chapter-per-file repository, GitHub Contents API on PR #103.

**Spec:** [docs/superpowers/specs/2026-10-21-amphitrite-chosen-mother-arc-design.md](../specs/2026-10-21-amphitrite-chosen-mother-arc-design.md)

## Global Constraints

- Percy and Annabeth alone retain autobiographical memories of the erased future.
- Amphitrite does not know Percy’s erased-future memories or altered-childhood memory gap.
- Percy’s bond with Amphitrite does not erase Sally or his grief for her.
- Silena’s relationship with Maria and Clarisse’s relationship with her own mother remain distinct and intact.
- Clarisse’s hurt about Poseidon’s unequal involvement remains valid and unresolved unless a later scene changes it.
- Silena chooses “Mom” before Clarisse; each title milestone is voluntary and occurs in a separate future scene.
- The current source ends at Chapter 193; do not write either sister’s title as an event that has already occurred.

## Review Focus

1. **Spoken address vs narration:** Change only Percy’s dialogue using “Mother” as an informal family reference; leave descriptive narration context-sensitive.
2. **Dual-mother grief:** Preserve the existing Sally conversation and do not frame Amphitrite as Sally’s replacement.
3. **Silena’s history and agency:** Do not resolve her relationship with Maria or make Silena responsible for Amphitrite’s feelings.
4. **Clarisse’s grievance:** Do not turn Amphitrite’s care into forgiveness of Poseidon or an obligation to visit Atlantis.
5. **Planned vs witnessed events:** Label the sisters’ future “Mom” milestones as planned in continuity profiles; do not insert them into the Chapter 001–193 timeline.

No automated tests are planned for these editorial changes. Use source comparison and manual review of the affected passages and GitHub diff.

---

### Task 1: Audit Percy’s existing address to Amphitrite

**Files:**
- Read: `chapters/001-193-*.md` at the pinned PR #103 branch head
- Read: `FIC_CONTEXT.md`

**Interfaces:**
- Produces: Exact chapter and line candidates where Percy directly addresses Amphitrite or refers to her informally as “Mother,” with enough surrounding dialogue to confirm speaker and meaning.

- [ ] Search the current GitHub chapter files for Percy’s spoken “Mother” uses and other direct-address variants; do not use the deprecated local copy.
- [ ] Read each candidate in its scene context and record whether it is Percy’s dialogue, another speaker’s dialogue, or narration.
- [ ] Check the result against the already-confirmed Chapter 99 address and Chapter 132 family reference before editing.

**Check:** Every proposed wording edit has a source locator and speaker confirmation; no global replacement is proposed.

### Task 2: Update Percy’s dialogue

**Files:**
- Modify: `chapters/099-mothers.md`
- Modify: `chapters/132-a-month-beneath-the-sea.md`
- Modify: Any additional Chapter 001–193 file only if Task 1 confirms Percy’s own informal address

**Interfaces:**
- Consumes: Task 1’s confirmed address candidates.
- Produces: Percy uses “Mom” in the confirmed dialogue, with surrounding scene facts and other speakers’ words preserved.

- [ ] Change Percy’s Chapter 99 spoken address from “Mother” to “Mom.”
- [ ] Change Chapter 132’s informal family reference from “Mother” to “Mom.”
- [ ] Apply the same targeted change only to any additional Percy dialogue confirmed by Task 1; do not replace formal or descriptive uses by other characters.

**Check:** Read each changed paragraph against its source version; confirm that only Percy’s chosen term changed and Sally’s grief remains intact.

### Task 3: Record the canon and continuity arc

**Files:**
- Modify: `FIC_CONTEXT.md`
- Modify: `continuity/character-states/percy.md`
- Modify: `continuity/character-states/silena.md`
- Modify: `continuity/character-states/clarisse.md`

**Interfaces:**
- Consumes: The approved spec and Task 2’s confirmed prose changes.
- Produces: Canon guidance plus profiles that separate source-confirmed relationships from planned future milestones.

- [ ] Add the voluntary chosen-mother arc and title boundaries to the relevant family/memory guidance in `FIC_CONTEXT.md`.
- [ ] Update Percy’s profile to record “Mom” as his chosen spoken address while retaining Sally as his mother and Amphitrite’s knowledge limit.
- [ ] Add a clearly marked future-arc note to Silena’s profile: she may choose “Mom” first after sustained care that respects her individual interests and boundaries; do not mark it as an event.
- [ ] Add a clearly marked future-arc note to Clarisse’s profile: she may choose “Mom” later after repeated care that respects her history and grief; do not mark it as an event.
- [ ] Keep the sisters’ relationships with their own mothers and Clarisse’s grievance with Poseidon explicit.

**Check:** The new notes do not alter the witnessed timeline through Chapter 193 or imply that either sister has already used the title.

### Task 4: Review the editorial diff

**Files:**
- Review: All files changed in Tasks 2–3

**Interfaces:**
- Consumes: Completed prose and canon/profile edits.
- Produces: A bounded, internally consistent PR diff.

- [ ] Read the full diff and confirm no unrelated chapter or continuity facts changed.
- [ ] Re-read Chapters 99 and 132 around each Percy wording change, and compare the sister-relationship notes against Chapters 125, 128, 129, and 132.
- [ ] Confirm future title milestones remain labeled as future work after Chapter 193.
- [ ] Report the files changed and the manual review performed; do not claim that future scenes or either sister’s title milestone are complete.

**Check:** The diff matches the approved spec, and every acceptance criterion is represented in the changed prose or continuity guidance.

---

## Execution note

Each GitHub Contents API file update creates its own commit on the existing PR branch. Keep writes sequential, re-fetch the branch head before each write if another update occurs, and review the resulting PR diff before reporting completion.
