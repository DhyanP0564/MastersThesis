"""fig:navier-stokes -- two-dimensional Navier-Stokes (R10).

(a) Vorticity at t = T decoded from the prepared state (descriptor, T2) for the Taylor-Green
vortex (R10a) and the vortex pair at a/nu = 10 (R10c), twelve modes, K = 3, n_t = 4, with its
departure from the Galerkin reference. (b) The minimax degree (T3) against the modes M at K = 2,
n_t = 4, both forms, as built (solid) and at alpha_R = ||R|| (dashed): R10c and R10a over M,
a/nu = 3 and 30 at M = 12, where alone they were estimated. (c) The lift's per-order error ratio
against M. Data as notebook 70_navier_stokes selects it; (a) through pihm.pipeline.solutions.

Run with the pihm environment:  /opt/miniconda3/envs/pihm/bin/python Figs/scripts/make_navier_stokes.py
"""

import math
from itertools import pairwise

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
from matplotlib.lines import Line2D
from pihm.pipeline.solutions import Catalogue, CaseKey, solution
from pihm.plotting.style import DIVERGING, SEQUENTIAL
from pihm.problems import ladder

import figstyle as fs

fs.apply()
results = fs.results()
MODES = {cutoff: count for count, cutoff in ladder.R10_MODES.items()}
FORMS = ("standard", "descriptor")
DASH = (0, (4, 2))
diverging = LinearSegmentedColormap.from_list("pihm-diverging", DIVERGING)

figure = plt.figure(figsize=(fs.WIDTH, 5.0), layout="constrained")
maps_fig, lines_fig = figure.subfigures(2, 1, height_ratios=[1, 1.45], hspace=0.04)

# (a) vorticity maps --------------------------------------------------------------------------
catalogue = Catalogue.read(results, ["p7_build", "p7_stateprep"])
side = np.linspace(0.0, 2.0 * np.pi, 97)
X, Y = np.meshgrid(side, side)
maps = maps_fig.subplots(1, 4)
for pair, (problem, title) in enumerate((("R10a-M12", "R10a, Taylor–Green"), ("R10c-M12", r"R10c, $a/\nu=10$"))):
    sol = solution(catalogue.case(CaseKey(problem, 4, 3)))
    space = sol.space
    last = int(np.argmax(sol.seconds))
    prepared = next(l for l in sol.layers if l.regime == "descriptor" and l.source == "T2")
    omega = space.field(prepared.field[:, last], X, Y)
    departure = omega - space.field(sol.reference[:, last], X, Y)
    field, error = maps[2 * pair], maps[2 * pair + 1]
    bound = np.abs(omega).max()
    image = field.pcolormesh(side, side, omega, cmap=diverging, norm=TwoSlopeNorm(0, -bound, bound),
                             shading="gouraud", rasterized=True)
    field.contour(side, side, space.stream(prepared.field[:, last], X, Y), levels=8,
                  colors=fs.INK_SECONDARY, linewidths=0.5)
    maps_fig.colorbar(image, ax=field, fraction=0.08, pad=0.03).ax.tick_params(labelsize=6.5)
    field.set_title(f"{title}\n" + rf"$\omega$ at $s={sol.seconds[last]:g}$ (T2)", fontsize=7)
    bound = np.abs(departure).max()
    image = error.pcolormesh(side, side, departure, cmap=diverging, norm=TwoSlopeNorm(0, -bound, bound),
                             shading="gouraud", rasterized=True)
    bar = maps_fig.colorbar(image, ax=error, fraction=0.08, pad=0.03, format="%.0e")
    bar.ax.tick_params(labelsize=6.5)
    error.set_title("departure from\n" + r"the Galerkin reference", fontsize=7)
for axis in maps:
    axis.set_aspect("equal")
    axis.grid(False)
    axis.set_xticks([0, np.pi, 2 * np.pi], ["0", r"$\pi$", r"$2\pi$"])
    axis.set_yticks([0, np.pi, 2 * np.pi], ["0", r"$\pi$", r"$2\pi$"])
    axis.set_xlabel("$x$", labelpad=1)
    for spine in axis.spines.values():
        spine.set_visible(False)
maps[0].set_ylabel("$y$")
maps_fig.text(0.0, 0.99, "(a)", fontweight="bold", fontsize=8.5, va="top")

# (b) degree against M --------------------------------------------------------------------------
degree, ratio = lines_fig.subplots(1, 2)
t3 = [r for r in results.rows("p7_t3") if r["status"] == "ok" and r["carleman"] == 2 and r["n"] == 4]


def estimates(problem_prefix, form):
    """Return a strength's K = 2, n_t = 4 estimates of one form over the modes, ordered by M."""
    rows = [r for r in t3 if r["regime"] == form and r["problem"].split("-")[0] == problem_prefix
            and "-W" not in r["problem"]]
    return sorted(rows, key=lambda r: MODES[ladder.navier_stokes_panel(r["problem"])[1]])


for prefix, name, marker in (("R10c", r"$a/\nu=10$", "o"), ("R10a", "Taylor–Green", "^")):
    for form in FORMS:
        rows = estimates(prefix, form)
        M = [MODES[ladder.navier_stokes_panel(r["problem"])[1]] for r in rows]
        colour = fs.COLOUR[form]
        degree.plot(M, [r["degree"] for r in rows], color=colour, marker=marker,
                    markerfacecolor=colour if prefix == "R10c" else "white", markeredgewidth=0.9)
        degree.plot(M, [r["ideal_degree"] for r in rows], color=colour, linestyle=DASH, linewidth=1.0)
    degree.annotate(name, xy=(M[-1], estimates(prefix, "standard")[-1]["degree"]), xytext=(5, 0),
                    textcoords="offset points", va="center", fontsize=7, color=fs.INK_SECONDARY)
for prefix, name, marker in (("R10b", r"$a/\nu=3$", "<"), ("R10d", r"$a/\nu=30$", ">")):
    for form in FORMS:
        (row,) = estimates(prefix, form)
        colour = fs.COLOUR[form]
        degree.plot(12, row["degree"], marker=marker, color=colour, linestyle="none")
        degree.plot(12, row["ideal_degree"], marker=marker, color=colour, markerfacecolor="white",
                    markeredgewidth=0.9, linestyle="none")
degree.set_xscale("log")
degree.set_yscale("log")
degree.set_xticks([12, 20, 28, 48], ["12", "20", "28", "48"])
degree.minorticks_off()
degree.set_xlim(10, 80)
degree.set_xlabel("modes $M$")
degree.set_ylabel(r"filter degree $d$ (T3)")
degree.legend(handles=[
    Line2D([], [], color=fs.STD, label="standard form"),
    Line2D([], [], color=fs.DESC, label="descriptor"),
    Line2D([], [], color=fs.INK_SECONDARY, linestyle=DASH, linewidth=1.0, label="ideal bound"),
    Line2D([], [], color=fs.INK_SECONDARY, marker="<", linestyle="none", label=r"$a/\nu=3$"),
    Line2D([], [], color=fs.INK_SECONDARY, marker=">", linestyle="none", label=r"$a/\nu=30$"),
], loc="upper left", ncols=2, fontsize=6.5, handlelength=1.6, columnspacing=0.8)
degree.set_ylim(top=degree.get_ylim()[1] * 6)
fs.label(degree, "(b)")

# (c) per-order ratio of the lift's error ---------------------------------------------------------
builds = [r for r in results.rows("p7_build") if r["status"] == "ok" and r["regime"] == "descriptor"]
finest = {}
for r in builds:
    key = (r["problem"], r["carleman"])
    if key not in finest or r["n"] > finest[key]["n"]:
        finest[key] = r


def per_order(problem):
    """Return the geometric mean of the lift error's ratio from one order to the next."""
    pts = sorted((k, r["lift_err_linf"]) for (p, k), r in finest.items() if p == problem)
    steps = [b[1] / a[1] for a, b in pairwise(pts) if b[0] == a[0] + 1]
    return math.exp(sum(math.log(s) for s in steps) / len(steps)) if steps else None


# Not drawn: with sine-only data each Carleman order corrects one parity of modes (K = 2 -> 3 the
# sines, 3 -> 4 the cosines), and this case's L-infinity error sits on a cosine mode, so its one
# step's ratio is 1 by construction, not a measured stall.
OMITTED = {"R10d-M48-W8"}
lines = ((3.0, 1.0, SEQUENTIAL[2], "-"), (10.0, 1.0, SEQUENTIAL[4], "-"), (30.0, 1.0, SEQUENTIAL[6], "-"),
         (30.0, 0.125, SEQUENTIAL[6], DASH))
for strength, window, colour, style in lines:
    pts = sorted(
        (MODES[cutoff], per_order(p))
        for p in {p for p, _ in finest} - OMITTED
        for s, cutoff, w in [ladder.navier_stokes_panel(p)]
        if s == strength and w == window
    )
    label = rf"$a/\nu={strength:g}$" + ("" if window == 1.0 else r", $T=\frac{1}{8}$")
    ratio.plot([m for m, _ in pts], [v for _, v in pts], color=colour, linestyle=style, marker="o", label=label)
ratio.axhline(1.0, color=fs.MUTED, linewidth=0.8)
ratio.text(10.5, 1.08, "above: the lift diverges", fontsize=6.5, color=fs.MUTED, ha="left", va="bottom")
ratio.set_xscale("log")
ratio.set_yscale("log")
ratio.set_xticks([12, 20, 28, 48], ["12", "20", "28", "48"])
ratio.minorticks_off()
ratio.set_xlim(10, 80)
ratio.set_xlabel("modes $M$")
ratio.set_ylabel("lift error, per order")
ratio.legend(loc="lower right", fontsize=6.5, handlelength=1.8)
fs.label(ratio, "(c)")
fs.save(figure, "navier_stokes")
