# ThesisPlanning.md: the thesis structure, built on Planning.md

## Turning the `pihm` rebuild into a submittable (and publishable) Master's thesis

*Version 1.1, 2026-09-25. **Adopted.** Version 1 was a plan for review; the same day you
accepted every recommendation (T-05 to T-15, §1.2), and wave W0 was carried out: the working
state was committed as snapshot `2cd640c`, §2's changes were applied to `CLAUDE.md` and
`thesis_guides/`, and the LaTeX was scaffolded to §4.2 (conventions in §4.3). Decisions T-16 to
T-19 arose while scaffolding. The plan supersedes parts of `CLAUDE.md` (the Standing Facts) and
of `thesis_guides/STRUCTURE_AND_RUBRIC.md` (the section tree, page budget and appendix map);
`thesis_guides/STYLE_GUIDE.md` stays in force except where §2.3 notes an update.*

**Premise.** Everything in `Code/Planning.md` (version 2, amended through decision 20) is built and
pans out: gates G0–G6 pass, tag `results-v1` exists, and the claims register (Planning §8) resolves
as planned. Where an outcome is genuinely uncertain, §12 gives the fallback. Numbers quoted here
are planning-stage values (Planning Appendix A, Journal E001–E024). The thesis cites only
`results-v1` values (§10.2).

**How to read this.**

- §0 is the one-page version: the thesis in a paragraph, the chapter map and the status board.
- §1 is the decision record: your answers of 2026-09-25, plus the decisions this plan proposes for
  you to confirm.
- §2 reconciles this plan with the existing thesis guides: what stays, what is restated and what
  retires.
- §3 fixes the contributions, the spine sentence and the vocabulary.
- §4 gives the page budget and the LaTeX tree. §5 goes chapter by chapter. It is the part you
  follow while writing.
- §6 covers the appendices, §7 the figures and tables, and §8 notation.
- §9 is the claims-to-thesis traceability register.
- §10 is the code-to-thesis transfer protocol, §11 the writing order by dependency, and §12 the
  risks and fallbacks.
- §13 covers the front matter and §14 the pre-submission checklist.

---

## 0. Summary

### 0.1 The thesis in one paragraph

Wu et al. (arXiv:2504.13174, `wu2025pihm`) encode a differential equation's Chebyshev-coefficient
solution as the ground state of a physics-informed effective Hamiltonian, and prepare it by
imaginary-time filtering. This thesis does four things with that method:

1. **Reproduces** it exactly: the printed η_e of all eleven ODE panels agree to within one unit of
   the last digit. Where it does not reproduce (Figs 6–7), the thesis records that.
2. **Removes the encoder confound.** It builds the best exact encoding of the paper's own
   *standard form*. The factorisation 𝔾 = R₀(2U_odd)Λ has α_G ≤ 2.12‖𝔾‖₂ and O(n²) gates, against
   2.2×10⁶ × ‖𝔾‖₂ for the published normalisation at n = 7. With the encoder no longer at fault, the
   standard form's cost is shown to lie in its **Hamiltonian**: ‖H‖ = Θ(N⁸) with a flat gap, so the
   GQSP-QITE degree is Θ̃(N⁴).
3. **Introduces the descriptor reformulation**, the headline contribution. Carrying the
   intermediate derivatives as unknowns, tied by the banded pair (B̃, D̃), makes the residual banded.
   This gives:
   - ‖H‖ = Θ(N²);
   - a flat LCU with α_A → ‖A_desc‖;
   - ⌈log₂(n+4)⌉ + 6 ancilla (for R2's family, second-order ODEs);
   - degree Θ̃(N);
   - exactly the same kernel.
4. **Verifies the whole stack in two pillars.** Pillar 1 checks the gate-level operators in exact,
   probe and IR modes. Pillar 2 runs GQSP-QITE in three tiers: circuit simulation, an exact
   polynomial emulation provably equal to it, and resource estimates. The runs use
   answer-independent initial states and a priori parameters. The same pipeline then extends to
   polynomial nonlinearity. Carleman linearisation gives a genuine preparation claim for
   dissipative IVPs in **both** forms, and the thesis culminates in 2-D incompressible
   Navier–Stokes. The doubled-space route of the paper is shown to project, not prepare.

### 0.2 What changes from the current thesis guides (the short version)

| topic | current guides (pre-rebuild) | this plan (from Planning.md) |
|---|---|---|
| the paper's regime | "collocation" | **standard form** (Planning decision 13) |
| contributions | exactly one (descriptor) | the descriptor as the **headline**, plus four numbered **supporting** contributions (§3.1) |
| rubric scale | undecided, written for both | **Modelling**: Formulation /30 + Results /30 |
| the cost story | an "encoding wall" (a dense 𝔾 is expensive to encode) | two walls. The **encoder wall** (the published α is ~N³ loose) is removed by our structured encoding. The **Hamiltonian wall** (‖H_std‖ = Θ(N⁸)) remains, and only the descriptor removes it |
| descriptor ancilla | "O(1), 9–10 flat" | **⌈log₂(n+4)⌉ + 6 = O(log n)** (B-03, decision 3) |
| query/degree claim | Θ̃(N²) vs Θ̃(N⁸) "floor for any encoding" | degree Θ(√(α_H/Δ) log 1/ε): **Θ̃(N) vs Θ̃(N⁴)** (B-08/B-09 ❌) |
| readout | "no measurement protocol implemented" | the paper's interferometric protocol is **reproduced on the circuit engine** (T1, with shots) at small n, with a correction for probabilistic preparation. Still no hardware |
| GQSP evidence | classical simulation, dim ≲ 2000, ideal `eigh` block encoding | three tiers: T1 is the real circuit, T2 is an exact emulation (T1 = T2 to ≤ 1e-10) and T3 is estimates. The walk is built from the Pillar-1 circuits, never from `eigh` |
| composed H | "not verified end to end" | the stacked-residual reflection V is **verified exactly** at small n (~14–20 qubits), and T1 checks the whole stack end to end where it fits |
| nonlinear preparation | "only the descriptor Carleman route prepares" | **Carleman prepares in both forms** (B-22). The descriptor's gain is the time-axis degree |
| FABLE | absent | absent (Planning decision 5) |
| legacy results (`Setonix/Results10+`, legacy notebooks) | quoted | **never cited** (V-11). Every number comes from `pihm` at `results-v1` |

### 0.3 Chapter map

| # | chapter | pp | rubric criterion | built from (Planning) | writable after |
|---|---|---|---|---|---|
| 1 | Introduction | 3.5 | Intro & Lit /20 | §0 | last (W6) |
| 2 | Background and Literature Review | 7.5 | Intro & Lit /20 | §3.7–3.8 (prior art only) | now (W1) |
| 3 | The Physics-Informed Effective Hamiltonian Method | 4 | Intro & Lit /20 (body-located; §5.3) | §3.1–3.3, §3.6, §7.6 | now (W1; G1 passed) |
| 4 | A Regime-Independent Quantum Pipeline | 6 | Formulation /30 | §3.5, §3.7 (composition), §3.8, §4, §6.2, §7, §10–11 | now (W1); numbers at G3 |
| 5 | The Standard Form, Encoded Exactly | 3.5 | Formulation /30 | §3.7, §6.3 | now (W1; P3 done) |
| 6 | The Descriptor Reformulation | 9.5 | Formulation /30 (the core) | §3.4, §6.4 | maths now; numbers at G4 |
| 7 | Polynomial Nonlinearity | 4 | Formulation /30 | §3.6, §5.3 (R6–R10), §6.5 | G5 |
| 8 | Numerical Study | 12 | Results /30 | §5, §6.6–6.7, §7.3–7.9, App A | chapter by chapter, G1→G6 |
| 9 | Discussion | 4.5 | Results /30 | §3.9, §13 | G6 |
| 10 | Conclusions and Future Work | 2.5 | Conclusions /10 | n/a | last (W6) |
| | **Total body** | **57** | | | |

Hard cap 60 pages (the guidelines penalise overrun). Target 55–58. Appendices A–M are uncapped
(§6).

### 0.4 Status board (update as you go)

Columns: **S** = scaffolded (headings and comment scaffold in the `.tex`), **D** = drafted, **N** =
numbers frozen to `results-v1`, **R** = reviewed (Review Mode, `CLAUDE.md`), **F** = final.

| chapter / item | S | D | N | R | F | notes |
|---|---|---|---|---|---|---|
| Front matter (title, declaration, achievement, abstract) | ☑ | ☐ | ☐ | ☐ | ☐ | §13; notation table and glossary built |
| 1 Introduction | ☑ | ☐ | ☐ | ☐ | ☐ | |
| 2 Background and Literature Review | ☑ | ☐ | n/a | ☐ | ☐ | §2.1 drafted (QC preliminaries), to compress |
| 3 PIHM (prior art) | ☑ | ☐ | ☐ | ☐ | ☐ | prior-art paragraphs kept, with REVISE flags |
| 4 Pipeline | ☑ | ☐ | ☐ | ☐ | ☐ | new chapter |
| 5 Standard form, exact | ☑ | ☐ | ☐ | ☐ | ☐ | new chapter |
| 6 Descriptor | ☑ | ☐ | ☐ | ☐ | ☐ | construction prose kept (§6.2–6.3) |
| 7 Nonlinearity | ☑ | ☐ | ☐ | ☐ | ☐ | |
| 8 Numerical Study | ☑ | ☐ | ☐ | ☐ | ☐ | T6, T7 filled with `\prov` values |
| 9 Discussion | ☑ | ☐ | ☐ | ☐ | ☐ | |
| 10 Conclusions | ☑ | ☐ | ☐ | ☐ | ☐ | |
| Appendices A–M | ☑ | ☐ | ☐ | ☐ | ☐ | §6; B drafted, C and D partly; K tables `\prov` |
| Verification Mode pass | | | | ☐ | | §14 |

---

## 1. Decisions

### 1.1 Decided (your answers, 2026-09-25)

| # | question | decision | consequence |
|---|---|---|---|
| T-01 | contribution framing | **descriptor as the headline, plus numbered supporting contributions** | §3.1; `CLAUDE.md`'s "one contribution" lock is restated (§2.1) |
| T-02 | rubric project type | **Modelling**: Model Formulation /30 + Results & Discussion /30 | Chapters 4–7 carry /30 and 8–9 carry /30. Software, model configuration and input options are named rubric requirements (§5.4) |
| T-03 | schedule | **no dates**; order the writing by dependency only | §11 |
| T-04 | publication | **thesis first**; mark paper-shaped material only where it falls out naturally | §3.4 is a light note, not a plan |

### 1.2 Decided 2026-09-25 (your acceptance of every recommendation)

T-14's recommendation was "keep the working title until wave W6, then choose from §13.1".

| # | question | decision | why |
|---|---|---|---|
| T-05 | chapter structure | **ten chapters**, with a separate *pipeline* chapter (4) and a *standard-form exact* chapter (5) ahead of the descriptor (6) | Planning makes the comparison "of Hamiltonians, not of encoders" (§0.2). The structure should show that: a shared pipeline, then two residuals plugged into it |
| T-06 | notation style for operators | **blackboard bold**, matching the paper and `pihm`'s Sphinx macros: 𝔾, B̃ as $\tilde{\mathbb B}$, D̃ as $\tilde{\mathbb D}$, 𝕄, 𝕟₁ | readers cross-check against Wu et al. The current thesis uses italic G, B̃, D̃; changing is mechanical |
| T-07 | regime subscripts | **H_std, A_std** and **H_desc, A_desc** everywhere; bare H or A only for regime-independent statements (Ch. 4) | ends the ambiguity the old guide flagged at every occurrence |
| T-08 | imaginary time symbol | **β** for imaginary time (filter e^{−β(1+x)}); τ(x) stays the paper's Chebyshev feature state | Planning uses τ for both; the thesis cannot (§8.2) |
| T-09 | Carleman ratio symbol | **ρ** for ‖u₀‖‖F₂‖/\|Re λ₁(F₁)\|; R stays the stacked residual | Planning uses R for both |
| T-10 | benchmark labels | keep **R1–R10** in tables, and call them *benchmark problems*. Never "rung", "pillar", "gate G3" or "tier T2" in body prose. Use *operator verification* and *state-preparation verification*, and *circuit simulation / exact emulation / resource estimate*, with (T1/T2/T3) in parentheses once | project-management vocabulary reads as a lab diary (Style Trap 6) |
| T-11 | the notation table | **stays in the front matter** (`1_header/6_notation.tex`), not as §2.9 | it already exists there. The rubric criterion only needs it to exist and be complete |
| T-12 | readout's status | **reproduction of prior art with a correction**: the paper's protocol, run on the circuit engine with shots at small n; the probabilistic-preparation identity is ours (Journal E024) | it is now built and measured, so "never implemented" would be false. It is still not hardware, and not a new protocol |
| T-13 | Chapter 3's register | **prior art, judged**, as in the current guide. All of *our* measurements of the paper live in Chapter 8 (§8.2) and in Chapters 4–5, never in Chapter 3's descriptive sections | keeps Trap 13 (authorship blur) closed |
| T-14 | title | keep the working title, or retitle to foreground the contribution (options in §13.1) | the current title names neither the descriptor nor the reproduction |
| T-15 | code→thesis numbers | **generated LaTeX macros** from `results-v1` (§10.2), with provisional values marked `\prov{}` until then. *Amended 2026-09-27:* built early as keyed lookups, `\res{<run>}{<metric>}`, exported whenever results change; a missing number renders its reason | one source of truth. Planning's freeze rule then covers the thesis too |

### 1.3 Decided while scaffolding (2026-09-25)

| # | question | decision | why |
|---|---|---|---|
| T-16 | the convention for 𝔾 | **𝔾 is the coefficient-space map f ↦ f′** (strictly upper triangular), as in Planning, `pihm` and the draft's own entry formula; the paper prints the same matrix as 𝔾ₙᵀ, said once in §3.3. The draft's Chapter 3 applied `G^\top` to ψ while defining G by upper-triangular entries, an internal inconsistency; the transposes were dropped, and Appendix C's worked example was transposed to match (checked against `pihm`) | one convention, matching the code |
| T-17 | how scaffold guidance appears | **LaTeX comments only** (your answer); placeholder figures, tables and equations render; provisional numbers render red via `\prov` | the PDF shows structure, not notes |
| T-18 | appendix files | **one file per appendix** under `3_footer/appendices/`, indexed by `appendices.tex`; the research proposal PDF copied to `3_footer/research_proposal.pdf` and included with `pdfpages` | mirrors the per-chapter body files |
| T-19 | further notation collisions found | the raw (unnormalised) Chebyshev basis takes the subscript **raw** (std now means the standard form); the block-rescaling constant is **ζ** (Planning's λ collides with eigenvalues); the published ladder's per-bit coefficient is **μ** (the draft's β collides with imaginary time); the condition number is written **cond(·)**, since κ is κ_read; the doubled-space Hamiltonian is **H_⊗**. Change any of these by editing one macro or line | each symbol means one thing |

---

## 2. Reconciliation with the existing thesis guides

The current `CLAUDE.md` and `thesis_guides/` were written against the legacy repository. Planning.md
§2.3 found that pipeline's results uncitable (V-01 to V-12), and §8.2 marks several of its claims ❌.
On adoption, the following changes are made in those files. **Applied 2026-09-25**: `CLAUDE.md`
now carries Standing Facts v2; `STRUCTURE_AND_RUBRIC.md` carries "superseded by" banners at
each replaced section and records the Modelling decision; `STYLE_GUIDE.md` has the §2.3 edits
and a banner on its remaining pre-rebuild numbers.

### 2.1 `CLAUDE.md` Standing Facts: proposed version 2

| # | current Standing Fact | verdict | proposed replacement | Planning source |
|---|---|---|---|---|
| SF-1 | one contribution, the descriptor; PIHM prior art; the collocation encoding is the published route's weakness, reproduced in §5.2; FABLE nowhere | **restate** | The headline contribution is the descriptor reformulation. There are four supporting contributions (§3.1). The PIHM framework is prior art, presented and judged in Ch. 3. The paper's regime is the *standard form*. Its published encoding and our structured exact encoding are both measured, and the structured one is ours. FABLE appears nowhere | decisions 5, 13; C-01, C-02 |
| SF-2 | no measurement protocol is implemented; every error is a classical state-vector read | **restate** | The paper's interferometric readout is reproduced by circuit simulation at small n (R1, R2a, R5), with shot sampling. Every other reported error is computed from the simulated or emulated state vector. Nothing has run on hardware | §7.6; decision 20; E024 |
| SF-3 | all GQSP results are classical simulations capped at dim ≲ 2000 by simulation cost | **restate** | All results are classical. Circuit simulation (T1) reaches about 20–22 qubits. Exact emulation (T2) is provably equal to the circuit's post-selected output and reaches dimensions of 10⁶–10⁷. Beyond that, only resource estimates (T3) are quoted. Always say which tier a number comes from. "Could not simulate" is never "cannot reach" | §7.1–7.5 |
| SF-4 | composed H not verified end to end; atoms to 1e-9–1e-11, composition to < 1e-10 | **retire** | The stacked-residual reflection V (which encodes 2H/α_R² − I) is verified **exactly** at small n. Larger n is verified by probe (≲ 30 qubits) and IR (any n). T1 = T2 end to end where both run. State the tolerances of §6.2 | B-13; §6.2 |
| SF-5 | neither regime is poly-log; α_H ≥ ‖H_sys‖ = Θ(N²) against Δ = Θ(1) forces Θ̃(N²) queries; descriptor meets the floor, collocation misses it by ≈ N⁶ | **restate** | Neither form is poly-log. The GQSP-QITE degree is d = Θ(√(α_H/Δ) log 1/ε), with α_H ≥ ‖H‖ for any block encoding. Descriptor: ‖H_desc‖ = Θ(N²), α_H/‖H‖ → 1, **d = Θ̃(N)**. Standard form: ‖H_std‖ = Θ(N⁸), so **d = Θ̃(N⁴) even with the best exact encoding**; the published normalisation makes it about N¹⁰. The gap Δ is problem-dependent (0.454 flat for {1,4,4}; 7.5e-6 for {1,5,400} unrescaled) | B-08, B-09 ❌; C-05; §3.9 |
| SF-6 | the descriptor basis change is the discrete shadow of the ultraspherical method (Olver & Townsend 2013); credit it | **keep** | unchanged | §3.4; Appendix E docstring |
| SF-7 | doubled space projects; only Carleman (dissipative IVP, Re λ(F₁) < 0) prepares | **keep; extend** | …and Carleman prepares in **both** forms. The descriptor's time axis lowers the degree (C-09). The precondition is ρ < 1 | B-22; §3.6 |
| SF-8 | descriptor costs Hilbert space 2^⌈log₂(k+1)⌉·N vs N | **keep** | unchanged; also volunteer the derivative-block scaling (‖𝔾‖ = Θ(N²) dominates the norm) and its remedy, block rescaling at Θ(n_f) gates | §3.4 |
| SF-9 | (new) | **add** | The classical reference is the smallest right singular vector of the stacked residual R (SVD), never `eigh(RᵀR)`. The latter fails for the standard form beyond n ≈ 7 (1 − \|cos\| = 0.73 at n = 8) | V-07; D4 |
| SF-10 | (new) | **add** | Initial states are answer-independent (geometric product state; uniform and random as controls), and γ is always reported. τ (β) and d are fixed a priori from (α, Δ, γ, ε), with Δ assumed known, as is standard. The paper's own time rule is evaluated as a variant | V-01, V-02; §7.2 |
| SF-11 | (new) | **add** | The descriptor ancilla count is ⌈log₂(n+4)⌉ + 6 (R2's second-order family), i.e. O(log n), not O(1). Exact LCU needs Ω(log L) ancilla (Chakraborty et al.) | B-03 |

**Terminology rules in `CLAUDE.md`** (Verification Mode) change from "descriptor vs collocation" to:
"standard form vs descriptor form", "prepared vs projected", "verified (mode) vs emulated vs
estimated", "paper-faithful vs corrected variant". **Also add to the symbol list:** β, ρ, γ, d,
α_R, α_H, H′, η_e, and n_f.

### 2.2 `STRUCTURE_AND_RUBRIC.md`: what changes

| section | change |
|---|---|
| §0 framing | replaced by §3.1 of this plan (headline plus supporting contributions) |
| §1 mark sheet | keep. **§2 project type:** resolved as Modelling (T-02). Delete the "write for both" hedge and replace it with §5.4's Modelling mapping |
| §2.1 page budget | replaced by §4.1 |
| §3 LaTeX tree | replaced by §4.2 (ten chapters) |
| §3.2 appendices | replaced by §6 (A–M) |
| §4 per-section checklists | replaced by §5. The generic checklists (Style & Presentation, pre-submission sweep) carry over into §14 |
| §5 traceability matrix | replaced by §9 and §14.3 |

### 2.3 `STYLE_GUIDE.md`: targeted updates (the guide otherwise stands)

- **§1.1 register table.** Replace these rows with SF-3 to SF-5 and SF-11: "O(1) ancilla", "gap
  ~1e-6 vs ~1e-15", "composed H hedged", "never assert prepared", "Θ̃(N²) floor" and "never
  read out". Keep "assert measured, hedge inferred", and keep "attribute, then judge" for Wu et al.
- **§3.5 comparison tables.** The encoding table gets **three rows**: published standard form,
  structured standard form (ours) and descriptor. The old "two rows, not three" rule existed to
  exclude FABLE, which stays excluded.
- **§4.1 gap statement.** Three questions, not two (§5.3).
- **§4.4 spine sentence.** Updated in §3.2.
- **Trap 14** ("presenting the published route as a rival you also built") is refined. Our
  structured standard-form encoding *is* ours and is claimed (S2), but as a fairness device for the
  headline comparison, not as a rival method. The published route is still reproduced, not rivalled.
- **Trap 16** ("implying readout was performed") becomes "implying readout was performed **on
  hardware**, or that it is a new protocol".

### 2.4 Existing `.tex` content: salvage map

| file | status | keep | rework or remove |
|---|---|---|---|
| `2_body/1_introduction.tex` | headings only | n/a | re-head per §4.2 |
| `2_body/2_literature.tex` | §2.1 drafted (definitions); rest empty | the definition blocks for objects reused later (block encoding; state space if referenced) | compress §2.1 to ≤ 2 pp; fix the stray `` `' ``, "initialized" → "initialised"; the `\todo`s; add the missing families (§5.2) |
| `2_body/3_pihm_collocation.tex` | substantially drafted | §3.2's residual paragraphs (feature map, 𝔾, the DE row, data constraints, the nonlinear extension) are sound prior-art description; the attribution discipline | **remove:** the "reconstructed encoding circuit" with its adder and n + 4 ancilla (that is the *legacy approximate* 𝔾, superseded by the Fig. 9 build, B-15); "composed H is not verified end to end" (SF-4); the α_H Θ(N⁸) "against ‖H‖ = Θ(N²)" conflation; the Θ̃(N²) floor (SF-5). **Move** all of *our* measurements to Ch. 8 (T-13). Rename the file to `3_pihm.tex` |
| `2_body/4_descriptor.tex` | partly drafted (construction, recurrence rows) | the construction paragraphs, the first-order example | "Cost" paragraph against SF-11; design rationale per §5.6; rename to `6_descriptor.tex` |
| `2_body/5_nonlinear.tex` … `8_conclusions.tex` | headings only | n/a | re-head per §4.2 |
| `3_footer/appendices.tex` B | drafted: recurrence, normalised basis, ultraspherical connection, N = 4 instance, higher order | all of it, after the notation pass (T-06) | the "padded block count" subsection moves to Appendix G |
| appendices C | drafted: collocation residual worked example, M_{x^p} | the M_{x^p} lift material (it matches Planning §3.2) | re-label "collocation" → "standard form"; add the paper's printed SM §A n = 2 matrices as reproduced (A-01) |
| appendices D | drafted: ladder mechanism and the derived ε_G bound | **nothing as-is.** It describes the legacy reconstruction | replace with the Fig. 9 build and the *measured* ε_G(n) (A-07). Re-derive a bound only if one holds for the Fig. 9 circuit |
| appendices E–L | stubs | n/a | re-map per §6 |
| `1_header/2_acknowledgments.tex` | "Jingbo **Want**" | n/a | → "Wang" |
| `1_header/6_notation.tex` | small table | structure | rebuild per §8 |
| `main.tex` | `\nocite{*}`, stray `\todo` | n/a | remove both before submission; add chapters per §4.2 |

**Done in the W0 pass (2026-09-25).** Every "keep" above was kept, converted to the §8 macros
and T-16's convention; every "remove" is preserved in snapshot `2cd640c`, not deleted from
history. Kept prose that states a retired or wrong claim carries a `% REVISE:` comment beside it.
Findings flagged there, for you to fix while writing:

- **Appendix C, `M_{x^1}` is a factor √2 too small.** `pihm`, whose lifts reproduce the paper's
  printed SM §A entry by entry, gives `[[0,1],[1,0],[0,1/√2],[0,0]]`; `M_{x^2}` agrees.
- **Appendix C, worked example.** It is now upper triangular (T-16). Its sentences "triangular
  only because…" and "three orders of magnitude" are wrong: every polynomial in 𝔾 is upper
  triangular, and the largest off-diagonal entry (30) is about one order below 400.
- **Chapter 3, doubled space.** Ψ = ψ ⊗ ψ lives in an N²-dimensional space, not 2N.
- **Chapter 3, constant coefficients.** Under the lift a constant enters as a_j 𝕄₁ (2N × N), not
  a_j I.
- **Chapter 3, regular constraints.** `Only one such regular constraint…` should be reconciled
  with the source row 𝔻⁽⁰⁾(x_s) (eq. `eq:pihm-A-source`).
- **Chapter 7 (moved from the draft's §4).** Its last clause says "descriptor Hamiltonian" where
  it means the doubled-space one.
- **Appendix G, variable coefficients.** It describes the legacy monomial route; the rebuild uses
  the square Galerkin form (D-005).
- **Appendix D departs from the map above.** The ladder mechanism, the proposition and its proof
  were **kept**, because `pihm`'s `derivative_ladder_error_bound` states the same bound for the
  Fig. 9 build (the map's "re-derive only if one holds" condition is met). Its legacy resource
  paragraph and ε_G column were dropped; ‖𝔾‖_S was recomputed and matches.
- **`ref.bib` `note` fields print in the IEEE bibliography** (e.g. "SWITCH-test readout protocol
  specialised in readout.py"): internal repo notes are visible, and four of them overflow the
  margin. Either strip them or add `\AtEveryBibitem{\clearfield{note}}` (§14.2).
- `pihm`'s `nlfft2025su2` entry has no authors, so the inverse-NLFT citation is still CITE-NEEDED.

---

## 3. Contributions, spine and vocabulary

### 3.1 The contributions (these appear, numbered, in §1.3, and each gets a verdict in §10.1)

**Headline.**

> **C. The descriptor reformulation.** Carrying the k intermediate derivatives as unknowns, tied by
> the banded pair (B̃, D̃), turns the physics-informed residual from dense to banded, *with exactly
> the same kernel*. Its block encoding is one flat LCU with α_A → ‖A_desc‖, ⌈log₂(n+4)⌉ + 6 ancilla
> (for R2's family) and O(n²) gates. Its Hamiltonian has ‖H_desc‖ = Θ(N²), so the GQSP-QITE degree
> is Θ̃(N), against Θ̃(N⁴) for the standard form's best exact encoding. The price is the
> ⌈log₂(k+1)⌉-qubit block register, plus block rescaling where derivative norms dominate. *Evidence:*
> Ch. 6, §8.3–8.6; claims C-05, C-06, B-01, B-04, B-05.

**Supporting.**

> **S1. A verified reproduction and audit of Wu et al.** The paper is rebuilt exactly, including
> its printed constraint points and Maclaurin sources:
> - its printed η_e agree with the exact solution's ‖b‖² to within one unit of the last printed
>   digit on all 11 ODE panels (9/11 equal when rounded);
> - the three PDE and two nonlinear panels do not reproduce, and each is triaged with a
>   discriminating test;
> - its circuits (Figs 2, 8 and 9) are built and their claims tested;
> - its readout identity is corrected for probabilistic preparation.
>
> *Evidence:* §8.2, Appendix K; claims A-01 to A-13, C-07.

> **S2. An exact structured encoding of the standard form.** 𝔾 = R₀(2U_odd)Λ gives α_G = N(N−1)
> ≤ 2.12‖𝔾‖₂ with O(n²) gates and n + O(log n) ancilla, against α/‖𝔾‖₂ = 2.2×10⁶ for the published
> normalisation at n = 7. With α_H/‖H‖ bounded (≈ 60, Fig. 3b), this isolates the standard form's
> remaining cost in its Hamiltonian, not its encoder. *Evidence:* Ch. 5, §8.3; claims C-01, C-02.

> **S3. A regime-independent verified pipeline.** It has four parts:
> - a stacked-residual reflection V, a Hermitian unitary with Π V Π = 2H/α_R² − I and a
>   controlled-V needing only a controlled reflection;
> - GQSP-QITE with Σ|p_k| = 1 exactly;
> - a priori parameters and answer-independent initial states;
> - verification in three tiers, with the exact emulation proven, and measured, equal to the
>   circuit (≤ 1e-10).
>
> *Evidence:* Ch. 4, §8.4; claims C-03, C-04, C-08.

> **S4. Nonlinearity: preparation versus projection.** The paper's doubled space encodes exactly
> but has an O(dim)-degenerate kernel, so it only projects. The Carleman lift (ρ < 1, dissipative)
> gives a one-dimensional near-kernel, and hence a real preparation claim, in *both* forms. The
> descriptor's time axis lowers the degree. The pipeline culminates in 2-D incompressible
> Navier–Stokes (Fourier–Galerkin + Carleman + Chebyshev time), compared like for like across
> forms. *Evidence:* Ch. 7, §8.7–8.8; claims C-09, C-10, B-12, B-18, B-19.

**Rules for the list.** Each item is one sentence of *what* and one clause of *evidence*. The
headline is always listed first and always carries its cost (the block register). S2 is phrased as
serving the comparison ("isolates…"), never as a rival solver.

### 3.2 The spine sentence

> *Carrying the intermediate derivatives instead of eliminating them turns the physics-informed
> residual from dense to banded, so the Hamiltonian's norm falls from Θ(N⁸) to Θ(N²) with its kernel
> unchanged, and every stage from block encoding to state preparation inherits the saving.*

Place it, lightly reworded each time, in:

- the Abstract;
- the end of §1.3;
- the close of §3.6 (as the question it answers);
- §6.1;
- §6.9;
- §8.9;
- §10.1.

### 3.3 Controlled vocabulary

| use | never | note |
|---|---|---|
| standard form | collocation, "state-space" | the paper's regime (decision 13). "Constraint points" for x_z, x_m, x_s |
| descriptor form | "our method" (in isolation), "sparse method" | |
| structured (exact) encoding | "our standard-form method", "improved Wu" | S2, a fairness device |
| published encoding | FABLE, "dense encoding", "naive" | Wu et al.'s Figs 2, 8 and 9 |
| prepared | "found", "solved" (for QITE output) | only for a one-dimensional (near-)kernel |
| projected | "prepared" (for the doubled space) | R6 |
| verified (exact / probe / IR) | "checked", "tested", "passes" | name the mode and tolerance |
| circuit simulation (T1) | "run on a quantum computer", "executed" | Aer statevector |
| exact emulation (T2) | "simulated" | provably equal to T1's post-selected output |
| resource estimate (T3) | "predicted to work" | |
| paper-faithful / corrected variant | "wrong version / fixed version" | §3.5 of Planning |
| benchmark problem R1–R10 | rung, case N | T-10 |
| a priori parameters | "tuned", "chosen" | never against the answer |
| infeasible (with the estimate) | "failed", "too big" | Planning decision 20 |

### 3.4 Paper-shaped material (light note only, T-04)

If you later want a paper, it falls out as follows: Ch. 5 + Ch. 6 + §8.3–8.6 + §9.2 form a
self-contained "descriptor vs standard form, like for like" article, with the reproduction (S1) as
its baseline section. Nothing in the plan depends on this.

---

## 4. Page budget and LaTeX tree

### 4.1 Page budget (Modelling scale)

| chapter | pp | criterion | marks it serves |
|---|---|---|---|
| 1 Introduction | 3.5 | Intro & Lit | /20 |
| 2 Background and Literature Review | 7.5 | Intro & Lit | /20 |
| 3 The PIHM method (prior art, judged) | 4 | Intro & Lit (HD gate: critical assessment) | /20 |
| 4 A Regime-Independent Quantum Pipeline | 6 | Model Formulation | /30 |
| 5 The Standard Form, Encoded Exactly | 3.5 | Model Formulation | /30 |
| 6 The Descriptor Reformulation | 9.5 | Model Formulation (core) | /30 |
| 7 Polynomial Nonlinearity | 4 | Model Formulation | /30 |
| 8 Numerical Study | 12 | Results & Discussion | /30 |
| 9 Discussion | 4.5 | Results & Discussion | /30 |
| 10 Conclusions and Future Work | 2.5 | Conclusions | /10 |
| **total** | **57** | | |

**Why this split.** The Modelling scale gives Results & Discussion 30 marks, not the Theoretical
20, so Chapters 8–9 get 16.5 pages, up from the old guide's 14–15. Formulation (Chapters 4–7, 23
pages) must let a reader "create equivalent models" (the rubric's words). That is why the software,
the model configuration diagram and the input options have body space (§5.4), with the detail in
Appendices F, I, J and L. **The overrun order, if over budget:** trim §2.1 first, then §8.6 (move a
case to Appendix J), then §3.4, then §4.8. Chapter 6 is cut last.

### 4.2 LaTeX section tree (file names proposed; rename only on adoption)

```latex
% 2_body/1_introduction.tex  (~3.5 pp)
\section{Introduction}
  \subsection{Differential Equations as a Target for Quantum Computation}
  \subsection{Physics-Informed Hamiltonians and Where Their Cost Lies}
  \subsection{Contributions and Scope}                  % numbered: C, S1–S4; scope statement
  \subsection{Outline}

% 2_body/2_literature.tex  (~7.5 pp)
\section{Background and Literature Review}
  \subsection{Quantum Computation Preliminaries}         % <= 1.5–2 pp, hard cap
  \subsection{Quantum Algorithms for Differential Equations}
      \subsubsection{Linear-Systems and Linear-Combination Routes}
      \subsubsection{Nonlinear Equations: Carleman and Related Linearisations}
      \subsubsection{Variational and Ground-State Routes}
      \subsubsection{Critical Assessment}                % comparison table with a "this work" row
  \subsection{Spectral Methods and Banded Differentiation}
      \subsubsection{Chebyshev Series, Differentiation and Galerkin Truncation}
      \subsubsection{The Ultraspherical Spectral Method}  % credit Olver & Townsend here
      \subsubsection{Fourier--Galerkin Discretisation of Periodic Flows}
  \subsection{Block Encoding, Linear Combinations of Unitaries and Qubitisation}
  \subsection{Quantum Signal Processing and Its Generalisation}
  \subsection{Ground-State Preparation by Filtering}
  \subsection{Readout and Amplitude Amplification}
  \subsection{Synthesis}                                  % hands the reader to Ch. 3

% 2_body/3_pihm.tex  (~4 pp)  PRIOR ART, judged
\section{The Physics-Informed Effective Hamiltonian Method}
  \subsection{Overview}
  \subsection{The Latent Chebyshev Model}
  \subsection{The Residual, the Hamiltonian and Its Constraints}
  \subsection{The Published Circuits, Filter and Readout}
  \subsection{The Doubled-Space Extension to Nonlinearity}
  \subsection{Critical Assessment}                        % the pivot; poses three questions

% 2_body/4_pipeline.tex  (~6 pp)  MODEL FORMULATION
\section{A Regime-Independent Quantum Pipeline}
  \subsection{Overview and Model Configuration}          % the pipeline figure
  \subsection{Problem Specification and Model Inputs}
  \subsection{The Classical Reference}
  \subsection{From Stacked Residual to Quantum Walk}
  \subsection{GQSP Imaginary-Time Filtering with A Priori Parameters}
  \subsection{Reading Out the Solution}
  \subsection{Verification Framework and Error Budget}
  \subsection{Software and Computational Configuration}

% 2_body/5_standard.tex  (~3.5 pp)
\section{The Standard Form, Encoded Exactly}
  \subsection{The Published Encoding, Rebuilt}
  \subsection{An Exact Factorisation of the Differentiation Matrix}
  \subsection{Circuits and Cost}                          % proposition
  \subsection{What Remains: The Standard-Form Hamiltonian}

% 2_body/6_descriptor.tex  (~9.5 pp)  THE CORE
\section{The Descriptor Reformulation}
  \subsection{The Idea}                                   % dense vs banded figure
  \subsection{The Banded Factorisation}
  \subsection{The Descriptor Residual and Kernel Equivalence}   % theorem
  \subsection{Constraints, Partial Differential Equations and Coupled Fields}
  \subsection{Block Rescaling}
  \subsection{The Block Encoding: One Flat Linear Combination}  % figure + algorithm
  \subsection{Cost of the Descriptor Encoding}                  % proposition
  \subsection{Consequences for the Spectrum and the Filter}
  \subsection{Summary}

% 2_body/7_nonlinear.tex  (~4 pp)
\section{Polynomial Nonlinearity}
  \subsection{Two Regime-Independent Treatments}
  \subsection{The Doubled Space: Exact Encoding, Degenerate Kernel}
  \subsection{The Carleman Lift in Space--Time}
  \subsection{Product Folds on a Circuit}
  \subsection{Fourier--Galerkin Fluids: Burgers and Navier--Stokes}
  \subsection{Preparation Versus Projection}

% 2_body/8_results.tex  (~12 pp)
\section{Numerical Study}
  \subsection{Experimental Design and Cost Conventions}
  \subsection{Reproducing Wu et al.}
  \subsection{Operator Verification and Encoding Cost}
  \subsection{State Preparation and Readout}
  \subsection{Scaling: Where the Cost Lies}               % headline figure
  \subsection{Representative Problems}                    % three, in depth
  \subsection{Nonlinear Benchmarks}
  \subsection{Case Study: Two-Dimensional Navier--Stokes}
  \subsection{Summary of Findings}                        % numbered, >= 1 negative

% 2_body/9_discussion.tex  (~4.5 pp)
\section{Discussion}
  \subsection{Why the Descriptor Form Wins, and What It Costs}
  \subsection{End-to-End Complexity}
  \subsection{What the Reproduction Says About the Published Method}
  \subsection{Where the Construction Applies}
  \subsection{Feasibility on Fault-Tolerant Hardware}
  \subsection{Limitations}

% 2_body/10_conclusions.tex  (~2.5 pp)
\section{Conclusions and Future Work}
  \subsection{Conclusions}
  \subsection{Future Work}
```

### 4.3 Scaffold conventions (as built)

**Files.** `main.tex` holds each chapter's `\section` and label (`sec:intro`, `sec:background`,
`sec:pihm`, `sec:pipeline`, `sec:standard`, `sec:descriptor`, `sec:nonlinear`, `sec:results`,
`sec:discussion`, `sec:conclusions`) and inputs `2_body/1_introduction.tex` …
`2_body/10_conclusions.tex`. `3_footer/appendices.tex` does the same for
`3_footer/appendices/A_gates.tex` … `M_proposal.tex`. Every subsection has a label.

**Comment tags.** Each file opens with a header and each subsection with a block, using:

| tag | meaning |
|---|---|
| PURPOSE, CRITERION, SOURCES, WRITE WHEN | the chapter's job, the rubric wording, where the material comes from, the wave (§11) |
| LAND | the claims to write, in order, with the page share |
| FIG, TAB | the placeholders that belong to the section (§7) |
| OFFLOAD | what goes to an appendix, with the pointer sentence |
| CHECKLIST, TRAPS | the marker checklist and the failure modes |
| REVISE | kept prose that states a retired or wrong claim: fix before the section is "D" |
| CITE-NEEDED | a citation not yet in `ref.bib`: add a real entry, never a guessed one |

**Macros** (`1_header/0_packages.tex`): `\G`, `\Bt`, `\Dt` (names shared with `pihm`'s Sphinx
configuration), `\M`, `\nfold` (𝕟, via `bbm`), `\Brow`, `\Dzero`, `\Ucg`, `\Uodd`, `\Astd`,
`\Adesc`, `\Hstd`, `\Hdesc`, `\fhat{j}`; `\prov{…}` for numbers `pihm` does not produce yet.
`pihm`'s numbers are quoted with `\res` from `0_results/results.tex` (§10.2).

**Placeholders.** Figures use the existing `\placeholderfigure[height]{caption}{label}{spec}`,
with the figure's specification inside the box. Tables carry their final columns, with `\prov`
values from `pihm`'s reports where they exist (T6, T7, and the tables of Appendices D, E, I and
K) and `\prov{--}` elsewhere. Propositions and theorems hold their mathematical statement, with the
prose to write in a `% STATE:` comment; proofs are appendix subsections with `LAND` comments,
never empty `proof` environments.

**Build check.** The scaffold compiles with no errors and no undefined references or citations
(68 pages including the 10-page proposal); its 17 overfull boxes are all in the pre-existing
draft or the bibliography notes.

---

## 5. Chapter by chapter

Each chapter entry gives:

- **Purpose**, in one sentence;
- **Criterion**, with the top-band wording it must satisfy;
- **Sources**: the Planning sections, `pihm` artefacts and claim IDs it draws on;
- **Scaffold**: the subsections, each with the claims it must land, in order, with page shares;
- **Figures and tables**, and **appendix offloads** (with the pointer rule: say what is there);
- **Marker checklist** and **traps**.

The `pihm` paths are relative to `Code/pihm/`.

---

### 5.1 Chapter 1: Introduction (3.5 pp; Intro & Lit /20)

**Purpose.** Establish that quantum DE solvers matter and that the physics-informed Hamiltonian
route has a specific, *located* cost problem. Then state what this thesis contributes, and what it
does not.

**Criterion.** "Comprehensive, superior understanding… with **excellent connection of the current
field to the project**". The introduction converges; it does not survey.

**Sources.** Planning §0; §3.1 of this plan.

**Scaffold.**

1. **§1.1 Differential equations as a target (1 p).** Applications (fluids, finance, fields);
   why quantum algorithms are proposed; the resource that matters: queries × gates per query, and
   qubits. Cite the families briefly and leave the detail to Ch. 2.
2. **§1.2 Physics-informed Hamiltonians and where their cost lies (1 p).** Wu et al.'s idea in
   three sentences, attributed at first mention. Then the question this thesis asks: *is the
   method's cost in its encoder or in its Hamiltonian?* One quantitative sentence before the end
   of page 2: at n = 8 (Fig. 3b), the degree needed is 8.2×10²³ as published, 1.2×10¹⁰ with the
   best exact encoding, and 5.6×10³ in descriptor form (Planning A-6; `results-v1` values in the
   final text).
3. **§1.3 Contributions and scope (1 p).**
   - The numbered list of §3.1, followed by the spine sentence.
   - **The scope statement, once, plainly:** every result is a classical computation; there is
     circuit simulation at small n, exact emulation beyond it, and resource estimates beyond that.
     Nothing ran on hardware. Readout is the paper's protocol, reproduced in simulation.
   - What is *not* claimed: poly-log end-to-end cost; preparation for degenerate formulations; a
     new readout protocol.
4. **§1.4 Outline (0.5 p).** One bullet per chapter naming its job. Mark Ch. 3 as reviewed prior
   art and Chs 4–7 as this thesis's model.

**Marker checklist.**

1. Can a non-specialist physicist state the problem after two pages?
2. Is there a number on page ≤ 2?
3. Is every contribution numbered and falsifiable, with its evidence named?
4. Is the scope statement explicit, including the tier vocabulary and "no hardware"?
5. Is Wu et al. attributed at first mention, not at first critique?
6. Does the outline match the headings verbatim?

**Traps.** Leading with the descriptor's advantage before the reader knows the baseline; claiming
a speed-up (Trap 9); listing S2 as a competing method.

---

### 5.2 Chapter 2: Background and Literature Review (7.5 pp; Intro & Lit /20)

**Purpose.** Command of the state of the art, **judged**. Only the prior art that Chapters 3–7
build on.

**Criterion.** "A critical assessment of the strengths and weaknesses of the material reviewed is
required for a high distinction." Every family gets a failure-mode sentence.

**Sources.** `ref.bib` (current keys) plus the additions listed at the end of this section; Planning
§3.7–3.8 for which primitives are needed.

**Scaffold.**

1. **§2.1 QC preliminaries (≤ 2 pp, hard cap).**
   - Prose, citing Nielsen & Chuang.
   - Numbered definitions *only* for block encoding ((α, m, ε), since α is used throughout) and the
     state space if re-invoked.
   - Complexity: queries versus gates, and the fault-tolerant frame. NISQ gets one paragraph,
     because the thesis's feasibility argument (§9.5) is fault-tolerant.
   - Gate table in Appendix A.
2. **§2.2 Quantum algorithms for DEs (2 pp).**
   - (a) Linear-systems routes: HHL, Berry's ODE solvers, Childs–Liu spectral methods, LCHS and
     Schrödingerisation. Each costs through condition number and state preparation, and each fails
     on readout, conditioning or the need for sparse access.
   - (b) Nonlinear routes: Carleman (Liu et al. 2021; Krovi 2023), with its dissipativity condition
     stated as the precondition it is.
   - (c) Variational routes: barren plateaus, and no guarantees.
   - (d) Ground-state (Hamiltonian-embedding) routes, among them Wu et al., as the family Chapter 3
     examines.
   - **Table:** approach × {assumptions, query cost, output, failure mode}, with a *this work* row.
3. **§2.3 Spectral methods (1.5 pp).**
   - Chebyshev series, differentiation (dense, strictly upper triangular), Galerkin truncation and
     aliasing.
   - **The ultraspherical method (Olver & Townsend 2013)**, credited here *before* Chapter 6 claims
     anything. State precisely what the increment is: applying the basis change to the
     *physics-informed residual*, so that block encoding and filtering inherit the bandedness, and
     proving the kernel is unchanged.
   - Fourier–Galerkin for periodic flows (needed for R9 and R10).
4. **§2.4 Block encoding, LCU, qubitisation (1 p).** PREPARE/SELECT; α = Σ|c_t|; the Ω(log L)
   ancilla lower bound for exact LCU (Chakraborty et al. 2025, Thm A.1); qubitised walks,
   Π W^k Π = T_k.
5. **§2.5 QSP → QSVT → GQSP (0.75 p).** The parity constraint and its removal (Motlagh & Wiebe);
   phase finding (NLFT, Weiss complement) as prior art, cited.
6. **§2.6 Ground-state preparation by filtering (0.5 p).** Imaginary time; Lin & Tong's filters;
   the known-gap assumption; the overlap γ; amplitude amplification.
7. **§2.7 Readout (0.5 p).** Hadamard test, overlap estimation, amplitude estimation, and the
   shot-count scaling O(1/δ²). No figure. Wu et al.'s interferometric protocol is described in
   Chapter 3, not here.
8. **§2.8 Synthesis (0.25 p).** Physics-informed Hamiltonians sit where? The paragraph hands the
   reader to Chapter 3 "on the same attributed footing".

**Citations to add to `ref.bib`** (check the keys against `Code/pihm/docs/references.bib` first,
which may already hold some):

- Harrow–Hassidim–Lloyd 2009;
- Berry 2014 (present) and Berry et al. 2017;
- Childs & Liu 2020 (spectral methods);
- An, Liu & Lin (LCHS);
- Jin, Liu & Yu (Schrödingerisation);
- Liu et al. 2021 (Carleman, PNAS);
- Krovi 2023;
- Lin & Tong 2020 (near-optimal ground-state preparation);
- Cuccaro et al. 2004 (the adder);
- Weiss / Berntson–Sünderhauf (complementary polynomials);
- Ni–Ying or Laneve (NLFT phase finding), whichever `pihm/qsp/phases.py` actually follows;
- Qiskit Aer;
- Taylor–Green; Cole–Hopf.

**Marker checklist.** Every method has a weakness sentence; the comparison table is present;
ultraspherical is credited before Chapter 6; §2.1 ≤ 2 pp; nothing in the chapter goes unused later;
IEEE-style `biblatex` throughout.

---

### 5.3 Chapter 3: The Physics-Informed Effective Hamiltonian Method (4 pp; Intro & Lit /20, body-located)

**Purpose.** Present Wu et al.'s method at journal-review depth, in the register of attributed
prior art, then judge it. The judgement poses the three questions Chapters 5, 6 and 7 answer.

**Criterion.** This chapter discharges the HD gate of Intro & Lit: "critical assessment". Its
opening sentence must say it presents reported prior art, and its closing section must read as a
gap statement (the old guide's §0 note still applies).

**Sources.** Planning §3.1 (model, η_e), §3.2 (operator dictionary), §3.3 (the standard form as
published), §3.6 (the doubled space), §3.7 ("Standard form, as published"), §3.8 (the paper's QSVT
and time rule, under "Documented deviations"), §7.6 (the paper's Eqs 36–39); claims A-01 to A-13
as *the paper's claims*, stated neutrally here and tested in §8.2.

**Scaffold.**

1. **§3.1 Overview (0.3 p).** The three-ingredient move: coefficients as the state, the equation
   as annihilation, the Hamiltonian's ground state as the solution. State that this chapter
   reports the method as published, and that *our* reproduction is in §8.2.
2. **§3.2 The latent Chebyshev model (0.5 p).** The normalised basis; f_q(x) = ⟨τ(x)|ψ⟩; the
   scale factor η; raw τ in rank-one rows. η_e = ‖b‖² = (N/π)∫f²/√(1−x²) is *our* closed form, so
   it is stated in §8.2 and not here.
3. **§3.3 The residual, the Hamiltonian and its constraints (1.2 p).**
   - A = Σ_j 𝕄_{a_j} 𝔾^j − 𝕄_r 𝔻⁽⁰⁾(x_s), with H = 𝒯(A) + Σ𝒯(𝔹_i).
   - Least squares, with an exact kernel only for polynomial solutions.
   - Invariant versus regular constraints; k − 1 invariants for order k.
   - Variable coefficients through the lifts 𝕄_{x^p}; sources through Maclaurin truncation.
   - PDE invariants hand-picked from the known solution.
   - A worked N = 4 instance goes to Appendix C.
4. **§3.4 The published circuits, filter and readout (1 p).**
   - Figs 2 and 8 (feature map + reflection) and Fig. 9 (the 𝔾 ladder: approximate value load,
     prefactor (2^{n−1} + 2ⁿ)‖𝔾‖_S).
   - The paper's claims: 2n + 3 qubits, O(n³) gates, error decreasing exponentially.
   - Mixed-parity QSVT on H/‖H‖_F; the time rule t ≥ λ_max/(λ₂(n−1)).
   - The interferometric readout (Eqs 36–39), described as published.
   - One schematic figure of the published pipeline (optional; drop it if over budget).
5. **§3.5 The doubled-space extension (0.4 p).** Ψ = ψ ⊗ ψ with the fold 𝕟₁. The paper's own
   statement of ≥ 2^{2n−1} zero eigenvalues, and that it "seeks a degenerate state that closely
   matches the analytic solution". The argument that kernels are subspaces and product states are
   not, so the method projects rather than prepares, belongs here as *assessment*.
6. **§3.6 Critical assessment (0.6 p).**
   - **Strengths:** a unified construction; exact kernels for polynomial solutions; poly(n) gates;
     no discretisation grid.
   - **Weaknesses, most severe first:**
     1. The spectrum. ‖H‖ grows as N⁸ against a flat gap, which fixes the filter degree whatever
        the encoder.
     2. The published normalisation is loose by a factor growing like N³.
     3. Printed choices distort the solution at the printed n: rounded points and Maclaurin
        sources.
     4. The PDE invariant sets determine the solution only at the printed n.
     5. The nonlinear route cannot prepare.
     6. The readout identity assumes deterministic preparation.
   - Each weakness carries a pointer, naming what is measured and where (§8.2 and §8.5).
   - **Close with three italic questions, each answered by a named chapter:**
     - (i) *Is the cost the encoder's or the Hamiltonian's?* → Chapter 5.
     - (ii) *Can the residual be reformulated so that its Hamiltonian is banded and
       well-conditioned, without changing its solution?* → Chapter 6.
     - (iii) *Can nonlinear equations be prepared rather than projected?* → Chapter 7.

**Figures and tables.** At most one (the published pipeline) in the body. The worked instance goes
to Appendix C and the circuits to Appendix D.

**Marker checklist.**

1. Could any sentence be read as claiming authorship of the framework (Trap 13)?
2. Is `wu2025pihm` cited at the head of §3.3 and at each construction?
3. Are *our* numbers absent from §3.2–3.5, and present in §3.6 only as pointed-to evidence?
4. Does §3.6 end with the three questions and the chapters that answer them?
5. Is the chapter ≤ 4 pp?

**Traps.** Naming "collocation"; retaining the legacy adder-ladder reconstruction; stating the
Θ̃(N²) floor.

---

### 5.4 Chapter 4: A Regime-Independent Quantum Pipeline (6 pp; Model Formulation /30)

**Purpose.** Specify the model: everything that is the same whichever residual is plugged in. That
covers problem inputs, the classical reference, the walk, the filter, readout, verification and
software. A reader could then "create equivalent models".

**Criterion (Modelling, verbatim):** "described in sufficient detail to permit readers to create
equivalent models. This should include: **a description of any software tools used and/or
created; a description and/or diagram of the model configuration; descriptions of the model input
options selected (boundary conditions…)**". The band-3 failure named is "**poor design of numerical
experiment**", so the experiment design belongs here in the body.

**Sources.**

- Planning §3.5 (the constraint layer) and §3.7 ("Composition of H…");
- §3.8 (qubitisation, GQSP, the filter, parameters, success probability, cost; the deviations from
  the paper);
- §4 (design principles D2, D4, D6, D7, D9, D10);
- §5.4 (what every run records);
- §6.2 (verification modes);
- §7 (Pillar 2: §7.2 protocol, §7.3 T1, §7.4 T2, §7.5 T3, §7.6 readout, §7.8 acceptance, §7.9
  error budget);
- §10.1–10.3 (software), §11 (HPC);
- claims C-03, C-04, C-08, B-13, B-16, B-24;
- Journal E022–E024 (the resource-estimate model; the readout identity);
- `pihm/src/pihm/circuits/compose.py`, `qsp/`, `pipeline/`.

**Scaffold.**

1. **§4.1 Overview and model configuration (0.75 p).**
   - **The pipeline figure: the most important figure in the thesis.** It runs problem spec →
     residual assembly (standard | descriptor) → stacked-residual block encoding → reflection V →
     walk W → GQSP-QITE → post-selection → readout, with the classical reference and the three
     verification tiers alongside.
   - The caption must stand alone as a summary of the model.
   - The design principle: the two forms differ *only* in the residual, so any difference in
     results is a difference of Hamiltonians.
2. **§4.2 Problem specification and model inputs (1 p).**
   - The three orthogonal axes: derivative representation, nonlinearity treatment and constraint
     rows (shared by both forms).
   - The constraint kinds: zero, collapse, ratio and datum slice (a table).
   - Paper-faithful versus corrected variants.
   - The benchmark ladder R1–R10: one new capability per problem, so a failure localises (a table
     of problem, reference and new capability; full specs in Appendix J).
   - The input options every run records: n, variant, form, encoder, ε = 1e-6, filter, initial
     state and rescaling.
3. **§4.3 The classical reference (0.4 p).** The smallest right singular vector of the stacked
   residual R, with a backward-error check. Why not `eigh(RᵀR)`: squaring doubles the condition
   number, and the standard form fails from n ≈ 7 (a single number; the table goes to Appendix I).
   Decoding, η_e, and the three metric levels (operator, state, decoded field) with explicit inner
   products (D9).
4. **§4.4 From stacked residual to quantum walk (1 p).**
   - **Proposition (S3):** for U_R encoding R = [R_1; …; R_L] with α_R = √(Σα_j²),
     V = U_R†(2Π_{a=0} − I)U_R is a Hermitian unitary with Π_in V Π_in = 2H/α_R² − I.
     Controlled-V needs only a controlled reflection. The proof goes to Appendix F.
   - The walk W = (2Π_in − I)V, with Π W^k Π = T_k(H′).
   - Interpretation: the quadrature combination has no ℓ₁ penalty, and the spectrum lands on
     [−1, 1] automatically.
   - Ancilla ⌈log₂ L⌉ + max_j a_j: about 14 at n = 2 for the descriptor, against 23 for the legacy
     Gram-sum composition. That is a number worth one sentence.
5. **§4.5 GQSP imaginary-time filtering (1 p).**
   - The filter f_β(x) = e^{−β(1+x)}, with coefficients (2 − δ_{k0})(−1)^k e^{−β} I_k(β).
   - **Σ|p_k| = 1 exactly**, so no rescaling is needed (a proposition; proof in Appendix F).
   - A priori β = (α_R²/2Δ) ln(1/ε_f), and d ≈ √(2β ln(2/ε_t)), hence
     d = Θ(√(α_H/Δ) log 1/ε).
   - Minimax is reported alongside.
   - **State what the a priori rule delivers**, as properties, not defects (Planning §3.8, D-072):
     it holds the *suppression* of the excited spectrum to ε, so the infidelity is at most
     ε²(1 − γ²)/γ² and the degree is higher than ε needs; and its tail ε/10 is absolute, so it
     certifies nothing once the ground state sits about a gap above the spectrum's edge
     (λ₀/Δ ≳ 0.8). Every run measures its own infidelity, so neither hides a miss.
   - Initial states: the geometric product state, n R_Y rotations, r = ±½ chosen by *measured*
     success probability, with γ reported.
   - Success probability and amplitude amplification (π/(4γ)).
   - Total cost ≈ (π/4γ)[2d·g(U_R) + d·g(refl)].
   - **Documented deviations from Wu et al.:** GQSP instead of mixed-parity QSVT; normalisation by
     the construction's α instead of ‖H‖_F; parameters from the gap. The paper's time rule is a
     variant run in R2.
   - Phases come from NLFT + Weiss, cited; the realised polynomial matches its target to ≤ 1e-12.
6. **§4.6 Reading out the solution (0.5 p).**
   - The paper's interferometric protocol as reproduced.
   - The finding: Eq. 36 assumes deterministic preparation. With GQSP success p_G < 1, the
     success-conditioned version leaves an x-dependent error (16 % at R1, n = 2, p_G = 0.70). The
     raw-probability identity f* = 4P_C − P_G − 1/(2N) = √(p_G/N) τ·ψ is exact for any p_G. Its
     derivation goes to Appendix F.
   - Shot cost O(1/δ²) per point.
   - The combiner controls only the state preparation's rotations, reflections and global phase,
     never U_R, so it costs one qubit more than T1.
   - Lesson L-22: a controlled global phase becomes a relative phase. One sentence, because it is
     a correctness condition of the construction, not a diary entry.
7. **§4.7 Verification framework and error budget (1 p).**
   - **Operator verification:** the exact / probe / IR / approximation modes, their sizes and their
     tolerances (a table). Why IR is not a tautology: it checks against an *independently
     assembled* operator.
   - **State-preparation verification:** T1, T2 and T3.
   - **The argument for T2 ≡ T1:** by qubitisation and GQSP the output depends on the encoding
     only through Π V Π. So T2 is exact, and T1 checks it (≤ 1e-10) where both run.
   - The resource estimate that precedes every T1 run (memory 16·2^q bytes from the circuit
     structure; time from one measured step), which records `infeasible` rather than attempting.
   - Acceptance criteria (a table, from Planning §7.8).
   - **The error budget** ‖f_Q − f‖ ≤ ε_disc + κ_read(ε_filter + ε_trunc + ε_phase + d·ε_BE) +
     ε_sample, every term measured separately.
8. **§4.8 Software and computational configuration (0.35 p).**
   - `pihm`: numpy, scipy, qiskit and qiskit-aer only; one implementation per concept; frozen,
     hashed problem specs; strict-JSON records with provenance; claims tests.
   - Setonix campaigns: manifests, resource classes and array jobs.
   - `results-v1`.
   - One sentence on the size of the test suite (unit, property, golden, reproduction, claims).
   - Detail goes to Appendix L. **No code listings in the body** (the rubric: "no need to include
     detailed codes").

**Figures and tables.**

- **Fig. 4.1**, the pipeline (a TikZ schematic);
- **Table 4.1**, the constraint kinds;
- **Table 4.2**, the benchmark ladder (short form);
- **Table 4.3**, verification modes and tolerances;
- optionally **Fig. 4.2**, the GQSP-QITE circuit R₀∏[C₀W R_k] (quantikz). This is one of the four
  body circuits the style guide allows.

**Appendix offloads.**

- Appendix F: the identities' proofs, filter coefficients, parameter formulas and the readout
  identity;
- Appendix I: the verification protocol in full, including the memory model (measured ratio
  0.85–1.05 against the model at 22 qubits);
- Appendix J: the full ladder specifications;
- Appendix L: software.

**Marker checklist.**

1. Is there a configuration diagram?
2. Is every input option named with its value?
3. Is the software described?
4. Is the numerical-experiment design justified (a ladder, identical specs across forms,
   answer-independent states, a priori parameters)?
5. Are the deviations from the paper listed?
6. Is the T2 ≡ T1 argument stated before any T2 number is used?
7. Is the readout correction attributed as ours and the protocol as the paper's?

**Traps.** Writing it as a software manual; letting "Pillar" and "tier" jargon leak in; presenting
the readout as new.

---

### 5.5 Chapter 5: The Standard Form, Encoded Exactly (3.5 pp; Model Formulation /30)

**Purpose.** Answer question (i). Build the paper's own encoding as published, then the best exact
encoding of the paper's regime, and show that even the best encoder leaves a Θ̃(N⁴) degree, because
the cost is in the Hamiltonian.

**Criterion.** Formulation /30, band 4: "providing a significant advance in the state of the art".
S2 is a genuine, verified construction.

**Sources.**

- Planning §3.7: the published build and the structured exact encoding (the factorisation;
  Λ, U_odd, R₀; lifts; rank-one rows; products with ancilla reuse);
- §6.3; A-4; A-6; claims A-06 to A-08, A-12, C-01, C-02;
- `pihm/src/pihm/circuits/standard.py` and `arithmetic.py`;
- `docs/PILLAR1.md`;
- lesson L-20 (a sign on a gateless term), as a correctness remark only if it is needed.

**Scaffold.**

1. **§5.1 The published encoding, rebuilt (0.75 p).**
   - Figs 2, 8 and 9 built as drawn, from the legible figure and the caption angles.
   - What is measured: the qubit count against the claimed 2n + 3; gates after MCX decomposition
     against the claimed O(n³); ε_G(n) against "exponentially decreasing"; the prefactor.
   - Results in one sentence, pointing to §8.3. **The key number:** α/‖𝔾‖₂ = 2.2×10⁶ at n = 7,
     growing like N³.
   - Every deviation from the figure is documented in Appendix D.
2. **§5.2 An exact factorisation of 𝔾 (1 p).**
   - **Proposition:** 𝔾 = R₀(2U_odd)Λ, with R₀ = I − (1 − 1/√2)|0⟩⟨0|,
     (U_odd)_{kp} = [p > k, p − k odd] and Λ = diag(p).
   - The idea in words first: every entry is (a row-0 weight) × (a parity-selected shift) × (the
     column index).
   - Proof in Appendix E. Measured to ≤ 2.3e-13 for n ≤ 10, but the proposition is exact, so
     quote the measurement as verification, not as evidence.
3. **§5.3 Circuits and cost (1 p).**
   - Λ as a Z-string LCU (α = N − 1, ⌈log₂(n+1)⌉ selectors, O(n) gates).
   - U_odd: uniform PREPARE over odd offsets; SELECT as in-place subtraction p ← p − d with a
     post-selected borrow flag, so wrapped terms vanish exactly (α = N/2, O(n) Toffolis).
   - R₀: a two-term LCU.
   - **Proposition (cost):** α_G = N(N−1), O(n²) gates, n + O(log n) ancilla. The Ω(n) floor comes
     from the N/2-term LCU, and that is a genuine regime difference from the descriptor.
   - Lifts, rank-one rows via the feature map, and products with ancilla reuse.
   - One representative circuit figure: U_odd's SELECT.
4. **§5.4 What remains: the standard-form Hamiltonian (0.75 p).**
   - α_H/‖H‖ stays bounded (22 → 60 over n = 2–8, Fig. 3b). The encoder has done its job.
   - But ‖H_std‖ = Θ(N⁸) against a flat gap (7.04), so d = Θ̃(N⁴): 1.2×10¹⁰ at n = 8.
   - **This is the Hamiltonian wall.** Interpretation: 𝔾 has ‖𝔾‖ = Θ(N²), squared by the
     Gram product and again by second derivatives; no encoder can undo a norm.
   - Close by naming Chapter 6 and what it changes: the Hamiltonian itself.

**Figures and tables.** One circuit (U_odd SELECT), and optionally a small table of α/‖𝔾‖₂ for the
structured and published encodings at n = 2, 4, 7 and 10. The full table (A-4) goes to Appendix E.

**Appendix offloads.** Appendix D covers the published circuits as built and the measured ε_G.
Appendix E covers the factorisation proof, the arithmetic SELECT and the resource derivation.

**Marker checklist.**

1. Is the published build reported as a test of the paper's claims, with each claim's verdict?
2. Is the factorisation stated as a proposition, with the proof pointed to by content?
3. Does §5.4 make the encoder-versus-Hamiltonian distinction unmissable?
4. Is S2 framed as serving the comparison?

**Traps.** Calling S2 "our standard-form solver"; quoting ε_G bounds from the legacy
reconstruction.

---

### 5.6 Chapter 6: The Descriptor Reformulation (9.5 pp; Model Formulation /30, the core)

**Purpose.** Answer question (ii). This is the thesis's headline, written as the methods section
of a journal article.

**Criterion.** Formulation band 4, "warranting publication". The body carries four things: the
idea, the object (stated once), the cost (as a formal result) and the interpretation. Everything
else goes to Appendices B and G.

**Sources.**

- Planning §3.4 (the state, the block-row table, kernel equivalence, bandedness, Neumann on the
  f′-block, PDEs and coupled fields, the cost of carrying derivatives, block rescaling);
- §3.7 ("Descriptor: the flat LCU compiled from the term IR");
- §6.4; A-1; A-2; A-6;
- claims B-01 to B-07, B-10, B-20, B-21, C-05, C-06;
- `pihm/src/pihm/assemble.py` (descriptor mode), `ir.py` and `circuits/lcu.py` (built in P5).

**Scaffold.**

1. **§6.1 The idea (0.75 p).**
   - One paragraph in words: differentiation of a Chebyshev series is banded if the derivative may
     live in a neighbouring basis. So carry f′, …, f⁽ᵏ⁾ as their own blocks and tie them by banded
     recurrences, rather than substituting the dense 𝔾.
   - A **figure**: the sparsity patterns of A_std and A_desc side by side for {1,4,4} at n = 4
     (dense upper triangle against a block-banded pattern).
   - The spine sentence.
2. **§6.2 The banded factorisation (0.75 p).**
   - 𝔾 = B̃⁻¹D̃, from the recurrence c_r p_r − p_{r+2} = 2(r+1)a_{r+1}.
   - B̃ has its diagonal and second superdiagonal occupied; D̃ its first superdiagonal.
   - **Re-credit Olver & Townsend at the point of construction.** Entries go to Appendix B.
3. **§6.3 The descriptor residual and kernel equivalence (1.5 p).**
   - The state w = (f̂⁽⁰⁾; …; f̂⁽ᵏ⁾), padded to 2^⌈log₂(k+1)⌉ blocks.
   - The block-row table: recurrence rows, the equation row, padding.
   - **Theorem (kernel equivalence):** ker A_desc = {(p, 𝔾p, …, 𝔾ᵏp) : p ∈ ker A_std}, exactly,
     given the same 𝕄. It follows because B̃ is invertible. Proof in the body if it fits in five
     lines; otherwise in Appendix G.
   - The least-squares ground states differ by row weighting and converge to the same function
     (restates B-02).
   - **Volunteer the cost in the same breath:** the Hilbert space grows from N to 2^⌈log₂(k+1)⌉·N.
4. **§6.4 Constraints, PDEs and coupled fields (1 p).**
   - The shared constraint layer on chosen blocks. Neumann sits on the f′-block: the same atom as
     Dirichlet, with no 𝔾 (this retires B-10's "Θ(N²) more").
   - PDEs: a shared f-block plus one derivative chain per axis. Coupled fields: one chain per
     field.
   - Datum slices for initial and boundary functions. Note that these are available to the
     standard form too, so "the descriptor avoids doubling for linear PDEs" is *not* claimed
     (B-20).
5. **§6.5 Block rescaling (0.75 p).**
   - Because ‖𝔾‖ = Θ(N²), derivative blocks dominate: Δ = 7.5e-6 for {1,5,400} unrescaled.
   - The remedy p_m → λ^{−m}p_m is a diagonal on the field register at Θ(n_f) gates.
   - Why general equilibration is excluded from circuit paths: Θ(P) gates (V-08).
   - λ is problem-derived (λ = ω for R2c), not fitted (Planning §14 item 4).
6. **§6.6 The block encoding: one flat LCU (1.5 p).**
   - Every block is a short sum of SHIFTˢ·diag terms. diag(k) = Σ_j 2^j (I − Z_j)/2; nearly
     constant diagonals use reflections R_m.
   - The term IR compiles to PREPARE/SELECT/PREPARE†.
   - **A quantikz figure** of the flat LCU and an **`algorithm2e` listing** (IR → circuit),
     followed by a line-referenced walkthrough (Snow's model).
   - Rank-one rows via the feature map, with no dense state preparation anywhere (I-01 fixed).
7. **§6.7 Cost of the descriptor encoding (1.25 p).**
   - **Proposition:** α_A = 2N + O(1), with α_A/‖A_desc‖ → 1 (measured 2.29 → 1.002 over
     n = 2–12); ancilla ⌈log₂(n+4)⌉ + 6 for R2's family; O(n²) gates.
   - With Ω(log L) for exact LCU, the ancilla count is order-optimal *among exact LCU encodings*.
     Hedge exactly that far.
   - Proof in Appendix G.
   - **Two paragraphs of operational interpretation in the body:** what 10 ancilla at n = 12 means
     next to the standard form's Ω(n); what α → ‖A‖ means for the filter.
8. **§6.8 Consequences for the spectrum and the filter (1.25 p).**
   - ‖H_desc‖ = Θ(N²); α_H/‖H‖ → 1 (5.3 → 1.05).
   - Δ is problem-dependent: flat at 0.454 for {1,4,4}; 7.5e-6 for {1,5,400} before rescaling.
   - Hence **d = Θ̃(N)**, against Θ̃(N⁴) (Chapter 5).
   - The relative gap: 7.0e-6 against 3.0e-15 at n = 7 for {1,4,4}. State its meaning precisely:
     the standard form's ground state is below double-precision resolution by `eigh`, *not* by
     SVD. The consequence is the degree, not unresolvability (restates B-07 and B-23).
   - Point to §8.5 for the measured curves.
9. **§6.9 Summary (0.25 p).** Four numbered takeaways and the spine sentence.

**Figures and tables.**

- **Fig. 6.1**, sparsity patterns;
- **Fig. 6.2**, the flat-LCU circuit;
- **Algorithm 6.1**, IR → PREPARE/SELECT;
- **Table 6.1**, block rows;
- optionally **Table 6.2**, the descriptor atoms (term type, arity, gate cost, verified residual).

**Appendix offloads.** Appendix B covers the entries of B̃ and D̃ and the ultraspherical identities.
Appendix G covers the construction in full, the padded block count, the kernel-equivalence proof,
the cost proof and the term-IR grammar.

**Marker checklist.**

1. Could a referee re-derive A_desc from the body plus Appendices B and G?
2. Is the Hilbert-space cost volunteered alongside the gains?
3. Is the ultraspherical antecedent credited twice (§2.3 and §6.2)?
4. Is the cost result a proposition *and* interpreted?
5. Is the ancilla claim O(log n), with optimality hedged to exact LCU?
6. Does the gap discussion distinguish `eigh` failure from true unresolvability?
7. Does every body equation pass the equation test?

**Traps.** "O(1) ancilla"; "bit-identical a-block"; "only the descriptor can prepare nonlinear
solutions"; equilibration numbers quoted without their Θ(P) gate cost.

---

### 5.7 Chapter 7: Polynomial Nonlinearity (4 pp; Model Formulation /30)

**Purpose.** Answer question (iii). Separate what the doubled space can claim (an exact encoding;
a projection) from what Carleman can (a preparation), in both forms. Then set up the fluid
problems.

**Sources.**

- Planning §3.6 (doubled or tripled space; the Carleman lift and its space-time forms; the product
  fold on a circuit);
- §5.3 R6–R10; §6.5; §7.7;
- claims A-10, B-12, B-18, B-19, B-22, C-09, C-10;
- `pihm/src/pihm/carleman.py` and `problems/fluids.py` (P6–P7).

**Scaffold.**

1. **§7.1 Two regime-independent treatments (0.25 p).** Nonlinearity is the second axis of §4.2.
   Both treatments work in both forms.
2. **§7.2 The doubled space (0.75 p).** An exact encoding; kernel dimension ≥ N² − 2N (legacy
   measurement; the paper says ≥ 2^{2n−1}). The claim is QITE → Π_ker φ₀ (projection).
   **Proposition:** no penalty makes the kernel one-dimensional, because kernels are subspaces and
   product states are not.
3. **§7.3 The Carleman lift in space-time (1.25 p).**
   - z = (u, u^{⊗2}, …, u^{⊗K}); the truncation error is O(ρ^K) with ρ < 1 **stated as a
     precondition**.
   - A linear IVP has a unique solution, so the space-time residual has a one-dimensional
     near-kernel.
   - The two time discretisations: A_st(std) = 𝔾_t ⊗ I − (T/2) I ⊗ 𝔸_K, and
     A_st(desc) = (B̃_t ⊗ I)·A_st(std). Same kernel, differing only by a banded invertible left
     factor. That is why R8–R10 compare like for like.
   - Initial data enter through ratio rows.
4. **§7.4 Product folds on a circuit (0.75 p).**
   - The nodal fold 𝕟₁^{(p)} = 2^{pℓ/2} 𝕌†Δ_p 𝕌^{⊗p}: 0 ancilla, and α = 2 = ‖𝕟₁‖ for p = 2, so
     **optimal, not merely tight** (operator-verified to ~1e-15).
   - The Fourier fold is QFT, CNOT copy, QFT† (native, exact).
   - The Chebyshev DCT is budgeted as a cited primitive (Klappenecker–Rötteler). Say plainly that
     it is not built gate-level (decision 6).
5. **§7.5 Fourier–Galerkin fluids (0.75 p).**
   - Burgers: F₁ = diag(−νk²), with F₂ the (u²)ₓ/2 convolution.
   - 2-D vorticity NS with ψ̂ = ω̂/|k|² eliminated.
   - The tensor-layout Carleman: K² structured terms, with F₂ = L ∘ fold assembled automatically
     from the problem specification.
   - Taylor–Green (J ≡ 0) as the validation case.
6. **§7.6 Preparation versus projection (0.25 p).** A two-column table: which route sits on which
   side, and why. One sentence tying back to §6.1's structural principle.

**Marker checklist.**

1. Is "prepared" never used for the doubled space?
2. Is ρ < 1 a stated precondition?
3. Is fold optimality distinguished from tightness?
4. Are the unbuilt components (the DCT) named, with the reason?
5. Is Carleman's uniqueness attributed to Carleman, not to the descriptor form?

---

### 5.8 Chapter 8: Numerical Study (12 pp; Results & Discussion /30)

**Purpose.** Evidence every claim in the Abstract and in §1.3, "without reference to any other
documents".

**Criterion.** "Complete, clearly presented results, with detailed discussion showing insight…
or warranting publication." Every figure is interpreted in prose.

**Sources.**

- `pihm/docs/REPRODUCTION.md`, `PILLAR1.md`, `PILLAR2.md`, `CLAIMS.md`;
- notebooks `10_paper_reproduction`, `20_pillar1_operators`, `30_pillar2_stateprep`,
  `40_scaling_and_claims` and `50_navier_stokes`;
- the P8 campaigns at `results-v1`;
- Planning §5.2, §5.4, §6.6–6.7, §7.3–7.9, App A.

**Scaffold.**

1. **§8.1 Experimental design and cost conventions (0.75 p).**
   - What counts as a gate: transpiled to {cx, u} at `optimization_level=1`, with logical counts
     alongside and optional Clifford+T.
   - How ancilla are counted: the composed V, not per atom.
   - **Which way the convention biases the comparison.** Declare it: the structured standard-form
     encoding is the *best* we could build, so any descriptor advantage is against the strongest
     baseline, i.e. a conservative comparison.
   - The tier of every number is marked in every table: T1, T2 or T3.
   - All numbers come from `results-v1`.
2. **§8.2 Reproducing Wu et al. (2 p).**
   - **Table:** the η_e reproduction for all 16 panels (printed, ideal ‖b‖², ours at the printed
     n, status). If over budget, keep the 11 ODE rows plus a summary line and move the rest to
     Appendix K.
   - The closed form η_e = (N/π)∫f²/√(1−x²) and what it validates: our conventions are the
     paper's.
   - **Figure:** paper-faithful against corrected solution curves for 5a–5d, showing the
     distortion from rounded points and Maclaurin sources.
   - The Fig. 6 and Fig. 7 non-reproductions: hypotheses tested and outcomes (R-D1, R-D2), the
     Laplace typo, and ISSUE-008's backward-heat observation.
   - The paper-claims verdict summary (A-01 to A-13): a compact table in Appendix K, with one
     paragraph here.
   - The tau-truncation ablation (decision 11) gets one sentence and a pointer.
3. **§8.3 Operator verification and encoding cost (1.5 p).**
   - Verification accuracy against n for each encoder and mode (a figure or table).
   - **The headline table (three rows): published standard form | structured standard form |
     descriptor.** Columns: ‖H‖, Δ, α_𝔾/‖𝔾‖₂, α_H/‖H‖, gates per query, ancilla, exactness,
     degree at n = 8 and degree scaling. This is Planning §3.9 at `results-v1`, and the Abstract
     references it.
   - Resource fits against n with fitted exponents (checking B-03, B-04, B-05, C-01, C-02 and
     A-07).
4. **§8.4 State preparation and readout (2 p).**
   - T1 = T2 agreement (≤ 1e-10) where both run.
   - Infidelity against the target ε, and against the predicted bound (≤ 10× predicted).
   - Measured against predicted p (relative ≤ 1e-8).
   - γ for the geometric, uniform and random initial states.
   - The Δ-underestimate sensitivity (×2, ×10).
   - **The paper's time rule against the a priori β** (A-11 verdict).
   - **The filter at like error** (claim B-17; `pihm/docs/FILTERS.md`, D-072): QITE against the
     minimax edge filter at equal suppression (1.67–1.92× fewer degrees for minimax, any gap),
     at equal certified infidelity, and at equal measured infidelity on the ladder's own states
     (0.77–2.99× at ε = 1e-4, where QITE can need fewer; 1.34–2.53× at 1e-8). The descriptor's
     comparison joins it if P5 reaches it (Planning decision 29); one table and two sentences.
   - **Readout, classically** (Planning decision 27): the decoded field and η_e from the regular
     datum. The paper's interferometric protocol is built and verified for R1, R2a and R5a
     (T1 = T2), which is one sentence here; the protocol itself is future work (§10.2).
   - A **figure:** decoded field against the analytic solution with the error budget terms broken
     out (§4.7).
5. **§8.5 Scaling: where the cost lies (1.5 p). THE HEADLINE FIGURE.**
   - **Fig. 8.x:** a three-panel log–log plot against N, with fitted exponents: (a) ‖H‖ and α_H
     for the three encodings; (b) Δ; (c) degree d.
   - T2 points where measured and T3 beyond, *visibly distinguished*.
   - Interpretation: the encoder wall (published against structured) and the Hamiltonian wall
     (structured against descriptor) as two separate gaps on one plot.
   - This single figure carries contributions C and S2.
6. **§8.6 Representative problems (1.75 p).** Three problems in depth, each with a solution figure
   and a both-forms comparison:
   - **R2c {1,5,400}**: stiffness and block rescaling, showing where the descriptor's weakness
     sits and how rescaling fixes it;
   - **R3 Legendre (m = 0)**: the exact-kernel machine-precision benchmark;
   - **R5 heat or wave**: multi-axis, datum slices against the paper's invariants.
   - Everything else goes to Appendix J, with a pointer naming what is there.
7. **§8.7 Nonlinear benchmarks (1 p).**
   - R6: kernel dimension, projection fidelity ≈ 1 against physical fidelity (low). This is the
     projection evidence.
   - R8: a K × n_t error surface showing geometric decay in K once n_t resolves time, both forms,
     with the degree comparison (C-09).
   - R9 Burgers against Cole–Hopf and the exact-lift floor.
8. **§8.8 Case study: 2-D Navier–Stokes (1 p).**
   - (10a) Taylor–Green validates F₁, the lift, the data rows and the time axis.
   - (10b) An active nonlinearity against DNS.
   - Descriptor-in-time against standard-in-time at fixed K (C-10).
   - T2 at small size and T3 beyond, stated plainly.
   - If G6 is "honestly bounded by T3", this subsection reports that bound (§12).
9. **§8.9 Summary of findings (0.5 p).** Five or six numbered findings. **At least two negative or
   limiting ones**, for example:
   - the descriptor's Hilbert-space cost and its need for rescaling on stiff problems;
   - the doubled space projects;
   - NS reaches only T3 at physically interesting K.

**Marker checklist.**

1. Is the cost convention and its bias stated before the first comparison?
2. Is the tier marked on every number?
3. Is "could not simulate" kept distinct from "cannot reach"?
4. Are there at most three in-depth problems?
5. Does every caption stand alone?
6. Is at least one finding negative?
7. Is every Abstract number backed here?
8. Is §8.2 framed as reproduction, not rivalry?

---

### 5.9 Chapter 9: Discussion (4.5 pp; Results & Discussion /30)

**Purpose.** Explain and judge; don't restate. This is "insight into the significance of the
work", the band-4 separator.

**Scaffold.**

1. **§9.1 Why the descriptor form wins, and what it costs (1 p).**
   - Norm, not encoding: the elimination of derivatives multiplies norms, and carrying them keeps
     each block O(N) in norm.
   - The trade: Hilbert space, a block register, and rescaling where derivative norms dominate.
2. **§9.2 End-to-end complexity (1 p).**
   - The corrected complexity argument in your own voice: d = Θ(√(α_H/Δ) log 1/ε), and α_H ≥ ‖H‖
     for *any* block encoding of this H.
   - So for this *filter family* the standard form cannot go below Θ̃(N⁴) and the descriptor
     reaches Θ̃(N). The minimax filter changes the constant (at most about 2× at equal
     suppression, §8.4), not the Θ.
   - Total gates Θ̃(N poly n) against Θ̃(N⁴ poly n).
   - Neither is poly-log. Say it first, yourself.
   - Hedge the "for any filter" generalisation to what Lin & Tong's lower bounds actually support
     (§12, risk TR-3).
3. **§9.3 What the reproduction says about the published method (0.75 p).** A fair verdict:
   - the conventions are sound, and the η_e values are right;
   - the printed choices distort at the printed n;
   - the PDE and NDE panels do not reproduce;
   - the normalisation is loose;
   - the readout identity needs a correction for probabilistic preparation.
   Then what that means for readers of the paper. Keep the register collegial and evidential.
4. **§9.4 Where the construction applies (0.5 p).** Guidance a practitioner could act on: which
   equations benefit; when rescaling is needed; the nonlinear scope (dissipative, ρ < 1).
5. **§9.5 Feasibility on fault-tolerant hardware (0.5 p).** Logical qubits, cx or T counts and
   depth at meaningful n from T3; why NISQ is out of scope.
6. **§9.6 Limitations (0.75 p).** Each with its analysis:
   - no hardware;
   - T1 only at small n;
   - the Δ-known assumption;
   - the DCT as a cited primitive;
   - the doubled space projects;
   - NS bounded by T3 at large K;
   - the descriptor Hilbert-space cost;
   - Figs 6–7 unreproduced (authors not contacted).

**Marker checklist.** Does it explain rather than restate? Is the complexity argument complete and
consistent with §3.6, §5.4 and §6.8? Is every limitation owned, with its analysis? Are consequences
drawn for the field?

---

### 5.10 Chapter 10: Conclusions and Future Work (2.5 pp; Conclusions /10)

**Scaffold.**

1. **§10.1 Conclusions (1.25 p).** A verdict per contribution (C, S1–S4), mirroring §1.3, with the
   headline numbers once more, compactly. End with the transferable principle (the spine sentence,
   generalised: *reformulate the residual before encoding it*).
2. **§10.2 Future work (1.25 p).** 4–5 items, each with a motivation and **a concrete first step**:
   1. hardware validation of R1 (11 qubits at n = 2; d = 89);
   2. a gate-level DCT, so the Chebyshev fold is fully built;
   3. gap estimation on-circuit, removing the Δ-known assumption;
   4. complex-valued and non-Hermitian equations (NLS, Ginzburg–Landau), returning to the research
      proposal's aim, which GQSP already permits;
   5. data-informed constraint rows, the proposal's second aim;
   6. (candidate) the paper's interferometric readout at scale, with shot-count studies: built and
      verified for R1, R2a and R5a, then scoped out (Planning decision 27). Choose four or five of
      these six at drafting.

No new results and no new citations in this chapter.

---

## 6. Appendices (not counted in the page limit)

| | appendix | content | from | cited in |
|---|---|---|---|---|
| A | Quantum gate reference | the gate table and multi-controlled decompositions | n/a | §2.1 |
| B | Chebyshev and ultraspherical identities | normalised basis, S, 𝔾 entries, B̃/D̃ recurrence, the ultraspherical connection, the N = 4 instance (keep the existing draft) | Planning §3.1–3.2 | §2.3, §3.3, §6.2 |
| C | Wu et al.'s standard form in full | worked N = 4 residual; 𝕄_{x^p}, 𝕄_a, 𝕟₁, 𝕟_x; the paper's printed SM §A matrices reproduced entry by entry (A-01) | §3.2–3.3; Journal E001 | §3.3 |
| D | The published circuits as built | Figs 2, 8 and 9 rebuilt; every deviation from the figure; measured qubits, gates and ε_G(n); the prefactor against ‖𝔾‖₂ | §3.7, §6.3; A-4 | §5.1 |
| E | The structured exact 𝔾 encoding | the factorisation proof; Λ, U_odd (subtraction with borrow), R₀; resource derivation; the A-4 table | §3.7; C-01 | §5.2–5.3 |
| F | The shared pipeline: identities and formulas | stacked reflection; qubitisation Π W^k Π = T_k (with the L-18 caution: one power, then one restriction); controlled-V; QITE coefficients and Σ\|p_k\| = 1; β and d formulas; success probability; the readout identity for p_G < 1; controlled global phase (L-22) | §3.7–3.8, §7.6; A-7; E024 | §4.4–4.6 |
| G | The descriptor construction in full | the block rows; padded block count; the kernel-equivalence proof; the term IR and its compilation; the cost proof; block rescaling | §3.4, §6.4; A-2 | §6.3–6.7 |
| H | The nonlinear route in full | doubled-space algebra and kernel bound; Carleman (symmetric and tensor layouts), ratio rows, space-time forms; the nodal and Fourier folds; Fourier–Galerkin F₁ and F₂ for Burgers and NS | §3.6, §6.5 | Ch. 7 |
| I | Verification protocol | modes, sizes and tolerances; the structured probes (wrap-around, T₀ weights, block edges, axis order, borrow flags); per-atom residuals; T1 memory and time model and its calibration; acceptance criteria; the error-budget measurement; the `eigh` against SVD table (A-3) | §6.2, §7.3, §7.8–7.9; E023–E024 | §4.3, §4.7 |
| J | Benchmark catalogue | R0–R10: equations, references, constraints, variants, n-grids, parameters; a per-problem results table (both forms, tiers) | §5; `results-v1` | §4.2, §8.6 |
| K | Reproduction record | all 16 panels; the Fig. 5 triage; R-D1 to R-D3; M-01 to M-07; the paper-claims register A-01 to A-13 with verdicts; the ablation | §5.2, §8.1, §9.4; `REPRODUCTION.md`; ISSUE-001 to ISSUE-008 | §8.2 |
| L | Software and reproducibility | `pihm` architecture (the import-direction diagram); records and provenance; campaigns and Setonix classes; test tiers; how to regenerate every figure from `results-v1`; environment pins | §10–11 | §4.8 |
| M | Research proposal, with deviations | the May 2025 proposal verbatim, plus a deviations table (§13.4) | `Research_Proposal.pdf` | n/a |

**The pointer rule** (unchanged): never "see Appendix E". Write "the factorisation's proof and the
borrow-flag SELECT are given in Appendix E".

**Appendix L is the one appendix a marker may never read.** It exists for the Modelling rubric
("software tools used and/or created") and for the guidelines' "laboratory handbook" role. Keep it
factual and short (3–4 pp).

---

## 7. Figures and tables plan

**Body figures** (11 planned; the figure test applies to each):

| # | figure | chapter | source | tier |
|---|---|---|---|---|
| F1 | model configuration / pipeline schematic | §4.1 | TikZ (hand-drawn) | n/a |
| F2 | GQSP-QITE circuit (optional) | §4.5 | quantikz | n/a |
| F3 | U_odd SELECT (subtraction with borrow) | §5.3 | quantikz | n/a |
| F4 | sparsity of A_std vs A_desc | §6.1 | `pihm.assemble` → spy plot | exact |
| F5 | the descriptor flat LCU (PREPARE/SELECT) | §6.6 | quantikz | n/a |
| F6 | paper-faithful vs corrected curves, Fig. 5 panels | §8.2 | `10_paper_reproduction` | classical |
| F7 | verification accuracy vs n | §8.3 | `20_pillar1_operators` | exact/probe/IR |
| F8 | decoded field with the error budget | §8.4 | `30_pillar2_stateprep` | T1/T2 |
| F9 | **headline:** ‖H‖, Δ and d against N, three encodings | §8.5 | `40_scaling_and_claims` | T2 + T3 |
| F10 | representative solutions (three problems, both forms) | §8.6 | `40_…` | T2 |
| F11 | Carleman K × n_t convergence; NS snapshot | §8.7–8.8 | `50_navier_stokes` | T2/T3 |

**Body tables:**

- T1 approaches (§2.2);
- T2 constraint kinds (§4.2);
- T3 benchmark ladder (§4.2);
- T4 verification modes (§4.7);
- T5 descriptor block rows (§6.3);
- T6 η_e reproduction (§8.2);
- **T7 the headline three-row table (§8.3)**;
- T8 preparation vs projection (§7.6).

**Caption template** (from the style guide): a bold claim, not a label; then what is plotted, on
which axes, for which problem and parameters; then each panel; then the one takeaway; then the
tier. Figure captions go below and table captions above.

---

## 8. Notation

### 8.1 Master table (it becomes `1_header/6_notation.tex`)

| symbol | meaning | first use |
|---|---|---|
| n, N = 2ⁿ | qubits per Chebyshev axis; truncation dimension | §3.2 |
| k | ODE order | §3.3 |
| p | polynomial degree of the nonlinearity | §7 |
| τ(x), \|τ(x)⟩ | the paper's raw Chebyshev feature state | §3.2 |
| ψ, η, η_e | normalised coefficient state; scale; η_e = ‖b‖² | §3.2 |
| 𝔾 | differentiation matrix (dense, nilpotent, ‖𝔾‖₂ = Θ(N²)) | §3.3 |
| B̃, D̃ | banded factors, 𝔾 = B̃⁻¹D̃ | §6.2 |
| 𝕄_{x^p}, 𝕄_a | multiplication (lift; smooth) | §3.3 |
| 𝕟₁, 𝕟_x | product-to-sum folds | §3.5 |
| 𝔹(x), 𝔻⁽⁰⁾(x_s) | rank-one zero and collapse rows | §3.3 |
| x_z, x_m, x_s | constraint points (zero, extremum, source) | §3.3 |
| A_std, A_desc | residual (standard; descriptor) | §3.3, §6.3 |
| H_std, H_desc | Hamiltonian = RᵀR of the stacked residual | §3.3, §6.8 |
| R = [R_1; …; R_L] | stacked residual | §4.4 |
| w = (f̂⁽⁰⁾; …; f̂⁽ᵏ⁾) | descriptor state; f̂⁽ʲ⁾ is the j-th derivative's coefficients | §6.3 |
| n_f | field (block) register qubits | §6.3 |
| α, α_R, α_H = α_R² | subnormalisations | §2.4, §4.4 |
| V, W, H′ = 2H/α_R² − I | reflection; walk; normalised Hamiltonian | §4.4 |
| Δ, γ | spectral gap λ₁ − λ₀; overlap \|⟨ψ_ref\|φ₀⟩\| | §4.5 |
| β, d, ε | imaginary time; GQSP degree; target infidelity | §4.5 |
| p_G | GQSP success probability | §4.5 |
| K, M, ρ | Carleman order; base dimension; ratio ρ < 1 | §7.3 |
| F₁, F₂, 𝔸_K | Carleman linear and quadratic terms; lifted generator | §7.3 |
| ‖𝔾‖_S | the paper's max(‖𝔾𝔾ᵀ‖₁, ‖𝔾ᵀ𝔾‖₁) | §3.4 |

### 8.2 Collisions to resolve (Planning notation → thesis)

| Planning / code | clash | thesis |
|---|---|---|
| τ (imaginary time), `tau` | τ(x) feature state | **β** (T-08) |
| R (Carleman ratio) | R stacked residual | **ρ** (T-09) |
| p_j (descriptor blocks) | p nonlinear degree; p_k filter coefficients; p success probability | **f̂⁽ʲ⁾** blocks; **q_k** filter coefficients; **p_G** success probability |
| c_k (Chebyshev weights, c₀ = 2) | the old thesis's c⁽ʲ⁾ blocks | keep c_k for weights only |
| P (padded dimension) | P(z) GQSP polynomial | **dim w**, or D_w |
| bare A, H | both forms | subscripts (T-07) |
| G, B̃, D̃ (italic, current thesis) | 𝔾 etc. in the paper and `pihm` | blackboard bold (T-06) |
| G^⊤ applied to ψ (draft Ch. 3) | the draft's own upper-triangular G | 𝔾, no transpose (T-16) |
| B̃_std, D̃_std (draft App. B, unnormalised basis) | std = standard form | B̃_raw, D̃_raw (T-19) |
| λ (block rescaling, Planning §3.4) | eigenvalues λ₀, λ₁ | ζ (T-19) |
| β (ladder coefficient, draft App. D) | β imaginary time | μ (T-19) |
| κ (condition number) | κ_read | cond(·) (T-19) |
| α, β (qubit amplitudes, draft §2.1) | subnormalisation; imaginary time | rename when compressing §2.1 (a REVISE comment marks it) |

---

## 9. Claims → thesis traceability register

Status is carried over from Planning §8 and must read ✅ at `results-v1` before the claim is
asserted. **Register:** **A** = assert; **H** = assert with an explicit hedge; **N** = narrative
only (described, not claimed); **X** = do not state (retired).

| ID | claim | thesis location | register | evidence artefact |
|---|---|---|---|---|
| A-01 | 𝔾, 𝕄, 𝕟₁, 𝔹 match SM §A | App C; §8.2 (one line) | A | R0 golden test |
| A-02 | printed η_e (11 ODE panels) | §8.2 T6 | A (within one printed digit; 9/11 when rounded) | `REPRODUCTION.md` §1 |
| A-03/A-04 | Figs 6–7 η_e | §8.2; App K | A (not reproduced) with hypotheses | ISSUE-002, ISSUE-003 |
| A-05 | Laplace typo | §8.2 (a footnote) | A | ISSUE-006 |
| A-06–A-08 | published circuits (qubits, gates, prefactor, ε_G) | §5.1; §8.3; App D | A (per claim verdict) | P3/P4 encode records |
| A-09 | linear H positive definite, distinct eigenvalues | App K | A/H | SVD spectra |
| A-10 | doubled space ≥ 2^{2n−1} zero eigenvalues | §7.2; §8.7 | A (measured ≥ N² − 2N) | R6 records |
| A-11 | the paper's time rule suffices | §8.4 | A (verdict) | R2 variant runs |
| A-12 | "poly(n) terms, implementable efficiently" | §3.6; §5.1 | A (true for gates, not for α) | A-4 |
| A-13 | examples solved accurately at the printed n | §8.2 F6 | A (distorted: 5a ±1.7 %, 5b ±5 %, 5c ±3 %, 5d off) | ISSUE-004, ISSUE-005 |
| B-01 | 𝔾 = B̃⁻¹D̃ | §6.2 | A | R0 |
| B-02 | "bit-identical a-block" | §6.3 | **restated**: exact kernels coincide; LS states converge | A-3 |
| B-03 | O(1) ancilla | n/a | **X**, replaced by C-06 | n/a |
| B-04/B-05 | α_A/‖A‖ → 1; α_H/‖H‖ → 1 | §6.7–6.8; T7 | A | A-2, A-6 → `results-v1` |
| B-06 | Δ = Θ(1) | §6.8 | **H**: problem-dependent; rescaling | A-1 |
| B-07 | relative gap 1e-6 vs 1e-15 at n = 7 | §6.8 | A (with the `eigh`/SVD distinction) | A-1 |
| B-08/B-09 | Θ̃(N²)/Θ̃(N⁸) queries; total gates | n/a | **X**, replaced by C-05 and §9.2 | n/a |
| B-10 | Neumann costs Θ(N²) more | n/a | **X** | n/a |
| B-11 | every linear oracle poly(n) | §6.6 | A after the I-01 fix | P5 |
| B-12 | nodal fold 0 ancilla, α = 2, optimal | §7.4 | A (operator level; DCT cited) | R0/R6 |
| B-13 | H verifiable only by parts | n/a | **X**, replaced by exact V verification | P3 |
| B-14 | Haar-average p_succ Θ(1) vs N^{−3/2} | §8.4 only if T3 confirms | H or omit | T3 |
| B-16 | NLFT phases ≤ 1e-13 to 2.6×10⁵ | App F | A | golden re-check |
| B-17 | minimax ~1.8× lower degree | §4.5; §8.5 | A if measured | T3 |
| B-18/B-19 | Carleman O(ρ^K), unique near-kernel; K² tensor terms | §7.3–7.5 | A | R8–R10 |
| B-20 | the descriptor avoids doubling for linear PDEs | n/a | **X** (datum rows serve both forms) | n/a |
| B-21 | equilibration makes {1,5,400} reachable | §6.5 | **restated** as block rescaling | P5 |
| B-22 | only the descriptor prepares nonlinear solutions | n/a | **X**; C-09 instead | n/a |
| B-23 | standard-form ground state unresolvable at n ≈ 7 | §6.8 | **restated**: `eigh` fails, SVD resolves; the degree cost stands | A-3 |
| B-24 | GQSP realises any \|P\| ≤ 1, no parity | §2.5; §4.5 | A | A-7, T1 |
| B-25 | ⟨τ(x)\| is an LCU of two product states | App F or omit | A if used | R0 |
| C-01 | exact structured 𝔾 | §5.2–5.3 | A | P3 circuits (exact/probe/IR) |
| C-02 | structured α_H/‖H‖ bounded | §5.4; T7 | A | P3/P8 |
| C-03 | stacked reflection identities | §4.4 | A | P3 |
| C-04 | Σ\|q_k\| = 1; Π P(W) Π = e^{−β(1+H′)} | §4.5 | A | P4 T1 = T2 |
| C-05 | degree Θ̃(N⁴) vs Θ̃(N) | §6.8; §8.5 F9 | A (measured exponents with fit uncertainty) | P8 |
| C-06 | ancilla ⌈log₂(n+4)⌉ + 6 | §6.7 | A | P5 |
| C-07 | exact reproduction of the ODE results; Figs 6–7 documented | §8.2 | A | G1 |
| C-08 | T2 = T1 ≤ 1e-10 | §4.7; §8.4 | A | P4 |
| C-09 | Carleman 1-D near-kernel in both forms; descriptor time axis lowers the degree | §7.3; §8.7 | A | P6 |
| C-10 | NS descriptor-in-time vs standard-in-time | §8.8 | A or H (per G6) | P7 |
| new | readout identity for p_G < 1 | §4.6; App F | A | E024 tests |

**Rule.** Before a claim ID is cited in prose, its row reads ✅ in the generated `CLAIMS.md` at
`results-v1`. If it does not, the prose is rewritten to what *is* supported.

---

## 10. Code → thesis transfer protocol

### 10.1 Sources of truth

1. **Results:** `pihm` tag `results-v1` (Planning §9.3): `summary.csv`, the NPZ subsets and the
   generated `CLAIMS.md`. Nothing from legacy `Setonix/`, legacy notebooks or `docs/` (V-11).
2. **Mathematics:** Planning §3, as implemented and tested. Where the code and Planning differ,
   the code and its tests win, and `DECISIONS.md` records why.
3. **History:** Journal.md and DECISIONS.md are *never* cited. The thesis presents the final
   construction, not the path to it (Style Trap 6). Lessons L-xx appear only where they are a
   correctness condition of the construction (L-18, L-21, L-22), phrased as mathematics.

### 10.2 Numbers (T-15)

*Amended 2026-09-27: the exporter was built early, and it quotes by key instead of one hand-named
macro per number (LaTeX macro names cannot hold digits). How to use it: `0_results/README.md`.*

- **The exporter** is `pihm/tools/thesis/export_numbers.py` (pihm decision D-062). It is run
  whenever results change, not only at `results-v1`. It writes `0_results/generated/numbers.tex`,
  which holds every value of every run the campaigns expect, keyed like the record directories
  (`stateprep/R2a/corrected/standard/n3/T2`). Statistics over n and quantities computed without a
  campaign come from `tools/thesis/derived.py`. Each value carries a comment with its record hash
  and commit.
- **The thesis quotes by key**: `\res{<run>}{<metric>}`, `\res[2,sci]{…}{…}` for the format, and
  `\resflag{<run>}{<flag>}{<true>}{<false>}` (for example the untrusted dagger). The reader is
  `0_results/results.tex`, which `main.tex` inputs. It documents the key scheme, the formats and
  the placeholders.
- **A missing number says why.** It renders as a box reading pending, infeasible, failed, stale,
  no value or unknown, and it raises a log warning. The exporter prints the same list with
  file and line. *Infeasible* is a legitimate final result ("beyond the simulation budget";
  `\resinfeasiblemark` in the final text); the rest are draft-only.
- **Provisional until the freeze.** Values exported before `results-v1` render tinted. `--final`
  (at the tag, from a clean tree) writes untinted values, and it refuses while any quoted number
  is not from the tag or not final. A final build turns every draft-only placeholder into an
  error.
- `\prov{…}` remains only for a number `pihm` does not produce yet. The pre-submission check fails
  if any `\prov` remains (§14).
- Tolerances are quoted as the acceptance thresholds (Planning §7.8) *and* the achieved value.

### 10.3 Figures

- The figure scripts live in `pihm` (notebooks `10`–`50`, or `tools/thesis/figures.py`), read only
  the results, and write vector PDF to `thesis/Latex/Figs/generated/`. They use the shared style in
  `pihm/plotting.py`, set to the thesis font and size, at 12 pt with a single-column width.
- Each `\includegraphics` has a LaTeX comment directly above it naming its script and campaign.
  Regenerating everything is one command, documented in Appendix L.
- Circuit figures are hand-written quantikz, not qiskit drawings. Check that each drawn circuit
  matches the verified one: the same registers, and the same controls.

### 10.4 Translation table (code → thesis)

| code / Planning | thesis |
|---|---|
| `assemble(problem, regime, n, …)` | "the residual assembly" |
| `regime="standard" / "descriptor"` | standard form / descriptor form |
| `method="published" / "structured" / "lcu"` | published / structured (exact) / descriptor LCU encoding |
| `compose.stacked_reflection` | the stacked-residual reflection V |
| `verify(mode=exact/probe/ir/approximation)` | exact / randomised-probe / IR verification; approximation error |
| `prepare(tier=circuit/emulate/estimate)` | circuit simulation / exact emulation / resource estimate |
| Pillar 1 / Pillar 2 | operator verification / state-preparation verification |
| `status="infeasible"` | "beyond the simulation budget; resource estimate quoted" |
| rung R1–R10 | benchmark problem R1–R10 |
| `variant="faithful"/"corrected"` | paper-faithful / corrected |
| `phi0="geometric"` | geometric product initial state |
| `tau` | β |
| `ISSUE-00x`, `D-0xx`, `E0xx` | never cited; the content is stated as a finding |

### 10.5 Australian English

The thesis uses `[australian]{babel}`, and `pihm` already enforces AU spelling with codespell.
Consider reusing `pihm/tools/codespell/us_to_au.txt` on the `.tex` files as a pre-submission check.
API names stay verbatim (`optimization_level`).

---

## 11. Writing order (by dependency; no dates, T-03)

The waves follow the Planning gates. A wave can start once its gate is passed, and it runs
alongside the code phases. Current position: **G1 passed; G2 passed for R1–R2; P4 in progress.**

| wave | unlocked by | write | notes |
|---|---|---|---|
| **W0** ✅ | adoption of this plan | update `CLAUDE.md` and the guides per §2; rename files per §4.2; notation pass (T-06 to T-09); fix "Want"; add the `\prov` macro | **done 2026-09-25** (after snapshot `2cd640c`; the scaffold itself is uncommitted) |
| **W1** | now | Ch. 2 (all); Ch. 3 (all); Ch. 5 §5.1–5.3; Ch. 4 §4.1–4.5 and §4.7–4.8 as formulation; App A, B, C, E, F (identities) | these rest on built, verified code (P1–P3, P4 T1–T3) |
| **W2** | G3 (standard form R1–R6 through both pillars, readout) | §4.6; §5.4; §8.2; the standard-form half of §8.3–8.4; App D, K | the reproduction chapter's numbers freeze here |
| **W3** | G4 (descriptor R1–R6) | Ch. 6 in full (the maths can be drafted during W1 from Planning §3.4, with numbers as `\prov`); §8.3–8.6; App G, I, J (linear part) | the core |
| **W4** | G5 (R7–R9) | Ch. 7 §7.1–7.4, §7.6; §8.7; App H | |
| **W5** | G6 and `results-v1` | §7.5; §8.8; §8.9; Ch. 9; replace every `\prov` with generated macros; App L | the numbers freeze |
| **W6** | W5 done | Ch. 1; Abstract; Ch. 10; Summary of Student Achievement; App M; title (T-14) | written last, so they promise only what was delivered |
| **W7** | W6 done | Verification Mode; Review Mode per chapter; page count; §14 checklist; supervisor draft (guideline 9) | |

**Supervisor touchpoints (guideline 9: "a general layout for approval, then drafts").** Send this
plan's §0.3 and §3.1 as the layout for approval. Then send drafts after W1 (Chs 2–3), W3 (Ch. 6)
and W6 (the full draft).

---

## 12. Risks and fallbacks (the rubric protects well-analysed negative results)

| id | risk | likelihood | fallback in the thesis |
|---|---|---|---|
| TR-1 | G6 NS not green | medium | §8.8 reports Taylor–Green (validation) plus T3 bounds for 10b, "honestly bounded by T3" (Planning G6). §9.6 owns it. If P7 does not run at all, §8.8 becomes Burgers (R9) and NS moves to Future Work |
| TR-2 | fitted degree exponents deviate from 4 and 1 | low–medium | report the measured exponents with fit ranges; restate C-05 as measured |
| TR-3 | "no encoding can beat Θ̃(N⁴)" over-generalises | medium | claim only for polynomial filters of the walk (degree ≥ Ω(√(α_H/Δ))), citing Lin–Tong's gap dependence. A proper lower bound is future work |
| TR-4 | T1 only at n ≤ 2–3 for R2+ | high | already designed for: T2 ≡ T1 is proven and measured; say so once in §4.7 and mark the tiers |
| TR-5 | R3–R6 circuits (lifts, source injection, multi-axis, fold) slip | medium | the reproduction (classical, G1) stands; Pillar-2 evidence for those problems is at T2 with operator verification by IR; §9.6 states the gap |
| TR-6 | the stiff descriptor problem (R2c) needs rescaling to be competitive | certain | a feature, not a bug: §6.5 and §8.6 present it as the descriptor's honest cost |
| TR-7 | page overrun | medium | the §4.1 trim order |
| TR-8 | the Figs 6–7 hypotheses stay open | certain | already decided: recorded as not reproduced, authors not contacted (decision 17) |
| TR-9 | the marker ticks Theoretical after all | low | the formulation chapters already satisfy "journal-article setup"; move 2–3 pp from Ch. 8 to Chs 5–6 |

---

## 13. Front matter and required elements

### 13.1 Title (T-14)

- **Keep:** *Quantum Circuits for Solving Differential Equations via Physics-Informed Effective
  Hamiltonians and GQSP Quantum Imaginary Time Evolution.*
- **Option A:** *Banded Physics-Informed Hamiltonians: A Descriptor Reformulation for Quantum
  Differential-Equation Solvers.*
- **Option B:** *Physics-Informed Hamiltonians for Quantum Differential-Equation Solvers:
  Reproduction, Exact Encoding and a Descriptor Reformulation.*

The title page and both declaration dates use `\today`: set them to the submission date before
submitting.

### 13.2 Abstract (≈ 250–300 words; five moves, each with a number)

1. The problem, and Wu et al.'s method (attributed).
2. What we found about it: an exact reproduction, the encoder wall and the Hamiltonian wall, with
   degrees at n = 8.
3. The descriptor reformulation, with its headline numbers (‖H‖ Θ(N²), degree Θ̃(N), ancilla
   ⌈log₂(n+4)⌉ + 6, same kernel).
4. How it is verified (the tiers, T1 = T2) and how far it extends (Carleman in both forms; 2-D NS).
5. The scope: classical computation, no hardware, and neither form poly-log.

### 13.3 Summary of Student Achievement (one page, first person, required)

Outline exactly what *you* did:

- the rebuild and its design;
- the reproduction and triage of the paper;
- the structured encoding;
- the descriptor reformulation;
- the verification framework;
- the GQSP circuit engine and the readout correction;
- the Carleman and NS extensions;
- the HPC campaigns;
- the thesis.

Name the help received (supervisor; AI coding assistance, if your School's policy requires it to
be declared: check that policy and mirror it in the Acknowledgements, per guideline 8).

### 13.4 Research proposal deviations (Appendix M table)

| proposed (May 2025) | outcome | why |
|---|---|---|
| QSVT → "GQSVT" for complex-valued, non-Hermitian operators | GQSP used throughout (no parity constraint); complex-valued equations not treated | the cost analysis showed the binding constraint is the Hamiltonian's norm, which had to be solved first |
| nonlinear PDEs (Burgers, NLS, Ginzburg–Landau) | Burgers and 2-D NS via Carleman; NLS and CGL not treated | the doubled-space route cannot prepare; Carleman needs dissipativity (NLS is not dissipative) |
| data-informed Hamiltonians | not pursued | scope; future work §10.2 |
| (not proposed) | exact reproduction; structured encoding; descriptor reformulation; verification framework | emerged from auditing the published method |

### 13.5 Seminar (outside the document, noted only)

The seminar is 25 minutes plus 5 minutes of questions, marked on content, presentation and
discussion. Figures F1, F9 and the three-row table T7 carry the talk.

---

## 14. Pre-submission checklist

### 14.1 Content

1. Every §1.3 contribution has a verdict in §10.1 and evidence in Ch. 8.
2. Every Abstract number has a generated macro and a Ch. 8 location.
3. Every claim ID cited in prose is ✅ in `CLAIMS.md` at `results-v1` (§9).
4. There are no "collocation", "O(1) ancilla", "Θ̃(N²) floor" or "not verified end to end"
   statements anywhere (`grep`).
5. Ultraspherical is credited in §2.3 and §6.2.
6. The prepared/projected and simulated/emulated/estimated vocabulary holds throughout (§3.3).
7. The tier is marked on every quantitative figure and table.
8. The research proposal is in Appendix M, with deviations.

### 14.2 Style and presentation (/10: "flawless")

1. `\nocite{*}` removed; zero `\todo`, `\prov`, `\placeholderfigure`, and zero `REVISE` or
   `CITE-NEEDED` comments (`grep -rn` over `1_header 2_body 3_footer`); the bibliography's
   `note` fields stripped or suppressed (`\AtEveryBibitem{\clearfield{note}}`).
   `export_numbers.py --final` succeeds, and the final build has no `pihm` errors (§10.2).
2. Compile clean: no warnings, and no overfull `\hbox` in the body.
3. Every float is referenced by `\Cref`; figure captions below and table captions above; every
   caption stands alone.
4. Acronyms are defined at first use, and the `glossaries` entries are complete (GQSP, QSP, QSVT,
   QITE, LCU, NLFT, IR, QFT, DCT, DNS, IVP, BVP, SVD, PIHM).
5. AU spelling sweep (§10.5); "Wang" spelt correctly; the declaration signed; the supervisor's
   endorsement present.
6. Body 40–60 pages (target 55–58), 12 pt, 1.5–2 cm margins.
7. The whole thesis read aloud once.

### 14.3 Rubric traceability (Modelling)

| criterion | marks | earned in | done |
|---|---|---|---|
| Intro & Lit: state of the art | /20 | Ch. 2, Ch. 3 | ☐ |
| — critical assessment (HD gate) | | §2.2 (table), **§3.6** | ☐ |
| — connection to the project | | §1.2, §3.6 → Chs 5–7 | ☐ |
| Model formulation | /30 | Chs 4–7 | ☐ |
| — software tools | | §4.8, App L | ☐ |
| — model configuration diagram | | F1 (§4.1) | ☐ |
| — input options (BCs etc.) | | §4.2, T2, T3, App J | ☐ |
| — reproducible ("create equivalent models") | | Chs 4–7 + App B–I | ☐ |
| — numerical experiment design | | §4.2, §4.7, §8.1 | ☐ |
| Results & Discussion | /30 | Chs 8–9 | ☐ |
| — self-contained results | | Ch. 8 + App J–K | ☐ |
| — significance for the field | | §9.1–9.5 | ☐ |
| — negative results analysed | | §8.9, §9.3, §9.6 | ☐ |
| Conclusions & further investigation | /10 | Ch. 10 | ☐ |
| Style & presentation | /10 | throughout | ☐ |

---

*Companion documents: `Code/Planning.md` (what is built and why), `Code/Journal.md` (what has been
done), `CLAUDE.md` and `thesis_guides/` (review protocol, style), to be updated per §2 on adoption.*
