"""fig:gap-cases -- the ideal-bound reversals: degree against N on R3a, R5b and R5a.

Both forms' minimax degree as built (solid) and at alpha_R = ||R|| (dashed), at the resolutions
whose reference is trusted in both forms; T2 filled where the preparation was emulated, T3 open
beyond. Data as notebook 43_representative_problems selects it.

Run with the pihm environment:  /opt/miniconda3/envs/pihm/bin/python Figs/scripts/make_gap_cases.py
"""

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pihm.pipeline.results import primary_preparations, reference_builds
from pihm.pipeline.summary import cases

import figstyle as fs

fs.apply()
results = fs.results()
PANELS = (("R3a", "R3a, Legendre"), ("R5b", "R5b, heat"), ("R5a", "R5a, Laplace"))
FORMS = ("standard", "descriptor")
builds = {
    "standard": reference_builds(results.rows("p2_reproduction")),
    "descriptor": reference_builds(results.rows("p5_build")),
}
estimates = {f: cases(results.rows("p5_t3", regime=f), variant="corrected") for f in FORMS}
emulated = {
    f: {(r["problem"], r["n"]) for r in primary_preparations(results.rows("p5_stateprep", regime=f))}
    for f in FORMS
}

figure, axes = plt.subplots(1, 3, figsize=(fs.WIDTH, 2.3), constrained_layout=True)
for axis, (problem, title), letter in zip(axes, PANELS, "abc", strict=True):
    trusted = sorted(
        n for (p, v, n), r in estimates["standard"].items()
        if p == problem and all(builds[f].get((p, "corrected", n), {}).get("trusted") is True for f in FORMS)
    )
    for form in FORMS:
        colour, marker = fs.COLOUR[form], fs.MARKER[form]
        rows = [estimates[form][(problem, "corrected", n)] for n in trusted]
        N = [2 ** n for n in trusted]
        fs.points(axis, N, [r["degree"] for r in rows], colour, marker,
                  [(problem, n) in emulated[form] for n in trusted])
        axis.plot(N, [r["ideal_degree"] for r in rows], color=colour, linestyle=(0, (4, 2)), linewidth=1.0)
    axis.set_xscale("log", base=2)
    axis.set_yscale("log")
    axis.set_xticks(N, [rf"$2^{{{n}}}$" for n in trusted])
    axis.minorticks_off()
    axis.set_xlabel(r"$N = 2^n$" + (" per axis" if problem.startswith("R5") else ""))
    axis.margins(x=0.1)
    fs.label(axis, f"({letter})")
    axis.set_title(title, loc="right", fontsize=8, color=fs.INK_SECONDARY)
axes[0].set_ylabel(r"filter degree $d$")

handles = [Line2D([], [], color=fs.COLOUR[f], marker=fs.MARKER[f], label=fs.NAME[f]) for f in FORMS]
handles += [
    Line2D([], [], color=fs.INK_SECONDARY, label="as built"),
    Line2D([], [], color=fs.INK_SECONDARY, linestyle=(0, (4, 2)), linewidth=1.0, label=r"ideal bound $\alpha_R=\|R\|_2$"),
    Line2D([], [], color=fs.INK_SECONDARY, marker="o", linestyle="none", label="T2 (emulated)"),
    Line2D([], [], color=fs.INK_SECONDARY, marker="o", markerfacecolor="white", linestyle="none", label="T3 (estimated)"),
]
figure.legend(handles=handles, loc="outside upper center", ncols=6, columnspacing=1.2, handlelength=1.8)
fs.save(figure, "gap_cases")
