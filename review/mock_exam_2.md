# Mock examination 2: external examiner's report

**Thesis:** *Physics-Informed Quantum Hamiltonians for Solving ODEs, PDEs and Navier–Stokes* (`1_header/1_title.tex:14`). Scratch build of 2026-10-16 from the current sources: 151 pp, body pp. 1–60, references from p. 61.
**Examiner stance:** a PRA referee who is also marking against the UWA *Master of Physics Thesis Mark Sheet* (`../Theses-AssessmentRubric.pdf`), Modelling scale, with the *Master Thesis Guidelines* (`../marking_guide.pdf`) as the formal requirements. Prose, register and layout **are** assessed this time; the first mock exam (`review/mock_exam.md`) ignored them.
**Read:** `ThesisPlanning.md` v3.17 (§§0–4 in full, the rest as needed), `thesis_guides/STRUCTURE_AND_RUBRIC.md`, the mark sheet, the guidelines, every chapter, Appendices D, H and J in full, and the structure and key passages of the other appendices. Figures, tables and resolved numbers were taken from the PDF.
**Anchors:** `file:line` in the `.tex` sources (each paragraph is one source line). The `cleaned/` copy is a comment-stripped mirror and is not cited.

---

## 0. Formal requirements and what changed since the first mock exam

| Requirement (guidelines) | Status | Consequence |
|---|---|---|
| Body ≤ 60 pp, 12 pt | Body is pp. 1–60: **exactly at the cap, with no slack** | Every fix below that adds text needs an offsetting cut. Chapter 9 runs about 7 pp against a budget of 3 and is the place to cut (§2, note after item 10). |
| One-page Summary of Student Achievement, first person | Present, one page (p. iii) | Satisfied. Tone and slips: "didn't", "python", "(almost) any differential equation we claim to be able to solve", "The paper was less substantial than I had first thought" (`4_StudentAchievement.tex:23,27`). The last phrase reads as a judgement of the authors rather than the paper. A reader who knows Kyriienko's group will notice it. |
| Proposal as appendix, deviations explained | App. K, Table K.1; `1_introduction.tex:127` | Satisfied, and well argued. |
| Declaration, supervisor endorsement | Both signatures are images dated `\today` (`3_declaration.tex:19,33`) | Confirm the supervisor's signature is her endorsement of *this* copy. |
| "Areas where help has been received should be identified and acknowledged" | The Acknowledgements name the supervisor and Pawsey only | If generative-AI tools were used to draft or edit, check the School's current policy on declaring them. This is a formal-compliance risk, not a marking one. |

**Status of the first mock exam's ten weaknesses.**

| # (first exam) | Item | Now |
|---|---|---|
| 1 | Summary of Student Achievement blank | **Fixed** |
| 2 | Diagonal preconditioning dismissed | **Partly addressed**, and now **escalated to item 1**. `10_conclusions.tex:103` poses the structured-diagonal question as open, but `5_descriptor.tex:172` is unchanged, and a 30-line classical check answers the question (§2, item 1). |
| 3 | Appendix J empty | **Fixed** (`J_software.tex:31-61`). Two `\todo` margin notes remain (tag/hash/DOI; where the records are deposited). |
| 4 | Two-point slopes; computed vs measured | **Open** (`8_results.tex:148,164`) |
| 5 | Edge-robustness evidence | **Text improved** (`9_discussion.tex:93`); evidence unchanged (`H_catalogue.tex:289`) |
| 6 | Positioning against linear-systems solvers | **Partly addressed**: parity is stated at `9_discussion.tex:34`, but Table 2.1 still has no row for this thesis |
| 7 | Two-axis verdict on two resolutions | **Partly addressed**: the caveat is now attached at `9_discussion.tex:42` |
| 8 | Empty appendix headings | **Fixed** |
| 9 | Increment list dilutes the claim | **Open** (`2_literature.tex:191`): it still omits Theorem 2 |
| 10 | Navier–Stokes wording; Reynolds number | **Open, and worse**: the title now promises "Solving … Navier–Stokes"; "Reynolds" appears nowhere in the sources |

**New since the first exam:** 28 result keys render as the word "unknown" in the PDF, four of them in the body (§2, item 2).

---

## 1. Score estimate by criterion

| Criterion | Max | Estimate | Band (mark-sheet range) |
|---|---:|---:|---|
| Introduction & Literature Review | 20 | **16.5** | 3 (15.0–17.9) |
| Project Body – Model Formulation | 30 | **25.5** | 3 (22–26.9) |
| Project Body – Results & Discussion | 30 | **25.0** | 3 (22–26.9) |
| Conclusions & Topics for Further Investigation | 10 | **9.0** | 4 (9.0+), at its floor |
| Style & Presentation | 10 | **7.0** | 2 (6.0–7.9) |
| **Written thesis** | **100** | **≈ 83** | |

The first exam gave ≈ 84.5 with prose excluded. The net change comes from three sources: Appendix J and the Summary were fixed (+); the introduction rewrite lost its connective argument and the body now shows "unknown" placeholders (−); and prose is now assessed (−). After the "under two hours" fixes of §2, a realistic estimate is 17.5 / 26.5 / 26.5 / 9.3 / 8.5, **≈ 88**. Band 4 in both Project Body criteria ("warranting publication") is then blocked mainly by item 1, which needs a measurement to close.

### 1.1 Introduction & Literature Review: 16.5 / 20 (band 3)

Band 3 is "Comprehensive understanding of historical background and state of the art, and a good attempt to relate this to the project and its goals". Band 4 is "Comprehensive, superior understanding … with excellent connection of the current field to the project". The sheet adds: "A critical assessment of the strengths and weaknesses of the material reviewed is required for a high distinction".

The critical-assessment gate is met convincingly:

- Each route in §2.2 closes on its strength and its weakness (`2_literature.tex:100,110,120,130`), and §2.2.5 synthesises them (`:140`).
- §3.5 judges Wu et al. under Strengths, Weaknesses in the cost, evidence and scope, and Open problems, then converts their open problems into Q(i)–(iii) (`3_pihm.tex:211-224`).
- The historical lines are present: HHL → Berry → Childs–Liu → Costa; Leyton–Osborne → Carleman → Liu → Krovi; tau/collocation → Olver–Townsend → FOSLS.

Four things keep it below 18:

1. **The introduction no longer carries the argument.** It is 1.3 pp against a planned 3. It states no headline number, never mentions the gap erosion, block rescaling or the flat-gap theorem, and does not pose the three questions (`1_introduction.tex:119-127`). A marker reads the introduction for "relevance of your project" and finds a list of things done.
2. **Table 2.1 has no row for this thesis** (`2_literature.tex:73-91`). Parity with the first-order linear-systems route is stated only in the Discussion (`9_discussion.tex:34`). That is exactly where a marker looks for "connection of the current field to the project".
3. **Two literature gaps that an examiner in the area will notice.**
   - *Spectral integration / integration preconditioning:* Greengard, SIAM J. Numer. Anal. 28 (1991); Coutsias, Hagstrom & Torres, Math. Comp. 65 (1996). This is the classical answer to the very conditioning problem the thesis is about, and it bears directly on item 1.
   - *Ground-state preparation beyond Lin–Tong:* Ge, Tura & Cirac, J. Math. Phys. 60 (2019); Dong, Lin & Tong, PRX Quantum 3 (2022). The thesis's method is a ground-state route, so these matter.
   - Check every field against the publisher before adding.
4. **Small accuracy slips in the introduction.** "an exact structured encoding whose cost is constant for constant coefficients" (`1_introduction.tex:121`): it is the looseness α/‖G‖ that is bounded; the gates grow as O(n²). "Cost is primarily determined by … and/or shots" (`:66`) is vague. "Readout is a research field of its own … Therefore we decode the field classically" (`:125`) gives no reason a referee would accept.

**Single change most likely to raise it a band:** add to Table 2.1 a row for this thesis's route, and one sentence at `2_literature.tex:140`.
- The row: descriptor ground state; assumes a regular problem and a known edge; queries Θ̃(N) on a regular problem, at least Θ̃(N²) on singular and two-axis problems; returns the solution as a ground state; fails on two axes and at a double zero.
- The sentence: the descriptor brings the physics-informed route to the conditioning a first-order linear-systems discretisation already pays (parity, not advantage), and states what it trades for that (no inverse, a residual whose kernel is the solution).

This is the literal "excellent connection" the band-4 wording asks for. Do it together with item 1's rescoping, so the row does not claim Θ̃(N) as a floor.

### 1.2 Model Formulation: 25.5 / 30 (band 3)

Band 3 is "Good model capable of yielding valid results but the description lacking in some respect e.g. minor omissions in description, poor design of numerical experiment". Band 4 is "Superlative model … providing a significant advance in the state of the art or warranting publication". The mark sheet's three named requirements are now all met:
- software: §7.8 and App. J;
- a configuration diagram: Fig. 7.1;
- input options: Tables H.3–H.4.

The model itself is of publishable quality:
- the standard form stated once with its departures (Def. 2, Table 4.2);
- the exact factorisation of G (Prop. 1, Fig. 4.1);
- the floor for every encoding (`4_standard.tex:443-456`);
- kernel equivalence (Thm 1);
- **Theorem 2, whose compactness proof holds up line by line** (`D_descriptor.tex:231-252`);
- the LCU cost with a scoped optimality claim (`5_descriptor.tex:237-249`);
- the stacked reflection (Prop. 5).

Two things keep it in band 3:

1. **The descriptor's Θ̃(N) is presented as the descriptor's law, but it is the law of the *unpreconditioned* descriptor.** A one-parameter diagonal weighting of the recurrence rows leaves the kernel and the state unchanged. On R2a it lowers the effective condition number's exponent from 1.0 to about 0.3 (§2, item 1). The formulation never considers row weighting. Its dismissal of per-amplitude weighting, at Θ(dim w) gates (`5_descriptor.tex:172`), is about a column (state) scaling of an unstructured diagonal, which is a different object.
2. **Design of the numerical experiment ("poor design of numerical experiment" is band 3's named failure).**
   - The standard-form side of every headline comparison is a resource estimate. Exact emulation of the standard form stops at n = 3 on R2a and never runs on R2b or R2c (Table H.5, `H_catalogue.tex:153`), although R2b at n = 4 (degree ≈ 7 × 10⁵) lies inside the emulation's 2²⁰.
   - The only test of the edge assumption is one imaginary-time, standard-form, n = 3 study of underestimates (`H_catalogue.tex:289`).

**Single change most likely to raise it a band:** item 1's text fix, rescoping every "Θ̃(N)" as the unpreconditioned descriptor's and stating that a left diagonal on the recurrence rows lowers it further. Ideally also the measurement as a `pihm` key; that needs new results.

### 1.3 Results & Discussion: 25.0 / 30 (band 3)

Band 3 is "Clear description of the results with discussion of most of the implications of the work". Band 4 is "Complete, clearly presented results, with detailed discussion showing insight into the significance of the work or warranting publication". The sheet also requires results "presented in a way that is easy to understand, without reference to any other documents".

The insight is band-4 material:
- Table 8.1 and Fig. 8.1 separate the encoder's cost from the Hamiltonian's.
- The reversals are reported as findings (`8_results.tex:187`).
- The negatives are numbered (`8_results.tex:311-317`).
- §9.1 ties Theorem 2 to FOSLS coercivity (`9_discussion.tex:27`).
- §9.2 reads the degree as the residual's condition number, in the linear-systems law's form (`9_discussion.tex:34`).
- Table 9.1 is a practitioner's map.
- §9.5 gives the limitations in the author's voice.

What stops "complete":

1. **Results missing from the page.**
   - "the share unknown of α_R" (`8_results.tex:160`); "γ² ranges from unknown to unknown" (`:262`); "between unknown and unknown … at most unknown round" (`:289`).
   - Table D.3 is unknown in every cell (`D_descriptor.tex:179-182`), yet §9.1 and §10.2 cite it as a measurement (`9_discussion.tex:27`, `10_conclusions.tex:101`).
   - The log reports 28 keys as unknown, several "no campaign has …".
2. **Computed more than measured.** The exponents are two-point slopes (`8_results.tex:148,164`; `7_pipeline.tex:281`), though Fig. 8.1 has seven resolutions. The standard form's degrees beyond n = 3–5 are Eq. (7.6) applied to an exact spectrum, which is exact but is not an observation of preparation.
3. **The significance verdict rests on the least-settled data**, two resolutions per axis (`9_discussion.tex:42`). It is now flagged as such, which helps.

**Single change most likely to raise it a band:** make every result in the body render.
- Rerun the exporter (`pihm/tools/thesis/export_numbers.py --used-only`) for the overlap and α-split keys.
- Either produce the `trace-weights` records or delete Table D.3 and the two sentences that cite it.
- Then replace the two-point slopes in Table 8.2 and H.7 by least-squares exponents over every trusted resolution, with spread. That is a derived key over existing records.

### 1.4 Conclusions & Further Investigation: 9.0 / 10 (band 4, floor)

Band 4 is "Detailed, comprehensive and insightful conclusions and significant suggestions for further investigation"; the conclusions must be "supported by the results and discussion and relate back to the original goal".

§10.1 answers Q(i)–(iii) in order, in words, with no new results (`10_conclusions.tex:87-95`). It ends on a transferable lesson: the encoder/Hamiltonian audit, and the reading of the degree as conditioning. §10.2's items are concrete and falsifiable:
- datum rows on derivative blocks tested on R5a at 3–5 qubits per axis (`:101`);
- a derived ζ tested on a dipping coefficient (`:103`);
- a quantitative flat-gap bound checked on R1/R2, and an order-to-order divergence test on R9 (`:105`);
- a noisy-observation study (`:107`).

Two risks:
- `:101` and `:103` treat as open a question a referee can settle in twenty minutes (item 1). That makes the further-work list look less significant than it is.
- `:91` repeats "from Burgers' equation to two-dimensional incompressible Navier–Stokes in exact emulation and resource estimate" without its regime.

**Single change most likely to raise it:** lead §10.2 with the row-preconditioned descriptor as the first test, with a decision criterion. For example: "if σ_max/σ₁ of the row-weighted residual grows more slowly than N on R2a–R2c and R4b–d, the descriptor's Θ̃(N) is not the floor for a banded residual on regular problems". Note that this *strengthens* §10.1's thesis statement that the formulation fixes the exponent.

### 1.5 Style & Presentation: 7.0 / 10 (band 2)

The sheet's wording: "grammar and spelling, presentation of figures and tables and general expression and layout"; band 3 is "Few insignificant errors" (8.0–9.9) and band 2 "Significant errors" (6.0–7.9). The guidelines add "readily understandable to a competent physicist not only to a narrow specialist" and "Considerable emphasis is placed on concise presentation".

The figures and tables are journal quality, with self-contained, claim-first captions. What a marker will count against it:

- **Visible "unknown" placeholders** in the body and in App. D (item 2).
- **Two yellow `\todo` margin notes** in App. J (`J_software.tex:31`).
- **The title** (`1_title.tex:14`): "Solving" contradicts the thesis's own vocabulary (prepared, never solved; nothing on hardware). It names Navier–Stokes, the least-supported result, and omits the descriptor, the headline.
- **The abstract** is about 650 words, against the plan's 250–300. One sentence groups Legendre's equation (one axis) under "On two axes" (`5_abstract.tex:21`). It uses "the published encoding" (`:19`), against plan §3.4.
- **The bibliography is a numbered chapter**, "11 References" (`main.tex:95`). "Acknowledgments" is the US spelling (`main.tex:17`); Australian is "Acknowledgements". "unadressed" (`2_literature.tex:282`).
- **84 overfull `\hbox` warnings** in the build, including the Acknowledgements and the Summary.
- **Density.** Most body paragraphs are a single sentence chain of 150–250 words with several embedded clauses and two or three `\Cref`s. That is precise, but a non-specialist marker will tire. The guidelines name exactly this reader.

**Single change most likely to raise it a band:** item 2 (no placeholder renders), plus the ten-minute items above: title, abstract length, numbered References, spelling, typo, the `\todo`s, and the front-matter overfull boxes.

---

## 2. The ten weaknesses most likely to cost marks

Ranked by marks at stake. "Cheapest fix" fits in under two hours unless marked **not before submission**. The body is exactly 60 pp, so every addition needs an offsetting cut (see the note after item 10).

### 1. Θ̃(N) is not the floor for a banded residual: a diagonal row weighting lowers it, and the thesis never considers one

- **Where:**
  - `2_literature.tex:173` (Olver–Townsend bounded "after a diagonal preconditioner"; "block rescaling takes the place of the preconditioner") and `:175` ("would match the descriptor's degree").
  - `5_descriptor.tex:58` (the ultraspherical reduction is not built "because its conversions weight the rows"), `:172` (per-amplitude equilibration at Θ(dim w) gates) and `:196` (block rescaling as "the counterpart" of the diagonal preconditioner).
  - `9_discussion.tex:27,34,95`; `10_conclusions.tex:101,103`.
- **Why a referee objects:**
  - The thesis cites a bounded preconditioned condition number for the ultraspherical operator, then claims Θ̃(N) for the descriptor built from the same factors. It never tries the obvious step: weighting the recurrence rows on the left.
  - A left diagonal changes neither the kernel nor the prepared state, so the readout and overlap objections do not apply.
  - The reason given for not building the ultraspherical reduction (row weighting) is one the mass form already accepts, `5_descriptor.tex:135`.
  - **Examiner's scratch check** (numpy, `review/` snippet below; not a `pihm` record and **not to be quoted in the thesis**): R2a's descriptor at ζ = 4 reproduces Table 8.1 exactly (Δ = 2.87, ‖H‖ = 4.2 × 10⁶ at n = 8). Multiplying each recurrence row p by (2(p+1))^(−s) gives:

    | Row weight on the recurrence rows | σ_max/σ₁ at n = 5, 7, 9 | Exponent of N, n = 7→9 |
    |---|---|---:|
    | none (the thesis's residual) | 146, 599, 2410 | 1.00 |
    | (2p)^(−1/2) | 37.6, 78.8, 173 | 0.57 |
    | (2p)^(−3/4) | 59.1, 87.2, 134 | 0.31 |
    | (2p)^(−1) (turns P·D̃ into a unit shift: spectral integration) | 118, 237, 542 | 0.60 |

    At n = 9 the ideal-bound degree would fall by about 18×, and its growth from ≈ N to ≈ N^0.3. This is one problem with a hand-picked s and no circuit: the diagonal (2p)^(−s) needs its own block encoding, by index arithmetic and a controlled rotation, poly(n) gates, not built. But it is enough for an examiner to say the headline exponent is an artefact of not preconditioning.
- **Cheapest fix (≈ 1.5 h, text only):**
  - Rescope Θ̃(N) everywhere as the unpreconditioned descriptor's (`5_descriptor.tex:258-267`, Table 5.1, `9_discussion.tex:34`, Table 9.1, the Abstract).
  - Narrow `5_descriptor.tex:172` to column scaling by an unstructured diagonal.
  - Add one paragraph to §5.4 or §9.5: a left diagonal on the recurrence rows preserves the kernel and the state; Olver–Townsend's and Greengard's results suggest it can bound the conditioning; it was not built.
  - Correct `2_literature.tex:175` and `9_discussion.tex:95`: with the preconditioner, the expectation is better than the descriptor's degree, not equal to it.
  - Make the row-weighted descriptor the first item of §10.2.
  - Frame it as support for the central claim (the formulation fixes the exponent), not as a retraction.
- **Not before submission:** the measurement as a `pihm` key (σ_max/σ₁ of the row-weighted residual on R2a–R2c, R3a, R4a, R5a, n = 3–10). It is a build-stage classical computation, so if `pihm` can add it in a day it would turn this weakness into a result.

### 2. Results render as "unknown" in the body and in Appendix D

- **Where:**
  - `8_results.tex:160` (`alpha-split/R2c/descriptor/n8`), `:262` (`overlap/carleman/T2`), `:289` (`overlap/R10/T3`, three metrics).
  - Table D.3 (`D_descriptor.tex:168-182`, `trace-weights/*`, 20 cells, "no campaign has …"), cited as a measurement at `9_discussion.tex:27` and `10_conclusions.tex:101`.
  - The build log: "Quoted numbers not current: 28 unknown".
- **Why an examiner objects:** results must be presented "without reference to any other documents"; a printed "unknown" is a missing result. The slice-row finding is used to close an argument in two chapters with no data behind it on the page.
- **Cheapest fix (≈ 30 min plus the exporter run):**
  - Rerun the exporter for the overlap and α-split keys.
  - If the `trace-weights` probe was never a campaign, delete Table D.3, the paragraph at `D_descriptor.tex:168`, the sentences at `9_discussion.tex:27` from "The remedy it points to was measured" to "missing coercivity", and the corresponding clause at `10_conclusions.tex:101`. Or run the campaign (**not before submission** if it needs Setonix).

### 3. The cost results are computed more than measured, and the experiment that would corroborate them is thinner than it could be

- **Where:**
  - two-point slopes: `8_results.tex:148`, Table 8.2 caption `:164`, `7_pipeline.tex:281`, Table H.7;
  - standard-form T2 coverage: Table H.5 (`H_catalogue.tex:153`): R2a n = 3 only, R2b and R2c none;
  - the caption that admits it: `8_results.tex:156`.
- **Why an examiner objects:**
  - Every standard-form degree in the headline is Eq. (7.6) on an exact spectrum. That is exact, but it is not an observation that the filter prepares the state.
  - R2a at n = 4 (degree ≈ 1.5 × 10⁵) and R2b at n = 4 (≈ 7 × 10⁵) lie within the 2²⁰ that T2 reaches, yet were not emulated.
  - Fig. 8.1 has seven resolutions, but the exponents use two.
- **Cheapest fix:**
  - (a) 20 min, text: open §8.2 with one paragraph separating three things. What is exact computation: norms, gaps and α of built circuits. What is derived: degrees from Eq. (7.6). What is tested: 321 trusted T2 preparations reach ε at the derived degree, and T1 = T2 on all 50 minimax circuit simulations.
  - (b) 1–2 h: least-squares exponents over every trusted resolution, with spread, as a derived key over existing records.
  - **Not before submission:** T2 of the standard form on R2a and R2b at n = 4. These are cheap runs, but they are new results.

### 4. The introduction no longer makes the case for the thesis

- **Where:** `1_introduction.tex:66-127`. There are no headline numbers, no gap erosion, rescaling or Theorem 2, and the three questions are not stated. Also `:121` ("cost is constant"), `:125` (readout) and `:66` ("and/or shots").
- **Why an examiner objects:** the mark sheet's opening sentence requires the introduction to show "the relevance of your project". The exemplars in `STRUCTURE_AND_RUBRIC.md` §4.2 put the numbers in the first pages. As written, a marker reaches Chapter 5 before learning what the descriptor achieves or what it costs.
- **Cheapest fix (≈ 1 h, about +0.4 pp):** one paragraph after `:68`. It should cover Wu et al.'s two open problems; the answer as a number by key (degree on R2a at n = 8 for the standard form, structured and ideal, against the descriptor's); the price (the gap, rescaling, two axes); and the three questions in one sentence. Then fix `:121` to "whose subnormalisation stays within a constant factor of ‖G‖".

### 5. The positioning against the established quantum ODE route is still qualitative in the literature review

- **Where:** Table 2.1 (`2_literature.tex:73-91`), `:140`; the parity statement is buried at `9_discussion.tex:34`.
- **Why an examiner objects:** "excellent connection of the current field to the project" (Intro & Lit band 4) and "consequences of them for the field" (R&D). A reader of Table 2.1 cannot tell whether the reformulated route is better than, equal to or worse than Childs–Liu with Costa et al. on the same discretisation.
- **Cheapest fix (≈ 45 min):** the row and sentence of §1.1, scoped by item 1.

### 6. The spectral edge and the overlap come from the classical answer, and the robustness evidence is one narrow study

- **Where:** `7_pipeline.tex:209` (edge from the reference), `:233` (γ from the reference); `8_results.tex:100`; `H_catalogue.tex:289` (imaginary time, standard form, R2a, n = 3, underestimates only); `9_discussion.tex:93`.
- **Why an examiner objects:**
  - The minimax filter on the descriptor, the configuration every headline uses, is never tested with a wrong edge.
  - The dangerous direction, an *over*estimated gap that silently misses ε, is not stated anywhere.
  - Ground-energy estimation, which would supply the bound, is not cited beyond Lin–Tong.
- **Cheapest fix (≈ 45 min, text):**
  - State the asymmetric risk.
  - Note that `9_discussion.tex:93` already gives the scaling argument (Δ_lb = cΔ keeps every law); add that Theorem 2 supplies the order but not c.
  - Cite Ge–Tura–Cirac and Dong–Lin–Tong for the bound, and say its cost is excluded.
- **Not before submission:** a minimax, descriptor edge-mis-estimate sweep (×½, ×2) on R2a and R3a.

### 7. The title and the Navier–Stokes framing over-reach

- **Where:** `1_title.tex:14`; `5_abstract.tex:23`; `10_conclusions.tex:91`; the regime at `6_extensions.tex:181` (ν = 1, ≤ 48 modes, a/ν ≤ 30). The truncation alone errs by order one at a/ν = 30 (`8_results.tex:285`). The Reynolds number is never stated.
- **Why an examiner objects:** "Solving … Navier–Stokes" will be read by a fluids-literate examiner as a fluid simulation. What the thesis shows is a low-Reynolds, 12–48-mode Galerkin system prepared by exact emulation, with no circuit simulated. The title also omits the headline contribution.
- **Cheapest fix (≈ 20 min):**
  - Retitle to name what is shown, e.g. "A Banded Descriptor Form for Physics-Informed Quantum Hamiltonians: Conditioning, Verified Preparation and Nonlinear Extension". This is your call; plan §13.1 lists options.
  - Add one clause in §6.7 giving the Reynolds number, of order a/ν on the 2π box, and calling R10 a low-Reynolds test of the pipeline.
  - "prepared by exact emulation on 12–48 modes and costed by resource estimate" in the Abstract and §10.1.

### 8. Presentation defects that cost cheap marks

- **Where:**
  - the `\todo` margin notes (`J_software.tex:31`);
  - "11 References" (`main.tex:95`: use `\section*`);
  - "Acknowledgments" (`main.tex:17`);
  - "unadressed" (`2_literature.tex:282`);
  - "didn't", "python" (`4_StudentAchievement.tex:23,27`);
  - "the published encoding" (`5_abstract.tex:19`);
  - the Legendre/two-axes sentence (`5_abstract.tex:21`);
  - an abstract of about 650 words;
  - 84 overfull `\hbox`;
  - the singular-value index clash in Theorem 2's proof, where σ₁, σ₂ and Δ = σ₂² − σ₁² stand against the notation table's σ₀, σ₁ (`D_descriptor.tex:239-249`).
- **Why an examiner objects:** "Flawless" is the only route to 10; each of these is visible on a first read.
- **Cheapest fix (≈ 1.5 h):** the mechanical items directly (on your instruction); then cut the abstract to its five moves, each with one number.

### 9. The increment list omits the strongest result and leads with the weakest

- **Where:** `2_literature.tex:191` ("What we add": kernel equivalence first; Theorem 2 absent); `1_introduction.tex:119` (no gap result); `8_results.tex:315` (finding 5).
- **Why an examiner objects:** Theorem 1 follows in two lines from B̃ being invertible, and "a trusted kernel does not certify a converged lift" is predicted in §6.5 from IVP uniqueness (`6_extensions.tex:132`). Leading with these and omitting Theorem 2 hands the examiner the "this is just ultraspherical + FOSLS" line (Q1) and undersells the proof that answers it.
- **Cheapest fix (≈ 30 min):** reorder the increment.
  - Lead with Theorem 2: discrete coercivity of the block-encoded residual on regular problems, proved.
  - Then the gap-erosion mechanism with its cure and limits, the encoder/Hamiltonian separation with a floor for every encoding, and the measured costs.
  - Present Theorem 1 as the enabling lemma.

### 10. Reproducibility rests on records that are not deposited

- **Where:** `J_software.tex:31` ("The production's records themselves are not under version control", and the DOI `\todo`); `7_pipeline.tex:290` ("every number and figure is regenerated from the archived records by one command").
- **Why an examiner objects:** a PRA referee would ask for a data-availability statement. The claim cannot be checked if the records are nowhere public.
- **Cheapest fix (≈ 1 h):** mint a Zenodo DOI for the `results-v1` tag together with a records archive, if the size allows, and cite both. Otherwise soften `7_pipeline.tex:290` to "regenerated by one command from the records, available from the author".

**Page budget for these fixes.** Items 1, 4, 5 and 6 add about 1 pp. Chapter 9 is about 7 pp against a budget of 3, and the cheapest cuts that lose no claim are:
1. The filter paragraph at `9_discussion.tex:40` (≈ 0.45 pp). It restates §8.1, and only its last two sentences are new.
2. The resolution paragraph's first half at `9_discussion.tex:42` (≈ 0.25 pp). It repeats `8_results.tex:92,98` number for number.
3. The third paragraph of §9.4 (`9_discussion.tex:86`, ≈ 0.3 pp). It repeats §8.1's T1 budget numbers; keep its last sentence.

---

## 3. Fifteen questions an examiner is likely to ask

"Adequate" means a marker reading only the thesis would accept the answer. A two-sentence model answer is given where it is not.

**Q1 (hostile). Is the descriptor reformulation just the ultraspherical method plus FOSLS?**
*Answered:* `2_literature.tex:173,189,191`; `5_descriptor.tex:58,60`; App. A.5 (`A_chebyshev.tex:135`); `9_discussion.tex:27`.
*Adequate?* **Partly.** The credit is exact (B̃ and D̃ are twice Olver–Townsend's S₀ and D₀, at the level of matrix entries). The increment is undersold: Theorem 2 is missing from "What we add" (item 9).
*Model answer:* "Algebraically, yes, and the thesis says so; neither antecedent concerns a block-encoded residual whose cost is paid in filter queries. What is new is Theorem 2, a discrete coercivity that makes the gap N-independent on regular problems, together with the mechanism by which the gap fails on singular and two-axis problems, its cure on one axis and the measured end-to-end costs."

**Q2 (hostile). Does anything here beat a classical solver?**
*Answered:* `1_introduction.tex:125`; `2_literature.tex:140`; `9_discussion.tex:42`; `10_conclusions.tex:95`.
*Adequate?* **Yes.** No advantage is claimed, and the reasons are given: O(N) classical work on one axis, N estimates to read the field, and log(1/δ) resolution for analytic solutions. Expect the follow-up "then why does it matter?"; the answer is `10_conclusions.tex:93` (formulation fixes conditioning; the encoder/Hamiltonian audit transfers).

**Q3 (hostile). Why should we trust exact emulation (T2)?**
*Answered:* `7_pipeline.tex:248-250`; `8_results.tex:94,96`; `9_discussion.tex:86,91`; App. F.
*Adequate?* **Mostly.** The argument is sound. The post-selected output is Σ q_k T_k(H′)ψ, which depends on the circuit only through ΠVΠ = H′. It is confirmed T1 = T2 to within 10⁻¹⁰ on all 50 minimax simulations, the worst being 1.9 × 10⁻¹². The gap is scope: 57 wider reflections are built but not verified (`8_results.tex:94`), including every two-axis descriptor reflection and the Navier–Stokes ones.
*Model answer for the gap:* "T2 is computed from the residual assembled from the problem, independently of the compiler, so it is the output of the intended operator; it is the circuit's output wherever ΠVΠ = H′ is verified, exactly to 25 qubits, by probe to 24, and term by term at any size. For the 57 unverified reflections I report T2 as the emulation of the target operator, and the compiler's correctness there rests on the IR check and the same code path verified at smaller widths."

**Q4 (hostile). What happens without the known spectral edge?**
*Answered:* `7_pipeline.tex:209`; `8_results.tex:100`; `H_catalogue.tex:289`; `9_discussion.tex:93`; `10_conclusions.tex:105`.
*Adequate?* **Partly.** The scaling argument is now in the text. The evidence is one imaginary-time, standard-form, n = 3 study of underestimates, and the over-estimate risk is never stated (item 6).
*Model answer:* "The degree needs only a lower bound Δ_lb ≤ Δ and grows as √(Δ/Δ_lb), so every law survives a bound of the right order in N, which Theorem 2 guarantees on regular problems without its constant. Overestimating the gap is the real danger because it silently misses ε, so in practice the bound would come from ground-energy estimation (Lin–Tong; Dong–Lin–Tong), whose cost I have not included."

**Q5 (hostile). Olver and Townsend precondition with a diagonal and get bounded conditioning. Why didn't you weight the recurrence rows, which changes neither the kernel nor the state?**
*Answered:* `2_literature.tex:173,175`; `5_descriptor.tex:58,172,196`; `9_discussion.tex:95`; `10_conclusions.tex:103`.
*Adequate?* **No** (item 1). The thesis treats the structured diagonal as open, but a scratch check shows it lowers R2a's exponent from 1.0 to about 0.3.
*Model answer:* "That is the natural next reformulation, and it fits the thesis's main claim that the formulation, not the circuit, fixes the exponent: a left diagonal keeps the kernel and the state, and a quick classical check on R2a lowers the growth of σ_max/σ₁ well below N. I did not build it because the diagonal (2p)^(−s) needs its own block encoding, by index arithmetic and a controlled rotation, and its effect on singular and two-axis problems is unmeasured; it is the first item of further work."

**Q6. Your exponents are two-point slopes and the standard form's degrees are mostly estimates. Why was the standard form emulated only to n = 3 on R2a, when n = 4 lies inside 2²⁰?**
*Answered:* `8_results.tex:148,156,164`; `7_pipeline.tex:281`; Table H.5 (`H_catalogue.tex:153`).
*Adequate?* **No** (item 3).
*Model answer:* "The degree is a deterministic function of the exact spectrum and the circuit's α_R, and T2 confirms at every resolution emulated that the preparation reaches ε at that degree, so the estimates are exact predictions, not extrapolations. Fitted over every trusted resolution the one-axis exponents are … ± … [the derived key], and emulating R2a and R2b at n = 4 in the standard form is a cheap confirmation I should have run."

**Q7 (hostile). Why benchmark against Wu et al. rather than the established linear-systems ODE solvers on the same discretisation?**
*Answered:* `9_discussion.tex:34`; `2_literature.tex:100,140`; Table 2.1.
*Adequate?* **Partly** (item 5). The parity statement exists but is buried.
*Model answer:* "Because the question is what the ground-state route costs and where. On a regular problem the descriptor brings it to the conditioning a first-order linear-systems discretisation already pays, parity rather than advantage, and it avoids an inverse at the price of an initial state with overlap γ; the comparison with Wu et al. isolates the cost of eliminating derivatives, which linear-systems solvers avoid by reducing the order first."

**Q8. The exact constraint points and the heat data come from the reference solution. Isn't the benchmark answer-dependent?**
*Answered:* `4_standard.tex:215,224`; `7_pipeline.tex:101`; `9_discussion.tex:93`.
*Adequate?* **Partly.** The dependence is disclosed but not shown to be irrelevant to the cost comparison.
*Model answer:* "The set-up is answer-dependent for R4, R6b and R5b only, and a new problem must supply its data; answer-free point-datum rows exist in Definition 2. The cost comparison is not affected, because the equation block sets the norm's leading term (the constraint rows grow more slowly, `4_standard.tex:266`) and the gap's upper bound holds for any rows (`4_standard.tex:443`)."

**Q9. Theorem 2 gives no constant, the unscaled gap on R2c is about 10⁻⁵, and ζ's constants were calibrated on the benchmark set. Is "Θ(1)" meaningful?**
*Answered:* `5_descriptor.tex:156,158,183`; `D_descriptor.tex:254`; `8_results.tex:216,228`; `9_discussion.tex:91,93`.
*Adequate?* **Mostly.** The compactness limitation and the in-sample calibration are both disclosed. The rescaled R2c gap (0.715, flat from n = 7 to 8) answers the practical concern. The dipping-coefficient test (`5_descriptor.tex:183`) is a good out-of-class probe.
*Model answer to a follow-up:* "The constant depends on the equation's own scale, which is why the unscaled gap on a stiff problem is small and why ζ exists; Θ(1) says the resolution does not erode it. A quantitative constant for constant coefficients, from the explicit solution operator, is the first step of self-certification in §10.2."

**Q10. "A trusted kernel does not certify a converged lift": isn't that obvious from IVP uniqueness?**
*Answered:* `6_extensions.tex:132`; `8_results.tex:250`; `9_discussion.tex:75`; `10_conclusions.tex:91`.
*Adequate?* **Yes, if it is framed as predicted and then confirmed.** §6.5 predicts it, and the finding is its practical consequence. Keep it out of the increment list (item 9).

**Q11 (hostile). Your title says "Solving … Navier–Stokes". What is the Reynolds number, and was anything run as a circuit?**
*Answered:* `6_extensions.tex:181`; `8_results.tex:281-303`; the title `1_title.tex:14`.
*Adequate?* **No** (item 7).
*Model answer:* "The flow is 2-D vorticity on a 2π box with ν = 1 and initial amplitude up to 30, a Reynolds number of order ten, truncated to 12–48 Fourier modes, and it was prepared by exact emulation with no circuit simulated. It demonstrates that the lift, ratio rows and time axis run end to end on an incompressible flow and that the descriptor's time axis lowers the degree there; it is not a fluid simulation of practical interest."

**Q12. Your gate counts are CX after transpiling to {CX, U}. A fault-tolerant cost is set by non-Clifford gates. What do 1.3 × 10⁹ two-qubit gates mean?**
*Answered:* `9_discussion.tex:82,84`; `7_pipeline.tex:277`.
*Adequate?* **Yes, as a caveat.** The omission of rotation synthesis, code overhead and depth is stated.
*Model answer to a follow-up:* "They compare the two forms per query on a common basis, and the forms' ratio is dominated by the degree, which is basis-independent; a T-count would multiply both forms' counts by the rotation-synthesis overhead and not change the comparison."

**Q13. The field is decoded from amplitudes a quantum computer does not expose. Doesn't readout (about N estimates) erase every gain?**
*Answered:* `2_literature.tex:282`; `7_pipeline.tex:267`; `9_discussion.tex:42,93`; `10_conclusions.tex:105`; `1_introduction.tex:125`.
*Adequate?* **Yes in Chapters 2, 7 and 9; weak in Chapter 1** ("a research field of its own").
*Model answer to a follow-up:* "For the full field, yes, which is shared by every route in Table 2.1 and is why I compare formulations, not solvers; a linear functional or point value costs O(1/δ) by amplitude estimation. Wu et al.'s interferometric readout, corrected for p_G < 1, is built and verified at small n, and a shot-count study on R2a is the further-work item that supplies the factor my costs omit."

**Q14. Your proposal promised the nonlinear Schrödinger and complex Ginzburg–Landau equations by generalised QSVT. Neither was done. Why?**
*Answered:* `1_introduction.tex:127`; App. K, Table K.1.
*Adequate?* **Yes.** The reasons are scientific: the cost had to be settled first; GQSP suffices for a Hermitian H = R†R; complex fields reduce to realification, with no non-Hermitian filter needed. A marker will accept this. Be ready to say what native complex preparation needs (complex loaders only, `10_conclusions.tex:107`).

**Q15 (hostile). On R3 the standard form wins at the ideal bound and the descriptor's as-built advantage is the encoder's. Isn't the R3 comparison an artefact of having no exact encoding of M_a G²?**
*Answered:* `4_standard.tex:460`; `8_results.tex:187`; `9_discussion.tex:71`; Table 9.1.
*Adequate?* **Yes.** This is one of the thesis's best-handled points. The as-built advantage is attributed to the encoder, the reversal is reported as a finding, the mechanism (a zero at both ends suppressing the top modes where Markov's inequality makes them largest) is given and contrasted with R4a, and a testable prediction for an interior zero is stated.

*Reserve questions:*
- Why is the widest exact verification a reproduction record (R4d as printed, 25 qubits) rather than a problem as run, while a 25-qubit two-axis reflection goes unverified? (`8_results.tex:94`: adequate as disclosed.)
- Your Table D.3 is empty; where is the evidence for the slice-row weighting? (Item 2: inadequate until fixed.)
- At n = 8 the descriptor's query costs about as many gates as the structured standard form's (46,260 against 46,324) and the ancilla differ by 3. Is the O(log n) ancilla claim visible at any size you ran? (`8_results.tex:199`: adequate; it is scoped as first showing at n = 8.)

---

## 4. Where the thesis is strongest (the rewrite must not weaken these)

1. **The encoder/Hamiltonian separation.** It runs from Ch. 4's opening (`4_standard.tex:85`) through the ideal-encoding bound and the floor for every encoding (`:456`) to Table 8.1 and Fig. 8.1. It is the most persuasive exhibit in the thesis. Keep the three columns, and keep the admission that the as-built comparison is *not* conservative (`7_pipeline.tex:279`).
2. **Theorem 2 and its proof.** It is sound, honest about its lack of a constant (`D_descriptor.tex:254`), and tied to FOSLS coercivity in §9.1. It is the intellectual centre of the thesis, and it should be promoted, not trimmed (item 9).
3. **Scope discipline.** `def:regular` is cited for every descriptor claim, and Table 5.1 and Table 9.1 carry the class. "Neither form is polylogarithmic" sits beside every gain, and the floor is hedged to what Lin–Tong supports (`9_discussion.tex:38`). A referee will find no unscoped headline, except Θ̃(N) as a floor (item 1). Rescope that one; do not loosen the others.
4. **Negative results reported as findings.**
   - R3 at the ideal bound, and the heat equation at n = 4;
   - the two-axis gap falling even when rescaled;
   - diverging lifts with trusted kernels on Burgers and on Navier–Stokes;
   - the three QITE T1 misses reported, not re-judged.

   This is exactly what the mark sheet's negative-results clause protects. Keep "*Negative:*" in §8.6.
5. **Chapter 3 as prior art, judged.** Strengths, Weaknesses (cost, evidence, scope) and Open problems turn into Q(i)–(iii) (`3_pihm.tex:211-224`), with Paine 2026 handled as concurrent work. This carries the high-distinction gate.
6. **The verification architecture.** Targets are assembled independently of the compiler; there are three operator modes with stated tolerances; T1 = T2 on every minimax record; acceptance bars are never adjusted; and the "limit of the simulation budget, not of the method" distinction is kept (`7_pipeline.tex:250`).
7. **The reproduction and audit of Wu et al. confined to Appendix I.** The body names each weakness once, and the validation paragraph (`4_standard.tex:303`) shows the baseline is the paper's method, with departures justified by error floors.
8. **Chapter 9's mechanism-first discussion**, notably the reading of the degree as the linear-systems law with the residual's condition number (`9_discussion.tex:34`), and the R3/R4a account (`:71`). This is the "insight into the significance" that band 4 asks for.
9. **Chapter 10's further work**: each item is a concrete, cheap, falsifiable test grown from a stated limit. Item 1 makes it stronger.

---

### Appendix to this report: the scratch check behind item 1

Not a `pihm` record and not for quotation. Rerun it in `pihm` if you want a key. The factors and constraint row are those of `5_descriptor.tex:51` and `4_standard.tex:213`, and the build reproduces Table 8.1's descriptor column (Δ = 2.87, ‖H‖ = 4.2 × 10⁶ at n = 8).

```python
import numpy as np
from numpy.polynomial import chebyshev as C

def factors(N):
    Dt = np.zeros((N, N)); Bt = np.eye(N); Bt[0, 0] = 2.0
    Dt[0, 1] = 2*np.sqrt(2)
    for i in range(1, N-1): Dt[i, i+1] = 2*(i+1)
    for i in range(N-2): Bt[i, i+2] = -1.0
    Bt[0, 2] = -np.sqrt(2)
    return Bt, Dt

def tau(x, N):
    s = np.full(N, np.sqrt(2.0/N)); s[0] = 1/np.sqrt(N)
    return np.array([C.chebval(x, np.eye(N)[k]) for k in range(N)])*s

def r2a(N, zeta=4.0, s=0.0):              # f''+4f'+4f=0, f(-1)=0; s = row-weight exponent
    Bt, Dt = factors(N); Z = np.zeros((N, N)); I = np.eye(N)
    P = np.diag((2.0*np.arange(1, N+1))**(-s))
    R = np.vstack([np.hstack([-P@Dt, P@Bt, Z]), np.hstack([Z, -P@Dt, P@Bt]),
                   np.hstack([4*I, 4*I, I]),
                   np.hstack([np.sqrt(N)*tau(-1.0, N), np.zeros(2*N)])[None, :]])
    return R @ np.diag(np.r_[np.ones(N), zeta*np.ones(N), zeta**2*np.ones(N)])

for s in (0.0, 0.5, 0.75, 1.0):
    sv = [np.linalg.svd(r2a(2**n, s=s), compute_uv=False)[::-1] for n in (7, 9)]
    c = [v[-1]/v[1] for v in sv]
    print(s, c, np.log2(c[1]/c[0])/2)       # sigma_max/sigma_1 and its exponent in N
```
