# Scientific PPT Plotting Skill

A reusable workflow for publication-quality scientific figures and clear research-group-meeting slides, with Python/Matplotlib templates.

## Contents

- `SKILL.md`: instructions for an AI coding assistant to create, review, and export scientific figures.
- `references/plotting-standard.md`: practical visual standards for research and presentation plots.
- `scripts/plot_demo.py`: runnable Matplotlib example that exports vector and raster figures.

## Quick start

Requirements: Python 3.9+, NumPy, Matplotlib.

```bash
python -m pip install numpy matplotlib
python scripts/plot_demo.py
```

The demo writes output files to a `figures/` directory by default, including PDF, SVG, and 300-dpi PNG versions.

## Design principles

1. Make the scientific message obvious before adding decoration.
2. Label axes with quantity and units; use consistent symbols and notation.
3. Use readable type, restrained colors, and line styles that remain distinguishable when printed.
4. Show uncertainty and sample size when relevant; state how error bars are defined.
5. Export vector formats for slides and manuscripts, and inspect the final rendered figure.
6. Never distort data, omit inconvenient results, or imply more precision than the data support.

## Suggested workflow

1. Define the question and the one key takeaway.
2. Choose a plot type that matches the data and comparison.
3. Clean and validate data, units, missing values, and uncertainty definitions.
4. Plot with a consistent style and explicit labels.
5. Export PDF/SVG plus PNG preview.
6. Check readability at the actual slide or manuscript size.

See [SKILL.md](SKILL.md) and [the plotting standard](references/plotting-standard.md) for details.
