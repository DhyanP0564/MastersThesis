"""fig:decoded-field -- the prepared field's error against its budget, R2a in the descriptor.

The L-infinity error of the field decoded classically from the prepared state, the
discretisation's error eps_disc, and the budget of eq:error-budget split into its filter,
truncation and phase terms; minimax filter, eps = 1e-6, exact emulation. The primary
preparations, as notebook 32_field_and_budget selects them.

Run with the pihm environment:  /opt/miniconda3/envs/pihm/bin/python Figs/scripts/make_decoded_field.py
"""

import matplotlib.pyplot as plt
from pihm.pipeline.results import primary_preparations
from pihm.plotting.style import SERIES

import figstyle as fs

fs.apply()
results = fs.results()
rows = sorted(
    (r for r in primary_preparations(results.rows("p5_stateprep", regime="descriptor"), problem="R2a", variant="corrected")
     if 3 <= r["n"] <= 8),
    key=lambda r: r["n"],
)
n = [r["n"] for r in rows]

figure, axis = plt.subplots(figsize=(4.6, 2.7), constrained_layout=True)
axis.plot(n, [r["field_budget"] for r in rows], color=fs.DESC, linewidth=2.2, alpha=0.45, label=r"budget (total, with $\varepsilon_{\mathrm{disc}}$)")
for column, text, colour, marker in (
    ("field_filter", "filter term", fs.DESC, "v"),
    ("field_truncation", "truncation term", SERIES[1], "s"),
    ("field_phases", "phase term", fs.STD, "^"),
):
    axis.plot(n, [r[column] for r in rows], color=colour, linestyle=(0, (3, 1.5)), linewidth=1.0,
              marker=marker, markerfacecolor="white", markeredgewidth=0.9, markersize=4, label=text)
axis.plot(n, [r["eps_disc"] for r in rows], color=fs.MUTED, linewidth=1.1, marker="D", markersize=3.5,
          label=r"discretisation $\varepsilon_{\mathrm{disc}}$")
axis.plot(n, [r["field_err_linf"] for r in rows], color=fs.INK, linewidth=1.5, marker="o",
          label=r"field error ($L^\infty$, emulated)", zorder=5)
axis.set_yscale("log")
axis.set_xlabel("$n$")
axis.set_ylabel("error in the field")
axis.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), fontsize=7)
fs.save(figure, "decoded_field")
