# ASCE 7-22 Roof Components & Cladding Wind Pressure Calculator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/asce-roof-wind-calculator.svg?style=social)](https://github.com/yourusername/asce-roof-wind-calculator/stargazers)

A sleek, intuitive web-based tool to estimate wind pressures and loads on roof components and cladding for low-rise buildings based on ASCE 7-22. This calculator dynamically interpolates GCp from ASCE figures, supporting various roof types (gable, hip, monoslope), slopes, and enclosure classifications for precise zone-specific results.

**Note:** This is an estimation tool for educational and preliminary purposes. Always consult a licensed engineer for final designs, as it uses interpolated values and assumes standard low-rise conditions (h ≤ 60 ft).

## Features

- **Input Parameters:**
  - Ultimate wind speed, V (mph)
  - Least horizontal dimension (ft)
  - Mean roof height, h (ft)
  - Roof slope (°)
  - Roof type (e.g., Flat Gable, Hip 20-27°)
  - Effective wind area, A (ft²)
  - Topographic factor, Kzt (default 1.0)
  - Exposure category (B, C, D)
  - Enclosure classification (Enclosed or Partially Enclosed)

- **Outputs:**
  - Velocity pressure qh (psf)
  - Internal pressure GCpi
  - End zone width 'a' (ft)
  - Exposure coefficient Kz
  - Net positive (inward) and negative (outward) pressures (psf) for Zones 1 (Interior), 2 (Edges), 3 (Corners/Ridges)
  - Corresponding wind loads (lbf)
  - Conceptual zone diagram
  - Warnings for heights >60 ft

- **Advanced Calculations:** Dynamic GCp interpolation based on area and roof type/slope from ASCE figures; tooltips for guidance.
- **Responsive Design:** Clean, modern UI inspired by premium apps—works seamlessly on desktop and mobile.
- **No Dependencies:** Pure HTML, CSS, and JavaScript—lightweight and browser-ready.

## Demo

You can try the calculator live [here]https://oasisengineering.com/free-wind-load-calculator-for-roof-comp-clad/

## Installation

No installation required! This is a static web page.

1. Clone the repository:
2. Open `index.html` in your web browser.

Alternatively, download the ZIP and open the HTML file directly.

## Usage

1. Enter wind speed, dimensions, slope, select roof type, exposure, enclosure, and other factors.
2. Click **Calculate** to generate results.
3. Review pressures and loads per zone, with a conceptual diagram for visualization.
4. If height >60 ft, a warning prompts for advanced ASCE methods.
5. Use **Reset** to clear and start over.

### Example

- Ultimate Wind Speed: 140 mph
- Least Horizontal Dimension: 40 ft
- Mean Roof Height: 20 ft
- Roof Slope: 26.6°
- Roof Type: Gable (20°-27°)
- Effective Wind Area: 10 ft²
- Topographic Factor: 1.0
- Exposure: C
- Enclosure: Enclosed

**Result:** 
- qh: ~41.2 psf
- GCpi: ±0.18
- a: 8 ft
- Kz: ~0.85
- Zone 1: Positive 24.7 psf, Negative -41.2 psf
- Zone 2: Positive 28.8 psf, Negative -90.6 psf
- Zone 3: Positive 28.8 psf, Negative -131.8 psf
- Loads scaled by area.

## Technical Details

- **Calculations:** Based on ASCE 7-22 Chapter 30 (C&C for roofs). Exact Kz formula, interpolated GCp neg from figures (log-scale for A 10-500 ft²), GCpi per enclosure. qh at h with Kd=1.0, Ke=1.0. Positive GCp often constant; negative varies by zone/type/slope.
- **Prescriptive Check:** 'a' per ASCE definition; supports multiple roof configurations via parameterized figures.
- **Limitations:** Low-rise only; no directionality (Kd=1.0); no overhangs/parapets; simplified for common cases. For complex roofs or high-rise, use full ASCE/software.

## Contributing

Contributions are welcome! Please fork the repo and submit a pull request.

1. Fork the project.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool provides estimates only and is not a substitute for professional engineering advice. Calculations are based on simplified interpolations from ASCE 7-22 figures. Verify all designs with a licensed structural engineer to ensure compliance with local codes and site-specific conditions. Oasis Engineering assumes no liability for any use of this tool or for any errors, omissions, or damages arising from its use.

## Acknowledgments

- Crafted with inspiration from Elon Musk's focus on simplicity and Steve Jobs' obsession with elegant design.
- Based on ASCE 7-22 Minimum Design Loads for Buildings.

If you find this useful, star the repo! ⭐
