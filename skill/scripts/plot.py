# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib>=3.8"]
# ///
"""Plot template for the readable skill.

Copy this file, fill DATA and OUT, pick one of the three functions at the
bottom, then run: uv run plot.py

Every number in DATA must come from the source document. Do not invent points.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- Fill these in -------------------------------------------------------

OUT = Path("assets/doc-name/figure-1.png")

# Line chart: x values and one or more named series.
DATA = {
    "x": [100, 200, 300, 400, 500, 600],
    "x_label": "Load (requests per second)",
    "y_label": "p99 latency (ms)",
    "series": {
        "with cache": [80, 82, 85, 90, 180, 360],
        "without cache": [95, 110, 140, 200, 420, 900],
    },
}

# Bar chart: categories and one or more named series.
BAR_DATA = {
    "categories": ["A", "B", "C"],
    "y_label": "Throughput (ops/s)",
    "series": {"before": [120, 90, 60], "after": [180, 150, 70]},
}

# Histogram: raw values.
HIST_DATA = {
    "values": [],
    "x_label": "Latency (ms)",
    "bins": 20,
}

# ---- Style ----------------------------------------------------------------

PALETTE = ["#2f5d8a", "#c0504d", "#5b8c5a", "#8a6d3b", "#6b5b95"]

plt.rcParams.update(
    {
        "figure.figsize": (7, 4),
        "figure.dpi": 200,
        "font.size": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "axes.prop_cycle": matplotlib.cycler(color=PALETTE),
    }
)


def _finish(fig: plt.Figure) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(OUT)
    print(f"wrote {OUT}")


# ---- Chart shapes ----------------------------------------------------------


def line_chart(d: dict = DATA) -> None:
    """Trend of one or more series over x. Direct labels, no legend, if <= 3 series."""
    fig, ax = plt.subplots()
    for name, ys in d["series"].items():
        ax.plot(d["x"], ys, marker="o", markersize=3, linewidth=1.6)
        if len(d["series"]) <= 3:
            ax.annotate(
                name,
                (d["x"][-1], ys[-1]),
                xytext=(6, 0),
                textcoords="offset points",
                va="center",
            )
    if len(d["series"]) > 3:
        ax.legend(frameon=False)
    ax.set_xlabel(d["x_label"])
    ax.set_ylabel(d["y_label"])
    ax.margins(x=0.12)
    _finish(fig)


def bar_chart(d: dict = BAR_DATA) -> None:
    """Compare a few values across categories. Grouped bars if several series."""
    fig, ax = plt.subplots()
    n = len(d["series"])
    width = 0.8 / n
    for i, (name, ys) in enumerate(d["series"].items()):
        xs = [j + (i - (n - 1) / 2) * width for j in range(len(d["categories"]))]
        bars = ax.bar(xs, ys, width=width, label=name)
        ax.bar_label(bars, padding=2, fontsize=8)
    ax.set_xticks(range(len(d["categories"])), d["categories"])
    ax.set_ylabel(d["y_label"])
    if n > 1:
        ax.legend(frameon=False)
    ax.grid(axis="x", visible=False)
    _finish(fig)


def histogram(d: dict = HIST_DATA) -> None:
    """Distribution of raw values."""
    fig, ax = plt.subplots()
    ax.hist(d["values"], bins=d["bins"], edgecolor="white")
    ax.set_xlabel(d["x_label"])
    ax.set_ylabel("Count")
    _finish(fig)


if __name__ == "__main__":
    line_chart()
