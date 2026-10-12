# Chapter 001 editorial audit
## The Weight of Salt and Sky

**Status:** Audit complete; source prose unchanged.
**Basis:** GitHub `chapters/001-the-weight-of-salt-and-sky.md` at blob `e1b194a905b73ed0225708a2c08b114624b11611`, checked against the repository's `FIC_CONTEXT.md` as of 2026-10-12.
**Method:** Full chapter read, spot-check of opening of chapter 2, mechanical phrase count, canon/rule-by-rule review.
**Mechanical count:** Approximately **10,097 body words**, calculated by splitting whitespace after excluding the Markdown chapter heading and `---` dividers; this is a reproducible approximate measure, not evidence that the prose meets quality standards.

### Editorial verdict

**Do a structural continuity pass before any broad line editing or word-count expansion.** The chapter already contains its essential emotional material: Percy's uncertainty about the new family; Amphitrite's refusal to make Sally into a rival; recognition with Annabeth; protective Thalia; first contact with Percy’s Poseidon siblings. The major obstruction is that stitched-together passages place events out of order, sometimes physically repeating them. Several sentences also overstate what Percy could know about a childhood he cannot remember.

**Preserve:** the opening awakening; Percy recognizing Grover without being recognized; the Sally/Amphitrite distinction; Annabeth's genuine familiarity with Percy and missing shared history with Thalia; sibling setup for Clarisse/Silena; Thalia as guarded rather than villainous. Maintain an affectionate, nonsexual Percabeth beat and a tangible family interaction.

### Confirmed continuity and assembly faults (fix first)

| ID | Severity | Source lines | Diagnosis | Minimum viable repair |
|---|---|---|---|---|
| C01 | **Critical** | [L414–418](../../chapters/001-the-weight-of-salt-and-sky.md#L414-L418), [L446–456](../../chapters/001-the-weight-of-salt-and-sky.md#L446-L456), [L486–504](../../chapters/001-the-weight-of-salt-and-sky.md#L486-L504), [L526–570](../../chapters/001-the-weight-of-salt-and-sky.md#L526-L570) | Percy and Grover are already walking through camp, and Grover discusses Percy's *reaction* to Annabeth before the text stages the first meeting. They later crest the hill after already walking inside camp. This is a genuine sequence error, not a mystery clue. | Put the approach and hilltop view **before** the first walk through camp; place the Grover observation **after** Percy actually meets Annabeth, or save it for Chapter 2. Remove duplicate tour/setup. |
| C02 | **Critical** | [L314–318](../../chapters/001-the-weight-of-salt-and-sky.md#L314-L318), [L336–358](../../chapters/001-the-weight-of-salt-and-sky.md#L336-L358) | Percy and his parents breach into sunlight, continue rising underwater, discuss whether Poseidon will accompany him *to* the surface, then rise again and emerge again. | Rebuild the travel scene as underwater ascent → discussion of the surface → final emergence → landing/dock goodbye. Preserve one arrival. |
| C03 | **High** | [L156–176](../../chapters/001-the-weight-of-salt-and-sky.md#L156-L176), [L210–240](../../chapters/001-the-weight-of-salt-and-sky.md#L210-L240), [L314](../../chapters/001-the-weight-of-salt-and-sky.md#L314) | “Night before his departure” is followed by “That evening,” a scene that concludes “By morning,” then a further morning conversation and “The morning of his departure.” The relative times cannot all work as currently staged. | Place the garden conversation and last-night brother conversation at clear points in the final week; retain only one final morning of departure. |
| C04 | **High** | [L790–822](../../chapters/001-the-weight-of-salt-and-sky.md#L790-L822) | Percy closes his eyes, lies in his bunk, and sleeps. The narrator then adds another ending in which Percy looks up at the stars, speaks, and goes inside. | Choose one closing scene. Better option: stop at the cabin and close with a distinct emotional choice rather than a second prophecy/resolve paragraph. |
| C05 | **High** | [L7](../../chapters/001-the-weight-of-salt-and-sky.md#L7), [L75–81](../../chapters/001-the-weight-of-salt-and-sky.md#L75-L81), [L105](../../chapters/001-the-weight-of-salt-and-sky.md#L105) | Percy initially cannot remember mornings beneath the Atlantis ceiling, yet later “remembered [the palace] from his original life,” knows guards and training-wing routines, knows Poseidon's “usual form,” and says the original-life Percy is no longer the child of Atlantis. These are **unearned autobiographical memories** under the bible. | Separate bodily familiarity or external knowledge from actual first-person memory. Let him infer or be told palace specifics rather than narrating them as lived memories. |
| C06 | **High** | [L732](../../chapters/001-the-weight-of-salt-and-sky.md#L732) | After dinner, the dock scene has both moonlight and sunlight lingering warmly on their shoulders. | Commit to night: remove the direct sunlight, retain night air and lake texture. |
| C07 | **Moderate** | [L536–544](../../chapters/001-the-weight-of-salt-and-sky.md#L536-L544) | Annabeth “pulled the door shut” yet the door subsequently “stopped” and she turns. The prose implies complete closure before interruption. | “Started to pull the door shut” or equivalent; have Percy's voice interrupt the motion. |
| C08 | **Moderate** | [L61–69](../../chapters/001-the-weight-of-salt-and-sky.md#L61-L69), [L101](../../chapters/001-the-weight-of-salt-and-sky.md#L101), [L156](../../chapters/001-the-weight-of-salt-and-sky.md#L156) | Amphitrite tells Percy his father wants to see him “before you go,” but Poseidon says departure is a week away. Not impossible conversationally, but misleading timing. | Say Poseidon wishes to see him *that morning* or wants to talk about the visit, rather than framing it as immediate departure. |

### Canon and causality to clarify (do not introduce new lore automatically)

| ID | Severity | Source lines | Diagnosis | Proposed handling |
|---|---|---|---|---|
| K01 | **High** | [L97–99](../../chapters/001-the-weight-of-salt-and-sky.md#L97-L99), [L13](../../chapters/001-the-weight-of-salt-and-sky.md#L13) | Poseidon says Percy has seemed older “these past few weeks,” even though the opening seems to be the immediate onset of Percy’s displaced memories. | Choose explicitly: are there weeks of observable changes before the narrated awakening, or is Poseidon's suspicion limited to today? The bible does not establish prior weeks of Percy’s change. |
| K02 | **High** | [L118–138](../../chapters/001-the-weight-of-salt-and-sky.md#L118-L138) | The secret about old gods has unclear logic. The old gods ask Poseidon where *they* hid *their own* sacred sites; he then promises not to tell anyone, and later says he has told no one though Amphitrite apparently knows he will disclose something. | Define who hid the places, what Poseidon knows, and what promise he actually made. If this mystery is intentional long-range setup, keep the secret but clarify the grammar and stakes. Do not invent a time architect or identify Kronos. |
| K03 | **Moderate** | [L720–728](../../chapters/001-the-weight-of-salt-and-sky.md#L720-L728) | Clarisse counts herself, the Zeus sisters, and Percy as Big Three children, but excludes Silena, although Silena is also Poseidon's daughter. | Either include Silena, make it clear the list is informal/non-exhaustive, or revise the dialogue. |
| K04 | **Moderate** | [L328–346](../../chapters/001-the-weight-of-salt-and-sky.md#L328-L346) | Poseidon tells Percy he will be significantly weakened on land, while Percy silently senses atmospheric and bodily water and claims broader original-life capabilities. This could be intended as an unreliable parental estimate, but the narration doesn't signal that. | Choose whether Poseidon is wrong/overprotective or whether the AU imposes a new limitation; do not inadvertently contradict established powers. |
| K05 | **Moderate** | [L248–274](../../chapters/001-the-weight-of-salt-and-sky.md#L248-L274) | Amphitrite accepts Percy reporting another lived timeline quite quickly. This respects the memory rule, but offers little uncertainty or follow-up despite an extraordinary claim. | Let her believe Percy's distress without automatically understanding the mechanics. Consider a practical follow-up question, hesitation, or a private worry. |
| K06 | **Low** | [L392](../../chapters/001-the-weight-of-salt-and-sky.md#L392) | A hoodie is said to hide Grover's goat legs. Unless unusually long, a hoodie would not conceal his lower legs. | Use trousers, the Mist, or clearly specify suitable disguise. |

### Sentence-level errors and repetition (after scene reordering)

| ID | Source lines | Current wording / behavior | Fix |
|---|---|---|---|
| P01 | [L39](../../chapters/001-the-weight-of-salt-and-sky.md#L39) | “Did you've the nightmare again?” | **Did you have**. |
| P02 | [L658–660](../../chapters/001-the-weight-of-salt-and-sky.md#L658-L660) | “Annabeth said, shifting **his** weight”; “Percy looked at her — **studied at her**.” | Correct pronoun and phrasing. |
| P03 | [L338–342](../../chapters/001-the-weight-of-salt-and-sky.md#L338-L342), [L754](../../chapters/001-the-weight-of-salt-and-sky.md#L754) | “I've to be at court”; “Wherever you're on the surface”; “I've to just carry that.” | Use natural contractions: “I have to,” “wherever you are,” etc. A global expansion pass may help, but inspect context. |
| P04 | [L67–744](../../chapters/001-the-weight-of-salt-and-sky.md#L67-L744) | Exact phrase **“shifting his weight against the cold” appears 12 times**, often mechanically appended to Percy’s dialogue. | Replace only where the action matters; remove most instances and vary with behavior *specific to the moment*. Do not swap for another repeated stock gesture. |
| P05 | [L23–166](../../chapters/001-the-weight-of-salt-and-sky.md#L23-L166) | “Salt air sharp in his lungs” appears **three times**, sometimes in underwater palace scenes. | Prefer physical description consistent with underwater breathing, current, pressure, or salt-taste, and avoid reusing a tagline. |
| P06 | [L706](../../chapters/001-the-weight-of-salt-and-sky.md#L706) | Pavilion has an “open-air” structure yet a “ceiling carved with constellations”; description also repeats “light/flickering light.” | Define pavilion roof structure or an illusion, and cut stacked descriptions. |
| P07 | [L320–324](../../chapters/001-the-weight-of-salt-and-sky.md#L320-L324) | “The surface animals ... none of them have teeth.” | If Poseidon is joking, put a clear cue in Percy's response. If meant literally, correct the fact. |
| P08 | [L772](../../chapters/001-the-weight-of-salt-and-sky.md#L772) | “First real smile” conflicts with Percy's prior smiles, including [L200](../../chapters/001-the-weight-of-salt-and-sky.md#L200) and [L222](../../chapters/001-the-weight-of-salt-and-sky.md#L222). | Distinguish the emotional *quality* of the smile instead of stating the first occurrence. |
| P09 | [L668–702](../../chapters/001-the-weight-of-salt-and-sky.md#L668-L702), [L740–760](../../chapters/001-the-weight-of-salt-and-sky.md#L740-L760) | Recognition, loneliness, relief, and promise are explained multiple times; two lakeside-style reassurance beats repeat similar emotional conclusions. | Preserve one full emotional exchange and let other beats introduce a new consequence or specific question. |
| P10 | [L482–484](../../chapters/001-the-weight-of-salt-and-sky.md#L482-L484), [L812–822](../../chapters/001-the-weight-of-salt-and-sky.md#L812-L822) | Multiple successive chapter-endings declare uncertainty and determination. | One primary closing beat; trim summary speeches that repeat the scene's meaning. |

### Strengths worth keeping (not automatic edits)

- [L3–35](../../chapters/001-the-weight-of-salt-and-sky.md#L3-L35): The awakening efficiently establishes displacement, physical change, and the remembered relationship.
- [L63–65](../../chapters/001-the-weight-of-salt-and-sky.md#L63-L65) and [L380–412](../../chapters/001-the-weight-of-salt-and-sky.md#L380-L412): Grover represents the cost of a familiar friendship becoming socially unfamiliar. His awkwardness works.
- [L254–300](../../chapters/001-the-weight-of-salt-and-sky.md#L254-L300): Amphitrite acknowledges Sally without demanding exclusive motherhood. The **Sally alive in remembered life / dead in altered life** distinction is accurately maintained here.
- [L564–610](../../chapters/001-the-weight-of-salt-and-sky.md#L564-L610): Percy and Annabeth recognize each other and explicitly retain original memories, as required. This is the central emotional payoff of the opening.
- [L626–648](../../chapters/001-the-weight-of-salt-and-sky.md#L626-L648): Thalia's guarded first reaction establishes later sisterhood tension without making her malicious.
- [L708–724](../../chapters/001-the-weight-of-salt-and-sky.md#L708-L724) and [L790–800](../../chapters/001-the-weight-of-salt-and-sky.md#L790-L800): The new Poseidon family is seeded, including Clarisse and Silena.

### Chapter requirements check

| Requirement | Result | Evidence / note |
|---|---|---|
| Percy and Annabeth remember their shared life | **Pass** | [L564–610](../../chapters/001-the-weight-of-salt-and-sky.md#L564-L610) |
| Percy/Sally/Amphitrite relationship and correct histories | **Pass, with memory inconsistencies elsewhere** | [L254–300](../../chapters/001-the-weight-of-salt-and-sky.md#L254-L300); C05 |
| Annabeth Grace, biological sister of Thalia Grace; both Zeus children | **Pass in main events** | [L504–512](../../chapters/001-the-weight-of-salt-and-sky.md#L504-L512), [L626–646](../../chapters/001-the-weight-of-salt-and-sky.md#L626-L646) |
| Clarisse and Silena Poseidon children | **Pass, but incomplete Big Three list** | [L720–724](../../chapters/001-the-weight-of-salt-and-sky.md#L720-L724), [L794–796](../../chapters/001-the-weight-of-salt-and-sky.md#L794-L796) |
| Third-person limited focus | **Mostly pass** | Mainly Percy; occasional claims of knowledge he does not have (C05) |
| Warm family centerpiece | **Pass** | Sally/Amphitrite conversation, Triton send-off |
| Established nonsexual Percabeth romantic beat | **Pass** | Recognizing one another, interlaced fingers, shared private conversation |
| Sibling beat in core cabin group (PCS or Grace sisters) | **Underdeveloped** | Clarisse gives a brief introduction; Silena's full exchange begins in Chapter 2. Percy/Triton material works as another sibling beat but not a full PCS introduction. |
| Forward-facing mystery without shortcut retcon | **Pass in premise; setup unclear** | Poseidon's secret, K02 |
| 10,000-word floor (if applied to this revision) | **Barely meets** | Approx. 10,097 body words. A substantial cut may place it below the target; repair using substantive interactions, not filler. |

### Proposed repair sequence, with no rewriting yet

1. **Create a precise scene order**: awakening → breakfast/father conversation → garden/Sally conversation during remaining week → final evening with Triton → departure and *single* emergence → Grover's approach/hill view → cabin orientation → Percy/Annabeth recognition → Thalia interruption → dinner/Clarisse → one private Percy/Annabeth follow-up → Cabin Three ending.
2. **Enforce memory limits** in every Percy POV sentence: he remembers Sally, original Camp Half-Blood, Tartarus, Annabeth, and some divine interactions, **not** a twelve-year Atlantean childhood.
3. **Resolve** Poseidon's ancient-gods conversation and the timeline of his suspicion without inventing extra time-rewrite rules.
4. **Strengthen the new-household setup** with a brief, distinct PCS exchange. More specific interaction is better than adding several generic reassurance paragraphs.
5. **Complete line edit**: grammar, unnatural contractions, pronouns, physical staging, and repeated gestures.
6. **Check chapter 2 handoff**: Percy meets Clarisse before bed, Silena at breakfast; location and family status should line up exactly.
7. **Recount body words, then run the manuscript assembly**, preserving a pre-revision version. Do not pad merely to cross 10,000 words.

### Continuity handoff for Chapter 2

- Percy: 12, remembers prior life through 17; new grief for Sally; has met Grover, Annabeth, Thalia, Clarisse by nightfall.
- Annabeth: 12, has retained remembered love for Percy; no genuine memories of growing up as Thalia's younger sister; stays Cabin One.
- Thalia: 16; protective and wary of the newly arrived Poseidon child, not omniscient and not a remembered-life holder.
- Poseidon siblings: Clarisse already introduced; Silena is present/assigned to Cabin Three, but Percy is to meet her properly the following morning.
- Setting: first night in Camp Half-Blood after arrival from Atlantis. Do not place Percy back in the palace without an established visit.
- Active threads: Poseidon's secret about ancient sites; identity of the time architect (unknown); new family expectations; sisters' conflicting memories; Grover's tentative friendship.
- **Chapter 2 should begin the next morning** with the sleeping arrangements and breakfast handoff consistent with Chapter 1's final canonical scene.

---

**Audit disposition:** Review saved; `chapters/001-the-weight-of-salt-and-sky.md` is unchanged. These are proposed editorial fixes, not already completed corrections.
