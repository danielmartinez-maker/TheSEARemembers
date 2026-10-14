# Character memory continuity: targeted corrections

**Date:** 2026-10-13  
**Branch:** edit/character-memory-continuity-2026-10-13  
**Scope:** Confirmed Amphitrite/Percy, Annabeth and Cabin Three memory failures; new persistent-memory procedures. This is **not** a completed semantic audit of all 193 chapters.

## Confirmed contradictions and patches

| ID | Established earlier scene | Problematic later scene, before patch | Resolution on branch | Status |
|---|---|---|---|---|
| M-01 | Ch. 30: Amphitrite meets Clarisse and Silena in person, discusses their family, shares lunch | Ch. 118: she says she is glad to 'meet you properly' as though it is a first meeting | She explicitly remembers their camp lunch; Clarisse remembers it too | **Fixed** |
| M-02 | Ch. 30: Amphitrite meets and embraces Annabeth, gives her a pearl bracelet | Ch. 123: 'And you are Annabeth. Percy has told me about you' reintroduces her | Amphitrite greets Annabeth by name and refers back to the camp lunch | **Fixed** |
| M-03 | Ch. 1 and FIC_CONTEXT §2.1: Amphitrite must not know Percy's old-timeline memories or autobiographical childhood gap | Ch. 99: she explicitly describes 'the life you remember' and 'years you cannot remember' | Amphitrite talks about the Sally history **she actually knows**, while Percy can still thank her as 'Mother' | **Fixed** |
| M-04 | Ch. 99: Percy explicitly chooses to call Amphitrite 'Mother' | Ch. 118 greeting risks another emotionally blank reset after that important step | Percy greets her as 'Mom', showing the choice carried forward without forcing the word into every interaction | **Fixed** |
| M-05 | Ch. 1: Sally and Amphitrite did not meet personally; timeline secret remains concealed | Ch. 126: Percy openly says he told Amphitrite about Sally's remembered-life kitchen; Amphitrite says she exchanged letters with Sally | Percy keeps the source of the mosaic private. Amphitrite knows Sally from Poseidon's stories rather than newly invented correspondence. Sally-related dialogue before the group avoids timeline disclosure. | **Fixed** |
| M-06 | Ch. 1: no disclosure of lost altered-childhood autobiographical memory | Ch. 127: Percy discusses remembering his childhood and Amphitrite responds about 'missing years' | Their conversation addresses returning to a changed home after time at camp, without granting her forbidden knowledge | **Fixed** |
| M-07 | Ch. 14: Amphitrite talks to Annabeth via Iris-message and thanks her for caring for Percy | Ch. 30: Amphitrite says 'And you must be Annabeth' and Annabeth treats it as first-ever acquaintance | The meeting is now explicitly **in person**, with a callback to the prior Iris-message | **Fixed** |
| M-08 | Ch. 32: Triton encounters Clarisse, Silena and Annabeth, and spars with Clarisse | Ch. 86: Triton says 'You must be Clarisse' and 'You must be ... Silena'; treats Annabeth as a newly liked stranger | He recalls the camp duel, recognizes Silena, and says he **still** likes Annabeth | **Fixed** |
| M-09 | Ch. 14 and Ch. 30: Annabeth already knows Amphitrite and received a bracelet from her | Ch. 120: Clarisse says Annabeth has **never met** Amphitrite, and Annabeth agrees | Annabeth refers to the established picnic, bunk inspection and bracelet | **Fixed** |
| M-10 | Ch. 1: Amphitrite is unaware Percy lacks memory of his altered childhood | Ch. 123: Percy assumes Amphitrite understands that he cannot remember the childhood story she tells | Percy's interior monologue preserves his secret while listening to a normal family anecdote | **Fixed** |

## Stable story rules to carry forward

- Percy remembers **choosing** to call Amphitrite Mother. He also remembers the Ch. 30 camp visit, Ch. 99 gifts, Ch. 118 invitation and subsequent palace experiences. He can still grieve Sally and sometimes choose a formal title.
- Amphitrite remembers the childhood she raised; Percy does not automatically remember it. Her knowledge comes from her life and subsequent conversations, **not** from Percy's unrevealed displacement.
- Annabeth and Amphitrite know each other from Ch. 30. Annabeth also has her own gift and later garden interactions.
- Clarisse and Silena remember meeting Amphitrite, receiving invitations and negotiating expectations. Their varying comfort with her remains an active choice.
- New scenes must carry shared interpersonal history and ongoing practical consequences (injuries, gifts, correspondence, grudges, reconciliation).
- Each character has a **local** knowledge state. Knowing that Percy or Annabeth described a different history is not the same as having first-person memories of it.

## Review method and limits

I inspected anchored passages including **001, 013, 014, 019, 025, 030, 032, 066, 074, 086, 099, 118, 120, 123, 126, 127, 128, 129, 132, 170, 177, 186 and 193**. I also ran a **full 193-chapter plus two-interlude lexical screen** for likely first-meeting dialogue, which found additional candidates for manual inspection. In total, I made **21 localized prose replacements in eight chapters**, updated FIC_CONTEXT, and added the ledger and reusable handoff. Surrounding scenes were preserved.

**Open review:** The lexical screen covers every numbered chapter and both interludes but is **not a semantic full-book audit**. It cannot reliably detect gradual emotional resets, forgotten private promises, changed objects, or all knowledge leaks. Other chapters still require source-based relationship checks when edited or referenced. Future writing must verify prior interactions and append ledger entries.

**Regression verification:** The eight patched chapters passed 8/8 direct positive/negative content checks after the changes. A repository script and GitHub Actions workflow were added to repeat source-anchored checks and flag suspicious introductions for human review. The automated checks cannot certify emotional or knowledge continuity on their own.

**No claim made:** This branch does not certify all chapters' word counts, global 300-word duplication checks, or PDF exports.
