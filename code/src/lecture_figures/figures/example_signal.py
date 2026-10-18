"""Example figure: a noisy sinusoid and its moving-average estimate."""

import numpy as np

from lecture_figures import style

NAME = "example_signal"


def make() -> None:
    rng = np.random.default_rng(0)
    t = np.linspace(0, 2, 400)
    clean = np.sin(2 * np.pi * 1.5 * t)
    noisy = clean + 0.4 * rng.standard_normal(t.size)
    window = 15
    smoothed = np.convolve(noisy, np.ones(window) / window, mode="same")

    fig, ax = style.figure()
    ax.plot(t, noisy, color=style.COLOURS[0], alpha=0.35, linewidth=1, label="Measured")
    ax.plot(t, smoothed, color=style.COLOURS[1], label=f"Moving average ($K={window}$)")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.legend(loc="lower right", bbox_to_anchor=(1, 1), ncol=2)
    style.save(fig, NAME)


if __name__ == "__main__":
    style.apply_style()
    make()
