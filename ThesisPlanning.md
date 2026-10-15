# ThesisPlanning.md: the thesis structure, built on `pihm` as built

## Turning the `pihm` rebuild into a submittable (and publishable) Master's thesis

*Version 3.17, 2026-10-16 (v3.17: Chapter 10 split into two subsections, after Gemini's point 10 (`GeminiReviewPlan.md` row 10, Prompt 5). §10.1 Conclusions answers Q(i)–(iii) in turn, naming them, then the thesis statement, the implications beyond the method and the two boundaries, one sentence for each point Ch. 9 proves and no mechanism retold; §10.2 Future Work carries bold run-in leads and gains the measured datum-row weights recast as a question, the ultraspherical expectation of §9.5 and the derivation of ζ from the equation. The no-results rule stands (§5.10, §4.2). v3.16: the ζ rule takes no name or term, never "a priori" (which stays for the filter's parameters) and never "calibrated rule"; §5.4 states that its two constants were selected by calibration on the benchmark problems and held fixed, why a simple zero needs ζ ∝ N, that a coefficient dipping near zero defeats the regular weight, and that deriving ζ from the equation is further work (GeminiReviewPlan.md rows 5a–5c). v3.15: Chapter 10 re-planned as four movements, the so-what (one thesis statement answering the three questions in words), implications beyond the method, limitations as boundaries with their barriers, and a forward horizon of three open questions; the verdict for each contribution is dropped as a restatement of Chs 8–9, and Ch. 10 now reframes Ch. 9 without re-deriving it (§5.10, §3.1). v3.14: the appendices restructured, 13 → 11, in chapter order: the gate reference deleted, every test of the paper gathered in Appendix I, every tier-labelled number outside Chapter 8 in Appendix H, Appendix J cut to one page that cites the repository at a frozen tag, and the material moved to the repository staged in `3_footer/appendices/_offload_to_pihm.tex`; every appendix letter in this plan updated, the old → new map in §6. v3.13: Chapter 1 re-planned against the drafted chapters to an unheaded opening (target, method, the cost left open, the number, quoted as built and at the ideal bound) and two subsections, Contributions and Scope (§1.1) and Outline (§1.2); the survey of algorithm families and concept figure F0 dropped, the contributions listed without labels; every §1.x pointer in this plan and the style guide retargeted (§5.1, §4.2). v3.12: Chapter 10 written as one continuous chapter, its two subsections merged: the verdicts in the order of the questions, without contribution labels or section pointers, and the further work grown out of the two limits that bound the result (§5.10, §4.2). v3.11: the class of problem named once. `def:regular` (§5.3, before `thm:flat-gap`) defines a *regular* problem, one axis, polynomial coefficients, a leading coefficient without zeros on [−1, 1], analytic data and a solution unique up to scale, which are `thm:flat-gap`'s hypotheses, and a *singular* one, whose leading coefficient has a zero; every later degree, gap and α scope cites the class by name (§3.4) instead of restating the condition, and the restatements that dropped part of the hypotheses are gone. v3.10: Chapter 5's "Constraints and Partial Differential Equations" merged into §5.2, renamed "The Descriptor Residual and Its Kernel", the constraints stated before the kernel theorem that assumes them and the several axes after it; §5.4–5.9 renumbered §5.3–5.8 throughout. v3.9: Chapter 5's opening, "The Idea" and "The Banded Factorisation" merged into one §5.1, the factorisation being the idea; §5.3–5.10 renumbered §5.2–5.9 throughout. v3.8: Chapter 5's review pass: block rescaling adds no ancilla but is not free in gates, so "no gate cost" is withdrawn everywhere; the regular one-axis gap proved Θ(1) (`thm:flat-gap`, App. D); Algorithm 5.1 moved to App. D beside its walkthrough. v3.7: the typeface, T-06: matrices italic, register-changing maps calligraphic, blackboard bold only for number sets, expectation and, pending, the constraint rows. v3.6: the opening and closing convention, §3.5 rule 1, and the narrative threads, §3.2, after Green's exemplar: a chapter arrives at its question from the tension the previous chapter left, carries no section roadmap, and closes on a hand-off; the chapter entries of §4.2 and §5 amended to match. v3.5: `StructuralReview.md` F4, F5 and F7 applied: Chapter 2 restructured and drafted (§5.2), Q(iii) given its second half (§3.2), the ladder moved to §4.1 and "trusted" defined at its first use in §4.3. v3.4: the structural pass F1–F3 of `StructuralReview.md` applied: the evidence rule in T-20, the departures compressed (T-30, T-34), Chapter 7 compressed, the budget of §4.1 revised. v3.3: Chapter 8 drafted against the results-v1 records; its deviations from §5.8 and the corrections they forced are marked "v3.3" in place. v3.2: plan §5.6 checked against `pihm`'s companion, reports and code; its corrections are marked "v3.2" in place). Ten chapters. Chapter 3 presents and judges Wu et al.'s method as
prior art; Chapter 4 states the construction once, in the form this thesis runs (the standard
form), and answers the first question; the reproduction and audit of the paper live in Appendix I.
v3.1 merges v3.0's Chapters 6 (systems and complex-valued fields) and 7 (nonlinearity) into one
chapter, "Systems and Nonlinearity" (T-31), so the pipeline, the study, the discussion and the
conclusions are now Chapters 7–10.*

**Premise.** `pihm` is built and verified through gate G6. Production (P8) reruns every campaign on
Setonix at one version of the code; that commit is tagged `results-v1`, and the thesis quotes only
its records, through `\res{<run>}{<metric>}`. **Numbers in this plan are planning values** taken
from `pihm`'s reports and the generated results guide. They locate the story; they are never typed
into the thesis. Where P8 moves one far enough to change a finding, §12 (TR-1) says what to do.

**How to read this.**

- §0 is the short version: the story, the chapter map and the status board.
- §1 is the decision record. §2 says how the other planning documents relate to this one, and
  lists the REVISE items still open.
- §3 fixes the contributions, the three questions, the spine sentence, the vocabulary and the
  rules that keep the thesis a scientific argument rather than a code map.
- §4 gives the page budget, the LaTeX tree and the scaffold conventions. §5 goes chapter by
  chapter; it is the part you follow while writing.
- §6 covers the appendices, §7 the figures and tables, §8 notation, §9 the claims register, §10
  how numbers and figures move from `pihm`, §11 the writing order, §12 risks, §13 the front matter
  and §14 the pre-submission checklist.
- **Section numbers.** "Plan §n" is this document. In the contributions' evidence lines, the
  chapter entries (plan §5), the figure and table plans and the claims register, a bare §n.m is
  the *thesis's* section n.m.

---

## 0. Summary

### 0.1 The thesis in one paragraph: the scientific story

Wu et al. (`wu2025pihm`) cast a differential equation's Chebyshev-coefficient solution as the
ground state of a physics-informed effective Hamiltonian H = R†R, and prepare it by filtering. Their
own Discussion leaves two questions open: how the spectral gap behaves, and what differentiation
costs. This thesis answers both, in seven steps (steps 6 and 7 are one chapter, Chapter 6).

1. **The standard form.** The paper's construction is stated once, in the form this thesis runs
   (Chapter 4), and defined by its state: the state holds the field alone and every derivative is
   eliminated through the dense G (with the paper's lifts and least squares), with each printed choice that would make the problem inaccurate, answer-dependent or
   ill posed replaced, and the reason given where the construction meets it: exact constraint
   points, Chebyshev sources, datum slices for initial and boundary functions, a substitution that
   removes a double zero, any number of axes, and a stacked residual R whose H = R†R is never
   formed. Table T10 collects the departures. They change the data, never G or the Gram structure,
   so the baseline has the paper's cost and better accuracy. Its paper-faithful variant reproduces
   the printed scale factors of all eleven ODE panels to within one unit of the last printed digit;
   the PDE and nonlinear panels do not reproduce (the record is Appendix I).
2. **Where the cost lies.** The filter's degree is d = Θ(√(α_H/Δ) log 1/ε): the residual's
   effective condition number. Two costs hide in it. The *encoder's cost*: the paper's
   normalisation of G is about N³ looser than ‖G‖, and our exact structured encoding removes it for
   constant-coefficient problems. The *Hamiltonian's cost*: ‖H_std‖ = Θ(N^{4k}) for an order-k
   equation against a gap measured flat, so d = Θ̃(N^{2k}) (Θ̃(N⁴) for the paper's second-order
   panels) whatever the encoder.
3. **The reformulation (headline).** The descriptor form replaces the dense G by its banded factors,
   G = B̃⁻¹D̃. An equation of higher order carries its derivatives as blocks tied by banded
   recurrences (the *chain*); a first-order equation or system is multiplied through by B̃ (the
   *mass form*). The kernel is unchanged, ‖H_desc‖ = Θ(N²), and the residual is one flat LCU with
   O(log n) ancilla. The idea has two classical antecedents, the ultraspherical spectral method
   (banded differentiation) and first-order-system least squares (conditioning); the increment is
   its transfer to a block-encoded Hamiltonian, with its consequences for ground-state preparation
   measured.
4. **Its challenge.** The descriptor's norm carries every derivative it carries. Its gap is flat
   only where the equation controls each of them: a *regular* problem (one axis, a leading
   coefficient without zeros; `def:regular`). On a *singular* problem, and on two axes, the gap closes with N, and the derivative blocks
   crowd the field block out of the ground state. Block rescaling, one weight per block folded into the LCU
   coefficients without ancilla, restores an O(1) gap on one axis. On two axes the gap still falls,
   and a double zero is beyond any rescaling. Measured as built and at an ideal encoding, the
   descriptor needs far fewer queries on one-axis problems, modestly fewer on most PDEs, and more
   on the heat panel at small n and on the Legendre problem at an ideal encoding.
5. **Verified preparation.** One pipeline serves both forms: a stacked-residual reflection, its
   qubitised walk, GQSP with the minimax edge filter (chosen by a QITE–minimax study), a priori
   parameters and answer-independent initial states. Operators are verified exactly, by probe and
   by IR. The circuit simulation equals the exact emulation to 1e-10 on every minimax record, and
   resource estimates carry the rest.
6. **Beyond one real field.** The paper treats one real scalar field, and its Discussion sets a
   complex-valued state aside as making the ground state "difficult to find". Several coupled
   fields share one state, a block each, in both forms (the descriptor's mass form); vector data
   enter as ratio rows; the coupling is a sum of matchings on a circuit. A complex R still gives a
   Hermitian H = R†R, so the filter never meets a non-Hermitian operator: complex-valued linear
   equations are carried by realification as coupled real systems (R7 is exactly z′ = −iπz), and
   one native complex encoding, the tensor layout's coupling, is built and verified but not used for
   preparation.
7. **Nonlinearity.** The paper's doubled space encodes exactly but projects: its kernel is
   exponentially degenerate. The Carleman lift prepares, in both forms. On Burgers its convergence
   follows a/ν, not the worst-case ratio ρ; on Navier–Stokes it also grows with the modes, yet
   converges at ρ far above one (v3.3: checked against the results-v1 records); on both, past the
   boundary, the kernel stays unique and trusted while the lift diverges. The descriptor's time axis
   lowers the degree in every Navier–Stokes pair, and the thesis culminates in 2-D incompressible
   Navier–Stokes: the Taylor–Green vortex and a vortex pair prepared on 12–48 modes and built to 80,
   and a tensor-layout coupling of 2K − 1 terms to 316 modes.

Neither form is poly-log, every result is a classical computation, and nothing ran on hardware.

### 0.2 Chapter map

| # | chapter | pp | rubric criterion | answers | writable |
|---|---|---|---|---|---|
| 1 | Introduction | 3 | Intro & Lit /20 | – | last (W4) |
| 2 | Background and Literature Review | 7 | Intro & Lit /20 | – | now (W1) |
| 3 | The Physics-Informed Effective Hamiltonian Method | 4 | Intro & Lit /20 (the HD gate) | poses Q(i)–(iii) | now (W1) |
| 4 | The Standard Form and Its Cost | 7.5 | Model Formulation /30 | Q(i); S1, S2 | now (W1) |
| 5 | The Descriptor Reformulation | 10.5 | Model Formulation /30 (the core) | Q(ii); C | now (W1) |
| 6 | Systems and Nonlinearity | 6.5 | Model Formulation /30 | Q(iii); S4 | now (W1) |
| 7 | Preparing and Verifying the Ground State | 6 | Model Formulation /30 (configuration, inputs, software, experiment design) | S3 | now (W1) |
| 8 | Numerical Study | 10 | Results & Discussion /30 | evidence for all | after P8's copy-back (W2) |
| 9 | Discussion | 3 | Results & Discussion /30 | – | W3 |
| 10 | Conclusions and Future Work | 2 | Conclusions /10 | – | last (W4) |
| | **total body** | **59.5** | | | |

The hard cap is 60 pages and the guidelines penalise overrun; the budget of §4.1 sums to 59.5. The drafted
chapters already run long (§0.3), so the trim order of §4.1 is live, not contingent. Appendices
A–M are outside the count (§6).

### 0.3 Status board (update as you go)

Columns: **S** = scaffolded to this plan, **D** = drafted, **N** = numbers current from P8,
**R** = reviewed (Review Mode, `CLAUDE.md`), **F** = final.

| chapter / item | S | D | N | R | F | notes |
|---|---|---|---|---|---|---|
| Front matter (title, declaration, achievement, abstract) | ☑ | ☐ | ☐ | ☐ | ☐ | §13 |
| 1 Introduction | ☑ | ☐ | ☐ | ☐ | ☐ | v3.13 (2026-10-14): re-planned against the drafted Chs 2–10 to an unheaded opening and two subsections (§5.1); scaffold rewritten, numbers by current key, F0 dropped. The outline (§1.2) must name Ch. 3 as judged prior art and Ch. 4 as the standard form. Open: the applications citations (CITE-NEEDED) |
| 2 Background and Literature Review | ☑ | ◐ | n/a | ☐ | ☐ | v3.5 (2026-10-12): restructured (F4) and drafted in full; every citation checked against its record and its claim. Reviewed and rewritten for density 2026-10-13 (no announcement sentences, aphorisms or rhetorical "not X but Y"; plainer headings), no claim dropped; length in §5.2. `eq:degree` now carries the edge argument (spectral gap amplification) and the polynomial-filter hedge |
| 3 PIHM (prior art), `3_pihm.tex` | ☑ | ◐ | ☐ | ☐ | ☐ | scaffold and first-pass prose to plan §5.3 |
| 4 Standard form, `4_standard.tex` | ☑ | ◐ | ☐ | ☐ | ☐ | scaffold and first-pass prose to plan §5.4. v3.4 pass (F1, F2): degrees to §8.2, departures to one clause (arguments and numbers to App. B and I), T10 compact; 5,574 → 4,999 words, about 10 pp against 7.5 |
| 5 Descriptor, `5_descriptor.tex` | ☑ | ◐ | ☐ | ◐ | ☐ | reviewed 2026-10-12 and fixes applied (pointers retargeted to Ch. 4; App. D drafted in full). The gates-per-query Standing Fact is scoped to constant coefficients (2026-10-12). Open: App. D's `\prov` probe tables. v3.4 pass (F1): degrees, gates per query and the reflection's ancilla to §8.2; rescaling constants, algorithm commentary and the Haar paragraph to App. D; 6,773 → 6,404 words, about 13.5 pp against 10.5. Review 2 (2026-10-13, v3.8): rescaling's gate claim corrected (code: weights before the Pauli expansion); Algorithm 5.1's order fixed and the listing moved to App. D; R5b quoted from n = 4 (n = 3 untrusted in both forms); `thm:flat-gap` proved (App. D); de-duplicated against App. D; 6,339 → 5,840 words, about 10.65 pp at the new margins (placeholder figures at 6 cm). v3.9 (2026-10-14): opening, §5.1 and §5.2 merged into §5.1, each of the antecedent credit, the factor-keeping move and the norm claim now stated once. v3.10 (2026-10-14): §5.3 merged into §5.2 ("The Descriptor Residual and Its Kernel"), the theorem's two forward references removed, the duplicated coefficient-and-source sentence dropped, the several-axis state cost stated in one clause with its count in App. D |
| 6 Beyond a single real field, `6_extensions.tex` | ☑ | ◐ | ☐ | ☐ | ☐ | first-pass prose to plan §5.6 v3.2 (2026-10-12), checked against companions, reports 16–17 and the code; apparatus moved to App. E, now drafted in full; ≈ 7.5 pp against 6.5 (v3.4: the tensor layout's CNOTs to `tab:lift-circuits`; §6.8's results to pointers). Open: two derived keys (R7's gap ratio; the fold norms) |
| 7 Pipeline, `7_pipeline.tex` | ☑ | ◐ | ☐ | ◐ | ☐ | first-pass prose to plan §5.7 (2026-10-12); reviewed 2026-10-12 and fixes applied: the fairness declaration corrected (as built favours the descriptor; also Ch. 4 §4.4, this plan, STYLE_GUIDE, CLAUDE.md); reflection credited to qubitisation/QSVT; trim candidates executed (F2 dropped; `tab:run-inputs` → App. H; iterative reference, T1 cost model and `tab:acceptance` → App. G; `eq:qite-filter` and `eq:readout-identity` → App. F); verification and filter-study numbers → §8.1's NOTE. v3.4 pass (F3): `tab:constraint-kinds` → App. H; `prop:filter-normalisation` and the imaginary-time detail → App. F; `tab:verification-modes` → App. G; the T1 frontier and the fairness numbers → §8.1–8.2; 5,147 → 4,223 words, about 9 pp against 6 (F3's estimate was optimistic: the next cuts are Review Mode's). Review 2 (2026-10-13): Lin–Tong attribution corrected; R2a's relative gap → §5.8, the iterative reference's reach → App. G (evidence rule); GQSP and the filter's optimality left to §2.4; heights, amplification footnote and `eq:error-budget` → App. F, G; probe claim narrowed; closing hand-off added; 8.3 → 7.5 pp measured. Open: plan §2.2 TODO |
| 8 Numerical Study, `8_results.tex` | ☑ | ◐ | ◐ | ☐ | ☐ | first pass 2026-10-12 against the results-v1 records (every key resolves; rerun the exporter `--used-only` to refresh the committed `numbers.tex`); deviations from §5.8 marked v3.3 (F10 → `tab:growth`; R10 scope 12–48 prepared, 80 built; no T1 on R10). Review pass 2 (2026-10-13): 13.3 → 10.9 pp measured against 10 (F7, F8 → App. G; F12 now the reversals figure in §8.2; three-problem list cut per §4.1's trim order; ideal-bound degrees added on R7, R8, Burgers; heat reversal scoped to R5b at the ideal bound; Burgers' time-axis advantage scoped to n_t ≥ 4). Figures F7–F9, F11–F14 are placeholders (notebooks not exported). Open: the `\prov` items of plan §2.1 |
| 9 Discussion, `9_discussion.tex` | ☐ | ☐ | ☐ | ☐ | ☐ | scaffold aligned 2026-10-12: "What the Reproduction Says About the Published Method" removed. Open: T9 gains two rows |
| 10 Conclusions, `10_conclusions.tex` | ☑ | ☑ | ☑ | ☐ | ☐ | v3.17 (2026-10-16): split into §10.1 Conclusions and §10.2 Future Work (§5.10), redrafted by Claude for the author to rewrite; no result quoted; 3.05 pp before the split, 2.4 pp after (§10.1 ≈ 1.25, §10.2 ≈ 1.15), measured in a scratch build, 0.4 pp over budget. Open: the author's rewrite; a Review Mode pass; the FOSLS CITE-NEEDED in §10.2 |
| Appendices A–K | ◐ | ☐ | ☐ | ☐ | ☐ | restructured 2026-10-15 (plan §6); A–H drafted (small REVISEs in F, G, H); I drafted except the hypotheses for Figs 6–7, the claims' derivations and the paper-faithful conventions; J to write (one page); the writing order is in §6 |
| `ref.bib` audit (T-29) | – | ☐ | – | – | ☐ | before W1 drafting ends |
| Verification Mode pass | | | | ◐ | | §14. Chs 3–7 against the appendices and the code, 2026-10-12: findings A1–A9, B1–B12, C applied |

**Measured length (2026-10-12 build, after v3.4's pass):** Ch. 2 5 pp (mostly unwritten), Ch. 3 5,
Ch. 4 10, Ch. 5 14, Ch. 6 8, Ch. 7 10, Ch. 8 14 (whole pages between chapter starts, floats
included; seven placeholder figures in Ch. 8). The pass removed about 1,850 words (about 3.5 pp)
from Chs 4–7 and added about 80 to Ch. 8. Review Mode ranks the further cuts; the drafts state every
claim the plan lists.

---

## 1. Decisions

Identifiers are stable references cited in the scaffold. T-05, T-12, T-33 and T-35 are not used;
their subjects are held by T-20 and T-31, T-24, T-27 and T-30.

| # | question | decision | why |
|---|---|---|---|
| T-01 | contribution framing | **The descriptor as the headline, plus numbered supporting contributions** (plan §3.1) | the descriptor is the result a referee would publish; the rest serves it or extends it |
| T-02 | rubric project type | **Modelling**: Model Formulation /30 + Results & Discussion /30. Chapters 4–7 carry the first, 8–9 the second. Software, the model configuration and its input options are named requirements (plan §5.7) | the work builds and studies a model; the mark sheet's Modelling wording fits it |
| T-03 | schedule | **No dates**; the writing is ordered by dependency only (§11) | |
| T-04 | publication | **Thesis first**; paper-shaped material is marked only where it falls out (plan §3.6) | |
| T-06 | operator notation | (v3.7, 2026-10-13, replacing blackboard bold) **Matrices italic**: G, B̃, D̃, R₀, U_odd, Λ, U_CG, and Γ for a system's coupling (Γ_K the lift's), since A is the residual and 𝔸 the paper's residual. **Calligraphic** for the maps that change the register: ℳ_{x^p}, ℳ_a (Olver & Townsend's ℳ[a]) and 𝒩₁, 𝒩_x, beside 𝒯, ℋ, 𝒪. **Blackboard bold** only for ℝ, ℂ, 𝔼 and, pending a decision, the constraint rows 𝔹, 𝔻⁽⁰⁾, 𝕊, 𝔽. The paper's convention (every non-unitary matrix blackboard bold) said once, in §3.2's footnote. Macro names unchanged, so `pihm`'s documentation still copies | the paper's convention was half kept under a different rule that the thesis broke (𝔸_K assembled, R₀ and S fixed); plain italic M, A, F, S, U, n were taken, hence ℳ, Γ, 𝒩, U_CG; the antecedents (Olver & Townsend, Trefethen, QSVT, Carleman) use italic or calligraphic |
| T-07 | regime subscripts | **H_std, A_std, H_desc, A_desc**; bare H, A or R only in regime-independent statements (Ch. 7). Ch. 6's system rows carry the subscripts too | the two forms are compared everywhere; an unsubscripted symbol is ambiguous |
| T-08 | imaginary-time symbol | **β** for QITE's imaginary time; τ(x) stays the paper's feature state. β appears only with the QITE filter | collision with τ(x) |
| T-09 | Carleman ratio symbol | **ρ**; R stays the stacked residual | collision with R |
| T-10 | benchmark labels and vocabulary | **R1–R10**, called *benchmark problems*; never "rung", "pillar", "gate G3" or "tier T2" in prose; *operator verification*, *state-preparation verification*, *circuit simulation / exact emulation / resource estimate* with (T1/T2/T3) once | code vocabulary is not thesis vocabulary |
| T-11 | the notation table | in the front matter (`1_header/6_notation.tex`) | |
| T-13 | Chapter 3's register | **Prior art, judged.** Ch. 3 presents Wu et al.'s method as published, with the paper's own equations only where a weakness is stated against them, and closes on Q(i)–(iii). Our measurements and constructions are never in §3.1–3.4; §3.5 points to where each weakness is argued (Ch. 4) or evidenced (App. I) | the Intro & Lit HD gate is a critical assessment of the material reviewed; a marker must be able to see what is the paper's |
| T-14 | title | keep the working title until W4, then choose from §13.1 | |
| T-15 | numbers | keyed lookups `\res{<run>}{<metric>}` from `pihm`'s exporter; a missing number renders its reason; `--final` checks source digests (D-130) | typed numbers drift |
| T-16 | G's convention | **G is the coefficient-space map f ↦ f′** (strictly upper triangular), as in `pihm`; the paper prints the same matrix as 𝔾ₙᵀ, said once (§4.2) | |
| T-17 | scaffold guidance | **LaTeX comments only**; placeholders render; provisional numbers render tinted | |
| T-18 | appendix files | **one file per appendix** under `3_footer/appendices/`; the proposal PDF included with `pdfpages` | |
| T-19 | notation collisions | raw basis subscript **raw**; block-rescaling constant **ζ**; the paper's ladder coefficient **μ**; condition number **cond(·)**; doubled-space Hamiltonian **H_⊗** | plan §8.2 |
| T-20 | chapter order | **Story first.** After the paper's critical assessment (Ch. 3) come the three answers in order: the standard form and its cost (Ch. 4, Q(i)); the descriptor (Ch. 5, Q(ii)); the extensions beyond one real field (Ch. 6, Q(iii)), coupled systems first, as the prerequisite of nonlinearity. The shared pipeline and the design of the numerical experiment follow as Ch. 7, immediately before the evidence (Ch. 8). The degree formula for filtering an edge ground state is in the background (§2.4, v3.5), so Chs 4–6 can argue costs. Ch. 8 has one section per question or contribution. **Evidence rule (v3.4, `StructuralReview.md` F1):** Chs 4–6 quote proofs and exact classical computations on the assembled operators only (norms, gaps, kernel dimensions, field weights, α/‖·‖ of built encodings); every filter degree, preparation, gate count and tier-labelled number lives in Ch. 8. A formulation chapter derives its law through `eq:degree` and names the results section that measures it; Ch. 7 states no result | the reader meets the tension (the Hamiltonian's cost) before the machinery; the pipeline, placed before Ch. 8, reads as the method of a numerical study, where the rubric's "design of numerical experiment" belongs |
| T-21 | the descriptor's challenge | **Its own body subsection** (§5.3, the gap of a carried derivative) before the cure (§5.4, block rescaling), and its own results section (§8.3) | a genuine failure of the naive reformulation, diagnosed, cured without fitting to any solution and bounded: what the top band calls insight |
| T-22 | first-order equations and systems | **The descriptor has two layouts**, named in the body: the chain (order ≥ 2) and the mass form (first-order equations and systems: I⊗D̃ − Γ⊗B̃, the standard rows times I⊗B̃). The kernel-equivalence theorem covers both; systems themselves are Ch. 6's | the mass form is the descriptor of R1 and R7–R10 |
| T-23 | the preparation filter | **The minimax edge filter** prepares every comparison and extension; QITE is the paper's filter, run in the reproduction (App. I) and in the filter study (§8.1). β, the Bessel coefficients and Σ\|q_k\| = 1 stay, as the studied filter's | P8 runs the R1–R5 comparison under minimax in both forms |
| T-24 | readout | **Classical.** The field is decoded from the prepared state; η from the regular datum. The paper's interferometric protocol, built and verified at small n with our correction for p_G < 1, is one paragraph in §7.7, its identity in Appendix F, and future work | `pihm` decision 27 |
| T-25 | fairness of the comparison | **Every cost comparison is quoted twice**: as built (each form's own circuits) and at the ideal-encoding bound α = ‖R‖, which has neither form's encoding in it. Where the order reverses, the reversal is a reported finding | the structured encoding is loose on R3 (C-02), so as-built comparisons there favour the descriptor for the wrong reason |
| T-26 | prior art for the headline | **Credit two antecedents** wherever the contribution is claimed: the ultraspherical spectral method (Olver & Townsend 2013) and first-order-system least squares (Cai, Lazarov, Manteuffel & McCormick 1994). Cite the concurrent Paine 2026 (arXiv:2609.26330) in §2.2 and §3.5 | "isn't this FOSLS, or ultraspherical?" is answered first; the increment is the transfer to a block-encoded Hamiltonian and its measured consequences |
| T-27 | variant vocabulary | **The problem is unnamed.** "R2a" is the problem. The paper's panel as printed is "R2a as printed" (or "paper-faithful") and appears **only in Appendix I and in §4.4's validation paragraph**. In Ch. 4's prose a printed choice is "the printed point", "the paper's source", never a variant name. Never write "corrected" outside App. I's verbatim record | the thesis runs one problem per panel; the printed variant exists only to test the paper |
| T-28 | software in the body | **One short paragraph** (§7.9); records, provenance and source digests in Appendix J only | the rubric asks for "a description of any software tools", not a manual |
| T-29 | bibliography | **Audit `ref.bib` before drafting ends.** `wu2025pihm`'s author list must read Hsin-Yu Wu, Annie E. Paine, Evan Philip, Antonio A. Gentile and Oleksandr Kyriienko; the `note` fields print internal notes. Missing entries are listed in §5.2 | a misattributed source paper costs the Style mark and credibility |
| T-30 | Chapter 4's job | **Build once, depart in place, then cost.** Ch. 4 states the construction once, as the standard form, crediting each piece to its source (Paine et al. for the latent space and lifts, Wu et al. for the residual and its Hamiltonian, Olver for the density of G). Each place the printed method is replaced, the departure is made in one clause where the construction meets it (the defect and the replacement, with a pointer); the printed choices are stated in §3.2 and not restated, and the arguments and their numbers live in App. B and I (v3.4, `StructuralReview.md` F2). Table T10 (§4.4) collects them, with the pipeline-level departures pointing to Ch. 7. One validation paragraph (§4.4) says that the paper-faithful variant reproduces the printed matrices and the eleven ODE scale factors, and that the PDE and nonlinear panels do not (App. I). Then Q(i): the paper's encoding of G (§4.5.1), the exact structured encoding (§4.5.2–4.5.3), and what no encoding removes (§4.6) | the model is specified where the Formulation criterion looks for it, once, as run; a reader never has to apply a list of changes to the paper's version to recover it |
| T-31 | coupled systems, complex fields and nonlinearity | **One chapter, Ch. 6, "Systems and Nonlinearity" (6.5 pp; v3.1, merging v3.0's Chs 6 and 7).** Its thread: each extension is carried as a coupled linear system on one state, a block per component (several fields directly; a complex field by realification; a polynomial nonlinearity by the Carleman lift, whose components are monomials), except the paper's doubled space, which projects. Order: systems (§6.1–6.2), complex-valued fields (§6.3), the doubled space (§6.4), the Carleman lift (§6.5), every coupling and product on a circuit in one place (§6.6), the fluids (§6.7), preparation against projection (§6.8). The mass form is *applied* (its definition and kernel equivalence stay in §5.2). The chapter answers Q(iii); the systems sections are its prerequisite, not a separate question | the paper treats one real scalar field, and S4 is one contribution; two short chapters split one argument and stated the circuits (matchings, tensor layout, folds) and the system-to-lift hand-off twice. One chapter states the system once, lets the lift *be* that system with Γ → Γ_K, and gives Q(iii) a single home |
| T-32 | complex-valued equations | **Scope: realification, plus the one native complex encoding that was built; no new code.** §6.3: a complex R gives a Hermitian positive semi-definite H = R†R; the route run is realification; R7 is exactly the realification of z′ = −iπz; R9 and R10 use real Fourier bases; the tensor layout's coupling is built on complex Fourier variables and verified but never used for preparation; native complex preparation is future work | the paper's Discussion sets complex states aside, and the proposal promised them; the honest answer is formulational with narrow evidence |
| T-34 | deviations from Wu et al. | **Table T10 in §4.4** lists every deviation, residual-level (made in §4.1–4.4) and pipeline-level (stated with a pointer to Ch. 7). v3.4: compact, four columns (choice, this thesis, the printed choice's defect, where), at `\footnotesize`; the evidence for each row is App. I's. The pipeline chapter's filter section points to T10 and restates none | one place for "what did the student change, and why" |
| T-36 | where the audit lives | **Appendix I.** The reproduction of every printed panel (Table T6), the Fig. 5 triage (Figure F6), the non-reproduced panels and the hypotheses tested, every claim A-01–A-13 with its derivation and verdict (positive definiteness, uniqueness, the time rule's bound, the readout identity's correction, the circuits), the paper's filter and the tau ablation. The body names each weakness in §3.5 and argues the departures it motivates in Ch. 4; no body section re-derives or tabulates the audit | the audit tests the paper; the thesis's argument is where the cost lies. Pages go to the descriptor's results and discussion, where the marks for insight are |
| T-37 | naming the standard form | **Define by its state, once in full per chapter, then name it.** The standard form is the field alone with every derivative eliminated through G; never "the paper's regime" or a bare "the paper's method". The rule is in §3.4 | the paper's regime is a reference, not a definition, and it implies the thesis's form is the paper's, against S1 |

---

## 2. How the planning documents relate

- **`CLAUDE.md`** (the working agreement) carries the **Standing Facts**: the facts a draft may
  not contradict. It is updated whenever this plan's facts change, and wins over the guides on
  facts.
- **`thesis_guides/STRUCTURE_AND_RUBRIC.md`** is the rubric and exemplar reference: the mark sheet,
  the guidelines' formal requirements, what the exemplars do, and the Style & Presentation sweep.
  This plan is the structure.
- **`thesis_guides/STYLE_GUIDE.md`** is the register: tone, exposition, empirical presentation and
  the traps.
- **`0_results/README.md`** is how to quote a number.
- **`Code/pihm/docs/02_methods.md`** is the method as built, the source for Chapters 4 and 7 and
  Appendix G.
- **`Code/pihm/docs/companion/`** is the mathematics as built, with derivations and proofs beside the
  code and tests that implement them, sectioned as Appendices A–G: the first source for every
  appendix proof and every body proposition. Its files are cited in §5 by number (for example
  "companion 51" for `51_mass_form.md`).
- **`Code/pihm/docs/06_results_guide/`** is generated from the records (81 reproduction → 87
  findings): the first stop for what a results section, or Appendix I, can claim.
- **`Code/pihm/docs/03_problems/`** gives each benchmark problem's equation, data, constraint rows,
  datum point and reference, as printed and as run.
- **`Code/pihm/docs/22_claims_register.md`** gives the verdict of every claim A-01–C-10;
  `18_claims.md`, generated, lists the tested ones.
- **`Code/pihm/docs/20_decisions.md`** (the user's decisions) and `21_decision_log.md` (the
  implementation's) hold the reasons; they are never cited (plan §3.5).

### 2.1 REVISE items still open (fix while drafting; then delete the comment)

**Appendices.**

- **Appendix I, measured ε_G(n), qubits and gates.** `tab:app-epsilon-G` is all `\prov`; the
  rebuilt circuit's measured counts and error are not exported. Needs a derived key, or the table
  stays a bound (companion 31 gives the bound and the measured fraction of it).
- **Appendix B, several axes (`app:pihm-multi-axis`).** A visible `\todo` stub: derive the
  register count, give a worked three-variable example and the lifted-axis bookkeeping.
- **Appendix I** is scaffolded as the reproduction record only; it must take the audit of plan §6
  (T-36), including the claims' derivations from the earlier Ch. 4 draft (the time rule's bound, the
  positive-definiteness verdict, the uniqueness count's role) and Table T6 and Figure F6 from Ch. 8.
- **Appendix G.** *Resolved 2026-10-12:* drafted in full; Wedin's bound against the eigensolver's
  is `prop:wedin` there and `eq:wedin` in §7.2. *Open:* `tab:eigh-vs-svd` is a planning probe on
  a problem that is not R2a (f(−½) = 0), all `\prov`: regenerate on R2a (an eigensolver column
  needs a build-stage metric or a derived key) or relabel it; the per-atom table needs a derived key.
- **Chapter 7 and Appendices F, G (2026-10-12):** their open items are in the end-of-drafting
  TODO (§2.2).

**Chapters.**

- **Chapter 6 (`6_extensions.tex`).** *Resolved 2026-10-12:* the v3.1 REVISE items (the
  "descriptor Hamiltonian" sentence, the fold's title, T8's column, the colouring bound); the König
  citation (`konig1916graphen`, checked against Crossref); Appendix E written in full, its fluids
  LAND errors gone; the notation table's ρ entry ("sufficient, not necessary"); Table T2's y_⊥.
  *Open:* derived keys for R7's gap ratio (about 2.1) and the fold norms (1.58, 1.665, 1.21), both
  `\prov`; a Pauli-word count for the matchings (App. E states it without a number); the notation
  table's `dim w` entry uses K for the block count (left as is at the author's instruction).
- **Chapter 8.** *Resolved 2026-10-12:* the Burgers caption (converges at a/ν = 3, diverges at 10),
  the trust threshold in `tab:eta-reproduction`'s caption (20, also in App. I's header); T7 now
  `\res` in every numeric cell (first pass, 2026-10-12). *Open (`\prov`, derived keys wanted):* the
  B-17 range 1.67–1.92 (§8.1); ρ for R9 (1.86, 16.1) and R10c-M48 (≈ 24) (§8.4–8.5); R7's gap ratio
  (≈ 2.1, shared with Ch. 6); the R10 truncation's error against DNS (§8.5); the counts behind
  "every" in §8.1 (verified circuits, minimax T1 keys, trusted T2 records) and in App. I's
  `app:repro-t1` (43 of 46 QITE keys).
- **The factorisation's error 3.4e-13 (§4.5.2)** is a one-off measurement, typed as `\prov`;
  replace with a derived key (the largest entrywise error of G = R₀(2U_odd)Λ against G, n ≤ 10) or
  delete the number.

**Results README and keys.**

- `0_results/README.md`: *resolved 2026-10-12* for `degree`/`tau`, the T3 metrics and the T1
  agreement metrics (`filtered_agreement` is C-08's, before normalising; `t2_agreement` is the
  normalised state's). *Open:* no rows yet for the `growth` and `looseness` derived keys.
- The Chapter 6 evidence keys. R7's mass-form gap against the chain's (2.1 at n ≥ 4,
  `16_extensions.md` §1.1) and the matchings' term count and α against Pauli words are not exported
  as `\res` keys; add derived keys before §6.1 and §6.6 quote them, or quote them as `\prov` with a
  REVISE.
- **C-08's scope.** Every minimax T1 record meets T1 = T2 ≤ 1e-10; 43 of the 46 QITE T1 records do,
  the misses reported with their degree. The QITE records are the reproduction's and the filter
  study's, so the body states C-08 for the minimax records and App. I reports the QITE misses.
  Checked at results-v1 (2026-10-12): 43 of 46.
- The ρ sentence of §6.5 cites Liu et al., *PNAS* 118, e2026805118 (2021); check it against the
  publisher and add it to `ref.bib` (T-29).
- **STYLE_GUIDE §7** quotes the relative gap at n = 8 (5.9e-15 at n = 7 is above 2⁻⁵²; 2.3e-17 at
  n = 8 is below it).

### 2.2 End-of-drafting TODO (review together at the end; do not act on these piecemeal)

Collected while drafting; each item says where it lives. Tick here when resolved.

**Evidence gaps the Chapter 7 draft exposes (2026-10-12).**

- [ ] **The largest exact verification is a reproduction record.** The 25-qubit exact check of the
  stacked reflection is `encode/R4d/faithful/standard/n3` (the printed Maclaurin source widens the
  register); the largest exact check of a problem as run is smaller. §7.5 says "from the
  reproduction". Decide: keep, or run an exact check of a problem as run near 25 qubits.
- [ ] **Unverified wide reflections.** The R5 descriptor reflections at n = (2, 2) (27 qubits) are
  construction-only (`verify=none`), above the 24-qubit probe ceiling, and their circuit simulations
  are beyond the budget; §7.5 says the reflection there is "built and counted but not independently
  verified". Decide: raise the probe ceiling for these, or keep the caveat.
- [x] **B-17's range is `\prov`.** *Resolved 2026-10-14:* `filters/synthetic/edge` (derived from the sweep). "1.67–1.92" (§7.4) is the synthetic sweep's
  (`docs/15_filters.md` §1), not a record.
- [x] **`tab:eigh-vs-svd` (App. G) is a planning probe on a problem that is not R2a** *Resolved 2026-10-14:* regenerated on R2a, sine of the angle, `reference/R2a/<regime>/n<n>`.
  ({1,4,4} with f(−½) = 0), all `\prov`. Regenerate on R2a (needs an eigensolver metric in the build
  stage or a derived key) or relabel.
- [x] **The circuit-simulation frontier.** *Resolved 2026-10-12 at results-v1:* the widest circuit
  simulated has 20 qubits (R4a and R4d at n = 3); the two-axis descriptor circuits, from 28 qubits,
  are beyond the budget with their estimate recorded. `CLAUDE.md` corrected; Ch. 7 and §8.1 quote
  the frontier by key.
- [ ] **Trust threshold wording.** The code trusts a gap ratio of *at least* 20; `CLAUDE.md` says
  "above 20". Immaterial; align `CLAUDE.md` to the code.

**Derived keys to export (`pihm/tools/thesis/derived.py`).** *2026-10-14:* every `\prov` in the
thesis is now a key: per-query gates and ancilla (`query/`), R7's chain ratio, the fold norms, ρ and
the truncation errors (`panel/`), the synthetic filter range, both encodings of G (`derivative-circuit/`),
the reference's accuracy, and App. D's probes (p9b–p22) ported as code-only keys, cached by source digest.

- [ ] Worst minimax `filtered_agreement` over every T1 record (C-08; §7.5 quotes one record).
- [x] Minimax/QITE degree ratio at equal suppression (B-17; replaces the `\prov` above).
- [ ] Worst `phases_max_error` over the records (B-16; App. F states it qualitatively).
- [x] The iterative reference's drift check against the dense SVD on R2a, n = 8–10 (App. G,
  qualitative). *Resolved 2026-10-14:* `iterative/R2a/standard/drift`.
- [ ] Per-atom exact errors over n (App. G's per-atom table).
- [ ] The worst exact-mode error over all records (C-03; App. F quotes the record that attains it in
  the pre-P8 export).

---

## 3. Contributions, questions, spine and vocabulary

### 3.1 The contributions (answered through the three questions in §10.1, without contribution labels; v3.15: no verdict for each contribution)

**Headline.**

> **C. The descriptor reformulation.** Replacing the dense differentiation matrix by its banded
> factors, carried as derivative blocks for higher-order equations and as a mass form for
> first-order equations and systems, turns the physics-informed residual from dense to banded *with
> exactly the same kernel*. Its Hamiltonian has ‖H_desc‖ = Θ(N²) against the standard form's
> Θ(N^{4k}); its block encoding is one flat LCU with ⌈log₂(n+4)⌉ + 8 ancilla for R2's system rows and
> α/‖A_desc‖ → 1 on regular problems. The gap the derivative blocks erode is restored on
> one axis by block rescaling without ancilla, so the filter degree is Θ̃(N) for a
> regular problem, against Θ̃(N^{2k}) for the standard form's best exact encoding. *Costs,
> volunteered:* the block register, a higher gate count per query at small n on constant-coefficient problems, a gap that still falls
> on two axes, and no remedy for a double zero. *Antecedents:* ultraspherical; first-order-system
> least squares. *Evidence:* Ch. 5, §8.2–8.3; claims C-05, C-06, B-01, B-02, B-04–B-06, B-21.

**Supporting.**

> **S1. The standard form, specified and validated.** Wu et al.'s construction, in which the state
> holds the field alone and every derivative is eliminated through G, stated once and completely, in the form every later chapter runs (answer-independent except its constraint points and the heat panel's initial function at t = −1, set up from the reference solution and said so): exact
> constraint points, Chebyshev sources, datum slices for initial and boundary functions, the R3c/R3d
> substitution, any number of axes and the stacked residual, each departure argued where it occurs
> and collected in Table T10. The departures change the data, never G or the Gram structure, so the
> baseline has the paper's cost and better accuracy. Its paper-faithful variant reproduces the
> printed scale factors of all eleven ODE panels to within one unit of the last printed digit; the
> PDE and nonlinear panels, which do not reproduce, are documented with the hypotheses tested.
> *Evidence:* §4.1–4.4, Table T10, Appendix I; claims A-01–A-05, A-09, A-11, A-13, C-07.

> **S2. An exact structured encoding of the standard form.** G = R₀(2U_odd)Λ gives α_G = N(N−1)
> ≤ 2.12‖G‖₂ with O(n²) gates and n + 4 ancilla for G alone, against an α/‖G‖₂ growing like N³ for the
> paper's normalisation. For constant coefficients it bounds α_H/‖H_std‖, isolating the standard
> form's cost in its Hamiltonian; for a lifted variable coefficient it is loose. *Evidence:* §4.5–4.6,
> §8.2; claims A-07, A-12, C-01, C-02.

> **S3. A regime-independent, verified preparation pipeline.** A stacked-residual reflection V with
> Π V Π = 2H/α_R² − I and a controlled V that needs only controlled reflections; GQSP with the
> minimax edge filter, chosen over imaginary time by a study in both forms; a priori parameters and
> answer-independent initial states; operator verification in three modes and state-preparation
> verification in three tiers, the exact emulation proven, and measured, equal to the circuit
> (≤ 1e-10); a certified-estimate iterative reference to half a million columns. *Evidence:* Ch. 7,
> §8.1; claims C-03, C-04, C-08, B-13, B-16, B-17, B-24.

> **S4. Beyond a single real field: systems, complex fields and nonlinearity.** Several coupled
> fields share one state in both forms (the descriptor's mass form), their vector data enter as
> ratio rows and their coupling is a sum of matchings on a circuit; a complex-valued linear equation
> is carried by realification as a coupled real system, because H = R†R stays Hermitian (R7 is
> z′ = −iπz realified), and the one native complex encoding built, the tensor layout's coupling, is
> verified. For nonlinearity, the paper's doubled space encodes exactly but leaves a kernel of
> dimension at least 2^{2n−1}, so it only projects; the Carleman lift, itself a coupled linear
> system, gives a one-dimensional near-kernel, a genuine preparation, in *both* forms; its
> convergence is measured (a/ν, not ρ, decides it), and a trusted kernel is shown not to certify a
> converged lift. The descriptor's time axis lowers the degree, in every Navier–Stokes pair
> compared. The pipeline reaches 2-D incompressible Navier–Stokes on 12–80 modes, and a
> tensor-layout coupling of 2K − 1 terms to 316 modes. *Costs, volunteered:* realification doubles
> the field count; native complex preparation is not built. *Evidence:* Ch. 6, §8.4–8.5;
> claims A-10, B-12, B-18, B-19, B-22, C-09, C-10.

**Rules for the list.** One sentence of *what*, one clause of *evidence*. The headline is listed
first and carries its costs and antecedents. S1 is a specification and a validation, not a
rivalry: it never reads as "we fixed the paper". S2 serves the comparison, never as a rival solver.

### 3.2 The three questions (the narrative's spine)

Wu et al.'s Discussion names two open problems: "studying the spectral gap dependence is an important
question for the future work", and "the cost of differentiation" as a guide to choosing the basis.
The critical assessment of Chapter 3 turns them into three questions, and every later chapter
answers one.

| question | answered (formulation) | evidenced (results) |
|---|---|---|
| (i) *How does the query count grow with the resolution, and how much of that growth belongs to the encoder and how much to the Hamiltonian?* | Ch. 4 (§4.5–4.6) | §8.2 |
| (ii) *Can the residual be reformulated so that its Hamiltonian is banded and well conditioned without changing its solution, and what does the reformulation cost?* | Ch. 5 | §8.2–8.3 |
| (iii) *Can nonlinear equations be prepared rather than projected, and does the reformulation's advantage survive there?* (with its prerequisite, the paper's scope: several fields, complex-valued fields, §6.1–6.3; v3.5, `StructuralReview.md` F5: the second half ties Q(iii) to the spine, answered in §6.8 through the time axis) | Ch. 6 | §8.4–8.5 |
| (how the answers are tested) | Ch. 7 | §8.1 |

Chapters open and close by §3.5 rule 1 (v3.6): a formulation chapter arrives at its question from
the tension the previous chapter left, states it in italics within its opening paragraph, and closes
on a hand-off (what it settled, what it leaves open, and where that is taken up, the results section
included). Ch. 4 first states the object its question is about (the standard
form, §4.1–4.4) and then answers it (§4.5–4.6). Ch. 6 opens with the scope the paper leaves (one
real scalar field; its Discussion's remark on complex-valued states; a doubled space for quadratic
terms) and with Q(iii); it builds the coupled linear system first (§6.1–6.3), because the Carleman
lift that answers Q(iii) is one (§6.5).

**The threads (v3.6).** Openings and closings carry the questions through two threads, named in each
chapter's own terms rather than by question number.

1. *The degree's two terms.* Wu et al.'s two open problems, the gap's behaviour and the cost of
   differentiation, are the denominator and (on the thesis's reading, argued in §3.5) the numerator
   of d = Θ(√(α_H/Δ) log 1/ε). Ch. 2: every route pays a ratio its discretisation fixes. Ch. 3: the
   assessment reduces to the two terms; Wu et al. measure the cost of differentiation by depth, but
   it is also paid in the norm, at every query. Ch. 4: the numerator splits into the encoder's cost
   and the Hamiltonian's; the latter is the cost of differentiation, paid in queries. Ch. 5: the
   numerator falls; the denominator erodes, and is restored on one axis. Ch. 6: the denominator at
   zero (a degenerate kernel projects); a lift with a unique ground state. Ch. 7: both terms
   measured on equal terms. Ch. 8: the degrees measured, in the order the predictions depend on one
   another. Ch. 9: the mechanism.
2. *What is prepared.* A unique ground state (Chs 3, 6); a trusted kernel (Chs 4, 7); the same
   kernel in both forms (Ch. 5); a trusted kernel that is not a converged lift (Chs 6, 8).

### 3.3 The spine sentence

> *Carrying the intermediate derivatives instead of eliminating them turns the physics-informed
> residual from dense to banded with its kernel unchanged, so the Hamiltonian's norm falls from
> Θ(N⁸) to Θ(N²) for a second-order equation; the price is a block register and a gap the
> derivative blocks erode, which block rescaling restores on one axis without ancilla.*

Place it, lightly reworded each time, in: the Abstract; the close of §1.1's first paragraph (the principal contribution); the close of §3.5 (as the
question it answers); §5.1; §5.8; §8.6; Ch. 10's close.

### 3.4 Controlled vocabulary

| use | never | note |
|---|---|---|
| standard form | "the paper's regime", "the paper's method" or "the method" (bare) for it; "collocation" or "state-space" for it; "our standard-form solver" | "constraint points" for x_z, x_m, x_s; "collocation" stays for the classical method (§2.3) and Childs & Liu |
| descriptor form; its chain and mass form | "our method" alone, "sparse method" | T-22 |
| block rescaling | equilibration, preconditioning (of the circuit) | general equilibration costs Θ(P) gates and is excluded |
| structured (exact) encoding | "our standard-form method", "improved Wu" | S2, a fairness device |
| the paper's encoding (of G) | FABLE, "dense encoding", "naive", "published" in visible prose (§14.2 item 8) | Wu et al.'s Figs 2, 8 and 9; `published` survives only in labels and keys |
| the encoder's cost; the Hamiltonian's cost | "encoder wall", "Hamiltonian wall" | defined once, in Ch. 4's opening |
| ideal-encoding bound (α = ‖R‖) | "best possible" | T-25 |
| minimax edge filter; imaginary-time (QITE) filter | "the filter" when it matters which | T-23 |
| prepared | "found", "solved" (for a filter's output) | only for a one-dimensional (near-)kernel |
| projected | "prepared" (for the doubled space) | R6 |
| trusted kernel | "converged", "correct" | trust is the kernel's isolation, not the lift's convergence |
| verified (exact / probe / IR) | "checked", "tested", "passes" | name the mode and the tolerance |
| circuit simulation (T1) | "run on a quantum computer", "executed" | the Aer statevector |
| exact emulation (T2) | "simulated" | provably equal to T1's post-selected output |
| resource estimate (T3) | "predicted to work" | |
| beyond the simulation budget (estimate quoted) | "failed", "too big", "infeasible" alone | |
| R2a; R2a as printed (paper-faithful) | "corrected R2a", "wrong/fixed version" | "as printed" as a variant name only in App. I and §4.4's validation paragraph (T-27) |
| the standard form takes / replaces / imposes …; "the printed point", "the paper's source" | "we fixed", "corrections", "bug", "the passage" | each departure named by the defect it removes and the property it gains (plan §3.5 rule 7) |
| several fields; a (coupled) system; the field register | "vector-valued solver", "multi-field method" | Ch. 6 |
| ratio row | "vector boundary condition" | pins the direction of vector data, leaves its scale free |
| sum of matchings | "sparse oracle" | Γ split by edge colouring (Ch. 6) |
| realification; complex-valued field | "complex solver", "handles complex equations" (unscoped) | T-32: native complex preparation is not built |
| benchmark problem R1–R10 | rung, case N | T-10 |
| a priori parameters | "tuned", "chosen" | never against the answer; only the filter's parameters (edge, α_R, ε) and the infidelity bound they give |
| block rescaling; the block weight ζ (`eq:zeta-rule`) | "a priori rule", "calibrated rule", any other name for the ζ rule | v3.16: the rule takes no term; its two constants were selected by calibration on the benchmark problems and held fixed (§5.4, App. D) |
| regular problem; singular problem (`def:regular`) | "a one-axis ODE whose leading coefficient does not vanish" restated as a scope; "well-behaved", "nice"; "regular" for a two-axis problem or for a coefficient condition alone | one axis only; regular bundles all of `thm:flat-gap`'s hypotheses; "regular datum" (the collapse row's value) is unrelated and keeps its name; x_s is the *datum point*, never "regular point", which in ODE theory means a_k(x) ≠ 0 (R3's x_s = 1 is a singular point of Legendre's equation) |

**Naming the forms (T-37).** The standard form is defined by its own construction, never by the
paper: *the state holds the field alone, and every derivative is eliminated through the dense
differentiation matrix G, so f⁽ʲ⁾ acts as Gʲ and the equation is one block of a stacked residual.* The
descriptor form is its counterpart (the state carries the derivatives as unknowns, tied by banded
factors). Neither definition mentions the paper. Wu et al. are cited where a piece is restated; the
printed method and "as printed" name the paper's choices where a departure is argued (Ch. 4, T10,
App. I); "the paper's" qualifies only things that are the paper's (its encoding, circuits, equations,
figures, data). **Full explanation once, at the first use in each chapter; later uses name the
standard form without re-explaining it.** Scope a claim by a mathematical condition (constant
coefficients, order k, one axis), not by "the paper's regime".

**Naming the class of problem (v3.11).** A descriptor degree, gap or α claim is scoped by the class
of `def:regular` (§5.3), never by restating its hypotheses: *on a regular problem*, *on singular
problems*, *on two axes*. The Definition carries the full hypotheses; a theorem or proposition cites
it ("the chain of a regular second-order problem"), so its statement stays self-contained by
reference. Before §5.3 (the Chapter 2 table, Chapter 3's critique, Chapter 4's uniqueness lemma) the
condition is stated in words, and the lemma keeps its own weaker hypothesis (a_k without zeros,
nothing on the data). After Chapter 5, the first use in a chapter carries a `\Cref{def:regular}`; a
caption that names a class glosses it ("one axis, the leading coefficient without and with a zero on
[−1, 1]"); the Abstract, §1 and §10 gloss it in a clause. Describing a particular equation's
coefficient ("R3a, whose leading coefficient vanishes at both ends"), a mechanism ("where a_k vanishes
the recovery of the top block fails") or the ζ rule's implemented test is not a scope and keeps
its words.

### 3.5 A scientific argument, not a code map

The rubric scores a model a reader could rebuild, not a tour of the software. Rules:

1. **Every chapter arrives at its question and closes on a hand-off** (v3.6, after Green's
   exemplar). The opening starts from the tension the previous chapter left and reaches the question,
   in italics, within its first paragraph; it carries no section-by-section roadmap (no list of
   `\Cref`s), which lives once, in §1.2. The closing states what the chapter settled and what it
   leaves open, in the threads' terms (§3.2), and names where that is taken up. No sentence only
   announces the next; no chapter opens with "this chapter describes the module…" or with its
   question quoted back. Ch. 3's first sentence stays its attribution (T-13).
2. **State constructions as mathematics.** `assemble`, `stacked_reflection`, `t2` and their
   relatives appear in the body only in §7.9 and the figure-script comments; elsewhere they are the
   residual, the reflection V, the exact emulation.
3. **Findings, not history.** Decisions, issues, Journal entries, probes, failed runs and gates are
   never cited. A finding that came from an issue is stated as a finding ("the descriptor's gap
   closes on singular problems"), with its evidence in a figure or appendix. A
   design choice is justified by its reason, never by "we decided".
4. **Records, hashes, campaigns, digests and Slurm** live in Appendix J. The body says "every number
   is regenerated from the archived records by one command (Appendix J)".
5. **The physics stays in view.** Each benchmark problem is introduced by its equation and the
   capability it tests or the physics it carries (stiffness, a singular leading coefficient, a heat
   equation, a vortex pair), never by its campaign.
6. **Negative results are findings**, numbered with the positive ones (the rubric protects them when
   analysed).
7. **Chapter 4's departures are arguments, not a changelog.** Each departure, inline and in Table
   T10, names a mathematical defect of the printed choice (answer-dependent data, an error floor, an
   ill-posed problem, a branch point, an approximate encoding) and the property its replacement
   gains; none says when or why *we* changed it, and none cites an issue or decision.

### 3.6 Paper-shaped material (light note, T-04)

Chs 4–5, §8.2–8.3 and §9.1–9.2 form a self-contained article ("a banded reformulation of
physics-informed effective Hamiltonians"), with Ch. 4 as its baseline section, and the Carleman
results a second paper. Nothing in the plan depends on this.

---

## 4. Page budget, LaTeX tree and scaffold conventions

### 4.1 Page budget (Modelling scale)

| chapter | pp | criterion |
|---|---|---|
| 1 Introduction | 3 | Intro & Lit /20 |
| 2 Background and Literature Review | 7 | Intro & Lit /20 |
| 3 The PIHM method (prior art, judged) | 4 | Intro & Lit /20 (HD gate: critical assessment) |
| 4 The standard form and where its cost lies | 7.5 | Model Formulation /30 |
| 5 The descriptor reformulation | 10.5 | Model Formulation /30 (core) |
| 6 Beyond a single real field: systems, complex fields and nonlinearity | 6.5 | Model Formulation /30 |
| 7 Preparing and verifying the ground state | 6 | Model Formulation /30 |
| 8 Numerical study | 10 | Results & Discussion /30 |
| 9 Discussion | 3 | Results & Discussion /30 |
| 10 Conclusions and future work | 2 | Conclusions /10 |
| **total** | **59.5** | |

*v3.4 (`StructuralReview.md` §1):* the budget revised to what the drafted chapters can reach; it
leaves no slack under the cap of 60.

**Why this split.** Formulation (Chapters 4–7, 30.5 pages) must let a reader "create equivalent
models", so the model is stated once in Ch. 4, and configuration, inputs and software have body
space in Chapter 7, with the detail in Appendices A–G and J. Results & Discussion (Chapters 8–9,
13 pages) carry the evidence and the insight; the audit of the source paper is evidence about the
paper, not about the thesis's questions, so it is in Appendix I (T-36). Half a page of slack remains
under the cap.

**Trim order if over budget:** (v3.4's pass, `StructuralReview.md` F1–F3, executed 2026-10-12; F6's tables for Ch. 8 next); §2.1 first; (Chapter 7's three candidates, the F2 placeholder, §7.2's iterative-reference detail and `tab:run-inputs`, were executed 2026-10-12); then §8.3's third representative problem (to Appendix
J); then §7.9 and §7.8 to their minimum; then §4.5.1 to its verdict (the rebuild's prose to
Appendix I); then §4.5.3's gate table to Appendix C; then §6.6's matchings to one paragraph (their
construction to Appendix E); then §3.3 to its claims only. Chapter 5 is cut last. The page budget is
enforced in Review Mode only (`CLAUDE.md`).

### 4.2 LaTeX section tree

```latex
% 2_body/1_introduction.tex  (~3 pp)
\section{Introduction}                                        % sec:intro
  % opening, no heading (v3.13): target, the method, the cost left open, the number
  \subsection{Contributions and Scope}                         % sec:contributions; spine sentence
  \subsection{Outline}                                         % sec:outline; the only roadmap

% 2_body/2_literature.tex  (~7 pp; v3.5)
\section{Background and Literature Review}                    % sec:background
  % opening, no heading
  \subsection{Quantum Computation Preliminaries}               % sec:bg-qc; <= 1 p, prose
  \subsection{Quantum Algorithms for Differential Equations}   % sec:bg-de
      % titled \paragraphs (2026-10-15): linear systems; Hamiltonian simulation and
      %   Schroedingerisation; variational; ground-state preparation; critical assessment
      %   (T1, one row per route, no PIHM or "this work" row)
  \subsection{Classical Discretisation and Linearisation}     % sec:bg-spectral
      \subsubsection{Chebyshev Discretisation and Differentiation}
      \subsubsection{The Ultraspherical Method}
      \subsubsection{First-Order System Least Squares}        % + the increment
      \subsubsection{Fourier--Galerkin Truncation}
      \subsubsection{Carleman Linearisation}                   % sec:bg-carleman (moved from §2.2)
  \subsection{Block Encodings, Signal Processing and Filtering} % sec:bg-primitives
      \subsubsection{Block Encodings and Linear Combinations of Unitaries}  % def:block-encoding
      \subsubsection{Quantum Signal Processing}
      \subsubsection{Ground-State Preparation by Filtering}    % eq:degree; readout paragraph
  \subsection{Synthesis}

% 2_body/3_pihm.tex  (~4 pp)  PRIOR ART, judged (T-13)
\section{The Physics-Informed Effective Hamiltonian Method}   % sec:pihm
  % opening, no heading
  \subsection{The Chebyshev Latent-Space Model}                % sec:pihm-model
  \subsection{Hamiltonian Construction}                        % sec:pihm-residual
  \subsection{Circuits, Filtering and Readout}                 % sec:pihm-encoding
  \subsection{Doubled-Space Extension to Nonlinearity}         % sec:pihm-doubled
  \subsection{Critical Assessment}                             % sec:pihm-assessment; poses Q(i)-(iii)

% 2_body/4_standard.tex  (~7.5 pp)  (T-30)
\section{The Standard Form and Its Cost}           % sec:standard
  % opening, no heading
  \subsection{The Model}                                       % sec:standard-model; eq:eta-e
  \subsection{Differentiation and Multiplication}              % sec:standard-operators
  \subsection{Constraints and Data}                            % sec:standard-constraints
  \subsection{The Standard Form}                               % sec:standard-form; def:standard-form; T10
  \subsection{Encoding the Derivative}                         % sec:standard-factorisation
      \subsubsection{The Paper's Encoding}                     % sec:standard-published
      \subsubsection{An Exact Factorisation}                   % sec:standard-exact; prop:G-factorisation
      \subsubsection{Circuits and Cost}                        % sec:standard-cost; F3
  \subsection{The Standard-Form Hamiltonian}     % sec:standard-hamiltonian

% 2_body/5_descriptor.tex  (~10.5 pp)  THE CORE
\section{The Descriptor Reformulation}                        % sec:descriptor
  % opening, no heading: the standard form by its state; its cost in the operator; Q(ii)
  \subsection{The Banded Factorisation}  % sec:descriptor-construction; the idea, antecedents, F4 (v3.9 merge)
  \subsection{The Descriptor Residual and Its Kernel}  % sec:descriptor-layouts; chain | mass form | constraints (sec:descriptor-constraints) | theorem | several axes (v3.10 merge)
  \subsection{The Descriptor's Gap}                 % the challenge (T-21); def:regular; thm:flat-gap
  \subsection{Block Rescaling}                                 % the cure and its limits
  \subsection{The Block Encoding} % F5 (algorithm in App. D, v3.8)
  \subsection{Cost of the Descriptor Encoding}                 % proposition
  \subsection{Consequences for the Spectrum and the Filter}
  \subsection{Summary}

% 2_body/6_extensions.tex  (~6.5 pp)  (T-31, T-32; v3.1 merges v3.0's Chs 6 and 7)
\section{Systems and Nonlinearity}   % sec:extensions
  % opening, no heading: the paper's scope; Q(iii); the thread (one state, a coupled linear system)
  \subsection{Several Fields on One State}                     % sec:systems-fields; time axis; mass form applied
  \subsection{Data for Several Fields: Ratio Rows}             % sec:systems-data
  \subsection{Complex-Valued Equations}                           % sec:systems-complex; T-32
  \subsection{The Doubled Space}  % sec:doubled-space; prop:no-penalty
  \subsection{The Carleman Lift in Space--Time}                % sec:carleman; the lift as a §6.1 system
  \subsection{Couplings and Products on a Circuit}             % sec:ext-circuits; matchings, tensor layout, folds
  \subsection{Burgers and Navier--Stokes}  % sec:fluids
  \subsection{Preparation Versus Projection}                   % sec:prep-vs-proj; T8; answers Q(iii)

% 2_body/7_pipeline.tex  (~6 pp)
\section{Preparing and Verifying the Ground State}            % sec:pipeline
  % opening, no heading: why a predicted ratio needs one pipeline to become a comparison (v3.6), the pipeline in one paragraph, F1. With no
  % "Overview" heading, this plan's §7.2-7.9 are the thesis's §7.1-7.8.
  \subsection{Problems and Model Inputs}                       % T3 ladder by pointer (in §4.1, v3.5)
  \subsection{The Classical Reference}                         % Wedin's bound
  \subsection{Block Encoding and the Quantum Walk}
  \subsection{The Filter and Its Parameters}
  \subsection{Verification and the Error Budget}               % T4
  \subsection{Reading Out the Solution}
  \subsection{Design of the Numerical Experiment}              % cost conventions, fairness
  \subsection{Software and Computation}

% 2_body/8_results.tex  (~10 pp)
\section{Numerical Study}                                     % sec:results
  \subsection{Validation of the Pipeline}                        % sec:results-faithful; S1 validation, S3: F7, F8
  \subsection{The Cost of the Two Forms}                             % sec:results-scaling; Q(i),(ii): F9, T7, tab:growth
  \subsection{The Descriptor's Gap and Its Rescaling}          % sec:results-gap; F11, F12
  \subsection{Systems and Nonlinear Problems}                  % sec:results-nonlinear; F13
  \subsection{Two-Dimensional Navier--Stokes}      % sec:results-ns; F14
  \subsection{Summary of Findings}                             % sec:results-summary; >= 2 negative

% 2_body/9_discussion.tex  (~3 pp)
\section{Discussion}                                          % sec:discussion
  \subsection{The Descriptor Form: Advantages and Costs}
  \subsection{End-to-End Complexity}
  \subsection{Where the Construction Applies}                  % T9 applicability
  \subsection{Feasibility on Fault-Tolerant Hardware}
  \subsection{Limitations}

% 2_body/10_conclusions.tex  (~2 pp)
\section{Conclusions and Future Work}                         % sec:conclusions
  \subsection{Conclusions}                                     % sec:conclusions-answers (v3.17)
  \subsection{Future Work}                                     % sec:future-work; bold run-in leads
```

### 4.3 Scaffold conventions

`main.tex` holds each chapter's `\section` and label and inputs the body files;
`3_footer/appendices.tex` does the same for `A_gates.tex` … `M_proposal.tex`. Every subsection has
a label. Comment tags: PURPOSE, CRITERION, SOURCES, WRITE WHEN, LAND, FIG, TAB, OFFLOAD, CHECKLIST,
TRAPS, REVISE, CITE-NEEDED. Macros in `1_header/0_packages.tex`: `\G`, `\Bt`, `\Dt`, `\M`,
`\nfold`, `\Brow`, `\Dzero`, `\Ucg`, `\Uodd`, `\Astd`, `\Adesc`, `\Hstd`, `\Hdesc`, `\fhat{j}`,
`\prov{…}`; numbers by `\res` (plan §10.2). Placeholders: `\placeholderfigure`; tables with final
columns; propositions with `% STATE:` and proofs in appendices.

**Labels follow the content they name.** An equation that moves keeps its label
(`eq:pihm-G-entries` in Ch. 4 is still that equation); a section whose role ends loses its label,
and every `\Cref` to it is retargeted in the same edit. A compile with zero undefined references
closes every structural change.

**Aligning the rest of the scaffold to this plan** (structural only, no prose drafted; the status
board tracks it): Ch. 8 loses its reproduction section, whose table (`tab:eta-reproduction`, T6)
and figure (`fig:faithful-vs-corrected`, F6) move to Appendix I with their labels, and §8.1 gains
its validation paragraph's LAND; Ch. 9 loses its reproduction section; Ch. 7's §7.3 LAND gains
Wedin's bound; Appendices B, I, G and I take the items of plan §6. *Done 2026-10-12:* the
Ch. 8 and Ch. 9 moves; the rest of Appendix I's audit is still open.

---

## 5. Chapter by chapter

Each entry gives the purpose, the rubric criterion, the sources, the scaffold (what each subsection
must land, in order, with its page share), figures and tables, appendix offloads, the marker's
checklist and the traps. `pihm` paths are relative to `Code/pihm/`; "nb NN" is a notebook of
Planning.md §10.8.

*v3.4 (`StructuralReview.md` F1–F3).* Where an entry below lists, for Chs 4–7, a filter degree, a
gate count, a preparation or any tier-labelled number, it now lives in Ch. 8 (T-20's evidence
rule). Where it lists the argument of a departure in §4.1–4.3, the argument and its numbers now
live in App. B or I and the body keeps one clause (T-30). Where it places a table or proposition
in Ch. 7 that v3.4 moved (`tab:constraint-kinds` → App. H, `tab:verification-modes` → App. G,
`prop:filter-normalisation` → App. F), the appendix holds it. The `.tex` scaffolds carry the
current LAND lists.

---

### 5.1 Chapter 1: Introduction (3 pp; Intro & Lit /20)

**Purpose.** Establish that quantum differential-equation solvers matter, that the physics-informed
Hamiltonian route has a *located* cost problem its authors left open, and what this thesis
contributes and does not.

**Criterion.** "Comprehensive, superior understanding… with **excellent connection of the current
field to the project**". The introduction converges; it does not survey.

**Form (v3.13, 2026-10-14).** An unheaded opening and two subsections, after Snow's three-part
introduction (motivation, contributions, outline) and Green's unheaded first page, under the
opening convention of §3.5 rule 1. v3.12's four subsections are reduced to two because their
first two were one argument split in half: §1.1 surveyed the algorithm families that Ch. 2 already
judges, and §1.2 then had to restart from Wu et al. The opening now runs target → method → the cost
left open → the number without a break, and §10.1 answers it (v3.17), so the
thesis opens on the tension and closes on its resolution. Dropped: the family-by-family sentences (Ch. 2's job; one sentence
of its thread stays), concept figure F0 (the number does its work, and `tab:headline` carries it in
Ch. 8), and an italic list of the three questions (stated formally once, in §3.5; the opening
names them in one prose sentence). The prose carries no internal labels (C, S1–S4, Q(i)–(iii)) and
no run-in headings.

**Scaffold.**

0. **Opening, no heading (1.5 pp), four paragraphs.**
   - *The target (0.3 p).* Applications (fluids, fields, finance; CITE-NEEDED, none in `ref.bib`);
     why quantum algorithms are proposed; output a state; cost = queries × gates per query on a
     register of qubits, fault-tolerant frame. Ch. 2's thread in one sentence (every route pays a
     ratio its discretisation fixes). The thesis compares quantum formulations with one another and
     claims no classical advantage.
   - *The method (0.35 p).* Wu et al. attributed at first mention, lineage in one clause
     (differentiable quantum circuits → Chebyshev latent space and lifts → the PIHM); the idea in
     three sentences; their poly(n)-gates-per-term claim.
   - *The cost left open (0.45 p).* One query against the number of queries; the degree law inline
     (the labelled `eq:degree` is Ch. 2's); Wu et al.'s two open problems quoted, as the degree's
     denominator and, on our reading, its numerator; the thesis's questions in one prose sentence,
     worded as §10.1's answers (what sets the number of queries; whether changing the residual
     rather than the circuit lowers it without changing the solution; whether that survives
     nonlinear equations, where the paper's construction projects).
   - *The number (0.4 p; before the end of page 2).* R2a at n = 8, minimax edge filter, resource
     estimates (T3, named), **as built and at the ideal bound** (T-25):
     `\res{stateprep/R2a/standard/n8/T3/filter=minimax/encoder=published}{degree}` (Wu et al.'s
     encoding), `\res{stateprep/R2a/standard/n8/T3/filter=minimax}{degree}` (structured) and its
     `{ideal_degree}`, `\res{stateprep/R2a/descriptor/n8/T3/filter=minimax}{degree}` and its
     `{ideal_degree}`. Read as the encoder's cost (removable by an exact encoding) and the
     Hamiltonian's cost (removable only by a different Hamiltonian with the same kernel). Scoped:
     R2a is a regular problem, glossed in a clause (§3.4); singular and two-axis problems gain less
     or reverse.
1. **§1.1 Contributions and Scope (1.1 pp; `sec:contributions`).**
   - *The principal contribution, one paragraph:* the descriptor reformulation (§3.1's C), its
     antecedents credited in the same paragraph, its costs volunteered (block register; gates per
     query at the sizes built on constant-coefficient problems; about N² on singular problems and
     the R3 reversal at the ideal bound; the gap on two axes and the heat reversal; the double
     zero), closing on the spine sentence (§3.3).
   - *Four supporting contributions, an enumerate in chapter order* (S1, S2, S4, S3), one or two
     sentences of what and one pointer of evidence each, no labels or bold run-in titles; S2 phrased
     as serving the comparison.
   - **The scope, once, plainly:** every result is a classical computation: circuit simulation (T1)
     to 20 qubits, exact emulation (T2, provably equal to the circuit's post-selected output) to
     degree 2²⁰, resource estimates (T3) beyond. Nothing ran on hardware. The field is read out
     classically from the prepared state; the interferometric protocol is built at small n and is
     further work. The spectral edge comes from the classical reference.
   - **What is not claimed** (one short prose paragraph): a poly-log end-to-end cost; an advantage
     over classical solvers; a floor for every algorithm (polynomial filters of the walk only, Lin &
     Tong's hedge); preparation from a degenerate formulation; native complex preparation
     (realification only, T-32); a converged lift certified by its kernel.
2. **§1.2 Outline (0.4 pp; `sec:outline`).** One paragraph of prose, each chapter by its heading
   verbatim and its job in a clause: Ch. 3 as reviewed prior art closing on the three questions;
   Ch. 4 the standard form, stated once, and where its cost lies; Ch. 5 the descriptor; Ch. 6 the
   step from one real field to coupled, complex-valued and nonlinear ones; Ch. 7 how the answers are
   tested; Ch. 8 the evidence; Chs 9–10 the mechanism, limits and further work; one sentence for
   the appendices (B–I apparatus, J catalogue, K reproduction and audit, L records, M proposal).
   The thesis's only roadmap (§3.5 rule 1).

**Marker checklist.** A non-specialist physicist can state the problem after the opening; a number
on or before page 2, as built and at the ideal bound; every contribution falsifiable with its
evidence; the scope explicit, tiers and "no hardware" included; Wu et al. attributed at first
mention; the outline matches the headings verbatim; every promise is answered in §10.1, and nothing
more is promised.

**Traps.** A survey of algorithm families; leading with the descriptor before the reader knows the
baseline; claiming a speed-up; listing S2 as a rival method; an unscoped descriptor claim; "the
readout protocol was reproduced"; the three questions as an italic list.

---

### 5.2 Chapter 2: Background and Literature Review (7 pp; Intro & Lit /20)

*v3.5 (2026-10-12, `StructuralReview.md` F4): restructured to five sections and drafted in full
(first pass). The old §§2.4–2.7 are one section around `eq:degree`; the preliminaries are prose.
Measured at about 10.7 pp; after the density rewrite of 2026-10-13 (5,300 → 4,270 words of source, no claim dropped) about 9.1 pp. The ranked cut list below still applies, its savings now somewhat smaller.*

**Purpose.** Command of the state of the art and its history, **judged**, and organised around the
thesis's own question: *what does each route's cost run through?* Only the prior art that Chapters
3–7 build on, each family with its failure mode.

**Criterion.** "Comprehensive, superior understanding of the **historical background** and state of
the art" with "**excellent connection of the current field to the project**"; "a **critical
assessment** of the strengths and weaknesses of the material reviewed is required for a high
distinction".

**The thread (what makes it a review rather than a survey).** Every quantum route to a differential
equation pays a ratio of scales that its discretisation fixes: κ for linear systems, ‖A‖T for
propagators, R for a Carleman lift, the encoded operator's norm against its gap for a ground-state
route. Spectral numerical analysis learned how a discretisation sets that ratio and how to lower it
(banded bases; first-order least squares). The quantum primitives say how the ratio becomes a query
count (`eq:degree`). The PIHM sits where the three meet, and its authors left its ratio unanalysed.

**Scaffold (as drafted).**

0. **Opening (0.2 p).** The ratio every route pays, which its discretisation fixes (the thread);
   the three bodies of work it is followed through; how the chapter judges (assumes, cost, returns,
   fails). No section roadmap (v3.6).
1. **§2.1 Quantum computation preliminaries (≤ 1 p, prose only).** Amplitude encoding and its two
   consequences (the norm carried separately, which is η; access only by measurement); ancilla and
   post-selection; queries × gates per query, and qubits; the tilde convention; the fault-tolerant
   frame, NISQ in one paragraph (Preskill 2018). No definitions: the block encoding is §2.4's.
2. **§2.2 Quantum algorithms for differential equations (2.6 p).** *Revised 2026-10-15 (the
   author's instruction): no subsubsections; one titled paragraph per route, each introducing the
   route, then its strengths, then its weaknesses: linear systems (a); Hamiltonian simulation,
   LCHS and Schrödingerisation (new, from (a)); variational (c); ground-state preparation (d,
   ending in one sentence placing the PIHM in the route, no PIHM lineage or review); critical
   assessment (e). Carleman (b) moved to §2.3 (`sec:bg-carleman`): a classical linearisation that
   composes with a route, not a route. Paine 2026 moved to §3.5's open problems. T1 has one row
   per route and no PIHM or this-work row. The items below are the pre-revision scaffold, kept
   for their content.*
   - (a) *Linear systems.* HHL (cost; the κ^{1−δ} bound) → Berry 2014 (multistep, poly 1/ε) →
     Berry et al. 2017 (Taylor, polylog) → Childs & Liu 2020 (Chebyshev collocation in time: dense;
     κ bounded by a degree-3.5 polynomial in the nodes) → Childs, Liu & Ostrander 2021 (PDEs) →
     Costa et al. 2022 (O(κ log 1/ε), optimal); LCHS; Schrödingerisation; Jennings et al. 2024
     (explicit counts; history state in O(T^{1/2})). **The ODE solvers take first-order systems**
     (the FOSLS point of §2.3). Judged: Aaronson's fine print; Montanaro & Pallister (at most
     polynomial at fixed dimension); κ grows with the resolution.
   - (b) *Nonlinear.* Leyton & Osborne (exponential in time) → Carleman → Liu et al. (R < 1;
     T²q/ε; intractable for R ≥ √2) → Krovi (log 1/ε; negative log-norm). R < 1 sufficient and
     worst-case; the measurement is the thesis's; dissipation must dominate; lift size M^K.
   - (c) *Variational.* Lubasch et al.; DQC (PINN loss); **ground states found variationally**:
     VQLS's H_G = A†(I − |b⟩⟨b|)A (the PIHM's Gram structure), the Feynman–Kitaev clock (Barison
     et al.) and a space–time Burgers ground state (Pool et al.). Judged: no guarantees; barren
     plateaus (McClean et al.).
   - (d) *Ground-state routes and the physics-informed lineage.* Subaşı, Somma & Orsucci; An & Lin;
     Costa; Lin & Tong's H₁ with its 1/κ gap. PINN → DQC → latent space → Wu et al. (Ch. 3) →
     Paine 2026 (what it does and does not do).
   - (e) *Critical assessment* with **Table T1** (assumes | cost runs through | returns | fails
     where), a PIHM row whose cost driver is marked as this thesis's reading, and a *this work* row
     (formulation facts only, scoped; recheck at W6). Three verdicts: each route pays a
     discretisation-fixed ratio; output is a state and gains are at most polynomial at fixed
     dimension, **so the thesis compares quantum methods with one another and claims no classical
     advantage**; guarantees are uneven.
3. **§2.3 Spectral methods and their conditioning (1.5 p).** Galerkin, tau, collocation; the PIHM
   as a least-squares relative of the tau method (never "collocation"); G dense, N² per
   derivative, tau/collocation conditioning N^{2k} (Olver & Townsend §4). **Ultraspherical:** the
   (S, D) pair, almost banded, κ linear, bounded after a diagonal preconditioner; B̃, D̃ its first
   pair; rescaling as the preconditioner; **volunteered: the full ultraspherical reduction (banded
   on N unknowns, no block register) is neither built nor compared** (App. A, §9.5). **FOSLS:**
   least squares of a second-order operator O(h⁻⁴) against O(h⁻²) (Bochev & Gunzburger 1998,
   §2.2); first-order decomposition restores O(h⁻²) and decouples the unknowns (§2.3); the standard
   form is the high-order least-squares method, the descriptor FOSLS in a spectral basis; the filter
   pays R's conditioning, not R†R's. **The increment** (kernel proof; flat LCU, O(log n) ancilla;
   the gap's erosion and block rescaling; the measured degree). Fourier–Galerkin in one
   paragraph.
4. **§2.4 Block encodings, signal processing and filtering (1.8 p; `sec:bg-primitives`).** The
   (α, m, ε) definition (`def:block-encoding`), α ≥ ‖A‖, LCU, ⌈log₂ L⌉ selectors, qubitisation;
   QSP → QSVT (parity) → mixed parity (the paper's) → GQSP; phases (complementary polynomial with
   error guarantees; inverse NLFT). **Filtering:** imaginary time, inverse iteration; Lin & Tong's
   filters are for an *interior* eigenvalue (degree ∝ α/Δ; essentially optimal in γ and Δ); at the
   *edge* of a PSD operator the square root appears (**`eq:degree`**), which is spectral gap
   amplification (Somma & Boixo 2013) realised by encoding R; the floor is a statement about
   polynomial filters only (§9.2). Overlap and amplification; readout as a closing paragraph.
5. **§2.5 Synthesis (0.2 p).** Where the PIHM sits; the hand-off to Ch. 3.

**Ranked cut list (Review Mode's to apply; the author's call).** At ≈ 10.7 pp the chapter is ≈ 3.7
over. In order, with the estimated saving: (1) §2.4's LCU mechanics and qubitisation paragraph to
App. F, keeping the definition and α ≥ ‖A‖ (0.3); (2) the readout paragraph to two sentences, T1's
"returns" column carrying the rest (0.2); (3) §2.4.2's phase-finding sentence to Ch. 7, which
already cites it (0.1); (4) §2.1's NISQ paragraph to one sentence (0.2); (5) §2.3.4 Fourier–Galerkin
to App. E's opening, one sentence kept (0.25); (6) §2.2(a)'s history compressed to one paragraph,
dropping Childs–Liu–Ostrander and the fast-forwarding detail (0.3); (7) Paine 2026 to one sentence
here, its assessment staying in §3.5 (0.1); (8) Lin & Tong's interior filters to two sentences
(0.2); (9) §2.5 merged into §2.2(e)'s close (0.2); (10) T1 at `\scriptsize` (0.15). Total ≈ 2 pp,
leaving ≈ 8.7. Reaching 7 needs either a strand removed or the budget moved: the recommendation is
to set Ch. 2 at 8.5 and take the 1.5 pp from Chs 4 and 7, which are already flagged over (§0.3);
the new material (the ground-state lineage, the edge argument behind `eq:degree`, the FOSLS
conditioning statement) is what the HD gate rewards.

**Marker checklist.** Every route has its strengths and a weakness; T1 is present, one row per
route, with no PIHM or this-work row (2026-10-15); the history is visible; ultraspherical and FOSLS credited before Ch. 5, with
the increment and the uncompared ultraspherical reduction; the concurrent work cited; §2.1 ≤ 1 p of
prose; `eq:degree` hedged (edge; polynomial filters); nothing unused; IEEE `biblatex` throughout.

**Bibliography (T-29, 2026-10-12).** Added, each checked against Crossref or arXiv and against the
claim: `berry2014highorder` (the 2014 ODE solver; `berry2014exponential` is the STOC Hamiltonian
simulation paper, not it), `childsliuostrander2021pde`, `aaronson2015fineprint`, `montanaro2016fem`,
`leyton2008nonlinear`, `mcclean2018barren`, `bravoprieto2023vqls`, `barison2022variational`,
`pool2024nonlinear`, `somma2013gap`, `lowchuang2017qsp`, `bochevgunzburger1998review`,
`preskill2018nisq`. Corrected: `subasi2019adiabatic`'s author order (Subaşı, Somma, Orsucci);
`jennings2023cost` now Quantum 8, 1553 (2024).

---

### 5.3 Chapter 3: The Physics-Informed Effective Hamiltonian Method (4 pp; Intro & Lit /20, body-located)

**Purpose.** Present Wu et al.'s method as attributed prior art, at the depth a referee needs to
follow the critique, and judge it; the judgement poses Q(i)–(iii). The construction is not built in
full here: Ch. 4 states it once, in the form the thesis runs (T-13, T-30). Ch. 3 carries the paper's
own equations only where a weakness is stated against them, in the thesis's notation. The paper's
equation numbers are not cited anywhere in the thesis: the notation differs (G for 𝔾ₙᵀ, β for t), and
the thesis stands alone; attribution is carried by naming Wu et al. and citing `wu2025pihm`.

**Criterion.** This chapter discharges the Intro & Lit HD gate, "critical assessment". Its first
sentence says it reports prior art; its last section reads as a gap statement. A marker skimming the
contents may file it under formulation, so the register must be unmistakable: "the paper", "Wu et
al.", "the authors"; "we" only in §3.5's verdicts.

**Sources.** The paper (`wu2025pihm`, arXiv:2504.13174; the PDF is in `Research/Papers/`): Eqs 1–16
(the model, 𝔾ₙᵀ, the lifts, the constraints, the Gram sum), Eqs 21–28 (sources, PDEs), Eqs 29–33
(the doubled space), Methods §1–3 (the circuits, QITE by QSVT and the time rule, the interferometric
readout), the Discussion (the open questions, the Fourier remark); Paine, Elfving & Kyriienko 2023
(the latent space and the lifts); Paine 2026 (concurrent work); companion 10, 11, 20, 21 for the
paper's conventions as `pihm` reproduces them, 31 (the circuits' claims), 42 (the time rule), 47 (the
readout), 60 (the doubled space); `docs/22_claims_register.md` A-01–A-13 for what the critique may
say; `docs/06_results_guide/81_reproduction.md` for what Appendix I shows.

**Scaffold.**

0. **Opening, no heading (0.4 p).** First sentence: the chapter presents and evaluates the method of
   Wu, Paine, Philip, Gentile and Kyriienko. The three-step move with the paper's example f″ + f = 0:
   coefficients as amplitudes, the equation and its data as operators that annihilate the state, the
   ground state of their summed Gram matrices as the solution. The lineage in one sentence
   (differentiable quantum circuits → the Chebyshev latent space). What the paper claims for the
   method, so the assessment has a target: no variational training, evaluation off any grid, poly(n)
   terms "implemented efficiently". Why the last claim must be read against the degree
   (`eq:degree`), so the assessment has a measure; Ch. 4 named as where the construction is stated
   in full (v3.6: no section roadmap).
1. **§3.1 The latent Chebyshev model (0.45 p; `sec:pihm-model`).** The quantum Chebyshev state
   |τ(x)⟩ₙ, displayed as the paper's Eq. 3 (`eq:pihm-chebyshev-feature-map`; §4.1 restates it as
   the normalised basis and adds what the thesis needs: orthogonality, η_e, the raw weight); the model
   f_Q = √η⟨τ(x)|ψ⟩ (`eq:pihm-fq`, the paper's Eq. 2) with η > 0 as the paper writes it; the paper
   discards ‖τ(x)‖ "since it can be implicitly incorporated into the scaling factor" (one clause; the
   raw τ is what the derivation then uses); η fixed after preparation from one regular datum.
2. **§3.2 The residual and its Hamiltonian (1.0 p; `sec:pihm-residual`).** As the paper builds
   them, compactly:
   - differentiation by G (printed 𝔾ₙᵀ; dense, because a single T_p differentiates into every lower
     polynomial of the other parity, cite Olver; entries in §4.2); the constant-coefficient residual
     A = Σ_j a_j G^j (`eq:pihm-A`, the paper's Eq. 15);
   - a variable coefficient or a source by the lift x^p⟨τ|ₙ = ⟨τ|ₙ₊₁ℳ_{x^p} (Eq. 5, credited to Paine
     et al.), the source as a truncated **Maclaurin** series through the collapse row 𝔻⁽⁰⁾(x_s)
     (Eqs 11–14), giving the general A (`eq:pihm-A-source`);
   - invariant data constraints 𝔹(x_z), 𝔹(x_m)G at points chosen by the authors (the printed
     points are rounded zeros and extrema of the known solution: −0.2, −0.73, 0.91, −0.75), and the
     regular datum that fixes η;
   - two variables by Kronecker products, with the PDE panels' invariant sets as printed (Laplace's
     three homogeneous sides; heat's f(t, ±1) = 0 and ∂ₓf(t, ±¾) = 0; wave's f(⅛, x) = f(⅞, x) = 0);
   - the Hamiltonian as the sum of Gram matrices, H = 𝒯(A) + Σ𝒯(𝔹_i) (`eq:pihm-hamiltonian`, the
     paper's Eq. 16), and the paper's description of it as "a real symmetric positive-definite
     matrix with distinct eigenvalues"; the physics-informed reading (a PINN-like loss, nothing
     trained). Nothing of ours in this subsection.
3. **§3.3 The paper's circuits, filter and readout (0.6 p; `sec:pihm-encoding`).** Three
   paragraphs, each the idea and the paper's claims, without our verdicts:
   - *Block encodings:* 𝔹 and 𝔻⁽⁰⁾ by the inverse feature map and a reflection (n + 2 qubits,
     "high probability"); G as an LCU loading entries as rotation amplitudes, at the prefactor
     (2ⁿ⁻¹ + 2ⁿ)‖G‖_S (`eq:pihm-published-prefactor`), 2n + 3 qubits, O(n³) gates, entry errors that
     "exponentially decrease". The registers and angles → Appendix I.
   - *The filter:* QITE by indefinite-parity QSVT on H/‖H‖_F; the time rule t ≥ λ_max/(λ₂(n − 1))
     (`eq:pihm-time-rule`), which the paper calls an approximate lower bound; its expected
     O(Δ⁻¹ polylog 1/ε) preparation time. It assumes §2.4 (v3.5). Detail → Appendix I.
   - *Readout:* the interferometric overlap measurement, two all-zero probabilities per point
     (Eqs 36–39). One paragraph; its identity in Ch. 7 and Appendix F.
4. **§3.4 The doubled-space extension (0.35 p; `sec:pihm-doubled`).** Ψ = ψ ⊗ ψ with the fold 𝒩₁
   (`eq:pihm-fold`), the linear terms tensored with 𝔻⁽⁰⁾; quadratic only (Paine 2026 notes the
   same); the paper's own count of at least 2^{2n−1} degenerate zero-energy states and its selection
   of the state that "closely matches the analytical solution". No proposition here: the argument
   that a filter can only project is §3.5's weakness, proved in §6.4 (`prop:no-penalty`).
5. **§3.5 Critical assessment (1.0 p; `sec:pihm-assessment`).**
   - **Strengths:** a unified least-squares construction for ODEs, PDEs and their data; exact
     kernels for polynomial solutions; no grid, so the model and its derivatives are available at
     every x; few terms.
   - **Weaknesses, most severe first**, each one sentence and a pointer:
     1. *the spectrum:* derivatives enter through powers of a matrix whose norm grows as N², and the
        degree takes the square root of α_H/Δ, so it pays the residual's norm ‖R‖ (N² per derivative
        eliminated through G), not the Gram product's squaring, which costs only an eigensolver on H;
        so the norm, not the circuit, may set the cost (credit Cai et al. as the classical remedy for
        high order). Stated qualitatively; the scaling Θ(N^{4k}) is Ch. 4's result
        (pointer `sec:standard-hamiltonian`), never asserted here;
     2. the prefactor of the G circuit is loose against ‖G‖ (pointer `sec:standard-published`);
     3. the printed choices (rounded constraint points, truncated Maclaurin sources) set an error
        floor at the printed n (pointer `sec:standard-constraints`, Appendix I);
     4. the PDE invariant sets omit the initial or boundary function that fixes the solution, are
        read off the known solution, and degenerate beyond the printed n; the heat panel's natural
        completion (its initial function at t = 0) would pose a backward, ill-posed problem on
        [−1, 0] (pointer `sec:standard-constraints`, Appendix I);
     5. "positive-definite with distinct eigenvalues" is stronger than a sum of Gram matrices allows
        (pointer `sec:standard-form`);
     6. the time rule contains no ε, so it cannot certify an accuracy, and needs λ_max and λ₂ in
        advance (pointer Appendix I; the thesis's filter, §7.5);
     7. the nonlinear route cannot prepare: any function of H acts as a scalar on its kernel
        (pointer `sec:doubled-space`);
     8. the readout identity assumes deterministic preparation (pointer `sec:pipeline-readout`,
        Appendix F);
     9. the construction is stated for one real scalar field, and the paper's Discussion sets
        complex-valued states aside (pointer `sec:extensions`).
     Group them into three themed paragraphs (cost; evidence; scope), keeping the ranking.
   - **The paper's own open questions**, quoted, and Paine 2026: a representation-dependent
     normalised gap on a few small instances, without scaling, circuits or a general ordering; it
     raises the first question without answering it.
   - **Close with Q(i)–(iii) in italics**, each with its chapter by `\Cref` (plan §3.2's table),
     and the spine as the question underneath all three.

**Figures and tables.** None. (A figure of the published pipeline would show the interferometric
readout, which is not the method's; Style Guide §2.4.)

**Appendix offloads.** Appendix I: the published circuits' registers, angles and counts. Appendix
K: the paper's filter in full (phase sets, the dilation, t = 15 and 8 at degrees (6, 7)), every claim
with its verdict. Appendix E: the p-copy extension of the doubled space. Ch. 7 and Appendix F: the
readout identity.

**Marker checklist.** The first sentence attributes; no sentence reads as authorship of the
framework (Style Trap 13); `wu2025pihm` at each construction (no equation numbers);
none of our numbers, our constructions or our lemmas in §3.1–3.4; §3.5's weaknesses each point to
where they are argued; the three questions close the chapter; ≤ 4 pp.

**Traps.** "Collocation"; stating Θ(N^{4k}) or a degree here (Ch. 4's result); re-deriving the
time rule's shortfall or the readout correction (App. I, App. F); defining the standard form here;
"published" in visible prose (§14.2 item 8); any Θ̃(N²) floor.

---

### 5.4 Chapter 4: The Standard Form and Its Cost (7.5 pp; Model Formulation /30)

**Purpose.** State Wu et al.'s construction once, in the form every later chapter runs, the
*standard form*, crediting each piece and arguing each departure from the printed method where it
occurs (T-30); then answer Q(i): separate the encoder's cost from the Hamiltonian's by encoding
G exactly, and show that the degree stays Θ̃(N^{2k}) because the cost is the Hamiltonian's.

**Criterion.** Formulation, band 4: "a significant advance in the state of the art", and "described
in sufficient detail to permit readers to create equivalent models": §4.1–4.4 with Appendix B is
that specification for the standard form. Carries S1 and S2.

**Sources.** `docs/02_methods.md` §1–3 (the problems, the model, the residual); `docs/companion/`
10–11 (basis, differentiation), 20–24 (multiplication, constraints, the standard residual, its
spectrum, worked R2a), 31–33 (the paper's and the structured encodings), 57 (degree scaling), 71
(the dense reference, for one sentence); `docs/03_problems/02_r2.md`–`06_r6.md` (each panel as
printed and as run); `docs/06_results_guide/81_reproduction.md` (the validation sentence's
numbers) and `83_cost.md` (the cost keys); `docs/22_claims_register.md` (A-01–A-13, C-01, C-02,
C-05, C-07); `src/pihm/basis.py`, `operators/` (derivative, multiplication, constraints),
`assemble/standard.py`, `circuits/standard.py`, `arithmetic.py`. The reasons for each departure are
in decisions 15, 31, 34 and 49; state them, never cite them (plan §3.5 rule 3).

**Chapter contract.**

- **Arc.** Opening (the gate-count claim against the degree, the two costs, Q(i), the attribution) → §4.1 the model → §4.2 the
  operators → §4.3 the constraints and data → §4.4 the standard form, defined, with T10 and the
  validation → §4.5 encoding G (the paper's encoding, then the exact factorisation and its cost)
  → §4.6 what no encoding removes, and the hand-off to Ch. 5. Each subsection ends on the sentence
  the next starts from.
- **Voice.** "Wu et al." / "the paper" for the source; "the printed X" for one of its choices; "we"
  only for a departure, a closed form, a lemma or a construction that is ours (η_e, the stacked
  residual's reading, the uniqueness count, the multi-axis generalisation, the datum slices, the
  factorisation). Every restated construction carries its citation (Paine et al. for the latent
  space and the lifts, Wu et al. for the residual and the Gram sum, Olver for G's density).
- **Departures.** Inline, at the construction they modify, in one or two sentences: the printed
  choice, the defect (a mathematical kind), the replacement, the property gained. No history, no
  "we fixed", no issue number. T10 collects them.
- **Numbers.** By `\res` only; at most one number per departure, and the validation paragraph's
  pointer to App. I.
- **First use.** Each benchmark problem by its equation at first use, then its tag (T-10). R2a
  (f″ + 4f′ + 4f = 0, f(−1) = 0, f(0) = ½; the paper's Fig. 3b) is the running example from §4.1;
  R4a–R4d in §4.3 (rounded points and Maclaurin sources); R3c/R3d in §4.3 (the double zero); R5a–R5c
  in §4.3 (the PDE data); R3a in §4.4 (an exact polynomial kernel) and §4.6 (the lifted
  multiplier); R2b in §4.6 (gap measured flat).

**Scaffold.**

0. **Opening, no heading (0.3 p).**
   - Arrive at Q(i) (`sec:pihm-assessment`) from the paper's gate-count claim: a gate count prices
     one query, the degree counts queries (v3.6).
   - Why the two costs separate: d depends on the encoding only through α (`eq:degree`), and
     α_H ≥ ‖H‖ for every block encoding. The **encoder's cost** (the excess of α_H over ‖H‖) and the
     **Hamiltonian's cost** (‖H‖ itself) defined here, once.
   - The attribution sentence: the construction is Wu et al.'s, on Paine et al.'s latent space; it
     is stated once here as the thesis runs it, the standard form, and each place it departs from
     the printed method is argued where it occurs and collected in Table T10.
   - No roadmap (v3.6). The close hands off to Ch. 5: the encoder's cost removable, the
     Hamiltonian's not, the cost of differentiation paid in queries; the operator is what is left.
1. **§4.1 The model (0.6 p; `sec:standard-model`).**
   - The basis functions φ₀ = T₀/√N, φ_k = T_k/√(N/2) (discretely orthonormal at the nodes), with f_N = ⟨τ(x)|b⟩ = ‖b‖⟨τ(x)|ψ_e⟩, ψ_e = b/‖b‖ (representability, not a requirement on the prepared state), so that τ(x) of `eq:pihm-chebyshev-feature-map`
     (the paper's Eq. 3, shown in §3.1) is the vector of the φ_k at x; orthonormal at
     the Chebyshev–Gauss nodes, orthogonal with common norm π/N under the Chebyshev weight.
   - **τ(x) is kept raw**, as the paper's derivation uses it: ‖τ(x)‖² varies with x (< 2), and every
     constraint row inherits that weight, so renormalising point by point would change the rows'
     relative weights and with them the least-squares solution (one sentence; companion 10, 21).
   - **The scale, ours:** η_e = ‖b‖² = (N/π)∫f_N²/√(1 − x²) dx (`eq:eta-e`), Parseval in the
     normalised basis: the ideal value of the paper's η, growing like N. The sign of η: √η =
     y_s/⟨τ(x_s)|ψ_g⟩ is negative when the ground state's global sign opposes the datum's, so η > 0 is a
     sign convention and the decoded field carries the sign (one clause).
   - Several axes: the feature vector τ(x) ⊗ τ(y), Kronecker order, each axis its own n.
2. **§4.2 Differentiation and multiplication (0.9 p; `sec:standard-operators`).**
   - G's entries (`eq:pihm-G-entries`): 2p/√c_k for p > k, p − k odd; exact on the represented
     space; strictly upper triangular, nilpotent, ker G^j the polynomials of degree < j;
     N²/4 non-zeros; ‖G‖₂ = Θ(N²), with its limit (proofs → Appendices A and C); orthogonally similar
     to the nodal differentiation matrix, so the N² is not an artefact of the basis. The paper prints
     the same matrix as 𝔾ₙᵀ (T-16), said once.
   - The lift ℳ_a ∈ ℝ^{2N×N} for a polynomial coefficient (`eq:pihm-Mxp`, Paine et al.'s): exact if
     and only if deg a ≤ N; a constant coefficient enters as a₀ℳ₁ = a₀√2[I; 0]. ‖ℳ_a‖₂ ≤ √2 sup|a|.
     The standard form keeps the paper's lift, and the descriptor applies the same lift on the same
     axes (`assemble/descriptor.py`, `mult="lift"`); the square Galerkin form is only the gap
     study's control (App. D).
   - **The equation block** A_std = Σ_j ℳ_{a_j}G^j − ℳ_r𝔻⁽⁰⁾(x_s), the source injected through the
     regular datum as the rank-one |r̂⟩⟨τ(x_s)|/f(x_s). **Departure (sources):** the paper expands r
     in a Maclaurin series truncated at p̄ = 3, 5, 7; a truncated source poses a different equation
     (the order-7 series is wrong by 130 % at x = −1 on R4d), so its error is a floor no resolution
     removes. The standard form loads r's Chebyshev coefficients on the lifted register: spectral
     accuracy, the same collapse row.
   - **Departure (axes):** the paper treats two variables; the residual on any number of Chebyshev
     axes is the Kronecker product over axes of ℳ_aG^{j_a}, each axis lifted if any term on it needs
     the exact product (`app:pihm-multi-axis`). Two are run; say so.
3. **§4.3 Constraints and data (0.9 p; `sec:standard-constraints`).**
   - The zero row 𝔹(x) = √N|0⟩⟨τ(x)| maps a field to the constant f_N(x); 𝔹(x)G^j imposes
     f^{(j)}(x) = 0. The collapse row 𝔻⁽⁰⁾(x_s) = 𝔹(x_s)/f(x_s) maps the solution to the constant 1
     whatever its scale, which is what makes a source expressible. Both the paper's (Eqs 9–11).
   - **Departure (constraint points):** a zero row is exact only where the true field's derivative
     vanishes. The paper's Fig. 5 points are rounded (−0.2, −0.73, 0.91, −0.75); a zero imposed where
     the solution does not vanish contradicts the equation, so least squares trades the two and the
     error floors. The standard form takes the point the problem defines, the zero or extremum of
     its solution, exactly: the root of the solution's derivative nearest the paper's value,
     computed from the reference solution when the problem is built (`exact_root`), outside the method:
     **not** an answer-independent quantity, and a new problem must supply its points. Each printed choice
     alone floors the error, and only both removed converge (one sentence; the triage → App. I).
   - **Uniqueness (ours, a lemma):** a homogeneous order-k ODE whose leading coefficient has no zero
     needs constraints of rank k − 1 on its solution space plus one regular datum; the rank is that
     on the solution space, not of the functionals (statement; proof → `app:uniqueness-count`). For
     an inhomogeneous equation or a singular leading coefficient the computed kernel decides
     (trusted, §7.3).
   - **Departure (PDE data → datum slices):** the paper's invariant sets omit the initial or
     boundary function that fixes the solution, are read off the known solution (heat's ∂ₓf at
     ±¾, wave's zeros at t = ⅛, ⅞), and lose rank beyond the printed n. The standard form imposes the
     function on its slice as one row family, 𝕊_a(x*) − ĝ τ(x_s)ᵀ/v (homogeneous in the scale, zero on
     the true field and its multiples; `app:datum-slice`), in both forms: answer-independent and well
     posed at every n. The heat panel's data are imposed at t = −1, so the problem runs forward (its
     data at t = 0 inside [−1, 1] would make it backward on [−1, 0], hence ill posed).
   - **Departure (a double zero):** the paper's R3c and R3d multiply the associated Legendre
     equation through by (1 − x²), leaving a leading coefficient (1 − x²)² with double zeros at ±1
     and a solution with a √(1 − x²) branch point, so convergence is algebraic. The substitution
     f = √(1 − x²)v gives an equation in v with simple zeros and polynomial coefficients: spectral
     convergence (`app:legendre-substitution`); it is also the form the descriptor can run (§5.4).
   - The Laplace panel's printed solution has cosh for cos (one clause; A-05). Vector data enter
     as ratio rows, defined with systems (`sec:systems-data`; forward pointer).
4. **§4.4 The standard form (0.9 p; `sec:standard-form`).**
   - **The stacked residual** R = [A_std; constraint rows], every block at weight one, H = R†R
     equal to the paper's sum of Gram matrices, never formed; the ground state is the smallest right
     singular vector of R, solved by SVD or Lanczos on R (`sec:pipeline-reference`): one sentence,
     with the reason (forming H squares R's conditioning).
   - **What H is (the claim A-09, stated as a property):** positive semi-definite, not definite as
     the paper describes it; an exact zero eigenvalue exactly when the solution is a polynomial in the
     span (R3a's Legendre polynomial from n = 3); otherwise λ₀ > 0 and the construction is least
     squares. The thesis relies on an isolated ground state, measured as a trusted kernel, never on
     definiteness.
   - **Definition (the standard form)** (`def:standard-form`): the stacked residual with equation
     block of §4.2, constraint rows of four kinds (zero, collapse, ratio, datum slice; Table T2 in
     §7.2 lists them as model inputs), on any number of axes; H_std = R†R. The problem is unnamed
     ("R2a").
   - **Table T10, `tab:deviations`** (≈ 0.6 p): aspect | Wu et al. | this thesis | defect removed or
     property gained | where. Rows: constraint points; sources; PDE data; a double zero; the Laplace
     reference; number of axes; the Gram sum; vector data; the G encoder; normalisation by ‖H‖_F;
     mixed-parity QSVT; QITE with the time rule; phases by fitting; the interferometric readout;
     eigh(H); initial states; the doubled space; one real field. Pipeline rows point to Ch. 7; the
     doubled space and one real field to Ch. 6.
   - **The fairness sentence:** the departures change the data and the solve, never G or the Gram
     structure, so the standard form has the paper's ‖H‖ and its cost, and better accuracy: the
     baseline is not weakened against the paper. (v3.2, 2026-10-12: it is *not* conservative
     against the descriptor. Its structured encoding is looser than the descriptor's (α_R/‖R‖ 7.7
     against 1.04 on R2a at n = 8, `looseness` keys), so an as-built comparison favours the
     descriptor; only the ideal bound isolates the Hamiltonian, §7.7.)
   - **The validation paragraph (S1's evidence, the only body trace of the reproduction):** the
     paper-faithful variant, with every printed choice kept, reproduces the paper's printed
     supplementary matrices entry by entry and the printed scale factors of all eleven ODE panels to
     within one unit of the last printed digit; the three PDE and two nonlinear panels do not
     reproduce, by the exact solution's η_e or any ground state computed. Pointer: the record, the
     triage and every claim's verdict are Appendix I. One `\res` at most (R2a's η_ideal against 1.29).
5. **§4.5 Encoding the derivative (1.6 p; `sec:standard-factorisation`).**
   - **§4.5.1 The paper's encoding (0.4 p; `sec:standard-published`).** What it is (an LCU loading
     the column value 2p as a rotation amplitude, approximate); the only claim that decides the cost
     is the prefactor: valid, but against ‖G‖₂ it grows as jN³, j = j_{−3/4,1} ≈ 1.06 the first positive zero
     of J_{−3/4} (`\res{derivative/n7}{published_ratio}`); efficient in gates, inefficient in subnormalisation.
     We rebuild the mechanism (registers of our own, odd offsets only) so that its cost can be
     counted like the others, at its own α, a third of the printed prefactor, the kinder reading;
     approximate, so it enters resource estimates only. The claims' verdicts, the rebuild and its
     error bound → Appendix I (`tab:published-verdicts`, `prop:epsilon-G`).
   - **§4.5.2 An exact factorisation (0.5 p; `sec:standard-exact`).** The idea in words (row weight ×
     parity-selected shift × column index, each depending on one index); `prop:G-factorisation`
     (C-01), G = R₀(2U_odd)Λ; the measured error as a check on the implementation, not as evidence.
   - **§4.5.3 Circuits and cost (0.7 p; `sec:standard-cost`).** Λ as a Z-string LCU, R₀ as two
     terms, U_odd by subtraction with a post-selected borrow flag (F3); `prop:standard-cost`
     (α_G = N(N−1), → 2j_{−3/4,1} ≈ 2.117 times ‖G‖₂; O(n²) gates; n + 4 ancilla, n − 1 of them the
     selector of the N/2-term LCU, the price of the sum of shifts against the descriptor's O(log n));
     `tab:alpha-G-short`; lifts, rank-one rows and products sharing one ancilla register; the
     stacked residual composed into one reflection (§7.4) and verified against the assembled H
     (§7.6). The arithmetic and the proofs → Appendix C.
6. **§4.6 What remains: the standard-form Hamiltonian (1.2 p; `sec:standard-hamiltonian`).**
   - For constant coefficients α_R/‖R‖ stays bounded on R2a (`looseness/…` keys; C-02): the encoder
     has done its job.
   - ‖H_std‖ = Θ(N^{4k}) (proved for constant coefficients with a_k ≠ 0 and constraints of lower
     order; `app:proof-standard-cost`), against a gap measured flat (R2a and R2b directly; the
     ideal-bound degree's exponent 2k on R1, R2 and R4); so by `eq:degree` d = Θ̃(N^{2k}), Θ̃(N⁴) at
     second order, **the Hamiltonian's cost**, since α_H ≥ ‖H‖ for any block encoding; the floor stated
     for the minimax filter and hedged to Lin & Tong. The n = 8 degrees as built and at α = ‖R‖
     (resource estimates).
   - The paper's gate count is the cost of one query; the cost of the method is that times the
     number of queries, which the norm fixes. The paper does not claim otherwise; it leaves the gap
     to future work.
   - The degree's growth with the paper's, the structured and the ideal encoding, separating the
     two costs (`growth` keys); the cause: the degree pays ‖R‖/σ₁, not the squared conditioning of
     H = R†R (only an eigensolver on H pays that), so the exponent 2k is the order eliminated
     through G; the classical remedies are the first-order system and the banded basis (§2.3).
   - **The scope, volunteered:** R3's lifted (1 − x²) multiplier, paid as ‖ℳ_a‖‖G²‖ ≫ ‖ℳ_aG²‖,
     where the encoder's cost reappears and the ideal-bound degree grows as N² (the descriptor's
     exponent there); hence the ideal-encoding bound beside every as-built cost (T-25), and R3's
     reversal reported.
   - Close: the answer to Q(i) in two sentences, and Ch. 5 named as changing the Hamiltonian.

**Figures and tables.** T10 (`tab:deviations`); `tab:alpha-G-short` (full table → Appendix C); F3
(`fig:uodd-select`). `tab:published-verdicts` is Appendix I's.

**Appendix offloads.** Appendix A: G's entries, structure and Θ(N²). Appendix B: the worked N = 4
residual, the lifts and folds, the multi-axis residual, the datum-slice rows, the R3c/R3d
substitution, the uniqueness count and its proof, the paper-faithful conventions. Appendix I: the
paper's circuits as rebuilt, their claims' verdicts and the error bound. Appendix C: the
factorisation's proof, the arithmetic SELECT, the cost proof, the Bessel-kernel limit and
‖G^k‖₂ = Θ(N^{2k}). Appendix G: eigh against SVD and Wedin's bound. Appendix I: the reproduction,
the triage and every claim's verdict.

**Marker checklist.** The first paragraph poses Q(i) and attributes the construction; every
restated construction cited; every departure inline, a defect and a property, and in T10; the
standard form defined once, formally, before §4.5 uses it; the validation paragraph names the
non-reproduced panels as well as the reproduced ones; the encoder/Hamiltonian distinction
unmissable and the R3 caveat stated; S2 serves the comparison; no variant name outside §4.4's
validation paragraph.

**Traps.** A changelog ("we then fixed…"); "corrected"; calling the exact constraint points
*answer-independent* (they are roots of the reference solution, answer-dependent set-up outside the method); re-deriving the paper's
claims (the time rule, the readout) here; "our standard-form solver"; "wall"; implying the
structured encoding is tight on every problem; claiming the gap flat in general.

---

### 5.5 Chapter 5: The Descriptor Reformulation (10.5 pp; Model Formulation /30, the core)

**Purpose.** Answer Q(ii): the headline, written as the methods section of a journal article,
including the reformulation's own challenge and its cure.

**Criterion.** Formulation, band 4, "warranting publication". The body carries the idea, the object
(stated once), the cost (a formal result), the challenge and the interpretation; entries,
constructions and proofs go to Appendices A and D.

**Sources.** `docs/02_methods.md` §3.2; `docs/13_descriptor.md`; `docs/14_descriptor_gap.md` (the
challenge); companion 12–13, 50–57; claims B-01–B-07, B-14, B-20, B-21, C-05, C-06;
`src/pihm/assemble/descriptor.py`, `systems.py`, `ir.py`, `circuits/lcu.py`, `problems/scales.py`.

**Scaffold.**

1. **§5.1 The banded factorisation (1.25 p; v3.9, 2026-10-14: the chapter opening, "The idea" and
   "The banded factorisation" merged, since the idea *is* the factorisation kept as rows).** The
   opening paragraph, before §5.1, arrives from §4.6 and poses Q(ii) only. §5.1 then: the idea in one
   sentence (dense because the derivative is expanded in the function's basis; banded into the
   neighbouring basis); B̃f̂⁽¹⁾ = D̃f̂⁽⁰⁾ and G = B̃⁻¹D̃, B̃ on its diagonal and second superdiagonal,
   D̃ on its first (entries and the recurrence → Appendix A), ‖D̃‖ = 2(N − 1), ‖B̃‖ ≤ 2 + √2; the
   ultraspherical antecedent credited once, with the reduction it would offer and why it is not
   built; the move (keep the factor as a row, carry the derivatives; chain and mass form named);
   first-order-system least squares credited and the increment named. **Figure F4**: the sparsity of
   A_std against A_desc for R2a at n = 4. The spine sentence closes the section.
2. **§5.2 The descriptor residual and its kernel (2.25 p; `sec:descriptor-layouts`; v3.10, 2026-10-14:
   "Two layouts and kernel equivalence" and "Constraints and partial differential equations" merged,
   since the theorem assumes the constraint placement and extends to the several-axis chains).**
   - *The chain* (order k ≥ 2): w = (f̂⁽⁰⁾; …; f̂⁽ᵏ⁾), padded to 2^⌈log₂(k+1)⌉ blocks; the block rows
     (recurrences −D̃f̂⁽ʲ⁾ + B̃f̂⁽ʲ⁺¹⁾ = 0, the equation row, padding) in the Definition's matrix;
     **Table T5** moved to Appendix D (`tab:app-descriptor-rows`), with the several-axis rows. A
     variable coefficient by the standard form's own lift, on the axes it lifts (§4.2), so the two
     equation rows apply the same operators (the kernel theorem needs this); stated once, here.
   - *The mass form* (first-order equations and systems): no derivative block, since the equation
     gives the derivative; the standard rows multiplied through by I⊗B̃, I⊗D̃ − Γ⊗B̃ for z′ = Γz; one
     block per component; the state, initial state and readout are the standard form's. The mass
     form is *defined* here, for z′ = Γz in general, because the theorem below covers both layouts;
     its use for several fields is Ch. 6's (one sentence pointing there). Its running example here is
     R1, a single first-order equation.
   - *Constraints* (paragraph, `sec:descriptor-constraints`, before the theorem that assumes it):
     constraint rows on the block they read; Neumann on the f′ block, the same atom as Dirichlet, no
     G; the regular datum on block 0, so decoding and scaling are the standard form's.
   - **Theorem (kernel equivalence)**, both layouts: ker A_desc = {(p, Gp, …, Gᵏp) : p ∈ ker A_std}
     for the chain, and ker A_desc = ker A_std for the mass form, because B̃ is invertible. Proof in
     five lines in the body if it fits, else Appendix D.
   - *Several axes* (paragraph, after the theorem): one field block and a chain per axis; mixed
     derivatives not built; datum slices for initial and boundary *functions* (defined with the
     standard form, §4.3), available to both forms (so "the descriptor avoids doubling for linear
     PDEs" is **not** claimed, B-20). The state cost in one clause, 2^⌈log₂(1+Σk_a)⌉·∏N_a against
     ∏N_a, the examples in App. D (`sec:app-variable-coeff`). Then the theorem's extension to several
     axes and to the rescaled residual (proof App. D).
   - The least-squares ground states differ by row weighting and converge to the same function (B-02).
   - **Volunteer the cost in the same breath:** the chain grows the state from N to 2^⌈log₂(k+1)⌉·N;
     the mass form grows nothing.
3. **§5.3 The gap of a carried derivative (1.0 p) — the challenge.**
   - The mechanism: on states satisfying the recurrences, the Rayleigh quotient of H_desc is
     ‖R_std p‖² / Σ_j‖G^j p‖², so the norm carries every derivative, and the gap is flat only where
     the equation controls each carried derivative.
   - **Definition (v3.11, `def:regular`), immediately before the theorem:** a linear problem on one
     axis (an equation, or a first-order system z′ = Γz with constant Γ) is *regular* if its
     coefficients are polynomials and its leading coefficient has no zero on [−1, 1], its source and
     solution are analytic, and its constraint rows read f, …, f^{(k−1)} at fixed points with every
     C^k function they and the equation annihilate a multiple of f; *singular* if a_k has a zero on
     [−1, 1]. R1, R2, R4b–d regular; R3, R4a singular. It names the theorem's hypotheses once, so
     every later scope is one word.
   - **Theorem (v3.8, `thm:flat-gap`):** for a regular problem the gap is
     Θ(1): in the chain unscaled or at a fixed ζ, and in the mass form, which has no derivative
     block and so nothing to rescale. Proof in App. D (`app:flat-gap`): the
     recurrence rows are the defect f_{j+1} − f_j′ in the U-weighted norm (`lem:second-kind`),
     integration recovers the lower blocks, the equation row the top block, and compactness
     closes it; no explicit constant.
   - Where it fails: a singular problem (the gap falls as N⁻⁴ at a simple endpoint
     zero, N⁻² inside); two axes, where the equation constrains only a sum of top derivatives; and
     the field block crowded out of the ground state, so an initial state on it has tiny overlap
     (R2c unscaled: field weight 5.4e-6).
   - What it is not: the lift, the padding, the precision, the constraints, the basis and the
     reference method are ruled out (one sentence; the evidence → Appendix D).
4. **§5.4 Block rescaling (1.0 p) — the cure and its limits.**
   - f̂⁽ᵐ⁾ ↦ ζ^{−m} f̂⁽ᵐ⁾ (`eq:block-rescaling`): S diagonal and invertible, so the kernel and the
     field block's readout are unchanged. **In the circuit it reweights the bands before the block
     register's patterns are expanded in Pauli words: no ancilla, but a pattern equal across its
     blocks gains words, so terms and gates per query grow by at most 4^{n_f}, fixed by the
     equation, not by n** (v3.8, 2026-10-13; the old "no gates" was false as built).
   - **The weight** (no name or term, v3.16): ζ = 2|ā₀/ā_k|^{1/k} for a regular problem; N/2 for a
     singular one; N per PDE axis, balanced by the
     top-order coefficients (the wave's (cN, N)). Padding decouples; c_pad = 1. Why ζ ∝ N at a
     simple zero: the concentrated states' quotient is O(N⁻⁴ζ^{2k}) (App. D), so ζ ∝ N^{2/k}, N at
     second order; a double zero needs N^{4/k}. The two constants (the 2 and the ½) were selected
     by calibration on the benchmark problems and held fixed, never refitted; the check is
     in-sample. The classes are asymptotic: a regular coefficient dipping near zero behaves as
     singular once resolved, where the regular weight loses (`zeta-dip` keys, App. D). Deriving ζ
     from the equation is further work (`sec:future-work`).
   - What it restores: an O(1) gap on every one-axis panel the descriptor runs, and γ² of order
     0.01–0.76 against as little as 1e-19 unscaled (§8.3 has P8's).
   - **What it does not:** on a singular problem ‖H‖ grows as ζ^{2k}, so the
     degree is about Θ̃(N²); on two axes the gap still falls with N; **a double zero is beyond any
     block rescaling** (the paper's own R3c and R3d multiply by (1 − x²)), which is why the
     problem is run with simple zeros (§4.3). General equilibration costs Θ(P) gates and is
     excluded from circuit paths.
   - The analogy, stated once: this is the descriptor's version of Olver & Townsend's diagonal
     preconditioner.
5. **§5.5 The block encoding: one flat LCU (1.0 p).** Every block a short sum of SHIFT·diag terms
   (truncated shifts through one overflow qubit; diag(k) as a Pauli-Z sum; near-constant diagonals
   by reflections); the rescaling in the coefficients; rank-one rows through the feature map, a
   source's N coefficients loaded by a rotation tree (O(N) gates for a general source, as for any
   general state, poly(n) for a polynomial one: B-11) and added by one further combination. A system's coupling Γ (a sum of matchings) is Ch. 6's: one pointer.
   **Figure F5** (quantikz) in the body; the **algorithm** (term IR → PREPARE/SELECT/PREPARE†)
   and its line-referenced walkthrough (Snow's model) together in App. D (`app:term-ir`; v3.8,
   2026-10-13, moved to meet the page budget, the walkthrough having moved in v3.4).
6. **§5.6 Cost of the descriptor encoding (1.0 p).**
   - **Proposition (structure):** an exact block encoding; ⌈log₂(n+4)⌉ + 8 ancilla for R2's system
     rows (O(log n): the block register, the term selector, the overflow and projection flags);
     O(n²) gates without a source or with a polynomial one, O(N) added by a general source (B-11). Proof → Appendix D. With Ω(log L), the ancilla count is order-optimal *among exact
     LCU encodings*; hedge exactly that far.
   - **Measured (assert, with `\res`):** α/‖A_desc‖ → 1 on regular problems, about 2 on
     singular ones, 2.3–4.1 on PDEs (B-04).
   - **Interpretation, two paragraphs:** what O(log n) ancilla mean beside the standard form's
     n + 4 for G alone; and, volunteered, that at reachable n on constant-coefficient problems the descriptor's
     gate count per query is *higher* than the structured standard form's (more terms, the block
     register), so its advantage there is the degree, not the gates per query; on the lifted
     variable-coefficient panels its query is the cheaper (R3 from n = 4, R4a from n = 3).
7. **§5.7 Consequences for the spectrum and the filter (1.25 p).**
   - ‖H_desc‖ = Θ(N²); with the rescaled gap flat on a regular problem, `eq:degree` gives
     **d = Θ̃(N)**, against Θ̃(N^{2k}) (`eq:standard-wall`); about Θ̃(N²) or faster on a singular
     problem or on two axes (C-05 as restated).
   - The relative gap, stated precisely: the standard form's ground state is below double-precision
     resolution by `eigh` from n = 8, **not** by SVD; the consequence is the degree, not
     unresolvability (B-07, B-23).
   - One query's post-selected success on a Haar-random input is Θ(1) here against N⁻¹ per axis in
     the structured standard form (B-14): it compares the encodings, not a cost of the pipeline.
   - The comparison will be quoted as built and at α = ‖R‖, and the expected reversals named (R3 at
     the ideal bound; the heat panel at small n); pointers to §8.2–8.3.
8. **§5.8 Summary (0.25 p).** Four numbered takeaways, one of them a limit, and the spine.

**Figures and tables.** F4 (sparsity, from `pihm.pipeline.solutions`' structure view), F5 (flat LCU),
Algorithm G.1 (App. D, v3.8), T5 (block rows; in Appendix D as `tab:app-descriptor-rows`); optionally T5b (the descriptor's term types: arity, gates, verified
residual).

**Appendix offloads.** Appendix A: B̃, D̃ entries and the ultraspherical identities. Appendix D: the
block rows in full, the padded count, the mass form, the kernel-equivalence proof, the gap mechanism
and its ruled-out artefacts, the rescaling rule and its checks against a grid, the term IR and its
compilation, the cost proof.

**Marker checklist.** A referee could re-derive A_desc from the body plus B and G; the Hilbert-space
and per-query costs volunteered; ultraspherical and first-order least squares credited at §2.3 and
§5.1; the cost a proposition and interpreted; the ancilla claim O(log n) with optimality hedged;
the gap's failure owned with its mechanism; the rescaling's limits stated; every body equation
passes the equation test.

**Traps.** "O(1) ancilla"; "+ 6 ancilla"; "bit-identical a-block"; "the gap is Θ(1)" unscoped;
"rescaling costs Θ(n_f) gates"; "ζ fitted" per problem (two constants calibrated once, held fixed); "a priori" for the ζ rule; "only the descriptor can prepare nonlinear solutions".

---

### 5.6 Chapter 6: Systems and Nonlinearity (6.5 pp; Model Formulation /30)

**Purpose.** Take the construction from one real scalar field, the paper's scope, to several
coupled fields, to complex-valued linear equations, and to polynomial nonlinearity, and answer
Q(iii) on the way. **The chapter's thread** (T-31): each extension is carried as a coupled linear
system on one state, a block per component (several fields directly; a complex field by
realification as two real ones; a polynomial nonlinearity by the Carleman lift, whose components
are monomials), and the one route that is not such a system, the paper's doubled space, only
projects. So the system is stated once (§6.1–6.2), the lift *is* that system with Γ → Γ_K (§6.5),
and every coupling and product meets the circuit in one place (§6.6).

**Criterion.** Formulation, "sufficient detail to permit readers to create equivalent models": the
rows, the data and the circuits of a system and of a lift must be rebuildable from the body plus
Appendix E. The chapter opens with the scope the paper leaves (one real field; its Discussion: with
a Fourier basis "the resulting total energy function is of a complicated form, rendering it
difficult to find the ground state"; a doubled space for quadratic terms) and with Q(iii), and
closes on Q(iii)'s answer (§6.8). Carries S4.

**Sources.** `docs/02_methods.md` §3.2 (the mass form), §3.3 (ratio rows), §3.4–3.5, §6.2 (a
system's initial state); `docs/companion/` 21 (constraints), 51 (mass form), 60–65 (the doubled
space, the time axis, the lift and its truncation, Burgers, Navier–Stokes); `docs/16_extensions.md`
§1.1 (R7, the mass form against the chain), §1.2–1.3 and §2–5; `docs/17_navier_stokes.md`;
`docs/03_problems/07_r7.md`; claims A-10, B-12, B-18, B-19, B-22, C-09, C-10; decisions 39, 42, 45
(reasons only); `src/pihm/assemble/systems.py`, `circuits/systems.py`, `ir.py` (`matching_terms`),
`operators/constraints.py` (`ratio_rows`), `carleman.py`, `problems/fluids.py` (`real_embedding`),
`circuits/tensor.py` (complex weights), `circuits/folds.py`; notebook 60. The paper's Discussion for
the complex-valued remark.

**Scaffold.**

0. **Opening, no heading (0.3 p).** The paper's scope (one real scalar field), its remark on
   complex-valued states, quoted, and its doubled space for quadratic terms (§3.4); Q(iii)
   (`sec:pihm-assessment`), arrived at from the doubled space's zero gap (no finite degree, so a
   filter projects); the thread, in one sentence: everything this chapter adds is a coupled linear
   system on one state, except the doubled space. No roadmap (v3.6). *(v3.2, checked
   against the paper's p. 11: the remark is about the **Fourier basis**, whose differentiation
   matrix is imaginary, so the state is complex-valued and "the resulting total energy function is
   of a complicated form". Quote it with that context; §6.3 answers it twice: H = R†R stays
   Hermitian, and a real Fourier basis avoids the complex state for a real field.)*
1. **§6.1 Several fields on one state (0.9 p; `sec:systems-fields`).**
   - A first-order system u_i′ = Σ_j Γ_ij u_j (constant coefficients; one equation per field, each
     holding its own first derivative) on one Chebyshev axis; on a time axis ξ = 2t/T − 1, with the
     factor T/2.
   - The state: one block per component, on a field register of ⌈log₂ C⌉ qubits, padded to a power
     of two with padding rows of weight 1 that decouple exactly.
   - The rows: standard I⊗G − Γ⊗I (the paper's elimination, applied per field); the descriptor's
     mass form (§5.2) multiplies them by I⊗B̃. Same kernel; an IVP with data has a one-dimensional
     near-kernel.
   - **Why the mass form and not a chain per field:** the equation already gives each derivative,
     so a derivative block carries nothing new, costs register and needs rescaling. Measured on R7
     (u′ = v, v′ = −π²u), the mass form's gap is about 2.1 times the block-rescaled chain's, flat in
     n from n = 3 (1.85 at n = 2); quote the two gaps by `\res` (`build/R7/descriptor/n8` and
     `…/layout=chain/chain`) and the ratio as `\prov` until a derived key exists (plan §2.1); the
     chain stays as a labelled ablation.
   - *(v3.2)* The rows are displayed **once**, here (`eq:system-rows`, components the most
     significant index, as §5.2's `eq:mass-form`), with the time axis's T/2; §6.5 does not
     re-display them (`eq:carleman-spacetime` retired; App. E's comment retargeted).
   - The standard and descriptor forms of a system share their state, initial state and readout,
     and differ only by I⊗B̃: the like-for-like comparison R7–R10 rely on.
   - Higher-order systems: by reduction to first order (one sentence; none run beyond R7's
     order-two equation written as two fields).
2. **§6.2 Data for several fields: ratio rows (0.4 p; `sec:systems-data`).**
   - The ratio row 𝔽 = y_a(I − |a⟩⟨a|) − y_⊥⟨a| on the field register, times 𝔹(x*): it imposes the
     *direction* of the vector datum and leaves its scale free, as a zero constraint does; its
     singular values are ‖y‖, |y_a| and 0; a zero datum holds its component to zero exactly.
   - The scale from the regular datum, as for one field. The initial state's weighting by w₀/‖w₀‖
     is stated in §7.5; one pointer, with the reason (equal weights cancel on Taylor–Green).
3. **§6.3 Complex-valued fields (0.7 p; `sec:systems-complex`).** Scope fixed by T-32.
   - **The formulation does not need a non-Hermitian filter.** For complex coefficients, data or
     sources R is complex, and H = R†R is still Hermitian and positive semi-definite; the ground
     state is still the smallest right singular vector of R; the stacked reflection and GQSP act on
     H′ unchanged. The non-Hermitian operator is R, which the filter never sees. (A formulation
     statement; no complex-R preparation was run.)
   - **Realification, the route run.** z = u + iv as two real fields: z′ = cz gives
     [u; v]′ = [[Re c, −Im c], [Im c, Re c]][u; v] (c, not a or α, which are taken), one more
     field-register qubit, the same kernel under the real-linear isomorphism: a §6.1 system.
     **R7 is exactly this:** with z = πu + iv, u′ = v and v′ = −π²u are z′ = −iπz, a single-mode
     Schrödinger-type equation. *(v3.2, precision a referee will check: R7's state is (u, v) =
     (Re z/π, Im z), the realified state with its first block divided by π, a diagonal change of
     variables, so its residual is the realification's up to that scaling and its kernel is the
     same line. Say so in one clause.)* The Fourier–Galerkin fluids (§6.7) are carried on real bases
     for the same reason: Burgers on sine modes, which are real because an odd solution stays odd (no
     realification is needed); Navier–Stokes on cos/sin, related to the complex Fourier variables by
     an isometric real embedding E (E†E = I).
   - **Native complex encoding, built once.** The tensor layout's coupling (§6.6) is built on
     complex Fourier variables, with complex phases i^{Σa} in its LCU weights, and verified (exact and
     IR); it is never used to prepare a state, because the classical pipeline carries real data only.
     One forward pointer. *(v3.2: the phases are a Fourier symbol's, i^{Σ_d a_d} for ∏k_d^{a_d};
     Burgers' derivative output is imaginary, the vorticity's fold real. Exact verification is at
     R9c-M4, K = 2 only (`lift/R9c-M4/standard/n0/carleman=2/lift=tensor`); IR to 316 modes at
     K = 2; K = 3 on 148 and 316 modes is construction-only. A preparation in this layout would load
     the data's complex moments, which the loaders refuse.)*
   - **Not built:** complex sources, data and coefficients in the circuits' loaders (a phase on the
     collapse row; a complex state loader), and so native complex preparation. Future work (Ch. 10).
   - The research proposal's "complex-valued, non-Hermitian equations" is answered here at the level
     of the formulation, and recorded as a deviation (§13.4).
4. **§6.4 The doubled space: exact encoding, degenerate kernel (0.6 p; `sec:doubled-space`).**
   - Opens on the two treatments of a polynomial nonlinearity: the doubled space (the paper's, §3.4;
     run here in the standard form only, since it projects in either) and the Carleman lift (both
     forms, §6.5). The first is not a linear system on one state, and that is where it fails.
   - An exact encoding (the fold, B-12); kernel dimension N² minus the rank, at least 2^{2n−1}
     (A-10, measured).
   - **Proposition (a filter projects; no answer-independent penalty isolates the solution)**
     (`prop:no-penalty`): a kernel containing ψ⊗ψ and φ⊗φ contains their sum, which is not a product
     state, so no Hamiltonian enforces the product structure; any function of H returns the initial
     state's projection onto the kernel; the paper's choice reported as the product state of least
     residual. Proof → Appendix E. *(v3.2: state it for any filter that is constant on the kernel
     and suppresses the rest, so it covers the minimax filter as well as QITE; the existing draft
     stated it for imaginary time only. The bound behind A-10 is dim ker ≥ N² − 2N − c for c
     invariant constraints, above 2^{2n−1} from n = 3; quote the measured count by
     `build/R6a/standard/n5`'s `kernel_count`.)*
5. **§6.5 The Carleman lift in space–time (1.0 p; `sec:carleman`).**
   - The hand-off in one sentence: the lift of a polynomial system is a linear system on its
     monomials, so §6.1–6.2 carry over: the components become monomials, the ratio rows carry the
     data's moments, and Γ becomes Γ_K. This section adds only the lift.
   - z = (u, u^{⊗2}, …, u^{⊗K}) in the symmetric layout, carried as u/s with s = max(‖u₀‖, 1), a
     diagonal similarity that keeps no level growing as ‖u₀‖^k.
   - The truncation error is O(ρ^K) for ρ = ‖u₀‖‖F₂‖/|Re λ₁(F₁)| < 1: **a sufficient condition, a
     worst case over all states** (cite Liu et al. 2021); the convergence is measured per order
     against the exact lift (§8.4).
   - A linear IVP has one solution, so the space–time residual has a one-dimensional near-kernel:
     the uniqueness is Carleman's, not the form's.
   - The lifted system on the time axis in both forms is §6.1's `eq:system-rows` with Γ → Γ_K,
     said in prose (v3.2: no second display); the like-for-like comparison of R8–R10. The symmetric
     layout's size, Σ_{k=1}^{K} C(M+k−1, k), and Γ_K's structure (block upper triangular in levels,
     eigenvalues the sums of F₁'s) in one sentence each; ‖F₂‖ in ρ is taken on symmetric tensors.
   - Initial data by §6.2's ratio rows on the data's moments; the error split into the lift's and
     the time axis's.
6. **§6.6 Couplings and products on a circuit (0.8 p; `sec:ext-circuits`).** Every coupling and
   product of the chapter, once.
   - **The coupling as a sum of matchings:** Γ (a system's, or the lift's Γ_K in the symmetric
     layout) split by edge colouring into at most 2Δ − 1 matchings (Δ its largest row or column
     degree); each a permutation of the field register's basis states, its entries a multiplexed
     rotation on one flag; α = the largest entry. Both forms pay the same for Γ. The matchings
     against Pauli words, one sentence with numbers (key to add). *(v3.2, checked against
     `ir.matching_terms` and companion 55: the **greedy** colouring guarantees ≤ 2Δ − 1; Δ is the
     least possible (König; Γ as a bipartite graph of rows and columns), and on every lift built the
     greedy colouring reached Δ. Each matching's α is its own largest entry, so the coupling's α is
     the **sum** of those. Measured α/‖Γ_K‖ (keys `lift/…/verify=ir`): about 1.1–1.5 on R9, 2.3–7.3
     on R10. No Pauli-word count is exported: compare the matchings with the tensor layout instead
     (both keyed), and put the Pauli count in App. E as `\prov` or drop it.)*
   - The ratio rows as three LCU terms (identity, projector, a loaded rank-one term).
   - **The tensor layout:** Γ_K in **2K − 1 terms** (not K²), each F_p on adjacent slots, which
     reaches field scale; built on complex Fourier variables (§6.3).
   - **Products:** the nodal fold 𝒩₁^{(p)} = 2^{pℓ/2}U_CG†Δ_pU_CG^{⊗p}: exact, no ancilla beyond
     padding, α = 2 for p = 2, **within 1.21 times ‖𝒩₁‖₂ (1.58–1.665): tight, not optimal**
     (`prop:fold-optimal`, to be retitled); the Fourier fold QFT, copy, QFT†; the Chebyshev DCT
     budgeted as a cited primitive (Klappenecker–Rötteler), **not built gate-level**, said plainly.
     *(v3.2, from companion 60 and B-12: the fold is 2^{pℓ/2}U_CGᵀΔ_p(U_CGE)^{⊗p} with E the zero-padding;
     its circuit's n + 1 ancilla are one padding qubit per copy and n − 1 spares that return the
     register to zero for stacking, so "no ancilla" is wrong; ‖𝒩₁‖₂ = 2√λ_max(Q∘Q) ≤ 2 is proved and
     the 1.21 computed to n = 12. The nodal fold serves the doubled space; the symmetric lift's
     products live in Γ_K and the tensor layout's in the Fourier fold.)*
7. **§6.7 Fourier–Galerkin fluids: Burgers and Navier–Stokes (0.7 p; `sec:fluids`).** Burgers:
   F₁ = diag(−νk²), F₂ the (u²)ₓ/2 convolution, on sine modes. 2-D vorticity Navier–Stokes on the
   real cos/sin basis (§6.3) with ψ̂ = ω̂/|k|² eliminated and exact rational couplings. Taylor–Green
   (its modes share |k|, so the lift is exact: a validation) and a counter-rotating vortex pair
   (active triads). References: the Galerkin system's IVP, Cole–Hopf for Burgers, a pseudo-spectral
   simulation for the truncation's own error. *(v3.2, from companions 64–65: Burgers runs on k ≤ M
   sine modes, M = 4, 8, 16, from a sin x at a/ν = 0.03–10, and ρ = a‖F₂‖/ν grows with M; R10 on
   the half-plane modes |k|² ≤ 4, 5, 9, 16 (M = 12–48), 25 (80) and, for the tensor layout only,
   49 and 100 (148, 316), ν = 1, the pair at a/ν = 3, 10, 30 over T = 1 and T = 1/8 at 30. One
   sentence of physics: the truncation conserves energy and enstrophy without viscosity. The
   wavenumber k collides with the order k locally; say so once.)*
8. **§6.8 Preparation versus projection (0.6 p; `sec:prep-vs-proj`).** **Table T8**: which route
   sits on which side, and why. *(v3.2: columns Route | forms run | kernel | what a filter returns
   | what a trusted kernel certifies; no "precondition" column. The time-axis advantage hedged as
   C-09/C-10 state it: lower in every Navier–Stokes pair, and on R8–R9 from n_t = 4; it narrows as
   the coupling's norm grows with the modes.)* **The caveat that matters:** a unique, trusted kernel certifies the
   lifted *linear* problem, not the lift's convergence, which is measured separately (§8.4). One
   sentence tying back to §5.1: the mass form is the same banded left factor, applied in time.
   Close: the answer to Q(iii) in two sentences, and §8.4–8.5 named as its evidence.

**Figures and tables.** T8 (`tab:prep-vs-proj`). No figure; R7's numbers go to §8.4. *(v3.2 cut, 2026-10-12: `prop:fold-optimal` moved to App. E with its proof, the body keeping one paragraph on the folds; the tensor layout's circuit, the matchings' construction, the lift's spectrum and level scale, R7's rows and the fluids' parameters likewise. App. E adds `tab:lift-circuits` and `tab:doubled-kernel`. Body ≈ 7.2 pp against 6.)*

**Appendix offloads.** Appendix E, in the chapter's order: (opening section, `app:systems`) the
system rows in full, the padding, the ratio rows and their three-term circuit, the matchings by edge
colouring, the realification map and its kernel equivalence, the real embedding of the Fourier
variables; then the doubled-space algebra, its kernel and `prop:no-penalty`'s proof; the symmetric
and tensor layouts and the space–time forms; the folds and `prop:fold-optimal`'s proof; F₁ and F₂
for Burgers and Navier–Stokes in full.

**Marker checklist.** The scope gap stated from the paper's own words, and Q(iii) at the head; the
thread (one state, a coupled linear system) visible in the opening and in §6.5's first sentence;
systems and lifts rebuildable from body and Appendix E; the mass form *applied*, not redefined (§5.2
owns it); realification stated as the route run, with R7 as its instance; every complex-valued claim
scoped (formulation; one encoding verified; preparation not built); "prepared" never for the doubled
space; ρ stated as sufficient; the fold's α = 2 called tight (within 1.21), not optimal; the DCT named
as unbuilt with the reason; uniqueness attributed to Carleman; trust distinguished from convergence;
each construction stated once in the chapter (matchings, ratio rows, the time axis).

**Traps.** "Handles complex equations" unscoped; any complex-valued result that rests on the legacy
`DESolverLib` (never cited); redefining the mass form or restating its kernel theorem; calling the
tensor encoding "prepared"; claiming higher-order systems were run; "vector-valued solver"; "K²
terms"; "both forms" for the doubled space; ρ < 1 as necessary; "optimal" for the fold; re-deriving
the space–time rows in §6.5 (they are §6.1's with Γ → Γ_K); a second statement of the matchings
outside §6.6.

---

### 5.7 Chapter 7: Preparing and Verifying the Ground State (6 pp; Model Formulation /30)

**Purpose.** Specify everything shared by both forms after the residual is built, and design the
numerical experiment, so a reader could "create equivalent models". The forms differ only in the
residual, so every difference in Ch. 8 is a difference of Hamiltonians.

**Criterion (Modelling, verbatim):** "described in sufficient detail to permit readers to create
equivalent models. This should include: **a description of any software tools used and/or created;
a description and/or diagram of the model configuration; descriptions of the model input options
selected (boundary conditions…)**". Band 3 names "**poor design of numerical experiment**".

**Sources.** `docs/02_methods.md` (all sections; it is this chapter's source of truth); Planning §3.5,
§3.7–3.8, §5.4, §6.2, §7; claims C-03, C-04, C-08, B-13, B-16, B-17, B-24; `docs/15_filters.md`;
`docs/companion/` 40–47 and 70–76.

**Scaffold.**

1. **§7.1 Overview and model configuration (0.75 p).** **Figure F1**, the model configuration:
   problem specification → residual (standard | descriptor; nonlinearity none | doubled | Carleman;
   shared constraint rows) → stacked-residual block encoding U_R → reflection V → walk W → GQSP
   filter → post-selection → decoded field, with the classical reference and the verification modes
   and tiers attached to the stages they check. Its caption stands alone. The design principle in one
   paragraph.
2. **§7.2 Problems and model inputs (1.0 p).** The benchmark ladder R1–R10 by pointer (**Table T3**
   moved to §4.1 beside the running example, v3.5, `StructuralReview.md` F7; full specifications →
   Appendix H).
   **Table T2**, the constraint kinds (zero, collapse, ratio, datum slice): the rubric's "boundary
   conditions". **`tab:run-inputs`** (v3.2, 2026-10-12): every input option with its values and
   default, for the checklist's "every input option named, with its value"; the body names the
   options and the table sits in Appendix H (`app:run-options`). A problem is data: equation terms, constraints, regular datum, reference. The paper's
   panels as printed appear only in Appendix I (T-27). The inputs every run records: n per axis,
   form, encoder, filter, ε = 1e-6, initial state, rescaling, Carleman order K.
3. **§7.3 The classical reference (0.5 p).** The smallest right singular vector of the stacked R:
   dense SVD to 8,192 physical columns, its accuracy Wedin's bound ε σ_max/(σ₁ − σ₀), the square
   root of the eigensolver's ε‖H‖/Δ (so `eigh(RᵀR)` is never used: one number, R2a's relative gap
   at n = 8 below 2⁻⁵²; the table → Appendix G); beyond, shift-invert Lanczos on the augmented
   system [[I, R], [R†, −μI]], which never squares R, then Rayleigh–Ritz, with an a posteriori
   estimate. Trusted means a one-dimensional kernel with its ratio above 20, the largest spacing the
   ladder's spectra show without one. Decoding, η_e, and the metrics at three levels (operator,
   state, field).
4. **§7.4 From stacked residual to quantum walk (0.75 p).** **Proposition (stacked reflection)**:
   for U_R encoding R = [R_1; …; R_L] with α_R = √(Σα_j²), V = U_R†(2Π − I)U_R is a Hermitian unitary
   with Π_in V Π_in = 2H/α_R² − I, and controlled V needs only controlled reflections (proof →
   Appendix F). W = (2Π_in − I)V, Π W^k Π = T_k(H′). The quadrature composition has no ℓ¹ penalty.
5. **§7.5 The filter and its parameters (1.0 p).**
   - GQSP realises any |P| ≤ 1 polynomial of the walk, without parity (prior art, §2.4).
   - **The minimax edge filter**, P = T_d(w(x))/T_d(w(−1)), w mapping the excited spectrum [x₁, 1]
     onto [−1, 1], at the least degree that suppresses it to ε relative to the ground value:
     d = ⌈arccosh(1/ε)/θ₀⌉, θ₀ = arccosh(−w(x₀)), computed from heights above the edge so the ground
     state's is resolved.
   - **The parameters are a priori:** the edge (σ₀, σ₁ of the reference) and α_R, never the
     solution. The edge is assumed known, the standard known-gap assumption; say so here and in
     §9.5. The paper's time rule contains no ε and falls short of it (one sentence; App. I), which
     is why the degree is set from the edge.
   - **Why minimax:** at equal suppression it needs 1.67–1.92 times fewer degrees than imaginary
     time with the ground state at the edge, in both forms (B-17); at equal *measured* infidelity
     the gain is smaller and reverses at loose ε. Imaginary time, e^{−β(1+x)} with
     q_k = (2 − δ_{k0})(−1)^k e^{−β} I_k(β) and **Σ|q_k| = 1** (proposition, C-04), is the paper's
     filter, run in the reproduction and the study.
   - Phases from Weiss's complement and the inverse NLFT (cited); the realised polynomial matches its
     target to ≤ 1e-12.
   - **Initial states:** the geometric product state on the field block (n R_Y rotations, r = ±½,
     the candidate with the larger measured success probability kept); for a system, each field's
     block weighted by the problem's stated initial data, w₀/‖w₀‖; uniform and random as controls; γ
     always reported.
   - Success probability p → γ², amplitude amplification ⌊π/(4 arcsin γ)⌋ rounds, the total count.
   - **Deviations from Wu et al.:** one sentence pointing to Table T10 (`tab:deviations`, §4.4),
     which lists them all (T-34); none is restated here.
6. **§7.6 Verification and the error budget (1.0 p).**
   - **Table T4**, operator verification: *exact* (the whole block, one statevector per column, to
     1e-10‖X‖; to 25 qubits), *probe* (16 Haar-random and 4 structured vectors against sparse
     products, to 1e-9; every construction-only circuit of ≤ 24 qubits), *IR* (the compiled terms
     rebuilt as a sparse matrix, at any size). Why IR is not a tautology: it compares against an
     independently assembled operator.
   - State-preparation verification: T1, T2 and T3, and **the T2 ≡ T1 argument** (by qubitisation
     and GQSP the post-selected output depends on the encoding only through Π V Π), stated before any
     T2 number is used. The pre-run estimate that records a run beyond the budget, with the estimate.
   - Acceptance (state ≤ ε and within its a priori bound; circuit against T2 ≤ 1e-10; probability
     relative ≤ 1e-8; phases ≤ 1e-12; field ≤ ε_disc + B(d)).
   - **The error budget**: the filter, truncation and phases terms, each carried to the field by
     B(d); the encodings are exact and the readout classical, so ε_BE = ε_sample = 0.
7. **§7.7 Reading out the solution (0.25 p).** The field is decoded classically from the prepared
   state's field blocks and scaled by the regular datum. One paragraph: the paper's interferometric
   protocol is built and verified at small n (R1, R2a, R5a), with our correction for p_G < 1
   (`eq:readout-identity`; derivation in Appendix F), and its study at scale is future work.
8. **§7.8 Design of the numerical experiment (0.5 p).** What the study varies (n, form, encoder,
   filter, initial state) and holds fixed (constraints, ε); what counts as a gate (transpiled to
   {cx, u}, dense cited primitives counted apart); ancilla counted on the composed V. **Fairness,
   declared:** the structured encoding is the cheapest exact standard-form encoding built, but it
   is looser than the descriptor's, so the as-built comparison favours the descriptor by about the
   ratio of the two looseness factors (v3.2 correction, 2026-10-12). Every comparison is quoted as
   built and at α = ‖R‖ (T-25); only the ideal-bound comparison is a statement about the
   Hamiltonians. The tier is marked on every number.
9. **§7.9 Software and computation (0.25 p).** `pihm` (numpy, scipy, qiskit, qiskit-aer): one
   implementation per concept, problems as hashed data, tests of each claim; production on Setonix;
   every number regenerated from archived records by one command (Appendix J). No code listings.

**Marker checklist.** A configuration diagram; every input option with its value; the software
described; the experiment's design and fairness justified; the deviations from the paper pointed to
T10; the T2 ≡ T1 argument before any T2 number; the readout classical, the protocol attributed.

**Traps.** A software manual; "Pillar" and "tier" jargon; QITE presented as the comparison's filter;
the readout presented as new or as the method's readout.

---

### 5.8 Chapter 8: Numerical Study (10 pp; Results & Discussion /30)

**Purpose.** Evidence every claim of the Abstract and of §1.1, "without reference to any other
documents", one section per question or contribution.

**Criterion.** "Complete, clearly presented results, with detailed discussion showing insight… or
warranting publication." Every figure is interpreted in prose; each section ends with what it
established.

**Sources.** P8's records (`results-v1`) through `\res`; the reports `docs/11_pillar1.md`,
`12_pillar2.md`, `13_descriptor.md`, `15_filters.md`, `16_extensions.md`, `17_navier_stokes.md`,
`18_claims.md`; the results guide `docs/06_results_guide/` 82–87, ordered as this chapter; the
notebooks of Planning §10.8, one per figure.

**Opening (0.25 p).** The predictions of Chs 4–6 as claims about operators, and the order in which
they depend on one another (v3.6: no section roadmap); the tiers; the records' provenance in one
sentence; the full per-problem results → Appendix H; the reproduction of the paper → Appendix I.

**Scaffold.**

1. **§8.1 The pipeline is faithful (1.5 p; S1, S3; `sec:results-faithful`).** One opening paragraph
   of validation: the standard form's operators and solutions converge spectrally to the reference
   on every linear panel (R1–R5, best trusted error and its n), and the paper-faithful variant
   reproduces the paper where it should (one sentence, App. I). Operators equal the assembled
   residuals in every mode (**Figure F7**, nb 20). The circuit equals the emulation before
   normalising, ≤ 1e-10, on every minimax T1 record (nb 31). Every trusted preparation within ε and
   its a priori bound (nb 30); the decoded field within its budget (**Figure F8**, nb 32). What the
   answer-independent choices cost: γ for the initial states, and an underestimated gap (nb 33).
   The filter study in one table and two sentences (nb 34; B-17).
2. **§8.2 Where the cost lies (2.0 p; Q(i), Q(ii); C, S2; `sec:results-scaling`).** **Figure F9,
   the headline** (nb 40): against N, the encodings' looseness α_H/‖H‖, the Hamiltonians' relative
   gap, and the degree (which grows as the square root of the first over the second), for the
   paper's, the structured and the descriptor encodings, with fitted exponents; T2 points where
   measured and T3 beyond, visibly distinguished. **Table T7** (nb 21, 40): the paper's | structured
   | descriptor, across ‖H‖ scaling, gap, α/‖·‖, cx per query, ancilla, exactness, degree at n = 8
   as built and at α = ‖R‖, and the degree's exponent. **Table `tab:growth`** (v3.3, replacing the
   optional Figure F10): the degree's growth exponent on every linear panel and R7, both forms, as
   built and at the ideal bound, grouped by the classes of `tab:descriptor-regimes`; the reversals
   in prose (R3 at the ideal bound, and why R4a, whose coefficient vanishes at one end only, does
   not reverse; the heat panel → §8.3). Interpretation: the encoder's cost (the paper's to
   structured) and the Hamiltonian's cost (structured to descriptor) as two gaps on one plot.
3. **§8.3 The descriptor's gap and its rescaling (1.5 p; the challenge; `sec:results-gap`).**
   **Figure F11** (nb 42): the gap and γ² unscaled against rescaled, every panel; the ζ rule
   against the best ζ on a grid; where it stops (two axes, the singular ‖H‖ growth). **Figure F12**
   (nb 43): three representative problems in both forms, each with its solution and cost: R2c
   (stiff: rescaling's biggest gain), R3a (a leading coefficient with zeros: where the ideal-bound
   comparison reverses), R5b (heat on two axes: the gap still falls, and the descriptor costs more
   at small n). The rest → Appendix H.
4. **§8.4 Systems and nonlinear problems (1.5 p; Ch. 6, Q(iii), S4; `sec:results-nonlinear`).**
   **R7 first (one paragraph, nb 60):** the coupled oscillator, the realification of z′ = −iπz, in
   both forms and the chain ablation: field error, the mass form's gap against the chain's (about
   2.1×), degree, γ² under the data-weighted initial state, and T1 = T2. Then R6's kernel beside
   R8's (the projection evidence: kernel dimensions against one) (nb 61). R8: the K × n_t error
   surface and the degree in both forms (C-09). R9, viscous Burgers (**Figure F13**, nb 62): the
   lift's error per order follows a/ν (about a/5ν) and not ρ, which grows with the modes; the lift
   converges at a/ν = 3 and diverges at a/ν = 10 while its kernel stays unique and trusted (a/ν ≈ 5,
   where a/5ν reaches one, is an extrapolation: say so): a negative finding with its analysis.
5. **§8.5 Case study: two-dimensional Navier–Stokes (1.25 p; `sec:results-ns`).** **Figure F14**
   (nb 70): vorticity snapshots and the degree pairs. Taylor–Green validates F₁, the rows and the
   time axis (the lift exact to rounding). The vortex pair at a/ν = 3, 10 and 30, prepared (T2, T3)
   on 12–48 modes and built classically to 80 (v3.3 scope, checked at results-v1): the lift's
   convergence against a/ν and M, and the truncation against a direct simulation; at a/ν = 30 the
   lift diverges from 28 modes with its kernel trusted (a second instance of B-18's negative
   finding), and the window T = 1/8 restores it on 28 modes but not on 48; every exact emulation within ε; the
   descriptor's time axis lowers the degree in every pair, the ratio narrowing as the modes grow
   (C-10). The tensor layout to 316 modes in 2K − 1 terms, a native complex encoding verified but
   not prepared (§6.3), with its gates per query against the matchings (B-19). No circuit simulation
   was attempted on R10 (no estimate record exists): the narrowest prepared circuit, 27 qubits at
   n_t = 4, is wider than any simulated (20). Said plainly.
6. **§8.6 Summary of findings (0.5 p; `sec:results-summary`).** Six numbered findings, **at least
   two negative**, for example:
   1. the cost of the standard form is its Hamiltonian's;
   2. the descriptor's degree advantage: large on one axis, modest on two, reversed on the heat panel
      at small n and on R3 at the ideal bound;
   3. the descriptor's gap erodes where derivatives are uncontrolled; rescaling restores it on one
      axis only;
   4. the pipeline is verified end to end at every size it reaches;
   5. coupled systems run in both forms on one state, and the mass form beats a chain per field;
      Carleman prepares in both forms, but a trusted kernel can hide a diverging lift;
   6. Navier–Stokes is reached by exact emulation and estimate, not by circuit simulation.

**Marker checklist.** Every number's tier marked; "could not simulate" kept apart from "cannot
reach"; at most three in-depth problems; every caption stands alone; at least two negative findings;
every Abstract number backed here; the paper's reproduction a pointer, not a section.

---

### 5.9 Chapter 9: Discussion (3 pp; Results & Discussion /30)

**Purpose.** Explain and judge; never restate. "Insight into the significance of the work" is the
band-4 separator.

**Scaffold.**

1. **§9.1 Why the descriptor form wins, and what it costs (1 p).** Norm, not encoding: eliminating
   derivatives multiplies norms; carrying them keeps each block O(N). The same mechanism that buys
   the norm weighs the gap (the norm carries every derivative): one idea, two consequences. The
   price: the block register, the per-query constant, rescaling, and no remedy on two axes or at a
   double zero. The classical mirror: first-order least squares and the ultraspherical method found
   the same trade.
2. **§9.2 End-to-end complexity (1 p).** In your own voice: d = Θ(√(α_H/Δ) log 1/ε) is the
   residual's effective condition number, so Θ̃(N^{2k}) against Θ̃(N) is the conditioning of an
   order-k least-squares discretisation against a first-order one. Total gates Θ̃(N poly n) against
   Θ̃(N^{2k} poly n) on a regular problem. **Neither is poly-log: say it first.** The minimax
   filter changes the constant, not the Θ. Hedge any "for every filter" statement to what Lin & Tong's
   optimality and the linear-system κ lower bounds support. The edge-known assumption. What this
   means for readers of the paper: its cost lives in the Hamiltonian it constructs, not in the
   circuits it reports.
3. **§9.3 Where the construction applies (0.5 p).** **Table T9**, an applicability map (Green's Fig.
   4.18 is the model): problem class (regular; singular with a simple zero;
   singular with a double zero; two-axis PDE; coupled first-order systems; complex-valued linear equations, by
   realification (formulation only: what doubles, what is not built); nonlinear with a converging
   lift; past the lift's boundary) × the descriptor's gain × what to do. Guidance a practitioner
   could act on.
4. **§9.4 Feasibility on fault-tolerant hardware (0.5 p).** Logical qubits, cx per preparation and
   depth at meaningful n from T3; set beside explicit resource counts for linear-system ODE solvers
   (Jennings et al.), hedged; why NISQ is out of scope.
5. **§9.5 Limitations (0.75 p).** Each with its analysis: no hardware; circuit simulation only at
   small n; the spectral edge assumed known; the DCT a cited primitive; the doubled space projects;
   Navier–Stokes bounded by emulation and estimate; the descriptor's Hilbert-space and per-query cost;
   the double zero excluded; the iterative reference's bound an estimate; trust is not convergence;
   complex-valued fields carried by realification only, with no native complex preparation; the
   paper's PDE and nonlinear panels unreproduced (App. I; the authors not contacted).

**Marker checklist.** Explains rather than restates; the complexity argument consistent with §3.5,
§4.6 and §5.7; every limitation owned with its analysis; consequences for the field drawn.

---

### 5.10 Chapter 10: Conclusions and Future Work (2 pp; Conclusions /10)

**Form (v3.17).** Two subsections, **§10.1 Conclusions** (about 1 p) and **§10.2 Future Work**
(about 1 p), after Gemini's point 10 (`GeminiReviewPlan.md` row 10): the v3.15 chapter's first five
paragraphs restated §§9.1–9.4 paragraph by paragraph and buried the further work, which the rubric
marks as half the criterion. **Ch. 10 reframes Ch. 9 and never re-derives, re-lists or re-numbers
it**: §9.1–9.5 hold the mechanisms and the inventory of limits, Ch. 10 what they mean, one sentence
for each point Ch. 9 proves and no mechanism retold. §10.1 is structured around the three questions
of §3.5 and may name them, (i)–(iii), with one pointer to §3.5; contribution labels (C, S1–S4) and
other section pointers stay out of the prose. §10.2's paragraphs carry bold run-in leads
(`\paragraph{…}`, as §3.5's), one open question each, with its motivation and one concrete first
step. **No results (author's rule, 2026-10-15):** Ch. 10 quotes no `\res`, no measured number and
discusses no result. Every point it uses is already proven by Ch. 9 from Ch. 8's results and
Ch. 7's method, and is stated as established; a point that needs a result is moved into Ch. 9 first
(the R2a division of the degree and the as-built bias went to §9.2, the R1 depth to §9.4). Problem
labels appear only in §10.2, to name where a first step would run. No new citations (works cited
elsewhere may be re-cited: `wu2025pihm`, `olver2013`, `cai1994fosls`, `liu2021carleman`); a claim
that needs a new source goes into Ch. 9 first. The v3.15 form (four movements, no subsections, no
run-in headings, no question numbers) and the v3.12 form before it are superseded.

**§10.1 Conclusions** (`sec:conclusions-answers`), in this order:

1. **Q(i).** Wu et al. priced one query and left the gap and the cost of differentiation open. The
   query count is the filter's degree; in their circuits its larger factor is the encoder's, which
   an exact structured encoding removes; the Hamiltonian's remainder is Θ̃(N^{2k}) for constant
   coefficients under every block encoding and every polynomial filter of the walk, so the cost of
   differentiation returns in the number of queries (§9.2).
2. **Q(ii).** Yes, with the same kernel: the banded factors kept apart (chain; mass form), Θ̃(N) on
   a regular problem (glossed in a clause); the price is the gap: block rescaling (no term for its
   rule, v3.16) restores it on one axis without ancilla at a gate cost fixed by the equation, about
   Θ̃(N²) on singular problems; on two axes it falls whatever the weights; the remaining prices are
   constants, so the advantage lies in the degree (§9.1).
3. **Q(iii).** Projection against preparation; the Carleman lift prepared in both forms to 2-D
   Navier–Stokes (T2, T3, named as exact emulation and resource estimate); the advantage survives
   through the time axis; uniqueness certifies the truncation only; ρ < 1 a worst case (§9.3).
4. **The thesis statement** and its implications: *ground-state preparation of a differential
   equation costs what its residual's conditioning costs, and conditioning is fixed by the
   formulation*; the filter, the encoder and the circuit change constants; neither form poly-log.
   (a) The encoder/Hamiltonian audit applies to any filter-based block-encoded algorithm, and a
   comparison speaks about Hamiltonians only at the ideal bound, as built favouring the tighter
   encoding (§9.2). (b) The degree has the linear-systems κ form; classical conditioning theory is the
   design toolkit (two pieces transferred); the classical solve already shows the conditioning
   (§9.2). (c) No speed-up over classical solvers claimed: log(1/δ) resolution, O(N) ultraspherical on
   one axis, an advantage possible only on several axes, where the gap is least secure; what is
   possible is a degree that tracks the classical cost in order on a regular problem, and nonlinear
   flows prepared as unique ground states.
5. **Two boundaries.** (a) The gap on several axes: a discrete coercivity that fails on two axes
   (an inference; the repairs tried, block rescaling and reweighting the datum rows, are stated in
   §10.2 and not repeated) (§9.1); the boundary lies where an advantage could exist. (b) The prepared state against the answer: edge,
   lift convergence and readout supplied classically, references that do not exist where the method
   would matter; depth, not width, places every preparation on error-corrected hardware (§9.4–9.5).

**§10.2 Future Work** (`sec:future-work` on its heading), four paragraphs with bold leads:

1. **A gap on several axes.** The question that decides whether the route competes with classical
   spectral solvers. Power weights on the datum rows were measured (§9.1, App. D): they raise the gap
   more than the norm and lower the cost modestly, but the weighted gap still falls with every qubit
   (never "the norm rises as fast", docs/14's claim, which the export did not bear out). The next
   question is whether any reweighting (alone or with block rescaling, untested), or added rows of
   the kind first-order-system least squares uses to make its functional coercive, supplies the
   coercivity (hedged; a specific FOSLS device needs a source, which goes into Ch. 9 first). First step: datum rows on the carried derivative blocks of Laplace's equation (R5a),
   which leave an exact kernel unchanged. Then the full ultraspherical reduction, with §9.5's
   expectation (Θ̃(N) on a regular problem, suggested, untested): build it and measure R2a, R3 and
   R5b.
2. **Deriving the block weight.** The two constants of ζ's rule were selected by calibration and
   held fixed; the concentrated states' quotient already fixes ζ's growth with N, so derive the
   weight, constants and crossover between the classes included, from the equation (the item §5.4
   points to); first step: the regular coefficient that dips towards zero (App. D). The floor
   beneath it: whether a diagonal structured in the Chebyshev index, cheap to encode, does for the
   degree what diagonal preconditioning does for the ultraspherical method, or whether N is the
   least on one axis.
3. **Self-certification.** A quantitative `thm:flat-gap` for constant coefficients (the explicit
   solution operator in place of compactness), checked on R1 and R2; on-circuit edge estimation from
   the walk's eigenphases elsewhere; consecutive Carleman orders as a reference-free convergence
   test, checked on existing references (Burgers between a/ν = 3 and 10, R9); a shot-count study of
   the interferometric readout on R2a.
4. **What the residual carries.** The residual as an interface (rows for fields, realified complex
   equations, in principle data); native complex preparation (complex loaders, no new filter;
   z′ = −iπz natively against R7); noisy data rows, whose least-squares fit may lose the gap (first
   step: noisy observations added to a regular problem). Close on the shift in one sentence: the
   route was built from its circuits outward; its cost is decided by the residual, best conditioned
   before it is encoded.

The live `\Cref{sec:future-work}` (§5.4 deriving ζ; Ch. 6 native complex; Ch. 7 readout; App. K
data rows) all land in §10.2, and Ch. 9's closing hands off to it. Dropped: the gate-level DCT.

---

## 6. Appendices (outside the page limit)

**Restructured 2026-10-15** (13 → 11; this table and every letter in this file use the new scheme). The
gate reference was deleted (§2.1 cites Nielsen & Chuang); everything that tests the paper (the
paper-faithful conventions, the Laplace invariant set, the published circuits) joined the
reproduction and audit (I); the tier-labelled filter and edge studies and the fluid problems' data
joined the catalogue (H); the order follows the chapters. Labels are unchanged. Material moved to
the repository is staged verbatim in `3_footer/appendices/_offload_to_pihm.tex` until ported. Old →
new: B→A, C→B, E→C, G→D, H→E, F→F, I→G, J→H, D and K→I, L→J, M→K.

| | appendix | content | cited in |
|---|---|---|---|
| A | Chebyshev and ultraspherical identities | normalised basis, S, G's entries, structure and Θ(N²) (`app:cheb-G-norm`), the B̃/D̃ recurrence, the ultraspherical connection, the N = 4 instance | §2.3, §4.2, §5.1 |
| B | The standard form in full | the finite-system step (`app:pihm-constraint-proof`); the worked N = 4 residual; ℳ_{x^p}, ℳ_a, 𝒩₁, 𝒩_x; the residual on any number of axes (`app:pihm-multi-axis`); the datum-slice rows (`app:datum-slice`); the R3c/R3d substitution (`app:legendre-substitution`); the uniqueness count and its proof (`app:uniqueness-count`); the exact constraint points (`app:exact-points`); lifts and folds (`app:lifts-folds`). Nothing paper-faithful (T-27) | §4.1–4.4 |
| C | The structured exact G encoding | the factorisation proof; Λ, U_odd (subtraction with borrow), R₀; the cost proof; α across n (`tab:alpha-G-full`); the Bessel-kernel limit and ‖G^k‖₂ = Θ(N^{2k}); the standard form's gap bound (`prop:std-gap-bound`) | §4.5–4.6 |
| D | The descriptor construction in full | block rows; the padded count; the mass form; the kernel-equivalence proof; the gap mechanism and its ruled-out artefacts; the proof of `thm:flat-gap`; the rescaling rule and its checks; the term IR and its compilation; the cost proof | §5.2–5.6 |
| E | Systems and the nonlinear route in full | **(opening, `app:systems`)** the system rows in both forms and the padding; ratio rows and their three-term circuit; the coupling as matchings by edge colouring; realification and its kernel equivalence; the real embedding of the Fourier variables; **then** the doubled-space algebra and kernel and the p-copy extension; the Carleman lift (symmetric and tensor layouts, the level scale, the tensor layout's complex weights); space–time forms; the folds (α = 2 within 1.21 of ‖𝒩₁‖₂); Fourier–Galerkin F₁ and F₂ for Burgers and Navier–Stokes (the problems' data are H's) | Ch. 6 (§6.1–6.3, then §6.4–6.7) |
| F | Shared pipeline identities | the stacked reflection; qubitisation (one power, then one restriction); the controlled walk; imaginary-time coefficients and Σ\|q_k\| = 1; the minimax edge filter and its degree; GQSP and its phases (the phase-finding recipe in the repository); amplification and the ideal-encoding degree; the readout identity for p_G < 1. Identities and proofs only: no tier-labelled result | §7.4–7.7 |
| G | Verification and the classical reference | modes, sizes and tolerances (structured probes and per-atom checks in one paragraph); `eigh` against SVD (`tab:eigh-vs-svd`) and Wedin's bound against the eigensolver's; the iterative reference and its checks against the dense SVD; the trust threshold; the T1 memory and time model; acceptance and the error budget | §7.3, §7.6 |
| H | Benchmark problems and results by problem | R1–R10: equations, references, constraints, data (the fluid problems' runs and initial conditions, `app:fluid-data`); the constraint kinds and run options; the per-problem results tables (both forms, tiers); the filter study and the underestimated edge (`app:filter-studies`) | §7.2, §8.1, §8.3 |
| I | The reproduction and audit of Wu et al. | the paper-faithful variant's conventions (`app:faithful-conventions`; the printed SM §A matrices in one sentence, A-01); every printed panel's η and errors, as printed and as run (**Table T6**, `tab:eta-reproduction`, one merged table); the Fig. 5 triage (**Figure F6**, `fig:faithful-vs-corrected`; `tab:app-fig5-triage`); the non-reproduced Figs 6–7 and the hypotheses tested, the printed errors and the Laplace invariant set (`app:repro-unreproduced`); every claim A-01–A-13 with its derivation and verdict (`app:paper-claims`, `tab:paper-claims`): positive definiteness and distinctness, the uniqueness count's role, the PDE invariant sets' rank loss, the time rule's suppression bound e^{−1/(n−1)} and its measured shortfall (`app:edge-study` in H), the readout identity's p_G correction (pointer F); Wu et al.'s circuits as rebuilt (`app:pihm-circuit`: `app:published-build`, `app:ladder`, `prop:epsilon-G`, `tab:app-epsilon-G`); the paper's filter (`app:paper-filter`); the tau ablation (`app:repro-tau`); the QITE T1 records' agreement with T2 | §3.3, §3.5, §4.4, §4.5.1, §7.5, §9.5 |
| J | Software and reproducibility | one page: the repository at a frozen reference (tag `results-v1`, commit, DOI); architecture, records and provenance, campaigns and Setonix, tests, regenerating every figure and number, environment — a few sentences each, the detail in the repository | §7.9, §8 |
| K | Research proposal, with deviations | the proposal verbatim and the deviations table (§13.4) | – |

**Writing order (v3.14).** What is still to write, in order of the marks at stake, each against the
REVISE scaffold in its file:
1. I, `app:repro-unreproduced`: the hypotheses tested for Figs 6–7 (R-D1, R-D2), one paragraph per
   figure. §9.5 says "not reproduced under any hypothesis tested" and points here; nothing answers it yet.
2. I, `app:paper-claims`: the derivations behind A-09, the uniqueness count and the PDE sets' rank loss,
   A-11 (the suppression bound e^{−1/(n−1)} and `eq:time-rule-shortfall`), and the readout pointer,
   adapted from the Chapter 4 first-pass prose commented out under the claims table.
3. I, `app:faithful-conventions`: the paper-faithful conventions, one line each, and A-01 in one sentence.
4. F, `app:gqsp-phases`: one sentence for phase-finding steps 2–4 (the citations survive in Ch. 2), then
   fix "in four steps".
5. G, `app:verification-modes`: one paragraph for the structured probes and the per-atom checks.
6. H, `app:fluid-data`: smooth the join of the moved Burgers sentence.
7. The repository: port the blocks of `_offload_to_pihm.tex` into `pihm`'s docs; freeze tag `results-v1`
   (commit hash; a Zenodo DOI if possible). J cites the repository, so this precedes J.
8. J: the one page.
9. Optional: E's one clause on the inviscid truncation's conservation; B's pointer to the three-axis
   example; A's 8 × 8 chain (keep or move).
10. Build, check the merged Table T6's width, and run a Verification Mode pass over A–K.

**The pointer rule:** never "see Appendix C"; write "the factorisation's proof and the borrow-flag
SELECT are given in Appendix C". **Appendix I** is where a reader who wants to check the paper goes;
it is written as a record with derivations, not as a narrative, and it may use "as printed" and the
paper-faithful variant names freely. **Appendix J** exists for the rubric's "software tools" and the
guidelines' "laboratory handbook" role; keep it factual and to one page, the detail in the
repository as the guidelines' "accompanying document" (Part B, items 12–13), cited at a frozen tag.

---

## 7. Figures and tables

**Body figures** (the figure test applies to each; optional ones go first if over budget):

| # | figure | section | source | tier |
|---|---|---|---|---|
| F0 | *dropped (v3.13)*: concept figure of the two costs; the opening's number and `tab:headline` carry it | — | — | — |
| F1 | model configuration (the pipeline) | §7.1 | TikZ | n/a |
| F2 | the GQSP circuit (optional; dropped from the body 2026-10-12, App. F if wanted) | §7.5 | quantikz | n/a |
| F3 | U_odd's SELECT (subtraction with borrow) | §4.5.3 | quantikz | n/a |
| F4 | sparsity of A_std against A_desc | §5.1 | `pipeline.solutions` structure view | exact |
| F5 | the descriptor's flat LCU | §5.5 | quantikz | n/a |
| F7 | verification accuracy against n | §8.1 | nb 20 | exact/probe/IR |
| F8 | decoded field with its error budget | §8.1 | nb 32 | T1/T2 |
| F9 | **headline:** looseness, relative gap and degree against N, three encodings | §8.2 | nb 40 | T2 + T3 |
| F10 | (replaced by `tab:growth`, v3.3) | §8.2 | – | T3 |
| F11 | the gap and γ², unscaled against rescaled | §8.3 | nb 42 | classical |
| F12 | three representative problems, both forms | §8.3 | nb 43 | classical + T2/T3 |
| F13 | the lift's convergence against a/ν (R9), with R8's surface | §8.4 | nb 61, 62 | classical + T2 |
| F14 | Navier–Stokes: vorticity and the degree pairs | §8.5 | nb 70 | T2 + T3 |

**Appendix figures:** F6, the panels as printed against the problem (Fig. 5), and the triage
(Appendix I; nb 11; classical).

**Body tables:** T1 approaches (§2.2); T2 constraint kinds (App. H, v3.4); T3 benchmark ladder (§4.1, v3.5, `StructuralReview.md` F7);
`tab:run-inputs`, the run options (App. H, named in §7.2); T4
verification modes (§7.6; the acceptance criteria, `tab:acceptance`, in App. G); T5 descriptor block rows (§5.2); **T7 the headline
three-encoding table (§8.2)**; T8 preparation versus projection (§6.8); T9 applicability map
(§9.3); **T10 deviations from the printed method (§4.4, `tab:deviations`)**; `tab:filter-study` (§8.1) and `tab:growth` (§8.2) (v3.3); `tab:alpha-G-short`
(§4.5.3). Appendix tables include T6 (`tab:eta-reproduction`, App. I) and
`tab:published-verdicts` (App. I). Ch. 6's one body table is T8; R7's numbers go to §8.4.

**Captions** (style guide §3.4): a bold claim, then what is plotted, on which axes, for which
problem and parameters, then each panel, then the takeaway, then the tier. Figure captions below,
table captions above.

---

## 8. Notation

### 8.1 Master table (it becomes `1_header/6_notation.tex`)

| symbol | meaning | first use |
|---|---|---|
| n, N = 2ⁿ | qubits per Chebyshev axis; truncation dimension | §3.1 |
| k; p | equation order; polynomial degree of a nonlinearity | §3.2; Ch. 6 |
| τ(x), \|τ(x)⟩ | the paper's raw Chebyshev feature state | §3.1 (named), §4.1 (entries) |
| ψ, η, η_e | normalised coefficient state; scale; η_e = ‖b‖² | §3.1; §4.1 |
| φ_k | normalised Chebyshev basis functions φ₀ = T₀/√N, φ_k = T_k/√(N/2); τ(x) is the vector of their values | §4.1 |
| ψ_e | the ideal state b/‖b‖ of the truncation f_N (distinct from the prepared ψ_g and the classical ψ_ref); the model represents f_N exactly at (ψ_e, η_e) | §4.1 |
| ψ_init | the filter's initial state (was φ₀) | §7.5 |
| G | differentiation (dense, strictly upper triangular; ‖G‖₂ = Θ(N²)) | §3.2 (named), §4.2 (entries) |
| B̃, D̃ | banded factors, G = B̃⁻¹D̃ | §5.1 |
| ℳ_{x^p}, ℳ_a | multiplication (lift; smooth coefficient) | §3.2; §4.2 |
| 𝒩₁, 𝒩_x | product-to-sum folds | §3.4 |
| 𝔹(x), 𝔻⁽⁰⁾(x_s) | rank-one zero and collapse rows | §3.2; §4.3 |
| x_z, x_m, x_s | constraint points (zero, extremum, datum point, where f(x_s) ≠ 0) | §3.2 |
| A_std, A_desc; H_std, H_desc | residuals; Hamiltonians H = R†R | §3.2, §4.2, §5.2 |
| R = [R_1; …; R_L]; σ₀, σ₁, σ_max | stacked residual; its singular values | §4.4; §7.3 |
| 𝕊_a(x*), ĝ | datum-slice row on axis a at x*; the datum function's coefficients | §4.3 |
| w = (f̂⁽⁰⁾; …; f̂⁽ᵏ⁾); n_f | descriptor state (chain); block-register qubits | §5.2 |
| ζ | block-rescaling constant | §5.4 |
| α, α_R, α_H = α_R² | subnormalisations | §2.4 (`def:block-encoding`), §4 opening, §7.4 |
| V, W, H′ = 2H/α_R² − I | reflection; walk; normalised Hamiltonian | §7.4 |
| Δ, γ | spectral gap λ₁ − λ₀; overlap \|⟨ψ_ref\|ψ_init⟩\| | §2.4, §7.5 |
| d, ε | filter degree; target | §2.4 (`eq:degree`) |
| x₀, x₁, w(·), θ₀ | ground value and edge of the excited spectrum on H′'s scale; the edge map; the minimax rate | §7.5 |
| β, q_k | imaginary time and its Chebyshev coefficients (the QITE filter) | §3.3; §7.5 |
| p_G | the filter's success probability | §7.5 |
| K, M, ρ, s | Carleman order; modes; worst-case ratio; level scale | §6.5 |
| F₁, F₂, Γ_K | linear and quadratic terms; lifted generator | §6.5 |
| a, ν, T, n_t | amplitude, viscosity, horizon, time-axis qubits | §6.7 |
| C; z; Γ | number of components of a system; its state (one block per component); its coupling matrix | §6.1 |
| 𝔽, y, y_a, y_⊥ | ratio row; the vector datum, its anchor component, its off-anchor part | §6.2 |
| w₀ | a system's stated initial data (weights the initial state) | §6.2, §7.5 |
| c = Re c + i Im c | a complex coefficient in the realification example | §6.3 |
| ‖G‖_S | the paper's max(‖GGᵀ‖₁, ‖GᵀG‖₁) | §3.3 |
| R₀, U_odd, Λ | the structured factors of G | §4.5.2 |

### 8.2 Collisions (Planning or code → thesis)

| Planning / code | clash | thesis |
|---|---|---|
| τ (imaginary time), `tau` | τ(x) feature state | **β** (T-08), QITE only |
| φ₀ (initial state) | φ₀ = T₀/√N, a basis function (§4.1, App. A) | **ψ_init** |
| τ̃(x) (the paper's point-normalised τ/‖τ‖) | B̃, D̃ use the tilde; the thesis keeps τ raw | name it once in §4.1 as the paper's τ̃, never use it |
| R (Carleman ratio) | stacked residual R | **ρ** (T-09) |
| λ (block rescaling) | eigenvalues λ₀, λ₁ | **ζ** (T-19) |
| p_j (descriptor blocks); p_k (filter coefficients); p (success) | p nonlinear degree | **f̂⁽ʲ⁾**; **q_k**; **p_G** |
| SHIFTˢ (shift offset) | s the lift's level scale | write the offset as ℓ |
| T1/T2/T3 (tiers) | T_k Chebyshev; T horizon | tiers only in words or upright text labels in tables, never as maths |
| P (padded dimension) | P(z) GQSP polynomial | **dim w** |
| bare A, H | both forms | subscripts (T-07) |
| 𝔾, 𝔸, 𝕄, 𝕟₁, 𝕌 (the paper's and the plan's blackboard bold) | M (Carleman dimension), A (residual), n (qubits), U (unitaries) | G; Γ; ℳ; 𝒩₁; U_CG (T-06, v3.7) |
| ℳ (a matching, App. E) | ℳ the lift | **𝒫** |
| Gᵀ applied to ψ (the paper's print) | upper-triangular G | G, no transpose (T-16) |
| B̃_std (raw basis) | std = standard form | **B̃_raw** (T-19) |
| β (the paper's ladder coefficient) | imaginary time | **μ** (T-19) |
| κ (condition number) | – | **cond(·)** (T-19) |
| α, β (qubit amplitudes, §2.1) | subnormalisation; imaginary time | resolved v3.5: §2.1 no longer names amplitudes |
| w (off-anchor data) | w the descriptor's state; w(·) the edge map; w = u/s the lift's variable | **y_⊥** |
| a (a complex coefficient, realification) | a the amplitude (fluids); a_j the equation's coefficients; α subnormalisation | **c** |
| ρ (rank of constraints, uniqueness lemma) | ρ the Carleman ratio | **r** for the rank |
| T10 (table) | T1–T3 tiers; T_k Chebyshev | a table label only, written "Table T10" in the plan and `\Cref{tab:deviations}` in the thesis |

---

## 9. Claims → thesis register

Status follows `pihm/docs/22_claims_register.md` and `18_claims.md`. **Register:** **A** = assert;
**H** = assert with the stated hedge or scope; **N** = narrative only; **X** = do not state.
**Rule:** before a claim ID is cited in prose, its row reads ✅ (or ⚠️ as restated) in the
register at `results-v1`; if not, the prose is rewritten to what is supported.

| ID | claim, as the evidence states it | thesis | register |
|---|---|---|---|
| A-01 | G, ℳ, 𝒩₁, 𝔹 match the printed SM §A | §4.4 validation (one clause); App C, K | A |
| A-02 | printed η_e, 11 ODE panels, within one unit of the last digit (9/11 when rounded) | §4.4 validation; App K T6 | A |
| A-03/A-04 | Figs 6–7 η_e not reproduced, hypotheses tested | §4.4 validation (one clause); App K | A |
| A-05 | the Laplace solution is a typo (cosh for cos) | §4.3 one clause; T10 | A |
| A-06–A-08 | the paper's circuits' qubits, gates, prefactors and error | §4.5.1 (the prefactor); App D (all) | A per verdict |
| A-09 | H positive semi-definite where the discrete solution is exact; not always distinct at the bottom | §3.5 (named); §4.4 (as a property of H_std); App K (the Laplace set's bottom) | A (refined) |
| A-10 | doubled-space kernel ≥ 2^{2n−1} | §3.4 (the paper's count); §6.4; §8.4 | A |
| A-11 | the paper's time rule falls short of ε | §3.5 (named); §7.5 (one sentence); App K (bound and numbers) | A (refuted) |
| A-12 | "poly(n) terms": true for gates, not for α | §3.5; §4.5.1; §4.6 | A |
| A-13 | the printed n distorts 5a–5d; 3c, 4c, 4d untrusted at the printed n | §4.2–4.3 (mechanism, one clause each); App K (F6, triage) | A |
| B-01 | G = B̃⁻¹D̃ | §5.1 | A |
| B-02 | exact kernels coincide; elsewhere both forms' fields converge alike | §5.2 | A (restated) |
| B-03 | "O(1) ancilla" | – | X → C-06 |
| B-04/B-05 | α/‖·‖ → 1 on regular panels; ~2 singular; 2.3–4.1 on PDEs | §5.6; T7 | H |
| B-06 | gap Θ(1) on regular problems, proved (def:regular, thm:flat-gap, App. D); rescaled gap O(1) on one axis, measured on singular problems; still falls on two | §5.3–5.4; §8.3 | H |
| B-07 | relative gap, with the eigh/SVD distinction | §5.7; §7.3 | A |
| B-08/B-09 | old query and gate scalings | – | X → C-05, §9.2 |
| B-10 | Neumann costs Θ(N²) more | – | X |
| B-12 | nodal fold exact at α = 2, within 1.21 of ‖𝒩₁‖₂ (tight, **not** optimal); DCT cited | §6.6 | A |
| B-13 | the composed H verifiable only by parts | – | X: refuted, V verified exactly to 25 qubits |
| B-14 | one query's Haar-average success Θ(1) (descriptor) vs N⁻¹ per axis | §5.7 | H (compares encodings, not a pipeline cost) |
| B-16 | NLFT phases to high degree | App F | A |
| B-17 | minimax 1.67–1.92× fewer degrees at equal suppression; smaller and sometimes reversed at equal measured infidelity | §7.5; §8.1 | A (refined) |
| B-18 | Carleman: a unique kernel at every order; convergence follows a/ν, not ρ; trust misleads past it | §6.5; §8.4 | A (refined) |
| B-19 | tensor layout 2K − 1 terms, cost growing slowly with M; built on complex Fourier variables, verified, not prepared | §6.3; §6.6; §8.5 | A (refined) |
| B-20 | the descriptor avoids doubling for linear PDEs | – | X (neither form doubles) |
| B-21 | rescaling makes R2c reachable | §5.4; §8.3 | A (restated) |
| B-22 | only the descriptor prepares nonlinear solutions | – | X: refuted |
| B-23 | standard-form ground state unresolvable at n ≈ 7 | §5.7; §7.3 | A (restated: eigh fails from n = 8, SVD resolves) |
| B-24 | GQSP: any \|P\| ≤ 1, no parity | §2.4; §7.5 | A |
| B-25 | ⟨τ(x)\| an LCU of two product states, plus the constant mode | App D, F | A if used |
| C-01 | exact structured G; n + 4 ancilla for G alone | §4.5.2–4.5.3 | A |
| C-02 | α_H/‖H‖ bounded for constant coefficients; loose for R3's lifted multiplier | §4.6; T7 | H |
| C-03 | the stacked reflection's identities | §7.4 | A |
| C-04 | Σ\|q_k\| = 1; the circuit equals T2 before normalising | §7.5 | A |
| C-05 | degree Θ̃(N^{2k}) (standard, best encoding) vs Θ̃(N) (descriptor, regular); ~Θ̃(N²)+ on singular problems or on two axes | §4.6 (standard); §5.7; §8.2 F9 | H (measured exponents with fit ranges) |
| C-06 | ⌈log₂(n+4)⌉ + 8 ancilla for R2's system rows | §5.6 | A |
| C-07 | the ODE reproduction; Figs 6–7 documented | §4.4 validation; App K | A |
| C-08 | T2 = T1 ≤ 1e-10 | §7.6; §8.1 | A for minimax records; the QITE misses reported in App K |
| C-09 | Carleman: a one-dimensional kernel in both forms; the descriptor's time axis lowers the degree from n_t = 4 | §6.5; §8.4 | A |
| C-10 | NS: the descriptor's time axis lowers the degree in all pairs at fixed K; the ratio narrows with the modes | §8.5 | A |
| – | the readout identity for p_G < 1 | §7.7 (one sentence); App F | A |
| – | reversals at the ideal bound (R3) and on the heat panel at small n | §4.6 (R3 named); §8.2–8.3 | A (negative finding) |
| – | per-query gates higher in the descriptor at small n | §5.6; T7 | A |
| – | η > 0 is a sign convention; the decoded field carries the sign | §4.1 (one clause) | N |
| – | an order-k ODE needs constraints of rank k − 1 on its solution space and one regular datum | §4.3; App C | A (lemma, ODEs with a non-vanishing leading coefficient) |
| – | each printed choice alone floors the error; only both removed converge (Fig. 5 triage) | §4.3 (one clause); App K | A |
| – | the R3c/R3d substitution leaves simple zeros and converges spectrally | §4.3; App C | A |
| – | the stacked residual's H equals the paper's Gram sum | §4.4 | A (identity) |
| – | the standard form's departures change the data, never G or the Gram structure, so its ‖H‖ is the paper's | §4.4 | A (by construction) |
| – | a system's two forms share state, initial state and readout, and one kernel | §6.1 | A (theorem in §5.2) |
| – | R7: the mass form's gap ≈ 2.1× the block-rescaled chain's, flat in n | §6.1; §8.4 | A, once a `\res` key exists (plan §2.1) |
| – | matchings: fewer terms and smaller α than Pauli words for Γ | §6.6 | A, once keyed |
| – | a complex R gives a Hermitian PSD H; no non-Hermitian filter is needed | §6.3 | N (mathematical; no complex-R preparation run) |
| – | R7 is the realification of z′ = −iπz | §6.3 | N (identity) |
| – | complex-valued fields are prepared | – | **X**: realification only; native complex preparation not built (T-32) |
| B-18 (wording) | "past a/ν ≈ 5 the lift diverges" | – | **X** as worded: converges at a/ν = 3, diverges at 10; 5 is an extrapolation |

---

## 10. Code → thesis transfer

### 10.1 Sources of truth

1. **Results:** P8's records, the commit tagged `results-v1`, read only through the exporter and the
   notebooks. Nothing from legacy `Setonix/`, legacy notebooks or the old `docs/`.
2. **The method:** `pihm/docs/02_methods.md`, the method as built, and the companion. Where they and
   Planning.md differ, 02_methods.md and the tests win.
3. **Reasons:** Planning.md, `pihm/docs/20_decisions.md` and `21_decision_log.md` explain why; they
   are never cited. The thesis states each choice with its reason (plan §3.5).
4. **History:** the Journal is never cited. Lessons appear only where they are a correctness
   condition of the construction (one power then one restriction for qubitisation; a controlled
   global phase becomes a relative one; the raw τ), phrased as mathematics.

### 10.2 Numbers (T-15)

- **The exporter** (`pihm/tools/thesis/export_numbers.py --used-only`) writes
  `0_results/generated/numbers.tex` from the records, keyed like the record directories
  (`stateprep/R2a/standard/n8/T3/filter=minimax`); statistics over n come from
  `tools/thesis/derived.py` (`derivative/n<n>`, `build/<p>/…/best`, `…/floor`,
  `looseness/stateprep/…`, `stateprep/<p>/<form>/growth/…`). Rerun it after P8's copy-back and
  after any draft adds a key. To browse keys before citing, write the full export to a scratch
  directory (`0_results/README.md`).
- **The thesis quotes by key**, `\res{<run>}{<metric>}`; formats and flags are in
  `0_results/README.md`. A missing number renders its reason; *infeasible* is a legitimate final
  result ("beyond the simulation budget", estimate quoted).
- **Final.** `export_numbers.py --final` requires every quoted record's source digest to match the
  committed package source, and makes every draft-only placeholder an error.
- `\prov{…}` only for a number `pihm` does not produce; §14 fails on any left.
- Tolerances are quoted as the acceptance threshold *and* the achieved value.

### 10.3 Figures

- One notebook per figure (Planning §10.8): the notebook computes, the thesis shows. Export vector
  PDF in the shared style (`pihm.plotting`) at the thesis's font and column width into
  `Figs/generated/`. A LaTeX comment above each `\includegraphics` names its notebook and campaigns.
- Circuit figures are hand-written quantikz; check each against the verified circuit (registers,
  controls).

### 10.4 Translation table (code → thesis)

| code / Planning | thesis |
|---|---|
| `assemble(problem, regime, n, …)` | the residual |
| `regime="standard" / "descriptor"` | standard form / descriptor form |
| `layout="chain"`, the mass form | the chain / the mass form |
| `rescale="block"` | block rescaling |
| `encoder="structured" / "published"` | structured (exact) encoding / the paper's encoding |
| `compose.stacked_reflection` | the stacked-residual reflection V |
| `verify="exact"/"probe"/"ir"` | exact / probe / IR verification |
| `t1` / `t2` / `t3` | circuit simulation / exact emulation / resource estimate |
| `filter="minimax"` / `"qite"` | minimax edge filter / imaginary-time filter |
| `tau` | β |
| `ideal_degree` | the degree at the ideal-encoding bound |
| `trusted` | a trusted (isolated, one-dimensional) kernel |
| `status="infeasible"` | beyond the simulation budget, estimate quoted |
| `carleman=K`, `lift="tensor"` | Carleman order K; the tensor layout |
| `variant="faithful"` vs the bare problem | R2a as printed (App K and §4.4's validation paragraph only) vs R2a |
| "corrected" (reports' word for the problem as run) | the problem itself, unnamed |
| `assemble.systems`, components, `monomials` | a system; its components (Ch. 6) |
| `ratio_rows`, `"ratio"` constraint | ratio rows |
| `datum_rows`, `"datum"` constraint | datum slices |
| `matching_terms`, decision 42 | the coupling as a sum of matchings |
| `layout="chain"` on a first-order system | the chain ablation (labelled; Ch. 6, §8.4) |
| `real_embedding`, `fourier_field` | the real (cos/sin) basis; the complex Fourier variables (§6.3) |
| `NotImplementedError` for complex data | native complex data not built (§6.3) |
| Pillar 1 / Pillar 2 | operator verification / state-preparation verification |
| rung R1–R10 | benchmark problem R1–R10 |
| `ISSUE-0xx`, `D-0xx`, `E0xx`, probes | never cited; stated as findings |

### 10.5 Australian English

`[australian]{babel}`; reuse `pihm/tools/codespell/us_to_au.txt` on the `.tex` files before
submission. API names stay verbatim.

---

## 11. Writing order (by dependency; no dates, T-03)

Every gate has passed (G0–G6); P8 is running. Formulation can be written now; numbers follow P8's
copy-back.

| wave | unlocked by | write | notes |
|---|---|---|---|
| **W0** | this plan | the scaffold aligned to this plan (§4.3: Ch. 8, Ch. 9, Appendices B, I, G, I); the REVISE sweep (plan §2.1); the `ref.bib` audit and additions (T-29, plan §5.2) | structural only; zero undefined references |
| **W1** | now | Ch. 2; Ch. 3; Ch. 4; Ch. 5; Ch. 6; Ch. 7; Appendices A–G | maths and method; numbers render as their placeholders |
| **W2** | P8 copied back; exporter rerun | Ch. 8 in order §8.1 → §8.5; Appendices H, I, J; then every `\res` in Chs 4–7 checked | the numbers freeze |
| **W3** | W2 | §8.6; Ch. 9 | check §8.6's findings against P8 first (TR-1) |
| **W4** | W3 | Ch. 1; Abstract; Ch. 10; Summary of Student Achievement; App M; the title (T-14) | written last, so they promise only what was delivered |
| **W5** | W4 | Verification Mode; Review Mode per chapter; page count; §14; the supervisor's draft (guideline 9) | |

**Supervisor touchpoints (guideline 9: "a general layout for approval, then drafts").** Send §0.1,
plan §0.2 and §3.1–3.2 as the layout for approval, then drafts after W1 (Chs 2–5) and W4 (the full
draft).

---

## 12. Risks and fallbacks (the rubric protects well-analysed negative results)

| id | risk | likelihood | response in the thesis |
|---|---|---|---|
| TR-1 | P8's records move a finding (an exponent, a ratio, a reversal) relative to the pre-P8 values this plan quotes | medium | the text is written from claims and `\res`; before W3, re-read §8.6's findings and Table T9 against P8 and rewrite what moved |
| TR-2 | fitted degree exponents deviate from 2k and 1 | low–medium | report the measured exponents with their fit ranges; restate C-05 as measured |
| TR-3 | "no encoding beats Θ̃(N^{2k})" over-generalises | medium | claim it for polynomial filters of the walk, which need degree Ω(√(α_H/Δ)); a general lower bound is future work |
| TR-4 | circuit simulation only at small n | certain | designed for: T2 ≡ T1 proven and measured; said once in §7.6 |
| TR-5 | "isn't this ultraspherical, or FOSLS?" | high | credited first (T-26), with the increment stated in §2.3 and §5.1 |
| TR-6 | the concurrent sibling (Paine 2026) is read as pre-empting | low | cite it in §2.2 and §3.5 with what it does and does not do: alternative constructions and encodings, but no gap scaling in resolution, no circuits and no banded reformulation |
| TR-7 | a marker reads the reversals (R3 at the ideal bound; the heat panel) as weakness | medium | they are numbered findings with their mechanism, and Table T9 turns them into guidance |
| TR-8 | the known-edge assumption is attacked | medium | own it in §7.5 and §9.5; the edge without the reference is §10.2's self-certification item |
| TR-9 | page overrun | high | plan §4.1's trim order; Review Mode's per-chapter estimate; Ch. 3 and Ch. 4 drafted against 4 and 7.5 pp |
| TR-10 | the marker ticks Theoretical | low | the formulation chapters already read as journal methods; move 2 pp from Ch. 8 into Chs 4–5 |
| TR-11 | bibliography errors (wu2025pihm's authors) reach submission | certain unless fixed | T-29; §14.2 item 1 |
| TR-12 | Figs 6–7 stay unexplained | certain | recorded in App K as not reproduced, hypotheses tested, authors not contacted; one clause in §4.4 and §9.5 |
| TR-13 | Ch. 4's departures read as a changelog of fixes (code-map drift, Formulation marks) | medium | §3.5 rule 7; every departure and T10 row a defect and a property; Review Mode checks §4.2–4.4 for "we then", dates, issue numbers |
| TR-14 | the complex-valued material is read as an overclaim | medium | T-32's scope stated in §6.3's first paragraph; the X row of §9; T9 marks it "formulation only"; no complex number in the Abstract |
| TR-15 | prior art blurred into contribution in Ch. 4, which restates the paper's construction (Style Trap 13) | medium | the attribution sentence in Ch. 4's opening; a citation at every restated construction; "we" only for departures and our own results; T10 as the record of what differs |
| TR-16 | a marker or examiner asks whether the baseline is the paper's or a weakened version | medium | §4.4's fairness sentence (data changed, G and the Gram structure not) and validation paragraph; App K for the full record |
| TR-17 | the audit creeps back into the body (the time rule's derivation, the claims table, T6) | medium | T-36; Ch. 3 names, Ch. 4 argues departures only, App K derives and tabulates; Verification Mode checks it |
| TR-18 | the mass form is defined twice (§5.2 and Ch. 6) | low | §5.2 defines and proves; Ch. 6 applies and cites |

---

## 13. Front matter and required elements

### 13.1 Title (T-14; choose at W4)

- **Keep:** *Quantum Circuits for Solving Differential Equations via Physics-Informed Effective
  Hamiltonians and GQSP Quantum Imaginary Time Evolution.* (Names imaginary time, which is not the
  comparison's filter.)
- **Option A:** *Banded Physics-Informed Hamiltonians: A Descriptor Reformulation for Quantum
  Differential-Equation Solvers.*
- **Option B:** *Physics-Informed Hamiltonians for Quantum Differential-Equation Solvers: An Exact
  Baseline and a Descriptor Reformulation.*
- **Option C:** *Where the Cost Lies: Reformulating Physics-Informed Hamiltonians for Quantum
  Differential-Equation Solvers.*

The title page and both declaration dates use `\today`: set them to the submission date.

### 13.2 Abstract (≈ 250–300 words; five moves, each with a number)

1. The problem, and Wu et al.'s method, attributed, with its open question.
2. What we found: the cost is its Hamiltonian's, not its encoder's, shown on the standard
   form (validated against the paper's printed panels), with the three degrees at n = 8.
3. The descriptor reformulation: ‖H‖ Θ(N²) against Θ(N⁸), the same kernel, degree Θ̃(N) on a regular
   one-axis problem, O(log n) ancilla; its challenge and the rescaling.
4. How it is verified (T1 = T2 ≤ 1e-10) and how far it reaches (coupled systems and Carleman in both
   forms; 2-D Navier–Stokes on up to 80 modes). No complex-valued claim in the Abstract (TR-14).
5. The scope: classical computation, no hardware, neither form poly-log.

### 13.3 Summary of Student Achievement (one page, first person, required)

What *you* did: the audit of the legacy pipeline and the decision to rebuild; `pihm`'s design; the
reproduction of the paper and its triage; the standard form; the structured encoding; the descriptor
reformulation, its gap investigation and the rescaling rule; the verification framework and the
GQSP circuit engine; the filter study; coupled systems and their circuits; the Carleman and
Navier–Stokes extensions; the Setonix production; the thesis. Name the help received: the
supervisor; AI coding assistance, if the School's policy requires it to be declared (check it, and
mirror it in the Acknowledgements, guideline 8).

### 13.4 Research proposal deviations (Appendix K)

| proposed (May 2025) | outcome | why |
|---|---|---|
| QSVT → a generalised QSVT for complex-valued, non-Hermitian operators | GQSP throughout (no parity constraint); the filter only ever acts on the Hermitian H = R†R, so no non-Hermitian filter is needed; complex-valued linear equations carried by realification as coupled real systems (Ch. 6, R7), one native complex encoding verified (the tensor layout), native complex preparation not built | the cost analysis showed the binding constraint is the Hamiltonian's norm and gap, which had to be solved first; realification reused the systems machinery at no new cost |
| nonlinear PDEs (Burgers, NLS, Ginzburg–Landau) | Burgers and 2-D Navier–Stokes by Carleman; NLS and CGL not treated | the doubled space cannot prepare; the Carleman lift needs dissipation (NLS is not dissipative) |
| data-informed Hamiltonians | not pursued | scope; future work |
| (not proposed) | the reproduction of the paper and the standard form; the structured encoding; the descriptor reformulation; coupled systems in both forms; the verification framework | emerged from auditing the published method |

### 13.5 Formal requirements from the guidelines

12 pt; 1.5–2 cm margins; body 40–60 pages excluding contents, proposal and appendices; one-page
Summary of Student Achievement in the first person; the proposal as an appendix with deviations
noted; the supervisor's electronic signature; the signed declaration; help received acknowledged.
The seminar (25 minutes plus questions) is outside the document; F0 or F1, F9 and T7 carry it.

---

## 14. Pre-submission checklist

### 14.1 Content

1. Every §1.1 contribution is answered, through its question, in §10.1, and has evidence in Ch. 8 or Appendix I.
2. Every Abstract number has a `\res` key and a Ch. 8 location.
3. Every claim ID cited in prose reads ✅ or ⚠️-as-restated in the register at `results-v1` (§9).
4. `grep` finds none of: "collocation" or "the paper's regime" naming the standard form; "O(1) ancilla"; "+ 6" ancilla;
   "Θ̃(N²) floor"; "not verified end to end"; "corrected" anywhere in prose outside App. I's verbatim
   record; "as printed" or "paper-faithful" outside Appendix I and §4.4's validation paragraph;
   "warm start"; "K^2 terms"; "Pillar"; "rung"; "wall"; QITE as the comparison's filter; "prepared"
   beside the doubled space or the tensor layout; the readout protocol "reproduced" as the method's
   readout; "optimal" for the nodal fold; "a/ν ≈ 5" as a measured boundary; a complex-valued field
   "prepared" or "solved"; "we fixed" or an issue number in Ch. 4; a typed `pihm` number.
5. Ultraspherical and first-order least squares credited in §2.3 and §5.1; Paine 2026 cited.
6. The vocabulary of plan §3.4 holds throughout; every chapter arrives at its question and closes on
   a hand-off, with no section roadmap (plan §3.5 rule 1).
7. The tier marked on every quantitative figure and table; every as-built comparison has its
   ideal-bound twin.
8. The research proposal in Appendix K, with deviations.

### 14.2 Style and presentation (/10: "flawless")

1. `\nocite{*}` removed; zero `\todo`, `\prov`, `\placeholderfigure`, `REVISE` or `CITE-NEEDED`
   (`grep -rn` over `1_header 2_body 3_footer`); bibliography `note` fields suppressed; `ref.bib`
   audited (T-29); `export_numbers.py --final` succeeds and the final build has no `pihm` errors.
2. Compile clean: no warnings, no overfull `\hbox` in the body.
3. Every float referenced by `\Cref`; figure captions below, table captions above; every caption
   stands alone.
4. Acronyms defined at first use; the `glossaries` entries complete (GQSP, QSP, QSVT, QITE, LCU,
   NLFT, IR, QFT, DCT, DNS, IVP, BVP, SVD, PIHM, FOSLS, PINN).
5. The AU spelling sweep; "Wang" spelt correctly; the declaration signed; the supervisor's
   endorsement present.
6. Body 40–60 pages (target 55–58), 12 pt, 1.5–2 cm margins.
7. The whole thesis read aloud once.
8. "Published" sweep: `wu2025pihm` is a pre-print, so no visible prose, caption, table cell or
   section title may call it, its encoding, prefactor or claims "published" (use "the paper's",
   "the printed"). Grep `published` over `1_header 2_body 3_footer`; labels and keys
   (`sec:standard-published`, `tab:published-verdicts`, `app:published-build`,
   `eq:pihm-published-prefactor`, `encoder=published`) do not render and may stay, and genuinely
   published works (Olver & Townsend 2013, Cai et al. 1994) are exempt.

### 14.3 Rubric traceability (Modelling)

| criterion | marks | earned in | done |
|---|---|---|---|
| Intro & Lit: history and state of the art | /20 | Ch. 2 (§2.2 history), Ch. 3 | ☐ |
| — critical assessment (HD gate) | | §2.2(e) T1, **§3.5** | ☐ |
| — connection to the project | | Ch. 1's opening (the cost left open, the number), §3.5's three questions → Chs 4, 5, 6 | ☐ |
| Model formulation | /30 | Chs 4–7 | ☐ |
| — software tools | | §7.9, App L | ☐ |
| — model configuration diagram | | F1 (§7.1) | ☐ |
| — input options (boundary conditions etc.) | | §4.3, §7.2 T2, T3; App J | ☐ |
| — reproducible ("create equivalent models") | | Chs 4–7 + App B–I; `def:standard-form` and T10 (§4.4) | ☐ |
| — design of the numerical experiment | | §7.8 (fairness, conventions), §7.6 | ☐ |
| Results & Discussion | /30 | Chs 8–9 | ☐ |
| — self-contained results | | Ch. 8 + App J–K | ☐ |
| — significance for the field | | §9.1–9.4 | ☐ |
| — negative results analysed | | §8.3, §8.4, §8.6, §9.5 | ☐ |
| Conclusions & further investigation | /10 | Ch. 10 | ☐ |
| Style & presentation | /10 | throughout | ☐ |

---

*Companion documents: `CLAUDE.md` (the working agreement and Standing Facts),
`thesis_guides/STRUCTURE_AND_RUBRIC.md` (the rubric and exemplar reference),
`thesis_guides/STYLE_GUIDE.md` (register), `0_results/README.md` (quoting numbers),
`Code/pihm/docs/02_methods.md` (the method as built), `Code/Planning.md` (what was built and why).*
