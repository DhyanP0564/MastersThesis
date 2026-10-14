"""fig:sparsity -- spy plots of R_std and R_desc for R2a (f'' + 4f' + 4f = 0) at n = 4.

Run with the pihm environment:  /opt/miniconda3/envs/pihm/bin/python Figs/scripts/make_sparsity.py
Reads nothing from results-v1: both residuals are assembled exactly as the pipeline assembles them.
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse as sp

from pihm.assemble import assemble
from pihm.problems.ladder import problem

OUT = Path(__file__).resolve().parents[1] / "sparsity.pdf"
N = 4
INK, MUTED = "#0b0b0b", "#898781"
STD, DESC = "#2a78d6", "#1baf7a"  # standard form slot 1, descriptor slot 3 (pihm.plotting.style)

mpl.rcParams.update({"font.size": 8, "pdf.fonttype": 42, "mathtext.fontset": "cm"})


def stacked(regime):
    """Return R with its identically zero rows dropped, and the row bands (label, start, stop)."""
    res = assemble(problem("R2a"), N, regime=regime)
    pieces, bands = [], []
    for block in res.blocks:
        m = sp.csr_array(block.matrix)
        m.eliminate_zeros()
        m = sp.csr_array(m[np.flatnonzero(np.diff(m.indptr))])
        if m.shape[0]:
            start = bands[-1][2] if bands else 0
            bands.append((block.kind, start, start + m.shape[0]))
            pieces.append(m)
    return sp.csr_array(sp.vstack(pieces, format="csr")), bands, res


def merge(bands):
    out = []
    for kind, a, b in bands:
        if out and out[-1][0] == kind:
            out[-1] = (kind, out[-1][1], b)
        else:
            out.append((kind, a, b))
    return out


LABEL = {"equation": "equation", "recurrence": "recurrences", "padding": "padding",
         "constraint": "constraints"}
fig, axes = plt.subplots(1, 2, figsize=(6.4, 3.5), gridspec_kw={"width_ratios": [1, 4]})
for ax, regime, colour, name in (
    (axes[0], "standard", STD, r"$R_{\mathrm{std}}$"),
    (axes[1], "descriptor", DESC, r"$R_{\mathrm{desc}}$"),
):
    R, bands, res = stacked(regime)
    h, w = R.shape
    c = R.tocoo()
    ax.scatter(c.col + 0.5, c.row + 0.5, s=5.5, marker="s", color=colour, linewidths=0)
    ax.set_xlim(0, w)
    ax.set_ylim(h, 0)
    ax.set_aspect("equal")
    for _, a, _b in merge(bands)[1:]:
        ax.axhline(a, color=MUTED, lw=0.6)
    nblocks = len(res.derivatives)
    for j in range(1, nblocks):
        ax.axvline(j * w / nblocks, color=MUTED, lw=0.6)
    ax.set_yticks([(a + b) / 2 for _, a, b in merge(bands)],
                  [LABEL[k] for k, _, _ in merge(bands)], fontsize=7)
    if regime == "standard":
        ax.set_xticks([w / 2], [r"$f$"])
    else:
        ax.set_xticks([(j + 0.5) * w / nblocks for j in range(nblocks)],
                      [r"$f$", r"$f'$", r"$f''$", "pad"][:nblocks])
    ax.xaxis.tick_top()
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_linewidth(0.6)
        s.set_color(MUTED)
    ax.set_xlabel(f"{name}: ${h}\\times{w}$, {R.nnz} nonzeros ({R.nnz / (h * w):.0%})",
                  color=INK, fontsize=8)
fig.tight_layout()
fig.savefig(OUT, bbox_inches="tight")
print(OUT)
