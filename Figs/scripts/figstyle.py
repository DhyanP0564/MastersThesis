"""The thesis figures' shared style and their access to pihm's results-v1 records.

Every make_*.py script beside this one imports it. Run each with the pihm environment:

    /opt/miniconda3/envs/pihm/bin/python Figs/scripts/make_<name>.py

The records are read through pihm's own selections (pihm.pipeline.results), from the results
directories configs/thesis.yaml names, so a figure reads exactly the records the notebooks, the
reports and numbers.tex read. The colours are pihm.plotting.style's, on a white page.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from pihm.pipeline.results import Results
from pihm.plotting.style import AXIS, GRID, INK, INK_SECONDARY, MUTED, SERIES

FIGS = Path(__file__).resolve().parents[1]
PIHM = Path.home() / "Documents/School/Masters/Research/Code/pihm"

#: The text width of the thesis (A4, 1.5 cm margins), in inches.
WIDTH = 7.0

#: The forms and encodings, as pihm.plotting.style colours them.
STD, PUB, DESC = SERIES[0], SERIES[1], SERIES[2]
COLOUR = {"structured": STD, "standard": STD, "published": PUB, "descriptor": DESC}
MARKER = {"structured": "s", "standard": "s", "published": "^", "descriptor": "o"}
NAME = {
    "published": "Wu et al.'s encoding",
    "structured": "structured encoding",
    "standard": "standard form",
    "descriptor": "descriptor",
}

__all__ = [
    "AXIS", "COLOUR", "DESC", "FIGS", "GRID", "INK", "INK_SECONDARY", "MARKER", "MUTED", "NAME",
    "PUB", "STD", "WIDTH", "apply", "label", "points", "results", "save",
]


def apply() -> None:
    """Set matplotlib to the thesis style: pihm's palette, small type, Computer Modern maths."""
    mpl.rcParams.update(
        {
            "font.size": 8,
            "axes.titlesize": 8.5,
            "axes.labelsize": 8,
            "xtick.labelsize": 7.5,
            "ytick.labelsize": 7.5,
            "legend.fontsize": 7.5,
            "pdf.fonttype": 42,
            "mathtext.fontset": "cm",
            "axes.edgecolor": AXIS,
            "axes.linewidth": 0.7,
            "axes.labelcolor": INK,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "axes.axisbelow": True,
            "grid.color": GRID,
            "grid.linewidth": 0.5,
            "xtick.color": MUTED,
            "ytick.color": MUTED,
            "xtick.labelcolor": INK_SECONDARY,
            "ytick.labelcolor": INK_SECONDARY,
            "lines.linewidth": 1.3,
            "lines.markersize": 4.5,
            "legend.frameon": False,
            "savefig.facecolor": "white",
            "figure.facecolor": "white",
        }
    )


def results() -> Results:
    """Return pihm's campaigns by name, as configs/thesis.yaml collects them."""
    return Results.at(PIHM)


def points(axis, x, y, colour, marker, filled, *, line="-", lw=1.3, label=None, zorder=3):
    """Draw a series as a line through markers, each filled or open by its flag."""
    axis.plot(x, y, color=colour, linestyle=line, linewidth=lw, label=label, zorder=zorder - 1)
    for u, v, f in zip(x, y, filled, strict=True):
        axis.plot(
            u, v, marker=marker, linestyle="none", color=colour,
            markerfacecolor=colour if f else "white", markeredgecolor=colour,
            markeredgewidth=0.9, zorder=zorder,
        )


def label(axis, text: str) -> None:
    """Write a panel's letter, (a), (b), ..., at its top left."""
    axis.set_title(text, loc="left", fontweight="bold")


def save(figure, name: str) -> Path:
    """Save the figure as Figs/<name>.pdf and return the path."""
    out = FIGS / f"{name}.pdf"
    figure.savefig(out, bbox_inches="tight")
    plt.close(figure)
    print(out)
    return out
