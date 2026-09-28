# STRUCTURE_AND_RUBRIC.md — Section Tree, Deliverables, Marker Checklists

Built from the official *Master of Physics Thesis Mark Sheet*
(`Theses-AssessmentRubric.pdf`), the School's *Master Thesis Guidelines*, and the
structural patterns of two high-scoring exemplars (Green 2024; Snow 2026).

Document class: `article`, `\section` at top level, matching `main.tex`.

> **Governing plan (2026-09-25).** `../ThesisPlanning.md` was adopted on
> 2026-09-25 and supersedes this document's framing (§0), project-type hedge (§2),
> page budget (§2.1), section tree (§3), appendix map (§3.2), per-section
> deliverables and checklists (§4) and traceability matrix (§5), as marked at each
> section. The mark-sheet analysis (§1) and the Style & Presentation checklist
> (end of §4) still stand. Where the two documents conflict, `ThesisPlanning.md`
> wins; section numbers below refer to the pre-plan eight-chapter tree.

---

## 0. Framing Decision (locked)

> **Superseded (2026-09-25)** by ThesisPlanning.md §3.1: the descriptor
> reformulation is the headline contribution, with four numbered supporting
> contributions (S1–S4); the paper's regime is the *standard form*, not
> "collocation"; our structured exact encoding of it (S2) is claimed, as a fairness
> device. Kept below for the record.

**The thesis has one contribution: the descriptor reformulation.** Everything else
is either prior art or evidence.

Three consequences, and every structural rule below descends from them:

1. **The physics-informed effective Hamiltonian framework is prior art**
   (Wu et al. 2025, `wu2025pihm`). Since 2026-09-15 it is presented in its own
   chapter, §3, immediately before the descriptor reformulation that responds to it
   — described, attributed, and then **judged**, in the same register attributed
   prior art carries anywhere else in the thesis. It is not a method this thesis
   co-authored, and no sentence of §3 (or any other section) may read as though it
   were. §3 is a *body* chapter only in its physical placement; for the purpose of
   which mark-sheet criterion it earns, it still functions as the critical-assessment
   payload of the Introduction & Literature Review criterion — see the note at the
   end of this section and the Traceability Matrix in §5.
2. **The collocation encoding is the published route's weakness, not a co-equal
   half.** Its failure is *diagnosed* in §3.5 (the critical assessment that gates
   the HD band) and *measured in full* in §6.2, where it is explicitly framed as "we
   implemented and characterised the published route". There is no
   descriptor-versus-collocation comparison chapter, because that framing implies
   ownership of both. FABLE is not discussed anywhere — not even inside §3's own
   description of the published encoding, which describes the data-loading
   mechanism generically (a multiplexed rotation ladder) rather than naming the
   specific published block-encoding algorithm.
3. **Narrative outranks completeness.** The body carries the story: the idea, the
   object stated once, the cost as a formal result, and the interpretation.
   Derivations, entry-level formulae, atom-by-atom constructions, per-case numbers
   and software detail live in the appendices, which do not count against the page
   limit. Equations and figures in the body are *supplementary to the argument* —
   each one must be doing narrative work or it belongs in an appendix.

The one-sentence statement of the contribution, which should be recognisable in the
Abstract, §1.3, §4.2, §6.8 and §8.1:

> Carrying the intermediate derivatives instead of eliminating them converts the
> dense physics-informed residual into a banded one, and the whole
> encoding-and-preparation pipeline inherits the structure.

**Note on the 2026-09-15 restructure.** The version of this document written before
that date located §2.4/§2.4.3 (PIHM description and critical assessment) *inside*
the literature review, on the argument that this is what makes the assessment count
toward the /20 Intro & Lit Review criterion rather than the /30–40 Groundwork
criterion. That placement changed: PIHM now has its own numbered top-level chapter
(§3), for pacing and readability reasons independent of this document. The rubric
argument has not changed, and the risk it was written to avoid has not gone away —
a marker skimming the table of contents sees §3 sitting among the numbered body
chapters and may file it, by position alone, as part of the /30–40 Groundwork
component rather than the /20 Lit Review component it is actually meant to discharge.
**§3's own prose must therefore do, explicitly, what its old position did implicitly**:
open by stating that it presents reported prior art in the register of literature
review, not new contributed work, and close its critical-assessment subsection
(§3.5) by naming, again, that this diagnosis is what motivates §4 — the language a
reader would expect from a literature review's gap statement, not from a methods
chapter. Re-verify this reads correctly at the next full pass; if a marker could
plausibly read §3 as a claim of authorship of the PIHM framework, that costs the
academic-integrity risk named in Trap 13 of `STYLE_GUIDE.md`, not merely a
rubric-category misfile.

---

## 1. The Mark Sheet — What Actually Scores

The thesis is 60% of the unit; within the thesis, marks divide as:

| Criterion | Marks | Top band (HD) requires |
| :-- | --: | :-- |
| **Introduction & Literature Review** | **/20** | "Comprehensive, superior understanding of the historical background and state of the art, **with excellent connection of the current field to the project**" (≥18). Explicitly: *"A critical assessment of the strengths and weaknesses of the material reviewed is required for a high distinction."* |
| **Project Body** | **/60** | Split depends on declared project type — see §2 |
| **Conclusions & Topics for Further Investigation** | **/10** | "Detailed, comprehensive and insightful conclusions **and significant suggestions for further investigation**" (≥9.0) |
| **Style & Presentation** | **/10** | "**Flawless**" = 10.0. "Few insignificant errors" = 8.0–9.9 |

### 1.1 The single most exploitable fact in the rubric

The phrase **"warranting publication in an international peer reviewed journal"**
appears verbatim in the top band of *three* Project Body criteria (Experimental
Method, Modelling Formulation, and both Results & Discussion variants). Publishability
is the literal wording of the highest mark band. Every drafting decision should be
tested against it.

### 1.2 The framing decision is itself worth marks

Treating the PIHM framework as reported literature, judged rather than claimed, is
not only a page-budget move. It converts a structural liability into two rubric
wins, and it does so regardless of which physical chapter carries the material:

- The critical assessment of the published encoding (§3.5) is precisely the
  *"critical assessment of the strengths and weaknesses of the material reviewed"*
  that the /20 criterion names as the **HD gate**. Most candidates write a survey;
  a survey with a verdict that the rest of the thesis then acts on is band 4. This
  only scores under Intro & Lit Review if §3 reads as reviewed literature — see the
  note at the end of §0.
- It leaves the /30–40 groundwork criterion carrying **one** construction rather than
  two: §4 (the descriptor reformulation) is the only chapter presenting a
  contribution this thesis claims, so it can be written at journal depth without the
  page budget collapsing. Focus is itself scored: *"clear focus… capacity to avoid
  the intrusion of less relevant detail."*

### 1.3 Negative and partial results are explicitly protected

Two separate criteria say so:

> "If the results are negative, there will not be a penalty **if a detailed
> discussion/analysis is given**." (Experimental R&D)

> "If there is a null or partial result due to the choice of an ill-posed or overly
> complex problem for the project, this should be noted and progress toward a solution
> detailed. There will be no marks penalty if there is a well justified case."
> (Theoretical R&D)

This licenses every honest caveat the work carries: no hardware execution; GQSP
figures capped at $\dim \lesssim 2000$ by simulation cost; **no measurement protocol
implemented — every reported solution error is a classical state-vector read**; the
$O(\log^2 M)$ transform held as a dense `UnitaryGate`; the structured $F_2$ assembly
unpackaged; the doubled-space route projecting rather than preparing. **Stating these
with analysis costs nothing and evidences the "insight into significance" the top band
demands. Concealing them and being caught costs the band.**

### 1.4 Self-containment is required twice

> "All your results need to be presented in a way that is easy to understand,
> **without reference to any other documents.**"

The thesis cannot lean on `DescriptorVscollocation.md`, the notebooks, or the repo
READMEs. Every number quoted in the body must be derivable from the body **or from an
appendix**. This is what makes the aggressive offloading below safe: the appendices
are part of the document, the repository is not.

---

## 2. ⚠ Declare Your Project Type — This Changes the Page Budget

The marker ticks one category to set the /60 scale:

| Type | Construction/setup component | Results & Discussion component |
| :-- | :-- | :-- |
| **Theoretical** | Groundwork: theory & background for calculations — **/40** | **/20** |
| **Modelling** | Project Process: Model Formulation — **/30** | **/30** |

The project straddles both: a theoretical construction (descriptor reformulation,
block-encoding cost analysis, Carleman lift) validated by numerical modelling
(classical circuit simulation, HPC benchmarks, `DESolverLib` / `desolver_hpc`).

**Resolved (2026-09-25): Modelling** (ThesisPlanning.md decision T-02) —
Model Formulation /30 + Results & Discussion /30. The Modelling criteria, and where
each is met, are ThesisPlanning.md §5.4 and §14.3. The Theoretical wording is kept
below as the fallback if the marker ticks it after all (ThesisPlanning.md §12,
TR-9):

- **Theoretical/4** demands: *"Outstanding description and detail in the background and
  setup of the calculations which follow, as would appear in a well written journal
  article."* Also names, explicitly, *"the notations and conventions that are being
  adopted"* and reproducibility: *"sufficient detail for the reader to be able to
  understand the techniques and/or to be able to reproduce the results."*
- **Modelling/4** demands: *"a description of any software tools used and/or created;
  a description and/or diagram of the model configuration; descriptions of the model
  input options selected."* It also says *"There is no need to include detailed codes,
  which could be included in appendix if desired."*

**In practice (ThesisPlanning.md):** the notation table in the front matter
(T-11); a model a reader could rebuild (Chapters 4–7 + Appendices B–I); the `pihm`
package and the Setonix configuration (§4.8 + Appendix L); a configuration diagram
(Fig. `fig:pipeline`); and every input option and experiment parameter stated (§4.2,
§8.1 + Appendix J).

> **Note on reproducibility under the appendix-heavy structure.** The Theoretical/4
> band asks that a reader be able to *reproduce the results*. It does not ask that
> they be able to do so without turning a page. A body that states the construction
> and points precisely to Appendix E for the atoms satisfies it; a body that states
> the construction and points to the *repository* does not.

### 2.1 Page budget

> **Superseded (2026-09-25)** by ThesisPlanning.md §4.1: ten chapters, 57 pages,
> weighted for the Modelling scale.

The guidelines set 40–60 pages (body, excluding contents, proposal, appendices) with
an explicit marks penalty for overrun. **Target 55–57 pages.**

| Section | Pages | Rubric criterion |
| :-- | --: | :-- |
| §1 Introduction | 4 | Intro & Lit Review /20 |
| §2 Background and Literature Review | 9 | Intro & Lit Review /20 |
| §3 The Physics-Informed Hamiltonian Method | 6 | Intro & Lit Review /20 (see §0 note — body-located, lit-review-scored) |
| §4 The Descriptor Reformulation | 15 | Body: groundwork |
| §5 Extension to Polynomial Nonlinearity | 4 | Body: groundwork |
| §6 Numerical Study | 10 | Body: results & discussion |
| §7 Discussion | 4–5 | Body: results & discussion |
| §8 Conclusions and Future Work | 3–4 | Conclusions /10 |
| **Total** | **~56** | |

Three consequences worth internalising.

**The literature review is leaner than the 2026-09 draft that folded PIHM into it.**
At 9 pages rather than 13, it is closer to the original 9–10 page estimate, because
§2 now carries only the shared preliminaries every method depends on — quantum
computation basics, competing DE-solving routes, classical spectral methods, block
encoding/LCU/qubitisation, QSP/imaginary-time filtering, and readout. The
compensating cut is unchanged: QC preliminaries capped at **two pages**, standard
material in flowing prose, gate table to Appendix A, numbered definitions only for
objects re-invoked later.

**§3 absorbs almost exactly what left §2.** Six pages against zero marks of its own
(it earns marks by discharging part of the Lit Review criterion, not by existing) —
description of the residual construction, the published encoding, this thesis's own
reproduction and measurement of it, and the critical assessment that motivates §4.
If §3 is running long, the numerical-verification subsection (§3.4) is the one to
compress — the full measured table belongs in §6.2 regardless, so §3.4 only needs
the handful of numbers that drive the diagnosis in §3.5, not the complete record.

**§4 is still the thesis.** Fifteen pages against a /30–40 criterion, carrying one
construction. If any section is over budget, it is not this one that gets cut.

---

## 3. LaTeX Section Tree

> **Superseded (2026-09-25)** by ThesisPlanning.md §4.2, which the live
> `2_body/*.tex` files now follow (files `1_introduction.tex` to
> `10_conclusions.tex`). The tree below is the pre-plan one.

Matched the live `2_body/*.tex` files before 2026-09-25.

```latex
% ---------- 2_body/1_introduction.tex  (~4 pp) ----------
\section{Introduction}
  \subsection{Differential Equations as a Target for Quantum Computation}
  \subsection{The Encoding Wall in Physics-Informed Quantum Solvers}
  \subsection{Contributions and Scope}     % numbered; scope statement lives here
  \subsection{Outline}

% ---------- 2_body/2_literature.tex  (~9 pp) ----------
\section{Background and Literature Review}
  \subsection{Quantum Computation Preliminaries}          % <= 2 pp, HARD CAP
      \subsubsection{Quantum Gates and Circuits}
      \subsubsection{Complexity of Quantum Algorithms}
      \subsubsection{Noisy Intermediate-Scale Quantum (NISQ) Era}
  \subsection{Quantum Algorithms for Differential Equations}
      \subsubsection{Linear-Systems and Hamiltonian-Simulation Routes}
      \subsubsection{Variational and Carleman-Linearisation Routes}
      \subsubsection{Critical Assessment}
  \subsection{Classical Spectral Methods and the Chebyshev Basis}
      \subsubsection{Chebyshev Expansion and Differentiation}
      \subsubsection{The Ultraspherical Spectral Method and Banded Differentiation}
  \subsection{Block Encoding, LCU and Qubitisation}
  \subsection{Quantum Signal Processing and Imaginary-Time Filtering}
      \subsubsection{From QSP and QSVT to the Generalised Construction}
      \subsubsection{Ground-State Preparation by Imaginary-Time Filtering}
  \subsection{Readout and Amplitude Amplification}        % ~1/3 pp, prior art only
  \subsection{Synthesis: The Gap This Thesis Addresses}
  \subsection{Notation and Conventions}                   % the table; rubric names it

% ---------- 2_body/3_pihm_collocation.tex  (~6 pp)   <-- PIHM AS ITS OWN CHAPTER,
%                                                          STILL PRIOR ART -- see §0 ----------
\section{The Physics-Informed Hamiltonian Method}
  \subsection{Overview}
  \subsection{The Residual Construction and Its Ground State}
  \subsection{The Published Collocation Encoding}
  \subsection{Numerical Verification: Reproducing and Characterising the Published Encoding}
  \subsection{Critical Assessment: The Encoding Wall}       % THE PIVOT

% ---------- 2_body/4_descriptor.tex  (~15 pp)   <-- THE CONTRIBUTION ----------
\section{The Descriptor Reformulation}
  \subsection{Overview: From Residual to Prepared State}       % pipeline figure
  \subsection{Design Rationale: Carry the Derivatives, Do Not Eliminate Them}
  \subsection{The Banded Factorisation and the Descriptor Residual}
  \subsection{Gate-Level Encoding of the Derivative Atoms}     % ONE section
  \subsection{The Block Encoding: A Single PREPARE/SELECT/PREPARE$^\dagger$}
  \subsection{Cost of the Descriptor Encoding}                 % proposition
  \subsection{Boundary Conditions and Data Injection}
  \subsection{Ground-State Preparation on the Descriptor Hamiltonian}
  \subsection{Extracting the Solution}                         % ~1/2 pp, scoped
  \subsection{Verification: What Is Established, and How}

% ---------- 2_body/5_nonlinear.tex  (~4 pp) ----------
\section{Extension to Polynomial Nonlinearity}
  \subsection{The Carleman Lift onto the Descriptor Path}
  \subsection{The Nodal Product-to-Sum Fold}
  \subsection{The Doubled-Space Route: Coverage and Its Limits}
  \subsection{Preparation Versus Projection}

% ---------- 2_body/6_results.tex  (~10 pp) ----------
\section{Numerical Study}
  \subsection{Experimental Design and Cost Conventions}
  \subsection{The Published Collocation Encoding, Reproduced and Characterised}
  \subsection{Encoding Cost of the Descriptor Construction}
  \subsection{Spectral Gap and Success Probability}
  \subsection{Solution Accuracy on Representative Problems}     % THREE cases
  \subsection{Nonlinear Benchmarks}
  \subsection{An Application Case Study}                        % ONE of BS / NS
  \subsection{Summary of Findings}

% ---------- 2_body/7_discussion.tex  (~4-5 pp) ----------
\section{Discussion}
  \subsection{Why the Trade-off Exists}
  \subsection{End-to-End Complexity: The Query Floor}
  \subsection{Where This Construction Applies, and Where It Does Not}
  \subsection{Feasibility on Near-Term and Early Fault-Tolerant Hardware}
  \subsection{Limitations}

% ---------- 2_body/8_conclusions.tex  (~3-4 pp) ----------
\section{Conclusions and Future Work}
  \subsection{Conclusions}
  \subsection{Future Work}
```

### 3.1 What changed, and when

1. **2026-09 (original narrative-first pass).** `3_formulation.tex` was retired.
   Its notation table moved to §2.9; the PIHM construction and the collocation
   encoding moved into the literature review as §2.4 prior art; the gate-level
   derivative atoms moved into the descriptor chapter as its own subsection; the
   spectral-gap collapse became §2.4.3 (diagnosis) plus a results-chapter subsection
   (measurement). FABLE was excluded from the narrative entirely. Eight sections
   became seven, and the descriptor section moved from §4 to §3.
2. **2026-09-15 (this restructure).** PIHM and the collocation encoding moved back
   out of the literature review into their own numbered chapter, §3
   (`2_body/3_pihm_collocation.tex`), pushing every later section down by one
   (descriptor §3→§4, nonlinearity §4→§5, results §5→§6, discussion §6→§7,
   conclusions §7→§8). The rubric argument for treating PIHM as reviewed literature
   did not change — see the note at the end of §0 for what this means for how §3
   must read.
3. **Readout is prior art plus a half-page scope statement.** §2.7 covers the
   primitives and quotes their costs; §4.9 states what the pipeline hands you and
   says plainly that no measurement protocol is implemented here. It reappears only
   in §7.5 (Limitations) and §8.2 (Future Work). It is never presented as
   contributed work.
4. **`\nocite{*}` and all `\todo` notes must go before submission.** `\nocite{*}`
   currently pulls every entry in `ref.bib` into the bibliography whether cited or
   not — a visible presentation failure under the /10 Style criterion.

### 3.2 Appendices — the load-bearing half of this structure

> **Superseded (2026-09-25)** by ThesisPlanning.md §6 (Appendices A–M, one file
> each under `3_footer/appendices/`). The pointer rule below still stands.

Appendices are **not counted in the page limit**, and both rubric variants explicitly
invite them (*"If there is insufficient room, appendices should be included"*; *"no
need to include detailed codes, which could be included in appendix"*). Under the
narrative-first structure they are not an overflow bin; they are where the thesis
discharges its reproducibility obligation.

| | Appendix | Referenced from |
| :-- | :-- | :-- |
| A | Quantum gate reference table | §2.1.2 |
| B | Chebyshev and ultraspherical identities; $G$, $\tilde{B}$, $\tilde{D}$ entries | §3.2, §4.3 |
| C | The published collocation residual (worked $N=4$ instance) and the lifting operator $M_{x^p}$ | §3.2 |
| D | The published encoding circuit and its error bound: ladder angle formulas, the proved $\epsilon_G$ bound, ancilla count | §3.3 |
| E | The descriptor construction in full: derivative atoms, composition algebra | §4.4, §4.5 |
| F | Proof of the cost proposition | §4.6 |
| G | The nonlinear route in full: Carleman lift, nodal fold, doubled-space algebra | §5 |
| H | Verification protocol and per-atom residuals | §4.10 |
| I | Catalogue of all DE cases solved, with parameters and status | §6.5–§6.7 |
| J | Readout protocols and their quoted costs | §4.9 |
| K | Software: `DESolverLib` / `desolver_hpc`, Setonix configuration | §6.1 |
| L | **Research proposal** — required by the guidelines, with deviations noted | — |

**The pointer rule.** Every appendix reference in the body must carry a reason, never
a bare cross-reference: not *"see Appendix E"* but *"the atom-by-atom constructions,
and the column-by-column residuals establishing each, are given in Appendix E"*. A
body that offloads without saying what was offloaded reads as evasive; one that names
what is there reads as disciplined.

**Appendix B stays descriptor/shared-identity scoped; §3's own apparatus lives in C
and D.** §3.2 states $G$'s own closed-form entries directly in the body, cited to
Trefethen as classical fact, rather than deriving them via the descriptor's own
$G=\tilde B^{-1}\tilde D$ factorisation — so it does not depend on that derivation's
own framing. It points into Appendix B's *"The $N=4$ instance"* subsection for a
concrete look at $G$'s fill-in. The PIHM-specific apparatus that a 2026-09-15 pass
had added into Appendix B (the $\{1,5,400\}$ worked collocation-residual example,
the lifting operator $M_{x^p}$'s own entries, and the ladder circuit's angle
formulas and proved $\epsilon_G$ bound) was moved out into two dedicated
appendices — C (*"The Published Collocation Residual and the Lifting Operator
$M_{x^p}$"*) and D (*"The Published Encoding Circuit and Its Error Bound"*) —
keeping B to the shared Chebyshev/ultraspherical identities both §3 and §4 build
on, and giving the PIHM-only apparatus its own small, precisely scoped home. $M_{x^p}$
(rectangular, exact, Appendix C) is distinct from the descriptor's own square,
truncated $M_{x^q}$ (Appendix E's "Higher order, variable coefficients" subsection)
— do not conflate the two.

---

## 4. Section Purpose, Deliverables, and Marker Checklists

> **Superseded (2026-09-25)** by ThesisPlanning.md §5 (one entry per chapter) and by
> the scaffold comments in each `.tex` file. The closing *Style & Presentation*
> subsection still stands, and is carried into ThesisPlanning.md §14.2.

---

### §1 Introduction — *Intro & Lit Review /20*

**Purpose.** Establish that the problem matters, that it has a specific unsolved
component, and that this thesis solves that component. The HD wording — *"excellent
connection of the current field to the project"* — means the introduction must not
merely survey; it must converge.

**Deliverables**
- A concrete opening: what breaks if differential equations cannot be solved on
  quantum hardware, with citations to the application domains.
- The bottleneck stated **quantitatively**: the $\Theta(N^2)$-gate, $(n{+}3)$-ancilla,
  $\alpha \approx \Theta(N^8)$ figures of the published encoding, and the
  machine-epsilon gap consequence — developed in full in §3, attributed there as the
  published route's cost, not presented here as an anonymous state of nature.
- Numbered contributions, each one sentence of *what* and one clause of *evidence*.
- **Scope, stated once and plainly, inside §1.3**: results are classical simulations
  of the pipeline, not hardware executions; no measurement protocol is implemented.
  Saying it here inoculates the whole thesis.
- Outline: one bullet per section, each naming the section's job — including §3 as
  reviewed prior art, distinct from §4's contributed construction.

**Marker checklist**
1. Can a non-specialist physicist state the problem after two pages?
2. Is the gap specific enough that a referee could check whether it is real?
3. Are the contributions numbered, and is each one falsifiable?
4. Does at least one quantitative figure appear before the end of page 2?
5. Is the scope statement — classical simulation, classical readout — explicit?
6. Is the published framework attributed at first mention, not first *critique*?
7. Does the outline match the actual section headings verbatim, and does it mark §3
   as prior art rather than as a second contribution?

---

### §2 Background and Literature Review — *Intro & Lit Review /20*

**Purpose.** Demonstrate command of the state of the art **and judge it**. The
rubric is unambiguous: *"A critical assessment of the strengths and weaknesses of
the material reviewed is required for a high distinction."* A survey without
verdicts caps at band 2–3 (11.0–17.9). Since 2026-09-15 this section carries only
the *shared* preliminaries — the PIHM-specific critical assessment that used to live
here (§2.4/§2.4.3) is now §3, and §2 hands the reader to it rather than absorbing it.

**Deliverables**
- **Compressed QC preliminaries, two pages, hard cap.** Numbered definitions only for
  objects reused later. Gate table to Appendix A. Cite Nielsen & Chuang and move on.
- For **each** competing family of DE algorithms: what it assumes, what it costs, and
  **where it fails**. Every method gets an explicit failure-mode sentence.
- **§2.3.2 — the ultraspherical antecedent, credited here.** The descriptor basis
  change is the discrete shadow of the ultraspherical spectral method (Olver &
  Townsend 2013). State it in the literature review, *before* §4 claims anything,
  then state precisely what the increment is: applying it to the physics-informed
  residual so the whole encode-and-prepare pipeline inherits bandedness, and showing
  the certified solution is unchanged. Pre-empting *"isn't this just ultraspherical?"*
  is worth more than hoping it is not asked.
- Block encoding, LCU, qubitisation, and QSP/QSVT/imaginary-time filtering as general
  prior art, at the depth §3 and §4 both need to build on without re-deriving.
- §2.7 readout as prior art only: the primitives, their quoted costs, one third of a
  page. No claim of implementation appears anywhere in this thesis.
- **§2.8 — a closing gap subsection.** Under the current structure this hands the
  reader to §3 rather than posing the descriptor gap directly: *the physics-informed
  effective Hamiltonian framework of \cite{wu2025pihm} is examined next, on the same
  attributed footing as the material above, before this thesis's own reformulation
  is introduced.* The actual open-question framing (*"can the residual be
  block-encoded without the $\Theta(N^2)$ cost, and with a gap that survives double
  precision?"*) is now posed at the *end* of §3 (§3.5), immediately before §4
  answers it — see `STYLE_GUIDE.md` §4.1, updated for this ordering.
- **§2.9 — the notation and conventions table.** The Theoretical rubric names this
  requirement explicitly. Fix $n$, $N = 2^n$, $k$, $p$, $\alpha$, $\Delta$, $G$,
  $\tilde{B}$, $\tilde{D}$, $A$, $A_\mathrm{sys}$, $H$, $H_\mathrm{sys}$,
  $\epsilon_G$, $M$. Placing it at the end of §2 makes it the handoff into §3.
  (Currently `1_header/6_notation.tex` uses bare $A$ and bare $H$ for both regimes,
  distinguished only by the surrounding chapter; the table's own header row says $A$
  is "dense in the collocation route, banded in the descriptor route" — deliberate,
  but worth a sentence in §2.9 saying so explicitly, since §4 will otherwise also
  write bare $A$ for its own, differently-shaped residual.)

**Marker checklist**
1. Does every reviewed method carry an explicit weakness, not just a description?
2. Is there a comparison table of DE approaches with a "this work" row?
3. Is the ultraspherical antecedent credited in §2.3.2, before §4 claims anything?
4. Is §2.1 ≤ 2 pages?
5. Does §2.8 hand the reader to §3 with a reason, rather than re-deriving PIHM here?
6. Is any subsection present that no later section depends on? Cut it.
7. Are all citations formatted consistently (IEEE style, via `biblatex`)?

---

### §3 The Physics-Informed Hamiltonian Method — *Intro & Lit Review /20, body-located*

**Purpose.** Present Wu et al.'s physics-informed effective Hamiltonian framework and
its published collocation encoding, at journal-review depth, then diagnose exactly
where it fails. This section earns marks under the **Introduction & Literature
Review** criterion, not Project Body — see the note at the end of §0. It is written
in the register of attributed description throughout: every non-trivial claim traces
to `wu2025pihm`, and first-person-plural "we" is reserved for what this thesis itself
reproduced, measured, or derived (the reconstructed circuit, its verification, the
rigorous error bound on $\epsilon_G$), never for the framework itself.

**Deliverables**
- **§3.1 — Overview, half a page.** The three-ingredient move in words (solution as
  coefficient vector; constraint as annihilation by an operator; Hamiltonian whose
  ground state is the solution), then one sentence naming what the rest of the
  chapter does and why it matters to §4.
- **§3.2 — the residual construction, math only.** $G$'s defining action and its
  density (entries to Appendix B), the constant-coefficient residual $A$, then the
  variable-coefficient case developed properly: the product-to-sum identity, the
  lifting operator $M_{x^p}$'s definition and rectangular exactness (entries to
  Appendix C), and the general row $A = \sum_j M_{a_j}G^{\top j}$. Boundary/initial
  conditions as invariant-versus-regular data constraints, and $H = A^\top A +
  \sum_i B_i^\top B_i$ as the object whose ground state is the solution. Include,
  briefly and critically, Wu et al.'s own doubled-space nonlinear extension and its
  degenerate kernel — this is prior-art content Wu et al. published, not this
  thesis's Carleman route (§5), and the distinction must be unmistakable. No
  measured numbers and no worked numeric instances belong in this subsection —
  they live in Appendix C and in §3.4.
- **§3.3 — the published encoding.** Why a matrix with $\Theta(N)$ distinct
  values per column resists a compact structured encoding; Wu et al.'s own
  small-angle rotation ladder, described mechanistically (SO(2) angle addition, a
  first-order Taylor approximation to a linear amplitude) without naming any
  third-party block-encoding algorithm — a circuit figure (placeholder until drawn)
  showing the ladder's structure; this thesis's own gate-for-gate reconstruction,
  its exact-reference verification, and the rigorously derived $\epsilon_G =
  O(N^{-5})$ bound that makes the source paper's qualitative claim quantitative —
  an assertable, measured result, distinct from the framework it characterises.
  Full mechanism, proof and ancilla count to Appendix D.
- **§3.4 — numerical verification, compressed.** The two-stage verification
  protocol (atoms to $10^{-9}$–$10^{-11}$, composition to $<10^{-10}$), the explicit
  hedge that the composed $H$ is not verified end-to-end, and only the handful of
  headline numbers ($\alpha \sim \Theta(N^4)$ per atom, $\alpha_H \approx
  \Theta(N^8)$, $p_\mathrm{succ} \to 0$ like $N^{-3/2}$, the gap collapse at
  $n \gtrsim 7$, the measured degenerate-kernel fraction for the nonlinear
  extension) that the diagnosis in §3.5 actually needs — a two-panel figure
  (placeholder until drawn) carrying the $\alpha_H$ and gap-collapse numbers. The
  complete measured table, with every case, is §6.2's job — point to it by name,
  not by a bare cross-reference.
- **§3.5 — critical assessment: the encoding wall.** The structural diagnosis
  (dense $G$ → Gram-squared $\alpha$ → polynomial blow-up), the query-floor argument
  stated *here* in preliminary form (developed fully in §7.2), and the numerically
  fatal consequence — the collapsed gap — as the section's closing, most severe
  finding. Close with the pivot sentence naming §4 by name and by what it changes.

**Marker checklist**
1. Could a reader mistake any sentence in this chapter for a claim of authorship of
   the PIHM framework? Rewrite it if so — this is Trap 13 of `STYLE_GUIDE.md`, and it
   is a harder trap to avoid now that the material sits in a numbered body chapter.
2. Is `wu2025pihm` attributed at the head of §3.2 and again at each specific
   construction (the residual, the boundary-condition generator, the doubled-space
   nonlinear extension)?
3. Is the doubled-space nonlinear extension clearly Wu et al.'s own published
   construction, and clearly distinguished from this thesis's Carleman route in §5?
4. Does §3.3 avoid naming any specific published block-encoding algorithm, per the
   locked framing decision, while still being precise about the mechanism and its
   cost?
5. Are the results attributed to this thesis's own reproduction (the gate-for-gate
   reconstruction, the verification, the derived $\epsilon_G$ bound) kept
   grammatically distinct from results attributed to Wu et al.?
6. Does §3.4 stop at the handful of numbers §3.5 needs, with the full table pointed
   to §6.2 by name?
7. Does §3.5 close with the same pivot sentence (or a close paraphrase) that §0
   fixes, naming §4 explicitly?
8. Is the chapter six pages or fewer? If not, §3.4 is the subsection to compress.

---

### §4 The Descriptor Reformulation — *Body: groundwork* — **the core**

**Purpose.** This section carries the thesis. Under the Theoretical scale it is the
heart of a /40 criterion whose top band reads *"as would appear in a well written
journal article."* Write it as the methods section of a PRA submission.

**The narrative rule for this section.** The body carries four things and offloads
the rest: **the idea** (in words, before algebra), **the object** (stated once, not
derived), **the cost** (as a formal proposition), and **the interpretation** (what it
means operationally). Entry-level formulae, atom-by-atom constructions and proofs go
to Appendices B, E–F. Test each equation: *does the argument break if a reader skips it?*
If not, it is an appendix equation.

**Deliverables**
- **§4.1 — a pipeline figure and one page of narrative.** The spine: residual →
  banded factorisation → block encoding → imaginary-time filter → solution. Every
  later subsection is a stage of this figure. A marker who reads only this page should
  be able to state what the thesis does.
- **§4.2 — design rationale before mechanism.** One paragraph, in words, on why
  carrying $f', f''$ buys bandedness. Then, and only then, the algebra.
- **§4.3 — the factorisation.** $G = \tilde{B}^{-1}\tilde{D}$ with $\tilde{B}$ banded,
  and the resulting block structure of $A_\mathrm{sys}$. State the Hilbert-space cost
  ($\lceil\log_2(k{+}1)\rceil$ extra qubits, $2^{\lceil\log_2(k+1)\rceil}\!\cdot\!N$
  versus $N$) in the same breath as the benefit — volunteering the cost is what makes
  the benefit credible. Entries of $\tilde{B}$, $\tilde{D}$ to Appendix B, alongside
  $G$'s own entries used already in §3.2.
- **§4.4 — the derivative atoms, as one section.** Name the atoms, tabulate them
  (arity, gate cost, ancilla, verified residual), and show **one** representative
  circuit. The Chebyshev feature map, the differential operator, the data constraints
  and the net operator are rows in that table, not four `\paragraph`s of derivation.
  Full constructions to Appendix E.
- **§4.5 — the block encoding** as a single flat `PREPARE/SELECT/PREPARE`$^\dagger$
  LCU, with a `quantikz` figure and an `algorithm2e` listing followed by a
  line-referenced walkthrough.
- **§4.6 — a formal cost result.** A proposition with a proof: gate count $O(n^2)$,
  ancilla $O(1)$ (9–10, flat in $n$), $\alpha_A \to \|A_\mathrm{sys}\|_2$ and hence
  $\alpha_H \to \|H_\mathrm{sys}\| = \Theta(N^2)$ — stated so the contrast with §3.4's
  $\alpha_H \approx \Theta(N^8)$ is legible without a comparison table this early.
  Proof to Appendix F; **two paragraphs of operational interpretation stay in the
  body.** A proposition without interpretation is a formula; with it, it is a result.
- **§4.7** — boundary conditions and rank-one PDE datum injection.
- **§4.8** — GQSP-QITE applied to $H_\mathrm{sys}$: filter design, degree, and why the
  recovered gap makes the filter viable. GQSP itself is prior art (§2.6) and is not
  re-derived here.
- **§4.9 — extracting the solution, half a page.** What the pipeline hands you; what a
  hardware read would cost, quoted from cited work; and the explicit statement that no
  measurement protocol is implemented in this thesis and every error reported in §6 is
  a classical state-vector read. Protocols and costs to Appendix J.
- **§4.10 — verification methodology, stated as a limitation.** Correctness is
  compositional: atoms verified column-by-column to $10^{-9}$–$10^{-11}$, the
  `lcu_sum`/`gram` recipe to $<10^{-10}$; the composed $H$ is *not* verified
  end-to-end because at 22+ qubits a dense simulation allocates hundreds of GB. Say
  this here rather than letting a marker find it.

**Marker checklist**
1. Could a referee re-derive $A_\mathrm{sys}$ from the body plus Appendices B, E?
2. Does every appendix pointer say what is in the appendix and why?
3. Is the cost result formally stated *and* interpreted operationally in the body?
4. Is the Hilbert-space penalty volunteered alongside the gate-count win?
5. Is the ultraspherical antecedent re-acknowledged at the point of construction?
6. Is the verification argument complete, including what is *not* verified and why?
7. Does §4.1's figure let a marker state the thesis after one page?
8. Does every body equation survive the test *"does the argument break without it?"*
9. Is exactness stated precisely (exact, bar the `mult_matrix_square` truncation at
   $\sim 10^{-13}$ for variable coefficients)?
10. Does §4.9 leave any impression that readout was implemented? It must not.
11. Does $A$ here read as unambiguously distinct from §3's dense $A$ — by an explicit
    subscript ($A_\mathrm{sys}$), a reminder sentence, or both?

---

### §5 Extension to Polynomial Nonlinearity — *Body: groundwork*

**Purpose.** Show the structural move generalises. Also where the
preparation/projection distinction must be made unmissable. Four pages: this is a
narrative beat, not a second contribution chapter. Derivations to Appendix G.

**Deliverables**
- The Carleman lift onto the linear descriptor path; the dissipativity condition
  $\mathrm{Re}\,\lambda(F_1) < 0$ stated **as a precondition**, not buried; why it
  yields a genuine 1-D kernel and therefore a real preparation claim; that it stays
  linear in $N$.
- The nodal fold $n_1$: zero ancilla, $\alpha = 2^{p\ell/2}$, and — stated explicitly —
  that for the quadratic case $\alpha = 2 = \|n_1\|$ exactly, so the encoding is
  **optimal, not merely tight**. Verified as an operator to $\sim10^{-15}$.
- The doubled-space route: what it covers that nothing else does (steady, two-point
  BVP, centre-type), and its honest status — it *projects* a classically-known target
  into a degenerate kernel; it does not prepare. One sentence distinguishing this
  route from §3.2's mention of Wu et al.'s own doubled-space nonlinear PIHM: this
  chapter's doubled-space route is applied to the *descriptor* residual, not the
  dense collocation one, even where both share the projection-not-preparation defect.
- A subsection drawing the preparation/projection line explicitly, naming which route
  sits on which side.
- What is not gate-level as shipped: the $O(\log^2 M)$ transform held as a dense
  `UnitaryGate` (Klappenecker–Rötteler cited), and the structured $F_2$ assembly as a
  caller-supplied hook.
- One sentence connecting back to §4.2's structural principle. The reader should see
  this section as the same idea applied again, not as new machinery.

**Marker checklist**
1. Is "prepared" never used where "projected" is meant?
2. Is the dissipativity precondition stated as a precondition?
3. Is the fold's optimality claim distinguished from mere tightness?
4. Are the unpackaged components named, with the honest reason?
5. Does this section connect back to §4's structural principle explicitly?
6. Is the doubled-space route here kept distinct from Wu et al.'s own doubled-space
   nonlinear extension in §3.2?
7. Is it within four pages, with the algebra in Appendix G?

---

### §6 Numerical Study — *Body: results & discussion*

**Purpose.** Evidence every claim. The top band demands *"complete, clearly presented
results"* understandable *"without reference to any other documents."*

**Deliverables**
- **§6.1 — cost conventions first.** What counts as a gate, which decomposition is
  assumed, how ancilla are counted, and **which direction the convention biases the
  comparison** — declare it conservative for the descriptor construction, so any
  advantage reported is a lower bound. The two scope statements live here too:
  simulations capped at $\dim \lesssim 2000$ by simulation cost *and not by the
  algorithm*, and every solution error a classical state-vector read. Name
  `DESolverLib` / `desolver_hpc` / Setonix; detail to Appendix K.
- **§6.2 — the published route, reproduced and characterised, in full.** This is the
  complete measured evidence for the §3.5 diagnosis, and it is *your* work: you
  implemented the published encoding and measured where it fails. Frame it exactly
  that way — a reproduction, not a rival. §3.4 already gave the handful of numbers
  the diagnosis needs; this subsection gives the rest — every case, the gap-collapse
  figure across the full range of $n$ tested ($\sim10^{-15}$ against
  $\epsilon_\mathrm{mach}$ at $n \gtrsim 7$), and the per-case table Appendix I backs.
- **§6.3 — the headline table**: gates, ancilla, $\alpha$, exactness, gap, for the
  published encoding versus the descriptor construction. Two rows, not three; FABLE
  does not appear.
- **§6.4** — gap and success probability: $\sim10^{-6}$ against $\sim10^{-15}$;
  $p_\mathrm{succ} \to \Theta(1)$ against $N^{-3/2}$ Haar-average.
- **§6.5 — three representative cases only**, carried in depth: one linear ODE, one
  PDE, one coupled or variable-coefficient case. Every remaining case goes into
  Appendix I with a pointer. This discipline keeps you under 60 pages while
  *increasing* the mark — a catalogue reads as unfocused, and focus is scored.
- **§6.6** — nonlinear benchmarks, evidencing §5.
- **§6.7 — one application case study.** Black–Scholes *or* Navier–Stokes, not both.
- Solution fidelity against classical baselines, including the
  $\cos\mathrm{sim} = 1.000000$ agreement of the descriptor $a$-block with the
  original Chebyshev solution.
- **§6.8 — numbered summary of findings**, 4–6 items, at least one a limitation of the
  descriptor construction itself (the Hilbert-space growth
  $2^{\lceil\log_2(k+1)\rceil}\!\cdot\!N$ versus $N$; the doubled-space route
  projecting rather than preparing).

**Marker checklist**
1. Is every figure interpreted in prose, not merely displayed?
2. Are all experimental parameters stated in the body or an appendix?
3. Is the cost convention stated *before* the first comparison, with its bias named?
4. Are "we could not simulate it" and "the algorithm cannot reach it" kept distinct
   everywhere they arise?
5. Is §6.2 framed as a reproduction of published work, never as a rival method, and
   does it avoid re-deriving what §3.3/§3.4 already established?
6. Are the in-depth cases ≤ 4, with the remainder in Appendix I?
7. Does each figure caption stand alone?
8. Do the numbered findings include at least one negative or limiting result?
9. Does every claim in the Abstract have a number in this section backing it?

---

### §7 Discussion — *Body: results & discussion*

**Purpose.** Demonstrate *"insight into the significance of the work"* — the phrase
separating band 3 from band 4. Description belongs in §6; §7 must explain and judge.

**Deliverables**
- Why the trade-off exists structurally: the descriptor construction buys bandedness
  and gap health by spending Hilbert space.
- **§7.2 — the query-floor argument, in your own voice, developed fully.** §3.5
  already states this argument in preliminary form to motivate §4; here it is
  completed: neither the published route nor this one is poly-log — $\alpha_H \ge
  \|H_\mathrm{sys}\| = \Theta(N^2)$ against $\Delta = \Theta(1)$ forces
  $\tilde\Theta(N^2)$ queries for *any* block encoding of this $H$. The descriptor
  construction **meets** that floor at $\tilde\Theta(N^2\,\mathrm{poly}\,n)$ total
  gates; the published collocation encoding misses it by $\approx N^6$. Making this
  argument yourself converts the largest vulnerability into evidence of command.
- Where the construction applies and where it does not — a guide a practitioner could
  act on.
- NISQ / early fault-tolerant feasibility, grounded in the ancilla and depth numbers.
- **§7.5 Limitations**, as its own subsection: no hardware execution;
  simulation-capped dimensions; compositional-only verification of the composed $H$;
  the unpackaged $F_2$ assembly and the dense `UnitaryGate` transform; **no
  measurement protocol implemented**; the projection-not-preparation status of the
  doubled-space route (both Wu et al.'s, §3.2, and this thesis's own, §5).

**Marker checklist**
1. Does this section explain rather than restate §6?
2. Is the query-floor argument completed here, consistent with its preliminary
   statement in §3.5, rather than introduced as if for the first time?
3. Are the limitations owned, each with its analysis attached (the rubric's condition
   for no penalty)?
4. Are consequences *for the field* discussed, not just for this project?
5. Is there actionable guidance a practitioner could follow?

---

### §8 Conclusions and Future Work — *Conclusions /10*

**Purpose.** The top band requires *"detailed, comprehensive and insightful
conclusions **and significant suggestions for further investigation**."* Both halves
are marked; a strong conclusion with a thin future-work paragraph caps at ~7/10.

**Deliverables**
- Conclusions tied back to the objectives as stated in §1 — the rubric says they
  *"relate back to the original goal of the report."* Mirror §1.3's numbered
  contributions and report the outcome of each.
- Quantitative recap: the headline figures, once more, compactly.
- **Substantive future work**, each item with a stated reason and a first step. Not
  "extend to more equations" but: implement a measurement protocol and validate the
  readout cost quoted in §4.9; package the structured $F_2$ assembly for a concrete
  PDE; realise the $O(\log^2 M)$ transform gate-level rather than as a dense
  `UnitaryGate`; hardware validation on a small instance.
- A closing sentence stating the transferable principle, not merely the result.

**Marker checklist**
1. Does every §1.3 contribution get a verdict here?
2. Are 3–5 future directions given, each with motivation and a concrete first step?
3. Is anything claimed here that was not evidenced in §6?
4. Is the transferable principle stated?
5. Is the section free of new results or new citations?

---

### Style & Presentation — */10, "Flawless" for full marks*

Only *"flawless"* earns 10.0; *"few insignificant errors"* caps at 9.9. Two marks are
available for proofreading alone — the cheapest marks in the rubric.

**Already present in the draft — fix these:**
1. `1_header/2_acknowledgments.tex`: "Jingbo **Want**" → "Jingbo **Wang**". A
   misspelled supervisor's name on page i is the worst possible first impression.
2. `2_body/2_literature.tex`: a stray `` `' `` after `\end{pmatrix}` in the State
   Space definition renders as spurious quote marks in the first equation.
3. Same file: "initial**ized**" in the Ancillary Qubits definition, against
   `[australian]{babel}`. Sweep for `-ize`/`-ized`/`-ization` throughout.
4. `main.tex`: `\nocite{*}` will pull every `ref.bib` entry into the bibliography.
5. Outstanding `\todo` notes across `2_literature.tex`, `4_descriptor.tex` and
   `main.tex`.

**Pre-submission sweep**
1. Compile clean — zero warnings, no overfull `\hbox` in the body.
2. Every figure and table referenced in the text via `\Cref`, none orphaned.
3. Captions: figures below, tables above, consistently.
4. Consistent symbol usage — run Verification Mode (see `CLAUDE.md`). In particular:
   confirm $A$ and $H$ are unambiguous between §3 (dense/collocation) and §4
   (banded/descriptor) at every occurrence, not only where a subscript is present.
5. All acronyms defined at first use; `glossaries` entries complete.
6. Bibliography uniform; no "et al." inconsistencies; arXiv IDs where applicable.
7. Page count within 40–60; declaration page signed; Summary of Student Achievement
   present, one page, first person.
8. Read the whole thesis aloud once. It is the only reliable way to catch the
   register slips the /10 is scoring.

---

## 5. Pre-Submission Traceability Matrix

> **Superseded (2026-09-25)** by ThesisPlanning.md §9 (claims → thesis) and §14.3
> (rubric traceability, Modelling scale).

| Criterion | Marks | Where it is earned | Done |
| :-- | --: | :-- | :-- |
| Historical background & state of the art | /20 | §2.2–§2.7, §3 | ☐ |
| — critical assessment (HD gate) | | §2.2.3, **§3.5**, §2.8 | ☐ |
| — connection to the project | | §1.2, §3.5, §2.8 | ☐ |
| — prior art correctly attributed | | §2.3.2, §3 (throughout) | ☐ |
| Groundwork / model formulation | /30–40 | §4, §5 | ☐ |
| — notation & conventions | | §2.9 | ☐ |
| — reproducibility | | §4 + Appendices B, E–F | ☐ |
| — software tools created | | §6.1 + Appendix K | ☐ |
| Results & Discussion | /20–30 | §6, §7 | ☐ |
| — significance for the field | | §7.1–§7.4 | ☐ |
| — negative results with analysis | | §6.8, §7.5 | ☐ |
| Conclusions | /10 | §8.1 | ☐ |
| — further investigation | | §8.2 | ☐ |
| Style & presentation | /10 | throughout | ☐ |

---

*Companion documents: `STYLE_GUIDE.md` (tone, exposition, common traps),
`../CLAUDE.md` (interactive review protocol).*
