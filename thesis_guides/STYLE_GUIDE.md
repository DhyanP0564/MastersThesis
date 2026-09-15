# STYLE_GUIDE.md — Stylistic DNA for the Thesis

Distilled from two high-scoring UWA physics theses (Green 2024, Honours, *Efficient
Quantum State Preparation*; Snow 2026, Masters, *Highly Optimised Quantum Circuit
Synthesis for Classical Data Encoding*) read against the School's marking guide.

The governing standard, stated plainly: **the markers are professors reading for
publishable work.** A thesis that could be cut down into a PRA submission with
minimal surgery scores well. A thesis that reads like a lab report, a tutorial, or
a catalogue of everything the student tried does not. Every rule below descends
from that standard.

---

## 1. Tone & Voice

### 1.1 Assert what you measured; hedge what you inferred

Both exemplars are notably **unhedged about their own results** and **carefully
hedged about extrapolations**. The distinction is the single most important tonal
habit to copy.

Assert (measured, verified, in-repo):

> "SSO improves prepared-state infidelity by roughly an order of magnitude over the
> Matrix Product Disentangler baseline at fixed depth" — Snow, Abstract

Hedge (inferred, asymptotic, unproven):

> "It should be noted that there are no rigorous guarantees in the root-exponential
> decay of $\|P\|_\infty$, which may not hold in some extreme cases." — Green, §5.2.2

For your work the boundary is sharp and you should police it:

| Claim | Register |
| :-- | :-- |
| $O(n^2)$ gates, $O(1)$ ancilla for the descriptor $E_{A}$ | **Assert** — gate-level, verified |
| $\alpha_H \to \|H_{\mathrm{sys}}\|$, tight | **Assert** — measured |
| Spectral gap $\sim 10^{-6}$ (descriptor) vs $\sim 10^{-15}$ (collocation) at $n=7$ | **Assert**, and state the machine-epsilon consequence |
| Composed $H$ correctness at 22+ qubits | **Hedge explicitly** — verified *by parts*, not end-to-end; say so and say why (dense simulation allocates hundreds of GB) |
| "A ground state has been prepared" | **Never assert.** Every GQSP figure is a classical simulation of the minimax filter, capped at $\dim \lesssim 2000$ by simulation cost, not by the algorithm |
| End-to-end poly-log speed-up | **Deny it yourself, first.** Neither route is poly-log; $\alpha_H \ge \|H_{\mathrm{sys}}\| = \Theta(N^2)$ against $\Delta = \Theta(1)$ forces $\tilde\Theta(N^2)$ queries for *any* encoding of this $H$. The claim is that the descriptor construction **meets** that floor |
| The physics-informed effective Hamiltonian framework | **Attribute, then judge.** It is Wu et al.'s (`wu2025pihm`). Describe it in §2.4 in the register of reported prior art, cite at the head of the subsection and at each specific construction, and reserve the verdict for §2.4.3 |
| The collocation encoding's failure | **Assert** — you implemented and measured it (§5.2). But frame it as *characterising the published route*, never as a rival method you also invented |
| "The solution was read out" | **Never assert.** No measurement protocol is implemented in this thesis. Every reported solution error is a classical state-vector read; readout appears only as prior art (§2.7), a costed feasibility statement (§3.9), a limitation (§6.5) and future work (§7.2) |

Pre-empting the examiner's objection in your own voice is worth more than any
amount of enthusiasm. Snow devotes a whole subsection to it:

> "**Limitations.** Honest accounting requires noting what the results do not
> establish." — Snow, §8.1

Write that paragraph. Markers reward it under *"awareness of the significance of
the work and its place in the wider field."*

### 1.2 First person plural for method, impersonal for fact

Both exemplars use **"we"** for authorial choices and **impersonal constructions**
for established results. Do not lapse into pure passive — it reads as evasive and
inflates word count.

- Good: "We generalise both the analytic MPD construction and the SSO framework to
  this family…" (Snow); "We consider target states of the form…" (Green)
- Good: "The infidelity is precisely the discarded Schmidt weight…" (Snow)
- Avoid: "It was decided that the descriptor form would be used." → *"We carry the
  intermediate derivatives rather than eliminating them."*

Use "this thesis" sparingly and only for scope statements ("This thesis addresses…",
"the contribution of this work is…"). Use "I" only in the Summary of Student
Achievement, which the guidelines require in first person.

### 1.3 Prose density

Target ~4–8 sentence paragraphs, each carrying one claim plus its warrant. Neither
exemplar has one-sentence paragraphs in the body, and neither has half-page blocks.

Kill these on sight — they are pure page-budget waste:
- "It is important to note that…" → delete, state the thing
- "In this section, we will discuss…" → replace with the actual roadmap sentence
- "As mentioned previously…" → use `\Cref{}` instead
- "very", "quite", "extremely", "obviously", "clearly" → delete or quantify
- "This is a very significant improvement" → "This is a factor of $N^6$ improvement"

### 1.4 Australian/UK spelling, consistently

Your preamble already loads `[australian]{babel}`. Both exemplars use *normalise,
parameterise, discretise, behaviour, generalise*. Pick it and never mix. Note the
exception: cite package/function names verbatim (`normalize` if that is the API).

---

## 2. Mathematical & Algorithm Exposition

### 2.1 Definition–theorem discipline, but earn each one

Green uses numbered `\begin{definition}` blocks (State Space, Qubit, Composite
Systems, Evolution Operator, Entanglement Entropy…) — you have already mirrored this
in `2_literature.tex`. Snow uses fewer definitions but adds formal `Theorem`/`Proposition`
with proofs for the results that carry the thesis.

The rule: **a numbered environment is for objects you will refer back to.** If a
definition is never re-invoked, it is background prose and belongs in a sentence or
an appendix. Your current lit review has ~9 definition blocks for standard QC
material — that is the right *style* but far too many for a subsection now capped at
two pages (see STRUCTURE_AND_RUBRIC.md §2.1 and §4/§2). Compress the elementary ones into flowing prose with
inline definitions, and reserve numbered blocks for:

- Block-encoding, $(\alpha, m, \epsilon)$ — you use $\alpha$ throughout
- The PIHM effective Hamiltonian $H = A^\top A + \sum_i B_i^\top B_i$
- The descriptor factorisation $G = \tilde{B}^{-1}\tilde{D}$
- The Carleman lift

Reserve **theorems with proofs** for your own claims. Snow's Theorem 4.1 (fidelity
guarantee) is the structural model: a formal statement, a proof that fits on half a
page, then two paragraphs of interpretation explaining what the bound *means*
operationally. Candidates in your work: the bandedness of $A_{\mathrm{sys}}$; the
ancilla count of the descriptor encoding; the optimality of the nodal fold
($\alpha = 2 = \|n_1\|$, so optimal not merely tight).

### 2.2 Intuition first, formalism second, consequence third

This is the strongest shared pattern in both exemplars and the highest-leverage
habit to adopt. Every non-trivial construction is introduced in three moves:

1. **The idea in one sentence, in words.**
   > "The idea in one line is to peel a qubit off the left, compress the link it
   > exposes, and carry the remainder forward, repeating until the whole chain has
   > been built." — Snow, §2.3.4
2. **The formal object.** Equations, algorithm listing, or circuit.
3. **What it costs / what it buys.** Immediately, not three pages later.

Your descriptor reformulation should open exactly this way. Something with the shape
of: *differentiation of a Chebyshev series is banded if the derivative is allowed to
live in a slightly different basis; carrying $f', f''$ as their own unknown blocks
buys that bandedness for the whole PIHM residual, at the cost of a
$\lceil\log_2(k{+}1)\rceil$-qubit block index.* Then the algebra. Then the gate count.

### 2.3 Annotated algorithm listings

Green's Algorithms 1–4 (`algorithm2e`, which you already load) are terse
Require/Ensure/numbered-line blocks. Snow goes further and follows each listing with
a **line-referenced walkthrough** under sub-headings ("Inputs and outputs", "The
first factorisation (lines 1–5)", "The sweep (lines 6–10)", "Termination (line 11)").

For a construction as intricate as the descriptor block encoding, use Snow's model.
It lets a non-specialist marker follow the mechanism without you inflating the
listing itself with comments.

### 2.4 Circuit diagrams

You already load `quantikz`. Both exemplars use circuit figures sparingly and always
with a caption that explains the *structure*, not just names the parts:

> "Each gate is shaded and labelled by its arity $1 + \log_2 b_m$… the arity ramps
> up from the boundary, plateaus at $1 + \log_2\chi$ in the bulk, and tapers to a
> single-qubit gate at site $n$. Increasing $\chi$ does not add gates — the layer
> always holds $n$ of them, one per site — but widens those in the bulk." — Snow, Fig. 6.1

Draw, in the body: the end-to-end pipeline schematic that opens §3.1, the descriptor
`PREPARE/SELECT/PREPARE†` LCU, one representative derivative atom, and the GQSP-QITE
filter. That is four body circuits and it is enough. Do **not** draw a
Hadamard-and-CNOT toy circuit in the background section, and do not draw a readout
primitive — no measurement protocol is implemented, so a circuit for one would imply
work that was not done. Put the gate table in Appendix A as your `\todo` already plans.

The §3.1 pipeline schematic is the most valuable figure in the thesis. It is what a
marker skimming `\listoffigures` will use to decide what the work *is*. Caption it so
it stands alone as a summary of the contribution.

### 2.5 Notation discipline

Fix every symbol once, early, and never overload. Snow includes an explicit
convention paragraph and a methods-comparison table (his Table 5.1) that doubles as
a notation key: *"$T$ denotes training iterations, $n$ qubits, $L$ layers, and
$\chi_{\max}$ the maximum intermediate MPS bond dimension."*

Your manuscript needs the same for: $n$ (qubits) vs $N = 2^n$ (dimension), $k$ (DE
order), $p$ (nonlinear degree), $\alpha$ (subnormalisation), $\Delta$ (spectral
gap), $G$, $\tilde{B}$, $\tilde{D}$, $A_{\mathrm{sys}}$, $H_{\mathrm{sys}}$,
$\epsilon_G$, $M$. Put it in a table at the end of the background section or in the
glossary you already load. Then **verify consistency at every review** — see
`CLAUDE.md` Verification Mode.

Footnote the one genuine trap: if you quote entropies or logs in different bases in
different sections, say so where it changes. Snow does exactly this in a footnote to
§2.3.2 rather than letting the reader trip over it.

### 2.6 Narrative primacy — what stays in the body, what goes to an appendix

The governing structural decision of this thesis is that **the body carries the
story and the appendices carry the apparatus.** The appendices do not count against
the 40–60 page limit, and both rubric variants explicitly invite their use. This is
not a licence to hide work; it is a licence to keep the argument legible.

A body passage earns its space if it does one of four things:

1. **States the idea** — the move, in words, before any algebra.
2. **States the object** — the construction written down once, not derived.
3. **States the cost** — a formal proposition, or a measured number.
4. **Interprets** — what the object or the number means operationally.

Everything else is apparatus: entry-level formulae, atom-by-atom constructions,
proofs, per-case parameter tables, software architecture, protocol detail. Send it to
an appendix and point at it.

**The equation test.** Before an equation stays in the body, ask: *does the argument
break if a reader skips it?* If the surrounding prose still carries the reader to the
next claim, the equation is illustrating rather than arguing, and it belongs in an
appendix. Applied honestly this removes most of a construction's algebra and none of
its persuasive force — a referee reading §3 wants to see $G = \tilde{B}^{-1}\tilde{D}$
and the block structure it induces, not the recurrence that generates $\tilde{B}$'s
entries.

**The figure test.** The same question, harder. Every body figure must be interpreted
in at least one paragraph of prose (the rubric penalises displayed-but-undiscussed
results). If you cannot write that paragraph, the figure is not carrying narrative
weight, and it belongs in an appendix or nowhere.

**The pointer rule.** Never write a bare cross-reference. Not *"see Appendix C"* but
*"the atom-by-atom constructions, and the column-by-column residuals establishing
each, are given in Appendix C."* A body that offloads without naming what was
offloaded reads as evasive; one that names it reads as disciplined, and it is the
difference between a marker trusting the structure and suspecting it.

**What this does not license.** Self-containment is required twice in the marking
guide: results must be understandable *"without reference to any other documents."*
Appendices are part of the document; the repository is not. Every number in the body
must be derivable from the body or from an appendix — never from `DESolverLib`, the
notebooks, or a README.

---

## 3. Empirical Presentation

### 3.1 Quantify relentlessly

Neither exemplar makes a comparative claim without a number attached. Snow:

> "on the disordered Heisenberg target it attained $F \approx 0.999$ at
> $\sim 3\times10^3$ CNOTs; an order of magnitude below the 43,170 CNOTs of the exact
> full-bond mapping."

Green: *"achieving a fidelity of 99.61%. The circuit depth was 3665 gates after
Qiskit decomposition."*

Your equivalents are already measured and should appear in this register: the
$O(n^2)$-vs-$\Theta(N^2)$ gate count, 9–10 ancilla flat in $n$ vs $n+3$, $\alpha_H$
$\Theta(N^2)$ vs $\approx\Theta(N^8)$, $p_{\mathrm{succ}} \to \Theta(1)$ vs
$N^{-3/2}$, the gap $10^{-6}$ vs $10^{-15}$, verification residuals $10^{-9}$–$10^{-11}$
and composition $< 10^{-10}$, $\cos\mathrm{sim} = 1.000000$ for the certified solution.

### 3.2 State the cost model before the first cost claim

Snow's most disciplined move: he fixes the accounting convention explicitly, and
declares its bias.

> "Each $\chi$-staircase is costed at the worst-case decomposition bound of its
> constituent gates given by the QSD recurrence… We stress that this costing is
> deliberately conservative for the higher-$\chi$ layers… Any intermediate-$\chi$
> advantage reported below is thus a *lower bound* on the advantage available under
> improved compilation."

Do the same before any descriptor-vs-collocation number: say what counts as a gate,
which decomposition you assume, whether ancilla are counted per-atom or composed,
and — critically — **which direction your convention biases the comparison.** A
conservative convention that still favours your method is far more persuasive than a
favourable one, and it disarms the obvious objection.

### 3.3 Numbered findings

Green closes his main numerical study with four bolded, numbered findings:

> "**1.** The analytic MPD scheme introduced by Ran generates exceptionally efficient,
> low-depth, and accurate circuits… **2.** The MPD algorithm generalises poorly beyond…
> **3.** The Ran+Opt scheme significantly improves… **4.** The Ran+Opt scheme suffers
> from trainability problems as the number of qubits increases."

Note that two of four findings are **negative**. Copy both the format and the
honesty. Your Results section should close on 4–6 numbered findings, and at least
one should be a limitation of your own method (e.g. the Hilbert-space growth,
$2^{\lceil\log_2(k+1)\rceil} \cdot N$ vs $N$, or the doubled-space route projecting
rather than preparing).

### 3.4 Self-contained figure and table captions

Both exemplars write captions that a marker can read in isolation. The template:

> **Figure N: [Bolded claim, not a label].** [What is plotted, on what axes, for what
> system with what parameters.] [What panel (a) shows; what panel (b) shows.] [The
> one thing the reader should take away.]

Compare a weak caption — *"Figure 5: Gate counts."* — with Snow's:

> "**Analytic $\chi$-staircase performance on the 2D Heisenberg ground state**
> ($4\times4$ lattice, $n = 16$; ground state of $H = \sum_{\langle ij\rangle}
> S_i\cdot S_j$ represented as an MPS of bond dimension $\chi_{\max}\le 64$).
> **(a)** Fidelity to target versus total CNOT count… **(b)** The corresponding
> infidelity… Analytically, the most CNOT-efficient bond dimension migrates from
> $\chi = 2$ to $\chi = 4$ to $\chi = 8$ as the depth budget grows."

Since you load `\listoffigures`, a marker may well skim captions first. Make them
load-bearing.

### 3.5 Comparison tables against the literature

Both exemplars anchor their contribution with a table whose rows are *methods* and
whose columns are *resources*. Green's Table 5.4 (Depth | Ancillas | Avoids
Arithmetic | Scope); Snow's Table 5.1 (Loss function | Layerwise | Joint | Init |
Complexity). Each has a "This Work" row.

You need two. **(i)** In §2, quantum DE-solving approaches (HHL-family / Carleman /
variational / physics-informed) with a "this work" row — this table is where the
literature review's critical assessment becomes legible at a glance. **(ii)** In §5.3,
encoding cost: the published collocation encoding versus the descriptor construction,
across gates, ancilla, $\alpha$, exactness and gap. **Two rows, not three** — FABLE is
not part of this thesis's story and does not appear. The second table is your headline
result and should be referenced from the Abstract.

### 3.6 Report the negative and the dimension-capped honestly

Your repo distinguishes *"we could not simulate the filter"* from *"the algorithm
cannot reach it."* Preserve that distinction in the prose every time it arises — it
is exactly the kind of precision that separates a High Distinction from a Distinction.
The marking guide explicitly asks for *"the positive (and negative) results and their
significance"* and notes *"a thesis can be an excellent one, even though the project
did not achieve its aims."*

---

## 4. Signposting & Transitions

### 4.1 The gap statement is a named section

Both exemplars close the literature review by naming the gap explicitly:

- Green §1.1: "Gaps in the Literature and Contribution"
- Snow §3.6: "Synthesis: the gap this thesis addresses", which ends by posing the
  open questions as italicised questions, then answering which chapter resolves each.

Snow's closing move is worth copying almost structurally:

> "Two questions therefore remained open. *(i) What per-layer objective should learned
> disentangling use?* Chapter 4 argues that… *(ii) How expressive should each layer
> be?* … Chapter 6 treats per-layer bond dimension as a design variable…"

Your analogue, and note that under the current framing both questions are raised *by
the critical assessment of Wu et al.'s encoding in §2.4.3*, not by a gap you assert
into existence: *(i) Can the physics-informed residual be block-encoded without the
$\Theta(N^2)$ uniformly-controlled-rotation cost, and with a spectral gap that survives
double precision?* → §3, the descriptor reformulation. *(ii) Does the same structural
move extend to polynomial nonlinearity?* → §4, the Carleman lift and nodal fold.

This is the strongest available version of the gap statement, because the reader has
just watched you diagnose the published method rather than being told a gap exists.
§2.8 should pose the two questions in italics and name the section that answers each,
by `\Cref`, exactly as Snow does.

### 4.2 Chapter-opening roadmaps, one to three sentences

Every exemplar chapter opens by declaring its job and its boundary:

> "This chapter assembles the technical machinery used throughout the thesis. The
> treatment is self-contained at the level needed to follow the algorithms and proofs
> of later chapters; for a fuller account… we refer the reader to…" — Snow, Ch. 2

That second clause is doing real work: it licenses brevity, which the marking guide
rewards. Use it to justify compressing standard quantum-computing background.

### 4.3 Forward and backward references carry a reason

Never a bare "see Section 5". Always the reason:

- "…the property that lets the nominal $O(Tn^2L\chi^3_{\max})$ complexity of (4.13)
  be realised in practice on hard targets."
- "This accumulated bound is what later converts a sum of per-bond truncation errors
  into a guarantee on the prepared-state fidelity, the basis of the analysis in
  Chapter 4."

You already load `cleveref`; use `\Cref{sec:...}` throughout and never hardcode a
number.

### 4.4 The recurring spine sentence

Both exemplars restate their thesis in one line at the end of each major section,
with slightly different emphasis each time. Snow's is the *"expressivity of each
disentangling layer should be matched to the entanglement actually remaining"*
principle, which recurs in the Abstract, §1.2, §7.5 and §8.1.

Draft your spine sentence before you write, and place it at the end of the
Introduction, the end of the descriptor methods section, the end of Results, and in
the Conclusion. Candidate shape: *carrying the intermediate derivatives instead of
eliminating them converts a dense residual into a banded one, and the whole
encoding-plus-preparation pipeline inherits the structure.*

### 4.5 Section-closing summaries for long sections

Green closes §4 with a "Summary" subsection; Snow closes §5 and §7 with "Summary."
Each is 3–5 sentences of numbered or enumerated takeaways. Use these after Results
and after the descriptor methods section — they are cheap, and they rescue a marker
who is skimming.

---

## 5. Common Traps (rubric-penalised)

Drawn from the marking guide's four stated assessment dimensions.

| # | Trap | Why it is penalised | Fix |
| :-- | :-- | :-- | :-- |
| 1 | **Textbook background** — deriving the Bloch sphere, tabulating Pauli matrices in the body | "The bulk of the report should be aimed at the professional physicist, not the narrow specialist"; and Part B §7 requires *"only a brief description of… background with the bulk of the report dealing with results and discussion"* | Compress to prose + cite Nielsen & Chuang; move gate tables to an appendix (as your `\todo` already plans) |
| 2 | **Catalogue results** — a subsection per DE case, each a paragraph and a plot | Penalised under "clear focus… capacity to avoid the intrusion of less relevant detail" | 3–4 representative cases in depth; the rest in one summary table + appendix (Snow's Appendix G is the model) |
| 3 | **Page over-run** | Explicit marks penalty in the guidelines: *"Overly exceed 60 pages"* | Budget per section up front; see STRUCTURE_AND_RUBRIC.md §4 |
| 4 | **Unreferenced claims** | "Usual conventions should be followed particularly as to references" | Every non-obvious assertion cites or points to your own verified result. Especially: credit the ultraspherical spectral method (Olver & Townsend 2013) as the antecedent of the descriptor basis change, and state precisely what *your* increment is |
| 5 | **Colloquial register** | Explicitly named: *"avoiding colloquial language"* | No "a bit", "pretty good", "huge", "we tried", rhetorical questions in the body, or exclamation marks |
| 6 | **Method narrated chronologically** | Reads as a lab diary, not a paper | Present the final construction and its justification. Failed routes go in Discussion as *characterised trade-offs*, not in Methods as a diary |
| 7 | **Undefined notation on first use** | "Clarity… understandability for the reader, even one without specialized knowledge" | Notation table; Verification Mode pass |
| 8 | **Orphaned `\todo` notes / `\nocite{*}`** | Presentation failure; visibly unfinished | Strip all `todonotes` and remove `\nocite{*}` from `main.tex` before submission — it currently pulls every entry in `ref.bib` into the bibliography |
| 9 | **Over-claiming a speed-up** | Fatal to credibility with a QC-literate marker | State the $\tilde\Theta(N^2)$ query floor yourself and claim only that descriptor *meets* it |
| 10 | **Figures without discussion** | "results & analysis" must be analysed, not displayed | Every figure gets at least one paragraph of interpretation; if it does not deserve one, it belongs in an appendix |
| 11 | **Boilerplate transitions** | Wastes the page budget the rubric is scoring you against | "This section will discuss…" → state the finding |
| 12 | **A one-paragraph Discussion** | The rubric weights significance-awareness heavily | Discussion must engage: why the trade-off exists, where the method fails, what a practitioner should choose, what it means for the field |
| 13 | **Blurring prior art into contribution** | Fatal to credibility, and the fastest route to an academic-integrity conversation. The physics-informed effective Hamiltonian framework is Wu et al.'s | Attribute at the head of §2.4 and at each specific construction. Read every sentence of §2.4 asking *could this be mistaken for a claim of authorship?* Reserve first-person-plural authorial "we" for §3 onwards |
| 14 | **Presenting the published route as a rival you also built** | Implies you invented two methods and picked one; halves the apparent focus of the thesis and invites "so what is actually new?" | §5.2 is framed as reproducing and characterising the published encoding. There is no descriptor-versus-collocation chapter, and the headline table in §5.3 has two rows |
| 15 | **Body pages spent on derivation** | Buries the narrative the whole structure is built to protect, and burns the page budget the rubric penalises you for exceeding | Apply the equation test in §2.6. Statement and cost in the body; derivation in Appendices B–E, with a pointer that names what is there |
| 16 | **Implying readout was performed** | No measurement protocol was implemented; every reported error is a classical state-vector read. A QC-literate marker will ask | Readout appears as prior art (§2.7), a costed feasibility statement (§3.9), a limitation (§6.5) and future work (§7.2). Never a method, never a results subsection, never a circuit figure |

---

## 6. The "Publishable Paper" Test

Before submitting any section, check it against these. Both exemplars pass all six.

1. **Could a referee reproduce it?** Every construction has parameters, a cost model,
   and a verification residual.
2. **Is the contribution separable from the background?** A reader must be able to
   say in one sentence what is new, and must be able to say in one sentence what was
   already there. Yours: *the physics-informed effective Hamiltonian framework is Wu
   et al.'s; the descriptor reformulation is this thesis's, and it makes their
   residual banded — replacing a $\Theta(N^2)$-gate, $(n{+}3)$-ancilla encoding with an
   $O(n^2)$-gate, $O(1)$-ancilla one, and keeping the spectral gap resolvable.*
3. **Are the limitations stated by the author, not discovered by the referee?**
4. **Does every figure earn its half-page?**
5. **Is the comparison fair by construction?** Cost conventions stated and biased
   against your own method where there is doubt.
6. **Does the Abstract contain numbers?** Both exemplars' abstracts do. Yours should
   carry the gate/ancilla/$\alpha$/gap figures.

---

## 7. Quick Reference — Register Examples

Rewrites illustrating the target register. Use the pattern, not the text.

| Weak | Target register |
| :-- | :-- |
| "We tried a few different ways to encode $H$ and the descriptor one worked best." | "Under a common cost model, the descriptor construction attains a subnormalisation that remains tight in $N$, which the published collocation encoding does not." |
| "We developed a physics-informed Hamiltonian method for differential equations." | "Wu et al. cast the differential equation as the ground state of a physics-informed effective Hamiltonian \\cite{wu2025pihm}. This thesis reformulates the residual that Hamiltonian is built from, so that its block encoding becomes banded." |
| "Our collocation implementation performs worse than our descriptor one." | "The published collocation encoding, reimplemented here and characterised in \\Cref{sec:baseline}, exhibits the failure diagnosed in \\Cref{sec:critical}: at $n = 7$ its composed $H$ has relative gap $\\sim 10^{-15}$." |
| "The prepared solution can then be read out." | "Extracting an observable from the prepared state requires a measurement protocol; the cost of the interferometric route is $\\mathcal{O}(\\cdot)$ per \\cite{williams2024readout}. No such protocol is implemented here — every error reported in \\Cref{sec:results} is computed from the classically simulated state vector." |
| "The gap is really small in the collocation case." | "At $n = 7$ the collocation composed $H$ has relative gap $\sim 10^{-15}$ — below double-precision machine epsilon, so the ground state is not resolvable at all — against $\sim 10^{-6}$ for $H_{\mathrm{sys}}$." |
| "This gives an exponential speed-up." | "The per-query encoding cost falls from $\Theta(N^2)$ to $O(n^2)$ gates. The end-to-end complexity does not become poly-logarithmic: $\alpha_H \ge \|H_{\mathrm{sys}}\| = \Theta(N^2)$ against $\Delta = \Theta(1)$ imposes an $\tilde\Theta(N^2)$ query floor on any block encoding of this $H$, which the descriptor construction meets." |
| "The results were verified." | "Atoms are state-vector-verified against reference matrices to $10^{-9}$–$10^{-11}$ column-by-column; the composition recipe is verified to $<10^{-10}$. The composed $H$ is not verified end-to-end — at 22+ qubits a dense simulation is infeasible — so correctness is established compositionally." |

---

*Companion documents: `STRUCTURE_AND_RUBRIC.md` (section tree, deliverables, marker
checklists), `../CLAUDE.md` (interactive review protocol).*
