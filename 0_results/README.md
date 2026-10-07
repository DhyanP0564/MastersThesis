# Quoting pihm's results

Every number the thesis takes from `pihm` is looked up by key, never typed:

```latex
The filter degree is \res{stateprep/R2a/standard/n3/T2}{degree}.
```

`generated/numbers.tex` holds the value of every run the thesis's own `\res`/`\resflag` calls
cite -- not every run the campaigns expect: at full size (thousands of runs) the file is too large
for pdfTeX to load (the string pool, then main memory), so only the committed, used-only export
actually compiles. It is written by `pihm/tools/thesis/export_numbers.py --used-only`, never by
hand. `results.tex` reads it and defines the commands below; `main.tex` inputs it. When a campaign
is rerun, the exporter rewrites the file, and the next compile shows the new numbers. A number that
does not exist yet renders as a box naming why. The design is ThesisPlanning.md §10.2 (decision
T-15, amended 2026-09-27) and pihm's D-062.

## The routine

| when | do |
|---|---|
| results changed (a campaign run or collected) | in `Code/pihm/`, with `conda activate pihm`: `python tools/thesis/export_numbers.py --used-only`, then recompile |
| you need a number | find its key (below), write `\res{<key>}{<metric>}` |
| you want to know what is missing | `python tools/thesis/export_numbers.py --check`: every quoted number not current, with file, line and fix (`--verbose` lists all) |
| the log says `Package pihm Warning` | the same list, one warning per placeholder, and a count at the end |
| submission | after P8: `export_numbers.py --final` (below) |

Commit `generated/numbers.tex` with the thesis: its diff shows exactly which numbers moved.

## Finding a key

A run's key is its record directory without the hash:

```
<stage>/<problem>/<variant>/<regime>/n<size>[/<tier>][/<option>=<value>...][/<label>]
```

| segment | values |
|---|---|
| stage | `build` (classical solve, P2), `encode` (circuit verification, Pillar 1), `stateprep` (state preparation, Pillar 2), `readout` (the paper's interferometric readout) |
| problem | `R1`, `R2a` … `R10c-M316`, then `faithful` for a paper panel as printed (the reproduction's only; the corrected problem names no variant) |
| regime | `standard` or `descriptor` |
| size | qubits per axis: `n3`, or `n3x3` on two axes (R5) |
| tier | `stateprep` and `readout` only: `T1` (circuit simulated) or `T2` (exact emulation) |
| options | only when not the default: `truncation=tau`, `verify=none`, `shots=100000`, `epsilon=1e-08`, `kind=uniform`, … |
| label | the campaign group's label, as its token in `pihm/configs/thesis.yaml` (`exact-root`, `chebyshev-source`, `maclaurin-7`, `xs=0.5`, …); most labels have an empty token and add nothing |

Examples: `build/R2a/faithful/standard/n3`, `build/R4b/faithful/standard/n5/exact-root`,
`build/R2a/faithful/standard/n5/truncation=tau`, `encode/R3c/standard/n4/verify=none`,
`readout/R1/standard/n2/T1/shots=100000`.

The two geometric initial states a T1 campaign runs separately share one key, and the key quotes the
one with the larger success probability, as the reports do.

**To look one up** once it is already cited, search the committed file. Each key has a comment line
with its status and source record, then one line per value:

```bash
grep -A40 '^% stateprep/R2a/standard/n3/T2 ' 0_results/generated/numbers.tex
```

**To browse before citing** (the committed file only holds cited keys), write the full export
somewhere scratch -- never commit it, and never point the thesis at it; at full size it does not
compile:

```bash
python tools/thesis/export_numbers.py --thesis /tmp/pihm-browse
grep -A40 '^% stateprep/R2a/standard/n3/T2 ' /tmp/pihm-browse/0_results/generated/numbers.tex
```

### Derived numbers

Quantities no single record holds come from `pihm/tools/thesis/derived.py`:

| key | metrics | meaning |
|---|---|---|
| `build/<p>/<variant>/<regime>/best[/<label>]` | `field_err_linf`, `n` | smallest *trusted* L∞ error over n, and the n where it occurs |
| `build/<p>/<variant>/<regime>/floor[/<label>]` | `low`, `high` | smallest and largest L∞ error from n = 4 on, trusted or not (the Fig. 5 triage) |
| `derivative/n<n>`, n = 2 … 10 | `norm`, `structured_alpha`, `structured_ratio`, `published_alpha`, `published_ratio` | ‖𝔾‖₂, and the structured and published encodings' α and α/‖𝔾‖₂ |

A statistic is `stale` if any run it ranges over is not current.

## Metrics

A metric is the record's own name for it, the same as the column names of pihm's `summary.csv`.
The ones most often quoted:

| stage | metric | meaning |
|---|---|---|
| all | `time_total` | the run's wall time, seconds |
| `build` | `eta`, `eta_ideal` | η_e of the ground state; ‖b‖² of the reference coefficients |
| | `field_err_linf`, `field_err_l2` | L∞ and relative L² error of the decoded field against the reference solution |
| | `infidelity` | 1 − \|⟨b̂\|ψ⟩\|² against the reference coefficients |
| | `gap`, `relative_gap`, `hamiltonian_norm` | Δ = λ₁ − λ₀, Δ/‖H‖₂, ‖H‖₂ = σ²_max |
| | `sigma_min`, `gap_ratio`, `kernel_dimension` | σ₀; the ratio at the kernel boundary; the kernel's size |
| | flag `trusted` | one-dimensional kernel with `gap_ratio` ≥ 100 (the † in the tables) |
| `encode` | `alpha_R` | α_R of the stacked-residual reflection |
| | `verify_max_error`, `verify_tolerance`, flag `verify_passed` | the circuit against the classical Hamiltonian |
| | `cx_count`, `depth`, `one_qubit_count`, `n_qubits_total`, `n_anc_qubits` | resources |
| `stateprep` | `degree`, `tau`, `epsilon` | the QITE filter's degree d, β (`tau` in the code), and target accuracy ε |
| | `success_probability`, `infidelity` | the post-selection probability p_G; the prepared state against the reference |
| | T1 only: `t2_agreement`, `n_qubits` | circuit output against T2; the circuit's width |
| | infeasible runs: `predicted_seconds`, `predicted_peak_gib` | the resource estimate that refused the run |
| `readout` | `eta`, `field_err_linf`, `success_probability` | the read-out η_e and field error, at the probe points |
| | T1 only: `t2_agreement`, `eta_agreement`, `sampled_eta` | against T2; with `shots`, the shot-sampled η_e |

The full definitions are in the stage code, under `Code/pihm/src/pihm/`: `pipeline/stages.py`
(`build`, `encode`) and `pipeline/pillar2.py` (`stateprep`, `readout`), with the quantities
documented in `classical.py` and `qsp/`. The generated file lists every metric each key has.

## Formatting

| write | gives |
|---|---|
| `\res{…}{…}` | 3 significant figures: fixed notation from 10⁻³ to 10⁵ (an integer digit is never rounded away), scientific outside |
| `\res[2]{…}{…}` | 2 significant figures |
| `\res[2,sci]{…}{…}`, `\res[4,fixed]{…}{…}` | force scientific or fixed notation |
| `\res[places=5]{…}{…}` | 5 decimal places, fixed |
| `\res[digits=4, notation=fixed]{…}{…}` | the long form of `[4,fixed]` |
| an integer metric (`degree`, `cx_count`, `n`) | printed exactly, grouped (`17 750`), unless `sci` |
| `\resflag{<run>}{<flag>}{<if true>}{<if false>}` | text chosen by a Boolean, e.g. `$\res[2,sci]{<run>}{field_err_linf}\resflag{<run>}{trusted}{}{^{\dagger}}$` |

`\res` works in text, tables, captions and maths; the result is one unbreakable box, so
`$\res{…}{…}^{\dagger}$` puts the dagger on the whole number. siunitx options for every quoted
number go in `\ressiunitx` (`results.tex`, top); for example, add `group-separator = {,}` for
comma-grouped thousands.

## Placeholders

| box | meaning | what to do |
|---|---|---|
| pending | in a campaign, not yet run | run the campaign (Setonix for heavy ones), collect, re-export |
| infeasible | refused on its resource estimate | a legitimate result: say so ("beyond the simulation budget"), quote the estimate (`predicted_seconds`, `predicted_peak_gib`). The final text prints `\resinfeasiblemark` (default `--`) |
| failed | the run failed | fix it in pihm, rerun |
| stale (framed value) | only a record of an earlier configuration exists; the old value is shown | rerun the campaign the reason names, re-export |
| no value | the run exists but records no such metric | check the metric name in the generated file |
| unknown | no campaign has the key: a typo, or a campaign not written yet | check the key; add the campaign to `pihm/configs/thesis.yaml` |

Values exported before the final export print tinted, so provisional numbers stay visible while
drafting (`\restintfalse` turns the tint off).

**Stale** means the run's *configuration* changed (the problem, an option, the run schema). A code
change that leaves the configuration alone does not make a record stale; the freeze rule
(Planning.md §9.3) covers those.

## The final export

With the package's source committed: `python tools/thesis/export_numbers.py --final`. It refuses,
listing why, unless every number the thesis quotes was made by the source the tree holds (each
record's source digest, the code that ran) and none is a draft-only placeholder. Once written, values print untinted, and any remaining
placeholder except `infeasible` is a compile error. To try a final build early, put `\resfinaltrue`
after `\input{0_results/results.tex}`.

## Extending

- **A new campaign:** add `<campaign file>: <results directory>` under `campaigns:` in
  `pihm/configs/thesis.yaml`. A new run label gets a token under `labels:` (`""` leaves it out of
  the key). If two runs end up with the same key, the exporter stops and says which; give one a
  label.
- **A new derived number:** a function in `pihm/tools/thesis/derived.py` that returns `Entry`
  objects under a new key, added to `DERIVED`, with a test in `tests/unit/test_thesis_export.py`.
  The arithmetic lives there, never in LaTeX.
- **`\prov{…}`** stays only for a number pihm does not produce yet; the pre-submission check
  (ThesisPlanning.md §14) fails on any left.

## Pitfalls

- The exporter's report reads literal `\res{…}{…}` in the `.tex` files. A key built by your own
  macro still resolves in LaTeX, but the report cannot see it.
- Changing a campaign's options or label token changes its keys; the report then lists the old
  keys as unknown.
- A `\res` in a caption is typeset twice (the caption and the list of tables), so it counts twice
  in the log.
- Never round a number by hand: the file holds full precision, and rounding is the format's job.
