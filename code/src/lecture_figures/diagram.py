"""Small drawing helpers for schematic figures (boxes, arrows, vectors)."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from lecture_figures import style

EHR = style.COLOURS[1]
ECG = style.COLOURS[0]
FUSED = style.COLOURS[2]
MODEL = "#d9d8d3"


def canvas(ax, width, height):
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis("off")


def box(ax, x, y, w, h, text, colour, text_colour="white", fontsize=8):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                fc=colour, ec="none"))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fontsize, color=text_colour)


def arrow(ax, x0, y0, x1, y1):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=style.TEXT_SECONDARY, lw=0.8))


def vector(ax, x, y, values, colour, cell=0.18, h=0.3):
    """Draw a vector as a strip of cells, shaded by value in [0, 1]. Returns the end x."""
    for i, v in enumerate(values):
        ax.add_patch(plt.Rectangle((x + i * cell, y), cell * 0.92, h, fc=colour,
                                   alpha=0.25 + 0.75 * float(v), ec="none"))
    return x + len(values) * cell
