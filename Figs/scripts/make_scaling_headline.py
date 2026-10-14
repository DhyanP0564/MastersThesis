"""fig:scaling-headline -- looseness, relative gap and filter degree against N on R2a.

(a) alpha_H/||H|| per encoding, (b) Delta/||H|| per Hamiltonian, (c) the minimax filter's degree
as built (solid) and at the ideal-encoding bound alpha_R = ||R|| (dashed); T2 filled where the
preparation was emulated, T3 open beyond. Data as notebook 40_where_the_cost_lies selects it.

Run with the pihm environment:  /opt/miniconda3/envs/pihm/bin/python Figs/scripts/make_scaling_headline.py
"""

import math

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pihm.pipeline.results import encoding_scaling, primary_preparations
from pihm.pipeline.summary import cases, encoder_of

import figstyle as fs

fs.apply()
results = fs.results()
standard_builds, descriptor_builds = results.rows("p2_reproduction"), results.rows("p5_build")
encoders = results.rows("p5_encoders")
estimates = {
    "structured": [r for r in encoders if encoder_of(r) == "structured"],
    "published": [r for r in encoders if encoder_of(r) == "published"],
    "descriptor": results.rows("p5_t3", regime="descriptor"),
}
table = encoding_scaling(
    {
        "published": (estimates["published"], standard_builds, []),
        "structured": (
            estimates["structured"],
            standard_builds,
            primary_preparations(results.rows("p5_stateprep", regime="standard")),
        ),
        "descriptor": (
            estimates["descriptor"],
            descriptor_builds,
            primary_preparations(results.rows("p5_stateprep", regime="descriptor")),
        ),
    },
    problem="R2a",
    variant="corrected",
)
ideal = {
    name: {n: float(r["ideal_degree"]) for (_, _, n), r in cases(rows, problem="R2a", variant="corrected").items()}
    for name, rows in estimates.items()
}
series = {
    name: sorted((r for r in table if r["encoding"] == name), key=lambda r: r["n"])
    for name in ("published", "structured", "descriptor")
}


def slope(axis, rows, ys, colour, *, above=True):
    """Annotate a series' growth, the exponent of N between n = 7 and 8 (Table 8.1's), at its last point."""
    pts = [(2 ** r["n"], y) for r, y in zip(rows, ys, strict=True) if r["n"] in (7, 8)]
    p = math.log2(pts[1][1] / pts[0][1])
    axis.annotate(
        rf"$N^{{{p:.2g}}}$" if abs(p) < 1 else rf"$N^{{{p:.1f}}}$", xy=pts[-1], xytext=(4, 3 if above else -3), textcoords="offset points",
        va="bottom" if above else "top", ha="left", fontsize=7, color=colour,
    )


figure, axes = plt.subplots(1, 3, figsize=(fs.WIDTH, 2.45), constrained_layout=True)
loose, gap, degree = axes
for name, rows in series.items():
    colour, marker = fs.COLOUR[name], fs.MARKER[name]
    N = [2 ** r["n"] for r in rows]
    values = [r["looseness"] for r in rows]
    fs.points(loose, N, values, colour, marker, [True] * len(rows))
    slope(loose, rows, values, colour, above=name != "descriptor")
    if name != "published":  # Wu et al.'s and the structured encoding encode the same H_std
        values = [r["relative_gap"] for r in rows]
        fs.points(gap, N, values, colour, marker, [True] * len(rows))
        slope(gap, rows, values, colour, above=name == "descriptor")
    values = [r["degree"] for r in rows]
    fs.points(degree, N, values, colour, marker, [r["measured_degree"] is not None for r in rows])
    slope(degree, rows, values, colour)
    if name != "published":
        values = [ideal[name][r["n"]] for r in rows]
        degree.plot(N, values, color=colour, linestyle=(0, (4, 2)), linewidth=1.0)
        slope(degree, rows, values, colour, above=False)

loose.set_ylabel(r"looseness $\alpha_H/\|H\|$")
gap.set_ylabel(r"relative gap $\Delta/\|H\|$")
degree.set_ylabel(r"filter degree $d$")
for axis, letter in zip(axes, "abc", strict=True):
    axis.set_xscale("log", base=2)
    axis.set_yscale("log")
    axis.set_xlabel(r"$N = 2^n$")
    axis.margins(x=0.08)
    axis.set_xlim(right=2 ** 8 * 2.6)
    fs.label(axis, f"({letter})")
gap.text(2 ** 2.2, 1e-15, r"$H_{\mathrm{std}}$", color=fs.STD, fontsize=7.5)
gap.text(2 ** 6, 3e-4, r"$H_{\mathrm{desc}}$", color=fs.DESC, fontsize=7.5)

handles = [Line2D([], [], color=fs.COLOUR[k], marker=fs.MARKER[k], label=fs.NAME[k]) for k in series]
handles += [
    Line2D([], [], color=fs.INK_SECONDARY, label="as built"),
    Line2D([], [], color=fs.INK_SECONDARY, linestyle=(0, (4, 2)), linewidth=1.0, label=r"ideal bound $\alpha_R=\|R\|_2$"),
    Line2D([], [], color=fs.INK_SECONDARY, marker="o", linestyle="none", label="T2 (emulated)"),
    Line2D([], [], color=fs.INK_SECONDARY, marker="o", markerfacecolor="white", linestyle="none", label="T3 (estimated)"),
]
figure.legend(handles=handles, loc="outside upper center", ncols=4)
fs.save(figure, "scaling_headline")
