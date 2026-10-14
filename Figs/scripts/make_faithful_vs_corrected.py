"""fig:faithful-vs-corrected -- Wu et al.'s Fig. 5 (R4a-R4d): the panels as printed against as run.

Top row: the analytic solution, the paper-faithful ground state (rounded constraint points,
Maclaurin sources) and R4a-R4d as run (exact roots, Chebyshev sources), at the printed n. Bottom
row: the L-infinity error against n for both variants. Classical ground states from the
reproduction (p2_reproduction), as notebooks 10_reproduction and 11_faithful_vs_corrected select.

Run with the pihm environment:  /opt/miniconda3/envs/pihm/bin/python Figs/scripts/make_faithful_vs_corrected.py
"""

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pihm.pipeline.summary import cases, read_arrays
from pihm.plotting.style import VARIANT_STYLE

import figstyle as fs

fs.apply()
results = fs.results()
rows = results.rows("p2_reproduction")
root = results.directory("p2_reproduction")
PANELS = ("R4a", "R4b", "R4c", "R4d")
NAME = {"faithful": "as printed (paper-faithful)", "corrected": "as run"}
variants = {v: cases(rows, variant=v, label="", truncation="none") for v in ("faithful", "corrected")}

figure, axes = plt.subplots(2, 4, figsize=(fs.WIDTH, 3.6), constrained_layout=True)
for column, problem in enumerate(PANELS):
    top, bottom = axes[0, column], axes[1, column]
    printed = int(next(r for (p, _, _), r in variants["faithful"].items() if p == problem)["printed_n"])
    reference_drawn = False
    for variant in ("faithful", "corrected"):
        colour, marker = VARIANT_STYLE[variant]
        row = variants[variant][(problem, variant, printed)]
        arrays = read_arrays(root, row)
        if not reference_drawn:
            top.plot(arrays["grid_0"], arrays["reference"], color=fs.INK, linewidth=2.4, alpha=0.25)
            reference_drawn = True
        top.plot(arrays["grid_0"], arrays["field"], color=colour,
                 linestyle="-" if variant == "faithful" else (0, (4, 2)), linewidth=1.2)
        series = sorted((r for (p, _, _), r in variants[variant].items() if p == problem), key=lambda r: r["n"])
        fs.points(bottom, [r["n"] for r in series], [r["field_err_linf"] for r in series], colour, marker,
                  [r["trusted"] is True for r in series], lw=1.1)
        print(problem, variant, "printed n", printed, "err", row["field_err_linf"])
    top.set_title(f"{problem}, $n={printed}$", loc="left", fontsize=8)
    top.set_xlabel("$x$")
    bottom.axvline(printed, color=fs.MUTED, linewidth=0.7, linestyle=(0, (1, 1.5)))
    bottom.set_yscale("log")
    bottom.set_xlabel("$n$")
axes[0, 0].set_ylabel("$f(x)$")
axes[1, 0].set_ylabel(r"field error ($L^\infty$)")
handles = [
    Line2D([], [], color=fs.INK, linewidth=2.4, alpha=0.25, label="analytic solution"),
    Line2D([], [], color=VARIANT_STYLE["faithful"][0], marker=VARIANT_STYLE["faithful"][1], label=NAME["faithful"]),
    Line2D([], [], color=VARIANT_STYLE["corrected"][0], marker=VARIANT_STYLE["corrected"][1], linestyle=(0, (4, 2)), label=NAME["corrected"]),
    Line2D([], [], color=fs.INK_SECONDARY, marker="o", markerfacecolor="white", linestyle="none", label="reference not trusted"),
    Line2D([], [], color=fs.MUTED, linewidth=0.7, linestyle=(0, (1, 1.5)), label="printed $n$"),
]
figure.legend(handles=handles, loc="outside upper center", ncols=5, fontsize=7, columnspacing=1.0)
fs.save(figure, "faithful_vs_corrected")
