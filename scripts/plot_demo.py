#!/usr/bin/env python3
"""Presentation-ready illustrative LGAD plots. All data in this demo are synthetic."""
from pathlib import Path
import argparse

import numpy as np
import matplotlib
matplotlib.use("Agg")  # Works on headless servers and in SSH sessions
import matplotlib.pyplot as plt

BLUE = "#0072B2"
VERMILION = "#D55E00"
GREEN = "#009E73"

def apply_style():
    plt.rcParams.update({
        "font.family": "STIXGeneral",
        "mathtext.fontset": "stix",
        "font.size": 16,
        "axes.labelsize": 20,
        "xtick.labelsize": 16,
        "ytick.labelsize": 16,
        "legend.fontsize": 16,
        "axes.linewidth": 1.1,
        "lines.linewidth": 3.0,
        "lines.markersize": 7,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.major.size": 6,
        "ytick.major.size": 6,
        "xtick.minor.size": 3,
        "ytick.minor.size": 3,
        "xtick.top": True,
        "ytick.right": True,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "svg.fonttype": "none",   # Editable text in SVG
        "pdf.fonttype": 42,
    })

def finish(fig, ax, out_dir, stem):
    ax.minorticks_on()
    ax.legend(frameon=False, loc="best")
    fig.tight_layout(pad=0.55)
    for ext in ("png", "svg", "pdf"):
        kwargs = {"dpi": 300} if ext == "png" else {}
        fig.savefig(out_dir / f"{stem}.{ext}", bbox_inches="tight", **kwargs)
    plt.close(fig)

def demo_electric_field(out_dir):
    # SYNTHETIC data for visual demonstration ONLY; not Sentaurus output.
    depth_um = np.linspace(0, 5, 400)
    case_a = 3.0e5 * np.exp(-((depth_um - 1.5) / 0.48)**2)
    case_b = 4.0e5 * np.exp(-((depth_um - 1.6) / 0.52)**2)
    fig, ax = plt.subplots(figsize=(9.4, 5.2))
    ax.plot(depth_um, case_a / 1e5, color=BLUE, label="Case A (illustrative)")
    ax.plot(depth_um, case_b / 1e5, color=VERMILION, linestyle="--",
            label="Case B (illustrative)")
    ax.set_xlabel(r"Depth ($\mu$m)")
    ax.set_ylabel(r"Electric field ($10^{5}$ V/cm)")
    ax.set_xlim(0, 5)
    ax.set_ylim(bottom=0)
    finish(fig, ax, out_dir, "electric_field_demo")

def demo_gain_bias(out_dir):
    # SYNTHETIC data for visual demonstration ONLY; not TCAD predictions.
    voltage_v = np.array([80, 100, 120, 140, 160, 180, 200])
    baseline = np.array([5, 6, 8, 10, 12, 14, 16], dtype=float)
    alternative = np.array([6, 8, 10, 13, 16, 18, 21], dtype=float)
    fig, ax = plt.subplots(figsize=(9.4, 5.2))
    ax.plot(voltage_v, baseline, "o-", color=BLUE, label="Case A (illustrative)")
    ax.plot(voltage_v, alternative, "s--", color=VERMILION,
            label="Case B (illustrative)")
    ax.axhline(20, color=GREEN, linestyle=":", linewidth=2,
               label="Example target: 20")
    ax.set_xlabel("Reverse-bias magnitude (V)")
    ax.set_ylabel("Charge gain")
    ax.set_xlim(75, 205)
    ax.set_ylim(bottom=0)
    finish(fig, ax, out_dir, "gain_bias_demo")

def plot_csv(x, y, filename, xlabel, ylabel, output, label):
    """Example of plotting real values from a two-column CSV with a header.

    The user must provide correct units/physical meanings for axis labels.
    No filtering, interpolation, smoothing, fitting or normalization is done.
    """
    data = np.genfromtxt(filename, delimiter=",", names=True,
                         dtype=float, encoding=None)
    if data.ndim == 0:
        data = np.array([data])
    if x not in data.dtype.names or y not in data.dtype.names:
        raise ValueError(f"Columns not found. Available: {data.dtype.names}")
    xv, yv = data[x], data[y]
    if not np.all(np.isfinite(xv)) or not np.all(np.isfinite(yv)):
        raise ValueError("CSV contains NaN or infinite values; review the source data.")
    fig, ax = plt.subplots(figsize=(9.4, 5.2))
    ax.plot(xv, yv, marker="o", color=BLUE, label=label)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    finish(fig, ax, output, "csv_plot")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="figures", help="Output directory")
    parser.add_argument("--csv", help="Optional real CSV file (first row headers)")
    parser.add_argument("--x", help="X column name in CSV")
    parser.add_argument("--y", help="Y column name in CSV")
    parser.add_argument("--xlabel", help="X axis physical quantity and units")
    parser.add_argument("--ylabel", help="Y axis physical quantity and units")
    parser.add_argument("--label", default="Data", help="Curve legend label")
    args = parser.parse_args()
    apply_style()
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    if args.csv:
        for name in ("x", "y", "xlabel", "ylabel"):
            if not getattr(args, name):
                parser.error("--csv requires --x, --y, --xlabel, --ylabel")
        plot_csv(args.x, args.y, args.csv, args.xlabel, args.ylabel,
                 output, args.label)
    else:
        demo_electric_field(output)
        demo_gain_bias(output)
    print(f"Plots saved in: {output.resolve()}")

if __name__ == "__main__":
    main()
