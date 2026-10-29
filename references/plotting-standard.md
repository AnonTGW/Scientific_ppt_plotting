# Scientific plotting standard for research slides

## Intended audience

Scientific group meetings, progress reports and PowerPoint presentations projected at a distance. A figure must make one principal finding obvious quickly while preserving accurate quantitative context.

## Slide versus manuscript

- For projected slides, prioritize large text and strong visual hierarchy over dense multi-panel detail.
- For manuscript figures, adapt to journal single- or double-column dimensions, usually smaller text than slide figures.
- Do **not** assume every image must itself be 16:9. Shape plots to fit a 16:9 slide while retaining appropriate axis geometry.

## Starting parameters (large plot occupying most of a slide)

| Attribute | Default range |
| --- | --- |
| Figure size | roughly 7.5–10 × 4.5–5.5 inches |
| Axis labels | 18–22 pt |
| Tick labels | 14–17 pt |
| Legend | 15–18 pt |
| Line width | 2.5–3.5 pt |
| Marker size | 6–9 pt |
| PNG preview | 200–300 dpi |
| Best final formats | SVG/PDF + PNG fallback |

Scale these values when figures occupy a smaller fraction of the slide. Export and inspect at final display dimensions.

## Typography and geometry

- Use a consistent, available font with legible mathematical glyphs (e.g. STIXGeneral/STIX math, DejaVu Sans, or a journal-prescribed font).
- Put physical quantity followed by its unit in parentheses: `Electric field (V/cm)`, `Depth (µm)`, `Time (ns)`, `Gain` (dimensionless).
- Use readable, non-overlapping tick intervals; prefer SI prefixes or scientific-notation offset text to huge tick labels.
- Show minor ticks only when useful; keep ticks consistent across panels. A top/right tick style can suit physics talks, but is not mandatory.
- Use a thin axis frame and restrained grid, if any. Use margins so no label is clipped.
- Use a short legend without a decorative box. Avoid redundant titles inside plots if the slide title already communicates the point.

## Color and identity

Use a colorblind-aware palette, paired with linestyles/markers:
- Blue `#0072B2`: baseline or PIN (if that mapping is established).
- Vermilion `#D55E00`: modified device or LGAD (if established).
- Green `#009E73`: third configuration or reference.
- Purple `#CC79A7`: additional comparison.

This mapping is a **suggestion**, not a physical meaning. Choose a mapping at the start of a project and apply it everywhere. Never rely on color alone.

## Choosing scientific plots

- Physical profile: line vs depth/time, if values sample a continuous function.
- Independent simulated or measured estimates: markers, with error bars when available.
- Histogram: event distribution; preserve bin widths/normalization.
- Fit: show raw points separately from the fitted line; provide the fit model/range where relevant.
- Parameters: use comparable axes across panels; don't overplot dozens of traces.
- Signed quantity with huge range: `symlog` or a dedicated signed panel; a regular `log` axis cannot represent negative values.
- If using a heatmap, specify colorbar quantity, units, color normalization, and data range.
- Do not use misleading truncated axes, unexplained dual axes, gratuitous 3D, or heavy gradients.

## Domain examples

### Sentaurus / LGAD
1. Doping profiles: plot donors `N_D`, acceptors `N_A`, and signed `N_D-N_A` carefully. Label depth origin and direction.
2. Field profiles: specify field magnitude or component, bias, depth, field units, and gain-layer region if justified.
3. Current transient: label current and time units; say whether PIN and LGAD used identical conditions.
4. Integrated-charge gain: label definition, e.g. `Q_LGAD/Q_PIN`, integration window, and statistical treatment. Do not call a fabricated level a measured saturation.
5. Parameter scans: plot dose/peak concentration/bias versus gain; distinguish measured/simulated points from interpolants.

### Geant4
Specify muon charge, incident kinetic energy, copper density/thickness, normalization by areal density, number of events, selection, and uncertainty definition. Separate PDG reference curves from simulation estimates visually.

### ROOT / AMS
Preserve event-selection cuts, histogram weights, normalization, binomial efficiency interval definitions, fit ranges, and axis units. Keep ROOT and Matplotlib labeling consistent if converting files.

## Reproducibility & validation checklist

- [ ] Data sources and physical units documented
- [ ] Every axis labeled; plot scale (linear/log/symlog) justified
- [ ] Treatments of missing data and uncertainties stated
- [ ] Lines/markers and colors consistent across slides
- [ ] No unjustified smoothing, cropping, rebinning, or manipulation
- [ ] PNG, SVG and PDF exported without clipping
- [ ] Figure visually reviewed at projected slide size
- [ ] Underlying script and data provenance retained

## Suggested caption or slide summary

**Finding:** one sentence describing what the plotted evidence shows. Follow with operating conditions and a note about statistics/uncertainties when relevant.
