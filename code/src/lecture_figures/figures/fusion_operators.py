"""Ways to combine two embeddings: concatenation, addition, gating, attention, shared space."""

import matplotlib.pyplot as plt
import numpy as np

from lecture_figures import diagram as d
from lecture_figures import style

NAME = "fusion_operators"


def make() -> None:
    rng = np.random.default_rng(1)
    h_ehr, h_ecg = rng.uniform(0, 1, 4), rng.uniform(0, 1, 4)
    gate = rng.uniform(0, 1, 4)
    cell = 0.16
    fig, axes = plt.subplots(1, 5, figsize=(style.TEXT_WIDTH_IN, 1.9))
    titles = ["Concatenation", "Addition", "Gating", "Attention", "Shared space"]
    for ax, title in zip(axes, titles):
        d.canvas(ax, 1.5, 3.0)
        ax.set_title(title, fontsize=8)
    note = dict(ha="center", va="top", fontsize=6.5, color=style.TEXT_SECONDARY)

    for ax in axes[:3]:
        d.vector(ax, 0.1, 2.35, h_ehr, d.EHR, cell=cell, h=0.25)
        d.vector(ax, 0.1, 1.85, h_ecg, d.ECG, cell=cell, h=0.25)

    ax = axes[0]
    end = d.vector(ax, 0.1, 0.9, h_ehr, d.EHR, cell=cell, h=0.25)
    d.vector(ax, end, 0.9, h_ecg, d.ECG, cell=cell, h=0.25)
    ax.text(0.75, 0.7, "twice as long", **note)

    ax = axes[1]
    d.vector(ax, 0.1, 0.9, (h_ehr + h_ecg) / 2, d.FUSED, cell=cell, h=0.25)
    ax.text(0.75, 0.7, "same size", **note)

    ax = axes[2]
    d.vector(ax, 0.1, 1.4, gate, style.TEXT_SECONDARY, cell=cell, h=0.18)
    d.vector(ax, 0.1, 0.9, gate * h_ehr + (1 - gate) * h_ecg, d.FUSED, cell=cell, h=0.25)
    ax.text(0.75, 0.7, "gate $g$ mixes\nper feature", **note)

    ax = axes[3]
    d.box(ax, 0.05, 2.3, 0.6, 0.35, "EHR", d.EHR, fontsize=7)
    d.box(ax, 0.85, 2.3, 0.6, 0.35, "ECG", d.ECG, fontsize=7)
    ax.bar([0.35, 1.15], [0.65, 0.35], width=0.4, bottom=1.35, color=[d.EHR, d.ECG], alpha=0.6)
    d.box(ax, 0.25, 0.85, 1.0, 0.3, "weighted sum", d.FUSED, fontsize=6.5)
    ax.text(0.75, 0.7, "weights depend\non the input", **note)

    ax = axes[4]
    centres = np.array([[0.4, 2.3], [1.1, 2.4], [0.5, 1.4], [1.2, 1.5]])
    for px, py in centres + rng.normal(0, 0.08, centres.shape):
        ax.scatter(px, py, color=d.ECG, s=14, zorder=3)
        ax.scatter(px + 0.1, py - 0.08, color=d.EHR, s=14, marker="s", zorder=3)
        ax.plot([px, px + 0.1], [py, py - 0.08], color=style.TEXT_SECONDARY, lw=0.6)
    ax.text(0.75, 0.7, "matching pairs\ntrained to be close", **note)

    plt.tight_layout(w_pad=0.2)
    style.save(fig, NAME)


if __name__ == "__main__":
    style.apply_style()
    make()
