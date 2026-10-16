"""fig:gap-rescaling -- block rescaling: the descriptor's gap and the field block's weight.

(a) The gap against N, unscaled (open) and block-rescaled (filled), a panel per problem, at the
resolutions whose reference is trusted. (b) The field block's weight w_f in the ground state at
n = 8 (n = 5 per axis on R5), unscaled against rescaled, with gamma^2 from exact emulation
marked where a preparation ran at that n. Data as notebook 42_block_rescaling selects it.

Run with the pihm environment:  /opt/miniconda3/envs/pihm/bin/python Figs/scripts/make_gap_rescaling.py
"""

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pihm.pipeline.results import primary_preparations, reference_builds
from pihm.pipeline.summary import cases

import figstyle as fs

fs.apply()
results = fs.results()
builds = [r for r in results.rows("p5_build") if r["status"] == "ok"]
unscaled = cases(builds, label="unscaled")
rescaled = reference_builds(builds)
gamma2 = {
    (r["problem"], r["n"]): r["gamma2"]
    for r in primary_preparations(results.rows("p5_stateprep", regime="descriptor"), variant="corrected")
}
GAPS = ("R2a", "R2c", "R3a", "R4a", "R5a", "R5b", "R5c")
WEIGHTS = sorted({p for p, _, _ in unscaled})
RESCALED, UNSCALED = fs.DESC, fs.INK_SECONDARY


def series(table, problem):
    """Return a problem's trusted rows of a build table, ordered by n."""
    return sorted((r for (p, _, _), r in table.items() if p == problem and r["trusted"] is True),
                  key=lambda r: r["n"])


figure = plt.figure(figsize=(fs.WIDTH, 3.5), layout="constrained")
left, right = figure.subfigures(1, 2, width_ratios=[2.15, 1], wspace=0.02)
grid = left.subplots(2, 4, sharex=True, sharey=True)
for axis, problem in zip(grid.ravel(), GAPS, strict=False):
    for table, colour, filled in ((unscaled, UNSCALED, False), (rescaled, RESCALED, True)):
        rows = series(table, problem)
        fs.points(axis, [2 ** r["n"] for r in rows], [r["gap"] for r in rows], colour, "o",
                  [filled] * len(rows), lw=1.1)
    axis.set_title(problem + (" (per axis)" if problem.startswith("R5") else ""), loc="right",
                   fontsize=7.5, color=fs.INK_SECONDARY)
grid[1, 3].remove()
for axis in grid.ravel()[:7]:
    axis.set_xscale("log", base=2)
    axis.set_yscale("log")
    axis.set_xticks([4, 16, 64, 256, 1024], ["$2^2$", "$2^4$", "$2^6$", "$2^8$", "$2^{10}$"])
    axis.minorticks_off()
for axis in grid[1, :3]:
    axis.set_xlabel(r"$N$")
grid[0, 3].xaxis.set_tick_params(labelbottom=True)
grid[0, 3].set_xlabel(r"$N$")
for axis in grid[:, 0]:
    axis.set_ylabel(r"gap $\Delta$")
fs.label(grid[0, 0], "(a)")

dots = right.subplots()
for row, problem in enumerate(WEIGHTS):
    top = 5 if problem.startswith("R5") else 8
    u, r = unscaled[(problem, "corrected", top)], rescaled[(problem, "corrected", top)]
    dots.plot([u["field_weight"], r["field_weight"]], [row, row], color=fs.GRID, linewidth=1.6, zorder=1)
    dots.plot(u["field_weight"], row, "o", color=UNSCALED, markerfacecolor="white", markeredgewidth=0.9, zorder=3)
    dots.plot(r["field_weight"], row, "o", color=RESCALED, zorder=3)
    if (problem, top) in gamma2:
        dots.plot(gamma2[(problem, top)], row, "x", color=fs.INK, markersize=4.5, markeredgewidth=1.0, zorder=4)
dots.set_yticks(range(len(WEIGHTS)), [p + (", n = 5" if p.startswith("R5") else "") for p in WEIGHTS], fontsize=7)
dots.set_ylim(len(WEIGHTS) - 0.5, -0.5)
dots.set_xscale("log")
dots.set_xlabel(r"field block's weight $w_f$ ($n = 8$)")
dots.grid(axis="y", visible=False)
fs.label(dots, "(b)")

handles = [
    Line2D([], [], color=UNSCALED, marker="o", markerfacecolor="white", label="unscaled"),
    Line2D([], [], color=RESCALED, marker="o", label="block-rescaled"),
    Line2D([], [], color=fs.INK, marker="x", linestyle="none", label=r"$\gamma^2$ (emulated)"),
]
figure.legend(handles=handles, loc="outside upper center", ncols=3)
fs.save(figure, "gap_rescaling")
