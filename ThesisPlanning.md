# ThesisPlanning.md: the thesis structure, built on `pihm` as built

## Turning the `pihm` rebuild into a submittable (and publishable) Master's thesis

*Version 2.1, 2026-10-08. Version 1.1 (adopted 2026-09-25) fixed the contributions, the Modelling
rubric, the notation and a ten-chapter scaffold, and wave W0 built that scaffold. Version 2.0
(2026-10-01) recalibrated the plan against `pihm` as built, the School's marking guide and rubric,
the two exemplar theses and the literature (decisions T-20 to T-29, §1.4). Version 2.1 rebuilds
Chapter 4 as the passage from the published method to the standard form, and adds a chapter on
coupled systems and complex-valued fields, so the thesis has **eleven chapters** (decisions T-30 to
T-35, §1.5). What changed, and why, is §0.2. The `.tex` scaffold follows version 2.0's ten-chapter
order: migrating it is wave W0c (§4.3, §11).*

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
costs. This thesis answers both, in seven steps.

1. **Audit, and the passage to the standard form.** The method is rebuilt exactly and its claims
   are checked, mathematically in Chapter 4 and numerically in §9.1. The printed η_e of all eleven
   ODE panels agree to within one unit of the last printed digit. The PDE and nonlinear panels do
   not reproduce, and the printed choices (rounded constraint points, Maclaurin sources, invariants
   read off the known solution) distort the solutions at the printed resolution. Removing each
   defect, with its reason, turns the faithful rebuild into the *standard form*: the paper's regime,
   answer-independent, well posed and spectrally convergent. The paper's circuits are rebuilt and
   their claims tested.
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
6. **Beyond one real field.** The paper treats one real scalar field, and its Discussion sets a
   complex-valued state aside as making the ground state "difficult to find". Several coupled
   fields share one state, a block each, in both forms (the descriptor's mass form); vector data
   enter as ratio rows; the coupling is a sum of matchings on a circuit. A complex R still gives a
   Hermitian H = R†R, so the filter never meets a non-Hermitian operator: complex-valued linear
   equations are carried by realification as coupled real systems (R7 is exactly z′ = −iπz), and
   one native complex encoding, the tensor layout's coupling, is built and verified but not used for
   preparation.
7. **Nonlinearity.** The paper's doubled space encodes exactly but projects: its kernel is
   exponentially degenerate. The Carleman lift prepares, in both forms. On Burgers and Navier–Stokes
   its convergence follows a/ν, not the worst-case ratio ρ, and past the boundary the kernel stays unique and trusted
   while the lift diverges. The descriptor's time axis lowers the degree in every Navier–Stokes
   pair, and the thesis culminates in 2-D incompressible Navier–Stokes: the Taylor–Green vortex and
   a vortex pair on 12–80 modes, and a tensor-layout coupling of 2K − 1 terms to 316 modes.

Neither form is poly-log, every result is a classical computation, and nothing ran on hardware.

### 0.2 What changed in version 2.1, and why

| topic | v2.0 | v2.1 | source |
|---|---|---|---|
| chapter count | ten | **eleven**: a new Ch. 6, Coupled Systems and Complex-Valued Fields; nonlinearity becomes Ch. 7, the pipeline Ch. 8, the Numerical Study Ch. 9, the Discussion Ch. 10, the Conclusions Ch. 11. Labels (`sec:pipeline`, `sec:results`, …) do not change | T-31 |
| Chapter 4 | the published encoding, the structured encoding, the Hamiltonian wall (4 pp) | **three passes** (6 pp): the faithful rebuild and the paper's claims checked mathematically (§4.1–4.2); the passage from the faithful rebuild to the standard form, each change argued by the defect it removes (§4.3, Table T10); then the structured encoding and the Hamiltonian wall (§4.4–4.5) | T-30 |
| where the audit lives | Ch. 3 names, §8.1 measures | Ch. 3 **names** each weakness; Ch. 4 **derives** it; §9.1 **shows the numbers**. Nothing is stated three times | T-30 |
| deviations from Wu et al. | a list in the pipeline chapter's filter section | **Table T10** in §4.3, every deviation (residual-level and pipeline-level) with the section that argues it; the pipeline chapter points to it | T-34 |
| "as printed" | the reproduction only (§8.1, App. K) | also Ch. 4's audit and passage (§4.1–4.3); "corrected" stays banned everywhere outside App. K's verbatim record | T-33 |
| coupled systems | scattered over §5.3, §5.4, §6.3, §6.4, §7.5 | **owned by Ch. 6** (§6.1–6.4): several fields on one state, ratio rows, the mass form for systems, the coupling as matchings; the descriptor chapter keeps the mass form's definition for z′ = 𝔸z and its kernel equivalence (one theorem covers both layouts) | T-31 |
| complex-valued equations | future work only (§13.4) | **§6.5**: H = R†R Hermitian for complex R; realification is the route run (R7 = z′ = −iπz realified; real Fourier bases for R9–R10); the tensor layout's coupling is the one native complex encoding, verified, never prepared; native complex preparation is future work | T-32 |
| S4 | nonlinearity: preparation versus projection | **beyond a single real field**: systems, complex fields by realification, and nonlinearity by lift | T-31, T-32 |
| page budget | 56 | **58** (cap 60): Ch. 2 7.5 → 7, Ch. 4 4 → 6, Ch. 5 9.5 → 9, new Ch. 6 2.75, nonlinearity 4 → 3.25, pipeline 6 → 5.5, Numerical Study 10.5 → 10 | §4.1 |
| sources | `docs/FILTERS.md`, `EXTENSIONS.md`, `NAVIER_STOKES.md`, `DECISIONS.md` | renamed `15_filters.md`, `16_extensions.md`, `17_navier_stokes.md`, `20_decisions.md`/`21_decision_log.md`; the mathematical companion (`docs/companion/`) and the results guide (`docs/06_results_guide/`) added | §2, §10.1 |

### 0.2.1 What changed in version 2.0 (2026-10-01; chapter numbers as of v2.0)

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
| 2 | Background and Literature Review | 7 | Intro & Lit /20 | – | now (W1) |
| 3 | The Physics-Informed Effective Hamiltonian Method | 4 | Intro & Lit /20 (the HD gate) | poses Q(i)–(iii) | drafted |
| 4 | The Standard Form: From the Published Method to an Exact Baseline | 6 | Model Formulation /30 | Q(i); S1 (formulation half), S2 | now (W1) |
| 5 | The Descriptor Reformulation | 9 | Model Formulation /30 (the core) | Q(ii); C | now (W1) |
| 6 | Coupled Systems and Complex-Valued Fields | 2.75 | Model Formulation /30 | serves Q(iii); S4 | now (W1) |
| 7 | Polynomial Nonlinearity | 3.25 | Model Formulation /30 | Q(iii); S4 | now (W1) |
| 8 | Preparing and Verifying the Ground State | 5.5 | Model Formulation /30 (configuration, inputs, software, experiment design) | S3 | now (W1) |
| 9 | Numerical Study | 10 | Results & Discussion /30 | evidence for all | after P8's copy-back (W2) |
| 10 | Discussion | 4.5 | Results & Discussion /30 | – | W3 |
| 11 | Conclusions and Future Work | 2.5 | Conclusions /10 | – | last (W4) |
| | **total body** | **58** | | | |

The hard cap is 60 pages and the guidelines penalise overrun; aim for 55–58. Version 2.1 sits at
the top of that range, so the trim order of §4.1 is live, not contingent. Appendices A–M are
outside the count (§6).

### 0.4 Status board (update as you go)

Columns: **S** = scaffolded in the v2.1 order, **D** = drafted, **N** = numbers current from P8,
**R** = reviewed (Review Mode, `CLAUDE.md`), **F** = final.

| chapter / item | S | D | N | R | F | notes |
|---|---|---|---|---|---|---|
| Front matter (title, declaration, achievement, abstract) | ☑ | ☐ | ☐ | ☐ | ☐ | §13 |
| 1 Introduction | ☑ | ☐ | ☐ | ☐ | ☐ | LAND needs the v2.0 scope (readout classical) and v2.1's outline (eleven chapters) |
| 2 Background and Literature Review | ☑ | ☐ | n/a | ☐ | ☐ | §2.1 drafted; history, lineage and FOSLS to add (§5.2). Incomplete: heading "Readout and Amplitude Amplification" differs from §4.2's "Readout" |
| 3 PIHM (prior art), `3_pihm.tex` | ☑ | ◐ | ☐ | ☐ | ☐ | drafted 2026-10-07; W0c retargets its pointers to Ch. 4 (§4.2, §4.3) and adds one scope clause (one real scalar field). Incomplete: headings "The Chebyshev Latent Space Model" and "Residual Hamiltonian Construction" differ from §4.2's, and §4.2's "Overview" has no heading |
| 4 Standard form, `4_standard.tex` | ☑ | ◐ | ☐ | ☐ | ☐ | W0c: restructure into §4.1–4.5 (plan §5.4, T-35); the 2026-10-07 draft becomes §4.2.2, §4.4 and §4.5. Incomplete: tab:deviations (T10) cells and the Ch. 6 pointers are empty `\todo`s (`4_standard.tex:258–277`) |
| 5 Descriptor, `5_descriptor.tex` | ☑ | ☐ | ☐ | ☐ | ☐ | W0c: move the systems material out of §5.4 and §5.7 to Ch. 6 |
| 6 Systems and complex fields, `6_systems.tex` | ☑ | ☐ | ☐ | ☐ | ☐ | W0c: new file and scaffold (plan §5.6); six subsections and labels as §4.2; 2 REVISE open |
| 7 Nonlinearity, `7_nonlinear.tex` (was `6_nonlinear.tex`) | ☑ | ☐ | ☐ | ☐ | ☐ | W0c: rename; the time axis and matchings move to Ch. 6. Incomplete: proposition title "The nodal fold is optimal" (`7_nonlinear.tex:141`) must read "tight" |
| 8 Pipeline, `8_pipeline.tex` (was `7_pipeline.tex`) | ☑ | ☐ | ☐ | ☐ | ☐ | W0c: rename; the deviations list becomes a pointer to T10 |
| 9 Numerical Study, `9_results.tex` (was `8_results.tex`) | ☑ | ☐ | ☐ | ☐ | ☐ | W0c: rename; §9.5 becomes "Systems and Nonlinear Problems". Incomplete: Burgers caption states "diverging past a/ν ≈ 5" (`9_results.tex:255`) |
| 10 Discussion, `10_discussion.tex` (was `9_discussion.tex`) | ☑ | ☐ | ☐ | ☐ | ☐ | W0c: rename; T9 gains two rows |
| 11 Conclusions, `11_conclusions.tex` (was `10_conclusions.tex`) | ☑ | ☐ | ☐ | ☐ | ☐ | W0c: rename; future-work item 5 narrowed |
| Appendices A–M | ☑ | ☐ | ☐ | ☐ | ☐ | B drafted, C and D partly; C, G and H to extend (§6) |
| `ref.bib` audit (T-29) | – | ☐ | – | – | ☐ | before W1 drafting |
| Verification Mode pass | | | | ☐ | | §14 |

---

## 1. Decisions

### 1.1 Decided at the start (2026-09-25)

| # | question | decision | consequence |
|---|---|---|---|
| T-01 | contribution framing | **the descriptor as the headline, plus numbered supporting contributions** | plan §3.1 |
| T-02 | rubric project type | **Modelling**: Model Formulation /30 + Results & Discussion /30 | Chapters 4–8 carry /30 and 9–10 carry /30 (v2.1 numbering). Software, the model configuration and its input options are named requirements (plan §5.8) |
| T-03 | schedule | **no dates**; the writing is ordered by dependency only | §11 |
| T-04 | publication | **thesis first**; paper-shaped material is marked only where it falls out | plan §3.6 |

### 1.2 Decided 2026-09-25 (your acceptance of every recommendation), as amended

| # | question | decision | status |
|---|---|---|---|
| T-05 | chapter structure | ten chapters, with a shared-pipeline chapter and a standard-form chapter ahead of the descriptor | **order superseded by T-20; count superseded by T-31** (eleven chapters) |
| T-06 | operator notation | **blackboard bold**, matching the paper and `pihm`: 𝔾, B̃ as $\tilde{\mathbb B}$, D̃, 𝕄, 𝕟₁ | in force |
| T-07 | regime subscripts | **H_std, A_std, H_desc, A_desc**; bare H, A or R only in regime-independent statements (Ch. 8) | in force; the bare-symbol chapter is now Ch. 8 (T-31). Ch. 6's system rows carry the subscripts too |
| T-08 | imaginary-time symbol | **β** for QITE's imaginary time; τ(x) stays the paper's feature state | in force; β now appears only with the QITE filter (T-23) |
| T-09 | Carleman ratio symbol | **ρ**; R stays the stacked residual | in force |
| T-10 | benchmark labels and project vocabulary | **R1–R10**, called *benchmark problems*; never "rung", "pillar", "gate G3" or "tier T2" in prose; *operator verification*, *state-preparation verification*, *circuit simulation / exact emulation / resource estimate* with (T1/T2/T3) once | in force; the variant vocabulary is amended by T-27 |
| T-11 | the notation table | stays in the front matter (`1_header/6_notation.tex`) | in force |
| T-12 | readout's status | the paper's protocol, reproduced with a correction | **superseded by T-24** |
| T-13 | Chapter 3's register | **prior art, judged**; our measurements of the paper live in Chs 4 and 9, never in Ch. 3's descriptive sections | in force; Ch. 4 derives, §9.1 measures (T-30) |
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
| T-20 | chapter order | *(v2.0 numbering in this row; T-31 inserts a new Ch. 6, so 6–10 become 7–11.)* **Story first.** After the paper's critical assessment (Ch. 3) come the three answers in order: the standard form, encoded exactly (Ch. 4, Q(i)); the descriptor (Ch. 5, Q(ii)); nonlinearity (Ch. 6, Q(iii)). The shared pipeline and the design of the numerical experiment follow as Ch. 7, immediately before the evidence (Ch. 8). The degree formula for filtering an edge ground state moves into the background (§2.6), so Chs 4–6 can argue costs. Ch. 8 is regrouped into one section per question or contribution | In v1.1 a reader crossed six pages of machinery (walk, filter, tiers, software) before meeting the thesis's tension, the Hamiltonian wall. Placed before Ch. 8, the same material reads as the method of a numerical study, which is where the Modelling rubric's "design of numerical experiment" belongs. Ch. 8 by stage read as a catalogue; by question it reads as evidence. The exemplars support either layout (Snow pairs method and results; Green groups them); the deciding factor is that the story leads |
| T-21 | the descriptor's challenge | **Its own body subsection** (§5.5, the gap of a carried derivative) before the cure (§5.6, block rescaling), and its own results section (§9.4) | It is the most interesting science in the project: a genuine failure of the naive reformulation, diagnosed, cured a priori, and bounded. v1.1 gave it 0.75 pages under the cure's name. Owning it, with its limits, is what the rubric's top band calls insight |
| T-22 | first-order equations and systems | *(Systems themselves move to Ch. 6, T-31; the layout stays the descriptor's.)* **The descriptor has two layouts**, named in the body: the chain (order ≥ 2) and the mass form (first-order equations and systems: I⊗D̃ − 𝔸⊗B̃, the standard rows times I⊗B̃). The kernel-equivalence theorem covers both | Decision 39 made the mass form the descriptor of R1 and R7–R10; v1.1's descriptor chapter did not mention it, and Ch. 6's space-time form used it unexplained |
| T-23 | the preparation filter | **The minimax edge filter** prepares every comparison and extension; QITE is the paper's filter, run in the reproduction (§9.1) and in the filter study (§9.2). β, the Bessel coefficients and Σ\|q_k\| = 1 stay, as the reproduced filter's | Decisions 35 and 50: P8 runs the R1–R5 comparison under minimax in both forms |
| T-24 | readout | **Classical.** The field is decoded from the prepared state; η from the regular datum. The paper's interferometric protocol, built and verified at small n with our correction for p_G < 1, is one paragraph in §8.7, its identity in Appendix F, and future work. Supersedes T-12 | Decision 27 |
| T-25 | fairness of the comparison | **Every cost comparison is quoted twice**: as built (each form's own circuits) and at the ideal-encoding bound α = ‖R‖ (decision 43), which has neither form's encoding in it. Where the order reverses, the reversal is a reported finding | The structured encoding is loose on R3 (C-02), so as-built comparisons there favour the descriptor for the wrong reason; the ideal bound shows the Hamiltonians alone |
| T-26 | prior art for the headline | **Credit two antecedents** wherever the contribution is claimed: the ultraspherical spectral method (Olver & Townsend 2013: banded differentiation, well conditioned after diagonal preconditioning) and first-order-system least squares (Cai, Lazarov, Manteuffel & McCormick 1994: least squares of an order-k operator squares its conditioning; a first-order reformulation avoids it). Cite the concurrent sibling of Wu et al., Paine 2026 (arXiv:2609.26330), in §2.2 and §3.6 | A numerical analyst will ask "isn't this FOSLS, or ultraspherical?" The honest answer, stated first, is that the classical ideas are known and the increment is their transfer to a block-encoded physics-informed Hamiltonian: the kernel equivalence, the flat LCU, the a priori rescaling and the measured consequences for ground-state preparation. Paine 2026 reports that the normalised gap depends on the representation, without scaling, circuits or a reformulation; it confirms the question and leaves the answer open |
| T-27 | variant vocabulary | **The problem is unnamed.** "R2a" is the problem; the paper's panel as printed is "R2a as printed" (or "paper-faithful"), and appears only in §9.1 and Appendix K, **amended by T-33** to admit Ch. 4's audit and passage (§4.1–4.3). Never write "corrected" | Decision 49 |
| T-28 | software in the body | **One short paragraph** (§8.9) names the package, its dependencies, its tests and the Setonix production; records, provenance and source digests live in Appendix L only | The Modelling rubric asks for "a description of any software tools used and/or created", not a manual; the code-map risk is concentrated here |
| T-29 | bibliography | **Audit `ref.bib` before drafting.** `wu2025pihm` lists "Wu, Yuan; Paine, Alex J.; Philip, Deep"; the paper is by Hsin-Yu Wu, Annie E. Paine, Evan Philip, Antonio A. Gentile and Oleksandr Kyriienko. The `note` fields print internal repository notes. Missing entries are listed in §5.2 | A misattributed source paper on page 1 costs the Style mark and credibility; every entry must be checked against its publisher, never guessed |

### 1.5 New in version 2.1 (adopted 2026-10-08)

| # | question | decision | why |
|---|---|---|---|
| T-30 | Chapter 4's job | **Three passes.** (1) The faithful rebuild and the paper's claims checked mathematically: the conventions and the classical solve (§4.1), the Hamiltonian and model claims (§4.2.1), the published circuits (§4.2.2; one audit subsection, T-35). (2) The passage from the faithful rebuild to the standard form, each change stated as the defect it removes and the property it gains, closed by a definition of the standard form and Table T10 (§4.3). (3) The structured encoding and the Hamiltonian wall, as in v2.0 (§4.4–4.5). The audit is split by kind: **Ch. 3 names** each weakness with a pointer, **Ch. 4 derives** it, **§9.1 shows the numbers**; no weakness is argued in two places | The author wants the chapter to rebuild and check the paper, then show how the faithful rebuild became the standard form used later. v2.0 left that passage implicit (it lived in §8.1's tables and Planning.md's variant list), so a marker met "the standard form" as an unexplained object. The three-way split keeps formulation (derivations) in the formulation chapter and evidence (records) in the results chapter, which is the Modelling rubric's division |
| T-31 | coupled systems | **A dedicated chapter, Ch. 6, "Coupled Systems and Complex-Valued Fields" (2.75 pp)**, between the descriptor and nonlinearity. It owns several fields on one state, ratio rows, the mass form *applied* to systems (its definition and kernel equivalence stay in §5.3, one theorem for both layouts), and the coupling on a circuit as a sum of matchings, and it ends by noting that a Carleman lift is such a system. It serves Q(iii) as its prerequisite and answers no new numbered question, so Ch. 3's three questions stand. Nonlinearity becomes Ch. 7, the pipeline Ch. 8, the Numerical Study Ch. 9, the Discussion Ch. 10, the Conclusions Ch. 11; labels do not change. Considered and rejected: the opening half of a combined "Systems and Nonlinearity" chapter (saves about 0.5 pp and the renumbering, but nonlinearity loses its own chapter) | The paper treats one real scalar field. `pihm` carries several (`assemble/systems.py`, `circuits/systems.py`, decisions 39, 42, 45; R7, and every Carleman lift), but v2.0 scattered that machinery over five sections and no section owned it. A Carleman lift is a linear system on its monomials, so stating systems once, before the lift, shortens Ch. 7 |
| T-32 | complex-valued equations | **Scope: realification, plus the one native complex encoding that was built; no new code.** §6.5 states: a complex R gives a Hermitian positive semi-definite H = R†R, so the filter never meets a non-Hermitian operator; the route run is realification, z = u + iv as two real fields, z′ = cz becoming [u; v]′ = [[Re c, −Im c], [Im c, Re c]][u; v] (one more field-register qubit), and R7 is exactly the realification of z′ = −iπz with z = πu + iv; R9 and R10 use real Fourier bases (sine; cos/sin with an isometric real embedding); the tensor layout's coupling is built on complex Fourier variables with complex LCU weights and verified (exact and IR), but never used for preparation, because the classical pipeline carries real data only; complex sources, data and coefficients are refused by `pihm`'s loaders, so native complex preparation is future work. Considered and rejected: adding native complex data to `pihm` before the freeze (new campaigns while P8 runs) | The paper's Discussion sets a complex-valued state aside: with a Fourier basis "the resulting total energy function is of a complicated form, rendering it difficult to find the ground state". The research proposal promised complex-valued and non-Hermitian equations. The honest answer is formulational (H stays Hermitian; realification costs one qubit) with narrow evidence (R7, the real Fourier bases, the tensor encoding). The legacy `DESolverLib`'s complex and coupled-field code exists but is never cited (Standing Facts) |
| T-33 | "as printed" in Ch. 4 | **Amend T-27**: "as printed" (or "paper-faithful") may appear in §4.1–4.3 as well as §9.1 and Appendix K. "Corrected" stays banned in prose; the problem is unnamed | The passage to the standard form cannot be written without naming what it passes from |
| T-34 | deviations from Wu et al. | **Table T10 in §4.3** lists every deviation, residual-level (argued in §4.3) and pipeline-level (stated with a pointer to Ch. 8: GQSP for mixed-parity QSVT, normalisation by α for ‖H‖_F, the minimax filter, a priori parameters, the classical readout, the SVD reference). The pipeline chapter's "Deviations from Wu et al." list is replaced by a pointer to T10 | One place for the whole passage from the paper to this thesis, which is what a marker looking for "what did the student change, and why" needs |
| T-35 | Chapter 4's audit (2026-10-08) | **Merge the two audit subsections.** The former §4.2 (the Hamiltonian and model claims) and §4.3 (the published circuits) become one subsection, §4.2 *Testing the Paper's Claims* (`sec:standard-audit`), with subsubsections §4.2.1 (`sec:standard-claims`) and §4.2.2 (`sec:standard-published`); the labels are kept, so every `\Cref` keeps its target. Later subsections renumber: the passage §4.3, the structured encoding §4.4, what remains §4.5 | Both halves test the paper's claims and differ only in the kind of evidence (algebra against circuits); the audit's opening paragraph already named the efficiency claim tested in the circuit half. One subsection makes pass 1 of T-30 read as rebuild then audit. "Validating" also presumed a verdict the subsection (refuted claims only) contradicts |
| S4 (amended) | contribution wording | **S4 widened** to "beyond a single real field": systems, complex fields by realification, nonlinearity by lift; no new S5 (§3.1) | The systems machinery is modest novelty on its own; it earns its place as the route to Carleman and Navier–Stokes |

---

## 2. How the planning documents relate

- **`CLAUDE.md`** (the working agreement) carries **Standing Facts v4** (2026-10-08): the facts a
  draft may not contradict. It is updated whenever this plan's facts change, and wins over the
  guides on facts.
- **`thesis_guides/STRUCTURE_AND_RUBRIC.md`** is the rubric and exemplar reference: the mark sheet,
  the guidelines' formal requirements, what the exemplars do, and the Style & Presentation sweep.
  Its pre-plan section tree, page budget and checklists were removed in v2.0 (they are in git
  history at `4b4e423`); this plan is the structure.
- **`thesis_guides/STYLE_GUIDE.md`** is the register: tone, exposition, empirical presentation and
  the traps. Its examples were updated to the current facts in v2.0.
- **`0_results/README.md`** is how to quote a number.
- **`Code/pihm/docs/02_methods.md`** is the method as built, the source for Chapter 8 and Appendix I.
- **`Code/pihm/docs/companion/`** is the mathematics as built, with derivations and proofs beside the
  code and tests that implement them, sectioned as Appendices B–I: the first source for every
  appendix proof and every body proposition (decision 51). Its files are cited in §5 by number
  (for example "companion 51" for `51_mass_form.md`).
- **`Code/pihm/docs/06_results_guide/`** is generated from the records and ordered by Chapter 9's
  sections (81 reproduction → 87 findings): the first stop for what a results section can claim.
- **Renamed reports.** v2.0's `FILTERS.md`, `EXTENSIONS.md`, `NAVIER_STOKES.md` and `DECISIONS.md` are
  `15_filters.md`, `16_extensions.md`, `17_navier_stokes.md` and `20_decisions.md` (the user's
  decisions) / `21_decision_log.md` (the implementation's), all under `Code/pihm/docs/`.

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
- **Chapter 7 (nonlinearity; `6_nonlinear.tex` until W0c).** A clause says "descriptor Hamiltonian" where it means the doubled-space one.
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

- **Gap flatness is measured, not proved (Chapter 4, §4.5; Chapter 9).** `eq:standard-wall`'s
  Θ̃(N^{2k}) assumes Δ = Θ(1) for the standard form. Measured so far on R2a (n = 6–8, 7.04) and R2b
  only. **Extend the check** to the other constant-coefficient one-axis panels (R1, R2c, R4*) and
  to other second-order coefficients, then widen or narrow the claim. Until then the text says
  "measured on R2a and R2b".
- **Appendix D, measured ε_G(n), qubits and gates.** `tab:app-epsilon-G` is all `\prov`; the
  published build's measured counts and error are not exported. Needs a derived key, then quote one
  measured ε_G in §4.2.2 beside the bound (REVISE in `4_standard.tex`).
- **Factorisation error 2.3e-13 (§4.4)** is the planning probe's figure, typed as `\prov`; replace
  with a derived key (max error of 𝔾 = R₀(2U_odd)Λ, n ≤ 10) or delete the number.
- **Appendix E must carry** the Bessel-kernel limit α_𝔾/‖𝔾‖₂ → 2j_{−3/4,1}, the theorem
  ‖𝔾^k‖₂/N^{2k} → ‖K^k‖ > 0 (so ‖H_std‖ = Θ(N^{4k})) and the published ratio ~ jN³
  (companion 31, 33, 57). Written when the appendices are.
- **`9_results.tex` (was `8_results.tex`) T7 `\prov` cells disagree with the records** (published degree at n = 8:
  8.2e23 against 9.1e22; descriptor gap 0.454 against 2.87). Resolved when T7 moves to `\res`.
- **STYLE_GUIDE §7 row on the relative gap** says "below double precision at n = 7"; the records give
  Δ/‖H‖ = 5.9e-15 at n = 7 and 2.3e-17 at n = 8, so it is below 2⁻⁵² only from n = 8.

Opened by v2.1 (2026-10-08): Chapter 3's "ours / to test" TODOs, routed (each becomes a pointer from
Ch. 3 and an item of Ch. 4's LAND at W0c; delete the Ch. 3 TODO once the pointer is in):

- **η > 0** (`3_pihm.tex`, the model): √η = y_s/⟨τ(x_s)|ψ_g⟩ is negative when the ground state's
  sign opposes the datum's → §4.2, as a global-phase convention (the decoded field carries the sign).
- **"positive-definite with distinct eigenvalues"** (Definition, `def:pihm-hamiltonian`) → §4.2 (A-09:
  positive semi-definite; exact kernels for polynomial solutions; the Laplace invariant set's
  near-degenerate bottom).
- **The k − 1 invariant count** and **a polynomial solution of degree below N is an exact kernel**:
  ours → §4.2, stated as a lemma with its scope (ordinary equations).
- **The stacked residual R and the least-squares reading**: ours → §4.3 (the standard form's
  definition); Ch. 3 keeps the paper's Gram-sum form and one pointer.
- **The density of 𝔾, its Θ(N²) entries, ‖𝔾‖₂ = Θ(N²) and the nodal similarity**: ours → Appendix B
  (`app:cheb-G-norm`), cited from Ch. 3 and §4.4.
- **Any number of axes** (`app:pihm-multi-axis`, currently unreferenced) → §4.3, item "axes".
- **Constant coefficients under the lift (a_j 𝕄₁)** against the descriptor's square Galerkin form →
  §4.3 (the standard form keeps the paper's lift) and Appendix G.

Opened by v2.1 from `pihm`'s Journal (E087, E114, E115: errors it found in this plan; the
first three are corrected in v2.1, the rest are open):

- *Corrected:* the nodal fold's α = 2 is within 1.21 of ‖𝕟₁‖₂ = 1.58–1.665, tight and **not
  optimal** (§5.7 item 4, B-12); the lift **converges at a/ν = 3 and diverges at 10**, and "a/ν ≈ 5"
  is where a/(5ν) reaches one, an extrapolation (§5.9 item 5); 𝔾's encoding alone takes **n + 4**
  ancilla, and the stacked rows add flags and selectors (R1's reflection n + 5) (S2, §5.4).
- *Open:* **C-08's scope.** Every minimax T1 record meets T1 = T2 ≤ 1e-10; 43 of the 46 QITE T1 keys
  (85 of 91 candidates) do, the misses reported with their degree (decision 30). The Standing Fact
  ("wherever both run") must be scoped after P8: either P8's rerun closes the misses, or the fact
  reads "on every minimax record; the reproduction's QITE misses reported".
- *Open:* `0_results/README.md` says `trusted` needs a gap ratio of at least 100 (pihm: 20), lists
  `degree` and `tau` as the QITE filter's (minimax runs have `degree` and no `tau`), and has no
  `growth` row. Fix the README before W2.
- *Open:* the ρ sentence of §7.3 cites Liu et al., *PNAS* 118, e2026805118 (2021); check it against
  the publisher and add it to `ref.bib` (T-29).

Opened by v2.1: the Chapter 6 evidence keys. R7's mass-form gap against the chain's (2.1 at n ≥ 4,
`16_extensions.md` §1.1) and the matchings' term count and α against Pauli words (decision 42) are
not exported as `\res` keys; add derived keys before §6.3–6.4 quote them, or quote them as
`\prov` with a REVISE.

---

## 3. Contributions, questions, spine and vocabulary

### 3.1 The contributions (numbered in §1.3; each gets a verdict in §11.1)

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
> least squares. *Evidence:* Ch. 5, §9.3–9.4; claims C-05, C-06, B-01, B-02, B-04–B-06, B-21.

**Supporting.**

> **S1. A verified reproduction and audit of Wu et al.** Rebuilt exactly, printed constraint points
> and Maclaurin sources included: the printed η_e agree with the exact solution's ‖b‖² to within one
> unit of the last printed digit on all 11 ODE panels; the PDE and nonlinear panels do not
> reproduce, each triaged by discriminating runs; the printed choices distort the solutions at the
> printed n; the paper's circuits (Figs 2, 8, 9) are built and their claims tested, and its
> time rule falls short of ε. Removing each printed defect, with its reason, turns the rebuild into
> the standard form (Table T10). *Evidence:* §4.1–4.3 (derivations), §9.1 (numbers), Appendix K;
> claims A-01–A-13, C-07.

> **S2. An exact structured encoding of the standard form.** 𝔾 = R₀(2U_odd)Λ gives α_G = N(N−1)
> ≤ 2.12‖𝔾‖₂ with O(n²) gates and n + 4 ancilla for 𝔾 alone, against an α/‖𝔾‖₂ growing like N³ for the
> published normalisation. For constant coefficients it bounds α_H/‖H_std‖, isolating the standard
> form's cost in its Hamiltonian; for a lifted variable coefficient it is loose. *Evidence:* §4.4–4.5,
> §9.3; claims C-01, C-02.

> **S3. A regime-independent, verified preparation pipeline.** A stacked-residual reflection V with
> Π V Π = 2H/α_R² − I and a controlled V that needs only controlled reflections; GQSP with the
> minimax edge filter, chosen over imaginary time by a study in both forms; a priori parameters and
> answer-independent initial states; operator verification in three modes and state-preparation
> verification in three tiers, the exact emulation proven, and measured, equal to the circuit
> (≤ 1e-10); a certified-estimate iterative reference to half a million columns. *Evidence:* Ch. 8,
> §9.2; claims C-03, C-04, C-08, B-13, B-16, B-17, B-24.

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
> the field count; native complex preparation is not built. *Evidence:* Ch. 6, Ch. 7, §9.5–9.6;
> claims A-10, B-12, B-18, B-19, B-22, C-09, C-10, and the new rows of §9 (plan).

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
| (i) *Is the method's cost its encoder's or its Hamiltonian's?* | Ch. 4 | §9.3 |
| (ii) *Can the residual be reformulated so that its Hamiltonian is banded and well conditioned, without changing its solution, and what does that cost?* | Ch. 5 | §9.3–9.4 |
| (prerequisite to (iii), and the paper's scope: several fields, complex-valued fields) | Ch. 6 | §9.5 |
| (iii) *Can nonlinear equations be prepared rather than projected?* | Ch. 7 | §9.5–9.6 |
| (how the answers are tested) | Ch. 8 | §9.1–9.2 |

Each formulation chapter opens by restating its question in one sentence and closes by naming the
results section that tests it. Ch. 6 answers no numbered question (T-31): it opens with the scope
the paper leaves (one real scalar field; its Discussion's remark on complex-valued states) and closes
by handing a coupled linear system to Ch. 7's lift. Ch. 3's three questions are unchanged.

### 3.3 The spine sentence

> *Carrying the intermediate derivatives instead of eliminating them turns the physics-informed
> residual from dense to banded with its kernel unchanged, so the Hamiltonian's norm falls from
> Θ(N⁸) to Θ(N²) for a second-order equation; the price is a block register and a gap the
> derivative blocks erode, which an a priori rescaling restores on one axis at no gate cost.*

Place it, lightly reworded each time, in: the Abstract; the end of §1.3; the close of §3.6 (as the
question it answers); §5.1; §5.10; §9.7; §11.1.

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
| R2a; R2a as printed (paper-faithful) | "corrected R2a", "wrong/fixed version" | T-27, T-33: "as printed" in §4.1–4.3, §9.1 and App. K only |
| the passage to the standard form; the standard form removes … | "we fixed", "corrections", "bug" | §4.3: each change named by the defect it removes and the property it gains |
| several fields; a (coupled) system; the field register | "vector-valued solver", "multi-field method" | Ch. 6 |
| ratio row | "vector boundary condition" | pins the direction of vector data, leaves its scale free |
| sum of matchings | "sparse oracle" | 𝔸 split by edge colouring (Ch. 6) |
| realification; complex-valued field | "complex solver", "handles complex equations" (unscoped) | T-32: native complex preparation is not built |
| benchmark problem R1–R10 | rung, case N | T-10 |
| a priori parameters | "tuned", "chosen" | never against the answer |

### 3.5 A scientific argument, not a code map

The rubric scores a model a reader could rebuild, not a tour of the software. Rules:

1. **Every chapter opens with its question and closes with its answer.** No chapter opens with "this
   chapter describes the module…".
2. **State constructions as mathematics.** `assemble`, `stacked_reflection`, `t2` and their
   relatives appear in the body only in §8.9 and the figure-script comments; elsewhere they are the
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
7. **Chapter 4's passage is an argument, not a changelog.** Each row of Table T10 names a
   mathematical defect of the printed method (answer-dependent data, an error floor, an ill-posed
   problem, an approximate encoding) and the property its replacement gains; no row says when or why
   *we* changed it, and none cites an issue or decision.

### 3.6 Paper-shaped material (light note, T-04)

Chs 4–5, §9.3–9.4 and §10.1–10.2 form a self-contained article ("a banded reformulation of
physics-informed effective Hamiltonians"), with the reproduction as its baseline section and the
Carleman results as a second paper. Nothing in the plan depends on this.

---

## 4. Page budget and LaTeX tree

### 4.1 Page budget (Modelling scale)

| chapter | pp | criterion |
|---|---|---|
| 1 Introduction | 3.5 | Intro & Lit /20 |
| 2 Background and Literature Review | 7 | Intro & Lit /20 |
| 3 The PIHM method (prior art, judged) | 4 | Intro & Lit /20 (HD gate: critical assessment) |
| 4 The standard form: from the published method to an exact baseline | 6 | Model Formulation /30 |
| 5 The descriptor reformulation | 9 | Model Formulation /30 (core) |
| 6 Coupled systems and complex-valued fields | 2.75 | Model Formulation /30 |
| 7 Polynomial nonlinearity | 3.25 | Model Formulation /30 |
| 8 Preparing and verifying the ground state | 5.5 | Model Formulation /30 |
| 9 Numerical Study | 10 | Results & Discussion /30 |
| 10 Discussion | 4.5 | Results & Discussion /30 |
| 11 Conclusions and Future Work | 2.5 | Conclusions /10 |
| **total** | **58** | |

**Why this split.** The Modelling scale gives Results & Discussion 30 marks, so Chapters 9–10 take
14.5 pages. Formulation (Chapters 4–8, 26.5 pages) must let a reader "create equivalent models", so
configuration, inputs and software have body space in Chapter 8, with the detail in Appendices F,
G, I, J and L. v2.1 moved pages into formulation: Chapter 4 now carries the audit's derivations
(from §9.1) and the deviations list (from Chapter 8), and Chapter 6 gathers material that was spread
over Chapters 5, 7 and 8. Two pages of slack remain under the cap; Chapter 3's draft already runs
long.

**Trim order if over budget:** §2.1 first; then §9.4's third representative problem (to Appendix
J); then §8.9 and §8.8 to their minimum; then §4.2.2 to its verdict table (the rebuild's prose to
Appendix D); then §6.4 to one paragraph (the matchings' detail to Appendix H); then §3.4. Chapter 5
is cut last. The page budget is enforced in Review Mode only (`CLAUDE.md`).

### 4.2 LaTeX section tree (v2.1; file names are the targets of W0c)

```latex
% 2_body/1_introduction.tex  (~3.5 pp)
\section{Introduction}                                        % sec:intro
  \subsection{Differential Equations as a Target for Quantum Computation}
  \subsection{Physics-Informed Hamiltonians and Where Their Cost Lies}   % F0 (optional)
  \subsection{Contributions and Scope}
  \subsection{Outline}

% 2_body/2_literature.tex  (~7 pp)
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

% 2_body/4_standard.tex  (~6 pp)
\section{The Standard Form: From the Published Method to an Exact Baseline}   % sec:standard
  \subsection{The Method Rebuilt}                              % sec:standard-rebuilt (new); eq:eta-e moves here
  \subsection{Testing the Paper's Claims}                      % sec:standard-audit (T-35)
      \subsubsection{The Hamiltonian, Its Filter and Its Readout}  % sec:standard-claims (new)
      \subsubsection{The Paper's Block Encodings}              % sec:standard-published (kept)
  \subsection{From the Faithful Rebuild to the Standard Form}  % sec:standard-passage (new); def:standard-form; T10
  \subsection{An Exact Structured Encoding}                    % sec:standard-factorisation (kept)
      \subsubsection{The Factorisation}                        % prop:G-factorisation
      \subsubsection{Circuits and Cost}                        % sec:standard-cost (kept); F3
  \subsection{What Remains: The Standard-Form Hamiltonian}     % sec:standard-hamiltonian (kept)

% 2_body/5_descriptor.tex  (~9 pp)  THE CORE
\section{The Descriptor Reformulation}                        % sec:descriptor
  \subsection{The Idea}                                        % F4 sparsity
  \subsection{The Banded Factorisation}
  \subsection{Two Layouts and Kernel Equivalence}              % chain | mass form; theorem
  \subsection{Constraints and Partial Differential Equations}  % sec:descriptor-constraints (kept); coupled fields -> Ch. 6
  \subsection{The Gap of a Carried Derivative}                 % the challenge (T-21)
  \subsection{Block Rescaling}                                 % the cure and its limits
  \subsection{The Block Encoding: One Flat Linear Combination} % F5, algorithm; matchings -> Ch. 6
  \subsection{Cost of the Descriptor Encoding}                 % proposition
  \subsection{Consequences for the Spectrum and the Filter}
  \subsection{Summary}

% 2_body/6_systems.tex  (~2.75 pp)   NEW (T-31)
\section{Coupled Systems and Complex-Valued Fields}          % sec:systems
  \subsection{Several Fields on One State}                     % sec:systems-fields; the time axis
  \subsection{Data for Several Fields: Ratio Rows}             % sec:systems-data
  \subsection{The Mass Form for Systems}                       % sec:systems-mass
  \subsection{The Coupling on a Circuit}                       % sec:systems-coupling; matchings
  \subsection{Complex-Valued Fields}                           % sec:systems-complex; T-32
  \subsection{From Systems to Lifts}                           % sec:systems-lifts; hand-off to Ch. 7

% 2_body/7_nonlinear.tex  (~3.25 pp)   [was 6_nonlinear.tex]
\section{Polynomial Nonlinearity}                             % sec:nonlinear
  \subsection{Two Treatments}
  \subsection{The Doubled Space: Exact Encoding, Degenerate Kernel}
  \subsection{The Carleman Lift in Space--Time}                % the time axis cited from sec:systems-fields
  \subsection{Products and Couplings on a Circuit}             % folds; tensor layout; matchings cited from sec:systems-coupling
  \subsection{Fourier--Galerkin Fluids: Burgers and Navier--Stokes}
  \subsection{Preparation Versus Projection}                   % T8

% 2_body/8_pipeline.tex  (~5.5 pp)   [was 7_pipeline.tex]
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

% 2_body/9_results.tex  (~10 pp)   [was 8_results.tex]
\section{Numerical Study}                                     % sec:results
  \subsection{Reproducing Wu et al.}                           % S1: T6, F6
  \subsection{The Pipeline Is Faithful}                        % S3: F7, F8
  \subsection{Where the Cost Lies}                             % Q(i),(ii): F9, T7, F10
  \subsection{The Descriptor's Gap and Its Rescaling}          % the challenge: F11, F12
  \subsection{Systems and Nonlinear Problems}                  % Ch. 6, Q(iii): F13
  \subsection{Case Study: Two-Dimensional Navier--Stokes}      % F14
  \subsection{Summary of Findings}                             % numbered, >= 2 negative

% 2_body/10_discussion.tex  (~4.5 pp)   [was 9_discussion.tex]
\section{Discussion}                                          % sec:discussion
  \subsection{Why the Descriptor Form Wins, and What It Costs}
  \subsection{End-to-End Complexity}
  \subsection{What the Reproduction Says About the Published Method}
  \subsection{Where the Construction Applies}                  % T9 applicability
  \subsection{Feasibility on Fault-Tolerant Hardware}
  \subsection{Limitations}

% 2_body/11_conclusions.tex  (~2.5 pp)   [was 10_conclusions.tex]
\section{Conclusions and Future Work}                         % sec:conclusions
  \subsection{Conclusions}
  \subsection{Future Work}
```

### 4.3 Scaffold conventions (as built) and the W0c migration

**Conventions (unchanged).** `main.tex` holds each chapter's `\section` and label and inputs the
body files; `3_footer/appendices.tex` does the same for `A_gates.tex` … `M_proposal.tex`. Every
subsection has a label. Comment tags: PURPOSE, CRITERION, SOURCES, WRITE WHEN, LAND, FIG, TAB,
OFFLOAD, CHECKLIST, TRAPS, REVISE, CITE-NEEDED. Macros in `1_header/0_packages.tex`: `\G`, `\Bt`,
`\Dt`, `\M`, `\nfold`, `\Brow`, `\Dzero`, `\Ucg`, `\Uodd`, `\Astd`, `\Adesc`, `\Hstd`, `\Hdesc`,
`\fhat{j}`, `\prov{…}`; numbers by `\res` (plan §10.2). Placeholders: `\placeholderfigure`; tables with
final columns; propositions with `% STATE:` and proofs in appendices.

**W0b (v2.0's migration) is done**: the files carry v2.0's names (`4_standard.tex` … `10_conclusions.tex`).

**The W0c migration (v2.1; not yet done).** Structural only: no prose is drafted or deleted, except
where a step moves existing prose verbatim.

1. **Rename** `6_nonlinear.tex` → `7_nonlinear.tex`, `7_pipeline.tex` → `8_pipeline.tex`,
   `8_results.tex` → `9_results.tex`, `9_discussion.tex` → `10_discussion.tex`, `10_conclusions.tex` →
   `11_conclusions.tex` (with `git mv`). **Create** `6_systems.tex`. In `main.tex`, add
   `\section{Coupled Systems and Complex-Valued Fields}\label{sec:systems}` with its `\input` between
   the descriptor and nonlinearity, retitle Chapter 4 to *The Standard Form: From the Published
   Method to an Exact Baseline*, and repoint the renamed inputs. Labels do not change, so every
   `\Cref` survives; "Chapter N" prose, header comments and the outline need renumbering.
2. **Restructure `4_standard.tex`** into the six subsections of plan §5.4. Keep the existing labels
   (`sec:standard-published`, `sec:standard-factorisation`, `sec:standard-cost`,
   `sec:standard-hamiltonian`); add `sec:standard-rebuilt`, `sec:standard-claims`,
   `sec:standard-passage`. The 2026-10-07 draft's prose moves verbatim into §4.2.2, §4.4 and §4.5 (numbering after T-35); the
   opening paragraph keeps its prose with a REVISE to widen its roadmap to the three passes. New
   subsections get LAND blocks only. Move `eq:eta-e`'s statement (not its numbers) from `8_results.tex`
   to §4.1, keeping the label; §9.1 keeps the table and cites it.
3. **Scaffold `6_systems.tex`** from plan §5.6: header block, six labelled subsections, LAND blocks,
   no prose. **Move, verbatim, into its LAND or as commented-out prose**: the coupled-fields clause of
   `5_descriptor.tex`'s `sec:descriptor-constraints`, the matchings paragraph of
   `sec:descriptor-block-encoding`, and the two space–time discretisations and ratio-row item of
   `7_nonlinear.tex`'s `sec:carleman`; leave a pointer (`\Cref{sec:systems-…}`) where each was.
4. **Header comments** of every renamed file and of Chapters 5, 7 and 8: rewrite PURPOSE, CRITERION,
   SOURCES and LAND to plan §5's v2.1 entries; replace old doc paths (`FILTERS.md` →
   `15_filters.md`, `EXTENSIONS.md` → `16_extensions.md`, `NAVIER_STOKES.md` → `17_navier_stokes.md`).
5. **Chapter 8** (`8_pipeline.tex`): in `sec:pipeline-filter`, replace the "Deviations from Wu et al."
   LAND item by a pointer to Table T10 (`tab:deviations`, §4.3). **Chapter 9**: retitle
   `sec:results-nonlinear` to *Systems and Nonlinear Problems* and add R7's LAND item (plan §5.9).
   **Chapter 10**: add T9's two new rows to the LAND. **Chapter 11**: narrow future-work item 5.
6. **Chapter 3 (pointers only; the prose is the author's):** retarget the pointers named in plan
   §5.3 to `sec:standard-claims` / `sec:standard-passage`, add the one scope clause of plan §5.3 as a
   `% REVISE:` for the author, and replace each "ours / to test" TODO by a REVISE naming its new home
   (plan §2.1, v2.1 list).
7. **Appendices:** add the LAND items of plan §6 to C (the multi-axis generalisation, the
   faithful-rebuild conventions) and H (systems, ratio rows, matchings, realification).
8. Add a `% REVISE:` beside each item of plan §2.1's v2.1 list; add `tab:deviations` (T10) as a
   table with final columns and `\prov`/placeholder cells.
9. Update `1_header/6_notation.tex` with plan §8.1's new rows and the acronym list if needed.
10. Compile into a scratch outdir; zero undefined references; report the page count per chapter.

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
     new readout protocol; the preparation of a complex-valued field by native complex encodings
     (realification only, T-32).
4. **§1.4 Outline (0.5 p).** One line per chapter naming its job: Ch. 3 as reviewed prior art; Ch. 4
   as the paper rebuilt, checked and turned into the standard form, and the answer to Q(i); Ch. 5 as
   the answer to Q(ii); Ch. 6 as the step from one real field to coupled and complex-valued ones; Ch.
   7 as the answer to Q(iii); Ch. 8 as how the answers are tested; Ch. 9 as the evidence.

**Marker checklist.** A non-specialist physicist can state the problem after two pages; a number on
or before page 2; every contribution numbered and falsifiable with its evidence; the scope explicit,
tiers and "no hardware" included; Wu et al. attributed at first mention; the outline matches the
headings verbatim.

**Traps.** Leading with the descriptor before the reader knows the baseline; claiming a speed-up;
listing S2 as a rival method; "the readout protocol was reproduced".

---

### 5.2 Chapter 2: Background and Literature Review (7 pp; Intro & Lit /20)

**Purpose.** Command of the state of the art and its history, **judged**: only the prior art that
Chapters 3–8 build on, each family with its failure mode.

**Criterion.** "Comprehensive, superior understanding of the **historical background** and state of
the art" and "a **critical assessment** of the strengths and weaknesses of the material reviewed is
required for a high distinction". v1.1's tree had no history and no classical-conditioning
antecedent; both are added.

**Scaffold.**

1. **§2.1 Quantum computation preliminaries (≤ 1.5 pp, hard cap).** Prose citing Nielsen & Chuang;
   numbered definitions only for objects reused (the (α, m, ε) block encoding); queries against
   gates; the fault-tolerant frame (NISQ one paragraph: §10.5's feasibility argument is
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
   mixed-parity construction and points here for what they are. **The degree formula**, `eq:degree`, stated here so Chs 4–7 can argue costs: for
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
   reproduction is in §9.1.
2. **§3.2 The latent Chebyshev model (0.5 p).** The normalised basis; f_q(x) = ⟨τ(x)|ψ⟩; the scale
   η; raw τ in rank-one rows. Our closed form for η_e belongs to §4.1 (its check against the
   printed values to §9.1).
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
   Eqs 36–39 → Ch. 8 / Appendix F. The optional figure was dropped (Style Guide §2.4).
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
        whatever the encoder (§4.5, §9.3);
     2. the published normalisation of 𝔾 is loose by a factor growing as N³ (§4.2.2, §9.3);
     3. printed choices distort the solution at the printed n (§4.3, §9.1);
     4. the PDE invariant sets degenerate beyond the printed n, are taken from the known solution,
        omit the initial or boundary function that fixes the solution (the heat panel's natural completion, its
        initial function at t = 0, is a backward heat problem on [−1, 0], hence ill posed)
        (§4.2, §4.3, §9.1; checked against `pihm/docs/10_reproduction.md` and D-028 on 2026-10-04);
     5. the time rule falls short of ε (§4.2, §9.1);
     6. the nonlinear route cannot prepare (§7.2, §9.5);
     7. the readout identity assumes deterministic preparation (§4.2, §8.7, Appendix F);
     8. *(v2.1, one clause in the drafted scope paragraph, added by the author)* the construction
        is stated for one real scalar field, and the paper's Discussion sets complex-valued states
        aside (pointer: Ch. 6).
   - **The paper's own open questions**, quoted, and the concurrent work (Paine 2026) that
     finds, on a few small instances, a representation-dependent normalised gap without a scaling
     in resolution, circuits or a general ordering: it raises the first question without
     answering it.
   - **Close with Q(i)–(iii) in italics**, each with its chapter by `\Cref` (plan §3.2's table).

**Marker checklist.** No sentence reads as authorship of the framework (Style Trap 13);
`wu2025pihm` at the head of §3.3 and at each construction; our numbers absent from §3.2–3.5 and in
§3.6 only as pointers; the three questions close the chapter; ≤ 4 pp.

**v2.1 (W0c) touches only the pointers.** The chapter is drafted (2026-10-07) and its structure
stands. Each weakness keeps one sentence and gains its Ch. 4 pointer: the claims Ch. 4 *derives*
(positive definiteness, the sign of η, the time rule, the readout identity, the PDE invariants) point
to `sec:standard-claims`; the printed choices point to `sec:standard-passage`; the encoder and the
Hamiltonian point to `sec:standard-published` and `sec:standard-hamiltonian`. The "ours / to test"
TODOs are routed by plan §2.1's v2.1 list. No argument is moved out of Ch. 3 or into it.

**Traps.** "Collocation"; the legacy adder-ladder reconstruction; any Θ̃(N²) floor.

---

### 5.4 Chapter 4: The Standard Form: From the Published Method to an Exact Baseline (6 pp; Model Formulation /30)

**Purpose.** Three passes (T-30). Rebuild the paper's method exactly and check its claims
mathematically; pass, defect by defect, from that faithful rebuild to the *standard form* every later
chapter uses; then answer Q(i): build the best exact encoding of the standard form and show that the
degree stays Θ̃(N^{2k}), because the cost is the Hamiltonian's.

**Criterion.** Formulation, band 4: "a significant advance in the state of the art", and "described
in sufficient detail to permit readers to create equivalent models": the standard form's definition
and Table T10 are that specification for the paper's regime. Carries S1's formulation half and S2.

**Sources.** `docs/companion/` 10–14 (basis, differentiation), 20–24 (multiplication, constraints, the
standard residual, its spectrum, worked R2a), 31–33 (published and structured encodings), 47 (the
readout identity), 57 (degree scaling); `docs/10_reproduction.md` §§1–4 and
`docs/06_results_guide/81_reproduction.md` (what §9.1 will show, so §4.1–4.3 point to it and do not
repeat it); claims A-01–A-13, C-01, C-02, C-07; `src/pihm/assemble/standard.py`,
`operators/constraints.py`, `problems/ladder.py` (the printed variants), `circuits/standard.py`,
`arithmetic.py`; derived keys `derivative/n<n>`. Decisions 9, 15, 17, 34 and 49 hold the reasons for
§4.3; state the reasons, never cite the decisions (§3.5 rule 3).

**The audit's division of labour (T-30).** Ch. 3 *names* each weakness in one sentence with a
pointer. Ch. 4 *derives* it: the mathematics, the mechanism and the verdict. §9.1 *shows the
numbers*: T6, F6, the triage table. A Ch. 4 subsection quotes at most one number per claim, by
`\res`, as a pointer to §9.1.

**Scaffold.**

0. **Opening, no heading (0.25 p).** Q(i) restated in one sentence. The encoder's cost and the
   Hamiltonian's cost defined once (the 2026-10-07 draft's opening, kept). The roadmap of the three
   passes in one or two sentences.
1. **§4.1 The method rebuilt (0.6 p; `sec:standard-rebuilt`).**
   - What "faithful" keeps: the normalised basis and the raw τ in the rank-one rows; 𝔾 on
     coefficients (the paper prints 𝔾ₙᵀ, T-16); variable coefficients and sources lifted from n to
     n + 1 qubits; Neumann data as 𝔹(x_m)𝔾; the printed constraint points, Maclaurin sources and PDE
     invariant sets; the doubled space for the quadratic panels (handed to Ch. 7). The printed SM §A
     matrices are reproduced entry by entry (A-01; the worked instance in Appendix C).
   - **The scale, ours:** η_e = ‖b‖² = (N/π)∫f²/√(1 − x²) dx (`eq:eta-e`, moved here from §9.1, its
     label kept): the ideal value of the paper's η, growing like N, so a built-in check on the
     resolution. Its comparison with the printed values is T6 (§9.1).
   - **The classical solve:** the ground state as the smallest right singular vector of the stacked
     residual (formalised in §4.3); never `eigh` of H, because H's relative gap falls below double
     precision (one `\res`, the B-07/B-23 key; the eigh/SVD table → Appendix I). Accuracy by Wedin's
     bound; the reference in full is §8.3, and a result is judged only where its kernel is trusted.
2. **§4.2 Testing the paper's claims (1.75 p; `sec:standard-audit`; T-35).** One audit, split by kind
   into two subsubsections after an opening paragraph that names the claims of both halves.

   **§4.2.1 The Hamiltonian, its filter and its readout (1.0 p; `sec:standard-claims`).** Each claim
   as printed, the mathematics that tests it, and what remains of it (no verdict words are required;
   the conclusion is the paragraph's last sentence):
   - *"Positive-definite with distinct eigenvalues"* (A-09): H = R†R is positive **semi**-definite;
     an exact discrete solution (a polynomial of degree below N, as R3's Legendre polynomials from
     n = 3) is an exact zero eigenvalue; and an under-determined constraint set leaves the bottom
     near-degenerate (the printed Laplace invariant set). Distinctness is tested by that set, not by the
     doubled space (Ch. 7's).
   - *η > 0*: √η = y_s/⟨τ(x_s)|ψ_g⟩ is negative whenever the ground state's sign opposes the datum's;
     the ground state is defined up to a global phase, so η > 0 is a sign convention, and the decoded
     field carries the sign.
   - *Uniqueness*: a homogeneous order-k ODE with a nowhere-vanishing leading coefficient needs
     constraints of rank k − 1 on its solution space, and one regular datum (lemma, ours; it concerns
     the continuous problem, and the truncated kernel is judged by its dimension and gap ratio). The
     PDE invariant sets omit the initial or boundary function, the heat and wave sets also carry
     constraints read off the known solution, and all lose rank beyond the printed n (measured:
     §9.1). The backward-heat observation belongs to §4.3's datum slice, not to this audit.
   - *The time rule* β ≥ λ_max/(λ₂(n − 1)), which the paper calls an approximate lower bound,
     contains no ε, so it cannot certify a target accuracy: the imaginary-time filter needs
     β ≳ ln(1/ε)/Δ on H's own scale; set the two side by side (A-11; the measured shortfall in §9.1).
   - *"poly(n) terms, implemented efficiently"* (A-12): true for gate counts, false for the
     subnormalisation, which sets the number of queries: the bridge to §4.2.2.
   - *The readout identity* assumes the prepared state is the ground state with certainty; a filter
     with post-selection succeeds with p_G < 1, and the identity acquires a correction (stated here,
     derived in Appendix F, the protocol itself further work, §8.7).
   - The units of the paper's O(1/Δ) cost are argued in §3.6 and are not repeated here.
   **§4.2.2 The paper's block encodings (0.75 p; `sec:standard-published`).** The 2026-10-07 draft's
   §4.1, unchanged: Figs 2, 8 and 9 built; each claim tested (`tab:published-verdicts`); the key
   number α/‖𝔾‖₂ growing like jN³ (`\res{derivative/n7}{published_ratio}`); the rebuilt α a third
   of the printed prefactor, so every published-encoding cost is the kinder reading; approximate, so
   it enters resource estimates only. Deviations from the printed figures → Appendix D. Its REVISE on
   ε_G stays open.
3. **§4.3 From the faithful rebuild to the standard form (1.5 p; `sec:standard-passage`).**
   - **Framing sentence:** the faithful rebuild reproduces the paper and inherits its printed
     choices; each is a defect of a stated mathematical kind, and the standard form removes it
     without leaving the paper's regime (derivatives eliminated through the dense 𝔾, the paper's
     lifts, least squares). §3.5 rule 7 applies to every item.
   - **The items, each as defect → replacement → property gained → evidence:**
     1. *Rounded constraint points* (−0.2, −0.73, 0.91, −0.75, 0.02615): a zero imposed where the
        solution does not vanish contradicts the equation, so least squares trades the two and the
        error floors at a level no resolution removes → the point the problem defines, taken exactly
        → convergence. The point is problem data inherited from the paper's statement, not an input
        read off the solution at run time (TRAPS).
     2. *Maclaurin sources* (p̄ = 3, 5, 7): a truncated source poses a different equation (the
        order-7 series is wrong by 130 % at x = −1 for 5d) → the source's Chebyshev coefficients on
        the lifted register, through the same collapse row 𝕄_r𝔻⁽⁰⁾(x_s) → spectral accuracy. Each
        printed choice alone floors the error, and only both removed converge (the triage, §9.1).
     3. *PDE data by hand-picked invariants* → **datum slices**: the initial or boundary *function*
        imposed on its slice as one row family, (𝕊_a(x*) − ĝ τ(x_s)ᵀ/v)Π_f, in both forms →
        answer-independent and well posed at every n; the heat panel's data are imposed at t = −1, so
        the problem runs forward.
     4. *A leading coefficient with a double zero* (R3c, R3d: the associated Legendre operator
        multiplied by 1 − x²): the substitution f = √(1 − x²)v leaves simple zeros and removes the
        branch point that limits convergence to algebraic → spectral convergence; it is also the form
        the descriptor can run (§5.6's double-zero limit).
     5. *The Laplace solution's typo* (cos, not cosh): the reference corrected, one clause.
     6. *Two axes* → any number: the residual on d Chebyshev axes by tensor products, constraints on
        slices (`app:pihm-multi-axis`). Two are run; say so.
     7. *The Gram sum* → **the stacked residual** R = [A; 𝔹₁; …; 𝔻-slices; ratio rows], with
        H = R†R equal to the paper's sum: the object solved (SVD, §8.3) and encoded (the stacked
        reflection, §8.4) is R, and H is never formed.
     8. *Kept on purpose:* least squares rather than the tau method (the tau ablation gives an exact
        kernel at comparable accuracy, Appendix K, but would leave the paper's construction); the
        paper's lift for variable coefficients (the descriptor's square Galerkin form is Ch. 5's).
     9. *Vector data* → ratio rows, defined with systems in §6.2 (forward pointer).
   - **Definition (the standard form)** (`def:standard-form`): the stacked residual with equation
     block Σ_j 𝕄_{a_j}𝔾^j − 𝕄_r𝔻⁽⁰⁾(x_s) and constraint rows of four kinds (zero, collapse, ratio,
     datum slice; Table T2 in §8.2 lists them as model inputs); H_std = R†R. The problem is unnamed
     ("R2a"); the paper's panel is "R2a as printed" (T-33).
   - **Table T10, `tab:deviations`** (≈ 0.5 p): aspect | Wu et al., as printed | this thesis | defect
     removed, or property gained | argued in. Residual rows from the items above; pipeline rows
     stated with their pointer: the 𝔾 encoder (§4.4), normalisation by ‖H‖_F → by the construction's
     α_R (§8.4), mixed-parity QSVT → GQSP, QITE with the time rule → the minimax edge filter at an a
     priori degree (§8.5; QITE kept for §9.1–9.2), phases by fitting → Weiss's complement and the
     inverse NLFT (§8.5), the interferometric readout → the classical decode (§8.7), `eigh(H)` → the
     SVD or Lanczos of R (§8.3), answer-independent initial states (§8.5), the doubled space → also
     the Carleman lift (Ch. 7), one real field → systems and realification (Ch. 6).
   - Close: the faithful-against-problem errors and the triage are §9.1's (F6).
4. **§4.4 An exact structured encoding (1.0 p; `sec:standard-factorisation`, with subsubsection
   `sec:standard-cost`).** The 2026-10-07 draft's §4.2 and §4.3, merged and tightened: the idea in
   words first (row weight × parity-selected shift × column index); `prop:G-factorisation` (C-01),
   the measured error as verification, not evidence; Λ as a Z-string LCU, U_odd by subtraction with
   a post-selected borrow flag (F3), R₀; `prop:standard-cost` (α_G = N(N−1), → 2j_{−3/4,1} ≈ 2.117
   times ‖𝔾‖₂, O(n²) gates, n + 4 ancilla, the n − 1 selector qubits as the price of N/2 terms);
   lifts, rank-one rows and products sharing one ancilla register. The arithmetic and the proofs →
   Appendix E.
5. **§4.5 What remains: the standard-form Hamiltonian (1.0 p; `sec:standard-hamiltonian`).** The
   2026-10-07 draft's §4.4, unchanged in substance:
   - for constant coefficients α_H/‖H_std‖ stays bounded (C-02): the encoder has done its job;
   - ‖H_std‖ = Θ(N^{4k}) against a gap measured flat (on R2a and R2b so far; plan §2.1), so by
     `eq:degree` d = Θ̃(N^{2k}), Θ̃(N⁴) at second order: **the Hamiltonian wall**, since α_H ≥ ‖H‖
     for any block encoding; the floor stated for the minimax filter and hedged to Lin & Tong;
   - the degree's growth with the published, the structured and the ideal encoding, separating the
     two costs; the classical reading (§2.3): H_std is the least-squares functional of an order-k
     operator and squares its conditioning;
   - **the scope, volunteered:** R3's lifted (1 − x²) multiplier, where the structured LCU is loose
     and the encoder's cost reappears; hence the ideal-encoding bound beside every as-built cost
     (T-25);
   - close by naming Ch. 5 and what it changes: the Hamiltonian.

**Figures and tables.** T10 (`tab:deviations`, new); `tab:published-verdicts`; `tab:alpha-G-short`
(full table → Appendix E); F3 (`fig:uodd-select`).

**Appendix offloads.** Appendix C: the faithful rebuild's conventions, the worked N = 4 residual,
the lifts, the multi-axis residual. Appendix D: the published build. Appendix E: the factorisation's
proof, the arithmetic SELECT, the cost proof, the Bessel-kernel limit and ‖𝔾^k‖₂ = Θ(N^{2k}).
Appendix F: the readout identity at p_G < 1. Appendix I: eigh against SVD. Appendix K: the triage,
the tau ablation, every panel's verdict.

**Marker checklist.** Every paper claim tested in §4.2 is stated as the paper states it, tested, and
points to its numbers; T10 lists every deviation, each row a defect and a property, none a date or a
decision; the standard form is defined once, formally, before §4.4 uses it; the encoder/Hamiltonian
distinction is unmissable and the R3 caveat stated; S2 serves the comparison; "as printed" appears
only in §4.1–4.3; nothing in §4.1–4.3 repeats Ch. 3's prose or §9.1's numbers.

**Traps.** A changelog ("we then fixed…", "after finding a bug…"); "corrected"; calling the exact
constraint points *answer-independent* (they are problem data inherited from the paper; the
answer-independent things are the initial state and the filter's parameters); quoting §9.1's tables
here; "our standard-form solver"; legacy ε_G bounds; implying the structured encoding is tight on
every problem.

---

### 5.5 Chapter 5: The Descriptor Reformulation (9 pp; Model Formulation /30, the core)

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
     block per component; the state, initial state and readout are the standard form's. The mass
     form is *defined* here, for z′ = 𝔸z in general, because the theorem below covers both layouts;
     its use for several fields (data, coupling, circuits, the comparison with a chain per field) is
     Ch. 6's (T-31). Its running example here is R1, a single first-order equation.
   - **Theorem (kernel equivalence)**, both layouts: ker A_desc = {(p, 𝔾p, …, 𝔾ᵏp) : p ∈ ker A_std}
     for the chain, and ker A_desc = ker A_std for the mass form, because B̃ is invertible. Proof in
     five lines in the body if it fits, else Appendix G.
   - The least-squares ground states differ by row weighting and converge to the same function (B-02).
   - **Volunteer the cost in the same breath:** the chain grows the state from N to 2^⌈log₂(k+1)⌉·N;
     the mass form grows nothing.
4. **§5.4 Constraints and partial differential equations (0.5 p; label `sec:descriptor-constraints`
   kept).** Constraint rows on the block they read; Neumann on the f′ block, the same atom as
   Dirichlet, no 𝔾; PDEs: one field block and a chain per axis; datum slices for initial and boundary
   *functions* (defined with the standard form, §4.3), available to both forms (so "the descriptor
   avoids doubling for linear PDEs" is **not** claimed, B-20). Coupled fields: one sentence pointing
   to Ch. 6.
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
     0.01–0.76 against as little as 1e-19 unscaled (planning values; §9.4 has P8's).
   - **What it does not:** where the leading coefficient vanishes, ‖H‖ grows as ζ^{2k}, so the
     degree is about Θ̃(N²); on two axes the gap still falls with N; **a double zero is beyond any
     block rescaling** (the paper's own R3c and R3d multiply by (1 − x²)), which is why the
     descriptor runs the problem with simple zeros. General equilibration costs Θ(P) gates and is
     excluded from circuit paths.
   - The analogy, stated once: this is the descriptor's version of Olver & Townsend's diagonal
     preconditioner.
7. **§5.7 The block encoding: one flat LCU (1.0 p).** Every block a short sum of SHIFT·diag terms
   (truncated shifts through one overflow qubit; diag(k) as a Pauli-Z sum; near-constant diagonals
   by reflections); the rescaling in the coefficients; rank-one rows through the feature map, with
   no dense state preparation. A system's coupling 𝔸 (a sum of matchings) is Ch. 6's: one pointer. **Figure F5** (quantikz)
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
     the ideal bound; the heat panel at small n); pointers to §9.3–9.4.
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

### 5.6 Chapter 6: Coupled Systems and Complex-Valued Fields (2.75 pp; Model Formulation /30) — NEW (T-31, T-32)

**Purpose.** Take the construction from one real scalar field, the paper's scope, to several
coupled fields, and with them to complex-valued linear equations; then hand a coupled linear system
to Ch. 7, since a Carleman lift is one.

**Criterion.** Formulation, "sufficient detail to permit readers to create equivalent models": the
rows, the data and the circuits of a system must be rebuildable from the body plus Appendix H. The
chapter answers no numbered question (T-31); it opens with the scope the paper leaves (one real field;
its Discussion: with a Fourier basis "the resulting total energy function is of a complicated form,
rendering it difficult to find the ground state") and closes on Q(iii)'s prerequisite.

**Sources.** `docs/02_methods.md` §3.2 (the mass form), §3.3 (ratio rows), §3.4, §6.2 (a system's
initial state); `docs/companion/` 21 (constraints), 51 (mass form), 61 (time axis);
`docs/16_extensions.md` §1.1 (R7, the mass form against the chain), §2–4; `docs/03_problems/07_r7.md`;
decisions 39, 42, 45 (reasons only); `src/pihm/assemble/systems.py`, `circuits/systems.py`,
`ir.py` (`matching_terms`), `operators/constraints.py` (`ratio_rows`), `problems/fluids.py`
(`real_embedding`), `circuits/tensor.py` (complex weights); notebook 60. The paper's Discussion
(p. 11) for the complex-valued remark.

**Scaffold.**

0. **Opening, no heading (0.2 p).** The paper's scope (one real scalar field), its remark on
   complex-valued states, quoted, and what this chapter adds; the roadmap.
1. **§6.1 Several fields on one state (0.6 p; `sec:systems-fields`).**
   - A first-order system u_i′ = Σ_j 𝔸_ij u_j (constant coefficients; one equation per field, each
     holding its own first derivative) on one Chebyshev axis; on a time axis ξ = 2t/T − 1, with the
     factor T/2 (moved here from Ch. 7's space–time paragraph).
   - The state: one block per component, on a field register of ⌈log₂ C⌉ qubits, padded to a power
     of two with padding rows of weight 1 that decouple exactly.
   - The rows: standard I⊗𝔾 − 𝔸⊗I (the paper's elimination, applied per field); the descriptor's
     mass form (§5.3) multiplies them by I⊗B̃. Same kernel; an IVP with data has a one-dimensional
     near-kernel.
   - Higher-order systems: by reduction to first order (one sentence; none run beyond R7's order-two
     equation written as two fields).
2. **§6.2 Data for several fields: ratio rows (0.4 p; `sec:systems-data`).**
   - The ratio row 𝔽 = y_a(I − |a⟩⟨a|) − w⟨a| on the field register, times 𝔹(x*): it imposes the
     *direction* of the vector datum and leaves its scale free, as a zero constraint does; divided
     by y_a it is scale-free; a zero datum holds its component to zero exactly.
   - The scale from the regular datum, as for one field. The initial state's weighting by w₀/‖w₀‖
     is stated in §8.5; one pointer, with the reason (equal weights cancel on Taylor–Green).
3. **§6.3 The mass form for systems (0.4 p; `sec:systems-mass`).**
   - Why the mass form and not a chain per field: the equation already gives each derivative, so a
     derivative block carries nothing new, costs register and needs rescaling. Measured on R7
     (u′ = v, v′ = −π²u), the mass form's gap is about 2.1 times the block-rescaled chain's, flat in
     n (key to add, plan §2.1); the chain stays as a labelled ablation.
   - The standard and descriptor forms of a system share their state, initial state and readout,
     and differ only by I⊗B̃: the like-for-like comparison R7–R10 rely on.
4. **§6.4 The coupling on a circuit (0.4 p; `sec:systems-coupling`).**
   - 𝔸 split by edge colouring into as many matchings as its largest row or column degree; each a
     permutation of the field register's basis states, its entries a multiplexed rotation on one
     flag; α = the largest entry. Both forms pay the same for 𝔸.
   - The ratio rows as three LCU terms (identity, projector, a loaded rank-one term).
   - The matchings against Pauli words, one sentence with numbers (key to add); construction →
     Appendix H.
5. **§6.5 Complex-valued fields (0.75 p; `sec:systems-complex`).** Scope fixed by T-32.
   - **The formulation does not need a non-Hermitian filter.** For complex coefficients, data or
     sources R is complex, and H = R†R is still Hermitian and positive semi-definite; the ground
     state is still the smallest right singular vector of R; the stacked reflection and GQSP act on
     H′ unchanged. The non-Hermitian operator is R, which the filter never sees. (Narrative and
     mathematical; no complex-R preparation was run.)
   - **Realification, the route run.** z = u + iv as two real fields: z′ = cz gives
     [u; v]′ = [[Re c, −Im c], [Im c, Re c]][u; v] (c, not a or α, which are taken), one more
     field-register qubit, the same kernel under the
     real-linear isomorphism. **R7 is exactly this:** with z = πu + iv, u′ = v and v′ = −π²u are
     z′ = −iπz, a single-mode Schrödinger-type equation. The Fourier–Galerkin fluids of Ch. 7 are
     carried on real bases for the same reason (sine modes for Burgers; cos/sin with an isometric
     real embedding for Navier–Stokes).
   - **Native complex encoding, built once.** The tensor layout's coupling (Ch. 7) is built on
     complex Fourier variables, with complex phases i^{Σa} in its LCU weights, and verified (exact and
     IR); it is never used to prepare a state, because the classical pipeline carries real data only.
   - **Not built:** complex sources, data and coefficients in the circuits' loaders (a phase on the
     collapse row; a complex state loader), and so native complex preparation. Future work (§11.2).
   - The research proposal's "complex-valued, non-Hermitian equations" is answered here at the level
     of the formulation, and recorded as a deviation (§13.4).
6. **§6.6 From systems to lifts (0.2 p; `sec:systems-lifts`).** A Carleman lift of a polynomial
   system is a linear system on its monomials, so every construction of this chapter carries over:
   the components become monomials, the ratio rows carry the data's moments, and 𝔸 becomes 𝔸_K.
   Ch. 7 adds only the lift and its products.

**Figures and tables.** None required. Optional: a two-column table of R7 in both forms and the chain
(gap, degree, γ²) if §9.5 cannot hold it; prefer §9.5.

**Appendix offloads.** Appendix H (new opening section, `app:systems`): the system rows in full,
the padding, the ratio rows and their three-term circuit, the matchings by edge colouring, the
realification map and its kernel equivalence, the real embedding of the Fourier variables.

**Marker checklist.** The scope gap stated from the paper's own words; systems rebuildable from body
and Appendix H; the mass form *applied*, not redefined (§5.3 owns it); realification stated as the
route run, with R7 as its instance; every complex-valued claim scoped (formulation; one encoding
verified; preparation not built); the hand-off to Ch. 7.

**Traps.** "Handles complex equations" unscoped; any complex-valued result that rests on the legacy
`DESolverLib` (never cited); redefining the mass form or restating its kernel theorem; calling the
tensor encoding "prepared"; claiming higher-order systems were run; "vector-valued solver".

---

### 5.7 Chapter 7: Polynomial Nonlinearity (3.25 pp; Model Formulation /30)

**Purpose.** Answer Q(iii): separate what the doubled space can claim (an exact encoding, a
projection) from what the Carleman lift can (a preparation, in both forms), and set up the fluids.
The lift is a coupled linear system, so Ch. 6's rows, data and circuits are cited, not restated.

**Sources.** Planning §3.6, §5.3 (R6–R10), §6.5, §7.7; `docs/02_methods.md` §3.4–3.5; `docs/companion/`
60–65; `docs/16_extensions.md`, `docs/17_navier_stokes.md`; claims A-10, B-12, B-18, B-19, B-22, C-09,
C-10; `src/pihm/carleman.py`, `problems/fluids.py`, `circuits/tensor.py`, `circuits/folds.py`.

**Scaffold.**

1. **§7.1 Two treatments (0.25 p).** The doubled space (the paper's; run here in the standard form
   only, since it projects in either) and the Carleman lift (both forms).
2. **§7.2 The doubled space (0.6 p).** An exact encoding; kernel dimension N² minus the rank, at least
   2^{2n−1} (A-10, measured); **Proposition (imaginary time projects; no answer-independent penalty
   isolates the solution)**: a kernel containing ψ⊗ψ and φ⊗φ contains their sum, which is not a
   product state, so no Hamiltonian enforces the product structure; imaginary time projects the
   initial state onto the kernel; the paper's choice reported as the product state of least residual.
3. **§7.3 The Carleman lift in space–time (1.0 p).**
   - z = (u, u^{⊗2}, …, u^{⊗K}) in the symmetric layout, carried as u/s with s = max(‖u₀‖, 1), a
     diagonal similarity that keeps no level growing as ‖u₀‖^k.
   - The truncation error is O(ρ^K) for ρ = ‖u₀‖‖F₂‖/|Re λ₁(F₁)| < 1: **a sufficient condition, a
     worst case over all states** (cite Liu et al. 2021); the convergence is measured per order
     against the exact lift (§9.5).
   - A linear IVP has one solution, so the space–time residual has a one-dimensional near-kernel:
     the uniqueness is Carleman's, not the form's.
   - The lifted system 𝔸_K on the time axis in both forms is Ch. 6's construction with 𝔸 → 𝔸_K
     (`sec:systems-fields`, `sec:systems-mass`): one sentence and the two displayed rows, not their
     derivation; the like-for-like comparison of R8–R10.
   - Initial data by Ch. 6's ratio rows on the data's moments; the error split into the lift's and
     the time axis's.
4. **§7.4 Products and couplings on a circuit (0.6 p).** The nodal fold 𝕟₁^{(p)} =
   2^{pℓ/2}𝕌†Δ_p𝕌^{⊗p}: exact, no ancilla beyond padding, α = 2 for p = 2, **within 1.21 times
   ‖𝕟₁‖₂ (1.58–1.665): tight, not optimal** (Journal E087 corrected v2.0's "optimal"); the Fourier
   fold QFT, copy, QFT†; the Chebyshev DCT budgeted as a cited primitive (Klappenecker–Rötteler),
   **not built gate-level**, said plainly. The lift's coupling 𝔸_K: as Ch. 6's matchings in the
   symmetric layout (one pointer), or in the **tensor layout with 2K − 1 terms** (not K²), each F_p
   on adjacent slots, which reaches field scale; its complex Fourier variables are noted with a
   pointer to §6.5.
5. **§7.5 Fourier–Galerkin fluids (0.6 p).** Burgers: F₁ = diag(−νk²), F₂ the (u²)ₓ/2 convolution,
   on sine modes. 2-D vorticity Navier–Stokes on the real cos/sin basis (§6.5) with ψ̂ = ω̂/|k|²
   eliminated and exact rational couplings. Taylor–Green (its modes share |k|, so the lift is exact:
   a validation) and a counter-rotating vortex pair (active triads). References: the Galerkin
   system's IVP, Cole–Hopf for Burgers, a pseudo-spectral simulation for the truncation's own error.
6. **§7.6 Preparation versus projection (0.4 p).** **Table T8**: which route sits on which side, and
   why. **The caveat that matters:** a unique, trusted kernel certifies the lifted *linear* problem,
   not the lift's convergence, which is measured separately (§9.5). One sentence tying back to
   §5.1: the mass form is the same banded left factor, applied in time.

**Marker checklist.** "Prepared" never for the doubled space; ρ stated as sufficient; the fold's
α = 2 called tight (within 1.21), not optimal; the DCT named as unbuilt with the reason; uniqueness
attributed to Carleman; trust distinguished from convergence; Ch. 6 cited, not restated.

**Traps.** "K² terms"; "both forms" for the doubled space; ρ < 1 as necessary; "optimal" for the
fold; re-deriving the space–time rows.

---

### 5.8 Chapter 8: Preparing and Verifying the Ground State (5.5 pp; Model Formulation /30)

**Purpose.** Specify everything shared by both forms after the residual is built, and design the
numerical experiment, so a reader could "create equivalent models". The forms differ only in the
residual, so every difference in Ch. 9 is a difference of Hamiltonians.

**Criterion (Modelling, verbatim):** "described in sufficient detail to permit readers to create
equivalent models. This should include: **a description of any software tools used and/or created;
a description and/or diagram of the model configuration; descriptions of the model input options
selected (boundary conditions…)**". Band 3 names "**poor design of numerical experiment**".

**Sources.** `docs/02_methods.md` (all sections; it is this chapter's source of truth); Planning §3.5,
§3.7–3.8, §5.4, §6.2, §7; claims C-03, C-04, C-08, B-13, B-16, B-17, B-24; `docs/15_filters.md`;
`docs/companion/` 40–47 and 70–76.

**Scaffold.**

1. **§8.1 Overview and model configuration (0.75 p).** **Figure F1**, the model configuration:
   problem specification → residual (standard | descriptor; nonlinearity none | doubled | Carleman;
   shared constraint rows) → stacked-residual block encoding U_R → reflection V → walk W → GQSP
   filter → post-selection → decoded field, with the classical reference and the verification modes
   and tiers attached to the stages they check. Its caption stands alone. The design principle in one
   paragraph.
2. **§8.2 Problems and model inputs (1.0 p).** **Table T3**, the benchmark ladder R1–R10: one new
   capability each, so a failure localises, with its physics (full specifications → Appendix J).
   **Table T2**, the constraint kinds (zero, collapse, ratio, datum slice): the rubric's "boundary
   conditions". A problem is data: equation terms, constraints, regular datum, reference. The paper's
   panels as printed appear only in the reproduction (T-27). The inputs every run records: n per
   axis, form, encoder, filter, ε = 1e-6, initial state, rescaling, Carleman order K.
3. **§8.3 The classical reference (0.5 p).** The smallest right singular vector of the stacked R:
   dense SVD to 8,192 physical columns (accuracy by Wedin's bound); beyond, shift-invert Lanczos on
   the augmented system [[I, R], [R†, −μI]], which never squares R, then Rayleigh–Ritz, with an a
   posteriori estimate. Trusted means a one-dimensional kernel with its ratio above 20, the largest
   spacing the ladder's spectra show without one. Why never `eigh(RᵀR)` (one number; the table →
   Appendix I). Decoding, η_e, and the metrics at three levels (operator, state, field).
4. **§8.4 From stacked residual to quantum walk (0.75 p).** **Proposition (stacked reflection)**:
   for U_R encoding R = [R_1; …; R_L] with α_R = √(Σα_j²), V = U_R†(2Π − I)U_R is a Hermitian unitary
   with Π_in V Π_in = 2H/α_R² − I, and controlled V needs only controlled reflections (proof →
   Appendix F). W = (2Π_in − I)V, Π W^k Π = T_k(H′). The quadrature composition has no ℓ¹ penalty.
5. **§8.5 The filter and its parameters (1.0 p).**
   - GQSP realises any |P| ≤ 1 polynomial of the walk, without parity (prior art, §2.5).
   - **The minimax edge filter**, P = T_d(w(x))/T_d(w(−1)), w mapping the excited spectrum [x₁, 1]
     onto [−1, 1], at the least degree that suppresses it to ε relative to the ground value:
     d = ⌈arccosh(1/ε)/θ₀⌉, θ₀ = arccosh(−w(x₀)), computed from heights above the edge so the ground
     state's is resolved.
   - **The parameters are a priori:** the edge (σ₀, σ₁ of the reference) and α_R, never the
     solution. The edge is assumed known, the standard known-gap assumption; say so here and in
     §10.6.
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
   - **Deviations from Wu et al.:** one sentence pointing to Table T10 (`tab:deviations`, §4.3),
     which lists them all (T-34); none is restated here.
6. **§8.6 Verification and the error budget (1.0 p).**
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
7. **§8.7 Reading out the solution (0.25 p).** The field is decoded classically from the prepared
   state's field blocks and scaled by the regular datum. One paragraph: the paper's interferometric
   protocol is built and verified at small n (R1, R2a, R5a), with our correction for p_G < 1
   (Appendix F), and its study at scale is future work.
8. **§8.8 Design of the numerical experiment (0.5 p).** What the study varies (n, form, encoder,
   filter, initial state) and holds fixed (constraints, ε); what counts as a gate (transpiled to
   {cx, u}, dense cited primitives counted apart); ancilla counted on the composed V. **Fairness,
   declared:** the structured encoding is the strongest standard-form baseline built, and every
   comparison is quoted as built and at α = ‖R‖ (T-25), so a reported advantage is not an encoder
   artefact. The tier is marked on every number.
9. **§8.9 Software and computation (0.25 p).** `pihm` (numpy, scipy, qiskit, qiskit-aer): one
   implementation per concept, problems as hashed data, tests of each claim; production on Setonix;
   every number regenerated from archived records by one command (Appendix L). No code listings.

**Marker checklist.** A configuration diagram; every input option with its value; the software
described; the experiment's design and fairness justified; the deviations from the paper listed; the
T2 ≡ T1 argument before any T2 number; the readout classical, the protocol attributed.

**Traps.** A software manual; "Pillar" and "tier" jargon; QITE presented as the comparison's filter;
the readout presented as new or as the method's readout.

---

### 5.9 Chapter 9: Numerical Study (10 pp; Results & Discussion /30)

**Purpose.** Evidence every claim of the Abstract and of §1.3, "without reference to any other
documents", one section per question or contribution.

**Criterion.** "Complete, clearly presented results, with detailed discussion showing insight… or
warranting publication." Every figure is interpreted in prose; each section ends with what it
established.

**Sources.** P8's records (`results-v1`) through `\res`; the reports `docs/10_reproduction.md`,
`11_pillar1.md`, `12_pillar2.md`, `13_descriptor.md`, `15_filters.md`, `16_extensions.md`,
`17_navier_stokes.md`, `18_claims.md`; the results guide `docs/06_results_guide/` 81–87, ordered as
this chapter; the notebooks of Planning §10.8, one per figure.

**Opening (0.25 p).** What each section evidences; the tiers; the records' provenance in one
sentence; the full per-problem results → Appendix J.

**Scaffold.**

1. **§9.1 Reproducing Wu et al. (1.75 p; S1).** **Table T6**: η_e for the 11 ODE panels (printed,
   ideal ‖b‖², ours at the printed n) and a summary line for the five others (Appendix K has all
   16). The closed form η_e (`eq:eta-e`, derived in §4.1) is cited, not restated: what it
   validates is that our conventions are the paper's. This section holds the numbers for the claims
   §4.2 derives; it does not re-argue them. **Figure F6** (nb 11): the panels as printed against the problem for Fig. 5, the
   distortion from rounded points and Maclaurin sources. The Fig. 6 and 7 non-reproductions and the
   hypotheses tested; the Laplace typo; the heat panel's backward data. The paper's quantum claims
   (nb 12): the time rule falls short of ε (A-11), the linear H is semi-definite where the discrete
   solution is exact (A-09), the doubled-space kernel count (A-10). The claims verdicts → Appendix K
   (one paragraph here).
2. **§9.2 The pipeline is faithful (1.5 p; S3).** Operators equal the assembled residuals in every
   mode (**Figure F7**, nb 20). The circuit equals the emulation before normalising, ≤ 1e-10, on every
   minimax T1 record (nb 31); the reproduction's QITE T1 records that miss the bar are reported with
   their degree (plan §2.1, open item: 43 of 46 keys pass before P8). Every trusted preparation within ε and its a priori bound (nb 30); the decoded
   field within its budget (**Figure F8**, nb 32). What the answer-independent choices cost: γ for
   the initial states, and an underestimated gap (nb 33). The filter study in one table and two
   sentences (nb 34; B-17).
3. **§9.3 Where the cost lies (2.0 p; Q(i), Q(ii); C, S2).** **Figure F9, the headline** (nb 40):
   against N, the encodings' looseness α_H/‖H‖, the Hamiltonians' relative gap, and the degree
   (which grows as the square root of the first over the second), for the published, structured and
   descriptor encodings, with fitted exponents; T2 points where measured and T3 beyond, visibly
   distinguished. **Table T7** (nb 21, 40): published | structured | descriptor, across ‖H‖ scaling,
   gap, α/‖·‖, cx per query, ancilla, exactness, degree at n = 8 as built and at α = ‖R‖, and the
   degree's exponent. **Figure F10** (nb 41, optional): case by case, the descriptor's cost over the
   standard form's, as built and at the ideal bound, with the reversals marked. Interpretation: the
   encoder wall (published to structured) and the Hamiltonian wall (structured to descriptor) as two
   gaps on one plot.
4. **§9.4 The descriptor's gap and its rescaling (1.75 p; the challenge).** **Figure F11** (nb 42):
   the gap and γ² unscaled against rescaled, every panel; the a priori rule against the best ζ on a
   grid; where it stops (two axes, the singular ‖H‖ growth). **Figure F12** (nb 43): three
   representative problems in both forms, each with its solution and cost: R2c (stiff: rescaling's
   biggest gain), R3a (a leading coefficient with zeros: where the ideal-bound comparison reverses),
   R5b (heat on two axes: the gap still falls, and the descriptor costs more at small n). The rest →
   Appendix J.
5. **§9.5 Systems and nonlinear problems (1.5 p; Ch. 6, Q(iii), S4; label `sec:results-nonlinear`
   kept).** **R7 first (one paragraph, nb 60):** the coupled oscillator, the realification of
   z′ = −iπz, in both forms and the chain ablation: field error, the mass form's gap against the
   chain's (about 2.1×), degree, γ² under the data-weighted initial state, and T1 = T2. Then R6's
   kernel beside R8's (the projection evidence: kernel dimensions against one) (nb 61). R8: the
   K × n_t error surface and the degree in both forms (C-09). R9, viscous Burgers (**Figure F13**,
   nb 62): the lift's error per order follows a/ν (about a/5ν) and not ρ, which grows with the
   modes; the lift converges at a/ν = 3 and diverges at a/ν = 10 while its kernel stays unique and
   trusted (a/ν ≈ 5, where a/5ν reaches one, is an extrapolation: say so): a negative finding with
   its analysis.
6. **§9.6 Case study: two-dimensional Navier–Stokes (1.25 p).** **Figure F14** (nb 70): vorticity
   snapshots and the degree pairs. Taylor–Green validates F₁, the rows and the time axis (the lift
   exact to rounding). The vortex pair at a/ν = 3, 10 and 30 on 12–80 modes: the lift's convergence
   and the truncation against a direct simulation; every exact emulation within ε; the descriptor's
   time axis lowers the degree in every pair, the ratio narrowing as the modes grow (C-10). The tensor
   layout to 316 modes in 2K − 1 terms, a native complex encoding verified but not prepared (§6.5),
   with its gates per query against the matchings (B-19). T1 is
   beyond the simulation budget here, with its estimate quoted: said plainly.
7. **§9.7 Summary of findings (0.5 p).** Six or seven numbered findings, **at least two negative**,
   for example:
   1. the paper's ODE results reproduce, its PDE and nonlinear ones do not;
   2. the cost of the standard form is its Hamiltonian's;
   3. the descriptor's degree advantage: large on one axis, modest on two, reversed on the heat panel
      at small n and on R3 at the ideal bound;
   4. the descriptor's gap erodes where derivatives are uncontrolled; rescaling restores it on one
      axis only;
   5. the pipeline is verified end to end at every size it reaches;
   6. coupled systems run in both forms on one state, and the mass form beats a chain per field;
      Carleman prepares in both forms, but a trusted kernel can hide a diverging lift;
   7. Navier–Stokes is reached by exact emulation and estimate, not by circuit simulation.

**Marker checklist.** Every number's tier marked; "could not simulate" kept apart from "cannot
reach"; at most three in-depth problems; every caption stands alone; at least two negative findings;
every Abstract number backed here; §9.1 framed as a test of the paper.

---

### 5.10 Chapter 10: Discussion (4.5 pp; Results & Discussion /30)

**Purpose.** Explain and judge; never restate. "Insight into the significance of the work" is the
band-4 separator.

**Scaffold.**

1. **§10.1 Why the descriptor form wins, and what it costs (1 p).** Norm, not encoding: eliminating
   derivatives multiplies norms; carrying them keeps each block O(N). The same mechanism that buys
   the norm weighs the gap (the norm carries every derivative): one idea, two consequences. The
   price: the block register, the per-query constant, rescaling, and no remedy on two axes or at a
   double zero. The classical mirror: first-order least squares and the ultraspherical method found
   the same trade.
2. **§10.2 End-to-end complexity (1 p).** In your own voice: d = Θ(√(α_H/Δ) log 1/ε) is the
   residual's effective condition number, so Θ̃(N^{2k}) against Θ̃(N) is the conditioning of an
   order-k least-squares discretisation against a first-order one. Total gates Θ̃(N poly n) against
   Θ̃(N^{2k} poly n) on a regular one-axis problem. **Neither is poly-log: say it first.** The minimax
   filter changes the constant, not the Θ. Hedge any "for every filter" statement to what Lin & Tong's
   optimality and the linear-system κ lower bounds support. The edge-known assumption.
3. **§10.3 What the reproduction says about the published method (0.75 p).** Conventions sound and
   η_e right; printed choices distort; PDE and nonlinear panels unreproduced; normalisation loose; the
   time rule short of ε; the readout identity needs p_G < 1. Collegial and evidential; what it means
   for readers of the paper. Interpret, do not restate, Ch. 4's T10: which of the paper's choices
   were defects of the method and which of its presentation.
4. **§10.4 Where the construction applies (0.5 p).** **Table T9**, an applicability map (Green's Fig.
   4.18 is the model): problem class (regular one-axis ODE; leading coefficient with a simple zero;
   double zero; two-axis PDE; coupled first-order systems; complex-valued linear equations, by
   realification (formulation only: what doubles, what is not built); nonlinear with a converging
   lift; past the lift's boundary) × the descriptor's gain × what to do. Guidance a practitioner could act on.
5. **§10.5 Feasibility on fault-tolerant hardware (0.5 p).** Logical qubits, cx per preparation and
   depth at meaningful n from T3; set beside explicit resource counts for linear-system ODE solvers
   (Jennings et al.), hedged; why NISQ is out of scope.
6. **§10.6 Limitations (0.75 p).** Each with its analysis: no hardware; circuit simulation only at
   small n; the spectral edge assumed known; the DCT a cited primitive; the doubled space projects;
   Navier–Stokes bounded by emulation and estimate; the descriptor's Hilbert-space and per-query cost;
   the double zero excluded; the iterative reference's bound an estimate; trust is not convergence;
   complex-valued fields carried by realification only, with no native complex preparation;
   Figs 6–7 unreproduced (authors not contacted).

**Marker checklist.** Explains rather than restates; the complexity argument consistent with §3.6,
§4.5 and §5.9; every limitation owned with its analysis; consequences for the field drawn.

---

### 5.11 Chapter 11: Conclusions and Future Work (2.5 pp; Conclusions /10)

**Scaffold.**

1. **§11.1 Conclusions (1.25 p).** A verdict per contribution (C, S1–S4), mirroring §1.3, each with
   its headline number once more. Close with the transferable principle (the spine generalised:
   *condition the residual before encoding it*).
2. **§11.2 Future work (1.25 p).** Four or five items, each with a motivation and **a concrete first
   step**:
   1. on-circuit gap or edge estimation, removing the known-edge assumption;
   2. a rescaling (or reformulation) that keeps the gap on two axes, the descriptor's open problem;
   3. a gate-level DCT, so the Chebyshev fold is fully built;
   4. hardware validation of R1 at n = 2 (its circuit is small enough to state);
   5. the research proposal's remaining aims: native complex encodings (a phase on the collapse
      row, a complex state loader) so that complex-valued fields are prepared without
      realification, the tensor layout's complex coupling taken through preparation (§6.5); and
      data-informed constraint rows;
   6. (candidate) the paper's interferometric readout at scale, with shot-count studies.
   Choose four or five.

No new results and no new citations in this chapter.

---

## 6. Appendices (outside the page limit)

| | appendix | content | cited in |
|---|---|---|---|
| A | Quantum gate reference | the gate table; multi-controlled decompositions | §2.1 |
| B | Chebyshev and ultraspherical identities | normalised basis, S, 𝔾 entries, the B̃/D̃ recurrence, the ultraspherical connection, the N = 4 instance | §2.3, §3.3, §5.2 |
| C | Wu et al.'s standard form in full | the faithful rebuild's conventions; worked N = 4 residual; 𝕄_{x^p}, 𝕄_a, 𝕟₁, 𝕟_x; the printed SM §A matrices reproduced (A-01); the residual on any number of axes (`app:pihm-multi-axis`); the datum-slice rows; the R3c/R3d substitution | §3.3, §4.1, §4.3 |
| D | The published circuits as built | Figs 2, 8, 9 rebuilt; every deviation; measured qubits, gates and ε_G(n); the prefactor against ‖𝔾‖₂ | §4.2.2 |
| E | The structured exact 𝔾 encoding | the factorisation proof; Λ, U_odd (subtraction with borrow), R₀; the cost proof; α across n; the Bessel-kernel limit and ‖𝔾^k‖₂ = Θ(N^{2k}) | §4.4–4.5 |
| F | Shared pipeline identities | the stacked reflection; qubitisation (one power, then one restriction); the controlled walk; imaginary-time coefficients and Σ\|q_k\| = 1; the minimax edge filter and its degree; GQSP phases; the interferometric readout and the identity for p_G < 1 | §8.4–8.7 |
| G | The descriptor construction in full | block rows; the padded count; the mass form; the kernel-equivalence proof; the gap mechanism and its ruled-out artefacts; the rescaling rule and its checks; the term IR and its compilation; the cost proof (matchings → H) | §5.3–5.8 |
| H | Systems and the nonlinear route in full | **(new opening, `app:systems`)** the system rows in both forms and the padding; ratio rows and their three-term circuit; the coupling as matchings by edge colouring; realification and its kernel equivalence; the real embedding of the Fourier variables; **then** the doubled-space algebra and kernel; the Carleman lift (symmetric and tensor layouts, the level scale, the tensor layout's complex weights); space–time forms; the folds (α = 2 within 1.21 of ‖𝕟₁‖₂); Fourier–Galerkin F₁ and F₂ for Burgers and Navier–Stokes; R9 and R10's panels | Ch. 6, Ch. 7 |
| I | Verification protocol | modes, sizes and tolerances; structured probes; per-term residuals; `eigh` against SVD (A-3); the iterative reference and its checks against the dense SVD; the T1 memory and time model; acceptance and the error budget | §8.3, §8.6 |
| J | Benchmark catalogue | R1–R10: equations, references, constraints, n-grids, parameters; a per-problem results table (both forms, tiers) | §8.2, §9.4 |
| K | Reproduction record | all 16 panels; the Fig. 5 triage; the non-reproductions; the paper's claims A-01–A-13 with verdicts; the tau-truncation ablation | §4.2, §4.3, §9.1 |
| L | Software and reproducibility | `pihm`'s architecture; records, provenance and the source digest; campaigns and Setonix; tests; regenerating every figure and number; environment pins | §8.9 |
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
| F1 | model configuration (the pipeline) | §8.1 | TikZ | n/a |
| F2 | the GQSP circuit (optional) | §8.5 | quantikz | n/a |
| F3 | U_odd's SELECT (subtraction with borrow) | §4.4 | quantikz | n/a |
| F4 | sparsity of A_std against A_desc | §5.1 | `pipeline.solutions` structure view | exact |
| F5 | the descriptor's flat LCU | §5.7 | quantikz | n/a |
| F6 | panels as printed against the problem (Fig. 5) | §9.1 | nb 11 | classical |
| F7 | verification accuracy against n | §9.2 | nb 20 | exact/probe/IR |
| F8 | decoded field with its error budget | §9.2 | nb 32 | T1/T2 |
| F9 | **headline:** looseness, relative gap and degree against N, three encodings | §9.3 | nb 40 | T2 + T3 |
| F10 | the forms head to head, as built and at α = ‖R‖ (optional) | §9.3 | nb 41 | T3 |
| F11 | the gap and γ², unscaled against rescaled | §9.4 | nb 42 | classical |
| F12 | three representative problems, both forms | §9.4 | nb 43 | classical + T2/T3 |
| F13 | the lift's convergence against a/ν (R9), with R8's surface | §9.5 | nb 61, 62 | classical + T2 |
| F14 | Navier–Stokes: vorticity and the degree pairs | §9.6 | nb 70 | T2 + T3 |

**Body tables:** T1 approaches (§2.2); T2 constraint kinds (§8.2); T3 benchmark ladder (§8.2); T4
verification modes and acceptance (§8.6); T5 descriptor block rows (§5.3); T6 η_e reproduction
(§9.1); **T7 the headline three-encoding table (§9.3)**; T8 preparation versus projection (§7.6); T9
applicability map (§10.4); **T10 deviations from the published method (§4.3, `tab:deviations`, new
in v2.1)**; and the two kept from the Ch. 4 draft, `tab:published-verdicts` (§4.2.2) and
`tab:alpha-G-short` (§4.4). Ch. 6 has no body table (R7's numbers go to §9.5).

**Captions** (style guide §3.4): a bold claim, then what is plotted, on which axes, for which
problem and parameters, then each panel, then the takeaway, then the tier. Figure captions below,
table captions above.

---

## 8. Notation

### 8.1 Master table (it becomes `1_header/6_notation.tex`)

| symbol | meaning | first use |
|---|---|---|
| n, N = 2ⁿ | qubits per Chebyshev axis; truncation dimension | §3.2 |
| k; p | equation order; polynomial degree of a nonlinearity | §3.3; Ch. 7 |
| τ(x), \|τ(x)⟩ | the paper's raw Chebyshev feature state | §3.2 |
| ψ, η, η_e | normalised coefficient state; scale; η_e = ‖b‖² | §3.2 |
| 𝔾 | differentiation (dense, strictly upper triangular; ‖𝔾‖₂ = Θ(N²)) | §3.3 |
| B̃, D̃ | banded factors, 𝔾 = B̃⁻¹D̃ | §5.2 |
| 𝕄_{x^p}, 𝕄_a | multiplication (lift; smooth coefficient) | §3.3 |
| 𝕟₁, 𝕟_x | product-to-sum folds | §3.5 |
| 𝔹(x), 𝔻⁽⁰⁾(x_s) | rank-one zero and collapse rows | §3.3 |
| x_z, x_m, x_s | constraint points (zero, extremum, regular datum) | §3.3 |
| A_std, A_desc; H_std, H_desc | residuals; Hamiltonians H = R†R | §3.3, §5.3 |
| R = [R_1; …; R_L]; σ₀, σ₁, σ_max | stacked residual; its singular values | §8.3–8.4 |
| w = (f̂⁽⁰⁾; …; f̂⁽ᵏ⁾); n_f | descriptor state (chain); block-register qubits | §5.3 |
| ζ | block-rescaling constant | §5.6 |
| α, α_R, α_H = α_R² | subnormalisations | §2.4, §8.4 |
| V, W, H′ = 2H/α_R² − I | reflection; walk; normalised Hamiltonian | §8.4 |
| Δ, γ | spectral gap λ₁ − λ₀; overlap \|⟨ψ_ref\|φ₀⟩\| | §2.6, §8.5 |
| d, ε | filter degree; target | §2.6 |
| x₀, x₁, w(·), θ₀ | ground value and edge of the excited spectrum on H′'s scale; the edge map; the minimax rate | §8.5 |
| β, q_k | imaginary time and its Chebyshev coefficients (the QITE filter) | §8.5 |
| p_G | the filter's success probability | §8.5 |
| K, M, ρ, s | Carleman order; modes; worst-case ratio; level scale | §7.3 |
| F₁, F₂, 𝔸_K | linear and quadratic terms; lifted generator | §7.3 |
| a, ν, T, n_t | amplitude, viscosity, horizon, time-axis qubits | §7.5 |
| C; z; 𝔸 | number of components of a system; its state (one block per component); its coupling matrix | §6.1 |
| 𝔽, y, y_a, y_⊥ | ratio row; the vector datum, its anchor component, its off-anchor part | §6.2 |
| w₀ | a system's stated initial data (weights the initial state) | §6.2, §8.5 |
| 𝕊_a(x*), ĝ | datum-slice row on axis a at x*; the datum function's coefficients | §4.3 |
| c = Re c + i Im c | a complex coefficient in the realification example | §6.5 |
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
| w (Planning's ratio row, off-anchor data) | w the descriptor's state; w(·) the edge map; w = u/s the lift's variable | **y_⊥** |
| a (a complex coefficient, realification) | a the amplitude (fluids); a_j the equation's coefficients; α subnormalisation | **c** |
| T10 (table) | T1–T3 tiers; T_k Chebyshev | a table label only, written "Table T10" in the plan and `\Cref{tab:deviations}` in the thesis |

---

## 9. Claims → thesis register

Status follows Planning §8 and `pihm/docs/18_claims.md`. **Register:** **A** = assert; **H** = assert
with the stated hedge or scope; **N** = narrative only; **X** = do not state. **Rule:** before a
claim ID is cited in prose, its row reads ✅ in the generated `18_claims.md` at `results-v1`; if not,
the prose is rewritten to what is supported.

| ID | claim, as the evidence states it | thesis | register |
|---|---|---|---|
| A-01 | 𝔾, 𝕄, 𝕟₁, 𝔹 match the printed SM §A | App C; §4.1 one line | A |
| A-02 | printed η_e, 11 ODE panels, within one unit of the last digit (9/11 when rounded) | §9.1 T6 (`eq:eta-e` derived in §4.1) | A |
| A-03/A-04 | Figs 6–7 η_e not reproduced, hypotheses tested | §9.1; App K | A |
| A-05 | the Laplace solution is a typo | §4.3 one clause; §9.1 footnote | A |
| A-06–A-08 | the published circuits' qubits, gates, prefactors and error | §4.2.2; App D | A per verdict |
| A-09 | H positive semi-definite where the discrete solution is exact; not always distinct at the bottom | §4.2 (argued); §9.1; App K | A (refined) |
| A-10 | doubled-space kernel ≥ 2^{2n−1} | §7.2; §9.5 | A |
| A-11 | the paper's time rule falls short of ε | §4.2 (the rule has no ε; companion 42); §9.1 (measured) | A (refuted) |
| A-12 | "poly(n) terms": true for gates, not for α | §3.6; §4.2 | A |
| A-13 | the printed n distorts 5a–5d | §4.3 (mechanism); §9.1 F6 (numbers) | A |
| B-01 | 𝔾 = B̃⁻¹D̃ | §5.2 | A |
| B-02 | exact kernels coincide; elsewhere both forms' fields converge alike | §5.3 | A (restated) |
| B-03 | "O(1) ancilla" | – | X → C-06 |
| B-04/B-05 | α/‖·‖ → 1 on regular one-axis panels; ~2 singular; 2.3–4.1 on PDEs | §5.8; T7 | H |
| B-06 | rescaled gap O(1) on one axis; still falls on two | §5.6; §9.4 | H |
| B-07 | relative gap, with the eigh/SVD distinction | §5.9 | A |
| B-08/B-09 | old query and gate scalings | – | X → C-05, §10.2 |
| B-10 | Neumann costs Θ(N²) more | – | X |
| B-12 | nodal fold exact at α = 2, within 1.21 of ‖𝕟₁‖₂ (tight, **not** optimal); DCT cited | §7.4 | A (v2.0's "optimal" withdrawn, Journal E087) |
| B-13 | the composed H verifiable only by parts | – | X: refuted, V verified exactly to 25 qubits |
| B-14 | one query's Haar-average success Θ(1) (descriptor) vs N⁻¹ per axis | §5.9 | H (compares encodings, not a pipeline cost) |
| B-16 | NLFT phases to high degree | App F | A |
| B-17 | minimax 1.67–1.92× fewer degrees at equal suppression; smaller and sometimes reversed at equal measured infidelity | §8.5; §9.2 | A (refined) |
| B-18 | Carleman: a unique kernel at every order; convergence follows a/ν, not ρ; trust misleads past it | §7.3; §9.5 | A (refined) |
| B-19 | tensor layout 2K − 1 terms, cost growing slowly with M; built on complex Fourier variables, verified, not prepared | §6.5; §7.4; §9.6 | A (refined) |
| B-20 | the descriptor avoids doubling for linear PDEs | – | X (neither form doubles) |
| B-21 | rescaling makes R2c reachable | §5.6; §9.4 | A (restated) |
| B-22 | only the descriptor prepares nonlinear solutions | – | X: refuted |
| B-23 | standard-form ground state unresolvable at n ≈ 7 | §5.9 | A (restated: eigh fails, SVD resolves) |
| B-24 | GQSP: any \|P\| ≤ 1, no parity | §2.5; §8.5 | A |
| B-25 | ⟨τ(x)\| an LCU of two product states, plus the constant mode | App F | A if used |
| C-01 | exact structured 𝔾; n + 4 ancilla for 𝔾 alone | §4.4 | A |
| C-02 | α_H/‖H‖ bounded for constant coefficients; loose for R3's lifted multiplier | §4.5; T7 | H |
| C-03 | the stacked reflection's identities | §8.4 | A |
| C-04 | Σ\|q_k\| = 1; the circuit equals T2 before normalising | §8.5 | A |
| C-05 | degree Θ̃(N^{2k}) (standard, best encoding) vs Θ̃(N) (descriptor, regular one-axis); ~Θ̃(N²)+ where the leading coefficient vanishes or on two axes | §5.9; §9.3 F9 | H (measured exponents with fit ranges) |
| C-06 | ⌈log₂(n+4)⌉ + 8 ancilla for R2's system rows | §5.8 | A |
| C-07 | the ODE reproduction; Figs 6–7 documented | §4.1–4.2 (what is checked); §9.1 | A |
| C-08 | T2 = T1 ≤ 1e-10 | §8.6; §9.2 | A for minimax records; the QITE reproduction's misses reported (plan §2.1 open item) |
| C-09 | Carleman: a one-dimensional kernel in both forms; the descriptor's time axis lowers the degree from n_t = 4 | §7.3; §9.5 | A |
| C-10 | NS: the descriptor's time axis lowers the degree in all pairs at fixed K; the ratio narrows with the modes | §9.6 | A |
| new | the readout identity for p_G < 1 | §4.2 (stated); §8.7; App F | A (one sentence) |
| new | reversals at the ideal bound (R3) and on the heat panel at small n | §9.3–9.4 | A (negative finding) |
| new | per-query gates higher in the descriptor at small n | §5.8; T7 | A |
| new (v2.1) | η > 0 is a sign convention; the decoded field carries the sign | §4.2 | N |
| new (v2.1) | an order-k ODE needs k − 1 independent invariant constraints and one regular datum | §4.2 | A (lemma, ODEs only) |
| new (v2.1) | each printed choice alone floors the error; only both removed converge (Fig. 5 triage) | §4.3 (mechanism); §9.1 | A |
| new (v2.1) | the R3c/R3d substitution leaves simple zeros and converges spectrally | §4.3; App K | A |
| new (v2.1) | the stacked residual's H equals the paper's Gram sum | §4.3 | A (identity) |
| new (v2.1) | a system's two forms share state, initial state and readout, and one kernel | §6.1, §6.3 | A (theorem in §5.3) |
| new (v2.1) | R7: the mass form's gap ≈ 2.1× the block-rescaled chain's, flat in n | §6.3; §9.5 | A, once a `\res` key exists (plan §2.1) |
| new (v2.1) | matchings: fewer terms and smaller α than Pauli words for 𝔸 | §6.4 | A, once keyed |
| new (v2.1) | a complex R gives a Hermitian PSD H; no non-Hermitian filter is needed | §6.5 | N (mathematical; no complex-R preparation run) |
| new (v2.1) | R7 is the realification of z′ = −iπz | §6.5 | N (identity) |
| new (v2.1) | complex-valued fields are prepared | – | **X**: realification only; native complex preparation not built (T-32) |
| B-18 (wording) | "past a/ν ≈ 5 the lift diverges" | – | **X** as worded: converges at a/ν = 3, diverges at 10; 5 is an extrapolation (Journal E087) |

---

## 10. Code → thesis transfer

### 10.1 Sources of truth

1. **Results:** P8's records, the commit tagged `results-v1`, read only through the exporter and the
   notebooks. Nothing from legacy `Setonix/`, legacy notebooks or the old `docs/`.
2. **The method:** `pihm/docs/02_methods.md`, the method as built. Where it and Planning.md differ,
   02_methods.md and the tests win.
3. **Reasons:** Planning.md, `pihm/docs/20_decisions.md` and `21_decision_log.md` explain why; they are never cited. The
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
| `variant="faithful"` vs the bare problem | R2a as printed (§4.1–4.3, §9.1, App K) vs R2a |
| `assemble.systems`, components, `monomials` | a system; its components (Ch. 6) |
| `ratio_rows`, `"ratio"` constraint | ratio rows |
| `matching_terms`, decision 42 | the coupling as a sum of matchings |
| `layout="chain"` on a first-order system | the chain ablation (labelled; Ch. 6, §9.5) |
| `real_embedding`, `fourier_field` | the real (cos/sin) basis; the complex Fourier variables (§6.5) |
| `NotImplementedError` for complex data | native complex data not built (§6.5) |
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
| **W0b** ✅ | v2.0 | the scaffold migration; the REVISE sweep (plan §2.1); the `ref.bib` audit and additions (T-29, plan §5.2) | files renamed to v2.0's names; the `ref.bib` audit's status is tracked in §0.4 |
| **W0c** | v2.1 | the eleven-chapter migration (plan §4.3): renames, `6_systems.tex`, Chapter 4's restructure, the moves into Ch. 6, Ch. 3's pointers, Table T10's shell | before drafting Chs 4 and 6 |
| **W1** | now (Ch. 3 drafted 2026-10-07) | Ch. 2; Ch. 4 (§4.1, §4.2.1, §4.3 new; §4.2.2, §4.4, §4.5 from the draft); Ch. 5; Ch. 6; Ch. 7; Ch. 8; Appendices A–I | maths and method; numbers render as their placeholders |
| **W2** | P8 copied back; exporter rerun | Ch. 9 in order §9.1 → §9.6; Appendices J, K, L; then every `\res` in Chs 4–8 checked | the numbers freeze |
| **W3** | W2 | §9.7; Ch. 10 | check §9.7's findings against P8 first (TR-1) |
| **W4** | W3 | Ch. 1; Abstract; Ch. 11; Summary of Student Achievement; App M; the title (T-14) | written last, so they promise only what was delivered |
| **W5** | W4 | Verification Mode; Review Mode per chapter; page count; §14; the supervisor's draft (guideline 9) | |

**Supervisor touchpoints (guideline 9: "a general layout for approval, then drafts").** Send §0.1,
plan §0.3 and §3.1–3.2 now as the layout for approval, then drafts after W1 (Chs 2–5) and W4 (the full
draft).

---

## 12. Risks and fallbacks (the rubric protects well-analysed negative results)

| id | risk | likelihood | response in the thesis |
|---|---|---|---|
| TR-1 | P8's records move a finding (an exponent, a ratio, a reversal) relative to the pre-P8 values this plan quotes | medium | the text is written from claims and `\res`; before W3, re-read §9.7's findings and Table T9 against P8 and rewrite what moved |
| TR-2 | fitted degree exponents deviate from 2k and 1 | low–medium | report the measured exponents with their fit ranges; restate C-05 as measured |
| TR-3 | "no encoding beats Θ̃(N^{2k})" over-generalises | medium | claim it for polynomial filters of the walk, which need degree Ω(√(α_H/Δ)); a general lower bound is future work |
| TR-4 | circuit simulation only at small n | certain | designed for: T2 ≡ T1 proven and measured; said once in §8.6 |
| TR-5 | "isn't this ultraspherical, or FOSLS?" | high | credited first (T-26), with the increment stated in §2.3 and §5.1 |
| TR-6 | the concurrent sibling (Paine 2026) is read as pre-empting | low | cite it in §2.2 and §3.6 with what it does and does not do; it proposes alternative constructions and encodings but has no gap scaling in resolution, no circuits and no banded reformulation (read in full 2026-10-04) |
| TR-7 | a marker reads the reversals (R3 at the ideal bound; the heat panel) as weakness | medium | they are numbered findings with their mechanism, and Table T9 turns them into guidance |
| TR-8 | the known-edge assumption is attacked | medium | own it in §8.5 and §10.6; on-circuit edge estimation is future work item 1 |
| TR-9 | page overrun | medium | plan §4.1's trim order |
| TR-10 | the marker ticks Theoretical | low | the formulation chapters already read as journal methods; move 2 pp from Ch. 9 into Chs 4–5 |
| TR-11 | bibliography errors (wu2025pihm's authors) reach submission | certain unless fixed | T-29 at W0b; §14.2 item 1 |
| TR-12 | Figs 6–7 stay unexplained | certain | recorded as not reproduced, hypotheses tested, authors not contacted (Planning decision 17) |
| TR-13 | Ch. 4's passage reads as a changelog of fixes (code-map drift, Formulation marks) | medium | §3.5 rule 7; every T10 row a defect and a property; Review Mode checks §4.3 for "we then", dates, issue numbers |
| TR-14 | the complex-valued material is read as an overclaim | medium | T-32's scope stated in §6.5's first paragraph; the X row of §9; T9 marks it "formulation only"; no complex number in the Abstract |
| TR-15 | the eleven-chapter body overruns (58 planned, Ch. 3 already long) | medium–high | §4.1's trim order, now live; the Review Mode page estimate per chapter at W5 |
| TR-16 | the audit is stated three times (Ch. 3, Ch. 4, §9.1) | medium | T-30's division of labour: Ch. 3 names, Ch. 4 derives, §9.1 shows numbers; Verification Mode checks it |
| TR-17 | the mass form is defined twice (§5.3 and Ch. 6) | low | §5.3 defines and proves; Ch. 6 applies and cites |

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
4. How it is verified (T1 = T2 ≤ 1e-10) and how far it reaches (coupled systems and Carleman in both
   forms; 2-D Navier–Stokes on up to 80 modes). No complex-valued claim in the Abstract (TR-14).
5. The scope: classical computation, no hardware, neither form poly-log.

### 13.3 Summary of Student Achievement (one page, first person, required)

What *you* did: the audit of the legacy pipeline and the decision to rebuild; `pihm`'s design; the
reproduction and its triage; the structured encoding; the descriptor reformulation, its gap
investigation and the rescaling rule; the verification framework and the GQSP circuit engine; the
filter study; coupled systems and their circuits; the Carleman and Navier–Stokes extensions; the Setonix production; the thesis. Name
the help received: the supervisor; AI coding assistance, if the School's policy requires it to be
declared (check it, and mirror it in the Acknowledgements, guideline 8).

### 13.4 Research proposal deviations (Appendix M)

| proposed (May 2025) | outcome | why |
|---|---|---|
| QSVT → a generalised QSVT for complex-valued, non-Hermitian operators | GQSP throughout (no parity constraint); the filter only ever acts on the Hermitian H = R†R, so no non-Hermitian filter is needed; complex-valued linear equations carried by realification as coupled real systems (Ch. 6, R7), one native complex encoding verified (the tensor layout), native complex preparation not built | the cost analysis showed the binding constraint is the Hamiltonian's norm and gap, which had to be solved first; realification reused the systems machinery at no new cost |
| nonlinear PDEs (Burgers, NLS, Ginzburg–Landau) | Burgers and 2-D Navier–Stokes by Carleman; NLS and CGL not treated | the doubled space cannot prepare; the Carleman lift needs dissipation (NLS is not dissipative) |
| data-informed Hamiltonians | not pursued | scope; future work |
| (not proposed) | the exact reproduction and the passage to the standard form; the structured encoding; the descriptor reformulation; coupled systems in both forms; the verification framework | emerged from auditing the published method |

### 13.5 Formal requirements from the guidelines

12 pt; 1.5–2 cm margins; body 40–60 pages excluding contents, proposal and appendices; one-page
Summary of Student Achievement in the first person; the proposal as an appendix with deviations
noted; the supervisor's electronic signature; the signed declaration; help received acknowledged.
The seminar (25 minutes plus questions) is outside the document; F0 or F1, F9 and T7 carry it.

---

## 14. Pre-submission checklist

### 14.1 Content

1. Every §1.3 contribution has a verdict in §11.1 and evidence in Ch. 9.
2. Every Abstract number has a `\res` key and a Ch. 9 location.
3. Every claim ID cited in prose is ✅ in `18_claims.md` at `results-v1` (§9).
4. `grep` finds none of: "collocation" naming the paper's regime; "O(1) ancilla"; "+ 6" ancilla; "Θ̃(N²) floor"; "not
   verified end to end"; "corrected" anywhere in prose; "as printed" outside §4.1–4.3, §9.1 and
   Appendix K; "warm start"; "K^2 terms"; "Pillar"; "rung"; QITE as the comparison's filter;
   "prepared" beside the doubled space or the tensor layout; the readout protocol "reproduced" as the
   method's readout; "optimal" for the nodal fold; "a/ν ≈ 5" as a measured boundary; a complex-valued
   field "prepared" or "solved"; "we fixed" or an issue number in §4.3; a typed `pihm` number.
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
8. "Published" sweep (deferred to the final pass): `wu2025pihm` is a pre-print, so no visible
   prose, caption, table cell or section title may call it, its encoding, prefactor or claims
   "published" (use "the paper's", "as printed" where §3.4 allows). Grep `published` over
   `1_header 2_body 3_footer`; labels and keys (`sec:standard-published`,
   `tab:published-verdicts`, `app:published-build`, `eq:pihm-published-prefactor`) do not render
   and may stay, and genuinely published works (Olver & Townsend 2013, Cai et al. 1994) are
   exempt. Includes the ThesisPlanning/scaffold comments only if they are copied into prose.

### 14.3 Rubric traceability (Modelling)

| criterion | marks | earned in | done |
|---|---|---|---|
| Intro & Lit: history and state of the art | /20 | Ch. 2 (§2.2 history), Ch. 3 | ☐ |
| — critical assessment (HD gate) | | §2.2(e) T1, **§3.6** | ☐ |
| — connection to the project | | §1.2, §3.6's three questions → Chs 4, 5, 7 (Ch. 6 as Q(iii)'s prerequisite) | ☐ |
| Model formulation | /30 | Chs 4–8 | ☐ |
| — software tools | | §8.9, App L | ☐ |
| — model configuration diagram | | F1 (§8.1) | ☐ |
| — input options (boundary conditions etc.) | | §8.2 T2, T3; App J | ☐ |
| — reproducible ("create equivalent models") | | Chs 4–8 + App B–I; `def:standard-form` and T10 (§4.3) | ☐ |
| — design of the numerical experiment | | §8.8 (fairness, conventions), §8.6 | ☐ |
| Results & Discussion | /30 | Chs 9–10 | ☐ |
| — self-contained results | | Ch. 9 + App J–K | ☐ |
| — significance for the field | | §10.1–10.5 | ☐ |
| — negative results analysed | | §9.4, §9.5, §9.7, §10.6 | ☐ |
| Conclusions & further investigation | /10 | Ch. 11 | ☐ |
| Style & presentation | /10 | throughout | ☐ |

---

*Companion documents: `CLAUDE.md` (the working agreement and Standing Facts v4),
`thesis_guides/STRUCTURE_AND_RUBRIC.md` (the rubric and exemplar reference),
`thesis_guides/STYLE_GUIDE.md` (register), `0_results/README.md` (quoting numbers),
`Code/pihm/docs/02_methods.md` (the method as built), `Code/Planning.md` (what was built and why).*
