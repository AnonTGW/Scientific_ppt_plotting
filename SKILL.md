---
name: scientific-ppt-plotting
description: Create clear, reproducible, presentation-ready scientific plots using Python and Matplotlib, especially for LGAD/Sentaurus TCAD, Geant4, ROOT, and physics group meetings.
---

# Scientific PPT Plotting

Use this skill whenever the user requests scientific plots, presentation figures, or visual cleanup of plots intended for a research group meeting or PowerPoint.

## Purpose

Generate readable, accurate, reproducible scientific figures for 16:9 research presentations. Prioritize scientifically honest visualization and a single clear finding per slide.

## Required workflow

1. Identify the scientific question, the data source, each column's physical meaning and units, the comparison groups, and intended slide layout (full-width or side by side).
2. Inspect data shape, units, missing values, sign conventions, event counts, ranges, and outliers **before** plotting. Do not silently discard data.
3. Choose the correct representation: line plot for continuous profiles, markers/error bars for independent measurements, histogram for distributions, signed/net-doping plot for donor-minus-acceptor concentrations, and log/symlog scales when justified.
4. Apply the defaults in `references/plotting-standard.md`; adapt legibility to the *actual size* in the slide. Keep mapping of variables to colors/linestyles consistent between figures.
5. Use Python/NumPy/Matplotlib for the plotting script. Prefer the reusable demo in `scripts/plot_demo.py`. Keep raw data separate from plotting code.
6. Label all axes with quantities and units. Define error bars, bias conditions, normalization, and physical assumptions in captions or accompanying notes where needed.
7. Export editable/vector `SVG` and `PDF`, plus high-quality `PNG` for preview, without changing aspect ratio. Verify that labels, symbols, legends, and curves are readable and unclipped in the final exported plot.
8. Return file locations and briefly describe what was plotted, the key observation, data sources, and any assumptions.

## Scientific integrity: hard rules

- Never invent simulated or measured values. Synthetic demo data must be explicitly labeled **illustrative, not simulation results**.
- Never silently smooth, normalize, offset, truncate, rebin, fit, interpolate, or log-transform values. State any such processing and provide a reproducible implementation.
- Never imply causal conclusions from visuals alone, and never imply a fitted curve is raw data.
- Respect uncertainties, statistical method, and significant figures. Do not invent error bars.
- Don't suppress data points simply because they disagree with an expected result.
- Avoid false precision, clipped comparisons, confusing dual axes, and deceptive chart ranges.
- Never treat doping concentration magnitude as a signed net-doping profile. Use `N_D - N_A` if net doping is meant, and use symlog or separate positive/negative panels if necessary.
- In LGAD comparisons, state the gain definition and ensure PIN/LGAD calculations share the same integration window and conditions when relevant.
- Use domain-specific mathematical symbols accurately; avoid embedding units in bare numerical values or legends with ambiguous units.

## Physics-specific guidance

**LGAD / Sentaurus:** Prefer doping vs depth, electric-field vs depth, transient current vs time, collected charge vs time, and gain vs voltage/dose. Clearly identify depth origin and direction, bias, doping polarity, and device variants. Distinguish electric-field magnitude from signed field component. Annotate peak and avalanche region only when data support that identification.

**Geant4:** Identify incident particle, kinetic energy, material and density, thickness, units, event count, and whether plotted stopping power is total deposited energy divided by areal density or track-length normalized. Distinguish simulated points from PDG/reference models.

**ROOT / AMS:** Preserve physical selection cuts, histogram bin definitions, normalization, and efficiency interval method; use markers for binned measurements and distinguish fits/reference curves.

## Slide-ready defaults

- White/transparent background; slide aspect ratio 16:9 but choose figure aspect ratio for content.
- For a large plot on a slide, axes labels about 18-22 pt, tick labels 14-17 pt, legend 15-18 pt; line widths 2.5-3.5 pt. For side-by-side plots, proportionally adjust while testing readability.
- Okabe-Ito palette: blue `#0072B2`, vermilion `#D55E00`, green `#009E73`, purple `#CC79A7`. Pair color with linestyle/markers.
- Prefer direct labels or short borderless legends; avoid excessive grids, gradients, and 3D visual effects.

Consult `references/plotting-standard.md` for rules, and `scripts/plot_demo.py` for a runnable example.