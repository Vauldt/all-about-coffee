---
tags: []
  - coffee/brewing
  - coffee/brewing/water
  - coffee/equipment
aliases:
  - TDS meter
  - EC meter coffee
  - Conductivity meter water
---

# TDS Meters

**Tags:** #coffee/brewing #coffee/brewing/water #coffee/equipment
**Aliases:** TDS meter, EC meter coffee, Conductivity meter water
**Related:** [Water in Coffee MOC](../maps-of-content/water-in-coffee-moc.md) | [TDS Measurement](tds-measurement.md) | [Total Dissolved Solids](total-dissolved-solids.md) | Measurement Tools
**Status:** ✅ Complete

---

## Overview

TDS meters (also called EC meters or conductivity meters) are electronic instruments that estimate the total dissolved solids concentration of water by measuring electrical conductivity. In coffee water management, they are the standard tool for rapid water monitoring — providing an immediate indication of total mineral content before and after treatment. TDS meters are inexpensive (AUD$20–200), require minimal maintenance, and give instant readings, making them practical for both daily café use and DIY water recipe verification.

## How TDS Meters Work

A TDS meter applies a small alternating electrical current between two or four submerged electrodes and measures the resulting conductance (ability of the solution to conduct electricity). This conductance, divided by the cell constant of the electrode geometry, gives electrical conductivity (EC) in µS/cm. The meter then multiplies EC by a built-in conversion factor (typically 0.5) to display an estimated TDS in mg/L (or ppm).

Because different ions conduct electricity with different efficiency, the conversion is approximate — the displayed TDS is an estimate based on an assumed average ion mix. For coffee water monitoring this is sufficiently accurate; precise ion-specific measurement requires laboratory analysis.

## Meter Types

### Two-Electrode Pen Meters

- Simplest design; two exposed electrodes at the tip
- Reading in mg/L (TDS) or µS/cm (EC) depending on model
- Cost: AUD$15–40
- Accuracy: adequate for water screening; some models have limited accuracy or drift
- Examples: generic pen meters widely available; HM Digital TDS-3

### Four-Electrode (Multi-Parameter) Meters

- Four-electrode design reduces polarisation effects; more accurate, especially at high conductivity
- Often includes temperature measurement and automatic temperature compensation (ATC)
- May also measure pH, pH, ORP, and other parameters
- Cost: AUD$50–200
- Examples: Apera PC60, Milwaukee MW302, Hanna HI 9813-6

### Benchtop Conductivity Meters

- Laboratory-grade; high accuracy (±0.5% or better); certified calibration capability
- Used in water treatment facilities, brewing research, and quality control labs
- Cost: AUD$300–1000+
- Examples: Mettler-Toledo FiveEasy, Hanna HI 5321

## Calibration

TDS/EC meters require periodic calibration with certified conductivity standard solution:
- **Typical standard:** 1413 µS/cm (KCl solution at 25°C)
- **Frequency:** Before first use; periodically per manufacturer recommendation; when in doubt about accuracy
- **Process:** Rinse electrode; immerse in standard; adjust meter reading to match certified value; rinse before use on samples

Temperature affects conductivity significantly (~2% per °C). Meters with ATC automatically correct for temperature; meters without ATC should be used at a consistent temperature for comparable readings.

## Reading Interpretation for Coffee Water

| TDS display (mg/L) | EC (µS/cm, ÷0.5) | Assessment for coffee |
| :--- | :--- | :--- |
| < 50 | < 100 | RO permeate / distilled; too low — remineralise |
| 50–150 | 100–300 | Low; reasonable for light roast; check alkalinity |
| 75–250 | 150–500 | SCA acceptable range |
| 150 | ~300 | SCA target TDS |
| 250–400 | 500–800 | Elevated; check alkalinity and hardness |
| > 400 | > 800 | High; treat water before use |

## Limitations

- TDS meters do not distinguish between mineral types — two waters at identical TDS can produce very different coffee depending on whether TDS comes from bicarbonate or from calcium/magnesium chloride/sulfate
- TDS measurement is a starting point, not a complete water assessment — always test alkalinity (KH) separately using a titration kit
- Contaminated electrodes (oil, mineral deposits) give inaccurate readings — clean electrodes regularly

## Key Facts

- TDS meters estimate dissolved mineral content by measuring electrical conductivity; display result in mg/L or ppm
- Conversion: EC (µS/cm) × 0.5 ≈ TDS (mg/L) — the built-in conversion factor in most meters
- SCA TDS target of 150 mg/L ≈ 300 µS/cm EC
- Pen-style meters (AUD$15–40) are adequate for routine café screening; four-electrode meters are more accurate
- TDS reading alone is insufficient for water quality assessment — always pair with KH (alkalinity) measurement

## Related Notes

- [TDS Measurement](tds-measurement.md)
- [Total Dissolved Solids](total-dissolved-solids.md)
- [TDS and Taste](tds-and-taste.md)
- [Optimal TDS Range](optimal-tds-range.md)
- Measurement Tools
- [Water in Coffee MOC](../maps-of-content/water-in-coffee-moc.md)

## References

- [Hanna Instruments — TDS and EC Meter Selection Guide](https://www.hannainst.com)
- [Apera Instruments — Water Quality Meters](https://www.aperainst.com)
- [Specialty Coffee Association — Water Quality Standards](https://sca.coffee/research)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-04-28 | Note created |

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
