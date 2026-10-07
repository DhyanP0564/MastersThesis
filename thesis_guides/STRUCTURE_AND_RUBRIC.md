# STRUCTURE_AND_RUBRIC.md — The Rubric, the Guidelines and the Exemplars

Built from the official *Master of Physics Thesis Mark Sheet* (`Theses-AssessmentRubric.pdf`),
the School's *Master Thesis Guidelines* (`marking_guide.pdf`), and two high-scoring exemplars:
Green 2024 (Honours, *Efficient Quantum State Preparation*) and Snow 2026 (Masters, *Highly
Optimised Quantum Circuit Synthesis for Classical Data Encoding*).

**What this file is.** The reference for *what is marked and what good looks like*. The thesis's
structure, contributions, chapter plans and checklists are in `../ThesisPlanning.md` (v2.0); the
facts a draft may state are `../CLAUDE.md`'s Standing Facts. Version 2.0 of this file
(2026-10-01) removed the pre-plan section tree, page budget, per-section deliverables and
traceability matrix, which the plan had superseded; they are in git history at `4b4e423`.

---

## 1. How the thesis is assessed

The unit's mark: **supervisor's assessment of the research 30%, the written thesis 60%, the
seminar 10%.** The thesis is marked by independent readers, not the supervisor, against this sheet:

| criterion | marks | top band (verbatim) |
| :-- | --: | :-- |
| **Introduction & Literature Review** | **/20** | "Comprehensive, superior understanding of the historical background and state of the art, **with excellent connection of the current field to the project**" (≥ 18). *"A critical assessment of the strengths and weaknesses of the material reviewed is required for a high distinction."* |
| **Project Body (Modelling)** | **/60** | Model Formulation /30 and Results & Discussion /30, below |
| **Conclusions & Topics for Further Investigation** | **/10** | "Detailed, comprehensive and insightful conclusions **and significant suggestions for further investigation**" (≥ 9.0). They "need to be supported by the results and discussion and relate back to the original goal of the report." |
| **Style & Presentation** | **/10** | "**Flawless**" = 10.0; "few insignificant errors" = 8.0–9.9; "significant errors" = 6.0–7.9 |

**The project type is Modelling** (ThesisPlanning.md T-02). Its two components, verbatim:

| Model Formulation /30 | |
| :-- | :-- |
| requirement | "The model formulation should be described in sufficient detail to permit readers to create equivalent models. This should include: **a description of any software tools used and/or created; a description and/or diagram of the model configuration; descriptions of the model input options selected** (boundary conditions, constitutive behaviours etc)" |
| band 4 (27+) | "Superlative model yielding relevant results capable of deep interpretation or providing a significant advance in the state of the art or **warranting publication in an international peer reviewed journal**." |
| band 3 (22–26.9) | "Good model capable of yielding valid results but the description lacking in some respect e.g. minor omissions in description, **poor design of numerical experiment**" |
| band 2 (16–21.9) | "Adequate model formulation, inadequately described in multiple respects (eg. values of key parameters omitted, and conditions)." |

| Results & Discussion /30 | |
| :-- | :-- |
| requirement | "The results need to be presented in a way that is easy to understand, **without reference to any other documents**. The discussion needs to show your understanding of the meaning of your findings and the consequences of them for the field. There is no need to include detailed codes, which could be included in appendix if desired." |
| band 4 (27+) | "Complete, clearly presented results, with detailed discussion showing **insight into the significance of the work** or warranting publication in an international peer reviewed journal." |
| band 3 (22–26.9) | "Clear description of the results with discussion of most of the implications of the work" |

**Fallback.** If a marker ticks Theoretical instead, the split is Groundwork /40 and Results /20;
its top band asks for "outstanding description and detail in the background and setup of the
calculations which follow, as would appear in a well written journal article", including "the
notations and conventions that are being adopted" and enough detail "to reproduce the results".
The plan's formulation chapters are written to satisfy both (ThesisPlanning.md TR-10).

---

## 2. What the guidelines require (formal; a penalty or refusal otherwise)

1. A PDF on LMS by Friday 4 pm of the last week of the last semester; late submission is
   penalised unless special consideration is granted.
2. **Body 40–60 pages**, "including figures but excluding contents, research proposal, and
   appendices"; overrunning 60 is penalised. 12 pt font, 1.5–2 cm margins on all edges.
3. A separate **one-page Summary of Student Achievement, in the first person**, outlining
   "exactly what **you** did".
4. **The research proposal as an appendix**, "and significant deviations from what was proposed
   should be noted and explained".
5. The supervisor's **electronic signature** endorsing the submitted copy, and the signed
   **declaration page** (the guidelines' wording).
6. "Areas where help has been received should be identified and acknowledged."
7. General content: introduction (including literature review), theoretical background, results
   and analysis, conclusion and discussion, future work.
8. Written "for physicists who are not specialists in the field", with "only a brief description
   of the experimental techniques and background with **the bulk of the report dealing with
   results and discussion** of them and their significance".
9. Research should stop at the end of the non-teaching break of the last semester; drafts go to
   the supervisor for "editorial advice as to style, content, and detail", starting from "a
   general layout for approval".

---

## 3. What the rubric rewards, read closely

### 3.1 Publishability is the literal top band

"Warranting publication in an international peer reviewed journal" appears in both Project Body
criteria. Test every drafting decision against it: would a referee accept this paragraph, this
figure, this claim?

### 3.2 Critical assessment is the Intro & Lit gate

A survey caps at band 2–3 (11.0–17.9). The HD needs a verdict on each strand, and "excellent
connection of the current field to the project". The plan earns it twice: §2.2(e)'s comparison
table with a *this work* row, and Chapter 3's critical assessment of Wu et al., which turns the
paper's own open questions into the three questions the thesis answers. **"Historical
background"** is named too: §2.2 gives each family's history, not only its present.

Chapter 3 sits among the body chapters, so a marker skimming the contents may file it under
formulation. Its first sentence must say it reports prior art, and its last section must read as
a gap statement.

### 3.3 Negative and partial results are protected

> "If the results are negative, there will not be a penalty **if a detailed discussion/analysis is
> given**." (Experimental R&D)

> "It is important to realise that a thesis can be an excellent one, even though the project did
> not achieve its aims." (Guidelines, Part A)

This licenses every honest caveat the work carries, **each with its analysis**: no hardware;
circuit simulation only at small n (exact emulation, proven equal, beyond it); the spectral edge
assumed known; the descriptor's gap falling on two axes and its double-zero limit; reversals of the
cost comparison at the ideal-encoding bound (R3) and on the heat panel at small n; the doubled
space projecting; a trusted kernel hiding a diverging Carleman lift; Navier–Stokes reached by
emulation and estimate only; the DCT a cited primitive; the paper's Figs 6–7 unreproduced. Stating
these with analysis costs nothing and evidences "insight into significance"; a marker who finds one
the thesis concealed takes the band.

### 3.4 Self-containment is required twice

Results must be understandable "without reference to any other documents". The appendices are
part of the document; the repository is not. Every number in the body is derivable from the body
or an appendix, and quoted by key from the archived records (`0_results/README.md`).

### 3.5 Formulation means a model someone else could rebuild

The rubric names three things a formulation chapter must contain: the **software** used or
created, a **configuration diagram**, and the **input options** (the rubric's own example is
boundary conditions). Band 3's named failure is a **poorly designed numerical experiment**, so the
design (what varies, what is held fixed, how costs are counted, why the comparison is fair)
belongs in the body. "No need to include detailed codes": describe, never list.

---

## 4. Calibration against the exemplars

### 4.1 Their structure

| | Green 2024 (Honours, ~50 pp) | Snow 2026 (Masters, ~60 pp) |
| :-- | :-- | :-- |
| introduction | 3 pp: gaps and contribution, significance, organisation | 3 pp: motivation, contributions, outline |
| background | 4 pp of QC definitions | 14 pp of theory, with propositions and proofs |
| literature | 9 pp, a *critical* review ending "Summary of Issues" | 7 pp in four strands, each assessed, ending "Synthesis: the gap this thesis addresses" with two italic questions |
| contributions | MPS chapter 21 pp (theory, methodology, two numerical studies, an application, summary); QSP chapter 11 pp (theory, new algorithm, complexity, comparison tables) | method chapter 7 pp → results chapter 5 pp; method chapter 4 pp → results chapter 16 pp; each results chapter ends "Summary" |
| close | future research 1.5 pp; conclusion 1 pp | conclusions and future work 4 pp: a quantitative summary of findings, significance, **Limitations**, four future directions |
| appendices | A–I: proofs, algorithms, extra results, circuits | A–G: initialisation study, global optimisation, proofs, parameterisation, the target-state table |

### 4.2 What both do, and the plan copies

1. **Abstracts with numbers** (99.6% fidelity; an order of magnitude at fixed depth).
2. **A named gap section closing the literature**, posing explicit questions that later chapters
   answer by name (Snow §3.6). Ours: Chapter 3's closing, Q(i)–(iii).
3. **Design rationale before mechanism** (Snow §4.1: "the question is what to optimise"). Ours:
   §5.1 "The idea".
4. **One formal result with a short proof and two paragraphs of interpretation** (Snow's Theorem
   4.1). Ours: the kernel-equivalence theorem, the factorisation and the stacked reflection.
5. **Cost conventions declared before the first comparison, with their bias** (Snow, Ch. 7's
   opening: the worst-case CNOT bound "is deliberately conservative… any advantage reported below
   is thus a lower bound"). Ours: §7.8, the strongest baseline and the ideal-encoding bound.
6. **Comparison tables with a "This Work" row** (Green Tables 5.3–5.4; Snow Table 5.1). Ours: T1
   and T7.
7. **Numbered findings, some negative** (Green's four, two negative; Snow's §5.3). Ours: §8.7.
8. **Self-standing, claim-first captions** (Snow Fig. 7.1–7.12).
9. **A practitioner's map of where each method applies** (Green Fig. 4.18). Ours: Table T9.
10. **A Limitations paragraph in the author's own voice** (Snow §8.1). Ours: §9.6.
11. **A catalogue of every target in an appendix** (Snow App. G). Ours: Appendix J.

### 4.3 What not to copy

- **Long textbook background.** Green spends 4 pp defining qubits and Pauli matrices; Snow 14 pp,
  which his 60-page Masters thesis can afford only because his contributions are compact. Ours is
  capped at 1.5 pp of QC preliminaries.
- **Superlatives.** Snow's conclusion calls his framework "field-leading" and claims "no prior
  method combines these properties". Claim what is measured, scoped; let the comparison table speak.
- **Errors a careful reader finds.** Green: "von Nuemann", Schmidt coefficients summing to 1 rather
  than their squares, θ^(t=1) for θ^(t+1) in an update rule. Snow: a figure title copied onto
  the wrong figure (Fig. 7.12), a results claim contradicted by its own appendix (warm start
  "systematically superior" against Appendix A's trapping regime). Each costs the Style mark and
  the reader's trust.
- **Typed numbers that drift.** Neither exemplar has a mechanism tying numbers to results; ours
  does (`\res`), and the rule is never to bypass it.

---

## 5. Style & Presentation — "flawless" for full marks

Only "flawless" earns 10.0; the proofreading marks are the cheapest in the rubric.

**Known in the draft:**

1. `ref.bib`: `wu2025pihm`'s author list is wrong (the paper is by Hsin-Yu Wu, Annie E. Paine,
   Evan Philip, Antonio A. Gentile and Oleksandr Kyriienko), and `note` fields print internal
   repository notes (ThesisPlanning.md T-29).
2. `main.tex`: `\nocite{*}` pulls every `ref.bib` entry into the bibliography; a stray `\todo`.
3. `2_body/2_literature.tex`: a stray `` `' `` after `\end{pmatrix}`; "initial**ized**".
4. Outstanding `\todo` notes across the body.

**Pre-submission sweep:**

1. Compile clean: zero warnings, no overfull `\hbox` in the body.
2. Every figure and table referenced by `\Cref`, none orphaned; captions below figures, above
   tables.
3. Symbols consistent (Verification Mode, `../CLAUDE.md`), notably `A` and `H` subscripted by form
   everywhere except Chapter 7.
4. Acronyms defined at first use; `glossaries` complete.
5. Bibliography uniform (IEEE `biblatex`), arXiv IDs where applicable, every entry checked.
6. Page count within 40–60; declaration signed; Summary of Student Achievement one page, first
   person; the proposal and its deviations in Appendix M; the supervisor's endorsement.
7. Read the whole thesis aloud once.

---

## 6. Traceability

The criterion-by-criterion map of where each mark is earned is ThesisPlanning.md §14.3.

*Companion documents: `../ThesisPlanning.md` (structure and plan), `STYLE_GUIDE.md` (register),
`../CLAUDE.md` (working agreement and Standing Facts).*
