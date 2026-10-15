# Mock examination: external examiner's report

**Thesis:** *Residual Hamiltonians for Quantum Differential-Equation Solvers: Descriptor Form, Conditioning and Verified State Preparation* (build of 2026-10-15, `build/main.pdf`, 144 pp; body pp. 1–59).
**Examiner stance:** a PRA referee who is also marking against the UWA *Master of Physics Thesis Mark Sheet* (Modelling scale). Only substance, structure, evidence and claims are judged. Prose and register were ignored throughout, as instructed.
**Sources read:** `ThesisPlanning.md` v3.14, `thesis_guides/STRUCTURE_AND_RUBRIC.md`, `../Theses-AssessmentRubric.pdf` (the mark sheet), `../marking_guide.pdf` (the guidelines), every chapter and appendix (in the PDF for figures, tables and resolved numbers, and in `.tex` for line anchors).

Line anchors are `file:line` in the `.tex` sources. Each paragraph is one source line, so an anchor points to the paragraph.

---

## 0. Formal requirements (checked before marking)

| Requirement (guidelines, Part A/B) | Status | Consequence |
|---|---|---|
| Body ≤ 60 pp, 12 pt, margins | Body runs pp. 1–59. Within the cap with one page spare | none |
| **One-page Summary of Student Achievement, first person** | **Page iv is blank.** `1_header/4_StudentAchievement.tex:1-18` contains only comments | "Reports will not be accepted or will attract a marks penalty for… failing to include" it. **This is the single largest mark risk in the document.** |
| Research proposal as appendix, deviations explained | Present (App. K, Table K.1; also `1_introduction.tex:183`) | satisfied, and well done |
| Declaration, supervisor endorsement | Present (supervisor signature to be confirmed) | check before submission |
| Help received acknowledged | Acknowledgements name the supervisor and Pawsey. The scaffold comment flags a possible AI-assistance declaration (`4_StudentAchievement.tex:16-17`) | check School policy |

**Page shares, by chapter start pages.** Intro, literature and Ch. 3 take ≈14 pp. Formulation (Chs 4–7) takes ≈27 pp (46%). Results and discussion (Chs 8–9) take ≈14.5 pp (25%), and the conclusions ≈2.3 pp. The guidelines ask for "the bulk of the report dealing with results and discussion of them and their significance". This thesis does the opposite. No cut is needed for the 60-page cap. The imbalance itself is a structural point a marker may raise under Results & Discussion (see §1.3).

---

## 1. Score estimate by criterion

| Criterion | Max | Estimate | Band |
|---|---:|---:|---|
| Introduction & Literature Review | 20 | **17.5** | 3 (15.0–17.9), at its top edge |
| Project Body – Model Formulation | 30 | **25.5** | 3 (22–26.9) |
| Project Body – Results & Discussion | 30 | **25.5** | 3 (22–26.9) |
| Conclusions & Further Investigation | 10 | **9.0** | 4 (9.0+), at its floor |
| Style & Presentation (non-prose items only) | 10 | **7.0** | 2 (6.0–7.9) |
| **Written thesis** | **100** | **≈ 84.5** | |

The Summary of Student Achievement penalty is not included in the total. A blank page there could make the thesis unacceptable or reduce the total by an unknown amount.

After the "fix before submission" items of §2, my estimate rises to about 18 / 27 / 26.5 / 9.2 / 8.5, which is **≈ 89**. The ceiling above that is set by items that need new results (§2, items 2 and 5).

### 1.1 Introduction & Literature Review: 17.5 / 20 (band 3, at the border of band 4)

Band 4 asks for a "comprehensive, superior understanding of the historical background and state of the art, *with excellent connection of the current field to the project*". Above that, the mark sheet says "a critical assessment of the strengths and weaknesses of the material reviewed is required for a high distinction".

The critical-assessment gate is clearly met. §2.2.5 (`2_literature.tex:108`) and Table 2.1 judge each route by what it assumes, which ratio it pays, what it returns and where it fails, with a *this work* row. Chapter 3's §3.5 (`3_pihm.tex:211-219`) judges Wu et al. under separate headings: strengths, cost, evidence, scope and open problems. It turns the paper's own open problems into Q(i)–(iii), the kind of "relate this to the project and its goals" that band 3 rewards and band 4 asks to be excellent. The historical lines are present: HHL → Berry → Childs–Liu → Costa; Leyton–Osborne → Carleman → Liu → Krovi; tau/collocation/Galerkin → Olver–Townsend → FOSLS.

Two things keep this short of 18:

- **The connection to the field is qualitative exactly where a marker will want it quantitative.** The thesis eventually says that the descriptor's Θ̃(N) is "the conditioning that the linear-systems solvers for ordinary equations also pay" (`9_discussion.tex:70`). That makes the headline parity with the established quantum ODE route, not an advance on it. Yet Table 2.1 gives that route no cost on the same Chebyshev discretisation, and the literature review never says so.
- **The ground-state-preparation history is thin.** Only Lin–Tong, the adiabatic line and Somma–Boixo appear. There is no Poulin–Wocjan or Ge–Tura–Cirac, and no phase-estimation-based preparation, although the whole method is a ground-state route.

**Single change most likely to raise it a band:** add to §2.2.5 / Table 2.1 one quantitative sentence or row. It should give the query count of the linear-systems route (Childs–Liu with Costa et al.'s O(κ log 1/ε)) on a first-order Chebyshev discretisation, and say plainly that the descriptor brings the physics-informed route to parity with it, not beyond. This is what turns "good attempt to relate" into "excellent connection". It also pre-empts the most damaging hostile question (Q8).

### 1.2 Model Formulation: 25.5 / 30 (band 3)

The mark sheet requires the formulation to be "described in sufficient detail to permit readers to create equivalent models", including "a description of any software tools used and/or created; a description and/or diagram of the model configuration; descriptions of the model input options selected". Band 4 is "superlative model … warranting publication". Band 3 is "good model capable of yielding valid results but the description lacking in some respect e.g. minor omissions in description, poor design of numerical experiment".

On the model itself this is band-4 work:

- Definition 2 (the standard form) and Definition 3 (the descriptor block).
- Theorem 1 (kernel equivalence), Theorem 2 (flat gap on regular problems, proved in App. D.5), Propositions 1–3 (exact encodings with ancilla and α), Proposition 5 (the stacked reflection) and Proposition 14 (the floor for every encoding).
- A configuration diagram (Fig. 7.1) and an input-option table (Tables H.3–H.4).
- An explicit design of the numerical experiment, including a fairness declaration that admits the as-built comparison favours the descriptor (`7_pipeline.tex:277`).

The "poor design of numerical experiment" failure is avoided.

It stays in band 3 for two reasons:

1. **The software requirement is named on the mark sheet and is not met.** §7.8 is one paragraph (`7_pipeline.tex:281-288`). It points to Appendix J for "architecture, records and commands", and Appendix J is six empty headings (`J_software.tex:26-72`). No repository URL, tag or commit is given anywhere, so the claim that "every number and figure is regenerated from the archived records by one command" cannot be checked. This is an "omission in description", and it is the one a marker is told to look for.
2. **A referee would press on preconditioning, and the formulation leaves an open flank there** (§2, item 2). The thesis states that Olver–Townsend's operator "is bounded after a diagonal preconditioner" (`2_literature.tex:169`). It then dismisses per-amplitude equilibration as needing Θ(dim w) gates (`5_descriptor.tex:169`), which holds for an unstructured diagonal but not for a structured one such as diag(1/(p+1)). That leaves the obvious preconditioned baselines unexamined.

**Single change most likely to raise it a band:** write Appendix J as the one page the plan specifies. It should give the repository URL with tag `results-v1` and its commit hash (a DOI if possible), what the repository holds, the regeneration command and the environment, with §7.8 citing it. This is cheap and directly answers a named rubric line. Item 2's text fix is the second lever.

### 1.3 Results & Discussion: 25.5 / 30 (band 3)

The mark sheet asks that results be "presented in a way that is easy to understand, without reference to any other documents", with discussion showing "your understanding of the meaning of your findings and the consequences of them for the field". Band 4 is "complete, clearly presented results, with detailed discussion showing insight into the significance of the work or warranting publication". Band 3 is "clear description of the results with discussion of most of the implications".

Strong points:

- Table 8.1 and Fig. 8.1 put the encoder's cost and the Hamiltonian's cost on one plot. This is the single most persuasive exhibit in the thesis.
- The reversals are reported as findings (Fig. 8.2; `8_results.tex:182`).
- The negatives are numbered (§8.6), and §9.1's mechanism links Theorem 2 to FOSLS coercivity.
- §9.2 states end-to-end complexity without over-claiming, Table 9.1 is a practitioner's map, and §9.5 lists limitations in the author's own voice.

This is insight, and much of it is publishable.

What keeps it in band 3:

- **The cost comparison is computed more than measured, and the thesis does not say so plainly.** Every standard-form degree beyond n = 3 on R2a is a resource estimate (Table H.5: the standard form is emulated only to n = 3 on R2a, and never on R2b or R2c). The degree is a deterministic function of (α_R, σ₀, σ₁, ε) (Eq. 7.6). So "the measured exponents are consistent with Θ̃(N^{2k})" restates the norm and gap computations. The growth exponents are two-point slopes (n = 7 → 8 on one axis, 4 → 5 per axis; `8_results.tex:143,159`), even though Fig. 8.1 shows the full range n = 2–8. "Complete" is the band-4 word this misses.
- **The significance verdict rests on the least-settled data.** "An advantage could appear only on many axes … the thesis leaves that open" (`9_discussion.tex:74`) is built on two resolutions per axis.
- **Results and discussion are 25% of the body**, against the guidelines' "bulk".

**Single change most likely to raise it a band:** open §8.2 by saying what the experiment actually establishes. Norms, gaps and α of the built circuits are exact computations. The degree then follows from Eq. (7.6), and the measurement is that 321 trusted T2 preparations reach ε at that predicted degree (`8_results.tex:93`). Then replace the two-point slopes in Tables 8.2 and H.7 by least-squares exponents over every trusted resolution, each with its spread. This needs an exporter key over existing records, not new runs.

### 1.4 Conclusions & Further Investigation: 9.0 / 10 (band 4, floor)

Band 4 asks for "detailed, comprehensive and insightful conclusions and significant suggestions for further investigation". Conclusions must "relate back to the original goal of the report".

Chapter 10 returns to the three questions in order, quotes the decisive numbers with their tiers, and states the price as well as the gain. Its further work grows out of the two limits that bound the result: the gap on several axes and the borrowed spectral edge. Each item is phrased as a concrete, cheap test: weighted datum rows at 3–5 qubits per axis, the ultraspherical reduction on one problem per class, a quantitative gap bound checked against R1/R2, order-to-order comparison as a divergence test, and complex loaders with R7 as the first comparison (`10_conclusions.tex:51-55`). The closing lesson (where a ground-state solver's cost is set) is a genuine insight. The proposal's unmet aims are carried into further work.

**Single change most likely to raise it:** put the preconditioned ultraspherical operator (item 2) at the head of the further-work list. It is the test that could overturn the headline. Give it a decision criterion: "if σ_max/σ₁ of the preconditioned residual stays bounded on R2a, the descriptor is dominated on regular problems". That makes the suggestions more significant and protects the conclusions from an examiner who raises it first.

### 1.5 Style & Presentation: 7.0 / 10 (band 2), non-prose items only

The mark sheet covers "grammar and spelling, presentation of figures and tables and general expression and layout"; "flawless" is 10, "few insignificant errors" 8.0–9.9, "significant errors" 6.0–7.9. Grammar, spelling and expression were **not assessed**, at your instruction.

The figures and tables are of journal quality, with self-contained, claim-first captions, and no placeholder boxes survive in the build. The layout, however, carries errors a marker will count as significant:

- a blank required page (iv);
- an appendix with headings and no text (J);
- five further headings with nothing under them: H.1 and H.2 (`H_catalogue.tex:19,54`), I.1 and I.2 (`I_reproduction.tex:26,45`) and I.6.3 (`I_reproduction.tex:328`).

I.1 matters most: it is meant to state the paper-faithful conventions on which §4.4's validation paragraph rests.

**Single change most likely to raise it a band:** fill or delete every empty heading (J, I.1, I.2, I.6.3, H.1, H.2) and write page iv. With those done, and assuming the prose sweep you are doing anyway, 8.5 is realistic.

---

## 2. The ten weaknesses most likely to cost marks

Ranked by marks at stake. "Cheapest fix" is achievable in under two hours unless marked **not before submission**.

### 1. The Summary of Student Achievement is blank

- **Where:** `1_header/4_StudentAchievement.tex:1-18` (comments only); PDF page iv.
- **Why an examiner objects:** it is a formal requirement with an explicit penalty or refusal clause. It is also where a marker learns what the student, rather than the literature, built: the standard form, the structured encoding, the descriptor, `pihm`, the verification tiers and the Setonix production.
- **Cheapest fix (≈ 40 min):** one page, first person, following the scaffold's own list. Name the help received, and check whether School policy requires declaring AI assistance.

### 2. Diagonal preconditioning is dismissed on a cost argument that does not hold for structured diagonals, and the preconditioned baselines are never examined

- **Where:** `2_literature.tex:169` states that Olver–Townsend's operator has "condition number [that] grows linearly … and is bounded after a diagonal preconditioner", and that "block rescaling takes the place of the preconditioner". `5_descriptor.tex:169` says a per-amplitude equilibration "would need a diagonal block encoding of its own, at Θ(dim w) gates". `9_discussion.tex:173` (Limitations), `A_chebyshev.tex:207` and `2_literature.tex:171` say the full ultraspherical reduction was "neither built nor compared".
- **Why a referee objects:** the descriptor's flat gap with ‖H_desc‖ = Θ(N²) gives an effective condition number Θ(N). That is the *unpreconditioned* ultraspherical conditioning. The thesis itself states that a diagonal preconditioner bounds the antecedent's condition number. If that bound carries over to the least-squares residual with constraint rows, the filter degree would be O(log 1/ε) independent of N, and the antecedent would dominate the headline. That is a plausible risk, not a demonstrated fact. The dismissal of per-amplitude weights is correct only for an *unstructured* diagonal. A structured diagonal such as diag(1/(p+1)) or diag(p⁻²) can be block-encoded with poly(n) reversible arithmetic. The same question applies to the baseline: the standard form was never given a column scaling (G·diag(1/p) has entries of order one and norm Θ(N)). So the fairness declaration covers encodings but not preconditioning. A PRA referee would ask both questions in the first report, and a marker who knows spectral methods will too.
- **Cheapest fix (≈ 1.5 h, text only):**
  - Narrow the claim at `5_descriptor.tex:169` to unstructured diagonals.
  - In §9.5, state what Olver–Townsend's bound would predict here and what blocks the transfer: the problem is least squares rather than square, the constraint rows are scale-free, the ground state would hold preconditioned coefficients (which changes the overlap and the readout), the conversions need an encoding, and the gap is unknown.
  - Say that a preconditioned standard form is not evaluated either.
  - Make it the first further-work item (§1.4).
- **The measurement** (σ_max/σ₁ of the preconditioned ultraspherical residual and of the column-scaled standard residual on R2a, n = 3–10) is **not before submission**, unless it can be added to `pihm` as a classical build stage with its own key.

### 3. Appendix J is empty, so the software requirement and the reproducibility claim have no support

- **Where:** `J_software.tex:26-72` (six headings, no text). Cited by `7_pipeline.tex:288` and `8_results.tex:74`.
- **Why an examiner objects:** "a description of any software tools used and/or created" is a named Model Formulation requirement. §7.8's claim that every number is regenerated by one command is unverifiable without a repository reference. A PRA referee would require a code-availability statement.
- **Cheapest fix (≈ 1 h):** the one page the plan already specifies. Give the URL, tag `results-v1` with its commit hash (and a Zenodo DOI if you can mint one today), one sentence per heading and the regeneration command.

### 4. The cost results are computed rather than measured, and the exponents are two-point slopes

- **Where:** `8_results.tex:143` and Table 8.2 (`8_results.tex:157-159`); Table H.7; Table H.5 (`H_catalogue.tex:141`), which shows the standard form emulated only to n = 3 on R2a, never on R2b or R2c, and to n ≤ 5 elsewhere.
- **Why an examiner objects:** every standard-form degree in the headline comparison (1.2 × 10¹⁰, 1.5 × 10⁹) is Eq. (7.6) applied to an exact spectrum and an α. That is legitimate and exact, but it is not an observation of the algorithm. Reporting the exponents as "measured", from two points, when Fig. 8.1 has seven, invites the charge that the Results chapter restates the formulation.
- **Cheapest fix:**
  - (a) Text, 20 min: one paragraph at the head of §8.2 separating what is exact computation (norms, gaps, α of built circuits), what is derived (degrees from Eq. 7.6) and what is tested (T2 preparations reach ε at the derived degree in 321 trusted cases, and T1 = T2 where both run).
  - (b) Fitted exponents over all trusted resolutions, with spread, in Tables 8.2 and H.7. This is an exporter-derived key from existing records, ≈ 1–2 h, and needs no new runs.

### 5. The spectral edge, the overlap and some constraint data are taken from the answer, and the robustness evidence is narrow

- **Where:** `7_pipeline.tex:207` (edge from the reference); `7_pipeline.tex:222` (γ from the reference); `4_standard.tex:214` and `B_standard_form.tex:171` (constraint points from the reference solution; answer-free point-datum rows exist but "none of our runs uses them"); `B_standard_form.tex:126` (heat data at t = −1). The robustness evidence is the edge study at `H_catalogue.tex:288`; the limitations paragraph is `9_discussion.tex:171`.
- **Why an examiner objects:** as costed, the algorithm needs a classical solution before it starts. The only robustness evidence is one *imaginary-time* study in the *standard* form on R2a at *n = 3*. It tests underestimates only. It covers neither the minimax filter nor the descriptor, and says nothing about the dangerous direction, an overestimated gap, which silently misses ε.
- **Cheapest fix (≈ 45 min, text):**
  - State the asymmetric risk.
  - Show that the degree laws survive any lower bound Δ_lb = cΔ with c fixed in N. This follows directly from Eq. (7.6).
  - Note that Theorem 2 supplies the order but not the constant, and cite ground-energy estimation (Lin–Tong) as the standard way to obtain a bound at polylog overhead.
  - Argue from Corollary 1 and Proposition 14 that the choice of constraint row moves neither the norm's leading term nor the gap's upper bound, so the comparison does not depend on the answer-derived points.
- **Not before submission:** a minimax, descriptor edge-underestimate study, and runs with point-datum rows in place of the exact constraint points.

### 6. The positioning against the established quantum ODE route is qualitative, which caps the "consequences for the field"

- **Where:** Table 2.1 (`2_literature.tex:119`) and §2.2.5 (`2_literature.tex:108`); `9_discussion.tex:70`.
- **Why an examiner objects:** the mark sheet asks for the "consequences … for the field" (R&D) and an "excellent connection of the current field to the project" (Intro & Lit). The thesis's own statement makes the descriptor's Θ̃(N) on a regular problem *parity* with first-order linear-systems solvers, but only in passing. An examiner reading Table 2.1 cannot tell whether the physics-informed route, after reformulation, is better than, equal to or worse than Childs–Liu with Costa et al. on the same discretisation.
- **Cheapest fix (≈ 1 h):** one sentence in §2.2.5, one column entry in Table 2.1 and two sentences in §9.2. Give the linear-systems query count on a first-order Chebyshev discretisation, state that the descriptor reaches it, and say what the ground-state route offers in exchange (no inverse, a residual whose kernel is the solution, the field at every x) and does not (still N samples to read the field).

### 7. The two-axis verdict rests on two resolutions

- **Where:** `8_results.tex:182` (the heat reversal at n = 4 and 5 per axis); Table 8.2 rows R5a/R5b; R5c untrusted below n = 5 (Table H.7 †); the competitiveness verdict at `9_discussion.tex:74`.
- **Why an examiner objects:** the thesis's most consequential sentence is that any advantage must come on several axes, where the gap falls. It is built on slopes the thesis calls "the least settled", and the heat reversal flips between n = 4 and 5. An examiner will accept the negative but will want its uncertainty carried into §9.2 and Chapter 10, not only into §9.5.
- **Cheapest fix (≈ 30 min):**
  - Quote the R5a gap and degree over n = 3, 4, 5 (trusted from n = 3), the three points already in Fig. 8.3.
  - Attach "between n = 4 and 5 per axis" to the competitiveness sentence itself.
  - In Chapter 10, phrase the two-axis outcome as an open measurement, not a settled fall.
- **Not before submission:** larger two-axis resolutions.

### 8. Empty appendix sections under headings the body cites

- **Where:** `I_reproduction.tex:26` (I.1, the paper-faithful conventions), `:45` (I.2) and `:328` (I.6.3); `H_catalogue.tex:19,54` (H.1, H.2).
- **Why an examiner objects:** §4.4's validation claim ("reproduces the scale factors of all eleven ODE panels within one unit of the last printed digit") cannot be audited without I.1's statement of what the paper-faithful variant restores. Empty headings also count against Style.
- **Cheapest fix (≈ 1–1.5 h):** half a page for I.1 (the rounded points, the Maclaurin sources, the hand-picked invariant sets, the unnormalised feature map and the printed n). One sentence each for I.2, I.6.3, H.1 and H.2 pointing to their tables, or delete those headings.

### 9. The increment list counts results a referee will call immediate

- **Where:** `2_literature.tex:187` ("What we add"); `1_introduction.tex:177`; `8_results.tex:305` (finding 5).
- **Why an examiner objects:** three of the listed results are close to immediate.
  - Theorem 1 follows in two lines from B̃ being invertible.
  - Proposition 4 (a filter projects onto a degenerate kernel) is immediate.
  - "A trusted kernel does not certify a converged lift" is predicted in §6.5 from IVP uniqueness (`6_extensions.tex:132`).

  Listing them beside Theorem 2 and the gap-erosion mechanism dilutes the claim. It also hands the examiner the "this is just ultraspherical + FOSLS" line (Q1).
- **Cheapest fix (≈ 30 min):** lead the increment with what is new: Theorem 2 in the block-encoded Chebyshev setting, the gap-erosion mechanism with its a priori cure and its limits, the encoder/Hamiltonian separation with the floor for every encoding, and the measured end-to-end costs. Present Theorem 1 as the enabling lemma, Proposition 4 as a correction of the paper's framing, and the lift result as a predicted consequence confirmed in practice, together with its proposed diagnostic.

### 10. Tier wording conflates estimate with preparation, and "Navier–Stokes" is stated without its regime

- **Where:** "prepare … for two-dimensional incompressible Navier–Stokes flow on up to 48 Fourier modes by exact emulation and resource estimate" at `5_abstract.tex:23`, `1_introduction.tex:177` and `10_conclusions.tex:46`; similar wording at `9_discussion.tex:169`. The flow's parameters are at `6_extensions.tex:169-178` (ν = 1, a/ν ≤ 30, 12–48 modes, T = 1).
- **Why an examiner objects:** by the thesis's own definition a resource estimate "prepares nothing" (`7_pipeline.tex:279`). A fluids-literate examiner will read "Navier–Stokes" as more than a strongly viscous flow with Reynolds number of order 10, resolved on 12 modes, whose Galerkin truncation alone errs by 0.2 at a/ν = 30 (`8_results.tex:277`).
- **Cheapest fix (≈ 20 min):** "prepared by exact emulation on 12–48 modes and costed by resource estimate". Add one clause stating the Reynolds number and calling the flow a low-Reynolds demonstration of the pipeline, not a fluid simulation.

---

## 3. Fifteen questions an examiner is likely to ask

"Adequate" means a marker reading only the thesis would accept the answer. A two-sentence model answer is given where it is not.

**Q1 (hostile). Is the descriptor reformulation just the ultraspherical method plus FOSLS?**
*Where answered:* `2_literature.tex:187`; `5_descriptor.tex:57`; App. A.5 (`A_chebyshev.tex`, the exact correspondence D̃_raw = 2D₀, B̃_raw = 2S₀); `9_discussion.tex:40`.
*Adequate?* **Partly.** The credit is exemplary and precise. The *increment* is diluted by listing the kernel-equivalence proof (item 9).
*Model answer:* "Algebraically yes, and the thesis says so. B̃ and D̃ are twice Olver–Townsend's S₀ and D₀, and carrying derivatives as unknowns is FOSLS. What is new is what happens when that residual is block-encoded and *filtered* rather than solved. The norm falls to Θ(N²), but the conditioning reappears in the gap, which Theorem 2 controls exactly on regular problems and which fails on singular and two-axis problems. That failure mode, its a priori cure and the measured end-to-end costs are not in either antecedent."

**Q2 (hostile). Does anything here beat a classical solver?**
*Where:* `1_introduction.tex:181`; `2_literature.tex:108`; `9_discussion.tex:74`; `10_conclusions.tex:51`.
*Adequate?* **Yes.** The thesis claims no advantage and gives the reason: O(N) classical work on one axis, and N samples to read the field. Expect the follow-up "then why is this worth a thesis?"; the closing lesson at `10_conclusions.tex` (last paragraph) answers it.

**Q3 (hostile). Why should we trust exact emulation (T2)?**
*Where:* `7_pipeline.tex:248`; `8_results.tex:91`; App. F.1–F.2, F.7; App. G.1.
*Adequate?* **Mostly.** The argument is sound: Proposition 5, qubitisation and GQSP make the post-selected output Σ q_k T_k(H′)ψ, which depends on the circuit only through ΠVΠ = H′. It is backed by 50/50 minimax T1 = T2 agreements within 10⁻¹⁰. The gap is scope. For every Navier–Stokes circuit (≥ 27 qubits) and the two-axis descriptor circuits, ΠVΠ = H′ is established only term by term (IR) plus a structural argument about the compiler, not on the gates.
*Model answer for the gap:* "Where the reflection is verified (exactly to 25 qubits, by probe to 24), T2 *is* the circuit's output up to rounding. Beyond that, T2 is the output of the circuit the compiler intends, verified term by term, so the Navier–Stokes results are exact emulations of an unverified-at-size circuit, and I report them as such."

**Q4 (hostile). What happens without the known spectral edge?**
*Where:* `7_pipeline.tex:207`; `8_results.tex:95`; `H_catalogue.tex:288`; `9_discussion.tex:171`; `10_conclusions.tex:53`.
*Adequate?* **No.** The evidence is one imaginary-time, standard-form, n = 3 study of underestimates.
*Model answer:* "The degree needs only a lower bound Δ_lb ≤ Δ. It grows as √(Δ/Δ_lb), so every scaling law survives a bound of the right order in N, which Theorem 2 guarantees on regular problems without its constant. An *over*estimate is the real danger, because it silently misses ε. In practice the bound would come from ground-energy estimation (Lin–Tong) at polylogarithmic overhead, which I have not costed."

**Q5 (hostile). Olver and Townsend show the ultraspherical operator is well conditioned after a diagonal preconditioner. Why isn't the preconditioned operator's degree N-independent, and why didn't you precondition the standard form?**
*Where:* `2_literature.tex:169,171`; `5_descriptor.tex:169`; `A_chebyshev.tex:207`; `9_discussion.tex:173`.
*Adequate?* **No.** See item 2. The Θ(dim w) argument does not cover structured diagonals.
*Model answer:* "That is the right question and I have not settled it. A structured diagonal such as diag(1/(p+1)) is cheap to encode. What is unknown is whether bounded conditioning survives the least-squares form with scale-free constraint rows, and what the change of variables does to the overlap and the readout. Computing σ_max/σ₁ for the preconditioned residual on R2a is the first experiment I would run, and if it stays bounded the descriptor is dominated on regular problems."

**Q6. ‖G‖ ∼ N² is textbook. What is new in your answer to Q(i)?**
*Where:* `4_standard.tex:312-330` (§4.5); `4_standard.tex:440-447` (Proposition 14 and Eq. 4.8); App. C.4–C.6.
*Adequate?* **Yes.** The new parts are three: the N³ looseness of the paper's prefactor, the exact encoding at 2.12‖G‖, and a floor that holds *for every encoding*, at an ideal bound containing no circuit. Theorem 3's Bessel-zero limit is a nice touch.

**Q7. Your exponents are two-point slopes. How robust are they?**
*Where:* `8_results.tex:143,159`; `9_discussion.tex:169`.
*Adequate?* **Partly.** The thesis says "consistent with the laws, not fits of them", which is honest but thin when seven resolutions exist.
*Model answer:* "Fitted over n = 3–8, the one-axis exponents are … with spread … (quote the derived key). The two-axis ones rest on n = 4–5 and I treat them as indicative."

**Q8 (hostile). Why benchmark against Wu et al. at all, rather than against the established linear-systems ODE solvers on the same discretisation?**
*Where:* `9_discussion.tex:70`; Table 2.1.
*Adequate?* **No** (item 6).
*Model answer:* "Because the question is what the ground-state route costs and where. On a regular one-axis problem the descriptor brings it to the Θ̃(N) query count that a first-order linear-systems discretisation pays, parity rather than advantage, and it avoids an inverse at the price of an answer-independent initial state with overlap γ. The comparison with Wu et al. isolates the cost of eliminating derivatives, which the linear-systems solvers never pay because they reduce order first."

**Q9. The exact constraint points and the heat data come from the reference solution. Isn't the benchmark answer-dependent?**
*Where:* `4_standard.tex:214`; `B_standard_form.tex:126,171`; `7_pipeline.tex:93`; `9_discussion.tex:171`.
*Adequate?* **Partly.** It is acknowledged, but not shown to be irrelevant to the comparison.
*Model answer:* "The set-up is answer-dependent, and a new problem must supply its data. The cost comparison is not, because the equation block fixes the norm's leading term (Corollary 1) and Proposition 14 bounds the gap for any rows. An answer-free point-datum row (Definition 2) would change the accuracy floor, not the scaling."

**Q10. Theorem 2 gives no constant, and on R2c the unscaled gap is 7.5 × 10⁻⁶. Is Θ(1) meaningful?**
*Where:* `5_descriptor.tex:151` and the proof at `D_descriptor.tex:202`; R2c at `8_results.tex:222`; `9_discussion.tex:169` (the stiffness dependence measured on R2c alone).
*Adequate?* **Mostly.** The rescaled gap of 0.715 answers the practical concern. The compactness proof is honest that it gives no bound.
*Model answer to the follow-up:* "The constant depends on the equation's own scale, and the a priori ζ removes that dependence on every regular problem run. A quantitative constant for constant coefficients is the stated next step, and its stiffness dependence was measured on one problem only."

**Q11. "A trusted kernel does not certify a converged lift": isn't that obvious, since a linear IVP always has a unique solution?**
*Where:* `6_extensions.tex:132`; `8_results.tex:244,305`.
*Adequate?* **Yes, if framed as predicted.** §6.5 already predicts it. The danger is §8.6 and the abstract presenting it as a discovery (item 9).
*Model answer:* "Yes, it follows from uniqueness, and §6.5 predicts it. The finding is its practical consequence: the residual offers no divergence diagnostic, so every Carleman preparation needs an independent convergence test, and I propose one that needs no reference."

**Q12. Is 12-mode, ν = 1 flow "Navier–Stokes" in any meaningful sense? What is the Reynolds number?**
*Where:* `6_extensions.tex:169-178`; `8_results.tex:277`.
*Adequate?* **No.** The Reynolds number is never stated (item 10).
*Model answer:* "With ν = 1 on a 2π box and ‖w₀‖ ≤ 30 the flow is strongly viscous, Reynolds number of order 10, and the 12-mode truncation alone errs by up to 0.2. It demonstrates that the lift, the ratio rows and the time axis run end to end on an incompressible flow. It is not a fluid simulation of any engineering interest."

**Q13. Your gate counts are two-qubit gates after transpiling to {CX, U}. A fault-tolerant cost is set by non-Clifford gates. What do 1.3 × 10⁹ CX gates mean?**
*Where:* `9_discussion.tex:132,147`; `7_pipeline.tex:279`.
*Adequate?* **Yes as a caveat.** The thesis says the counts omit rotation synthesis, the code overhead and depth.
*Model answer to a follow-up:* "The counts compare the two forms per query on a common basis. The fault-tolerant cost would multiply both by the rotation-synthesis overhead, and the ratio of the two forms' costs is dominated by the degree, which is basis-independent."

**Q14. Your proposal promised complex-valued nonlinear PDEs (NLS, CGL) by generalised QSVT. None was done. Why?**
*Where:* `1_introduction.tex:183`; App. K, Table K.1.
*Adequate?* **Yes.** The reasons are scientific: the cost had to be settled first, GQSP already lifts the parity and real-coefficient restrictions, H = R†R stays Hermitian, and Liu et al.'s guarantee excludes cubic, norm-conserving and amplifying equations. A marker will accept this.

**Q15. The field is decoded classically from amplitudes a quantum computer does not expose. Doesn't the readout cost (≈ N samples) erase every gain you report?**
*Where:* `2_literature.tex:236` (Readout); `7_pipeline.tex` §7.6; `9_discussion.tex:74`; `10_conclusions.tex:55`.
*Adequate?* **Yes.** It is acknowledged in four places, and the costs are explicitly stopped at the prepared state.
*Model answer to a follow-up:* "For the full field, yes. That is shared by every route in Table 2.1 and is why I compare formulations, not solvers. A linear functional or a point value costs O(1/δ) by amplitude estimation, and the interferometric readout, corrected for p_G < 1, is built and verified at small n."

*Reserve questions:*
- Why is the widest exact verification a reproduction record (R4d as printed) rather than a problem as run? (`8_results.tex:91`; adequate as disclosed.)
- How was ζ's constant chosen, and is the check in-sample? (`5_descriptor.tex:176`; adequate, since in-sample is disclosed and the window of a factor 2 is shown.)
- Why does R3 reverse at the ideal bound? (`8_results.tex:182`, `9_discussion.tex` §9.3; adequate, and a good answer.)

---

## 4. Where the thesis is strongest (do not weaken in the rewrite)

1. **The encoder/Hamiltonian separation.** It runs from Chapter 4's opening through the ideal-encoding bound (Proposition 32), Table 8.1 and Fig. 8.1: two costs on one plot, with the ideal bound containing no circuit. This is the most persuasive argument in the thesis. Keep its three columns and the sentence that the as-built comparison is *not* conservative (`7_pipeline.tex:277`).
2. **Reversals and negatives reported as findings.** R3 at the ideal bound, the heat equation at n = 4, the two-axis gap fall, the diverging lifts and the QITE T1 misses not re-judged (App. I.9). This is what the mark sheet's negative-results clause protects. Do not soften "Negative:" in §8.6.
3. **Scope discipline.** `def:regular` and every degree, gap and α claim carry their class (Table 5.1, Table 9.1). "Neither form is polylogarithmic" is stated where the gains are. The Lin–Tong hedge on the floor is kept. A referee will find no unscoped headline. Keep the class glosses in the Abstract, §1 and §10.
4. **Antecedent credit at the level of matrix entries** (App. A.5) and the concurrent Paine work handled in both §2.2.4 and §3.5. This is the best defence against Q1. Keep it exact.
5. **Chapter 3 as prior art, judged**, with Strengths / Weaknesses (cost, evidence, scope) / Open problems → Q(i)–(iii). This carries the Intro & Lit high-distinction gate.
6. **Theorem 2 with an honest proof** (compactness, no constant claimed), and the mechanism of §5.3 tied to FOSLS coercivity in §9.1. This is the intellectual centre of the discussion.
7. **The verification architecture.** Targets are assembled independently of the compiler, there are three operator modes with stated tolerances, T1 = T2 holds within 10⁻¹⁰ on every minimax record, the acceptance bars are never adjusted, and the error budget is shown to be conservative (Fig. G.2). Keep the "beyond the simulation budget, not beyond the method" distinction.
8. **The validation against the printed paper** (Table I.1, the Fig. 5 triage in Table I.2). It shows that the baseline is Wu et al.'s method and that the departures are justified by error floors.
9. **The proposal-deviation account** (§1, Table K.1). The reasons are scientific, not circumstantial.
10. **Chapter 10's further work**, each item a concrete, cheap and falsifiable test grown from a stated limit.
