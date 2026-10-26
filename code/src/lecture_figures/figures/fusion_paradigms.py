"""Early, intermediate and late fusion of two modalities (EHR and ECG)."""

from lecture_figures import diagram as d
from lecture_figures import style

NAME = "fusion_paradigms"


def inputs(ax, y):
    d.box(ax, 1.9, y + 0.1, 1.0, 0.4, "EHR", d.EHR)
    d.box(ax, 1.9, y - 0.5, 1.0, 0.4, "ECG", d.ECG)


def output(ax, x, y):
    d.arrow(ax, x, y, 8.6, y)
    ax.text(8.7, y, "prediction", va="center", fontsize=8)


def make() -> None:
    fig, ax = style.figure(height_ratio=0.42)
    d.canvas(ax, 9.8, 4.2)
    rows = {"Early": 3.4, "Intermediate": 2.0, "Late": 0.6}
    for name, y in rows.items():
        ax.text(0.0, y, name, ha="left", va="center", fontsize=9, weight="bold")

    y = rows["Early"]
    inputs(ax, y)
    d.box(ax, 3.9, y - 0.25, 1.5, 0.5, "join features", d.FUSED)
    d.box(ax, 6.3, y - 0.25, 1.5, 0.5, "one model", d.MODEL, "black")
    d.arrow(ax, 2.9, y + 0.3, 3.9, y)
    d.arrow(ax, 2.9, y - 0.3, 3.9, y)
    d.arrow(ax, 5.4, y, 6.3, y)
    output(ax, 7.8, y)

    y = rows["Intermediate"]
    inputs(ax, y)
    d.box(ax, 3.3, y + 0.1, 1.2, 0.4, "encoder", d.MODEL, "black")
    d.box(ax, 3.3, y - 0.5, 1.2, 0.4, "encoder", d.MODEL, "black")
    d.box(ax, 5.1, y - 0.25, 1.4, 0.5, "combine", d.FUSED)
    d.box(ax, 7.0, y - 0.25, 0.9, 0.5, "head", d.MODEL, "black")
    for dy in (0.3, -0.3):
        d.arrow(ax, 2.9, y + dy, 3.3, y + dy)
        d.arrow(ax, 4.5, y + dy, 5.1, y)
    d.arrow(ax, 6.5, y, 7.0, y)
    output(ax, 7.9, y)
    ax.text(5.8, y - 0.5, "concatenate, add, gate, attend", ha="center", va="top", fontsize=7,
            color=style.TEXT_SECONDARY)

    y = rows["Late"]
    inputs(ax, y)
    d.box(ax, 3.3, y + 0.1, 1.6, 0.4, "EHR model", d.MODEL, "black")
    d.box(ax, 3.3, y - 0.5, 1.6, 0.4, "ECG model", d.MODEL, "black")
    d.box(ax, 5.8, y - 0.25, 2.0, 0.5, "combine predictions", d.FUSED)
    for dy in (0.3, -0.3):
        d.arrow(ax, 2.9, y + dy, 3.3, y + dy)
        d.arrow(ax, 4.9, y + dy, 5.8, y)
    output(ax, 7.8, y)
    style.save(fig, NAME)


if __name__ == "__main__":
    style.apply_style()
    make()
