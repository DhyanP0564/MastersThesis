"""fig:verification-accuracy -- verification error of every circuit, by mode, and R2a's cx per query.

(a) verify_max_error against n_qubits_total for every verified encode and lift record of
results-v1 (construction-only records carry no error), marker by mode, colour by encoding, with
each mode's tolerance dashed. (b) Transpiled two-qubit gates per query of the reflection against
n on R2a, structured standard and descriptor forms. As notebook 20_circuits_exact selects them.

Run with the pihm environment:  /opt/miniconda3/envs/pihm/bin/python Figs/scripts/make_verification_accuracy.py
"""

from collections import Counter

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

import figstyle as fs

fs.apply()
results = fs.results()
LIFT = fs.INK_SECONDARY
records = []  # (encoding, mode, qubits, error)
for campaign in ("p3_pillar1", "p5_encode", "p6_encode", "p7_encode", "p7_lift"):
    for r in results.rows(campaign):
        if r["status"] != "ok" or r["verify_mode"] in ("none", "") or r["verify_max_error"] == "":
            continue
        encoding = "lift" if campaign == "p7_lift" else ("structured" if r["regime"] == "standard" else "descriptor")
        records.append((encoding, r["verify_mode"], int(r["n_qubits_total"]), float(r["verify_max_error"]),
                        float(r["verify_tolerance"])))
print(Counter((e, m) for e, m, *_ in records))
print("worst error/tolerance", max(err / tol for *_, err, tol in records))
FLOOR = 1e-17  # an exact zero is drawn here
STYLE = {"exact": ("o", True), "probe": ("o", False), "ir": ("x", True)}
COLOUR = {"structured": fs.STD, "descriptor": fs.DESC, "lift": LIFT}

figure, (scatter, gates) = plt.subplots(1, 2, figsize=(fs.WIDTH, 2.7), width_ratios=[1.7, 1], constrained_layout=True)
for encoding, mode, qubits, error, _ in records:
    marker, filled = STYLE[mode]
    colour = COLOUR[encoding]
    scatter.plot(qubits, max(error, FLOOR), marker=marker, linestyle="none", color=colour,
                 markerfacecolor=colour if filled else "white", markeredgewidth=0.8, markersize=4, alpha=0.85)
for level, text in ((1e-10, r"exact ($10^{-10}\|X\|$) and IR tolerance"), (1e-9, "probe tolerance")):
    scatter.axhline(level, color=fs.MUTED, linestyle=(0, (4, 2)), linewidth=0.8)
    scatter.text(53, level * 1.4, text, ha="right", va="bottom", fontsize=6.5, color=fs.MUTED)
scatter.set_yscale("log")
scatter.set_ylim(FLOOR / 3, 1e-8)
scatter.text(53, FLOOR * 1.8, "exactly zero", ha="right", va="bottom", fontsize=6.5, color=fs.MUTED)
scatter.set_xlabel("circuit width (qubits)")
scatter.set_ylabel("largest error against the operator")
scatter.legend(handles=[
    Line2D([], [], color=fs.STD, marker="s", linestyle="none", label="structured standard form"),
    Line2D([], [], color=fs.DESC, marker="s", linestyle="none", label="descriptor"),
    Line2D([], [], color=LIFT, marker="s", linestyle="none", label="Carleman lift coupling"),
    Line2D([], [], color=fs.INK, marker="o", linestyle="none", markersize=4, label="exact"),
    Line2D([], [], color=fs.INK, marker="o", markerfacecolor="white", linestyle="none", markersize=4, label="probe"),
    Line2D([], [], color=fs.INK, marker="x", linestyle="none", markersize=4, label="IR"),
], loc="center right", bbox_to_anchor=(1.0, 0.43), ncols=2, fontsize=6.5, columnspacing=0.8, handletextpad=0.3)
fs.label(scatter, "(a)")

for campaign, form in (("p3_pillar1", "standard"), ("p5_encode", "descriptor")):
    rows = sorted((r for r in results.rows(campaign) if r["problem"] == "R2a" and r["variant"] == "corrected"
                   and r["status"] == "ok"), key=lambda r: r["n"])
    fs.points(gates, [r["n"] for r in rows], [r["cx_count"] for r in rows], fs.COLOUR[form], fs.MARKER[form],
              [True] * len(rows), label={"standard": "structured standard form", "descriptor": "descriptor"}[form])
gates.set_xticks([2, 3, 4, 5])
gates.set_ylim(0, None)
gates.set_xlabel("$n$")
gates.set_ylabel("two-qubit gates per query")
gates.legend(loc="lower right")
gates.set_title("R2a, the reflection", loc="right", fontsize=8, color=fs.INK_SECONDARY)
fs.label(gates, "(b)")
fs.save(figure, "verification_accuracy")
