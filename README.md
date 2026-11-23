# ASCE 7-22 Roof Components & Cladding Wind Pressure Calculator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A single-page calculator for components and cladding (C&C) wind pressures on the roofs of low-rise buildings, per ASCE 7-22
Chapter 30, Part 1. It covers gable and hip roofs from flat to 45°, draws the roof zones in proportion to your plan, and reports
every zone at strength level and at ASD.

Live version: <https://oasisengineering.com/free-wind-load-calculator-for-roof-comp-clad/>

**This is a calculation aid.** A licensed engineer confirms every input and result before it is used for design.

## What it does

| | |
|---|---|
| Roofs | Gable and hip, 0° to 45°, mean roof height h ≤ 60 ft |
| Figures | 30.3-2A (θ ≤ 7°), 30.3-2B / 2C / 2D (gable), 30.3-2E / 2F / 2G (hip, with the Note 6 interpolation between 27° and 45°) |
| Inputs | V, exposure, enclosure, roof shape, slope (degrees or rise in 12), mean roof height, plan dimensions, effective wind area, K<sub>zt</sub>, ground elevation |
| Outputs | K<sub>h</sub>, q<sub>h</sub>, zone widths, GC<sub>p</sub> and design pressure per zone (strength and ASD), downward pressure, a live zone drawing, and a table across 10 to 500 sq ft |

Not covered: roof overhangs (Sec. 30.7), parapets, monoslope roofs steeper than 3°, stepped / sawtooth / multispan roofs, open
buildings, buildings over 60 ft, rooftop equipment, tornado loads (Chapter 32).

## Method

- K<sub>h</sub> = 2.41 (z / z<sub>g</sub>)<sup>2/α</sup>, Table 26.10-1, with z not less than 15 ft **in every exposure**.
- K<sub>e</sub> = e<sup>−0.0000362 z<sub>e</sub></sup>, Table 26.9-1.
- q<sub>h</sub> = 0.00256 K<sub>h</sub> K<sub>zt</sub> K<sub>e</sub> V², Eq. 26.10-1.
- p = q<sub>h</sub> K<sub>d</sub> [(GC<sub>p</sub>) − (GC<sub>pi</sub>)], Eq. 30.3-1, K<sub>d</sub> = 0.85, GC<sub>pi</sub> = ±0.18 or ±0.55.
- Not less than 16 psf either way at strength level (Sec. 30.2.2). ASD = 0.6 × strength.
- Zone width a = lesser of 10% of the least horizontal dimension and 0.4 h, not less than 4% of that dimension or 3 ft.
  The low-slope figure (30.3-2A) is laid out from h instead: edge strip 0.6 h, corner L 0.6 h by 0.2 h, Zone 1′ beyond 1.2 h.

### Example

V = 160 mph, Exposure C, enclosed, h = 30 ft, slope 3°, A = 10 sq ft: K<sub>h</sub> = 0.981, q<sub>h</sub> = 64.26 psf, and at
strength level Zone 1′ = −59.0, Zone 1 = −102.7, Zone 2 = −135.5, Zone 3 = −184.6 psf.

## How sure are the numbers

`test/cc-wind.test.js` pins 163 values: K<sub>z</sub> against Table 26.10-1, the wall and roof baselines, and GC<sub>p</sub> for every figure.

The GC<sub>p</sub> lines each have two sources: the equations in the ASCE 7-22 commentary (Tables C30.3-1 to C30.3-8), and a back-calculation from the 2024 IRC Table R301.2.1(1), which is computed from the same figures. The test file reproduces 55 printed IRC values to within 0.1 psf across every gable and hip figure. No line is left unconfirmed.

The zone layouts for the gable and hip figures (which strip is Zone 2, which is Zone 3, and the a and 2a widths) are drawn from a reading of the figures. Published summaries agree on the structure (one hip layout with Zone 3 along the eaves; two gable layouts split at 27°, with the ridge in Zone 1 on the steeper one), but the widths are only in the figures themselves. Glance at Figs. 30.3-2B to 2G once to confirm.

## Files

| File | |
|---|---|
| `index.html` | The calculator, one self-contained file. Open it in a browser, or embed it. Built, do not edit by hand. |
| `src/cc-wind.js` | The calculation engine. No dependencies; works in a browser (`CCWind`) and in Node. |
| `src/cc-wind-diagram.js` | Zone drawings as SVG (`CCWindDiagram`). |
| `src/page.html` | The page around them. |
| `build.py` | `python build.py` writes `index.html`; `python build.py --check` fails if it is stale. |
| `test/cc-wind.test.js` | `node test/cc-wind.test.js` |

## Changelog

**v2.0**
- Fixed: K<sub>h</sub> in Exposure B below 30 ft. v1 held z at 30 ft (K<sub>h</sub> = 0.70); that floor belongs to the
  Chapter 28 envelope procedure, not to components and cladding. Chapter 30 uses z = 15 ft (K<sub>h</sub> = 0.57), so v1
  overstated Exposure B pressures by about 20% for roofs under 30 ft.
- Added: gable and hip roofs above 7°, up to 45°.
- Added: downward (positive) pressure, the 16 psf minimum, ASD values, K<sub>d</sub> shown, a table by effective wind area.
- Fixed: the low-slope zone description and drawing. Fig. 30.3-2A zones are set by h (0.6 h, 0.2 h, 1.2 h), not by a.
- Fixed: monoslope roofs. Fig. 30.3-2A applies to them only up to 3°.
- Fixed: the over-60 ft message now points to Sec. 30.4 and Fig. 30.4-1.
- The drawing is now live and in proportion to the plan.

**v1.0** Low-slope roofs only (Fig. 30.3-2A).

## License

MIT. See [LICENSE](LICENSE).
