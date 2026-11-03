"""Plot a readings CSV. Usage: python tools/plot_readings.py readings.csv out.png
Needs matplotlib: pip install matplotlib
"""
import csv
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


def load(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def column(rows, name):
    xs, ys = [], []
    for r in rows:
        if r.get(name, "") != "":
            xs.append(float(r["uptime_s"]) / 3600.0)
            ys.append(float(r[name]))
    return xs, ys


def main(src, dst):
    rows = load(src)
    if not rows:
        sys.exit("No rows in " + src)
    fig, axes = plt.subplots(2, 1, sharex=True, figsize=(8, 5))
    for ax, name, label in ((axes[0], "soil_moisture_pct", "Soil moisture (%)"),
                            (axes[1], "air_temp_c", "Air temperature (C)")):
        xs, ys = column(rows, name)
        ax.plot(xs, ys, marker="o", linewidth=1)
        ax.set_ylabel(label)
        ax.grid(True, alpha=0.3)
    axes[1].set_xlabel("Hours since the board started")
    fig.tight_layout()
    fig.savefig(dst, dpi=150)
    print("Saved", dst)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
