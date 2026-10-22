# Manuscript-wide prose and character-voice overhaul — October 22, 2026

**Author directive:** Improve the prose and style of **every existing chapter, 001–213**, beginning with the in-progress PR #103 family arc. Aim for **at least 70 words in substantial narrative paragraphs** where the scene naturally supports it, remove habitual staccato dialogue, retire robotic/managerial speech, and portray specific people with desires, contradictions, humor, anger, grief, attraction, resentment, fear, and imperfect judgment. The manuscript must sound like a novel, not a compliance checklist or a transcript of negotiations.

**Scope and source:** Source of truth is the latest chapter text on PR #103's head `audit/four-phase-continuity-2026-10-13`, initially pinned on this editorial branch at `45a0719f3066799c359a829ad66e8213ae36832a`. This editorial branch is separate; PR #103 remains draft and unmerged. Newer changes on PR #103 must be reconciled before landing. Existing locked canon and cumulative memory still apply. Do not treat these edits as completed certification of any untouched chapter.

## Prose contract

1. **Narrative:** Target full, varied paragraphs whose concrete observation, interior reaction, or physical movement earns the space. Use 70–140+ words when naturally suited; a 20-word beat, a quick transition, or an isolated moment can still be right. The target applies mainly to narrative paragraphs, **not every spoken turn**. Never merge different speakers into a single paragraph merely to reach 70 words. Never pad with stock weather, repeated emotion labels, or ornamental adjectives.
2. **Dialogue:** Eliminate systemic one-question/one-answer loops; repeated "I know," "Okay," "Do you want," "That's not the same," "You can," and performative corrections when they do not reveal character. Let responses ramble when plausible, interrupt, mishear, deflect, complain, change subject, tell jokes, contradict an earlier claim, or remain angrily unresolved. Characters should speak from their specific history, not explain lessons about agency, fairness, and consent.
3. **Emotion:** The viewpoint character may feel love and resentment at once; distress need not be well articulated. Do not immediately translate gesture to the correct psychological interpretation. Show feelings through memory, private perception, unwanted impulses, practical choices, and consequences. Give the supporting cast private motives beyond demonstrating someone else's growth.
4. **Story:** Each scene must have a situation, competing wants, change, and residue. Reject repetitive sequences of maintenance problem → permission exchange → corrected wording → harmless error → calm acknowledgement → checklist update. Domestic scenes are welcome when they are alive, varied, and consequential.
5. **Voice:** Percy irreverent, impulsive, observant, sometimes clumsy in care; Annabeth intelligent and proud, sometimes controlling and wrong, with warmth and mischief; Thalia impatient, fiercely protective, capable of bitterness; Clarisse blunt, proud, angry, deeply loyal; Silena creative, perceptive, sometimes evasive and frustrated; Amphitrite an affectionate, political mother with her own pain and agency; Zeus capricious, powerful, self-justifying and frightening in ordinary conversation; Leandros defensive, skilled on the water, proud, capable of tenderness; Ianthe ambitious and observant, desperate for praise while resisting condescension. Other characters require equivalent individually observed patterns.
6. **Canon and POV:** Preserve chapter chronology, ages, cabins, parentage, time-memory boundaries, injuries, objects, promises, romances, and secrecy. Percy and Annabeth alone remember their erased future; they remain an established couple. Leandros and Ianthe are their specified paternal half-siblings. Silena's private title for Amphitrite is not known to Percy or Clarisse. No mechanical/regex rewrite should be committed as literary editing.
7. **Acceptance:** Full chapter must be reread end to end and undergo developmental then line/dialogue edits; compare preceding final scene, following opening, and current character handoff. Confirm >=10,000 **body** words per numbered chapter, order, source-anchored memory, and every-offset 300-word duplicate checks. Record *editorial pass* only when those checks are actually complete; machine QA alone is never proof of quality.

## Current progress — truthful and scoped

| Chapter(s) | Editorial state | Scope |
| --- | --- | --- |
| 001–193 | **Not yet passed under this new directive** | Preserve old continuity and earlier edits; each must still undergo a human prose/voice and scene-level pass. Historical mechanical QA does not certify prose. |
| 194–208 | **Not yet revised under this directive** | Recent family-first chapters need substantial developmental rewriting: repetitive repair/task structure and clipped correction dialogue are known risks. |
| 209 | **Partial rewrite committed; full-chapter pass pending** | Zeus/Ianthe/Thalia/Annabeth confrontation rewritten to restore volatility, distinct voices, sustained narration and emotion. Surrounding scenes remain to review. |
| 210 | **Pending** | Cabin window and sibling scenes; avoid repeated measurement and permission patterns. |
| 211 | **Partial rewrite committed; full-chapter pass pending** | Silena's private “Mom” choice scene rewritten with grief, affection, guilt and emotional complexity. Remaining scenes still require line edit. |
| 212 | **Pending** | Leandros's navigation skill should create stakes, not become a sequence of procedural corrections. |
| 213 | **Partial rewrite committed; full-chapter pass pending** | Opening Percabeth scene, basin argument/parental-absence sequence and final Leandros conversation revised; unedited passages remain. |
| 214–218 | **Not drafted as of this branch's source checkpoint** | Do not claim completion. New chapters should adopt this standard when drafting resumes. |

**Critical distinction:** "Partial rewrite committed" is not "chapter completed." The user's request covers the full 213 existing chapters. A complete manuscript-wide rewrite requires successive source-grounded chapter passes and QA; no automated paragraph merging is an acceptable substitute.

## Working order

- First complete the *rest* of 209, 211, 213; then work back through 194–208, including 210 and 212. The family-first arc should be internally coherent before new installments.
- Then 001–193 in contiguous five-chapter batches, using current source snapshots and adjacent chapter handoffs. Identify high-quality scenes worth preserving; correct artificial speech and narrative sameness, not merely increase length.
- For every batch, log original/revised body words, specific edited files, narrative paragraph distributions (informational only), character/POV continuity, repeated-scene findings, duplicate-window test results and an editorial signoff. Preserve the user's wording where it already works.
- Do not merge this editorial branch directly into main. Reconcile PR #103 changes first, obtain review, and land bounded changes on its head branch or through a child PR.

## Evidence and limitations

On this branch, the first scoped replacements were written and committed in Chapters 209, 211 and 213. No one has read and recast all 213 chapter files during this pass. End-to-end chapter editorial reviews, all-chapter prose metrics, full-manuscript duplication checks and hosted Actions for the new branch remain unverified until expressly run.
