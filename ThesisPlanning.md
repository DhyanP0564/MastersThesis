# ThesisPlanning.md: the thesis structure, built on `pihm` as built

## Turning the `pihm` rebuild into a submittable (and publishable) Master's thesis

*Version 2.0, 2026-10-01. Version 1.1 (adopted 2026-09-25) fixed the contributions, the Modelling
rubric, the notation and a ten-chapter scaffold, and wave W0 built that scaffold. Version 2.0
recalibrates the plan against four things: `pihm` as built (gates G0–G6 passed, P8 running on
Setonix), the School's marking guide and rubric, the two exemplar theses, and the literature. What
changed, and why, is §0.2. The new decisions are T-20 to T-29 (§1.4); they are adopted in this
version, and any of them can be vetoed. The `.tex` scaffold still follows version 1.1's chapter
order: migrating it is wave W0b (§11).*

**Premise.** `pihm` is built and verified through gate G6. Production (P8) reruns every campaign on
Setonix at one version of the code; that commit is tagged `results-v1`, and the thesis quotes only
its records, through `\res{<run>}{<metric>}`. **Numbers in this plan are planning values** taken
from `pihm`'s reports before P8. They locate the story; they are never typed into the thesis. Where
P8 moves one far enough to change a finding, §12 (TR-1) says what to do.

**How to read this.**

- §0 is the short version: the story, what changed, the chapter map and the status board.
- §1 is the decision record. §2 says how the other planning documents relate to this one.
- §3 fixes the contributions, the three questions, the spine sentence, the vocabulary and the
  rules that keep the thesis a scientific argument rather than a code map.
- §4 gives the page budget and the LaTeX tree. §5 goes chapter by chapter; it is the part you
  follow while writing.
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
costs. This thesis answers both, in six steps.

1. **Audit.** The method is rebuilt exactly. The printed η_e of all eleven ODE panels agree to
   within one unit of the last printed digit. The PDE and nonlinear panels do not reproduce, and the
   printed choices (rounded constraint points, Maclaurin sources) distort the solutions at the
   printed resolution. The paper's circuits are rebuilt and their claims tested.
2. **Where the cost lies.** The filter's degree is d = Θ(√(α_H/Δ) log 1/ε): the residual's
   effective condition number. Two walls hide in it. The *encoder wall*: the published normalisation
   of 𝔾 is about N³ looser than ‖𝔾‖, and our exact structured encoding removes it for
   constant-coefficient problems. The *Hamiltonian wall*: ‖H_std‖ = Θ(N^{4k}) for an order-k
   equation against a flat gap, so d = Θ̃(N^{2k}) (Θ̃(N⁴) for the paper's second-order panels)
   whatever the encoder.
3. **The reformulation (headline).** The descriptor form replaces the dense 𝔾 by its banded factors,
   𝔾 = B̃⁻¹D̃. An equation of higher order carries its derivatives as blocks tied by banded
   recurrences (the *chain*); a first-order equation or system is multiplied through by B̃ (the
   *mass form*). The kernel is unchanged, ‖H_desc‖ = Θ(N²), and the residual is one flat LCU with
   O(log n) ancilla. The idea has two classical antecedents, the ultraspherical spectral method
   (banded differentiation) and first-order-system least squares (conditioning); the increment is
   its transfer to a block-encoded Hamiltonian, with its consequences for ground-state preparation
   measured.
4. **Its challenge.** The descriptor's norm carries every derivative it carries. Its gap is flat
   only where the equation controls each of them: a one-axis ODE whose leading coefficient does not
   vanish. Where it vanishes, and on two axes, the gap closes with N, and the derivative blocks
   crowd the field block out of the ground state. An a priori block rescaling, folded into the LCU
   coefficients at no gate cost, restores an O(1) gap on one axis. On two axes the gap still falls,
   and a double zero is beyond any rescaling. Measured as built and at an ideal encoding, the
   descriptor needs 14–1200 times fewer queries on one-axis problems, modestly fewer on most PDEs,
   and more on the heat panel at small n and on the Legendre problem at an ideal encoding.
5. **Verified preparation.** One pipeline serves both forms: a stacked-residual reflection, its
   qubitised walk, GQSP with the minimax edge filter (chosen by a QITE–minimax study), a priori
   parameters and answer-independent initial states. Operators are verified exactly, by probe and
   by IR. The circuit simulation equals the exact emulation to 1e-10 wherever both run, and
   resource estimates carry the rest.
6. **Nonlinearity.** The paper's doubled space encodes exactly but projects: its kernel is
   exponentially degenerate. The Carleman lift prepares, in both forms. On Burgers and Navier–Stokes
   its convergence follows a/ν, not the worst-case ratio ρ, and past the boundary the kernel stays unique and trusted
   while the lift diverges. The descriptor's time axis lowers the degree in every Navier–Stokes
   pair, and the thesis culminates in 2-D incompressible Navier–Stokes: the Taylor–Green vortex and
   a vortex pair on 12–80 modes, and a tensor-layout coupling of 2K − 1 terms to 316 modes.

Neither form is poly-log, every result is a classical computation, and nothing ran on hardware.

### 0.2 What changed in version 2.0, and why

| topic | v1.1 | v2.0 | source |
|---|---|---|---|
| chapter order | pipeline (Ch. 4) before the two forms | story first: the standard form (Ch. 4), the descriptor (Ch. 5), nonlinearity (Ch. 6), then the shared pipeline and the numerical experiment (Ch. 7) | T-20 |
| Numerical Study | nine sections, by pipeline stage | seven, one per question or contribution | T-20 |
| the descriptor's challenge | one 0.75-page subsection on rescaling | its own subsection (the gap of a carried derivative) before rescaling, and its own results section | T-21; `pihm/docs/14_descriptor_gap.md` |
| first-order equations and systems | absent from the descriptor chapter | the mass form, the descriptor's second layout | T-22; decision 39 |
| the preparation filter | QITE, minimax alongside | the minimax edge filter for every comparison and extension; QITE for the reproduction and the filter study | T-23; decisions 35, 50 |
| readout | the paper's protocol reproduced, in the body | classical (the decoded state); the protocol built at small n, in Appendix F and future work | T-24; decision 27 |
| fairness of the comparison | as built | as built **and** at the ideal-encoding bound α = ‖R‖; reversals reported | T-25; decision 43 |
| descriptor ancilla | ⌈log₂(n+4)⌉ + 6 | ⌈log₂(n+4)⌉ + 8 for R2's system rows (12–13 for the reflection) | claim C-06 restated |
| α → ‖A‖ | everywhere | on regular one-axis problems; about 2 on singular ones, 2.3–4.1 on PDEs | B-04, B-05 |
| degree scaling | Θ̃(N) against Θ̃(N⁴) | Θ̃(N) for a regular one-axis ODE, about Θ̃(N²) or faster where the leading coefficient vanishes or on two axes; standard form Θ̃(N^{2k}) | C-05 restated |
| block rescaling | Θ(n_f) gates, λ fitted to R2c | a priori rule, folded into the LCU coefficients: no gates, no ancilla | decision 33 |
| S2's scope | α_H/‖H‖ bounded | bounded for constant coefficients; loose for R3's lifted multiplier | C-02 refined |
| antecedents | ultraspherical | ultraspherical **and** first-order-system least squares; concurrent work Paine 2026 | T-26 |
| variants | paper-faithful / corrected | the problem is unnamed; "as printed" only in the reproduction | T-27; decision 49 |
| classical reference | SVD | dense SVD to 8,192 columns, iterative shift-invert Lanczos beyond (to 524,288) | D-115, D-128 |
| trust threshold | gap ratio 100 | 20 | decision 40 |
| verification reach | exact at small n, probe ≲ 30 qubits | exact to 25 qubits; probe on every construction-only circuit ≤ 24 qubits; IR at any size | B-13; decision 50 |
| circuit simulation reach | about 20–22 qubits | to 26 qubits at n = 2; R10's T1 infeasible on its own estimate | METHODS §8 |
| initial state | geometric; warm start as a variant | geometric on the field block; a system's fields weighted by its stated initial data; no warm start | decisions 8, 45 |
| Carleman | ρ < 1 as the precondition | ρ is sufficient, not necessary; convergence measured; a trusted kernel can hide a diverging lift | decisions 41, 44; B-18 |
| tensor layout | K² terms | 2K − 1 terms | D-118; B-19 |
| doubled space | both forms | the standard form only | decision 36 |
| Navier–Stokes | 10a/10b, T2 small, T3 beyond | R10a–R10d on 12–80 modes, K ≤ 5; T1 infeasible; C-10 in 32 of 32 pairs | G6; D-120 |
| provenance | tag `results-v1` | the P8 commit is tagged `results-v1`; `--final` checks each record's source digest | D-130 |
| bibliography | not audited | `wu2025pihm`'s author list is wrong; audit before drafting | T-29 |

### 0.3 Chapter map

| # | chapter | pp | rubric criterion | answers | writable |
|---|---|---|---|---|---|
| 1 | Introduction | 3.5 | Intro & Lit /20 | – | last (W4) |
| 2 | Background and Literature Review | 7.5 | Intro & Lit /20 | – | now (W1) |
| 3 | The Physics-Informed Effective Hamiltonian Method | 4 | Intro & Lit /20 (the HD gate) | poses Q(i)–(iii) | now (W1) |
| 4 | The Standard Form: Encoder Cost and Hamiltonian Cost | 4 | Model Formulation /30 | Q(i); S2 | now (W1) |
| 5 | The Descriptor Reformulation | 9.5 | Model Formulation /30 (the core) | Q(ii); C | now (W1) |
| 6 | Polynomial Nonlinearity | 4 | Model Formulation /30 | Q(iii); S4 | now (W1) |
| 7 | Preparing and Verifying the Ground State | 6 | Model Formulation /30 (configuration, inputs, software, experiment design) | S3 | now (W1) |
| 8 | Numerical Study | 10.5 | Results & Discussion /30 | evidence for all | after P8's copy-back (W2) |
| 9 | Discussion | 4.5 | Results & Discussion /30 | – | W3 |
| 10 | Conclusions and Future Work | 2.5 | Conclusions /10 | – | last (W4) |
| | **total body** | **56** | | | |

The hard cap is 60 pages and the guidelines penalise overrun; aim for 55–58. Appendices A–M are
outside the count (§6).

### 0.4 Status board (update as you go)

Columns: **S** = scaffolded in the v2.0 order, **D** = drafted, **N** = numbers current from P8,
**R** = reviewed (Review Mode, `CLAUDE.md`), **F** = final.

| chapter / item | S | D | N | R | F | notes |
|---|---|---|---|---|---|---|
| Front matter (title, declaration, achievement, abstract) | ☑ | ☐ | ☐ | ☐ | ☐ | §13 |
| 1 Introduction | ☑ | ☐ | ☐ | ☐ | ☐ | LAND needs the v2.0 scope (readout classical) |
| 2 Background and Literature Review | ◐ | ☐ | n/a | ☐ | ☐ | §2.1 drafted; history, lineage and FOSLS to add (§5.2) |
| 3 PIHM (prior art) | ☑ | ☐ | ☐ | ☐ | ☐ | prior-art paragraphs kept, with REVISE flags |
| 4 Standard form (file `5_standard.tex`) | ◐ | ☐ | ☐ | ☐ | ☐ | W0b: rename; add the classical reading of the wall |
| 5 Descriptor (file `6_descriptor.tex`) | ◐ | ☐ | ☐ | ☐ | ☐ | W0b: add §5.3's mass form and §5.5; fix ancilla +8 |
| 6 Nonlinearity (file `7_nonlinear.tex`) | ◐ | ☐ | ☐ | ☐ | ☐ | W0b: 2K − 1 terms; doubled space standard only |
| 7 Pipeline (file `4_pipeline.tex`) | ◐ | ☐ | ☐ | ☐ | ☐ | W0b: minimax primary; readout one paragraph; experiment design moved in |
| 8 Numerical Study | ◐ | ☐ | ☐ | ☐ | ☐ | W0b: regroup into seven sections |
| 9 Discussion | ☑ | ☐ | ☐ | ☐ | ☐ | add the applicability table (T9) |
| 10 Conclusions | ☑ | ☐ | ☐ | ☐ | ☐ | |
| Appendices A–M | ☑ | ☐ | ☐ | ☐ | ☐ | B drafted, C and D partly; G and H to extend (§6) |
| `ref.bib` audit (T-29) | – | ☐ | – | – | ☐ | before W1 drafting |
| Verification Mode pass | | | | ☐ | | §14 |

---

## 1. Decisions

### 1.1 Decided at the start (2026-09-25)

| # | question | decision | consequence |
|---|---|---|---|
| T-01 | contribution framing | **the descriptor as the headline, plus numbered supporting contributions** | plan §3.1 |
| T-02 | rubric project type | **Modelling**: Model Formulation /30 + Results & Discussion /30 | Chapters 4–7 carry /30 and 8–9 carry /30. Software, the model configuration and its input options are named requirements (§5.7) |
| T-03 | schedule | **no dates**; the writing is ordered by dependency only | §11 |
| T-04 | publication | **thesis first**; paper-shaped material is marked only where it falls out | plan §3.6 |

### 1.2 Decided 2026-09-25 (your acceptance of every recommendation), as amended

| # | question | decision | status |
|---|---|---|---|
| T-05 | chapter structure | ten chapters, with a shared-pipeline chapter and a standard-form chapter ahead of the descriptor | **order superseded by T-20**; the ten chapters stand |
| T-06 | operator notation | **blackboard bold**, matching the paper and `pihm`: 𝔾, B̃ as $\tilde{\mathbb B}$, D̃, 𝕄, 𝕟₁ | in force |
| T-07 | regime subscripts | **H_std, A_std, H_desc, A_desc**; bare H, A or R only in regime-independent statements (Ch. 7) | in force; the bare-symbol chapter is now Ch. 7 |
| T-08 | imaginary-time symbol | **β** for QITE's imaginary time; τ(x) stays the paper's feature state | in force; β now appears only with the QITE filter (T-23) |
| T-09 | Carleman ratio symbol | **ρ**; R stays the stacked residual | in force |
| T-10 | benchmark labels and project vocabulary | **R1–R10**, called *benchmark problems*; never "rung", "pillar", "gate G3" or "tier T2" in prose; *operator verification*, *state-preparation verification*, *circuit simulation / exact emulation / resource estimate* with (T1/T2/T3) once | in force; the variant vocabulary is amended by T-27 |
| T-11 | the notation table | stays in the front matter (`1_header/6_notation.tex`) | in force |
| T-12 | readout's status | the paper's protocol, reproduced with a correction | **superseded by T-24** |
| T-13 | Chapter 3's register | **prior art, judged**; our measurements of the paper live in Chs 4 and 8, never in Ch. 3's descriptive sections | in force |
| T-14 | title | keep the working title until wave W4, then choose from §13.1 | in force |
| T-15 | numbers | keyed lookups `\res{<run>}{<metric>}` from `pihm`'s exporter; a missing number renders its reason | in force; `--final` now checks source digests (D-130) |

### 1.3 Decided while scaffolding (2026-09-25)

| # | decision |
|---|---|
| T-16 | **𝔾 is the coefficient-space map f ↦ f′** (strictly upper triangular), as in `pihm`; the paper prints the same matrix as 𝔾ₙᵀ, said once in §3.3 |
| T-17 | scaffold guidance as **LaTeX comments only**; placeholders render; provisional numbers render tinted |
| T-18 | **one file per appendix** under `3_footer/appendices/`; the proposal PDF included with `pdfpages` |
| T-19 | notation collisions: raw basis subscript **raw**; block-rescaling constant **ζ**; published ladder coefficient **μ**; condition number **cond(·)**; doubled-space Hamiltonian **H_⊗** |

### 1.4 New in version 2.0 (adopted 2026-10-01; veto any)

| # | question | decision | why |
|---|---|---|---|
| T-20 | chapter order | **Story first.** After the paper's critical assessment (Ch. 3) come the three answers in order: the standard form, encoded exactly (Ch. 4, Q(i)); the descriptor (Ch. 5, Q(ii)); nonlinearity (Ch. 6, Q(iii)). The shared pipeline and the design of the numerical experiment follow as Ch. 7, immediately before the evidence (Ch. 8). The degree formula for filtering an edge ground state moves into the background (§2.6), so Chs 4–6 can argue costs. Ch. 8 is regrouped into one section per question or contribution | In v1.1 a reader crossed six pages of machinery (walk, filter, tiers, software) before meeting the thesis's tension, the Hamiltonian wall. Placed before Ch. 8, the same material reads as the method of a numerical study, which is where the Modelling rubric's "design of numerical experiment" belongs. Ch. 8 by stage read as a catalogue; by question it reads as evidence. The exemplars support either layout (Snow pairs method and results; Green groups them); the deciding factor is that the story leads |
| T-21 | the descriptor's challenge | **Its own body subsection** (§5.5, the gap of a carried derivative) before the cure (§5.6, block rescaling), and its own results section (§8.4) | It is the most interesting science in the project: a genuine failure of the naive reformulation, diagnosed, cured a priori, and bounded. v1.1 gave it 0.75 pages under the cure's name. Owning it, with its limits, is what the rubric's top band calls insight |
| T-22 | first-order equations and systems | **The descriptor has two layouts**, named in the body: the chain (order ≥ 2) and the mass form (first-order equations and systems: I⊗D̃ − 𝔸⊗B̃, the standard rows times I⊗B̃). The kernel-equivalence theorem covers both | Decision 39 made the mass form the descriptor of R1 and R7–R10; v1.1's descriptor chapter did not mention it, and Ch. 6's space-time form used it unexplained |
| T-23 | the preparation filter | **The minimax edge filter** prepares every comparison and extension; QITE is the paper's filter, run in the reproduction (§8.1) and in the filter study (§8.2). β, the Bessel coefficients and Σ\|q_k\| = 1 stay, as the reproduced filter's | Decisions 35 and 50: P8 runs the R1–R5 comparison under minimax in both forms |
| T-24 | readout | **Classical.** The field is decoded from the prepared state; η from the regular datum. The paper's interferometric protocol, built and verified at small n with our correction for p_G < 1, is one paragraph in §7.7, its identity in Appendix F, and future work. Supersedes T-12 | Decision 27 |
| T-25 | fairness of the comparison | **Every cost comparison is quoted twice**: as built (each form's own circuits) and at the ideal-encoding bound α = ‖R‖ (decision 43), which has neither form's encoding in it. Where the order reverses, the reversal is a reported finding | The structured encoding is loose on R3 (C-02), so as-built comparisons there favour the descriptor for the wrong reason; the ideal bound shows the Hamiltonians alone |
| T-26 | prior art for the headline | **Credit two antecedents** wherever the contribution is claimed: the ultraspherical spectral method (Olver & Townsend 2013: banded differentiation, well conditioned after diagonal preconditioning) and first-order-system least squares (Cai, Lazarov, Manteuffel & McCormick 1994: least squares of an order-k operator squares its conditioning; a first-order reformulation avoids it). Cite the concurrent sibling of Wu et al., Paine 2026 (arXiv:2609.26330), in §2.2 and §3.6 | A numerical analyst will ask "isn't this FOSLS, or ultraspherical?" The honest answer, stated first, is that the classical ideas are known and the increment is their transfer to a block-encoded physics-informed Hamiltonian: the kernel equivalence, the flat LCU, the a priori rescaling and the measured consequences for ground-state preparation. Paine 2026 reports that the normalised gap depends on the representation, without scaling, circuits or a reformulation; it confirms the question and leaves the answer open |
| T-27 | variant vocabulary | **The problem is unnamed.** "R2a" is the problem; the paper's panel as printed is "R2a as printed" (or "paper-faithful"), and appears only in §8.1 and Appendix K. Never write "corrected" outside them | Decision 49 |
| T-28 | software in the body | **One short paragraph** (§7.9) names the package, its dependencies, its tests and the Setonix production; records, provenance and source digests live in Appendix L only | The Modelling rubric asks for "a description of any software tools used and/or created", not a manual; the code-map risk is concentrated here |
| T-29 | bibliography | **Audit `ref.bib` before drafting.** `wu2025pihm` lists "Wu, Yuan; Paine, Alex J.; Philip, Deep"; the paper is by Hsin-Yu Wu, Annie E. Paine, Evan Philip, Antonio A. Gentile and Oleksandr Kyriienko. The `note` fields print internal repository notes. Missing entries are listed in §5.2 | A misattributed source paper on page 1 costs the Style mark and credibility; every entry must be checked against its publisher, never guessed |

---

## 2. How the planning documents relate

- **`CLAUDE.md`** (the working agreement) carries **Standing Facts v3** (2026-10-01): the facts a
  draft may not contradict. It is updated whenever this plan's facts change, and wins over the
  guides on facts.
- **`thesis_guides/STRUCTURE_AND_RUBRIC.md`** is the rubric and exemplar reference: the mark sheet,
  the guidelines' formal requirements, what the exemplars do, and the Style & Presentation sweep.
  Its pre-plan section tree, page budget and checklists were removed in v2.0 (they are in git
  history at `4b4e423`); this plan is the structure.
- **`thesis_guides/STYLE_GUIDE.md`** is the register: tone, exposition, empirical presentation and
  the traps. Its examples were updated to the current facts in v2.0.
- **`0_results/README.md`** is how to quote a number.
- **`Code/pihm/docs/02_methods.md`** is the method as built, the source for Chapter 7 and Appendix I.

### 2.1 REVISE items still open in the scaffold (fix while drafting; then delete the comment)

Carried from v1.1's W0 pass:

- **Appendix C, 𝕄_{x¹} is a factor √2 too small.** `pihm`, whose lifts reproduce the paper's SM §A
  entry by entry, gives `[[0,1],[1,0],[0,1/√2],[0,0]]`.
- **Appendix C, worked example.** Its sentences "triangular only because…" and "three orders of
  magnitude" are wrong: every polynomial in 𝔾 is upper triangular, and the largest off-diagonal entry
  (30) is about one order below 400.
- **Chapter 3, doubled space.** Ψ = ψ ⊗ ψ lives in an N²-dimensional space, not 2N.
- **Chapter 3, constant coefficients.** Under the lift a constant enters as a_j 𝕄₁ (2N × N), not a_j I.
- **Chapter 3, regular constraints.** Reconcile "Only one such regular constraint…" with the source
  row 𝔻⁽⁰⁾(x_s).
- **Chapter 6 (was 7).** A clause says "descriptor Hamiltonian" where it means the doubled-space one.
- **Appendix G, variable coefficients.** It describes the legacy monomial route; the rebuild uses the
  square Galerkin form (D-005).
- **Appendix G, padding.** The padding blocks carry weight c_pad = 1 and decouple exactly; say so.
- `nlfft2025su2` has no authors, so the inverse-NLFT citation is still CITE-NEEDED.

New in v2.0, found by grep in the scaffold (each becomes a `% REVISE:` at W0b):

- `6_descriptor.tex`: the cost proposition and its LAND say ⌈log₂(n+4)⌉ + 6 (now + 8 for R2's
  system rows); the rescaling LAND says "Θ(n_f) gates" and "ζ = ω for R2c" (now the a priori rule,
  in the coefficients, no gates); "α_A = 2N + O(1)" and "→ 1" need the scope of B-04.
- `4_pipeline.tex`: the filter section's QITE-primary LAND and equations (T-23); "warm start as a
  labelled variant" (none was built); the readout section (T-24); "Paper-faithful versus
  corrected variants" (T-27).
- `7_nonlinear.tex` and Appendix H: "K² structured terms" (now 2K − 1); "both forms" for the
  doubled space (standard only); ρ < 1 as "the" precondition (sufficient, not necessary).
- `8_results.tex`: the headline table's ancilla cell `+ 6`; `fig:faithful-vs-corrected` naming
  (T-27); the CHECK note on the filter of A-6 (resolved: P8's comparison is minimax).
- `1_introduction.tex`: "Readout is the paper's protocol, reproduced in simulation" (T-24).
- `3_pihm.tex` figure caption: fine as the *published* pipeline; keep the interferometric readout
  there, described as published.

Opened with the Chapter 4 draft (2026-10-06):

- **Gap flatness is measured, not proved (Chapter 4, §4.4; Chapter 8).** `eq:standard-wall`'s
  Θ̃(N^{2k}) assumes Δ = Θ(1) for the standard form. Measured so far on R2a (n = 6–8, 7.04) and R2b
  only. **Extend the check** to the other constant-coefficient one-axis panels (R1, R2c, R4*) and
  to other second-order coefficients, then widen or narrow the claim. Until then the text says
  "measured on R2a and R2b".
- **Appendix D, measured ε_G(n), qubits and gates.** `tab:app-epsilon-G` is all `\prov`; the
  published build's measured counts and error are not exported. Needs a derived key, then quote one
  measured ε_G in §4.1 beside the bound (REVISE in `4_standard.tex`).
- **Factorisation error 2.3e-13 (§4.2)** is the planning probe's figure, typed as `\prov`; replace
  with a derived key (max error of 𝔾 = R₀(2U_odd)Λ, n ≤ 10) or delete the number.
- **Appendix E must carry** the Bessel-kernel limit α_𝔾/‖𝔾‖₂ → 2j_{−3/4,1}, the theorem
  ‖𝔾^k‖₂/N^{2k} → ‖K^k‖ > 0 (so ‖H_std‖ = Θ(N^{4k})) and the published ratio ~ jN³
  (companion 31, 33, 57). Written when the appendices are.
- **`8_results.tex` T7 `\prov` cells disagree with the records** (published degree at n = 8:
  8.2e23 against 9.1e22; descriptor gap 0.454 against 2.87). Resolved when T7 moves to `\res`.
- **STYLE_GUIDE §7 row on the relative gap** says "below double precision at n = 7"; the records give
  Δ/‖H‖ = 5.9e-15 at n = 7 and 2.3e-17 at n = 8, so it is below 2⁻⁵² only from n = 8.

---

## 3. Contributions, questions, spine and vocabulary

### 3.1 The contributions (numbered in §1.3; each gets a verdict in §10.1)

**Headline.**

> **C. The descriptor reformulation.** Replacing the dense differentiation matrix by its banded
> factors, carried as derivative blocks for higher-order equations and as a mass form for
> first-order equations and systems, turns the physics-informed residual from dense to banded *with
> exactly the same kernel*. Its Hamiltonian has ‖H_desc‖ = Θ(N²) against the standard form's
> Θ(N^{4k}); its block encoding is one flat LCU with ⌈log₂(n+4)⌉ + 8 ancilla for R2's system rows and
> α/‖A_desc‖ → 1 on regular one-axis problems. The gap the derivative blocks erode is restored on
> one axis by an a priori block rescaling at no gate cost, so the filter degree is Θ̃(N) for a
> regular one-axis ODE, against Θ̃(N^{2k}) for the standard form's best exact encoding. *Costs,
> volunteered:* the block register, a higher gate count per query at small n, a gap that still falls
> on two axes, and no remedy for a double zero. *Antecedents:* ultraspherical; first-order-system
> least squares. *Evidence:* Ch. 5, §8.3–8.4; claims C-05, C-06, B-01, B-02, B-04–B-06, B-21.

**Supporting.**

> **S1. A verified reproduction and audit of Wu et al.** Rebuilt exactly, printed constraint points
> and Maclaurin sources included: the printed η_e agree with the exact solution's ‖b‖² to within one
> unit of the last printed digit on all 11 ODE panels; the PDE and nonlinear panels do not
> reproduce, each triaged by discriminating runs; the printed choices distort the solutions at the
> printed n; the paper's circuits (Figs 2, 8, 9) are built and their claims tested, and its
> time rule falls short of ε. *Evidence:* §4.1, §8.1, Appendix K; claims A-01–A-13, C-07.

> **S2. An exact structured encoding of the standard form.** 𝔾 = R₀(2U_odd)Λ gives α_G = N(N−1)
> ≤ 2.12‖𝔾‖₂ with O(n²) gates and n + O(log n) ancilla, against an α/‖𝔾‖₂ growing like N³ for the
> published normalisation. For constant coefficients it bounds α_H/‖H_std‖, isolating the standard
> form's cost in its Hamiltonian; for a lifted variable coefficient it is loose. *Evidence:* Ch. 4,
> §8.3; claims C-01, C-02.

> **S3. A regime-independent, verified preparation pipeline.** A stacked-residual reflection V with
> Π V Π = 2H/α_R² − I and a controlled V that needs only controlled reflections; GQSP with the
> minimax edge filter, chosen over imaginary time by a study in both forms; a priori parameters and
> answer-independent initial states; operator verification in three modes and state-preparation
> verification in three tiers, the exact emulation proven, and measured, equal to the circuit
> (≤ 1e-10); a certified-estimate iterative reference to half a million columns. *Evidence:* Ch. 7,
> §8.2; claims C-03, C-04, C-08, B-13, B-16, B-17, B-24.

> **S4. Nonlinearity: preparation versus projection.** The paper's doubled space encodes exactly but
> leaves a kernel of dimension at least 2^{2n−1}, so it only projects. The Carleman lift gives a
> one-dimensional near-kernel, a genuine preparation, in *both* forms; its convergence is measured
> (a/ν, not ρ, decides it), and a trusted kernel is shown not to certify a converged lift. The
> descriptor's time axis lowers the degree, in every Navier–Stokes pair compared. The pipeline
> reaches 2-D incompressible Navier–Stokes on 12–80 modes, and a tensor-layout coupling of 2K − 1
> terms to 316 modes. *Evidence:* Ch. 6, §8.5–8.6; claims A-10, B-12, B-18, B-19, B-22, C-09, C-10.

**Rules for the list.** One sentence of *what*, one clause of *evidence*. The headline is listed
first and carries its costs and antecedents. S2 is phrased as serving the comparison, never as a
rival solver. S1 is a test of the paper, not a rivalry.

### 3.2 The three questions (the narrative's spine)

Wu et al.'s Discussion names two open problems: "studying the spectral gap dependence is an important
question for the future work", and "the cost of differentiation" as a guide to choosing the basis.
The critical assessment of Chapter 3 turns them into three questions, and every later chapter
answers one.

| question | answered (formulation) | evidenced (results) |
|---|---|---|
| (i) *Is the method's cost its encoder's or its Hamiltonian's?* | Ch. 4 | §8.3 |
| (ii) *Can the residual be reformulated so that its Hamiltonian is banded and well conditioned, without changing its solution, and what does that cost?* | Ch. 5 | §8.3–8.4 |
| (iii) *Can nonlinear equations be prepared rather than projected?* | Ch. 6 | §8.5–8.6 |
| (how the answers are tested) | Ch. 7 | §8.1–8.2 |

Each formulation chapter opens by restating its question in one sentence and closes by naming the
results section that tests it.

### 3.3 The spine sentence

> *Carrying the intermediate derivatives instead of eliminating them turns the physics-informed
> residual from dense to banded with its kernel unchanged, so the Hamiltonian's norm falls from
> Θ(N⁸) to Θ(N²) for a second-order equation; the price is a block register and a gap the
> derivative blocks erode, which an a priori rescaling restores on one axis at no gate cost.*

Place it, lightly reworded each time, in: the Abstract; the end of §1.3; the close of §3.6 (as the
question it answers); §5.1; §5.10; §8.7; §10.1.

### 3.4 Controlled vocabulary

| use | never | note |
|---|---|---|
| standard form | "collocation" or "state-space" for the paper's regime | "constraint points" for x_z, x_m, x_s; "collocation" stays for the classical method (§2.3) and Childs & Liu |
| descriptor form; its chain and mass form | "our method" alone, "sparse method" | T-22 |
| block rescaling | equilibration, preconditioning (of the circuit) | general equilibration costs Θ(P) gates and is excluded |
| structured (exact) encoding | "our standard-form method", "improved Wu" | S2, a fairness device |
| published encoding | FABLE, "dense encoding", "naive" | Wu et al.'s Figs 2, 8 and 9 |
| ideal-encoding bound (α = ‖R‖) | "best possible" | T-25 |
| minimax edge filter; imaginary-time (QITE) filter | "the filter" when it matters which | T-23 |
| prepared | "found", "solved" (for a filter's output) | only for a one-dimensional (near-)kernel |
| projected | "prepared" (for the doubled space) | R6 |
| trusted kernel | "converged", "correct" | trust is the kernel's isolation, not the lift's convergence |
| verified (exact / probe / IR) | "checked", "tested", "passes" | name the mode and the tolerance |
| circuit simulation (T1) | "run on a quantum computer", "executed" | the Aer statevector |
| exact emulation (T2) | "simulated" | provably equal to T1's post-selected output |
| resource estimate (T3) | "predicted to work" | |
| beyond the simulation budget (estimate quoted) | "failed", "too big", "infeasible" alone | Planning decision 20 |
| R2a; R2a as printed (paper-faithful) | "corrected R2a", "wrong/fixed version" | T-27 |
| benchmark problem R1–R10 | rung, case N | T-10 |
| a priori parameters | "tuned", "chosen" | never against the answer |

### 3.5 A scientific argument, not a code map

The rubric scores a model a reader could rebuild, not a tour of the software. Rules:

1. **Every chapter opens with its question and closes with its answer.** No chapter opens with "this
   chapter describes the module…".
2. **State constructions as mathematics.** `assemble`, `stacked_reflection`, `t2` and their
   relatives appear in the body only in §7.9 and the figure-script comments; elsewhere they are the
   residual, the reflection V, the exact emulation.
3. **Findings, not history.** Decisions, issues, Journal entries, probes, failed runs and gates are
   never cited. A finding that came from an issue is stated as a finding ("the descriptor's gap
   closes where the leading coefficient vanishes"), with its evidence in a figure or appendix. A
   design choice is justified by its reason, never by "we decided".
4. **Records, hashes, campaigns, digests and Slurm** live in Appendix L. The body says "every number
   is regenerated from the archived records by one command (Appendix L)".
5. **The physics stays in view.** Each benchmark problem is introduced by the capability it tests
   and the physics it carries (stiffness, a singular leading coefficient, a heat equation, a vortex
   pair), never by its campaign.
6. **Negative results are findings**, numbered with the positive ones (the rubric protects them when
   analysed).

### 3.6 Paper-shaped material (light note, T-04)

Chs 4–5, §8.3–8.4 and §9.1–9.2 form a self-contained article ("a banded reformulation of
physics-informed effective Hamiltonians"), with the reproduction as its baseline section and the
Carleman results as a second paper. Nothing in the plan depends on this.

---

## 4. Page budget and LaTeX tree

### 4.1 Page budget (Modelling scale)

| chapter | pp | criterion |
|---|---|---|
| 1 Introduction | 3.5 | Intro & Lit /20 |
| 2 Background and Literature Review | 7.5 | Intro & Lit /20 |
| 3 The PIHM method (prior art, judged) | 4 | Intro & Lit /20 (HD gate: critical assessment) |
| 4 Where the cost lies: the standard form | 4 | Model Formulation /30 |
| 5 The descriptor reformulation | 9.5 | Model Formulation /30 (core) |
| 6 Polynomial nonlinearity | 4 | Model Formulation /30 |
| 7 Preparing and verifying the ground state | 6 | Model Formulation /30 |
| 8 Numerical Study | 10.5 | Results & Discussion /30 |
| 9 Discussion | 4.5 | Results & Discussion /30 |
| 10 Conclusions and Future Work | 2.5 | Conclusions /10 |
| **total** | **56** | |

**Why this split.** The Modelling scale gives Results & Discussion 30 marks, so Chapters 8–9 take
15 pages. Formulation (Chapters 4–7, 23.5 pages) must let a reader "create equivalent models", so
configuration, inputs and software have body space in Chapter 7, with the detail in Appendices F,
G, I, J and L. Four pages of slack under the cap absorb figures.

**Trim order if over budget:** §2.1 first, then §8.4's third representative problem (to Appendix J),
then §7.9 and §7.8 to their minimum, then §3.4. Chapter 5 is cut last.

### 4.2 LaTeX section tree (v2.0; file names are the targets of W0b)

```latex
% 2_body/1_introduction.tex  (~3.5 pp)
\section{Introduction}                                        % sec:intro
  \subsection{Differential Equations as a Target for Quantum Computation}
  \subsection{Physics-Informed Hamiltonians and Where Their Cost Lies}   % F0 (optional)
  \subsection{Contributions and Scope}
  \subsection{Outline}

% 2_body/2_literature.tex  (~7.5 pp)
\section{Background and Literature Review}                    % sec:background
  \subsection{Quantum Computation Preliminaries}               % <= 1.5 pp, hard cap
  \subsection{Quantum Algorithms for Differential Equations}
      \subsubsection{Linear-Systems and Linear-Combination Routes}
      \subsubsection{Nonlinear Equations: Carleman and Related Linearisations}
      \subsubsection{Variational Routes}
      \subsubsection{Ground-State Routes and the Physics-Informed Lineage}
      \subsubsection{Critical Assessment}                      % T1 table, "this work" row
  \subsection{Spectral Methods and Their Conditioning}
      \subsubsection{Chebyshev Series, Galerkin Truncation and Differentiation}
      \subsubsection{Banded Differentiation: the Ultraspherical Method}
      \subsubsection{First-Order Reformulation and Least Squares}
      \subsubsection{Fourier--Galerkin Discretisation of Periodic Flows}
  \subsection{Block Encoding, Linear Combinations of Unitaries and Qubitisation}
  \subsection{Quantum Signal Processing and Its Generalisation}
  \subsection{Ground-State Preparation by Filtering}          % the degree formula
  \subsection{Readout}
  \subsection{Synthesis}

% 2_body/3_pihm.tex  (~4 pp)  PRIOR ART, judged
\section{The Physics-Informed Effective Hamiltonian Method}   % sec:pihm
  \subsection{Overview}
  \subsection{The Latent Chebyshev Model}
  \subsection{The Residual, the Hamiltonian and Its Constraints}
  \subsection{The Published Circuits, Filter and Readout}
  \subsection{The Doubled-Space Extension to Nonlinearity}
  \subsection{Critical Assessment}                             % poses Q(i)-(iii)

% 2_body/4_standard.tex  (~4 pp)   [was 5_standard.tex]
\section{The Standard Form: Encoder Cost and Hamiltonian Cost}   % sec:standard
  \subsection{The Published Encoding, Rebuilt}
  \subsection{An Exact Factorisation of the Differentiation Matrix}
  \subsection{Circuits and Cost}
  \subsection{What Remains: The Standard-Form Hamiltonian}

% 2_body/5_descriptor.tex  (~9.5 pp)  THE CORE   [was 6_descriptor.tex]
\section{The Descriptor Reformulation}                        % sec:descriptor
  \subsection{The Idea}                                        % F4 sparsity
  \subsection{The Banded Factorisation}
  \subsection{Two Layouts and Kernel Equivalence}              % chain | mass form; theorem
  \subsection{Constraints, Partial Differential Equations and Coupled Fields}
  \subsection{The Gap of a Carried Derivative}                 % the challenge (T-21)
  \subsection{Block Rescaling}                                 % the cure and its limits
  \subsection{The Block Encoding: One Flat Linear Combination} % F5, algorithm
  \subsection{Cost of the Descriptor Encoding}                 % proposition
  \subsection{Consequences for the Spectrum and the Filter}
  \subsection{Summary}

% 2_body/6_nonlinear.tex  (~4 pp)   [was 7_nonlinear.tex]
\section{Polynomial Nonlinearity}                             % sec:nonlinear
  \subsection{Two Treatments}
  \subsection{The Doubled Space: Exact Encoding, Degenerate Kernel}
  \subsection{The Carleman Lift in Space--Time}
  \subsection{Products and Couplings on a Circuit}
  \subsection{Fourier--Galerkin Fluids: Burgers and Navier--Stokes}
  \subsection{Preparation Versus Projection}                   % T8

% 2_body/7_pipeline.tex  (~6 pp)   [was 4_pipeline.tex]
\section{Preparing and Verifying the Ground State}            % sec:pipeline
  \subsection{Overview and Model Configuration}                % F1
  \subsection{Problems and Model Inputs}                       % T2 constraint kinds, T3 ladder
  \subsection{The Classical Reference}
  \subsection{From Stacked Residual to Quantum Walk}
  \subsection{The Filter and Its Parameters}
  \subsection{Verification and the Error Budget}               % T4
  \subsection{Reading Out the Solution}
  \subsection{Design of the Numerical Experiment}              % cost conventions, fairness
  \subsection{Software and Computation}

% 2_body/8_results.tex  (~10.5 pp)
\section{Numerical Study}                                     % sec:results
  \subsection{Reproducing Wu et al.}                           % S1: T6, F6
  \subsection{The Pipeline Is Faithful}                        % S3: F7, F8
  \subsection{Where the Cost Lies}                             % Q(i),(ii): F9, T7, F10
  \subsection{The Descriptor's Gap and Its Rescaling}          % the challenge: F11, F12
  \subsection{Nonlinear Problems}                              % Q(iii): F13
  \subsection{Case Study: Two-Dimensional Navier--Stokes}      % F14
  \subsection{Summary of Findings}                             % numbered, >= 2 negative

% 2_body/9_discussion.tex  (~4.5 pp)
\section{Discussion}                                          % sec:discussion
  \subsection{Why the Descriptor Form Wins, and What It Costs}
  \subsection{End-to-End Complexity}
  \subsection{What the Reproduction Says About the Published Method}
  \subsection{Where the Construction Applies}                  % T9 applicability
  \subsection{Feasibility on Fault-Tolerant Hardware}
  \subsection{Limitations}

% 2_body/10_conclusions.tex  (~2.5 pp)
\section{Conclusions and Future Work}                         % sec:conclusions
  \subsection{Conclusions}
  \subsection{Future Work}
```

### 4.3 Scaffold conventions (as built) and the W0b migration

**Conventions (unchanged).** `main.tex` holds each chapter's `\section` and label and inputs the
body files; `3_footer/appendices.tex` does the same for `A_gates.tex` … `M_proposal.tex`. Every
subsection has a label. Comment tags: PURPOSE, CRITERION, SOURCES, WRITE WHEN, LAND, FIG, TAB,
OFFLOAD, CHECKLIST, TRAPS, REVISE, CITE-NEEDED. Macros in `1_header/0_packages.tex`: `\G`, `\Bt`,
`\Dt`, `\M`, `\nfold`, `\Brow`, `\Dzero`, `\Ucg`, `\Uodd`, `\Astd`, `\Adesc`, `\Hstd`, `\Hdesc`,
`\fhat{j}`, `\prov{…}`; numbers by `\res` (plan §10.2). Placeholders: `\placeholderfigure`; tables with
final columns; propositions with `% STATE:` and proofs in appendices.

**The W0b migration (not yet done).**

1. Rename `4_pipeline.tex` → `7_pipeline.tex`, `5_standard.tex` → `4_standard.tex`,
   `6_descriptor.tex` → `5_descriptor.tex`, `7_nonlinear.tex` → `6_nonlinear.tex`, and reorder
   `main.tex`'s inputs. Labels do not change (`sec:pipeline`, `sec:standard`, …), so every `\Cref`
   survives; only "Chapter N" prose and the outline need renumbering.
2. In the renamed files, rewrite the header comments (PURPOSE, CRITERION, LAND) to §5's entries.
   Move the degree formula `eq:degree` and its text to `2_literature.tex`'s filtering subsection,
   keeping its label. Move `8_results.tex`'s experimental-design LAND into `7_pipeline.tex`.
3. Add the new subsections (`sec:descriptor-layouts`, `sec:descriptor-gap`,
   `sec:pipeline-design`, the two new background subsubsections) with their LAND blocks.
4. Regroup `8_results.tex` into §5.8's seven sections; keep the existing figure and table labels.
5. Add a `% REVISE:` beside each item of §2.1's new list.
6. Compile into a scratch outdir; zero undefined references.

---

## 5. Chapter by chapter

Each entry gives the purpose, the rubric criterion, the sources, the scaffold (what each subsection
must land, in order, with its page share), figures and tables, appendix offloads, the marker's
checklist and the traps. `pihm` paths are relative to `Code/pihm/`; "nb NN" is a notebook of
Planning.md §10.8.

---

### 5.1 Chapter 1: Introduction (3.5 pp; Intro & Lit /20)

**Purpose.** Establish that quantum differential-equation solvers matter, that the physics-informed
Hamiltonian route has a *located* cost problem its authors left open, and what this thesis
contributes and does not.

**Criterion.** "Comprehensive, superior understanding… with **excellent connection of the current
field to the project**". The introduction converges; it does not survey.

**Scaffold.**

1. **§1.1 Differential equations as a target (1 p).** Applications (fluids, finance, fields); why
   quantum algorithms are proposed; the resource that matters: queries times gates per query, and
   qubits. One sentence per algorithm family, the judgement left to Ch. 2.
2. **§1.2 Physics-informed Hamiltonians and where their cost lies (1 p).**
   - Wu et al.'s idea in three sentences, attributed at first mention, with its lineage in one
     clause (physics-informed quantum machine learning in a Chebyshev latent space).
   - Their two open questions, quoted: the gap's dependence, and the cost of differentiation.
   - The question this thesis asks: *is the method's cost its encoder's or its Hamiltonian's?*
   - **One quantitative sentence before the end of page 2**: the filter degree for the paper's
     Fig. 3b problem at n = 8 as published, with the best exact encoding, and in descriptor form:
     `\res{stateprep/R2a/standard/n8/T3/encoder=published}{degree}`,
     `\res{stateprep/R2a/standard/n8/T3}{degree}`, `\res{stateprep/R2a/descriptor/n8/T3}{degree}`
     (resource estimates; name the tier).
   - Optional concept figure F0 (½ p): the degree as √(looseness × 1/relative gap), with the
     encoder wall and the Hamiltonian wall marked.
3. **§1.3 Contributions and scope (1 p).**
   - The numbered list of plan §3.1, then the spine sentence.
   - **The scope, once, plainly:** every result is a classical computation: circuit simulation (T1)
     at small n, exact emulation (T2) beyond it, resource estimates (T3) beyond that. Nothing ran on
     hardware. The solution is read out classically from the prepared state.
   - **What is not claimed:** a poly-log end-to-end cost; preparation for a degenerate formulation; a
     lower bound for every filter; on-circuit gap estimation (the spectral edge is assumed known); a
     new readout protocol.
4. **§1.4 Outline (0.5 p).** One line per chapter naming its job: Ch. 3 as reviewed prior art; Chs
   4–6 as the answers to Q(i)–(iii); Ch. 7 as how they are tested; Ch. 8 as the evidence.

**Marker checklist.** A non-specialist physicist can state the problem after two pages; a number on
or before page 2; every contribution numbered and falsifiable with its evidence; the scope explicit,
tiers and "no hardware" included; Wu et al. attributed at first mention; the outline matches the
headings verbatim.

**Traps.** Leading with the descriptor before the reader knows the baseline; claiming a speed-up;
listing S2 as a rival method; "the readout protocol was reproduced".

---

### 5.2 Chapter 2: Background and Literature Review (7.5 pp; Intro & Lit /20)

**Purpose.** Command of the state of the art and its history, **judged**: only the prior art that
Chapters 3–7 build on, each family with its failure mode.

**Criterion.** "Comprehensive, superior understanding of the **historical background** and state of
the art" and "a **critical assessment** of the strengths and weaknesses of the material reviewed is
required for a high distinction". v1.1's tree had no history and no classical-conditioning
antecedent; both are added.

**Scaffold.**

1. **§2.1 Quantum computation preliminaries (≤ 1.5 pp, hard cap).** Prose citing Nielsen & Chuang;
   numbered definitions only for objects reused (the (α, m, ε) block encoding); queries against
   gates; the fault-tolerant frame (NISQ one paragraph: §9.5's feasibility argument is
   fault-tolerant). The gate table goes to Appendix A.
2. **§2.2 Quantum algorithms for differential equations (2.5 pp): a short history, then judged.**
   - (a) *Linear systems and linear combinations.* HHL (2009) → Berry's ODE solvers (2014, 2017)
     → Childs & Liu's spectral methods (2020: Chebyshev collocation, whose matrices are dense and
     ill conditioned) → optimal-κ linear-system solvers (Costa et al. 2022) → linear combination of
     Hamiltonian simulation (An, Liu & Lin 2023) and Schrödingerisation (Jin, Liu & Yu 2023).
     Their cost runs through κ, state preparation and readout; explicit resource counts (Jennings
     et al. 2023) show the constants matter.
   - (b) *Nonlinear equations.* Carleman linearisation (Liu et al. 2021; Krovi 2023), with its
     ratio condition R < 1 stated as the sufficient condition it is; other routes in one sentence.
   - (c) *Variational routes.* Lubasch et al. 2020; differentiable quantum circuits (Kyriienko,
     Paine & Elfving 2021): flexible, but without guarantees, and with barren plateaus.
   - (d) *Ground-state routes and the physics-informed lineage.* The solution as a null vector of a
     positive semi-definite Hamiltonian is old in linear systems (Subaşı, Somma & Orsucci 2019; An &
     Lin 2022; Lin & Tong's eigenstate filtering 2020). The physics-informed line: differentiable
     quantum circuits (2021) → the Chebyshev latent space (Paine, Elfving & Kyriienko 2023) → the
     effective Hamiltonian (Wu et al. 2025) → alternative constructions, the concurrent Paine 2026
     (read in full 2026-10-04): alternative Hamiltonian constructions and function encodings whose
     normalised gaps, on a few small instances, depend on both ("do not establish a general
     ordering"); no scaling in resolution and no circuits; its lift is polynomial-only and needs
     more registers with the degree. This family is examined in Ch. 3.
   - (e) *Critical assessment*, with **Table T1**: approach × {assumptions, cost driver, output,
     failure mode}, and a *this work* row.
3. **§2.3 Spectral methods and their conditioning (1.5 pp).** The antecedents of the headline,
   credited *before* Ch. 5 claims anything.
   - Chebyshev series; Galerkin, tau and collocation; the differentiation matrix is dense and
     strictly upper triangular, and an order-k operator's norm grows as N^{2k}.
   - **The ultraspherical method** (Olver & Townsend 2013): differentiation maps Chebyshev into
     ultraspherical bases, so it is banded; with a diagonal preconditioner the systems are well
     conditioned. The descriptor's B̃ and D̃ are its first step, and its block rescaling plays the
     preconditioner's part.
   - **First-order reformulation and least squares** (Cai, Lazarov, Manteuffel & McCormick 1994;
     Bochev & Gunzburger 2009): least squares of an order-k operator squares its conditioning, and
     recasting it as a first-order system avoids that. The physics-informed Hamiltonian *is* a
     least-squares functional, H = R†R, so this is the classical reading of the Hamiltonian wall.
   - **State the increment precisely here:** applying both ideas to a block-encoded physics-informed
     Hamiltonian, proving its kernel unchanged, encoding it as one flat LCU, rescaling it a priori,
     and measuring what it does to ground-state preparation.
   - Fourier–Galerkin discretisation of periodic flows (for R9 and R10).
4. **§2.4 Block encoding, LCU and qubitisation (1 p).** PREPARE/SELECT; α = Σ|c_t| and α ≥ ‖X‖ for
   any block encoding; the Ω(log L) ancilla lower bound for exact LCU (Chakraborty et al. 2025);
   qubitised walks, Π W^k Π = T_k.
5. **§2.5 QSP, QSVT and GQSP (0.75 p).** The parity constraint and its removal (Motlagh & Wiebe);
   phase finding by Weiss's complement and the inverse nonlinear Fourier transform (Berntson &
   Sünderhauf; Laneve), as prior art.
6. **§2.6 Ground-state preparation by filtering (0.75 p).** Imaginary time; Lin & Tong's minimax
   Chebyshev filters and their optimality; the known-gap assumption; the overlap γ; amplitude
   amplification. Ch. 3 assumes this section and §2.5: it names QITE by QSVT and the paper's
   mixed-parity construction and points here for what they are. **The degree formula**, `eq:degree`, stated here so Chs 4–6 can argue costs: for
   the ground state at the edge of H = R†R block-encoded at α_H = α_R², a Chebyshev filter needs
   d = Θ(√(α_H/Δ) log 1/ε), which is Θ(α_R/σ₁ · log 1/ε) when the kernel is exact: the
   residual's effective condition number.
7. **§2.7 Readout (0.25 p).** The readout problem (Williams et al. 2024) and the standard primitives
   in one paragraph; Wu et al.'s protocol is described in Ch. 3.
8. **§2.8 Synthesis (0.25 p).** Where physics-informed Hamiltonians sit, and the hand-off to Ch. 3
   "on the same attributed footing".

**Citations to add to `ref.bib`** (T-29; check each against the publisher; several are in
`Research/Papers/`):

- HHL 2009; Berry et al. 2017; Childs & Liu 2020 (CMP); Costa et al. 2022 (PRX Quantum);
  An, Liu & Lin 2023 (PRL); Jin, Liu & Yu (Schrödingerisation, PRA); Jennings et al. 2023
  (arXiv:2309.07881);
- Liu et al. 2021 (PNAS); Krovi 2023 (Quantum);
- Lubasch et al. 2020 (PRA); Kyriienko, Paine & Elfving 2021 (PRA); Paine, Elfving & Kyriienko 2023
  (arXiv:2308.01827); **Paine 2026 (arXiv:2609.26330)**;
- Subaşı, Somma & Orsucci 2019 (PRL); An & Lin 2022; **Lin & Tong 2020, eigenstate filtering
  (Quantum 4, 361)**, besides the present near-optimal ground-state paper (Quantum 4, 372);
- **Cai, Lazarov, Manteuffel & McCormick 1994 (SIAM J. Numer. Anal.)**; Bochev & Gunzburger 2009
  (book);
- Taylor & Green 1937; Cole 1951 and Hopf 1950; Qiskit Aer; the `nlfft2025su2` authors.
- **Fix:** `wu2025pihm`'s authors (T-29). **Strip or suppress** every `note` field
  (`\AtEveryBibitem{\clearfield{note}}`). Do not import `camps2022fable`.

**Marker checklist.** Every method has a weakness sentence; T1 is present; the history is visible;
ultraspherical and first-order least squares are credited before Ch. 5; the concurrent work is
cited; §2.1 ≤ 1.5 pp; nothing in the chapter goes unused; IEEE `biblatex` throughout.

---

### 5.3 Chapter 3: The Physics-Informed Effective Hamiltonian Method (4 pp; Intro & Lit /20, body-located)

**Purpose.** Present Wu et al.'s method at journal-review depth, as attributed prior art, then judge
it. The judgement poses Q(i)–(iii).

**Criterion.** This chapter discharges the Intro & Lit HD gate, "critical assessment". Its first
sentence says it reports prior art; its last section reads as a gap statement.

**Sources.** Planning §3.1–3.3, §3.6, §3.8 ("Documented deviations"), §7.6; the paper's Discussion
(for the two open questions); claims A-01–A-13 stated neutrally as the paper's.

**Scaffold.**

1. **§3.1 Overview (0.3 p).** The three-ingredient move (coefficients as the state, the equation as
   annihilation, the ground state as the solution), the lineage in one sentence, and that *our*
   reproduction is in §8.1.
2. **§3.2 The latent Chebyshev model (0.5 p).** The normalised basis; f_q(x) = ⟨τ(x)|ψ⟩; the scale
   η; raw τ in rank-one rows. Our closed form for η_e belongs to §8.1.
3. **§3.3 The residual, the Hamiltonian and its constraints (1.2 p).** A = Σ_j 𝕄_{a_j}𝔾^j −
   𝕄_r𝔻⁽⁰⁾(x_s), H = 𝒯(A) + Σ𝒯(𝔹_i); least squares, exact kernel only for polynomial solutions;
   invariant and regular constraints; lifts 𝕄_{x^p}; Maclaurin sources; hand-picked PDE invariants;
   the transpose convention once (T-16). Worked N = 4 instance → Appendix C.
4. **§3.4 The published circuits, filter and readout (0.7 p, contracted 2026-10-04).** Three
   paragraphs, each the idea, the paper's claims and a pointer, with no attribution padding (the
   Overview already says the method is the paper's; cite only for specifics). Block encodings: B,
   D⁽⁰⁾ from the inverse feature map and S_{n+1}; 𝔾 as an LCU with entries loaded as rotation
   amplitudes; the prefactor; the claims (2n + 3 qubits, O(n³) gates, exponentially decreasing
   error). Filter: QITE by QSVT on H/‖H‖_F, the time rule, the O(1/Δ) expectation; **it assumes §2.5
   and §2.6**. Readout: interferometric, two all-zero probabilities, point by point. **Relocated,
   not lost:** the Fig. 8/9 registers, subroutines, angles and counts → Appendix D
   (`app:published-build`); the QSVT detail (even/odd phases, the dilation, PREPARE/SELECT, t = 15
   and 8 at degrees (6, 7), the 1/√Δ thermalisation remark, GQSP) → Appendix K (`app:paper-filter`);
   Eqs 36–39 → Ch. 7 / Appendix F. The optional figure was dropped (Style Guide §2.4).
5. **§3.5 The doubled-space extension (0.4 p).** Ψ = ψ ⊗ ψ with 𝕟₁; **quadratic only** (a
   degree-p term needs p copies of dimension N^p, folded back; Paine 2026 notes the same; detail →
   Appendix H); the paper's own count of zero eigenvalues and its selection of "a degenerate state
   that closely matches the analytical solution". The assessment: any function of H returns the
   projection of the initial state onto the kernel; kernels are subspaces and product states are
   not (**scope the argument: a penalty built without knowledge of the solution**).
6. **§3.6 Critical assessment (0.6 p).**
   - **Strengths:** a unified construction; exact kernels for polynomial solutions; poly(n) terms;
     no grid; derivatives of the solution available at every x.
   - **Weaknesses, most severe first**, each with a pointer to where it is measured:
     1. the spectrum: ‖H‖ grows as N^{4k} against a flat gap, which fixes the filter's degree
        whatever the encoder (§4.4, §8.3);
     2. the published normalisation of 𝔾 is loose by a factor growing as N³ (§4.1, §8.3);
     3. printed choices distort the solution at the printed n (§8.1);
     4. the PDE invariant sets degenerate beyond the printed n, are taken from the known solution,
        and the heat panel's t = 0 data make it a backward heat problem on [−1, 0], hence ill posed
        (§8.1; checked against `pihm/docs/10_reproduction.md` and D-028 on 2026-10-04);
     5. the time rule falls short of ε (§8.1);
     6. the nonlinear route cannot prepare (§6.2, §8.5);
     7. the readout identity assumes deterministic preparation (§7.7, Appendix F).
   - **The paper's own open questions**, quoted, and the concurrent work (Paine 2026) that
     finds, on a few small instances, a representation-dependent normalised gap without a scaling
     in resolution, circuits or a general ordering: it raises the first question without
     answering it.
   - **Close with Q(i)–(iii) in italics**, each with its chapter by `\Cref` (plan §3.2's table).

**Marker checklist.** No sentence reads as authorship of the framework (Style Trap 13);
`wu2025pihm` at the head of §3.3 and at each construction; our numbers absent from §3.2–3.5 and in
§3.6 only as pointers; the three questions close the chapter; ≤ 4 pp.

**Traps.** "Collocation"; the legacy adder-ladder reconstruction; any Θ̃(N²) floor.

---

### 5.4 Chapter 4: The Standard Form: Encoder Cost and Hamiltonian Cost (4 pp; Model Formulation /30)

**Purpose.** Answer Q(i). Build the paper's encoding as published, then the best exact encoding of
its regime, and show that even the best encoder leaves the degree Θ̃(N^{2k}), because the cost is the
Hamiltonian's.

**Criterion.** Formulation, band 4: "a significant advance in the state of the art". S2 is a
verified construction.

**Sources.** Planning §3.7, §6.3; claims A-06–A-08, A-12, C-01, C-02; `src/pihm/circuits/standard.py`,
`arithmetic.py`; `docs/11_pillar1.md`; derived keys `derivative/n<n>` (structured and published α).

**Scaffold.**

1. **§4.1 The published encoding, rebuilt (0.75 p).** Figs 2, 8 and 9 built; what is measured against
   each claim (qubits, gates after decomposition, error, prefactor). **The key number:** α/‖𝔾‖₂ for
   the published normalisation, growing as N³ (`\res{derivative/n7}{published_ratio}`). Fig. 9's
   exact wiring cannot be rebuilt from the figure; the rebuilt circuit's α is below the printed
   prefactor, so every published-encoding cost quoted is the kinder side. Deviations →
   Appendix D. The published encoder is also composed into the same stacking, so its degree is
   costed like the others (§8.3).
2. **§4.2 An exact factorisation of 𝔾 (1 p).** The idea in words (a row-0 weight × a
   parity-selected shift × the column index); the proposition 𝔾 = R₀(2U_odd)Λ; proof → Appendix E;
   the measurement quoted as verification, not evidence.
3. **§4.3 Circuits and cost (1 p).** Λ as a Z-string LCU; U_odd by subtraction with a post-selected
   borrow flag (wrapped terms vanish exactly); R₀; the cost proposition (α_G = N(N−1), O(n²) gates,
   n + O(log n) ancilla, the Ω(n) from the N/2-term LCU); lifts, rank-one rows by the feature map,
   products sharing one ancilla register. Figure F3: U_odd's SELECT.
4. **§4.4 What remains: the standard-form Hamiltonian (1.25 p).**
   - For constant coefficients α_H/‖H_std‖ stays bounded (C-02): the encoder has done its job.
   - But ‖H_std‖ = Θ(N^{4k}) against a flat gap, so by `eq:degree` d = Θ̃(N^{2k}): Θ̃(N⁴) for the
     paper's second-order panels. **This is the Hamiltonian wall**: α_H ≥ ‖H‖ for any block
     encoding, so no encoder removes it.
   - The classical reading (§2.3): H_std is the least-squares functional of an order-k operator, and
     squares its conditioning.
   - **The scope, volunteered:** for a lifted variable coefficient (R3's 1 − x²), the structured LCU
     pays ‖𝕄_a‖‖𝔾²‖ ≫ ‖𝕄_a𝔾²‖, so the encoder wall reappears there; §8.3 therefore quotes the
     ideal-encoding bound beside every as-built cost (T-25).
   - Close by naming Ch. 5 and what it changes: the Hamiltonian.

**Figures and tables.** F3; optionally a four-row table of α/‖𝔾‖₂ (structured, published) at
n = 2, 4, 7, 10 from the `derivative/n<n>` keys; the full table → Appendix E.

**Marker checklist.** The published build reported as a test of each claim, with its verdict; the
factorisation a proposition with its proof pointed to by content; §4.4 makes the encoder/Hamiltonian
distinction unmissable and states the R3 caveat; S2 serves the comparison.

**Traps.** "Our standard-form solver"; legacy ε_G bounds; implying the structured encoding is tight on
every problem.

---

### 5.5 Chapter 5: The Descriptor Reformulation (9.5 pp; Model Formulation /30, the core)

**Purpose.** Answer Q(ii): the headline, written as the methods section of a journal article,
including the reformulation's own challenge and its cure.

**Criterion.** Formulation, band 4, "warranting publication". The body carries the idea, the object
(stated once), the cost (a formal result), the challenge and the interpretation; entries,
constructions and proofs go to Appendices B and G.

**Sources.** Planning §3.4, §3.7 ("Descriptor: the flat LCU compiled from the term IR"), §6.4;
`docs/02_methods.md` §3.2; `docs/13_descriptor.md`; `docs/14_descriptor_gap.md` (the challenge); claims B-01–B-07,
B-14, B-20, B-21, C-05, C-06; `src/pihm/assemble/descriptor.py`, `systems.py`, `ir.py`,
`circuits/lcu.py`, `problems/scales.py`.

**Scaffold.**

1. **§5.1 The idea (0.75 p).** In words: differentiation of a Chebyshev series is banded if the
   derivative may live in a neighbouring basis; so do not substitute the dense 𝔾, but keep its banded
   factors, carrying the derivatives as unknowns where the equation needs them. The antecedents
   re-credited (§2.3) and the increment named. **Figure F4**: the sparsity of A_std against A_desc
   for R2a at n = 4. The spine sentence.
2. **§5.2 The banded factorisation (0.5 p).** 𝔾 = B̃⁻¹D̃ from c_r p_r − p_{r+2} = 2(r+1)a_{r+1}; B̃ on
   its diagonal and second superdiagonal, D̃ on its first; entries → Appendix B.
3. **§5.3 Two layouts and kernel equivalence (1.75 p).**
   - *The chain* (order k ≥ 2): w = (f̂⁽⁰⁾; …; f̂⁽ᵏ⁾), padded to 2^⌈log₂(k+1)⌉ blocks; the block rows
     (recurrences −D̃f̂⁽ʲ⁾ + B̃f̂⁽ʲ⁺¹⁾ = 0, the equation row, padding) in **Table T5**.
   - *The mass form* (first-order equations and systems): no derivative block, since the equation
     gives the derivative; the standard rows multiplied through by I⊗B̃, I⊗D̃ − 𝔸⊗B̃ for z′ = 𝔸z; one
     block per component; the state, initial state and readout are the standard form's.
   - **Theorem (kernel equivalence)**, both layouts: ker A_desc = {(p, 𝔾p, …, 𝔾ᵏp) : p ∈ ker A_std}
     for the chain, and ker A_desc = ker A_std for the mass form, because B̃ is invertible. Proof in
     five lines in the body if it fits, else Appendix G.
   - The least-squares ground states differ by row weighting and converge to the same function (B-02).
   - **Volunteer the cost in the same breath:** the chain grows the state from N to 2^⌈log₂(k+1)⌉·N;
     the mass form grows nothing.
4. **§5.4 Constraints, PDEs and coupled fields (0.75 p).** Constraint rows on the block they read;
   Neumann on the f′ block, the same atom as Dirichlet, no 𝔾; PDEs: one field block and a chain per
   axis; datum slices for initial and boundary *functions*, available to both forms (so "the
   descriptor avoids doubling for linear PDEs" is **not** claimed, B-20); coupled first-order
   fields in mass form.
5. **§5.5 The gap of a carried derivative (1.0 p) — the challenge.**
   - The mechanism: on states satisfying the recurrences, the Rayleigh quotient of H_desc is
     ‖R_std p‖² / Σ_j‖𝔾^j p‖², so the norm carries every derivative, and the gap is flat only where
     the equation controls each carried derivative.
   - Where it fails: a leading coefficient that vanishes (the gap falls as N⁻⁴ at a simple endpoint
     zero, N⁻² inside); two axes, where the equation constrains only a sum of top derivatives; and
     the field block crowded out of the ground state, so an initial state on it has tiny overlap
     (R2c unscaled: field weight ~5e-6; planning values).
   - What it is not: the lift, the padding, the precision, the constraints, the basis and the
     reference method are ruled out (one sentence; the evidence → Appendix G).
6. **§5.6 Block rescaling (1.0 p) — the cure and its limits.**
   - f̂⁽ᵐ⁾ ↦ ζ^{−m} f̂⁽ᵐ⁾ (`eq:block-rescaling`): S diagonal and invertible, so the kernel and the
     field block's readout are unchanged. **In the circuit it multiplies each LCU term's coefficient
     by ζ to the order of its column block: no gates, no ancilla.**
   - **The a priori rule** (never fitted): ζ = 2|ā₀/ā_k|^{1/k} for a one-axis ODE whose leading
     coefficient has no zero on [−1, 1]; N/2 where it has one; N per PDE axis, balanced by the
     top-order coefficients (the wave's (cN, N)). Padding decouples; c_pad = 1.
   - What it restores: an O(1) gap on every one-axis panel the descriptor runs, and γ² of order
     0.01–0.76 against as little as 1e-19 unscaled (planning values; §8.4 has P8's).
   - **What it does not:** where the leading coefficient vanishes, ‖H‖ grows as ζ^{2k}, so the
     degree is about Θ̃(N²); on two axes the gap still falls with N; **a double zero is beyond any
     block rescaling** (the paper's own R3c and R3d multiply by (1 − x²)), which is why the
     descriptor runs the problem with simple zeros. General equilibration costs Θ(P) gates and is
     excluded from circuit paths.
   - The analogy, stated once: this is the descriptor's version of Olver & Townsend's diagonal
     preconditioner.
7. **§5.7 The block encoding: one flat LCU (1.25 p).** Every block a short sum of SHIFT·diag terms
   (truncated shifts through one overflow qubit; diag(k) as a Pauli-Z sum; near-constant diagonals
   by reflections); the rescaling in the coefficients; a system's coupling 𝔸 as a sum of matchings;
   rank-one rows through the feature map, with no dense state preparation. **Figure F5** (quantikz)
   and an **algorithm** (term IR → PREPARE/SELECT/PREPARE†) with a line-referenced walkthrough
   (Snow's model).
8. **§5.8 Cost of the descriptor encoding (1.0 p).**
   - **Proposition (structure):** an exact block encoding; ⌈log₂(n+4)⌉ + 8 ancilla for R2's system
     rows (O(log n): the block register, the term selector, the overflow and projection flags);
     O(n²) gates. Proof → Appendix G. With Ω(log L), the ancilla count is order-optimal *among exact
     LCU encodings*; hedge exactly that far.
   - **Measured (assert, with `\res`):** α/‖A_desc‖ → 1 on regular one-axis problems, about 2 on
     singular ones, 2.3–4.1 on PDEs (B-04).
   - **Interpretation, two paragraphs:** what O(log n) ancilla mean beside the standard form's Ω(n);
     and, volunteered, that at reachable n the descriptor's gate count per query is *higher* than the
     structured standard form's (more terms, the block register) and level with it by n = 8 on R2a,
     so its advantage is the degree, not the gates per query.
9. **§5.9 Consequences for the spectrum and the filter (1.25 p).**
   - ‖H_desc‖ = Θ(N²); with the rescaled gap flat on a regular one-axis problem, `eq:degree` gives
     **d = Θ̃(N)**, against Θ̃(N^{2k}) (`eq:standard-wall`); about Θ̃(N²) or faster where the leading
     coefficient vanishes or on two axes (C-05 as restated).
   - The relative gap, stated precisely: the standard form's ground state is below double-precision
     resolution by `eigh`, **not** by SVD; the consequence is the degree, not unresolvability (B-07,
     B-23).
   - One query's post-selected success on a Haar-random input is Θ(1) here against N⁻¹ per axis in
     the structured standard form (B-14): it compares the encodings, not a cost of the pipeline.
   - The comparison will be quoted as built and at α = ‖R‖, and the expected reversals named (R3 at
     the ideal bound; the heat panel at small n); pointers to §8.3–8.4.
10. **§5.10 Summary (0.25 p).** Four numbered takeaways, one of them a limit, and the spine.

**Figures and tables.** F4 (sparsity, from `pihm.pipeline.solutions`' structure view), F5 (flat LCU),
Algorithm 5.1, T5 (block rows); optionally T5b (the descriptor's term types: arity, gates, verified
residual).

**Appendix offloads.** Appendix B: B̃, D̃ entries and the ultraspherical identities. Appendix G: the
block rows in full, the padded count, the mass form, the kernel-equivalence proof, the gap mechanism
and its ruled-out artefacts, the rescaling rule and its checks against a grid, the term IR and its
compilation, the matchings, the cost proof.

**Marker checklist.** A referee could re-derive A_desc from the body plus B and G; the Hilbert-space
and per-query costs volunteered; ultraspherical and first-order least squares credited at §2.3 and
§5.1–5.2; the cost a proposition and interpreted; the ancilla claim O(log n) with optimality hedged;
the gap's failure owned with its mechanism; the rescaling's limits stated; every body equation
passes the equation test.

**Traps.** "O(1) ancilla"; "+ 6 ancilla"; "bit-identical a-block"; "the gap is Θ(1)" unscoped;
"rescaling costs Θ(n_f) gates"; "ζ fitted"; "only the descriptor can prepare nonlinear solutions".

---

### 5.6 Chapter 6: Polynomial Nonlinearity (4 pp; Model Formulation /30)

**Purpose.** Answer Q(iii): separate what the doubled space can claim (an exact encoding, a
projection) from what the Carleman lift can (a preparation, in both forms), and set up the fluids.

**Sources.** Planning §3.6, §5.3 (R6–R10), §6.5, §7.7; `docs/02_methods.md` §3.4–3.5; claims A-10,
B-12, B-18, B-19, B-22, C-09, C-10; `src/pihm/carleman.py`, `problems/fluids.py`,
`circuits/tensor.py`, `circuits/folds.py`.

**Scaffold.**

1. **§6.1 Two treatments (0.25 p).** The doubled space (the paper's; run here in the standard form
   only, since it projects in either) and the Carleman lift (both forms).
2. **§6.2 The doubled space (0.6 p).** An exact encoding; kernel dimension N² minus the rank, at least
   2^{2n−1} (A-10, measured); **Proposition (imaginary time projects; no answer-independent penalty
   isolates the solution)**: a kernel containing ψ⊗ψ and φ⊗φ contains their sum, which is not a
   product state, so no Hamiltonian enforces the product structure; imaginary time projects the initial state onto the
   kernel; the paper's choice reported as the product state of least residual.
3. **§6.3 The Carleman lift in space–time (1.25 p).**
   - z = (u, u^{⊗2}, …, u^{⊗K}) in the symmetric layout, carried as u/s with s = max(‖u₀‖, 1), a
     diagonal similarity that keeps no level growing as ‖u₀‖^k.
   - The truncation error is O(ρ^K) for ρ = ‖u₀‖‖F₂‖/|Re λ₁(F₁)| < 1: **a sufficient condition, a
     worst case over all states**; the convergence is measured per order against the exact lift
     (§8.5).
   - A linear IVP has one solution, so the space–time residual has a one-dimensional near-kernel:
     the uniqueness is Carleman's, not the form's.
   - The two time discretisations: standard 𝔾_t ⊗ I − (T/2) I ⊗ 𝔸_K; descriptor mass form
     D̃_t ⊗ I − (T/2) B̃_t ⊗ 𝔸_K = (B̃_t ⊗ I)·(standard). Same kernel, a banded invertible left factor
     apart: the like-for-like comparison of R8–R10.
   - Initial data by ratio rows; the error split into the lift's and the time axis's.
4. **§6.4 Products and couplings on a circuit (0.75 p).** The nodal fold 𝕟₁^{(p)} =
   2^{pℓ/2}𝕌†Δ_p𝕌^{⊗p}: no ancilla beyond padding, α = 2 = ‖𝕟₁‖ for p = 2, so **optimal, not merely
   tight**; the Fourier fold QFT, copy, QFT†; the Chebyshev DCT budgeted as a cited primitive
   (Klappenecker–Rötteler), **not built gate-level**, said plainly. The lift's coupling 𝔸_K: as
   matchings in the symmetric layout, or in the **tensor layout with 2K − 1 terms** (not K²), each
   F_p on adjacent slots, which reaches field scale.
5. **§6.5 Fourier–Galerkin fluids (0.75 p).** Burgers: F₁ = diag(−νk²), F₂ the (u²)ₓ/2 convolution.
   2-D vorticity Navier–Stokes on the real cos/sin basis with ψ̂ = ω̂/|k|² eliminated and exact
   rational couplings. Taylor–Green (its modes share |k|, so the lift is exact: a validation) and a
   counter-rotating vortex pair (active triads). References: the Galerkin system's IVP, Cole–Hopf
   for Burgers, a pseudo-spectral simulation for the truncation's own error.
6. **§6.6 Preparation versus projection (0.4 p).** **Table T8**: which route sits on which side, and
   why. **The caveat that matters:** a unique, trusted kernel certifies the lifted *linear* problem,
   not the lift's convergence, which is measured separately (§8.5). One sentence tying back to
   §5.1: the mass form is the same banded left factor, applied in time.

**Marker checklist.** "Prepared" never for the doubled space; ρ stated as sufficient; fold optimality
distinguished from tightness; the DCT named as unbuilt with the reason; uniqueness attributed to
Carleman; trust distinguished from convergence.

**Traps.** "K² terms"; "both forms" for the doubled space; ρ < 1 as necessary.

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
§3.7–3.8, §5.4, §6.2, §7; claims C-03, C-04, C-08, B-13, B-16, B-17, B-24; `docs/FILTERS.md`.

**Scaffold.**

1. **§7.1 Overview and model configuration (0.75 p).** **Figure F1**, the model configuration:
   problem specification → residual (standard | descriptor; nonlinearity none | doubled | Carleman;
   shared constraint rows) → stacked-residual block encoding U_R → reflection V → walk W → GQSP
   filter → post-selection → decoded field, with the classical reference and the verification modes
   and tiers attached to the stages they check. Its caption stands alone. The design principle in one
   paragraph.
2. **§7.2 Problems and model inputs (1.0 p).** **Table T3**, the benchmark ladder R1–R10: one new
   capability each, so a failure localises, with its physics (full specifications → Appendix J).
   **Table T2**, the constraint kinds (zero, collapse, ratio, datum slice): the rubric's "boundary
   conditions". A problem is data: equation terms, constraints, regular datum, reference. The paper's
   panels as printed appear only in the reproduction (T-27). The inputs every run records: n per
   axis, form, encoder, filter, ε = 1e-6, initial state, rescaling, Carleman order K.
3. **§7.3 The classical reference (0.5 p).** The smallest right singular vector of the stacked R:
   dense SVD to 8,192 physical columns (accuracy by Wedin's bound); beyond, shift-invert Lanczos on
   the augmented system [[I, R], [R†, −μI]], which never squares R, then Rayleigh–Ritz, with an a
   posteriori estimate. Trusted means a one-dimensional kernel with its ratio above 20, the largest
   spacing the ladder's spectra show without one. Why never `eigh(RᵀR)` (one number; the table →
   Appendix I). Decoding, η_e, and the metrics at three levels (operator, state, field).
4. **§7.4 From stacked residual to quantum walk (0.75 p).** **Proposition (stacked reflection)**:
   for U_R encoding R = [R_1; …; R_L] with α_R = √(Σα_j²), V = U_R†(2Π − I)U_R is a Hermitian unitary
   with Π_in V Π_in = 2H/α_R² − I, and controlled V needs only controlled reflections (proof →
   Appendix F). W = (2Π_in − I)V, Π W^k Π = T_k(H′). The quadrature composition has no ℓ¹ penalty.
5. **§7.5 The filter and its parameters (1.0 p).**
   - GQSP realises any |P| ≤ 1 polynomial of the walk, without parity (prior art, §2.5).
   - **The minimax edge filter**, P = T_d(w(x))/T_d(w(−1)), w mapping the excited spectrum [x₁, 1]
     onto [−1, 1], at the least degree that suppresses it to ε relative to the ground value:
     d = ⌈arccosh(1/ε)/θ₀⌉, θ₀ = arccosh(−w(x₀)), computed from heights above the edge so the ground
     state's is resolved.
   - **The parameters are a priori:** the edge (σ₀, σ₁ of the reference) and α_R, never the
     solution. The edge is assumed known, the standard known-gap assumption; say so here and in
     §9.6.
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
   - **Deviations from Wu et al.**, a short list: GQSP for mixed-parity QSVT; normalisation by the
     construction's α for ‖H‖_F; the minimax filter for imaginary time; parameters from the edge.
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
   (Appendix F), and its study at scale is future work.
8. **§7.8 Design of the numerical experiment (0.5 p).** What the study varies (n, form, encoder,
   filter, initial state) and holds fixed (constraints, ε); what counts as a gate (transpiled to
   {cx, u}, dense cited primitives counted apart); ancilla counted on the composed V. **Fairness,
   declared:** the structured encoding is the strongest standard-form baseline built, and every
   comparison is quoted as built and at α = ‖R‖ (T-25), so a reported advantage is not an encoder
   artefact. The tier is marked on every number.
9. **§7.9 Software and computation (0.25 p).** `pihm` (numpy, scipy, qiskit, qiskit-aer): one
   implementation per concept, problems as hashed data, tests of each claim; production on Setonix;
   every number regenerated from archived records by one command (Appendix L). No code listings.

**Marker checklist.** A configuration diagram; every input option with its value; the software
described; the experiment's design and fairness justified; the deviations from the paper listed; the
T2 ≡ T1 argument before any T2 number; the readout classical, the protocol attributed.

**Traps.** A software manual; "Pillar" and "tier" jargon; QITE presented as the comparison's filter;
the readout presented as new or as the method's readout.

---

### 5.8 Chapter 8: Numerical Study (10.5 pp; Results & Discussion /30)

**Purpose.** Evidence every claim of the Abstract and of §1.3, "without reference to any other
documents", one section per question or contribution.

**Criterion.** "Complete, clearly presented results, with detailed discussion showing insight… or
warranting publication." Every figure is interpreted in prose; each section ends with what it
established.

**Sources.** P8's records (`results-v1`) through `\res`; the reports `docs/10_reproduction.md`,
`11_pillar1.md`, `12_pillar2.md`, `13_descriptor.md`, `FILTERS.md`, `EXTENSIONS.md`, `NAVIER_STOKES.md`,
`18_claims.md`; the notebooks of Planning §10.8, one per figure.

**Opening (0.25 p).** What each section evidences; the tiers; the records' provenance in one
sentence; the full per-problem results → Appendix J.

**Scaffold.**

1. **§8.1 Reproducing Wu et al. (1.75 p; S1).** **Table T6**: η_e for the 11 ODE panels (printed,
   ideal ‖b‖², ours at the printed n) and a summary line for the five others (Appendix K has all
   16). The closed form η_e = (N/π)∫f²/√(1−x²) and what it validates: our conventions are the
   paper's. **Figure F6** (nb 11): the panels as printed against the problem for Fig. 5, the
   distortion from rounded points and Maclaurin sources. The Fig. 6 and 7 non-reproductions and the
   hypotheses tested; the Laplace typo; the heat panel's backward data. The paper's quantum claims
   (nb 12): the time rule falls short of ε (A-11), the linear H is semi-definite where the discrete
   solution is exact (A-09), the doubled-space kernel count (A-10). The claims verdicts → Appendix K
   (one paragraph here).
2. **§8.2 The pipeline is faithful (1.5 p; S3).** Operators equal the assembled residuals in every
   mode (**Figure F7**, nb 20). The circuit equals the emulation before normalising, ≤ 1e-10, on every
   T1 record (nb 31). Every trusted preparation within ε and its a priori bound (nb 30); the decoded
   field within its budget (**Figure F8**, nb 32). What the answer-independent choices cost: γ for
   the initial states, and an underestimated gap (nb 33). The filter study in one table and two
   sentences (nb 34; B-17).
3. **§8.3 Where the cost lies (2.0 p; Q(i), Q(ii); C, S2).** **Figure F9, the headline** (nb 40):
   against N, the encodings' looseness α_H/‖H‖, the Hamiltonians' relative gap, and the degree
   (which grows as the square root of the first over the second), for the published, structured and
   descriptor encodings, with fitted exponents; T2 points where measured and T3 beyond, visibly
   distinguished. **Table T7** (nb 21, 40): published | structured | descriptor, across ‖H‖ scaling,
   gap, α/‖·‖, cx per query, ancilla, exactness, degree at n = 8 as built and at α = ‖R‖, and the
   degree's exponent. **Figure F10** (nb 41, optional): case by case, the descriptor's cost over the
   standard form's, as built and at the ideal bound, with the reversals marked. Interpretation: the
   encoder wall (published to structured) and the Hamiltonian wall (structured to descriptor) as two
   gaps on one plot.
4. **§8.4 The descriptor's gap and its rescaling (1.75 p; the challenge).** **Figure F11** (nb 42):
   the gap and γ² unscaled against rescaled, every panel; the a priori rule against the best ζ on a
   grid; where it stops (two axes, the singular ‖H‖ growth). **Figure F12** (nb 43): three
   representative problems in both forms, each with its solution and cost: R2c (stiff: rescaling's
   biggest gain), R3a (a leading coefficient with zeros: where the ideal-bound comparison reverses),
   R5b (heat on two axes: the gap still falls, and the descriptor costs more at small n). The rest →
   Appendix J.
5. **§8.5 Nonlinear problems (1.5 p; Q(iii), S4).** R6's kernel beside R8's (the projection
   evidence: kernel dimensions against one) (nb 61). R8: the K × n_t error surface and the degree in
   both forms (C-09). R7: the mass form against the chain (nb 60, one sentence or two). R9, viscous
   Burgers (**Figure F13**, nb 62): the lift's error per order follows a/ν (about a/5ν) and not ρ,
   which grows with the modes; past a/ν ≈ 5 the lift diverges while its kernel stays unique and
   trusted: a negative finding with its analysis.
6. **§8.6 Case study: two-dimensional Navier–Stokes (1.25 p).** **Figure F14** (nb 70): vorticity
   snapshots and the degree pairs. Taylor–Green validates F₁, the rows and the time axis (the lift
   exact to rounding). The vortex pair at a/ν = 3, 10 and 30 on 12–80 modes: the lift's convergence
   and the truncation against a direct simulation; every exact emulation within ε; the descriptor's
   time axis lowers the degree in every pair, the ratio narrowing as the modes grow (C-10). The tensor
   layout to 316 modes in 2K − 1 terms, with its gates per query against the matchings (B-19). T1 is
   beyond the simulation budget here, with its estimate quoted: said plainly.
7. **§8.7 Summary of findings (0.5 p).** Six or seven numbered findings, **at least two negative**,
   for example:
   1. the paper's ODE results reproduce, its PDE and nonlinear ones do not;
   2. the cost of the standard form is its Hamiltonian's;
   3. the descriptor's degree advantage: large on one axis, modest on two, reversed on the heat panel
      at small n and on R3 at the ideal bound;
   4. the descriptor's gap erodes where derivatives are uncontrolled; rescaling restores it on one
      axis only;
   5. the pipeline is verified end to end at every size it reaches;
   6. Carleman prepares in both forms, but a trusted kernel can hide a diverging lift;
   7. Navier–Stokes is reached by exact emulation and estimate, not by circuit simulation.

**Marker checklist.** Every number's tier marked; "could not simulate" kept apart from "cannot
reach"; at most three in-depth problems; every caption stands alone; at least two negative findings;
every Abstract number backed here; §8.1 framed as a test of the paper.

---

### 5.9 Chapter 9: Discussion (4.5 pp; Results & Discussion /30)

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
   Θ̃(N^{2k} poly n) on a regular one-axis problem. **Neither is poly-log: say it first.** The minimax
   filter changes the constant, not the Θ. Hedge any "for every filter" statement to what Lin & Tong's
   optimality and the linear-system κ lower bounds support. The edge-known assumption.
3. **§9.3 What the reproduction says about the published method (0.75 p).** Conventions sound and
   η_e right; printed choices distort; PDE and nonlinear panels unreproduced; normalisation loose; the
   time rule short of ε; the readout identity needs p_G < 1. Collegial and evidential; what it means
   for readers of the paper.
4. **§9.4 Where the construction applies (0.5 p).** **Table T9**, an applicability map (Green's Fig.
   4.18 is the model): problem class (regular one-axis ODE; leading coefficient with a simple zero;
   double zero; two-axis PDE; first-order systems; nonlinear with a converging lift; past the lift's
   boundary) × the descriptor's gain × what to do. Guidance a practitioner could act on.
5. **§9.5 Feasibility on fault-tolerant hardware (0.5 p).** Logical qubits, cx per preparation and
   depth at meaningful n from T3; set beside explicit resource counts for linear-system ODE solvers
   (Jennings et al.), hedged; why NISQ is out of scope.
6. **§9.6 Limitations (0.75 p).** Each with its analysis: no hardware; circuit simulation only at
   small n; the spectral edge assumed known; the DCT a cited primitive; the doubled space projects;
   Navier–Stokes bounded by emulation and estimate; the descriptor's Hilbert-space and per-query cost;
   the double zero excluded; the iterative reference's bound an estimate; trust is not convergence;
   Figs 6–7 unreproduced (authors not contacted).

**Marker checklist.** Explains rather than restates; the complexity argument consistent with §3.6,
§4.4 and §5.9; every limitation owned with its analysis; consequences for the field drawn.

---

### 5.10 Chapter 10: Conclusions and Future Work (2.5 pp; Conclusions /10)

**Scaffold.**

1. **§10.1 Conclusions (1.25 p).** A verdict per contribution (C, S1–S4), mirroring §1.3, each with
   its headline number once more. Close with the transferable principle (the spine generalised:
   *condition the residual before encoding it*).
2. **§10.2 Future work (1.25 p).** Four or five items, each with a motivation and **a concrete first
   step**:
   1. on-circuit gap or edge estimation, removing the known-edge assumption;
   2. a rescaling (or reformulation) that keeps the gap on two axes, the descriptor's open problem;
   3. a gate-level DCT, so the Chebyshev fold is fully built;
   4. hardware validation of R1 at n = 2 (its circuit is small enough to state);
   5. the research proposal's aims: complex-valued and non-Hermitian equations (which GQSP
      permits) and data-informed constraint rows;
   6. (candidate) the paper's interferometric readout at scale, with shot-count studies.
   Choose four or five.

No new results and no new citations in this chapter.

---

## 6. Appendices (outside the page limit)

| | appendix | content | cited in |
|---|---|---|---|
| A | Quantum gate reference | the gate table; multi-controlled decompositions | §2.1 |
| B | Chebyshev and ultraspherical identities | normalised basis, S, 𝔾 entries, the B̃/D̃ recurrence, the ultraspherical connection, the N = 4 instance | §2.3, §3.3, §5.2 |
| C | Wu et al.'s standard form in full | worked N = 4 residual; 𝕄_{x^p}, 𝕄_a, 𝕟₁, 𝕟_x; the printed SM §A matrices reproduced (A-01) | §3.3 |
| D | The published circuits as built | Figs 2, 8, 9 rebuilt; every deviation; measured qubits, gates and ε_G(n); the prefactor against ‖𝔾‖₂ | §4.1 |
| E | The structured exact 𝔾 encoding | the factorisation proof; Λ, U_odd (subtraction with borrow), R₀; the cost proof; α across n | §4.2–4.3 |
| F | Shared pipeline identities | the stacked reflection; qubitisation (one power, then one restriction); the controlled walk; imaginary-time coefficients and Σ\|q_k\| = 1; the minimax edge filter and its degree; GQSP phases; the interferometric readout and the identity for p_G < 1 | §7.4–7.7 |
| G | The descriptor construction in full | block rows; the padded count; the mass form; the kernel-equivalence proof; the gap mechanism and its ruled-out artefacts; the rescaling rule and its checks; the term IR and its compilation; matchings; the cost proof | §5.3–5.8 |
| H | The nonlinear route in full | the doubled-space algebra and kernel; the Carleman lift (symmetric and tensor layouts, the level scale); ratio rows and space–time forms; the folds; Fourier–Galerkin F₁ and F₂ for Burgers and Navier–Stokes; R9 and R10's panels | Ch. 6 |
| I | Verification protocol | modes, sizes and tolerances; structured probes; per-term residuals; `eigh` against SVD (A-3); the iterative reference and its checks against the dense SVD; the T1 memory and time model; acceptance and the error budget | §7.3, §7.6 |
| J | Benchmark catalogue | R1–R10: equations, references, constraints, n-grids, parameters; a per-problem results table (both forms, tiers) | §7.2, §8.4 |
| K | Reproduction record | all 16 panels; the Fig. 5 triage; the non-reproductions; the paper's claims A-01–A-13 with verdicts; the tau-truncation ablation | §8.1 |
| L | Software and reproducibility | `pihm`'s architecture; records, provenance and the source digest; campaigns and Setonix; tests; regenerating every figure and number; environment pins | §7.9 |
| M | Research proposal, with deviations | the proposal verbatim and the deviations table (§13.4) | – |

**The pointer rule:** never "see Appendix E"; write "the factorisation's proof and the borrow-flag
SELECT are given in Appendix E". **Appendix L** exists for the rubric's "software tools" and the
guidelines' "laboratory handbook" role; keep it factual and short (3–4 pp).

---

## 7. Figures and tables

**Body figures** (the figure test applies to each; optional ones go first if over budget):

| # | figure | section | source | tier |
|---|---|---|---|---|
| F0 | concept: degree = √(looseness/relative gap), the two walls (optional) | §1.2 | TikZ | n/a |
| F1 | model configuration (the pipeline) | §7.1 | TikZ | n/a |
| F2 | the GQSP circuit (optional) | §7.5 | quantikz | n/a |
| F3 | U_odd's SELECT (subtraction with borrow) | §4.3 | quantikz | n/a |
| F4 | sparsity of A_std against A_desc | §5.1 | `pipeline.solutions` structure view | exact |
| F5 | the descriptor's flat LCU | §5.7 | quantikz | n/a |
| F6 | panels as printed against the problem (Fig. 5) | §8.1 | nb 11 | classical |
| F7 | verification accuracy against n | §8.2 | nb 20 | exact/probe/IR |
| F8 | decoded field with its error budget | §8.2 | nb 32 | T1/T2 |
| F9 | **headline:** looseness, relative gap and degree against N, three encodings | §8.3 | nb 40 | T2 + T3 |
| F10 | the forms head to head, as built and at α = ‖R‖ (optional) | §8.3 | nb 41 | T3 |
| F11 | the gap and γ², unscaled against rescaled | §8.4 | nb 42 | classical |
| F12 | three representative problems, both forms | §8.4 | nb 43 | classical + T2/T3 |
| F13 | the lift's convergence against a/ν (R9), with R8's surface | §8.5 | nb 61, 62 | classical + T2 |
| F14 | Navier–Stokes: vorticity and the degree pairs | §8.6 | nb 70 | T2 + T3 |

**Body tables:** T1 approaches (§2.2); T2 constraint kinds (§7.2); T3 benchmark ladder (§7.2); T4
verification modes and acceptance (§7.6); T5 descriptor block rows (§5.3); T6 η_e reproduction
(§8.1); **T7 the headline three-encoding table (§8.3)**; T8 preparation versus projection (§6.6); T9
applicability map (§9.4).

**Captions** (style guide §3.4): a bold claim, then what is plotted, on which axes, for which
problem and parameters, then each panel, then the takeaway, then the tier. Figure captions below,
table captions above.

---

## 8. Notation

### 8.1 Master table (it becomes `1_header/6_notation.tex`)

| symbol | meaning | first use |
|---|---|---|
| n, N = 2ⁿ | qubits per Chebyshev axis; truncation dimension | §3.2 |
| k; p | equation order; polynomial degree of a nonlinearity | §3.3; Ch. 6 |
| τ(x), \|τ(x)⟩ | the paper's raw Chebyshev feature state | §3.2 |
| ψ, η, η_e | normalised coefficient state; scale; η_e = ‖b‖² | §3.2 |
| 𝔾 | differentiation (dense, strictly upper triangular; ‖𝔾‖₂ = Θ(N²)) | §3.3 |
| B̃, D̃ | banded factors, 𝔾 = B̃⁻¹D̃ | §5.2 |
| 𝕄_{x^p}, 𝕄_a | multiplication (lift; smooth coefficient) | §3.3 |
| 𝕟₁, 𝕟_x | product-to-sum folds | §3.5 |
| 𝔹(x), 𝔻⁽⁰⁾(x_s) | rank-one zero and collapse rows | §3.3 |
| x_z, x_m, x_s | constraint points (zero, extremum, regular datum) | §3.3 |
| A_std, A_desc; H_std, H_desc | residuals; Hamiltonians H = R†R | §3.3, §5.3 |
| R = [R_1; …; R_L]; σ₀, σ₁, σ_max | stacked residual; its singular values | §7.3–7.4 |
| w = (f̂⁽⁰⁾; …; f̂⁽ᵏ⁾); n_f | descriptor state (chain); block-register qubits | §5.3 |
| ζ | block-rescaling constant | §5.6 |
| α, α_R, α_H = α_R² | subnormalisations | §2.4, §7.4 |
| V, W, H′ = 2H/α_R² − I | reflection; walk; normalised Hamiltonian | §7.4 |
| Δ, γ | spectral gap λ₁ − λ₀; overlap \|⟨ψ_ref\|φ₀⟩\| | §2.6, §7.5 |
| d, ε | filter degree; target | §2.6 |
| x₀, x₁, w(·), θ₀ | ground value and edge of the excited spectrum on H′'s scale; the edge map; the minimax rate | §7.5 |
| β, q_k | imaginary time and its Chebyshev coefficients (the QITE filter) | §7.5 |
| p_G | the filter's success probability | §7.5 |
| K, M, ρ, s | Carleman order; modes; worst-case ratio; level scale | §6.3 |
| F₁, F₂, 𝔸_K | linear and quadratic terms; lifted generator | §6.3 |
| a, ν, T, n_t | amplitude, viscosity, horizon, time-axis qubits | §6.5 |
| ‖𝔾‖_S | the paper's max(‖𝔾𝔾ᵀ‖₁, ‖𝔾ᵀ𝔾‖₁) | §3.4 |

### 8.2 Collisions (Planning or code → thesis)

| Planning / code | clash | thesis |
|---|---|---|
| τ (imaginary time), `tau` | τ(x) feature state | **β** (T-08), QITE only |
| R (Carleman ratio) | stacked residual R | **ρ** (T-09) |
| λ (block rescaling) | eigenvalues λ₀, λ₁ | **ζ** (T-19) |
| p_j (descriptor blocks); p_k (filter coefficients); p (success) | p nonlinear degree | **f̂⁽ʲ⁾**; **q_k**; **p_G** |
| SHIFTˢ (shift offset) | s the lift's level scale | write the offset as ℓ |
| T1/T2/T3 (tiers) | T_k Chebyshev; T horizon | tiers only in words or upright text labels in tables, never as maths |
| P (padded dimension) | P(z) GQSP polynomial | **dim w** |
| bare A, H | both forms | subscripts (T-07) |
| G, B̃, D̃ (italic, old draft) | 𝔾 etc. | blackboard bold (T-06) |
| G^⊤ applied to ψ (old draft) | upper-triangular 𝔾 | 𝔾, no transpose (T-16) |
| B̃_std (old App. B, raw basis) | std = standard form | **B̃_raw** (T-19) |
| β (old ladder coefficient) | imaginary time | **μ** (T-19) |
| κ (condition number) | – | **cond(·)** (T-19) |
| α, β (qubit amplitudes, §2.1) | subnormalisation; imaginary time | rename while compressing §2.1 |

---

## 9. Claims → thesis register

Status follows Planning §8 and `pihm/docs/18_claims.md`. **Register:** **A** = assert; **H** = assert
with the stated hedge or scope; **N** = narrative only; **X** = do not state. **Rule:** before a
claim ID is cited in prose, its row reads ✅ in the generated `18_claims.md` at `results-v1`; if not,
the prose is rewritten to what is supported.

| ID | claim, as the evidence states it | thesis | register |
|---|---|---|---|
| A-01 | 𝔾, 𝕄, 𝕟₁, 𝔹 match the printed SM §A | App C; §8.1 one line | A |
| A-02 | printed η_e, 11 ODE panels, within one unit of the last digit (9/11 when rounded) | §8.1 T6 | A |
| A-03/A-04 | Figs 6–7 η_e not reproduced, hypotheses tested | §8.1; App K | A |
| A-05 | the Laplace solution is a typo | §8.1 footnote | A |
| A-06–A-08 | the published circuits' qubits, gates, prefactors and error | §4.1; App D | A per verdict |
| A-09 | H positive semi-definite where the discrete solution is exact; not always distinct at the bottom | §8.1; App K | A (refined) |
| A-10 | doubled-space kernel ≥ 2^{2n−1} | §6.2; §8.5 | A |
| A-11 | the paper's time rule falls short of ε | §8.1 | A (refuted) |
| A-12 | "poly(n) terms": true for gates, not for α | §3.6; §4.1 | A |
| A-13 | the printed n distorts 5a–5d | §8.1 F6 | A |
| B-01 | 𝔾 = B̃⁻¹D̃ | §5.2 | A |
| B-02 | exact kernels coincide; elsewhere both forms' fields converge alike | §5.3 | A (restated) |
| B-03 | "O(1) ancilla" | – | X → C-06 |
| B-04/B-05 | α/‖·‖ → 1 on regular one-axis panels; ~2 singular; 2.3–4.1 on PDEs | §5.8; T7 | H |
| B-06 | rescaled gap O(1) on one axis; still falls on two | §5.6; §8.4 | H |
| B-07 | relative gap, with the eigh/SVD distinction | §5.9 | A |
| B-08/B-09 | old query and gate scalings | – | X → C-05, §9.2 |
| B-10 | Neumann costs Θ(N²) more | – | X |
| B-12 | nodal fold exact at α = 2, optimal; DCT cited | §6.4 | A |
| B-13 | the composed H verifiable only by parts | – | X: refuted, V verified exactly to 25 qubits |
| B-14 | one query's Haar-average success Θ(1) (descriptor) vs N⁻¹ per axis | §5.9 | H (compares encodings, not a pipeline cost) |
| B-16 | NLFT phases to high degree | App F | A |
| B-17 | minimax 1.67–1.92× fewer degrees at equal suppression; smaller and sometimes reversed at equal measured infidelity | §7.5; §8.2 | A (refined) |
| B-18 | Carleman: a unique kernel at every order; convergence follows a/ν, not ρ; trust misleads past it | §6.3; §8.5 | A (refined) |
| B-19 | tensor layout 2K − 1 terms, cost growing slowly with M | §6.4; §8.6 | A (refined) |
| B-20 | the descriptor avoids doubling for linear PDEs | – | X (neither form doubles) |
| B-21 | rescaling makes R2c reachable | §5.6; §8.4 | A (restated) |
| B-22 | only the descriptor prepares nonlinear solutions | – | X: refuted |
| B-23 | standard-form ground state unresolvable at n ≈ 7 | §5.9 | A (restated: eigh fails, SVD resolves) |
| B-24 | GQSP: any \|P\| ≤ 1, no parity | §2.5; §7.5 | A |
| B-25 | ⟨τ(x)\| an LCU of two product states, plus the constant mode | App F | A if used |
| C-01 | exact structured 𝔾 | §4.2–4.3 | A |
| C-02 | α_H/‖H‖ bounded for constant coefficients; loose for R3's lifted multiplier | §4.4; T7 | H |
| C-03 | the stacked reflection's identities | §7.4 | A |
| C-04 | Σ\|q_k\| = 1; the circuit equals T2 before normalising | §7.5 | A |
| C-05 | degree Θ̃(N^{2k}) (standard, best encoding) vs Θ̃(N) (descriptor, regular one-axis); ~Θ̃(N²)+ where the leading coefficient vanishes or on two axes | §5.9; §8.3 F9 | H (measured exponents with fit ranges) |
| C-06 | ⌈log₂(n+4)⌉ + 8 ancilla for R2's system rows | §5.8 | A |
| C-07 | the ODE reproduction; Figs 6–7 documented | §8.1 | A |
| C-08 | T2 = T1 ≤ 1e-10 | §7.6; §8.2 | A |
| C-09 | Carleman: a one-dimensional kernel in both forms; the descriptor's time axis lowers the degree from n_t = 4 | §6.3; §8.5 | A |
| C-10 | NS: the descriptor's time axis lowers the degree in all pairs at fixed K; the ratio narrows with the modes | §8.6 | A |
| new | the readout identity for p_G < 1 | §7.7; App F | A (one sentence) |
| new | reversals at the ideal bound (R3) and on the heat panel at small n | §8.3–8.4 | A (negative finding) |
| new | per-query gates higher in the descriptor at small n | §5.8; T7 | A |

---

## 10. Code → thesis transfer

### 10.1 Sources of truth

1. **Results:** P8's records, the commit tagged `results-v1`, read only through the exporter and the
   notebooks. Nothing from legacy `Setonix/`, legacy notebooks or the old `docs/`.
2. **The method:** `pihm/docs/02_methods.md`, the method as built. Where it and Planning.md differ,
   02_methods.md and the tests win.
3. **Reasons:** Planning.md and `pihm/docs/DECISIONS.md` explain why; they are never cited. The
   thesis states each choice with its reason (plan §3.5).
4. **History:** the Journal is never cited. Lessons appear only where they are a correctness
   condition of the construction (one power then one restriction for qubitisation; a controlled
   global phase becomes a relative one), phrased as mathematics.

### 10.2 Numbers (T-15)

- **The exporter** (`pihm/tools/thesis/export_numbers.py`) writes `0_results/generated/numbers.tex`
  from the records, keyed like the record directories (`stateprep/R2a/standard/n8/T3`); statistics
  over n come from `tools/thesis/derived.py`. Rerun it after P8's copy-back.
- **The thesis quotes by key**, `\res{<run>}{<metric>}`; formats and flags are in
  `0_results/README.md`. A missing number renders its reason; *infeasible* is a legitimate final
  result ("beyond the simulation budget", estimate quoted).
- **Final.** `export_numbers.py --final` requires every quoted record's source digest to match the
  committed package source (D-130), and makes every draft-only placeholder an error.
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
| `encoder="structured" / "published"` | structured (exact) / published encoding |
| `compose.stacked_reflection` | the stacked-residual reflection V |
| `verify="exact"/"probe"/"ir"` | exact / probe / IR verification |
| `t1` / `t2` / `t3` | circuit simulation / exact emulation / resource estimate |
| `filter="minimax"` / `"qite"` | minimax edge filter / imaginary-time filter |
| `tau` | β |
| `ideal_degree` | the degree at the ideal-encoding bound |
| `trusted` | a trusted (isolated, one-dimensional) kernel |
| `status="infeasible"` | beyond the simulation budget, estimate quoted |
| `carleman=K`, `lift="tensor"` | Carleman order K; the tensor layout |
| Pillar 1 / Pillar 2 | operator verification / state-preparation verification |
| rung R1–R10 | benchmark problem R1–R10 |
| `variant="faithful"` | as printed (reproduction only) |
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
| **W0** ✅ | v1.1 | the scaffold, the notation pass, the guides | done 2026-09-25 |
| **W0b** | v2.0 | the scaffold migration (plan §4.3); the REVISE sweep (plan §2.1); the `ref.bib` audit and additions (T-29, plan §5.2) | before drafting |
| **W1** | now | Ch. 2; Ch. 3; Ch. 4; Ch. 5; Ch. 6; Ch. 7; Appendices A–I | maths and method; numbers render as their placeholders |
| **W2** | P8 copied back; exporter rerun | Ch. 8 in order §8.1 → §8.6; Appendices J, K, L; then every `\res` in Chs 4–7 checked | the numbers freeze |
| **W3** | W2 | §8.7; Ch. 9 | check §8.7's findings against P8 first (TR-1) |
| **W4** | W3 | Ch. 1; Abstract; Ch. 10; Summary of Student Achievement; App M; the title (T-14) | written last, so they promise only what was delivered |
| **W5** | W4 | Verification Mode; Review Mode per chapter; page count; §14; the supervisor's draft (guideline 9) | |

**Supervisor touchpoints (guideline 9: "a general layout for approval, then drafts").** Send §0.1,
plan §0.3 and §3.1–3.2 now as the layout for approval, then drafts after W1 (Chs 2–5) and W4 (the full
draft).

---

## 12. Risks and fallbacks (the rubric protects well-analysed negative results)

| id | risk | likelihood | response in the thesis |
|---|---|---|---|
| TR-1 | P8's records move a finding (an exponent, a ratio, a reversal) relative to the pre-P8 values this plan quotes | medium | the text is written from claims and `\res`; before W3, re-read §8.7's findings and Table T9 against P8 and rewrite what moved |
| TR-2 | fitted degree exponents deviate from 2k and 1 | low–medium | report the measured exponents with their fit ranges; restate C-05 as measured |
| TR-3 | "no encoding beats Θ̃(N^{2k})" over-generalises | medium | claim it for polynomial filters of the walk, which need degree Ω(√(α_H/Δ)); a general lower bound is future work |
| TR-4 | circuit simulation only at small n | certain | designed for: T2 ≡ T1 proven and measured; said once in §7.6 |
| TR-5 | "isn't this ultraspherical, or FOSLS?" | high | credited first (T-26), with the increment stated in §2.3 and §5.1 |
| TR-6 | the concurrent sibling (Paine 2026) is read as pre-empting | low | cite it in §2.2 and §3.6 with what it does and does not do; it proposes alternative constructions and encodings but has no gap scaling in resolution, no circuits and no banded reformulation (read in full 2026-10-04) |
| TR-7 | a marker reads the reversals (R3 at the ideal bound; the heat panel) as weakness | medium | they are numbered findings with their mechanism, and Table T9 turns them into guidance |
| TR-8 | the known-edge assumption is attacked | medium | own it in §7.5 and §9.6; on-circuit edge estimation is future work item 1 |
| TR-9 | page overrun | medium | plan §4.1's trim order |
| TR-10 | the marker ticks Theoretical | low | the formulation chapters already read as journal methods; move 2 pp from Ch. 8 into Chs 4–5 |
| TR-11 | bibliography errors (wu2025pihm's authors) reach submission | certain unless fixed | T-29 at W0b; §14.2 item 1 |
| TR-12 | Figs 6–7 stay unexplained | certain | recorded as not reproduced, hypotheses tested, authors not contacted (Planning decision 17) |

---

## 13. Front matter and required elements

### 13.1 Title (T-14; choose at W4)

- **Keep:** *Quantum Circuits for Solving Differential Equations via Physics-Informed Effective
  Hamiltonians and GQSP Quantum Imaginary Time Evolution.* (Names imaginary time, which is no longer
  the comparison's filter.)
- **Option A:** *Banded Physics-Informed Hamiltonians: A Descriptor Reformulation for Quantum
  Differential-Equation Solvers.*
- **Option B:** *Physics-Informed Hamiltonians for Quantum Differential-Equation Solvers:
  Reproduction, Exact Encoding and a Descriptor Reformulation.*
- **Option C:** *Where the Cost Lies: Reformulating Physics-Informed Hamiltonians for Quantum
  Differential-Equation Solvers.*

The title page and both declaration dates use `\today`: set them to the submission date.

### 13.2 Abstract (≈ 250–300 words; five moves, each with a number)

1. The problem, and Wu et al.'s method, attributed, with its open question.
2. What we found: the exact reproduction; the encoder wall and the Hamiltonian wall, with the three
   degrees at n = 8.
3. The descriptor reformulation: ‖H‖ Θ(N²) against Θ(N⁸), the same kernel, degree Θ̃(N) on a regular
   one-axis problem, O(log n) ancilla; its challenge and the rescaling.
4. How it is verified (T1 = T2 ≤ 1e-10) and how far it reaches (Carleman in both forms; 2-D
   Navier–Stokes on up to 80 modes).
5. The scope: classical computation, no hardware, neither form poly-log.

### 13.3 Summary of Student Achievement (one page, first person, required)

What *you* did: the audit of the legacy pipeline and the decision to rebuild; `pihm`'s design; the
reproduction and its triage; the structured encoding; the descriptor reformulation, its gap
investigation and the rescaling rule; the verification framework and the GQSP circuit engine; the
filter study; the Carleman and Navier–Stokes extensions; the Setonix production; the thesis. Name
the help received: the supervisor; AI coding assistance, if the School's policy requires it to be
declared (check it, and mirror it in the Acknowledgements, guideline 8).

### 13.4 Research proposal deviations (Appendix M)

| proposed (May 2025) | outcome | why |
|---|---|---|
| QSVT → a generalised QSVT for complex-valued, non-Hermitian operators | GQSP throughout (no parity constraint); complex-valued equations not treated | the cost analysis showed the binding constraint is the Hamiltonian's norm and gap, which had to be solved first |
| nonlinear PDEs (Burgers, NLS, Ginzburg–Landau) | Burgers and 2-D Navier–Stokes by Carleman; NLS and CGL not treated | the doubled space cannot prepare; the Carleman lift needs dissipation (NLS is not dissipative) |
| data-informed Hamiltonians | not pursued | scope; future work |
| (not proposed) | the exact reproduction; the structured encoding; the descriptor reformulation; the verification framework | emerged from auditing the published method |

### 13.5 Formal requirements from the guidelines

12 pt; 1.5–2 cm margins; body 40–60 pages excluding contents, proposal and appendices; one-page
Summary of Student Achievement in the first person; the proposal as an appendix with deviations
noted; the supervisor's electronic signature; the signed declaration; help received acknowledged.
The seminar (25 minutes plus questions) is outside the document; F0 or F1, F9 and T7 carry it.

---

## 14. Pre-submission checklist

### 14.1 Content

1. Every §1.3 contribution has a verdict in §10.1 and evidence in Ch. 8.
2. Every Abstract number has a `\res` key and a Ch. 8 location.
3. Every claim ID cited in prose is ✅ in `18_claims.md` at `results-v1` (§9).
4. `grep` finds none of: "collocation" naming the paper's regime; "O(1) ancilla"; "+ 6" ancilla; "Θ̃(N²) floor"; "not
   verified end to end"; "corrected" outside §8.1 and Appendix K; "warm start"; "K^2 terms";
   "Pillar"; "rung"; QITE as the comparison's filter; "prepared" beside the doubled space; the
   readout protocol "reproduced" as the method's readout; a typed `pihm` number.
5. Ultraspherical and first-order least squares credited in §2.3 and §5.1–5.2; Paine 2026 cited.
6. The vocabulary of plan §3.4 holds throughout; every chapter opens with its question (plan §3.5).
7. The tier marked on every quantitative figure and table; every as-built comparison has its
   ideal-bound twin.
8. The research proposal in Appendix M, with deviations.

### 14.2 Style and presentation (/10: "flawless")

1. `\nocite{*}` removed; zero `\todo`, `\prov`, `\placeholderfigure`, `REVISE` or `CITE-NEEDED`
   (`grep -rn` over `1_header 2_body 3_footer`); bibliography `note` fields suppressed; `ref.bib`
   audited (T-29); `export_numbers.py --final` succeeds and the final build has no `pihm` errors.
2. Compile clean: no warnings, no overfull `\hbox` in the body.
3. Every float referenced by `\Cref`; figure captions below, table captions above; every caption
   stands alone.
4. Acronyms defined at first use; the `glossaries` entries complete (GQSP, QSP, QSVT, QITE, LCU,
   NLFT, IR, QFT, DCT, DNS, IVP, BVP, SVD, PIHM, FOSLS).
5. The AU spelling sweep; "Wang" spelt correctly; the declaration signed; the supervisor's
   endorsement present.
6. Body 40–60 pages (target 55–58), 12 pt, 1.5–2 cm margins.
7. The whole thesis read aloud once.

### 14.3 Rubric traceability (Modelling)

| criterion | marks | earned in | done |
|---|---|---|---|
| Intro & Lit: history and state of the art | /20 | Ch. 2 (§2.2 history), Ch. 3 | ☐ |
| — critical assessment (HD gate) | | §2.2(e) T1, **§3.6** | ☐ |
| — connection to the project | | §1.2, §3.6's three questions → Chs 4–6 | ☐ |
| Model formulation | /30 | Chs 4–7 | ☐ |
| — software tools | | §7.9, App L | ☐ |
| — model configuration diagram | | F1 (§7.1) | ☐ |
| — input options (boundary conditions etc.) | | §7.2 T2, T3; App J | ☐ |
| — reproducible ("create equivalent models") | | Chs 4–7 + App B–I | ☐ |
| — design of the numerical experiment | | §7.8 (fairness, conventions), §7.6 | ☐ |
| Results & Discussion | /30 | Chs 8–9 | ☐ |
| — self-contained results | | Ch. 8 + App J–K | ☐ |
| — significance for the field | | §9.1–9.5 | ☐ |
| — negative results analysed | | §8.4, §8.5, §8.7, §9.6 | ☐ |
| Conclusions & further investigation | /10 | Ch. 10 | ☐ |
| Style & presentation | /10 | throughout | ☐ |

---

*Companion documents: `CLAUDE.md` (the working agreement and Standing Facts v3),
`thesis_guides/STRUCTURE_AND_RUBRIC.md` (the rubric and exemplar reference),
`thesis_guides/STYLE_GUIDE.md` (register), `0_results/README.md` (quoting numbers),
`Code/pihm/docs/02_methods.md` (the method as built), `Code/Planning.md` (what was built and why).*
