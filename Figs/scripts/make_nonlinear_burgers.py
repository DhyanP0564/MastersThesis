"""fig:nonlinear-burgers -- convergence of the Carleman lift on Burgers (R9) and R8.

(a) R9's lift error against the Galerkin system against the order K, a line per a/nu, on M = 4
(filled) and 16 (open) sine modes, at each order's finest time axis. (b) R8's field error
against n_t, a line per K. Descriptor builds, as notebooks 61_carleman_lift and 62_burgers select.

Run with the pihm environment:  /opt/miniconda3/envs/pihm/bin/python Figs/scripts/make_nonlinear_burgers.py
"""

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pihm.plotting.style import SEQUENTIAL
from pihm.problems import ladder

import figstyle as fs

fs.apply()
results = fs.results()
builds = [r for r in results.rows("p6_build") if r["status"] == "ok" and not r["label"] and r["regime"] == "descriptor"]
STRENGTHS = sorted(ladder.R9_STRENGTHS.values())
RAMP = SEQUENTIAL[2:]  # five steps, light to dark


def finest(rows):
    """Return each (problem, K)'s record at its finest time axis."""
    found = {}
    for r in rows:
        key = (r["problem"], r["carleman"])
        if key not in found or r["n"] > found[key]["n"]:
            found[key] = r
    return found


figure, (lift, field) = plt.subplots(1, 2, figsize=(fs.WIDTH, 2.6), constrained_layout=True)
burgers = finest(r for r in builds if r["rung"] == "R9")
for strength, colour in zip(STRENGTHS, RAMP, strict=True):
    for modes in (4, 16):
        rows = sorted((r for (p, _), r in burgers.items() if ladder.burgers_panel(p) == (strength, modes)),
                      key=lambda r: r["carleman"])
        K, err = [r["carleman"] for r in rows], [r["lift_err_linf"] for r in rows]
        if modes == 4:
            fs.points(lift, K, err, colour, "o", [True] * len(rows), lw=1.1)
        else:  # rings round M = 4's markers: the two coincide
            lift.plot(K, err, "o", markersize=8, markerfacecolor="none", markeredgecolor=colour,
                      markeredgewidth=0.9, zorder=5)
    last = max((r for (p, _), r in burgers.items() if ladder.burgers_panel(p) == (strength, 4)),
               key=lambda r: r["carleman"])
    lift.annotate(rf"$a/\nu={strength:g}$", xy=(last["carleman"], last["lift_err_linf"]), xytext=(6, 0),
                  textcoords="offset points", va="center", fontsize=7, color=colour)
lift.set_yscale("log")
lift.set_xticks(range(2, 6))
lift.set_xlim(1.8, 6.1)
lift.set_xlabel(r"Carleman order $K$")
lift.set_ylabel(r"lift error ($L^\infty$, against Galerkin)")
lift.legend(handles=[
    Line2D([], [], color=fs.INK_SECONDARY, marker="o", label=r"$M=4$"),
    Line2D([], [], color=fs.INK_SECONDARY, marker="o", markersize=8, markerfacecolor="none", linestyle="none", label=r"$M=16$"),
], loc="lower left")
fs.label(lift, "(a)")

r8 = [r for r in builds if r["problem"] == "R8"]
orders = sorted({r["carleman"] for r in r8})
for order, colour in zip(orders, RAMP, strict=True):
    rows = sorted((r for r in r8 if r["carleman"] == order), key=lambda r: r["n"])
    fs.points(field, [r["n"] for r in rows], [r["field_err_linf"] for r in rows], colour, "o", [True] * len(rows), lw=1.1)
    field.annotate(rf"$K={order}$", xy=(rows[-1]["n"], rows[-1]["field_err_linf"]), xytext=(6, 0),
                   textcoords="offset points", va="center", fontsize=7, color=colour)
field.set_yscale("log")
field.set_xlim(2.7, 9.0)
field.set_xlabel(r"time-axis qubits $n_t$")
field.set_ylabel(r"field error ($L^\infty$)")
fs.label(field, "(b)")
field.set_title(r"R8: $y'=-y+y^2$", loc="right", fontsize=8, color=fs.INK_SECONDARY)
lift.set_title("R9: viscous Burgers", loc="right", fontsize=8, color=fs.INK_SECONDARY)
fs.save(figure, "nonlinear_burgers")
