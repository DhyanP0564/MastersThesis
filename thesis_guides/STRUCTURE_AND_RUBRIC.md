# STRUCTURE_AND_RUBRIC.md — Section Tree, Deliverables, Marker Checklists

Built from the official *Master of Physics Thesis Mark Sheet*
(`Theses-AssessmentRubric.pdf`), the School's *Master Thesis Guidelines*, and the
structural patterns of two high-scoring exemplars (Green 2024; Snow 2026).

Document class: `article`, `\section` at top level, matching `main.tex`.

---

## 0. Framing Decision (locked)

**The thesis has one contribution: the descriptor reformulation.** Everything else
is either prior art or evidence.

Three consequences, and every structural rule below descends from them:

1. **The physics-informed effective Hamiltonian framework is prior art**
   (Wu et al. 2025, `wu2025pihm`). It is presented in the literature review at the
   same depth and in the same register as GQSP — described, attributed, and then
   **judged**. It is not a method this thesis co-authored, and no section of the body
   may read as though it were.
2. **The collocation encoding is the published route's weakness, not a co-equal
   half.** Its failure is *diagnosed* in §2.4.3 (the critical assessment that gates
   the HD band) and *measured* in §5.2, where it is explicitly framed as "we
   implemented and characterised the published route". There is no
   descriptor-versus-collocation comparison chapter, because that framing implies
   ownership of both. FABLE is not discussed anywhere.
3. **Narrative outranks completeness.** The body carries the story: the idea, the
   object stated once, the cost as a formal result, and the interpretation.
   Derivations, entry-level formulae, atom-by-atom constructions, per-case numbers
   and software detail live in the appendices, which do not count against the page
   limit. Equations and figures in the body are *supplementary to the argument* —
   each one must be doing narrative work or it belongs in an appendix.

The one-sentence statement of the contribution, which should be recognisable in the
Abstract, §1.3, §3.2, §5.8 and §7.1:

> Carrying the intermediate derivatives instead of eliminating them converts the
> dense physics-informed residual into a banded one, and the whole
> encoding-and-preparation pipeline inherits the structure.

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

Moving the PIHM framework into the literature review is not only a page-budget move.
It converts a structural liability into two rubric wins:

- The critical assessment of the published encoding (§2.4.3) is precisely the
  *"critical assessment of the strengths and weaknesses of the material reviewed"*
  that the /20 criterion names as the **HD gate**. Most candidates write a survey;
  a survey with a verdict that the rest of the thesis then acts on is band 4.
- It leaves the /30–40 groundwork criterion carrying **one** construction rather than
  two, so the descriptor section can be written at journal depth without the page
  budget collapsing. Focus is itself scored: *"clear focus… capacity to avoid the
  intrusion of less relevant detail."*

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

**Action: ask your supervisor which category will be ticked.** Until you know, write
to satisfy both — the requirements are compatible:

- **Theoretical/4** demands: *"Outstanding description and detail in the background and
  setup of the calculations which follow, as would appear in a well written journal
  article."* Also names, explicitly, *"the notations and conventions that are being
  adopted"* and reproducibility: *"sufficient detail for the reader to be able to
  understand the techniques and/or to be able to reproduce the results."*
- **Modelling/4** demands: *"a description of any software tools used and/or created;
  a description and/or diagram of the model configuration; descriptions of the model
  input options selected."* It also says *"There is no need to include detailed codes,
  which could be included in appendix if desired."*

**The union, in practice:** a notation-and-conventions table (§2.9), a construction a
referee could re-derive (§3 + Appendices B–D), a named description of `DESolverLib` /
`desolver_hpc` and the Setonix configuration (§5.1 + Appendix I), and every numerical
experiment's parameters stated (§5.1 + Appendix G).

> **Note on reproducibility under the appendix-heavy structure.** The Theoretical/4
> band asks that a reader be able to *reproduce the results*. It does not ask that
> they be able to do so without turning a page. A body that states the construction
> and points precisely to Appendix C for the atoms satisfies it; a body that states
> the construction and points to the *repository* does not.

### 2.1 Page budget

The guidelines set 40–60 pages (body, excluding contents, proposal, appendices) with
an explicit marks penalty for overrun. **Target 54–56 pages.**

| Section | Pages | Rubric criterion |
| :-- | --: | :-- |
| §1 Introduction | 4 | Intro & Lit Review /20 |
| §2 Background and Literature Review | 13 | Intro & Lit Review /20 |
| §3 The Descriptor Reformulation | 15 | Body: groundwork |
| §4 Extension to Polynomial Nonlinearity | 4 | Body: groundwork |
| §5 Numerical Study | 11 | Body: results & discussion |
| §6 Discussion | 4–5 | Body: results & discussion |
| §7 Conclusions and Future Work | 3–4 | Conclusions /10 |
| **Total** | **~55** | |

Two consequences worth internalising.

**The literature review grew, and that is deliberate.** It is now 13 pages rather than
9–10 because it absorbed the PIHM framework and the critical assessment that the whole
thesis pivots on. It is still only ~24% of the page budget against 20% of the marks.
The compensating cut is in QC preliminaries: **two pages, hard cap**, standard material
in flowing prose, gate table to Appendix A, numbered definitions only for objects
re-invoked later.

**§3 is the thesis.** Fifteen pages against a /30–40 criterion, carrying one
construction instead of two. If any section is over budget, it is not this one that
gets cut.

---

## 3. LaTeX Section Tree

Matches the live `2_body/*.tex` files.

```latex
% ---------- 2_body/1_introduction.tex  (~4 pp) ----------
\section{Introduction}
  \subsection{Differential Equations as a Target for Quantum Computation}
  \subsection{The Encoding Wall in Physics-Informed Quantum Solvers}
  \subsection{Contributions and Scope}     % numbered; scope statement lives here
  \subsection{Outline}

% ---------- 2_body/2_literature.tex  (~13 pp) ----------
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
  \subsection{The Physics-Informed Effective Hamiltonian Framework}   % PRIOR ART
      \subsubsection{The Residual Construction and Its Ground State}
      \subsubsection{The Published collocation Encoding}
      \subsubsection{Critical Assessment: The Encoding Wall}          % THE PIVOT
  \subsection{Block Encoding, LCU and Qubitisation}
  \subsection{Quantum Signal Processing and Imaginary-Time Filtering}
      \subsubsection{From QSP and QSVT to the Generalised Construction}
      \subsubsection{Ground-State Preparation by Imaginary-Time Filtering}
  \subsection{Readout and Amplitude Amplification}        % ~1/3 pp, prior art only
  \subsection{Synthesis: The Gap This Thesis Addresses}
  \subsection{Notation and Conventions}                   % the table; rubric names it

% ---------- 2_body/3_descriptor.tex  (~15 pp)   <-- THE CONTRIBUTION ----------
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

% ---------- 2_body/4_nonlinear.tex  (~4 pp) ----------
\section{Extension to Polynomial Nonlinearity}
  \subsection{The Carleman Lift onto the Descriptor Path}
  \subsection{The Nodal Product-to-Sum Fold}
  \subsection{The Doubled-Space Route: Coverage and Its Limits}
  \subsection{Preparation Versus Projection}

% ---------- 2_body/5_results.tex  (~11 pp) ----------
\section{Numerical Study}
  \subsection{Experimental Design and Cost Conventions}
  \subsection{The Published collocation Encoding, Reproduced and Characterised}
  \subsection{Encoding Cost of the Descriptor Construction}
  \subsection{Spectral Gap and Success Probability}
  \subsection{Solution Accuracy on Representative Problems}     % THREE cases
  \subsection{Nonlinear Benchmarks}
  \subsection{An Application Case Study}                        % ONE of BS / NS
  \subsection{Summary of Findings}

% ---------- 2_body/6_discussion.tex  (~4-5 pp) ----------
\section{Discussion}
  \subsection{Why the Trade-off Exists}
  \subsection{End-to-End Complexity: The Query Floor}
  \subsection{Where This Construction Applies, and Where It Does Not}
  \subsection{Feasibility on Near-Term and Early Fault-Tolerant Hardware}
  \subsection{Limitations}

% ---------- 2_body/7_conclusions.tex  (~3-4 pp) ----------
\section{Conclusions and Future Work}
  \subsection{Conclusions}
  \subsection{Future Work}
```

### 3.1 What changed from the previous structure, and why

1. **`3_formulation.tex` is gone.** Its notation table moved to §2.9; the PIHM
   construction and the collocation encoding moved to §2.4 as prior art; the
   gate-level derivative atoms moved into §3.4 as part of the contribution; the
   spectral-gap collapse became §2.4.3 (diagnosis) plus §5.2 (measurement).
2. **FABLE is not discussed.** It was a route through the published formulation, not
   part of this thesis's story.
3. **Eight sections became seven**, and the descriptor section moved from §4 to §3 —
   the contribution now begins on roughly page 18 rather than page 25.
4. **Readout is prior art plus a half-page scope statement.** §2.7 covers the
   primitives and quotes their costs; §3.9 states what the pipeline hands you and
   says plainly that no measurement protocol is implemented here. It reappears only
   in §6.5 (Limitations) and §7.2 (Future Work). It is never presented as
   contributed work.
5. **`\nocite{*}` and all `\todo` notes must go before submission.** `\nocite{*}`
   currently pulls every entry in `ref.bib` into the bibliography whether cited or
   not — a visible presentation failure under the /10 Style criterion.

### 3.2 Appendices — the load-bearing half of this structure

Appendices are **not counted in the page limit**, and both rubric variants explicitly
invite them (*"If there is insufficient room, appendices should be included"*; *"no
need to include detailed codes, which could be included in appendix"*). Under the
narrative-first structure they are not an overflow bin; they are where the thesis
discharges its reproducibility obligation.

| | Appendix | Referenced from |
| :-- | :-- | :-- |
| A | Quantum gate reference table | §2.1.2 |
| B | Chebyshev and ultraspherical identities; $\tilde{B}$, $\tilde{D}$ entries | §3.3 |
| C | The descriptor construction in full: derivative atoms, composition algebra | §3.4, §3.5 |
| D | Proof of the cost proposition | §3.6 |
| E | The nonlinear route in full: Carleman lift, nodal fold, doubled-space algebra | §4 |
| F | Verification protocol and per-atom residuals | §3.10 |
| G | Catalogue of all DE cases solved, with parameters and status | §5.5–§5.7 |
| H | Readout protocols and their quoted costs | §3.9 |
| I | Software: `DESolverLib` / `desolver_hpc`, Setonix configuration | §5.1 |
| J | **Research proposal** — required by the guidelines, with deviations noted | — |

**The pointer rule.** Every appendix reference in the body must carry a reason, never
a bare cross-reference: not *"see Appendix C"* but *"the atom-by-atom constructions,
and the column-by-column residuals establishing each, are given in Appendix C"*. A
body that offloads without saying what was offloaded reads as evasive; one that names
what is there reads as disciplined.

---

## 4. Section Purpose, Deliverables, and Marker Checklists

---

### §1 Introduction — *Intro & Lit Review /20*

**Purpose.** Establish that the problem matters, that it has a specific unsolved
component, and that this thesis solves that component. The HD wording — *"excellent
connection of the current field to the project"* — means the introduction must not
merely survey; it must converge.

**Deliverables**
- A concrete opening: what breaks if differential equations cannot be solved on
  quantum hardware, with citations to the application domains.
- The bottleneck stated **quantitatively**: the $\Theta(N^2)$ gate / $(n{+}3)$ ancilla
  / $\alpha \approx \Theta(N^8)$ figures of the published encoding, and the
  machine-epsilon gap consequence. Attributed as the published route's cost, not
  presented as an anonymous state of nature.
- Numbered contributions, each one sentence of *what* and one clause of *evidence*.
- **Scope, stated once and plainly, inside §1.3**: results are classical simulations
  of the pipeline, not hardware executions; no measurement protocol is implemented.
  Saying it here inoculates the whole thesis.
- Outline: one bullet per section, each naming the section's job.

**Marker checklist**
1. Can a non-specialist physicist state the problem after two pages?
2. Is the gap specific enough that a referee could check whether it is real?
3. Are the contributions numbered, and is each one falsifiable?
4. Does at least one quantitative figure appear before the end of page 2?
5. Is the scope statement — classical simulation, classical readout — explicit?
6. Is the published framework attributed at first mention, not first *critique*?
7. Does the outline match the actual section headings verbatim?

---

### §2 Background and Literature Review — *Intro & Lit Review /20*

**Purpose.** Demonstrate command of the state of the art **and judge it**. This
section now does double duty: it is both the background and the presentation of the
framework the thesis improves. The rubric is unambiguous: *"A critical assessment of
the strengths and weaknesses of the material reviewed is required for a high
distinction."* A survey without verdicts caps at band 2–3 (11.0–17.9).

**Deliverables**
- **Compressed QC preliminaries, two pages, hard cap.** Numbered definitions only for
  objects reused later. Gate table to Appendix A. Cite Nielsen & Chuang and move on.
  This is the page budget that funds §2.4.
- For **each** competing family of DE algorithms: what it assumes, what it costs, and
  **where it fails**. Every method gets an explicit failure-mode sentence.
- **§2.3.2 — the ultraspherical antecedent, credited here.** The descriptor basis
  change is the discrete shadow of the ultraspherical spectral method (Olver &
  Townsend 2013). State it in the literature review, *before* §3 claims anything, then
  state precisely what the increment is: applying it to the physics-informed residual
  so the whole encode-and-prepare pipeline inherits bandedness, and showing the
  certified solution is unchanged. Pre-empting *"isn't this just ultraspherical?"* is
  worth more than hoping it is not asked.
- **§2.4 — the PIHM framework as prior art.** Present $H = A^\top A + \sum_i B_i^\top B_i$,
  why its ground state is the solution, what the $B_i$ encode, and the published
  collocation encoding — at the depth a reader needs to follow §3, in the register of
  attributed description. Cite `wu2025pihm` at the head of the subsection and again
  wherever a specific construction is theirs.
- **§2.4.3 — the critical assessment, and the pivot of the thesis.** The published
  encoding's failure stated *structurally*: $G$ is dense, so the residual is dense, so
  the block encoding costs $\Theta(N^2)$ uniformly-controlled rotations and $(n{+}3)$
  ancilla, and $\alpha_H$ inflates to $\approx\Theta(N^8)$; at $n \gtrsim 7$ the
  composed $H$'s relative gap falls below double-precision machine epsilon, so the
  ground state is not resolvable at all. Diagnose here; the **measured** evidence is
  §5.2, and this subsection must forward-reference it with a reason.
- §2.7 readout as prior art only: the primitives, their quoted costs, one third of a
  page. No claim of implementation appears anywhere in this thesis.
- **§2.8 — a closing gap subsection** that poses the open questions as questions and
  names which section answers each.
- **§2.9 — the notation and conventions table.** The Theoretical rubric names this
  requirement explicitly. Fix $n$, $N = 2^n$, $k$, $p$, $\alpha$, $\Delta$, $G$,
  $\tilde{B}$, $\tilde{D}$, $A$, $A_\mathrm{sys}$, $H$, $H_\mathrm{sys}$,
  $\epsilon_G$, $M$. Placing it at the end of §2 makes it the handoff into the
  contribution.

**Marker checklist**
1. Does every reviewed method carry an explicit weakness, not just a description?
2. Is there a comparison table of DE approaches with a "this work" row?
3. Is `wu2025pihm` attributed at the head of §2.4 and at each specific construction?
4. Could a reader mistake any sentence in §2.4 for a claim of authorship? Rewrite it.
5. Is the ultraspherical antecedent credited in §2.3.2, before §3 claims anything?
6. Is §2.1 ≤ 2 pages?
7. Does §2.4.3 diagnose *structurally* and forward-reference the measurement in §5.2?
8. Does §2.8 name the gap and point forward by section number?
9. Is any subsection present that no later section depends on? Cut it.
10. Are all citations formatted consistently (IEEE style, via `biblatex`)?

---

### §3 The Descriptor Reformulation — *Body: groundwork* — **the core**

**Purpose.** This section carries the thesis. Under the Theoretical scale it is the
heart of a /40 criterion whose top band reads *"as would appear in a well written
journal article."* Write it as the methods section of a PRA submission.

**The narrative rule for this section.** The body carries four things and offloads
the rest: **the idea** (in words, before algebra), **the object** (stated once, not
derived), **the cost** (as a formal proposition), and **the interpretation** (what it
means operationally). Entry-level formulae, atom-by-atom constructions and proofs go
to Appendices B–D. Test each equation: *does the argument break if a reader skips it?*
If not, it is an appendix equation.

**Deliverables**
- **§3.1 — a pipeline figure and one page of narrative.** The spine: residual →
  banded factorisation → block encoding → imaginary-time filter → solution. Every
  later subsection is a stage of this figure. A marker who reads only this page should
  be able to state what the thesis does.
- **§3.2 — design rationale before mechanism.** One paragraph, in words, on why
  carrying $f', f''$ buys bandedness. Then, and only then, the algebra.
- **§3.3 — the factorisation.** $G = \tilde{B}^{-1}\tilde{D}$ with $\tilde{B}$ banded,
  and the resulting block structure of $A_\mathrm{sys}$. State the Hilbert-space cost
  ($\lceil\log_2(k{+}1)\rceil$ extra qubits, $2^{\lceil\log_2(k+1)\rceil}\!\cdot\!N$
  versus $N$) in the same breath as the benefit — volunteering the cost is what makes
  the benefit credible. Entries of $\tilde{B}$, $\tilde{D}$ to Appendix B.
- **§3.4 — the derivative atoms, as one section.** Name the atoms, tabulate them
  (arity, gate cost, ancilla, verified residual), and show **one** representative
  circuit. The Chebyshev feature map, the differential operator, the data constraints
  and the net operator are rows in that table, not four `\paragraph`s of derivation.
  Full constructions to Appendix C.
- **§3.5 — the block encoding** as a single flat `PREPARE/SELECT/PREPARE`$^\dagger$
  LCU, with a `quantikz` figure and an `algorithm2e` listing followed by a
  line-referenced walkthrough.
- **§3.6 — a formal cost result.** A proposition with a proof: gate count $O(n^2)$,
  ancilla $O(1)$ (9–10, flat in $n$), $\alpha_A \to \|A_\mathrm{sys}\|_2$ and hence
  $\alpha_H \to \|H_\mathrm{sys}\| = \Theta(N^2)$. Proof to Appendix D; **two
  paragraphs of operational interpretation stay in the body.** A proposition without
  interpretation is a formula; with it, it is a result.
- **§3.7** — boundary conditions and rank-one PDE datum injection.
- **§3.8** — GQSP-QITE applied to $H_\mathrm{sys}$: filter design, degree, and why the
  recovered gap makes the filter viable. GQSP itself is prior art (§2.6) and is not
  re-derived here.
- **§3.9 — extracting the solution, half a page.** What the pipeline hands you; what a
  hardware read would cost, quoted from cited work; and the explicit statement that no
  measurement protocol is implemented in this thesis and every error reported in §5 is
  a classical state-vector read. Protocols and costs to Appendix H.
- **§3.10 — verification methodology, stated as a limitation.** Correctness is
  compositional: atoms verified column-by-column to $10^{-9}$–$10^{-11}$, the
  `lcu_sum`/`gram` recipe to $<10^{-10}$; the composed $H$ is *not* verified
  end-to-end because at 22+ qubits a dense simulation allocates hundreds of GB. Say
  this here rather than letting a marker find it.

**Marker checklist**
1. Could a referee re-derive $A_\mathrm{sys}$ from the body plus Appendices B–C?
2. Does every appendix pointer say what is in the appendix and why?
3. Is the cost result formally stated *and* interpreted operationally in the body?
4. Is the Hilbert-space penalty volunteered alongside the gate-count win?
5. Is the ultraspherical antecedent re-acknowledged at the point of construction?
6. Is the verification argument complete, including what is *not* verified and why?
7. Does §3.1's figure let a marker state the thesis after one page?
8. Does every body equation survive the test *"does the argument break without it?"*
9. Is exactness stated precisely (exact, bar the `mult_matrix_square` truncation at
   $\sim 10^{-13}$ for variable coefficients)?
10. Does §3.9 leave any impression that readout was implemented? It must not.

---

### §4 Extension to Polynomial Nonlinearity — *Body: groundwork*

**Purpose.** Show the structural move generalises. Also where the
preparation/projection distinction must be made unmissable. Four pages: this is a
narrative beat, not a second contribution chapter. Derivations to Appendix E.

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
  into a degenerate kernel; it does not prepare.
- A subsection drawing the preparation/projection line explicitly, naming which route
  sits on which side.
- What is not gate-level as shipped: the $O(\log^2 M)$ transform held as a dense
  `UnitaryGate` (Klappenecker–Rötteler cited), and the structured $F_2$ assembly as a
  caller-supplied hook.
- One sentence connecting back to §3.2's structural principle. The reader should see
  this section as the same idea applied again, not as new machinery.

**Marker checklist**
1. Is "prepared" never used where "projected" is meant?
2. Is the dissipativity precondition stated as a precondition?
3. Is the fold's optimality claim distinguished from mere tightness?
4. Are the unpackaged components named, with the honest reason?
5. Does this section connect back to §3's structural principle explicitly?
6. Is it within four pages, with the algebra in Appendix E?

---

### §5 Numerical Study — *Body: results & discussion*

**Purpose.** Evidence every claim. The top band demands *"complete, clearly presented
results"* understandable *"without reference to any other documents."*

**Deliverables**
- **§5.1 — cost conventions first.** What counts as a gate, which decomposition is
  assumed, how ancilla are counted, and **which direction the convention biases the
  comparison** — declare it conservative for the descriptor construction, so any
  advantage reported is a lower bound. The two scope statements live here too:
  simulations capped at $\dim \lesssim 2000$ by simulation cost *and not by the
  algorithm*, and every solution error a classical state-vector read. Name
  `DESolverLib` / `desolver_hpc` / Setonix; detail to Appendix I.
- **§5.2 — the published route, reproduced and characterised.** This is the measured
  evidence for the §2.4.3 diagnosis, and it is *your* work: you implemented the
  published encoding and measured where it fails. Frame it exactly that way — a
  reproduction, not a rival. Carries the gap-collapse figure ($\sim10^{-15}$ against
  $\epsilon_\mathrm{mach}$ at $n \gtrsim 7$), which is the single sharpest motivating
  fact in the thesis.
- **§5.3 — the headline table**: gates, ancilla, $\alpha$, exactness, gap, for the
  published encoding versus the descriptor construction. Two rows, not three; FABLE
  does not appear.
- **§5.4** — gap and success probability: $\sim10^{-6}$ against $\sim10^{-15}$;
  $p_\mathrm{succ} \to \Theta(1)$ against $N^{-3/2}$ Haar-average.
- **§5.5 — three representative cases only**, carried in depth: one linear ODE, one
  PDE, one coupled or variable-coefficient case. Every remaining case goes into
  Appendix G with a pointer. This discipline keeps you under 60 pages while
  *increasing* the mark — a catalogue reads as unfocused, and focus is scored.
- **§5.6** — nonlinear benchmarks, evidencing §4.
- **§5.7 — one application case study.** Black–Scholes *or* Navier–Stokes, not both.
- Solution fidelity against classical baselines, including the
  $\cos\mathrm{sim} = 1.000000$ agreement of the descriptor $a$-block with the
  original Chebyshev solution.
- **§5.8 — numbered summary of findings**, 4–6 items, at least one a limitation of the
  descriptor construction itself (the Hilbert-space growth
  $2^{\lceil\log_2(k+1)\rceil}\!\cdot\!N$ versus $N$; the doubled-space route
  projecting rather than preparing).

**Marker checklist**
1. Is every figure interpreted in prose, not merely displayed?
2. Are all experimental parameters stated in the body or an appendix?
3. Is the cost convention stated *before* the first comparison, with its bias named?
4. Are "we could not simulate it" and "the algorithm cannot reach it" kept distinct
   everywhere they arise?
5. Is §5.2 framed as a reproduction of published work, never as a rival method?
6. Are the in-depth cases ≤ 4, with the remainder in Appendix G?
7. Does each figure caption stand alone?
8. Do the numbered findings include at least one negative or limiting result?
9. Does every claim in the Abstract have a number in this section backing it?

---

### §6 Discussion — *Body: results & discussion*

**Purpose.** Demonstrate *"insight into the significance of the work"* — the phrase
separating band 3 from band 4. Description belongs in §5; §6 must explain and judge.

**Deliverables**
- Why the trade-off exists structurally: the descriptor construction buys bandedness
  and gap health by spending Hilbert space.
- **§6.2 — the query-floor argument, in your own voice.** Neither the published route
  nor this one is poly-log: $\alpha_H \ge \|H_\mathrm{sys}\| = \Theta(N^2)$ against
  $\Delta = \Theta(1)$ forces $\tilde\Theta(N^2)$ queries for *any* block encoding of
  this $H$. The descriptor construction **meets** that floor at
  $\tilde\Theta(N^2\,\mathrm{poly}\,n)$ total gates; the published collocation encoding
  misses it by $\approx N^6$. Making this argument yourself converts the largest
  vulnerability into evidence of command.
- Where the construction applies and where it does not — a guide a practitioner could
  act on.
- NISQ / early fault-tolerant feasibility, grounded in the ancilla and depth numbers.
- **§6.5 Limitations**, as its own subsection: no hardware execution;
  simulation-capped dimensions; compositional-only verification of the composed $H$;
  the unpackaged $F_2$ assembly and the dense `UnitaryGate` transform; **no
  measurement protocol implemented**; the projection-not-preparation status of the
  doubled-space route.

**Marker checklist**
1. Does this section explain rather than restate §5?
2. Is the query-floor argument made in your own voice, before a referee makes it?
3. Are the limitations owned, each with its analysis attached (the rubric's condition
   for no penalty)?
4. Are consequences *for the field* discussed, not just for this project?
5. Is there actionable guidance a practitioner could follow?

---

### §7 Conclusions and Future Work — *Conclusions /10*

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
  readout cost quoted in §3.9; package the structured $F_2$ assembly for a concrete
  PDE; realise the $O(\log^2 M)$ transform gate-level rather than as a dense
  `UnitaryGate`; hardware validation on a small instance.
- A closing sentence stating the transferable principle, not merely the result.

**Marker checklist**
1. Does every §1.3 contribution get a verdict here?
2. Are 3–5 future directions given, each with motivation and a concrete first step?
3. Is anything claimed here that was not evidenced in §5?
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
5. Five `\todo` notes in `2_literature.tex` and one in `main.tex`.

**Pre-submission sweep**
1. Compile clean — zero warnings, no overfull `\hbox` in the body.
2. Every figure and table referenced in the text via `\Cref`, none orphaned.
3. Captions: figures below, tables above, consistently.
4. Consistent symbol usage — run Verification Mode (see `CLAUDE.md`).
5. All acronyms defined at first use; `glossaries` entries complete.
6. Bibliography uniform; no "et al." inconsistencies; arXiv IDs where applicable.
7. Page count within 40–60; declaration page signed; Summary of Student Achievement
   present, one page, first person.
8. Read the whole thesis aloud once. It is the only reliable way to catch the
   register slips the /10 is scoring.

---

## 5. Pre-Submission Traceability Matrix

| Criterion | Marks | Where it is earned | Done |
| :-- | --: | :-- | :-- |
| Historical background & state of the art | /20 | §2.2–§2.7 | ☐ |
| — critical assessment (HD gate) | | §2.2.3, **§2.4.3**, §2.8 | ☐ |
| — connection to the project | | §1.2, §2.4.3, §2.8 | ☐ |
| — prior art correctly attributed | | §2.3.2, §2.4 | ☐ |
| Groundwork / model formulation | /30–40 | §3, §4 | ☐ |
| — notation & conventions | | §2.9 | ☐ |
| — reproducibility | | §3 + Appendices B–D | ☐ |
| — software tools created | | §5.1 + Appendix I | ☐ |
| Results & Discussion | /20–30 | §5, §6 | ☐ |
| — significance for the field | | §6.1–§6.4 | ☐ |
| — negative results with analysis | | §5.8, §6.5 | ☐ |
| Conclusions | /10 | §7.1 | ☐ |
| — further investigation | | §7.2 | ☐ |
| Style & presentation | /10 | throughout | ☐ |

---

*Companion documents: `STYLE_GUIDE.md` (tone, exposition, common traps),
`../CLAUDE.md` (interactive review protocol).*
