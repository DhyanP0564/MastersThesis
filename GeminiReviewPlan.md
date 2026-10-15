# Gemini Review: Verification and Fix Plan

Source: Gemini 4's referee report on the thesis (`Review.md`, supplied 2026-10-16).
Verified 2026-10-16 against the `.tex` sources, `build/main.pdf` (15 Oct), `pihm` (code, `docs/`, `results/`, `0_results/generated/numbers.tex`) and the thesis's own appendices.

Rule followed: Gemini's **style** points are accepted as given. Its **factual and mathematical** claims were each checked, and only what survived goes into the prompts. Part B lists what must **not** be imported.

---

## Part A: Verdicts

| # | Gemini's claim (short) | Verdict | Evidence | Action |
|---|---|---|---|---|
| 1 | §2.4's square root is the edge Chebyshev mechanism, not frustration-freeness; it degrades when σ₀ is large | **Partly correct** | `2_literature.tex:270` attributes the square root to frustration-free amplification, though the paragraph before it (l. 263) already derives it from the edge. Gemini's degradation formula for θ₀ is **wrong**: by `eq:minimax-filter` and App. F (`F_pipeline.tex:100-104`), −w(x₀) = 1 + 2(σ₁²−σ₀²)/(α_R²−σ₁²), so θ₀ ≈ 2√Δ/α_R whatever σ₀ is. A non-zero ground value costs only the factor P_d(x₀)² in p_G, which App. F (l. 122) and §7.4 already state | Prompt 2: reword one sentence |
| 2 | The full ultraspherical reduction is not compared; a "killer" justification is offered | **Premise correct, justification wrong** | The reduction is not compared (`5_descriptor.tex:55`, `A_chebyshev.tex:207`, `9_discussion.tex:52`). Gemini claims ‖D_{m−1}⋯D₀‖ = Θ(N^{2m}) and that a Θ(N^k) right preconditioner is needed; both are false. Olver–Townsend's D_λ is a scaled shift with entries ∝ index, so its norm is Θ(N) at every order, and the condition number grows linearly **without** a preconditioner (as `2_literature.tex:169` itself says). That implies the reduction would plausibly reach the descriptor's Θ̃(N) class on N unknowns, so §9.5's "nothing here predicts" contradicts §2.3 | Prompt 2 (§5.1 pointer) and Prompt 4 (§9.5 and Ch. 10 expectation, hedged) |
| 3 | The exact interior roots are answer-dependent; justify keeping Wu et al.'s invariant rows | **Correct, wrong scope** | Only **R4a–d and R6b** use computed roots (`pihm/docs/03_problems/04_r4.md`, `06_r6.md`), not "R2–R4". The justification already exists in App. B (`B_standard_form.tex:171`) but not in §4.3 (`4_standard.tex:191`) | Prompt 2: bring one sentence into §4.3 |
| 4 | On R3a the structured encoding pays ‖M_a‖‖G²‖ = Θ(N⁴) while ‖M_aG²‖ = Θ(N²); the ideal bound needs a fused encoding | **Correct core, overreach** | Matches `4_standard.tex:457` and `8_results.tex:182`. It is provable that any encoding built as a product with G² or as a combination of terms holding G² has α ≥ √2‖G²‖ = Θ(N⁴). "No modular circuit can reach the bound" is **not** proven | Prompt 2: one hedged sentence in §4.6 |
| 5a | The ζ rule switches discontinuously between classes; a nearly singular regular problem behaves as singular | **Correct, already measured** | App. D's dipping coefficient (`D_descriptor.tex:282`, `zeta-dip` keys): the rule's cost reaches 2.3× and 4.7× the grid's best at δ = 10⁻³. The body (§5.4) doesn't mention it | Prompt 1 |
| 5b | §5.4 doesn't explain why a simple zero needs ζ ∝ N | **Correct, derivation exists** | App. D (`D_descriptor.tex:247`): the concentrated states' quotient is O(N⁻⁴ζ^{2k}), so ζ ∝ N^{2/k} for a simple zero (N at k = 2) and N^{4/k} for a double zero (consistent with `5_descriptor.tex:187`). Gemini's own derivation is muddled; use App. D's | Prompt 1 |
| 5c | "A priori" is the wrong word for a calibrated rule | **Correct** (your decision: no term) | `5_descriptor.tex:171` names "The a priori rule"; App. D says the constants were set by a sweep. The term appears in ~10 places, plus CLAUDE.md and ThesisPlanning.md | Prompt 1 |
| 6 | The 2-D gap falls because datum-row (trace) energy is small against the interior H² seminorm; weight the rows | **Mechanism plausible; remedy already tested** | The thesis already gives this reading as an inference (`9_discussion.tex:6`). Gemini's exponents (Θ(N) against Θ(N⁴)) are a heuristic upper bound. Crucially, pihm's probe `tools/probes/p15_trace_weights.py` (`docs/14_descriptor_gap.md` §5.4) tried weights (m+1)^s: s = ½ was best, cutting the cost only 1.4–2.4× because ‖H‖ rose as fast as Δ ("not a cure"). The thesis still calls these weights the first remedy to test (§9.1, Ch. 10) | Prompt 0 (export the probe) and Prompt 4 (report as measured, recast the future work) |
| 7 | γ is never reported on R8–R10; the Carleman initial state is ambiguous | **Correct** | No `.tex` file quotes a Carleman γ² or p_G. Values exist: γ² is 0.78 on R8 (K=4), 0.56 on R9c (K=2), 0.23 on R9e (K=5, a/ν=10) and 0.46 on R10d-W8 (K=3); the T3 p_G on R10 is 0.46–0.66 across K = 2–4 and M = 12–48, falling mildly with both, with at most one amplification round. Code (`pihm/qsp/initial.py`, `Residual.field_blocks`): w₀/‖w₀‖ sits on the **degree-one (level-1) blocks only**; higher levels start at zero. The two sentences in §7.4 are consistent but read as ambiguous | Prompt 0 (range keys), Prompt 2 (§7.4 clarity), Prompt 3 (§8.4/§8.5 report) |
| 8 | No reason given for matchings over a sparse-access oracle | **Correct that none is given; proposed reason not the documented one** | The documented alternative was **Pauli words** (pihm decision 42: on R9, 4–16 matchings against 85–29,944 words, with α 2–3.4× smaller). Provable: greedy colouring gives α ≤ (2δ−1)‖Γ‖_max, within 2× of the sparse-access s‖Γ‖_max with s = δ | Prompt 2: one sentence |
| 9 | R2c's 0.656 (as built) against 0.975 (ideal) is an additive constant in α_R, not "still rising" | **Correct** (its constant is off) | Records (`results/p5_t3`): the gap is 0.7150 at n=7 and 0.7148 at n=8, so the slope is α_R's alone. α_R grows by exactly 80 = 2ζ per unit of N for n = 5–8 (ζ = 40), i.e. α_R ≈ c₀ + 2ζ(N−1) with c₀ ≈ 7.6×10³ (Gemini estimated 5.5×10³). ‖R‖ ≈ 2ζ(N−1) already at n=8 (20498 against 20400). The current clause (`8_results.tex:155`) is vague | Prompt 0 (split key), Prompt 3 |
| 10 | Ch. 10's first ~1.8 pp restate §§9.1–9.4; future work buried; split into 10.1/10.2 | **Correct** (style, accepted) | Paragraph by paragraph: Ch. 10 ¶1 ↔ §9.2 ¶2 and Ch. 9's closing; ¶2 ↔ §9.1; ¶3 ↔ §9.3; ¶4 ↔ §9.2 and §9.4 (the emulation lesson nearly verbatim); ¶5 ↔ §9.2 ¶1 and its last paragraph. This conflicts with ThesisPlanning v3.15 §5.10 ("no subsections, no run-in headings, no question numbers"), which must be updated | Prompt 5 |
| P1 | "have k−1" is missing "rank" (§4.3) | **False** | Source and PDF both read "have rank k − 1" | none |
| P2 | Ceiling bracket clipped (notation table; §5.2) | **Style, accepted** | Present, but cramped in the exponent (rendered p. 24) | Prompt 2 |
| P3 | §7.4 initial-state ambiguity | **Accepted** | = row 7 | Prompt 2 |
| P4 | "20 at n_t=4 and 12 at n_t=5" reads as degrees | **Style, accepted** | `8_results.tex:279` | Prompt 3 |
| P5 | Student signature missing | **False** | `Figs/SignatureDP.jpg` renders on p. i; its white box overlaps the rule slightly | optional: Prompt 3 note |
| – | §2.2 "slightly imprecise asymptotic comparisons with QLSS" | **Unspecified** | No claim given to check | none |

---

## Part B: Do not import

Any session working from this plan must **not** write these Gemini claims into the thesis:

1. That θ₀ (and so the degree) degrades toward (σ₁²−σ₀²)/(α_Rσ₀) when σ₀ is large. The degree is set by Δ alone; σ₀ costs success probability through P_d(x₀)².
2. That ‖D_{m−1}⋯D₀‖ = Θ(N^{2m}), or that the ultraspherical reduction needs an amplitude-distorting Θ(N^k) right preconditioner. Both are false.
3. That R2–R3 use answer-dependent interior points. Only R4a–d and R6b do.
4. That no modular circuit can reach the ideal bound on R3a. Only term-wise and product encodings built on G² are provably Θ(N⁴).
5. Gemini's own derivations of ζ ∝ N ("N⁻¹ in weighted L²", "recurrence controls f′ up to ‖D̃‖"). Use App. D's quotient O(N⁻⁴ζ^{2k}).
6. Gemini's 2-D exponents (trace Θ(N), interior Θ(N⁴)) stated as fact, and the claim that weighted datum rows are an untested remedy.
7. "Avoids coherent arithmetic" stated as the *reason* matchings were chosen. It may appear as a comparison; the documented comparison is against Pauli words.
8. Gemini's constant (≈5460) or "quadrature" for ‖R‖. Quote exported keys and the formula 2ζ(N−1) only.

---

## Part C: Decisions taken (2026-10-16)

- **Trace-weight probe:** export it into results-v1 keys and report it as a measured partial remedy; recast the future-work item.
- **Ultraspherical reduction:** state the hedged expectation from Olver–Townsend's bound; §5.1 points to App. A's reasons.
- **ζ rule:** use **no term** for it. Never "a priori", never "the calibrated rule". Say once (§5.4, with App. D) that its two constants were selected by calibration on the benchmark problems and then held fixed. Say in the right places that deriving ζ from the equation should be possible, and list that as further work. "A priori" stays for the filter's parameters (edge, α_R, ε), which are untouched.
- **Exporter:** new keys will be added (Prompt 0).
- **Ch. 10:** split into 10.1 Conclusions and 10.2 Future Work, as Gemini asks, with ThesisPlanning.md updated to match.

---

## Part D: Prompts

Run them in order, each in a fresh session. Prompt 0 is in the pihm repo; Prompts 1–5 are in this repo. After Prompts 1–5, run the exporter and the closing check (Prompt 6).

### Shared rules (every thesis prompt)

Paste-free: each prompt says "follow the Shared rules in `GeminiReviewPlan.md`". They are:

- You are drafting **at the user's request**. Every draft is a first pass for the user to rewrite. Follow `CLAUDE.md` (Standing Facts, evidence rule T-20, tiers), `thesis_guides/STYLE_GUIDE.md`, and the touched sections' entries in `ThesisPlanning.md` §5. Read `0_results/README.md` before quoting a number.
- Every pihm number is `\res{key}{metric}`, never typed. A placeholder box is expected until the exporter reruns. Exact construction facts (e.g. ζ‖D̃‖ = 2ζ(N−1), ζ = 40 on R2c from the rule) may be written as formulas.
- One line per paragraph (no hard wrapping). Australian spelling. No AI-writing tells: no "not only … but", no reflexive triplets, no internal labels in prose, no list-like run-in paragraphs; write cohesive narrative.
- Keep each file's scaffold comments. Update its LAND, CHECKLIST and HISTORY lines to reflect what changed. Never delete a REVISE or CITE-NEEDED comment unless this change resolves it. Add CITE-NEEDED where a new claim needs a source you cannot verify.
- Do not import anything in Part B.
- Build to a scratch directory, never `build/`: `latexmk -pdf -outdir="$TMPDIR/thesis-check" main.tex`. If biber exits silently with code 25, run `rm -rf $TMPDIR/par-*` and rebuild. Report new warnings or undefined references.
- Finish with: each edit as file:line, a one-line page-budget note if a section grows noticeably, and reviewer notes on anything left weak.

---

### Prompt 0 — pihm: new exporter keys

> Work in `~/Documents/School/Masters/Research/Code/pihm` (conda env `pihm`). Read `tools/thesis/derived.py`'s module docstring and follow its conventions; ported probes (p10–p17, p21) are the model. Add three derived-key functions to `DERIVED`, each with a docstring listing its keys, plus a unit test in the style of the existing ones:
>
> 1. **`trace_weights`**: port `tools/probes/p15_trace_weights.py` faithfully. Keys `trace-weights/<R5a|R5b>/n<n>x<n>` for n = 3, 4, with metrics `best_s` (the weight in `WEIGHTS` with least cost), `cost_ratio` (the best weighted cost over the unweighted descriptor's, cost = √(‖H‖/Δ)/γ as in the probe), `gap_ratio` and `norm_ratio` at `best_s` against s = 0, and `cost_ratio_s1` (s = 1 over s = 0). Check the values reproduce `docs/14_descriptor_gap.md` §5.4 (s = ½ best, 1.4–2.4× lower cost, s ≥ 1 worse). If they don't, stop and report rather than adjust.
> 2. **`carleman_overlap`**: over the current Carleman stateprep records (R8, R9*, R10*, both forms). Key `overlap/carleman/T2`: `gamma2_min`, `gamma2_max`, `count`, and the problem/K of the minimum. Key `overlap/R10/T3`: `p_min`, `p_max` of `predicted_p`, `max_rounds` (amplification rounds), `count`, and the K and M ranges covered. The current p7_t3 records show p_G 0.46–0.66 over K = 2–4, M = 12–48, with at most one round; confirm.
> 3. **`alpha_split`**: for the T3 descriptor series of R2c, key `alpha-split/R2c/descriptor/n<n>` for n = 5–8: `derivative_part` = the contribution to α_R of the terms that carry D̃'s diagonal (ζ·2(N−1) for the rescaled recurrence), `constant_part` = α_R − `derivative_part`, `constant_share` = `constant_part`/α_R. Derive the split from the encoder's actual LCU coefficients (`compile_system`), not by assumption; check that `derivative_part` + `constant_part` equals the record's α_R, and report how α_R combines blocks (ℓ¹ within the flat system LCU, quadrature across stacked rows). Records show α_R rising by 80·ΔN for n = 5–8 (ζ = 40), so c₀ ≈ 7.6×10³.
>
> Run the tests. Don't run the full export yet (the thesis must cite the keys first; the export is `--used-only`). Report the computed values so the thesis prompts can be checked against them. Don't commit.

---

### Prompt 1 — The ζ rule: calibration, its derivation and its limits (§5.4, everywhere ζ is named)

> Follow the Shared rules in `GeminiReviewPlan.md` (read Parts A–C first). Context: Gemini's report point 5, verified in rows 5a–5c. Decision: the ζ rule gets **no name or term**. Remove "a priori" (and don't substitute "calibrated rule") wherever it qualifies ζ, the rule or the rescaling. Keep "a priori" for the filter's parameters (edge, α_R, ε), §7.4 "The parameters are a priori", and App. F/G.
>
> 1. **§5.4 (`2_body/5_descriptor.tex`, "The a priori rule" paragraph, ~l. 171–176).** Retitle or merge the run-in heading so it carries no term. Keep the rule and its rationale. Add, in tight prose:
>    - why a simple zero needs ζ ∝ N: the concentrated states' quotient is O(N⁻⁴ζ^{2k}) (App. D, `D_descriptor.tex:247`), so balancing needs ζ ∝ N^{2/k}, which is N at second order; a double zero gives N^{4/k}, consistent with "Remaining limits" item 3;
>    - one sentence stating that the rule's two constants (the 2 and the ½) were **selected by calibration** on the benchmark problems and then held fixed, never refitted (its check is in-sample, as now);
>    - one sentence that the classes are asymptotic: a regular coefficient that dips close to zero behaves as singular once the resolution sees the dip, where the regular weight loses (App. D's "A coefficient that dips", `zeta-dip` keys; quote one or two with `\res`);
>    - one sentence that deriving ζ from the equation, rather than calibrating its constants, should be possible and is further work (point to `sec:future-work`).
> 2. **App. D (`3_footer/appendices/D_descriptor.tex` ~l. 228–282).** Make the calibration wording consistent with §5.4 and remove "a priori" where it qualifies the rule (e.g. l. 267). Keep the derivation there; the body states its result.
> 3. **Every other occurrence.** `grep -n "a priori"` across `1_header/`, `2_body/`, `3_footer/appendices/`. Rewrite each that qualifies ζ, the rule, the rescaling or the block weights. Known: `2_literature.tex:187`, `5_descriptor.tex:59, 264, 290`, `8_results.tex:304, 309`, `9_discussion.tex:49`, `10_conclusions.tex:63`, `D_descriptor.tex:267`, and check `H_catalogue.tex:130, 148, 291`. Also the Abstract's "a rescaling fixed in advance" (`1_header/5_abstract.tex`) and Chapter 1. Rephrase plainly ("block rescaling", "a weight per block set from the equation's coefficients and the resolution"). Don't leave a stock substitute phrase repeated everywhere.
> 4. **Governing documents.** Update `CLAUDE.md` Standing Facts ("The descriptor's gap" bullet: replace "an a priori ζ from the equation and the resolution, never fitted" with the calibration wording; keep "without ancilla" and "not free in gates" intact). Update `ThesisPlanning.md` wherever ζ's rule is called a priori (≈ l. 72, 331, 426, 866, 1335, 1748; keep l. 458's glossary row for filter parameters, adding a row that the ζ rule takes no term). Bump the plan's version line and the Standing Facts version with a one-line note.
>
> Don't touch Ch. 10's further-work prose beyond l. 63's wording; Prompt 5 adds the ζ item there.

---

### Prompt 2 — Formulation chapters: precision sentences (§2.4, §4.3, §4.6, §5.1, §5.2, §6.6, §7.4, notation)

> Follow the Shared rules in `GeminiReviewPlan.md` (read Parts A–C first). Each item is one or two sentences in place; don't restructure. Verified context is in Part A, rows 1, 2, 3, 4, 7, 8, P2.
>
> 1. **§2.4 (`2_body/2_literature.tex:270`).** Reword the frustration-free sentence. The square root comes from the ground value sitting at the edge of the encoded spectrum, where Chebyshev growth goes as the square root of the distance; for frustration-free Hamiltonians this is Somma and Boixo's amplification (`somma2013gap`), and H = R†R is frustration-free exactly when its kernel is exact. A small non-zero ground value leaves the degree unchanged and costs only the factor P_d(x₀)² in success probability (point to App. F / §7.4). Don't add a degradation formula (Part B.1). Keep `eq:degree` and the HOME OF eq:degree rule intact.
> 2. **§4.3 (`2_body/4_standard.tex:191`).** After "The root depends on the answer…", add App. B's reason (`B_standard_form.tex:171`): keeping Wu et al.'s invariant row, moved to the exact root, makes the residual differ from the printed one only in the defect, which keeps the comparison with their construction one-to-one; the stated data could enter answer-independently as the point-datum rows of `def:standard-form`, which no run uses in place of an invariant row. Name the scope: R4 and R6b only.
> 3. **§4.6 (`2_body/4_standard.tex:457`).** After the R3a sentence, add one hedged sentence: any encoding built from G², as a product with M_a's encoding or as a combination of terms each holding G², has subnormalisation at least of order ‖G²‖ = Θ(N⁴) (the constant term alone gives √2‖G²‖), so reaching the ideal bound on R3a would need M_aG² encoded as one operator; none is built, and whether one exists at polynomial cost in n is open. No "no modular circuit can" claim (Part B.4).
> 4. **§5.1 (`2_body/5_descriptor.tex:55`).** Extend "that reduction is not built or compared here" with App. A's reasons in one clause (the conversions weight the rows, so its least-squares problem differs; their entries must be encoded; the gap mechanism doesn't carry over unmeasured), and point to `sec:limitations` for what Olver–Townsend's bound leads one to expect (Prompt 4 writes that). Nothing from Part B.2.
> 5. **§5.2 and notation (`5_descriptor.tex:130`; `1_header/6_notation.tex:31`).** Replace the cramped exponent 2^{⌈log₂(1+Σ_a k_a)⌉} with 2^{n_f}, with n_f = ⌈log₂(1+Σ_a k_a)⌉ stated in running text (the several-axis generalisation of l. 104's n_f). Keep the notation table's entry and its one-axis case consistent with §8's symbol list.
> 6. **§6.6 (`2_body/6_extensions.tex:148`).** Add one sentence: the greedy colouring uses at most 2δ−1 matchings, so α ≤ (2δ−1)‖Γ‖_max, within a factor of two of the s‖Γ‖_max of a sparse-access encoding with s = δ (cite `gilyen2019qsvt`, checking the lemma), without that encoding's index-computing oracles for the symmetric layout's irregular monomial index. If you mention the alternative actually weighed, it is the Pauli-word expansion the other field-register matrices use, qualitatively (its numbers are not in results-v1). Keep it to the comparison (Part B.7).
> 7. **§7.4 (`2_body/7_pipeline.tex`, "The initial state").** Resolve the apparent ambiguity: a system's fields carry the state weighted by w₀/‖w₀‖, the problem's stated initial data; in a Carleman lift these are the level-one blocks, the physical fields, and every higher level starts at zero, as the descriptor's derivative blocks and padding do. Then keep the γ ≤ √(field weight) sentence. (Verified in `pihm/src/pihm/qsp/initial.py` and `Residual.field_blocks`.)

---

### Prompt 3 — Results: R2c's slope, Carleman overlaps, small fixes (§8.2, §8.4, §8.5)

> Follow the Shared rules in `GeminiReviewPlan.md` (read Parts A–C first). Prompt 0's keys must exist in pihm; cite them and leave placeholders until the export reruns. Rows 7, 9 and P4 of Part A hold the verified facts.
>
> 1. **§8.2, R2c (`2_body/8_results.tex:155`).** Replace "because its degree is still rising towards the asymptotic regime at n = 8" with the mechanism. The gap is the same in both columns and constant between n = 7 and 8 (cite `build/R2c/descriptor/n7` and `n8` gaps or the T3 records), so the two exponents differ only through α_R against ‖R‖. The subnormalisation adds the rescaled recurrence's 2ζ(N−1), with ζ = 40 from the rule, to an N-independent part that is still a large share at n = 8 (`\res{alpha-split/R2c/descriptor/n8}{constant_share}`), whereas ‖R‖₂ is already close to ζ‖D̃‖₂ (cite `norm_R` at n = 8). So the as-built exponent approaches one only as 2ζ(N−1) overtakes the constant, beyond the resolutions estimated; say this as a prediction. Also cite `stateprep/R2c/descriptor/n7/T3/filter=minimax` α_R if it helps (the export picks it up once cited). No typed numbers; nothing from Part B.8.
> 2. **Growth exponents' precision.** Gemini objects to three significant figures on two-point slopes. Change the growth-exponent `\res[3]{…/growth/…}` calls in `8_results.tex` (`tab:growth` and prose), `9_discussion.tex`, and `H_catalogue.tex` (`tab:catalogue-growth`) to `\res[2]`. Check that no prose then states a difference only the third figure showed.
> 3. **§8.4 and §8.5: Carleman overlap.** Add one or two sentences, in the systems/nonlinear subsection or where the R9/R10 preparations are first costed: the data-weighted initial state keeps the overlap of order one on every Carleman lift, γ² from `\res{overlap/carleman/T2}{gamma2_min}` to `…{gamma2_max}` (its minimum on R9e at K = 5), and on Navier–Stokes the estimated success probability stays between `\res{overlap/R10/T3}{p_min}` and `…{p_max}` across K = 2–4 and 12–48 modes, falling slowly with both, with at most `…{max_rounds}` round of amplification. So the 1/γ factor of `eq:total-cost` doesn't grow with the lift at the sizes run. Name the tier of each (T2, T3). Don't extrapolate to large K or M.
> 4. **§8.5 (`8_results.tex:279`).** Change "the descriptor's degree is the lower in every pair estimated, \res{…n4}{pairs} at n_t=4 and \res{…n5}{pairs} at n_t=5" to "… lower in all \res{…}{pairs} pairs at n_t = 4 and all \res{…}{pairs} at n_t = 5", so the counts can't be read as degrees.
> 5. Optional: the student signature on p. i is present but its JPG has a white box over the rule. If the user wants, swap in a transparent PNG; otherwise leave it.

---

### Prompt 4 — Discussion: the 2-D gap, the trace-weight measurement, the ultraspherical expectation (§9.1, §9.5, App. D)

> Follow the Shared rules in `GeminiReviewPlan.md` (read Parts A–C first). Prompt 0's `trace-weights/…` keys must exist in pihm. Rows 2 and 6 of Part A hold the verified facts.
>
> 1. **App. D, descriptor-gap section (`3_footer/appendices/D_descriptor.tex`, `app:descriptor-gap`).** Add a short paragraph reporting the trace-weight measurement: each datum-slice row weighted by (m+1)^s, m its tangential mode, for s from 0 to 2, on R5a and R5b at three and four qubits per axis. The weight raises the gap, but the norm rises about as fast; the best weight (`best_s`) lowers the cost by `cost_ratio`, and s = 1 makes it worse (`cost_ratio_s1`). Exact classical computation.
> 2. **§9.1 (`2_body/9_discussion.tex:6`).** Rewrite the sentences from "The datum rows of … weigh a boundary function equally at every frequency" through "the first remedy to test". Keep the coercivity reading as an inference, and you may state the trace-against-interior mismatch qualitatively: the slice rows penalise a high-frequency near-solution at the order of its field norm, while the rescaled derivative blocks that dominate the denominator grow with N (no exponents; Part B.6). Then report the measurement in one or two sentences: weighting the datum rows by a power of the tangential mode helps by a small constant factor and doesn't restore the gap, because the norm rises with the gap. So the missing coercivity isn't supplied by reweighting the existing rows alone. Point to App. D.
> 3. **§9.5 (`9_discussion.tex:52`).** Replace "and nothing here predicts whether it keeps the descriptor's norm without eroding the gap" with a hedged expectation. Olver and Townsend's operator has derivative factors whose norm grows linearly in N at every order, and its condition number grows linearly in N under their hypotheses (§2.3). On a regular problem this suggests the reduction would reach the descriptor's Θ̃(N) degree on N unknowns without the block register. Its least-squares weighting, its encoding with variable coefficients, and its gap on singular problems and on two axes are untested. Before writing, check the precise hypotheses Olver–Townsend state for the 2-norm bound (`olver2013`; the paper isn't in `~/…/Papers`, so fetch or flag CITE-NEEDED). Keep the claim at "suggests"; it changes §9.5's limitation from "unknown" to "expected and untested". Make `2_literature.tex:171` and `A_chebyshev.tex:207` consistent with it (one clause each at most).
> 4. Check Ch. 9's closing paragraph (`9_discussion.tex:54`) still reads true after items 2–3.
>
> Leave Ch. 10 to Prompt 5, but list for it the future-work changes these imply.

---

### Prompt 5 — Chapter 10: Conclusions and Future Work, restructured

> Follow the Shared rules in `GeminiReviewPlan.md` (read Parts A–C first). This is Gemini's point 10, accepted as a style decision: Ch. 10's first five paragraphs restate §§9.1–9.4 and the future work is buried. Run this after Prompts 1–4.
>
> 1. **Governing plan first.** Update `ThesisPlanning.md` §5.10 and the FORM block of `2_body/10_conclusions.tex`'s scaffold: Ch. 10 now has **two subsections, 10.1 Conclusions and 10.2 Future Work**. 10.2's paragraphs carry bold run-in leads. 10.1 is structured around the three questions of §3.5, Q(i)–(iii), which may be named. Keep the rules: no results quoted, no `\res`, no measured numbers, no new citations (memory: "Conclusion quotes no results"). Record the change in HISTORY and bump the plan version. Update CLAUDE.md's Verification-mode bullet on chapter and section numbers to include "Conclusions Ch. 10 with two sections".
> 2. **10.1 Conclusions (about one page).** Compress the current ¶1–¶5 into a tight answer to Q(i), Q(ii) and Q(iii) in turn, then the single thesis statement ("costs what its residual's conditioning costs; conditioning is fixed by the formulation"), the implications beyond the method (the encoder/Hamiltonian audit and the ideal bound; the link to linear-systems conditioning; no speed-up over classical solvers claimed), and the two boundaries (the gap on several axes; the prepared state versus the answer). Reframe, don't re-derive: one sentence per point that Ch. 9 proves, no mechanism retold. Keep the Standing Facts' scopes (regular, singular, two axes; neither form poly-log) and the wording from Prompt 1 (no term for the ζ rule).
> 3. **10.2 Future Work, with bold leads.** Rebuild from the current ¶8–¶10 and fold in:
>    - **A gap on several axes:** power weights on the datum rows were measured and are not enough (Ch. 9 now says so). Recast the first step as the next question: whether any reweighting, or additional boundary rows of the kind first-order-system least squares uses, restores coercivity (hedge; flag CITE-NEEDED if a FOSLS specific is claimed). Then the full ultraspherical reduction, with the expectation of §9.5: build it and measure R2a, R3 and R5b.
>    - **Deriving the block weight:** replace the calibrated constants by a ζ derived from the equation (the item from Prompt 1).
>    - The existing self-certification (quantitative flat-gap bound; on-circuit edge; consecutive Carleman orders; readout shot count) and "what the residual carries" (native complex; noisy data rows) items, each with its one concrete first step.
>    - Keep `\label{sec:future-work}` on 10.2's heading, so the pointers from Chs 6, 7, 9 and App. K still resolve. Check every `\Cref{sec:future-work}` and `\Cref{sec:conclusions}` caller still reads correctly.
> 4. Close on the shift (residual first, circuit second) in one sentence. Report the chapter's length before and after; target about 2 pp.

---

### Prompt 6 — Export, build and consistency check

> In pihm: `python tools/thesis/export_numbers.py --used-only`, then `--check`; report any key still pending or stale. In the thesis: build to `$TMPDIR/thesis-check` and confirm no `Package pihm Warning` remains for the keys Prompts 0–5 introduced. Then run a **Verification Mode** pass (`CLAUDE.md`), limited to what this plan touched:
> - "a priori" now qualifies only the filter's parameters, never ζ, the rule or the rescaling, in the `.tex` files, CLAUDE.md and ThesisPlanning.md;
> - the trace-weight result, the ultraspherical expectation and the R2c mechanism are stated identically wherever they recur (Ch. 2, §5.1, §8.2, §9.1, §9.5, Ch. 10, App. A, App. D);
> - Ch. 10 quotes no result and adds no citation; `sec:future-work` resolves to 10.2;
> - growth exponents are `\res[2]` everywhere;
> - nothing in Part B appears anywhere.
>
> Report only actual inconsistencies, with file:line. Don't commit.
