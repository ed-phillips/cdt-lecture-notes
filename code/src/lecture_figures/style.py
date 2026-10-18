"""Shared plotting style so every figure matches the typeset notes."""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

REPO_ROOT = Path(__file__).resolve().parents[3]
OUTPUT_DIR = REPO_ROOT / "figures" / "generated"

# Text width of lecture_notes.tex: A4 (21cm) minus 2.5cm margins either side.
TEXT_WIDTH_IN = 16.0 / 2.54

# Categorical colours, assigned in this fixed order (never cycled).
COLOURS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]
TEXT = "#0b0b0b"
TEXT_SECONDARY = "#52514e"
GRID = "#e4e3df"


def apply_style() -> None:
    """Use the document font (Computer/Latin Modern) and recessive axes for all plots."""
    mpl.rcParams.update(
        {
            # cmr10 (Computer Modern) ships with matplotlib and matches the
            # document's Latin Modern. It lacks a unicode minus sign, so tick
            # labels are rendered with mathtext instead.
            "font.family": "serif",
            "font.serif": ["cmr10"],
            "axes.formatter.use_mathtext": True,
            "mathtext.fontset": "cm",
            "font.size": 10,
            "axes.titlesize": 10,
            "axes.labelsize": 10,
            "legend.fontsize": 9,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
            "text.color": TEXT,
            "axes.labelcolor": TEXT_SECONDARY,
            "axes.edgecolor": TEXT_SECONDARY,
            "xtick.color": TEXT_SECONDARY,
            "ytick.color": TEXT_SECONDARY,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.color": GRID,
            "grid.linewidth": 0.6,
            "axes.prop_cycle": mpl.cycler(color=COLOURS),
            "lines.linewidth": 1.5,
            "legend.frameon": False,
            "figure.dpi": 150,
            "savefig.bbox": "tight",
            "pdf.fonttype": 42,
        }
    )


def figure(height_ratio: float = 0.45, width_fraction: float = 1.0, **kwargs):
    """Create a figure sized to (a fraction of) the document text width."""
    width = TEXT_WIDTH_IN * width_fraction
    return plt.subplots(figsize=(width, width * height_ratio), **kwargs)


def save(fig, name: str) -> Path:
    """Save a figure as figures/generated/<name>.pdf, ready for \\includegraphics."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / f"{name}.pdf"
    fig.savefig(path)
    plt.close(fig)
    return path
