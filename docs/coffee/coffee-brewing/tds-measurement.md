---
tags: []
  - coffee/brewing
  - coffee/brewing/water
aliases:
  - Measuring water TDS
  - EC measurement water
  - Total dissolved solids testing
---

# TDS Measurement

**Tags:** #coffee/brewing #coffee/brewing/water
**Aliases:** Measuring water TDS, EC measurement water, Total dissolved solids testing
**Related:** [Water in Coffee MOC](../maps-of-content/water-in-coffee-moc.md) | [Total Dissolved Solids](total-dissolved-solids.md) | [TDS Meters](tds-meters.md) | [Water Standards](water-standards.md) | Measurement Tools
**Status:** ✅ Complete

---

## Overview

Water TDS (Total Dissolved Solids) is measured by one of two methods: electrical conductivity (EC) measurement using a conductivity meter, which provides a rapid estimate of total ion concentration, or gravimetric analysis (evaporation to dryness), which is the definitive laboratory method. In coffee water management, EC meters are the practical tool of choice — inexpensive, fast, and sufficiently accurate for water recipe development and monitoring. The relationship between EC and TDS requires a conversion factor that varies depending on the ion composition of the specific water.

## Electrical Conductivity (EC) Method

Dissolved ions conduct electricity; the more ions present, the higher the conductivity. An EC meter measures the ability of the water to conduct electrical current between two electrodes, expressed in microsiemens per centimetre (µS/cm) or millisiemens per centimetre (mS/cm).

**TDS (mg/L) ≈ EC (µS/cm) × conversion factor**

Common conversion factors:
- **0.5** (widely used for natural water and water recipes with mixed mineral composition)
- **0.64** (used by some instruments for sodium chloride–calibrated measurements)
- **0.67** (used for water rich in bicarbonate/carbonate)
- **0.7** (some European water standards)

The conversion factor is an approximation because different ions conduct electricity with different efficiency:
- Sodium, potassium, chloride, and bicarbonate are highly conductive per unit mass
- Calcium and magnesium are somewhat less conductive per unit mass

For coffee water work, the 0.5 factor is the most common and produces estimates that are sufficiently accurate for recipe work and monitoring purposes. The SCA target TDS of 150 mg/L corresponds to approximately 250–300 µS/cm EC.

## Gravimetric Analysis

The reference method for TDS measurement:
1. Filter a known volume of water through a 0.45 µm membrane filter to remove suspended solids
2. Evaporate the filtered sample to dryness at 180°C in a pre-weighed evaporating dish
3. Cool to room temperature in a desiccator, then weigh the residue
4. TDS (mg/L) = (residue mass in mg) ÷ (sample volume in litres)

This method is slow, requires laboratory equipment, and is not practical for routine café use — but it is the definitive measurement against which EC-based methods are calibrated.

## EC Meters for Coffee Water

Pocket EC/TDS meters are the standard tool for routine coffee water monitoring:
- **Design:** Handheld probe with two or four electrodes; temperature sensor; digital display
- **Reading:** Display in µS/cm (conductivity) or direct TDS estimate in mg/L (using internal conversion factor)
- **Calibration:** With certified conductivity standard solution (typically 1413 µS/cm KCl standard)
- **Accuracy:** ±2–5% of reading for quality instruments
- **Common brands:** Hanna Instruments (HI 9813-6, HI 98301), Milwaukee (MW302), Apera (PC60)

See [TDS Meters](tds-meters.md) for detailed instrument selection guidance.

## What EC Does Not Measure

EC meters measure only ionic dissolved substances — not non-ionic dissolved organics, dissolved gases (CO₂, O₂), or colloidal material. This is rarely a practical concern for clean municipal or well water used for coffee, but:
- Distilled water with dissolved CO₂ from the atmosphere shows low but non-zero EC (CO₂ forms carbonic acid, which ionises slightly)
- Water with organic contamination may have low EC but significant non-ionic dissolved material

## Interpreting TDS Readings

| EC (µS/cm) | Estimated TDS (×0.5) | Assessment |
| :--- | :--- | :--- |
| < 50 | < 25 mg/L | Very low (RO permeate or distilled); requires remineralisation |
| 100–200 | 50–100 mg/L | Low-moderate; may produce thin body |
| 200–350 | 100–175 mg/L | SCA target zone (75–250 mg/L TDS) |
| 350–500 | 175–250 mg/L | SCA acceptable upper range |
| > 500 | > 250 mg/L | Elevated; check alkalinity and hardness |
| > 1000 | > 500 mg/L | Very high; unsuitable for coffee without treatment |

## Key Facts

- Water TDS is measured by EC (rapid, practical) or gravimetric analysis (laboratory reference method)
- EC (µS/cm) × 0.5 ≈ TDS (mg/L) for typical mixed-mineral water; exact factor varies by ion composition
- SCA TDS target: 150 mg/L ≈ 250–300 µS/cm EC
- EC meters require calibration with certified conductivity standard; accuracy ±2–5%
- EC measures ionic content only; non-ionic dissolved organics are not detected

## Related Notes

- [Total Dissolved Solids](total-dissolved-solids.md)
- [TDS Meters](tds-meters.md)
- [TDS and Taste](tds-and-taste.md)
- [Optimal TDS Range](optimal-tds-range.md)
- [Water Standards](water-standards.md)
- [Water in Coffee MOC](../maps-of-content/water-in-coffee-moc.md)

## References

- [Specialty Coffee Association — Water Quality Standards](https://sca.coffee/research)
- [Hanna Instruments — EC/TDS Measurement Guide](https://www.hannainst.com)
- [Colonna-Dashwood, M. & Hendon, C. (2015). *Water for Coffee*](https://www.colonnacoffee.com)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-04-28 | Note created |

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
