# StructuralReview.md — whole-manuscript structural review (2026-10-12)

*Review Mode, structural, against plan v3.3 and the build of 2026-10-12 (173 pp). Companion to
`ThesisPlanning.md`; where the two differ, the plan wins once it has been updated to adopt a finding
(status below). Line references are to the files at commit `dd21774`.*

**Status (2026-10-12).** F1, F2 and F3 applied as one pass (plan v3.4). Every move listed below was
made; zero undefined references in the build. The pass removed about 1,850 words of prose from
Chapters 4–7 (Ch. 4 −575, Ch. 5 −369, Ch. 6 −37, Ch. 7 −924), about 3.5 pp, and added about 80 to
Chapter 8. That is short of the estimates in §1: Chapter 7 is about 9 pp against a target of 6, and
Chapter 5 about 13.5 against 10.5. The remaining gap is Review Mode's to rank, not a further move of
this pass. F4–F8 open, in the order of §4.

**Status (2026-10-12, second pass; plan v3.5).** F7, F5 and F4 applied. F7: `tab:ladder` in §4.1 beside
the running example with its ordering principle, Chapter 7 pointing to it; "trusted" defined in two
sentences at its first use, §4.3 (it is used there before §4.4), the procedure left in §7.2. F5: Q(iii)
carries its second half in Chapter 3's item and closing line, Chapter 6's opening and §6.8's answer,
§8.4's new opening and close, plan §3.2, the style guide, and Chapter 1's scaffold. F4: Chapter 2
restructured (plan §5.2 v3.5) and drafted in full; it measures about 10.7 pp against 7, and plan §5.2
carries the ranked cut list and the recommendation to re-budget. Zero undefined references.

## Verdict

Keep the skeleton; do not move to line-editing yet. The chapter order, the three-question spine and
the Chapter 3 / Chapter 4 split are sound and visibly working in the drafts. But the draft is on
course for about 81 pages against a hard, penalised cap of 60, and the plan's trim order (§4.1)
recovers about 6. The overrun is not wordiness; it is allocation: the same evidence lives in the
formulation and the results chapters, the paper's defects are argued three times, and the pipeline
chapter has become a methods manual. Those are also where the narrative stalls. One reallocation pass
(moves and deletions, little new prose) fixes both; then edit.

## 1. Where the draft stands

| Ch. | plan pp | measured | projected if unchanged | target |
|---|---|---|---|---|
| 1 Intro | 3.5 | empty | 3.5 | 3 |
| 2 Background & Lit | 7 | 5 (mostly empty headings) | 8–9 | 7 |
| 3 PIHM | 3.75 | 5 | 5 | 4 |
| 4 Standard form | 6.5 | 11 | 11 | 7.5 |
| 5 Descriptor | 9 | 14 | 14 | 10.5 |
| 6 Extensions | 6 | 8 | 8 | 6.5 |
| 7 Pipeline | 5.5 | 11 | 11 | 6 |
| 8 Numerical study | 8.5 | 14 (7 placeholder figures) | 14+ | 10 |
| 9 Discussion | 3.75 | empty | 3.75 | 3 |
| 10 Conclusions | 2.5 | empty | 2.5 | 2 |
| **Total** | **56** | **≈ 67 drafted** | **≈ 81** | **≈ 59.5** |

The `\newpage \todo` spacers in `main.tex` add about 2 pp to the measurement. The targets leave no
slack; Chapter 5 is cut last.

## 2. What to preserve

- Chapter 3's assessment turning the paper's own open problems into Q(i)–(iii).
- Chapters 4–6 each open with their question and close with its answer.
- Chapter 5's arc: theorem → challenge (§5.5) → cure (§5.6) → "what it does not remove".
- Chapter 6's single thread: every extension that prepares is a coupled linear system on one state.
- §8.6's numbered findings with negatives.
- The chapter order (T-20). Moving the pipeline before the forms loses the tension before the
  machinery; folding results into each formulation chapter scatters the Results & Discussion evidence
  and orphans the ideal-bound comparison, which needs both forms.

## 3. Findings, ranked by marks at stake

### F1. The evidence lives in two places — *applied*

The R2a encoder looseness at n = 8 was quoted in Chapters 4, 5, 7 and 8; the n = 8 degrees in 4, 5
and 8; the R3a reversal in §5.6, §5.9, §8.2, §8.3 and §8.6; R7's mass-form gap in §6.1 and §8.4.
Chapter 4 held 16 references into Chapter 7 and 17 tier-labelled numbers, Chapter 5 held 13: results
quoted before the method that produces them, which reads as the band-3 failure "poor design of
numerical experiment", and leaves Chapter 8 as a rerun.

**Rule (plan T-20, v3.4).** Chapters 4–6 quote proofs and exact classical computations on the
assembled operators only: norms, gaps, kernel dimensions, field weights, and α/‖·‖ of built
encodings. Every filter degree, preparation, gate count and tier-labelled number lives in Chapter 8.
A formulation chapter derives its law through `eq:degree` and names the results section that measures
it.

### F2. The paper's defects argued three times; Chapter 4 interrupted — *applied*

§3.5 names each defect; §4.3 restated the paper's choices and argued them again; Table T10 restated
every row on a full `\scriptsize` page; Appendix K evidences them. §4.3 is about accuracy inside a
chapter whose question is cost. **Fix:** Chapter 4 states each data choice of the standard form
once, with a one-clause reason and a pointer; the arguments (the Laplace mode family, the
associated Legendre branch point, the backward heat problem, the misprinted Laplace solution, the
rounded points' error floors) move to Appendix K; T10 becomes a compact table. Plan T-30 and T-34 are
amended accordingly.

### F3. Chapter 7 at twice its budget, where momentum stalls — *applied*

After Chapter 6 answers Q(iii) the reader crossed 11 pages of machinery before any evidence. Keep the
position; cut to about 6 pp: the imaginary-time paragraph and `prop:filter-normalisation` to Appendix
F; `tab:verification-modes` and the trust threshold's rationale to Appendix I; Wedin against
Davis–Kahan stated once; the error budget to its equation; GQSP phase detail to Appendix F; one of
`tab:constraint-kinds` and the definition's prose list.

### F4. Chapter 2 is the largest unfinished risk — *applied (first pass; over budget)*

Intro & Lit /20, with only Chapter 3 currently assessing critically. Unwritten: the four literature
strands, the comparison table, the ultraspherical and first-order-system least-squares subsections
(the antecedent credit the headline's novelty rests on). The drafted QC preliminaries are about 3 pp
of definition boxes against a 1.5 pp cap, and `2_literature.tex:50` says a qubit can "encode both 0
and 1 simultaneously", a misstatement a physics marker will penalise (also the Feynman-diagram
analogy, `:112`). Cut the preliminaries to ≤ 1 pp of prose; merge §§2.4–2.7 into one section of about
2 pp around `eq:degree`.

### F5. Q(iii) only loosely belongs to the spine — *applied*

`3_pihm.tex:224` says one question lies beneath all three (where the norm comes from), but Q(iii)
(`:222`) asks preparation against projection. Give Q(iii) a second half, "…and does the
reformulation's advantage survive there?", which §6.8 already answers. Edits: Chapter 3's item and
closing line, Chapter 6's opening, §8.4's opening, plan §3.2, later §1.3.

### F6. Chapter 8: answers sooner, numbers in tables — *open*

§8.1 is 2.5 pp before any question is answered: keep it first, at about 1 pp, with answer
independence and the filter study to appendices in a sentence each. Number-dense paragraphs to
tables (§8.3's gaps and field weights; §§8.4–8.5's lift errors; the Burgers paragraph carries about
15 keyed numbers). Drop the R3a bullet of "Three problems in both forms", which repeats §8.2's
reversals. Export the real figures before cutting: the 7 placeholders and the `\prov` numbers set
the chapter's true length.

### F7. Benchmarks used 30 pages before their table — *applied*

Move `tab:ladder` to §4.1 beside the running example; define "trusted" in two sentences at §4.4,
where the reference first appears.

### F8. The endgame without four statements of each finding — *open*

The spine sentence: four placements (Abstract, §1.3, §5.1, §10.1), not seven. "Neither form is
poly-log" and the Lin–Tong hedge: once in the formulation (§5.9), interpreted in §9.2 only. Roles:
§8.6 the findings with one number each; Chapter 9 mechanism and consequence, no new numbers except
T9; Chapter 10 a verdict per contribution. Chapter 9 at 3 pp, §9.4 folded into §9.2.

### Smaller items

- §5.7's line-by-line commentary on the algorithm, the Haar-success paragraph and the rescaling
  constants' `\prov` paragraph to Appendix G (applied with F1).
- The `\todo` to prove the gap flat (`5_descriptor.tex:156`): drop the attempt; the claim is stated as
  measured.
- Remove the `\newpage \todo` spacers in `main.tex` before measuring pages.

## 4. Order of work

1. Reallocation pass: F1 + F2 + F3 (*done*), then F7 and F5's rewording.
2. Write Chapter 2 (F4).
3. Export the Chapter 8 figures, resolve its `\prov` keys, then F6.
4. Chapters 9 and 10, then Chapter 1 and the Abstract (F8).
5. Measure; Review Mode per chapter against the new budget.
6. Line-edit for density: one claim per sentence, numbers to tables, for physicists who are not
   specialists.

## Three highest-impact fixes

1. F1 + F2 + F3 as one pass: the page-cap penalty and the results-before-method order (Model
   Formulation /30, Results & Discussion /30).
2. F4: Chapter 2 at register, with the antecedents (Intro & Lit /20).
3. F5: Q(iii) tied to the spine (coherence; Conclusions /10's "relate back to the original goal").
