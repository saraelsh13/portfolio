"""Optional chart rendering: pip install matplotlib, then python plot_results.py."""
import csv
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent
rows = list(csv.DictReader((ROOT / "results/summary.csv").open()))
plt.rcParams.update({"svg.fonttype": "none", "font.size": 10})
fig, axes = plt.subplots(1, 3, figsize=(13, 4), layout="constrained")
panels = [("in_class", "accuracy", "True rule included", "Held-out accuracy"),
          ("omitted_rule", "accuracy", "True rule omitted", "Held-out accuracy"),
          ("omitted_rule", "false_certainty_rate", "True rule omitted", "Unanimous wrong predictions / all test points")]
for ax, (condition, metric, title, label) in zip(axes, panels):
    for strategy, color in [("fixed", "#64748b"), ("random", "#d97706"),
                            ("disagreement", "#2563eb")]:
        data = [r for r in rows if r["condition"] == condition and r["strategy"] == strategy]
        ax.plot([int(r["budget"]) for r in data], [float(r[metric]) for r in data],
                marker="o", label=strategy, color=color)
    ax.set(title=title, xlabel="Label queries", ylabel=label, ylim=(0, 1.05))
    ax.grid(alpha=0.15)
axes[0].legend(frameon=False)
fig.suptitle("Which Question Next?  |  100 paired synthetic trials per condition\nDescriptive means; finite rule space; no learning across trials", fontsize=12)
fig.savefig(ROOT / "results/overview.svg", metadata={"Date": None})
fig.savefig(ROOT / "results/overview.png", dpi=150)
