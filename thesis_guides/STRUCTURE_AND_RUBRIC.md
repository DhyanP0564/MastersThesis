# STRUCTURE_AND_RUBRIC.md — Section Tree, Deliverables, Marker Checklists

Built from the official *Master of Physics Thesis Mark Sheet*
(`Theses-AssessmentRubric.pdf`), the School's *Master Thesis Guidelines*, and the
structural patterns of two high-scoring exemplars (Green 2024; Snow 2026).

Framing decision (locked): **descriptor form as the resolution of the state-space
encoding wall.** State-space appears as a characterised baseline, not a co-equal half.
Document class: `article`, `\section` at top level, matching your existing
`main.tex`.

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
is not an informal aspiration a professor mentioned to you — it is the literal
wording of the highest mark band. Every drafting decision should be tested against it.

### 1.2 Negative and partial results are explicitly protected

Two separate criteria say so:

> "If the results are negative, there will not be a penalty **if a detailed
> discussion/analysis is given**." (Experimental R&D)

> "If there is a null or partial result due to the choice of an ill-posed or overly
> complex problem for the project, this should be noted and progress toward a solution
> detailed. There will be no marks penalty if there is a well justified case."
> (Theoretical R&D)

This directly licenses the honest caveats your work carries — no hardware execution,
GQSP figures capped at $\dim \lesssim 2000$ by simulation cost, the $O(\log^2 M)$
transform held as a dense `UnitaryGate`, the structured $F_2$ assembly unpackaged,
the doubled-space route projecting rather than preparing. **Stating these with
analysis costs you nothing and evidences the "insight into significance" the top band
demands. Concealing them and being caught costs you the band.**

### 1.3 Self-containment is required twice

> "All your results need to be presented in a way that is easy to understand,
> **without reference to any other documents.**"

The thesis cannot lean on `DescriptorVsStateSpace.md`, the notebooks, or the repo
READMEs. Every number quoted must be derivable from what is printed in the thesis or
its appendices.

---

## 2. ⚠ Declare Your Project Type — This Changes the Page Budget

The marker ticks one category to set the /60 scale. The two plausible fits for your
work split the 60 marks very differently:

| Type | Construction/setup component | Results & Discussion component |
| :-- | :-- | :-- |
| **Theoretical** | Groundwork: theory & background for calculations — **/40** | **/20** |
| **Modelling** | Project Process: Model Formulation — **/30** | **/30** |

Your project straddles both: it is a theoretical construction (descriptor
reformulation, block-encoding cost analysis, Carleman lift) validated by numerical
modelling (classical circuit simulation, HPC benchmarks, `DESolverLib` /
`desolver_hpc`).

**Action: ask your supervisor which category will be ticked.** Until you know, write
to satisfy both — the requirements are compatible, and the union is what the top band
of either looks like:

- **Theoretical/4** demands: *"Outstanding description and detail in the background and
  setup of the calculations which follow, as would appear in a well written journal
  article."* Also names, explicitly, *"the notations and conventions that are being
  adopted"* and reproducibility: *"sufficient detail for the reader to be able to
  understand the techniques and/or to be able to reproduce the results."*
- **Modelling/4** demands: *"a description of any software tools used and/or created;
  a description and/or diagram of the model configuration; descriptions of the model
  input options selected."* It also says *"There is no need to include detailed codes,
  which could be included in appendix if desired."*

**The union, in practice:** a notation-and-conventions table, a construction written
so a referee could re-derive it, a named description of `DESolverLib` /
`desolver_hpc` and the Setonix configuration, and every numerical experiment's
parameters stated. Do all four and you satisfy the top band under either tick.

### 2.1 Page budget

The guidelines set 40–60 pages (body, excluding contents, proposal, appendices) with
an explicit marks penalty for overrun. **Target 54–56 pages** — enough slack that a
late figure does not push you over. Allocate proportional to marks, hedged across
both project types:

| Section | Pages | Rubric criterion |
| :-- | --: | :-- |
| §1 Introduction | 4 | Intro & Lit Review /20 |
| §2 Background & Literature Review | 9–10 | Intro & Lit Review /20 |
| §3 Formulation & the State-Space Baseline | 6–7 | Body: groundwork |
| §4 The Descriptor Reformulation | 10–11 | Body: groundwork |
| §5 Extension to Polynomial Nonlinearity | 5 | Body: groundwork |
| §6 Numerical Study (Results) | 12–13 | Body: results & discussion |
| §7 Discussion | 4–5 | Body: results & discussion |
| §8 Conclusions & Future Work | 3–4 | Conclusions /10 |
| **Total** | **~54** | |

Two consequences worth internalising. Intro + Background is 20% of the marks, so it
gets ~25% of the pages and **not one page more** — your current `2_literature.tex`
plan (nine subsections, several with subsubsections, ~9 numbered definitions of
standard material) will blow through this if written at full depth. And §3–§7 must
carry ~34 pages against 60 marks; that is where the thesis is won.

---

## 3. Recommended LaTeX Section Tree

Maps onto your existing `2_body/*.tex` files. Suggested new filenames in brackets
where a split is warranted.

```latex
% ---------- 2_body/1_introduction.tex  (~4 pp) ----------
\section{Introduction}
  \subsection{Differential equations as a target for quantum computation}
  \subsection{The encoding bottleneck}          % problem statement, sharply posed
  \subsection{Contributions of this thesis}     % numbered, quantitative
  \subsection{Outline}                          % bulleted, one line per section

% ---------- 2_body/2_literature.tex  (~9-10 pp) ----------
\section{Background and Literature Review}
  \subsection{Quantum computation preliminaries}      % COMPRESS - see 4.2
  \subsection{Quantum algorithms for differential equations}
      \subsubsection{Linear-systems and Hamiltonian-simulation routes}
      \subsubsection{Variational and Carleman-linearisation routes}
      \subsubsection{Critical assessment}             % REQUIRED for HD
  \subsection{Spectral methods and the Chebyshev basis}
  \subsection{The physics-informed effective Hamiltonian framework}
  \subsection{Block encoding, LCU and qubitisation}
  \subsection{Quantum signal processing}
      \subsubsection{QSP, QSVT and the generalised construction}
      \subsubsection{Ground-state preparation by imaginary-time filtering}
  \subsection{Readout and amplitude amplification}
  \subsection{Synthesis: the gap this thesis addresses}   % the pivot

% ---------- 2_body/3_methods.tex  (~6-7 pp) ----------
\section{Formulation and the State-Space Encoding}
  \subsection{Notation and conventions}          % the table; rubric names this
  \subsection{From differential equation to effective Hamiltonian}
  \subsection{State-space encoding routes}
      \subsubsection{FABLE on the dense Hamiltonian}
      \subsubsection{Gate-level composition of derivative atoms}
  \subsection{Cost characterisation}              % gates, ancilla, alpha
  \subsection{The spectral-gap collapse}          % 10^-15 vs eps_machine
  \subsection{Diagnosis: what must change}        % pivot to the contribution

% ---------- 2_body/3b_descriptor.tex  (~10-11 pp)   <-- CONTRIBUTION ----------
\section{The Descriptor Reformulation}
  \subsection{Design rationale: carry the derivatives, do not eliminate them}
  \subsection{The banded factorisation}           % G = Btilde^-1 Dtilde
  \subsection{The descriptor residual and effective Hamiltonian}
  \subsection{Block encoding by a single PREPARE/SELECT/PREPARE$^\dagger$}
  \subsection{Cost analysis}                      % proposition + proof
  \subsection{Boundary conditions and data injection}
  \subsection{Verification methodology}           % by-parts argument, residuals

% ---------- 2_body/3c_nonlinear.tex  (~5 pp) ----------
\section{Extension to Polynomial Nonlinearity}
  \subsection{Carleman lift onto the descriptor path}
  \subsection{The nodal product-to-sum fold}
  \subsection{Doubled-space residuals: coverage and its limits}
  \subsection{Preparation versus projection}      % the honest distinction

% ---------- 2_body/4_results.tex  (~12-13 pp) ----------
\section{Numerical Study}
  \subsection{Experimental design and cost conventions}   % state the bias
  \subsection{Encoding cost}                      % headline comparison
  \subsection{Spectral gap and success probability}
  \subsection{Solution accuracy on representative problems}   % 3 cases ONLY
  \subsection{Nonlinear benchmarks}
  \subsection{Application case study}             % ONE of BS / Navier-Stokes
  \subsection{Readout}
  \subsection{Summary of findings}                % numbered, incl. negatives

% ---------- 2_body/5_discussion.tex  (~4-5 pp) ----------
\section{Discussion}
  \subsection{Why the trade-off exists}
  \subsection{Which regime to use, and when}
  \subsection{Feasibility on near-term and early fault-tolerant hardware}
  \subsection{Limitations}

% ---------- 2_body/7_conclusions.tex  (~3-4 pp) ----------
\section{Conclusions and Future Work}
  \subsection{Summary of findings}
  \subsection{Future work}
```

### 3.1 Three structural changes to your current `main.tex`

1. **Merge `6_futurework.tex` into `7_conclusions.tex`.** The rubric scores
   *"Conclusions **and Topics for Further Investigation**"* as one /10 criterion.
   Snow does exactly this (Ch. 8: "Conclusions and Future Work"). Saves a page of
   section whitespace and reads as one coherent unit.
2. **Split `3_methods.tex` into three files.** The baseline, the contribution, and
   the nonlinear extension are three distinct sections; keeping them in one file
   makes the contribution look like a subsection of the method rather than the point
   of the thesis.
3. **Remove `\nocite{*}` and all `\todo` notes before submission.** `\nocite{*}`
   currently pulls every entry in `ref.bib` into the bibliography whether cited or
   not — a visible presentation failure under the /10 Style criterion.

### 3.2 Appendices (not counted in the page limit — use them)

Both exemplars offload aggressively. Both rubric variants explicitly invite it
(*"If there is insufficient room, appendices should be included"*; *"no need to
include detailed codes, which could be included in appendix"*).

- A. Quantum gate reference table (resolves your existing `\todo`)
- B. Chebyshev/ultraspherical identities and the $\tilde{B}$, $\tilde{D}$ entries
- C. Full derivation of the descriptor cost bound
- D. Verification protocol: per-atom residuals, composition-algebra tests
- E. Table of all DE cases solved, with parameters and status (Snow's Appendix G model)
- F. Software: `DESolverLib` / `desolver_hpc` architecture, Setonix configuration
- G. **Research proposal** — required by the guidelines, with deviations noted

---

## 4. Section Purpose, Deliverables, and Marker Checklists

Each block below gives the rubric criterion in play, the content required for the top
band, and a numbered checklist to run before you consider the section done.

---

### §1 Introduction — *Intro & Lit Review /20*

**Purpose.** Establish that the problem matters, that it has a specific unsolved
component, and that this thesis solves that component. The rubric's HD wording —
*"excellent connection of the current field to the project"* — means the introduction
must not merely survey; it must converge.

**Deliverables**
- A concrete opening: what breaks if differential equations cannot be solved on
  quantum hardware, with citations to the application domains.
- The bottleneck stated **quantitatively**, not qualitatively. Not "encoding is
  expensive" but the $\Theta(N^2)$ gate / $(n{+}3)$ ancilla / $\alpha \approx \Theta(N^8)$
  figures, and the machine-epsilon gap consequence.
- Numbered contributions. Green's §1.1 and Snow's §1.2 are the models. Each
  contribution gets one sentence of *what* and one clause of *evidence*.
- Scope boundary: state that results are classical simulations of the pipeline, not
  hardware executions. Say it here, once, plainly — it inoculates the whole thesis.
- Outline: one bullet per section, each naming the section's job.

**Marker checklist**
1. Can a non-specialist physicist state the problem after two pages?
2. Is the gap specific enough that a referee could check whether it is real?
3. Are the contributions numbered, and is each one falsifiable?
4. Does at least one quantitative figure appear before the end of page 2?
5. Is the "classical simulation, not hardware" scope stated explicitly?
6. Does the outline match the actual section headings verbatim?

---

### §2 Background and Literature Review — *Intro & Lit Review /20*

**Purpose.** Demonstrate command of the state of the art **and judge it**. The rubric
is unambiguous: *"A critical assessment of the strengths and weaknesses of the
material reviewed is required for a high distinction."* A survey without verdicts
caps at band 2–3 (11.0–17.9).

**Deliverables**
- Compressed QC preliminaries. Two pages maximum. Keep numbered definitions only for
  objects reused later (block encoding, PIHM Hamiltonian, subnormalisation). Move the
  gate table to an appendix. Cite Nielsen & Chuang and move on.
- For **each** competing family of DE algorithms: what it assumes, what it costs, and
  **where it fails**. Snow's Ch. 3 is the template — every method gets an explicit
  failure-mode paragraph.
- The PIHM framework presented as prior art, with its provenance clearly attributed.
- Honest attribution of the descriptor idea's antecedent: it is the discrete shadow of
  the ultraspherical spectral method (Olver & Townsend 2013). **State this, then state
  precisely what your increment is** — applying it to the PIHM residual so the whole
  encode-and-prepare pipeline inherits bandedness, and showing the certified solution
  is unchanged. Pre-empting "isn't this just ultraspherical?" is worth more than
  hoping it is not asked.
- A closing gap subsection that poses the open questions and names which section
  answers each.

**Marker checklist**
1. Does every reviewed method carry an explicit weakness, not just a description?
2. Is there a comparison table with a "this work" row?
3. Is the ultraspherical antecedent credited *before* the contribution is claimed?
4. Is the QC preliminaries subsection ≤ 2 pages?
5. Does the section end by naming the gap and pointing forward?
6. Are all citations formatted consistently (IEEE style, via `biblatex`)?
7. Is any subsection present that no later section depends on? Cut it.

---

### §3 Formulation and the State-Space Encoding — *Body: groundwork*

**Purpose.** Build the shared machinery and establish the baseline's cost honestly
enough that your improvement is measured against a fair opponent. A strawman baseline
is the fastest way to lose a referee.

**Deliverables**
- **Notation and conventions table.** The Theoretical rubric names this requirement
  explicitly. Fix $n$, $N = 2^n$, $k$, $p$, $\alpha$, $\Delta$, $G$, $\tilde{B}$,
  $\tilde{D}$, $A$, $A_\mathrm{sys}$, $H$, $H_\mathrm{sys}$, $\epsilon_G$, $M$.
- The PIHM construction: $H = A^\top A + \sum_i B_i^\top B_i$, why its ground state is
  the solution, what the $B_i$ encode.
- Both state-space routes described at the level a reader could implement.
- The cost characterisation, derived not asserted.
- The gap collapse, with the machine-epsilon consequence spelled out: at $n \gtrsim 7$
  the composed $H$'s relative gap is below $\epsilon_\mathrm{mach}$, so the ground
  state is not resolvable in double precision *at all*. This is the sharpest
  motivating fact in the thesis — give it a figure.
- A diagnosis paragraph that names the structural cause (density of $G$) and thereby
  motivates §4 without yet describing it.

**Marker checklist**
1. Is the baseline described strongly enough that beating it means something?
2. Is every cost claim derived, cited, or measured — never asserted?
3. Is the notation table complete, and does the rest of the thesis obey it?
4. Would a competent reader be able to reproduce the baseline from this section?
5. Does the section end by motivating the contribution structurally?

---

### §4 The Descriptor Reformulation — *Body: groundwork* — **the core**

**Purpose.** This section carries the thesis. Under the Theoretical scale it is the
heart of a /40 criterion whose top band reads *"as would appear in a well written
journal article."* Write it as if it were the methods section of a PRA submission.

**Deliverables**
- **Design rationale before mechanism.** One paragraph, in words, on why carrying
  $f', f''$ buys bandedness. Then the algebra.
- The factorisation $G = \tilde{B}^{-1}\tilde{D}$ with $\tilde{B}$ banded, and the
  resulting block structure of $A_\mathrm{sys}$. State the Hilbert-space cost
  ($\lceil\log_2(k{+}1)\rceil$ extra qubits) in the same breath as the benefit —
  volunteering the cost is what makes the benefit credible.
- The block encoding as a single flat `PREPARE/SELECT/PREPARE`$^\dagger$ LCU, with a
  `quantikz` figure and an `algorithm2e` listing.
- **A formal cost result.** State it as a proposition with a proof: gate count
  $O(n^2)$, ancilla $O(1)$ (9–10, flat in $n$), $\alpha_A \to \|A_\mathrm{sys}\|_2$
  and hence $\alpha_H \to \|H_\mathrm{sys}\| = \Theta(N^2)$. Follow with two
  paragraphs of interpretation, Snow's Theorem 4.1 pattern.
- Boundary conditions and rank-one PDE datum injection.
- **Verification methodology, stated as a limitation.** Correctness is compositional:
  atoms verified column-by-column to $10^{-9}$–$10^{-11}$, the `lcu_sum`/`gram` recipe
  to $<10^{-10}$; the composed $H$ is *not* verified end-to-end because at 22+ qubits
  a dense simulation allocates hundreds of GB. Say this here rather than letting a
  marker find it.

**Marker checklist**
1. Could a referee re-derive $A_\mathrm{sys}$ from what is written?
2. Is the cost result formally stated *and* interpreted operationally?
3. Is the Hilbert-space penalty volunteered alongside the gate-count win?
4. Is the ultraspherical antecedent re-acknowledged at the point of construction?
5. Is the verification argument complete, including what is *not* verified and why?
6. Does at least one figure show the circuit structure, not just cite it?
7. Is exactness stated precisely (exact, bar the `mult_matrix_square` truncation at
   $\sim 10^{-13}$ for variable coefficients)?

---

### §5 Extension to Polynomial Nonlinearity — *Body: groundwork*

**Purpose.** Show the structural move generalises. Also the section where the
preparation/projection distinction must be made unmissable.

**Deliverables**
- The Carleman lift onto the linear descriptor path; the dissipativity condition
  $\mathrm{Re}\,\lambda(F_1) < 0$; why this yields a genuine 1-D kernel and therefore
  a real preparation claim; that it stays linear in $N$.
- The nodal fold $n_1$: zero ancilla, $\alpha = 2^{p\ell/2}$, and — worth stating
  explicitly — that for the quadratic case $\alpha = 2 = \|n_1\|$ exactly, so the
  encoding is **optimal, not merely tight**. Verified as an operator to $\sim10^{-15}$.
- The doubled-space route: what it covers that nothing else does (steady, two-point
  BVP, centre-type), and its honest status — it *projects* a classically-known target
  into a degenerate kernel; it does not prepare.
- A subsection that draws the preparation/projection line explicitly and says which
  route sits on which side.
- What is not gate-level as shipped: the $O(\log^2 M)$ transform held as a dense
  `UnitaryGate` (Klappenecker–Rötteler cited), and the structured $F_2$ assembly as a
  caller-supplied hook.

**Marker checklist**
1. Is "prepared" never used where "projected" is meant?
2. Is the dissipativity precondition stated as a precondition, not buried?
3. Is the fold's optimality claim distinguished from mere tightness?
4. Are the unpackaged components named, with the honest reason?
5. Does this section connect back to §4's structural principle explicitly?

---

### §6 Numerical Study — *Body: results & discussion*

**Purpose.** Evidence every claim. The top band demands *"complete, clearly presented
results"* that are understandable *"without reference to any other documents."*

**Deliverables**
- **Cost conventions first.** What counts as a gate, which decomposition is assumed,
  how ancilla are counted, and **which direction the convention biases the
  comparison**. Snow's model: declare the convention conservative for your own method
  and note that any advantage reported is therefore a lower bound.
- The headline encoding-cost comparison as a table: gates, ancilla, $\alpha$,
  exactness, gap — FABLE vs atom-compose vs descriptor.
- Gap and success probability: $\sim10^{-6}$ vs $\sim10^{-15}$;
  $p_\mathrm{succ} \to \Theta(1)$ vs $N^{-3/2}$ Haar-average.
- **Three or four representative cases only**, carried in depth: one linear ODE, one
  PDE, one nonlinear, one application. Every remaining case goes into a single
  summary table with a pointer to Appendix E. This is the discipline that keeps you
  under 60 pages while *increasing* the mark — the rubric rewards focus, and a
  catalogue reads as unfocused.
- Solution fidelity against classical baselines, including the $\cos\mathrm{sim} =
  1.000000$ agreement of the descriptor $a$-block with the original Chebyshev solution.
- Readout results.
- **Numbered summary of findings**, 4–6 items, of which at least one is a limitation
  of your own method (e.g. the Hilbert-space growth $2^{\lceil\log_2(k+1)\rceil}\cdot N$
  versus $N$). Green's four-finding close, two of them negative, is the model.

**Marker checklist**
1. Is every figure interpreted in prose, not merely displayed?
2. Are all experimental parameters stated in-thesis (self-containment rule)?
3. Is the cost convention stated *before* the first comparison, with its bias named?
4. Are "we could not simulate it" and "the algorithm cannot reach it" kept distinct
   everywhere they arise?
5. Are the case studies ≤ 4, with the remainder tabulated?
6. Does each figure caption stand alone?
7. Do the numbered findings include at least one negative or limiting result?
8. Does every claim in the Abstract have a number in this section backing it?

---

### §7 Discussion — *Body: results & discussion*

**Purpose.** Demonstrate *"insight into the significance of the work"* — the phrase
separating band 3 from band 4. Description belongs in §6; §7 must explain and judge.

**Deliverables**
- Why the trade-off exists structurally: descriptor buys bandedness and gap health by
  spending Hilbert space; state-space buys a smaller space by accepting a dense
  operator.
- **The end-to-end honesty paragraph.** Neither regime is poly-log:
  $\alpha_H \ge \|H_\mathrm{sys}\| = \Theta(N^2)$ against $\Delta = \Theta(1)$ forces
  $\tilde\Theta(N^2)$ queries for *any* block encoding of this $H$. Descriptor **meets**
  that floor at $\tilde\Theta(N^2\,\mathrm{poly}\,n)$ total gates; state-space misses
  it by $\approx N^6$. Making this argument yourself converts your largest
  vulnerability into evidence of command.
- A regime-selection guide: which method for which problem class, and why.
- NISQ / early fault-tolerant feasibility, grounded in the ancilla and depth numbers.
- **Limitations**, as its own subsection: no hardware execution; simulation-capped
  dimensions; compositional-only verification of the composed $H$; unpackaged $F_2$;
  the projection-not-preparation status of the doubled-space route.

**Marker checklist**
1. Does this section explain rather than restate §6?
2. Is the query-floor argument made in your own voice?
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
  *"relate back to the original goal of the report."* Mirror §1's numbered
  contributions and report the outcome of each.
- Quantitative recap: the headline figures, once more, compactly.
- **Substantive future work**, each item with a stated reason and a first step. Not
  "extend to more equations" but: package the structured $F_2$ assembly for a concrete
  PDE; realise the $O(\log^2 M)$ transform gate-level rather than as a dense
  `UnitaryGate`; port the descriptor pipeline's measured Setonix track record to
  parity with state-space; hardware validation on a small instance.
- A closing sentence stating the transferable principle, not merely the result.

**Marker checklist**
1. Does every §1 contribution get a verdict here?
2. Are 3–5 future directions given, each with motivation and a concrete first step?
3. Is anything claimed here that was not evidenced in §6?
4. Is the transferable principle stated?
5. Is the section free of new results or new citations?

---

### Style & Presentation — */10, "Flawless" for full marks*

Only *"flawless"* earns 10.0; *"few insignificant errors"* caps at 9.9. Two marks are
available for proofreading alone — the cheapest marks in the rubric.

**Already present in your draft — fix these:**
1. `1_header/2_acknowledgments.tex`: "Jingbo **Want**" → "Jingbo **Wang**". A
   misspelled supervisor's name on page i is the worst possible first impression.
2. `2_body/2_literature.tex`: a stray `` `' `` after `\end{pmatrix}` in the State
   Space definition renders as spurious quote marks in Eq. (2.1).
3. Same file: "initial**ized**" in the Ancillary Qubits definition, against
   `[australian]{babel}`. Sweep for `-ize`/`-ized`/`-ization` throughout.
4. `main.tex`: `\nocite{*}` will pull every `ref.bib` entry into the bibliography.
5. `main.tex` and `2_literature.tex`: six `\todo` notes still rendering (five in `2_literature.tex`, one in `main.tex`).

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

Before submitting, confirm each rubric criterion has an identifiable home:

| Criterion | Marks | Where it is earned | Done |
| :-- | --: | :-- | :-- |
| Historical background & state of the art | /20 | §2.2–§2.7 | ☐ |
| — critical assessment (HD gate) | | §2.2.3, §2.8 | ☐ |
| — connection to the project | | §1.2, §2.8 | ☐ |
| Groundwork / model formulation | /30–40 | §3, §4, §5 | ☐ |
| — notation & conventions | | §3.1 | ☐ |
| — reproducibility | | §4, Appendix C–D | ☐ |
| — software tools created | | Appendix F | ☐ |
| Results & Discussion | /20–30 | §6, §7 | ☐ |
| — significance for the field | | §7.1–§7.3 | ☐ |
| — negative results with analysis | | §6.8, §7.4 | ☐ |
| Conclusions | /10 | §8.1 | ☐ |
| — further investigation | | §8.2 | ☐ |
| Style & presentation | /10 | throughout | ☐ |

---

*Companion documents: `STYLE_GUIDE.md` (tone, exposition, common traps),
`../CLAUDE.md` (interactive review protocol).*
