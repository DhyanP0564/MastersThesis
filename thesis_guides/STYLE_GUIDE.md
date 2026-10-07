# STYLE_GUIDE.md — Stylistic DNA for the Thesis

Distilled from two high-scoring UWA physics theses (Green 2024, Honours, *Efficient Quantum State
Preparation*; Snow 2026, Masters, *Highly Optimised Quantum Circuit Synthesis for Classical Data
Encoding*) read against the School's marking guide.

The governing standard, stated plainly: **the markers are professors reading for publishable
work.** A thesis that could be cut down into a PRA submission with minimal surgery scores well. A
thesis that reads like a lab report, a tutorial, a software manual, or a catalogue of everything
the student tried does not. Every rule below descends from that standard.

> **Version 2.0 (2026-10-01).** Updated with `../ThesisPlanning.md` v2.0: the examples now state
> the current facts (`../CLAUDE.md`'s Standing Facts v3), section references follow the v2.0
> chapter order, and Traps 17–20 are new. Where an example and a Standing Fact disagree, the
> Standing Fact wins.

---

## 1. Tone & Voice

### 1.1 Assert what you measured; hedge what you inferred; scope everything

Both exemplars are notably **unhedged about their own results** and **carefully hedged about
extrapolations**. The distinction is the single most important tonal habit to copy.

Assert (measured, verified):

> "SSO improves prepared-state infidelity by roughly an order of magnitude over the Matrix Product
> Disentangler baseline at fixed depth" — Snow, Abstract

Hedge (inferred, asymptotic, unproven):

> "It should be noted that there are no rigorous guarantees in the root-exponential decay of
> $\|P\|_\infty$, which may not hold in some extreme cases." — Green, §5.2.2

For this thesis a third habit matters as much: **scope**. Almost every descriptor claim holds for a
class of problems, and stating it without the class is an over-claim a referee will find.

| claim | register |
| :-- | :-- |
| ⌈log₂(n+4)⌉ + 8 ancilla for R2's system rows, O(log n) | **Assert**, gate-level and verified; optimal only among exact LCU encodings |
| α/‖A_desc‖ → 1 | **Assert, scoped**: regular one-axis problems; about 2 on singular ones, 2.3–4.1 on PDEs |
| d = Θ̃(N) for the descriptor | **Assert, scoped**: a one-axis ODE whose leading coefficient does not vanish; about Θ̃(N²) or faster where it vanishes or on two axes |
| d = Θ̃(N^{2k}) for the standard form | **Assert**, even with the best exact encoding, since α_H ≥ ‖H‖ for any block encoding |
| the relative gap at n = 7 | **Assert, with the distinction**: the standard form's ground state is below double-precision resolution by `eigh`, not by SVD; the consequence is the degree, not unresolvability |
| correctness of the composed H | **Assert what is verified**: V exact to 25 qubits, probe on every construction-only circuit ≤ 24 qubits, IR at any size; T1 = T2 to ≤ 1e-10 where both run |
| "a ground state has been prepared" | **Assert only for a one-dimensional (near-)kernel, with its tier**: circuit simulation (T1), exact emulation (T2, provably equal to T1) or resource estimate (T3). Never "on hardware"; never for the doubled space (it projects) |
| a Carleman lift's solution | **Assert the kernel's uniqueness; measure the convergence separately.** A trusted kernel is not a converged lift |
| end-to-end poly-log speed-up | **Deny it yourself, first.** d = Θ(√(α_H/Δ) log 1/ε) with α_H ≥ ‖H‖; hedge any "for every filter" floor to what Lin & Tong support |
| the physics-informed effective Hamiltonian framework | **Attribute, then judge.** It is Wu et al.'s (`wu2025pihm`). Describe it in Chapter 3 as reported prior art; reserve the verdict for §3.6 |
| the descriptor's novelty | **Credit, then claim the increment.** The ultraspherical method and first-order-system least squares came first; the increment is the transfer to a block-encoded physics-informed Hamiltonian and its measured consequences |
| the published encoding's cost | **Assert**, rebuilt and measured (§4.1, §8.3), framed as testing the paper's claims. The structured exact encoding (S2) is ours, as a fairness device, never as a rival solver |
| "the solution was read out" | **Assert as classical**: the field is decoded from the prepared state. The paper's interferometric protocol is built at small n and is further work; never "on hardware", never the method's readout |

Pre-empting the examiner's objection in your own voice is worth more than any amount of
enthusiasm. Snow devotes a paragraph to it:

> "**Limitations.** Honest accounting requires noting what the results do not establish." — Snow,
> §8.1

Write that paragraph (§9.6). Markers reward it under "awareness of the significance of the work and
its place in the wider field".

### 1.2 First person plural for method, impersonal for fact

Both exemplars use **"we"** for authorial choices and **impersonal constructions** for established
results. Do not lapse into pure passive; it reads as evasive and inflates word count.

- Good: "We generalise both the analytic MPD construction and the SSO framework to this family…"
  (Snow); "We consider target states of the form…" (Green)
- Good: "The infidelity is precisely the discarded Schmidt weight…" (Snow)
- Avoid: "It was decided that the descriptor form would be used." → *"We keep the banded factors of
  𝔾 rather than forming it."*

Use "this thesis" sparingly and only for scope statements. Use "I" only in the Summary of Student
Achievement, which the guidelines require in the first person.

### 1.3 Prose density

Target 4–8 sentence paragraphs, each carrying one claim plus its warrant. Neither exemplar has
one-sentence paragraphs in the body, and neither has half-page blocks.

Kill these on sight; they are pure page-budget waste:
- "It is important to note that…" → delete, state the thing
- "In this section, we will discuss…" → replace with the actual roadmap sentence
- "As mentioned previously…" → use `\Cref{}` instead
- "very", "quite", "extremely", "obviously", "clearly" → delete or quantify
- "This is a very significant improvement" → "This is a factor of N³ in the degree"

### 1.4 Australian/UK spelling, consistently

The preamble loads `[australian]{babel}`. Both exemplars use *normalise, parameterise, discretise,
behaviour, generalise*. Never mix. Cite package and function names verbatim (`optimization_level`).

---

## 2. Mathematical & Algorithm Exposition

### 2.1 Definition–theorem discipline, but earn each one

Green uses numbered `definition` blocks; Snow uses fewer definitions but formal theorems and
propositions with proofs for the results that carry the thesis.

**A numbered environment is for an object you refer back to.** Background used once is prose.
Reserve numbered blocks for:

- the (α, m, ε) block encoding (α is used throughout);
- the physics-informed Hamiltonian H = R†R of a stacked residual;
- the banded factorisation 𝔾 = B̃⁻¹D̃;
- the Carleman lift.

Reserve **theorems and propositions with proofs** for your own claims. Snow's Theorem 4.1
(fidelity guarantee) is the model: a formal statement, a proof that fits on half a page, then two
paragraphs of what the bound *means*. Candidates here: kernel equivalence (both layouts); the
factorisation of 𝔾; the stacked reflection; the descriptor's cost; the nodal fold's optimality
(α = 2 = ‖𝕟₁‖, so optimal, not merely tight); the doubled space's kernel is a subspace and
product states are not, so no answer-independent penalty makes it one-dimensional.

### 2.2 Intuition first, formalism second, consequence third

The strongest shared pattern in both exemplars. Every non-trivial construction is introduced in
three moves:

1. **The idea in one sentence, in words.**
   > "The idea in one line is to peel a qubit off the left, compress the link it exposes, and carry
   > the remainder forward, repeating until the whole chain has been built." — Snow, §2.3.4
2. **The formal object.** Equations, an algorithm listing, or a circuit.
3. **What it costs and what it buys.** Immediately, not three pages later.

The descriptor chapter opens exactly this way: *differentiation of a Chebyshev series is banded if
the derivative may live in a neighbouring basis; keeping the banded factors, and carrying the
derivatives as unknowns where the equation needs them, buys a banded residual whose Hamiltonian's
norm grows as N² rather than N^{4k}, at the cost of a block register and a gap the derivative
blocks erode.* Then the algebra. Then the cost.

### 2.3 Annotated algorithm listings

Green's algorithms are terse Require/Ensure blocks. Snow follows each listing with a
**line-referenced walkthrough** under sub-headings ("Inputs and outputs", "The first factorisation
(lines 1–5)", "The sweep (lines 6–10)"). Use Snow's model for the descriptor's term IR → circuit
compilation (§5.7).

### 2.4 Figures and circuit diagrams

`quantikz` is loaded. Both exemplars use circuit figures sparingly, each with a caption that
explains the *structure*:

> "Each gate is shaded and labelled by its arity $1 + \log_2 b_m$… the arity ramps up from the
> boundary, plateaus at $1 + \log_2\chi$ in the bulk, and tapers to a single-qubit gate at site
> $n$." — Snow, Fig. 6.1

Body circuits (ThesisPlanning.md §7): U_odd's SELECT (F3), the descriptor's flat LCU (F5), and
optionally the GQSP circuit (F2). The model-configuration diagram (F1, TikZ) and the headline
scaling figure (F9) are what a marker skimming the list of figures will use to decide what the work
*is*; caption both so each stands alone as a summary. Do **not** draw a Hadamard-and-CNOT toy in the
background, and do not draw the interferometric readout in the body: it is not the method's
readout.

### 2.5 Notation discipline

Fix every symbol once, early, and never overload. Snow's methods table doubles as a notation key:
*"$T$ denotes training iterations, $n$ qubits, $L$ layers, and $\chi_{\max}$ the maximum
intermediate MPS bond dimension."*

The master table is ThesisPlanning.md §8.1 (front matter, `1_header/6_notation.tex`), with its
collisions resolved in §8.2: β only for the QITE filter's imaginary time, ρ for the Carleman ratio,
ζ for the rescaling, tiers T1–T3 never as maths. Verify at every review (`../CLAUDE.md`,
Verification Mode). Snow footnotes his change of logarithm base where it happens; do the same for
any convention that changes mid-thesis.

### 2.6 Narrative primacy — what stays in the body, what goes to an appendix

**The body carries the story and the appendices carry the apparatus.** Appendices do not count
against the 40–60 pages, and the rubric invites them. This is a licence to keep the argument
legible, not to hide work.

A body passage earns its space if it does one of four things:

1. **States the idea**: the move, in words, before any algebra.
2. **States the object**: the construction written down once, not derived.
3. **States the cost**: a formal proposition, or a measured number.
4. **Interprets**: what the object or the number means operationally.

Everything else is apparatus: entry-level formulae, term-by-term constructions, proofs, per-case
parameter tables, software architecture, protocol detail. Send it to an appendix and point at it.

**The equation test.** Before an equation stays in the body, ask: *does the argument break if a
reader skips it?* If the prose still carries the reader to the next claim, the equation belongs in
an appendix. A referee reading Chapter 5 wants 𝔾 = B̃⁻¹D̃ and the block structure it induces, not
the recurrence that generates B̃'s entries.

**The figure test.** Every body figure is interpreted in at least one paragraph. If you cannot
write that paragraph, the figure belongs in an appendix or nowhere.

**The pointer rule.** Never "see Appendix G"; write *"the kernel-equivalence proof and the
mass-form rows are given in Appendix G."*

**What this does not license.** Results must be understandable "without reference to any other
documents". Every number in the body is derivable from the body or an appendix, never from the
repository, a notebook or a README.

### 2.7 A scientific argument, not a code map

The project was built as software; the thesis is not about the software. ThesisPlanning.md §3.5's
rules, in brief: every chapter opens with its question and closes with its answer; constructions
are stated as mathematics, never as function names; findings are stated as findings, never as the
history of the issue that found them; records, campaigns, hashes and Slurm live in Appendix L; each
benchmark problem is introduced by the physics it carries.

---

## 3. Empirical Presentation

### 3.1 Quantify relentlessly, through `\res`

Neither exemplar makes a comparative claim without a number:

> "on the disordered Heisenberg target it attained $F \approx 0.999$ at $\sim 3\times10^3$ CNOTs;
> an order of magnitude below the 43,170 CNOTs of the exact full-bond mapping." — Snow, §7.2

Here every such number comes from the records by key (`0_results/README.md`): the three encodings'
degrees at n = 8, the degree exponents, α/‖·‖, ancilla and cx per query, the gap and γ² before and
after rescaling, T1 against T2, the field error against its bound, the lift's error per order, the
Navier–Stokes degree ratios. A number typed by hand is a defect even when it is right today.

### 3.2 State the cost model before the first cost claim, with its bias

Snow's most disciplined move:

> "Each $\chi$-staircase is costed at the worst-case decomposition bound of its constituent gates…
> We stress that this costing is deliberately conservative for the higher-$\chi$ layers… Any
> intermediate-$\chi$ advantage reported below is thus a *lower bound* on the advantage available
> under improved compilation."

Do the same (§7.8) before any standard-versus-descriptor number: what counts as a gate, how ancilla
are counted, and **which way the convention biases the comparison**. Ours: the structured encoding
is the strongest standard-form baseline built, and every comparison is also quoted at the
ideal-encoding bound α = ‖R‖, which contains neither form's encoding. A conservative convention that
still favours your method persuades; one that hides a reversal is found.

### 3.3 Numbered findings, some negative

Green closes his numerical study with four numbered findings, two of them negative. Copy the format
and the honesty. Chapter 8 closes on six or seven (§8.7), at least two negative: the reversals at the
ideal bound and on the heat panel; the gap falling on two axes; a trusted kernel hiding a diverging
lift; Navier–Stokes reached by emulation and estimate only.

### 3.4 Self-contained figure and table captions

The template:

> **Figure N: [Bold claim, not a label].** [What is plotted, on what axes, for what problem, with
> what parameters.] [What panel (a) shows; what panel (b) shows.] [The one takeaway.] [The tier.]

Compare *"Figure 5: Gate counts."* with Snow's:

> "**Analytic $\chi$-staircase performance on the 2D Heisenberg ground state** ($4\times4$ lattice,
> $n = 16$…). **(a)** Fidelity to target versus total CNOT count… **(b)** The corresponding
> infidelity… Analytically, the most CNOT-efficient bond dimension migrates from $\chi = 2$ to
> $\chi = 4$ to $\chi = 8$ as the depth budget grows."

### 3.5 Comparison tables against the literature

Both exemplars anchor their contribution with a table whose rows are methods and whose columns are
resources, with a "This Work" row. Two here: **T1** (§2.2), quantum DE approaches by assumptions,
cost driver, output and failure mode; and **T7** (§8.3), the published, structured and descriptor
encodings across ‖H‖, gap, α/‖·‖, cx per query, ancilla, exactness, and the degree as built and at
α = ‖R‖. **Three encodings**: the middle one separates the encoder wall from the Hamiltonian wall.
FABLE does not appear. T7 is referenced from the Abstract.

### 3.6 Report the negative and the dimension-capped honestly

Keep *"we could not simulate it"* apart from *"the algorithm cannot reach it"* every time it
arises; quote the estimate that refused a run. The guidelines ask for "the positive (and negative)
results and their significance" and note that "a thesis can be an excellent one, even though the
project did not achieve its aims."

---

## 4. Signposting & Transitions

### 4.1 The gap statement is a named section

Green §1.1 "Gaps in the Literature and Contribution"; Snow §3.6 "Synthesis: the gap this thesis
addresses", which poses italic questions and names the chapter that answers each:

> "Two questions therefore remained open. *(i) What per-layer objective should learned disentangling
> use?* Chapter 4 argues that… *(ii) How expressive should each layer be?* … Chapter 6 treats
> per-layer bond dimension as a design variable…"

Ours is stronger, because it starts from the source paper's own Discussion ("studying the spectral
gap dependence is an important question for the future work"; "the cost of differentiation") and
is raised by a critical assessment the reader has just watched. §3.6 poses Q(i)–(iii) in italics,
each answered by `\Cref`: (i) *is the cost the encoder's or the Hamiltonian's?* → Chapter 4; (ii)
*can the residual be reformulated so that its Hamiltonian is banded and well conditioned, without
changing its solution, and what does that cost?* → Chapter 5; (iii) *can nonlinear equations be
prepared rather than projected?* → Chapter 6.

### 4.2 Chapter-opening roadmaps, one to three sentences

> "This chapter assembles the technical machinery used throughout the thesis. The treatment is
> self-contained at the level needed to follow the algorithms and proofs of later chapters; for a
> fuller account… we refer the reader to…" — Snow, Ch. 2

The second clause licenses brevity, which the marking guide rewards. Chapters 4–6 open with their
question instead of a roadmap.

### 4.3 Forward and backward references carry a reason

Never a bare "see Section 5". Always the reason:

- "…the property that lets the nominal $O(Tn^2L\chi^3_{\max})$ complexity of (4.13) be realised in
  practice on hard targets." (Snow)

Use `\Cref{sec:...}` throughout; never hard-code a number.

### 4.4 The recurring spine sentence

Both exemplars restate their thesis in one line at the end of each major section. Ours
(ThesisPlanning.md §3.3), placed in the Abstract, §1.3, §3.6, §5.1, §5.10, §8.7 and §10.1, reworded
each time:

> *Carrying the intermediate derivatives instead of eliminating them turns the physics-informed
> residual from dense to banded with its kernel unchanged, so the Hamiltonian's norm falls from
> Θ(N⁸) to Θ(N²) for a second-order equation; the price is a block register and a gap the
> derivative blocks erode, which an a priori rescaling restores on one axis at no gate cost.*

### 4.5 Section-closing summaries for long sections

Green closes his MPS chapter with "Summary"; Snow closes each results chapter with one. Use them
after Chapter 5 (§5.10) and Chapter 8 (§8.7): 3–7 numbered takeaways.

---

## 5. Common Traps (rubric-penalised)

| # | trap | why it is penalised | fix |
| :-- | :-- | :-- | :-- |
| 1 | **Textbook background** | "the bulk of the report should be aimed at the professional physicist"; background brief, "the bulk… dealing with results and discussion" | prose citing Nielsen & Chuang; gate table to Appendix A; §2.1 ≤ 1.5 pp |
| 2 | **Catalogue results** | "clear focus… capacity to avoid the intrusion of less relevant detail" | one section per question; three representative problems in depth; the rest in Appendix J |
| 3 | **Page overrun** | an explicit penalty beyond 60 pages | the budget and trim order of ThesisPlanning.md §4.1 |
| 4 | **Uncredited antecedents** | "usual conventions… particularly as to references" | credit the ultraspherical method and first-order-system least squares where the headline is claimed; cite the concurrent Paine 2026 |
| 5 | **Colloquial register** | "avoiding colloquial language" | no "a bit", "huge", "we tried", rhetorical questions or exclamation marks |
| 6 | **Method narrated chronologically** | reads as a lab diary | present the final construction and its reason; findings, not history |
| 7 | **Undefined notation on first use** | "understandability for the reader, even one without specialized knowledge" | the notation table; Verification Mode |
| 8 | **Orphaned `\todo` notes, `\nocite{*}`** | visibly unfinished | strip before submission |
| 9 | **Over-claiming a speed-up** | fatal to credibility with a QC-literate marker | say first that neither form is poly-log; claim the degree's scaling, scoped |
| 10 | **Figures without discussion** | results must be analysed, not displayed | a paragraph per figure, or the figure goes |
| 11 | **Boilerplate transitions** | wastes the scored page budget | state the finding |
| 12 | **A thin Discussion** | significance is weighted heavily | why the trade-off exists, where it fails, what a practitioner should choose, what it means for the field |
| 13 | **Blurring prior art into contribution** | the fastest route to an academic-integrity conversation | attribute Wu et al. at the head of Chapter 3 and at each construction; "we" for our work from Chapter 4 on |
| 14 | **The published route as a rival you also built** | halves the apparent focus; invites "so what is new?" | the published encoding is rebuilt *to test the paper's claims*; the structured encoding (S2) is ours, framed as isolating the Hamiltonian's cost |
| 15 | **Body pages spent on derivation** | buries the narrative | the equation test (§2.6); derivations in Appendices B, E–H |
| 16 | **Implying the readout was performed on hardware, or is the method's** | a QC-literate marker will ask | "decoded classically from the prepared state"; the interferometric protocol is the paper's, built at small n, further work |
| 17 | **An unscoped descriptor claim** | the claim is false for part of the ladder, and a referee will find the part | every degree, gap and α claim carries its class (regular one-axis, singular, two-axis) |
| 18 | **Code-map drift** | the rubric scores a model, not a tour of the software | function names, records and campaigns out of the body (ThesisPlanning.md §3.5) |
| 19 | **Trust read as convergence** | a trusted kernel certifies the lifted linear problem, not the lift | quote the lift's measured error beside every Carleman preparation |
| 20 | **Hiding a reversal** | the fairness device exists to show it | report the ideal-bound comparison everywhere, and number the reversals among the findings |

---

## 6. The "Publishable Paper" Test

Before submitting any section, check it against these. Both exemplars pass all six.

1. **Could a referee reproduce it?** Every construction has its parameters, a cost model and a
   verification residual.
2. **Is the contribution separable from the background?** In one sentence each: *the
   physics-informed effective Hamiltonian framework is Wu et al.'s; banded differentiation and
   first-order least squares are classical; the descriptor reformulation transfers them to the
   block-encoded Hamiltonian, keeps its kernel, and lowers its norm from Θ(N^{4k}) to Θ(N²), at the
   cost of a block register and a gap that needs rescaling.*
3. **Are the limitations stated by the author, not discovered by the referee?**
4. **Does every figure earn its half-page?**
5. **Is the comparison fair by construction?** Cost conventions stated; the ideal-encoding bound
   beside every as-built number.
6. **Does the Abstract contain numbers?** Both exemplars' do.

---

## 7. Quick Reference — Register Examples

Rewrites illustrating the target register. Use the pattern, not the text; quote numbers by `\res`.

| weak | target register |
| :-- | :-- |
| "We tried a few ways to encode $H$ and the descriptor one worked best." | "Under one cost model, and again at the ideal-encoding bound, the descriptor's filter degree grows as $N$ on a regular one-axis second-order problem, where the standard form's grows as $N^{4}$." |
| "We developed a physics-informed Hamiltonian method for differential equations." | "Wu et al. cast a differential equation as the ground state of a physics-informed effective Hamiltonian \cite{wu2025pihm}. This thesis reformulates the residual that Hamiltonian is built from, so that it is banded." |
| "Our descriptor is a new idea." | "Banded differentiation is the ultraspherical method's \cite{olver2013}, and avoiding the squared condition number of a high-order least-squares problem is first-order-system least squares' \cite{…}. The increment here is their transfer to a block-encoded Hamiltonian: the kernel is unchanged, the residual is one flat LCU, and the filter's degree falls accordingly." |
| "The descriptor has a flat gap." | "On a one-axis equation whose leading coefficient does not vanish, the rescaled descriptor's gap is flat in $N$; where the coefficient vanishes, and on two axes, it is not (\Cref{sec:descriptor-gap})." |
| "The prepared solution can then be read out." | "The field is decoded classically from the prepared state's field blocks and scaled by the regular datum. The paper's interferometric protocol, built and verified at small $n$, is left to future work." |
| "The gap is really small in the standard form." | "At $n = 7$ the standard form's relative gap lies below double-precision resolution by `eigh` but not by SVD; what it costs is the filter's degree, which grows as $N^{4}$ for this second-order problem." |
| "This gives an exponential speed-up." | "Neither form is poly-logarithmic. The degree is $\Theta(\sqrt{\alpha_H/\Delta}\log 1/\varepsilon)$ with $\alpha_H \ge \|H\|$ for any block encoding; the reformulation lowers $\|H\|$ from $\Theta(N^{8})$ to $\Theta(N^{2})$ for a second-order equation, and with it the degree from $\tilde\Theta(N^4)$ to $\tilde\Theta(N)$ on a regular one-axis problem." |
| "The results were verified." | "Each circuit equals its independently assembled operator: exactly to 25 qubits, by probe on every construction-only circuit of at most 24, and by IR at any size. Where both run, the simulated circuit equals the exact emulation to within $10^{-10}$ before normalising." |
| "Burgers was solved with Carleman." | "The lift's kernel is one-dimensional at every order, so imaginary time prepares it; whether the lift converges is a separate question, answered by its error per order, which follows $a/\nu$ and not $\rho$." |

---

*Companion documents: `STRUCTURE_AND_RUBRIC.md` (rubric and exemplars), `../ThesisPlanning.md`
(structure), `../CLAUDE.md` (working agreement and Standing Facts).*
