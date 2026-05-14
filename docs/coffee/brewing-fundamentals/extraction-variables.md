---
tags: []
  - coffee/brewing
  - coffee/brewing/fundamentals
aliases:
  - Brewing variables
  - Extraction parameters
  - Variables affecting extraction
---

# Extraction Variables

**Tags:** #coffee/brewing #coffee/brewing/fundamentals
**Aliases:** Brewing variables, Extraction parameters, Variables affecting extraction
**Related:** [Coffee Extraction Fundamentals MOC](../maps-of-content/coffee-extraction-fundamentals-moc.md) | [Extraction Science](extraction-science.md) | [Extraction Yield](extraction-yield.md) | ../Maps of Content/Grind Size MOC | [Brewing Control Chart](../coffee-brewing-science/brewing-control-chart.md)
**Status:** ✅ Complete

---

## Overview

Extraction variables are the controllable factors that determine how much coffee dissolves into water during brewing, how quickly extraction occurs, and which compounds are extracted. Each brewing method involves manipulating the same fundamental variables — though specific values and their relative importance vary by method. Understanding these variables and their interactions transforms brewing from guesswork into a predictable, repeatable process.

## Primary Variables

The six primary variables have the greatest influence on extraction yield and cup quality:

### Grind Size

Grind size determines the surface area of coffee exposed to water and the flow resistance of the coffee bed. It is the most impactful single variable in extraction. A finer grind increases surface area exposure and slows water flow, producing higher extraction yield; a coarser grind reduces surface area and increases flow rate, producing lower extraction yield.

- Under-extracted: grind finer
- Over-extracted: grind coarser

See ../Maps of Content/Grind Size MOC for complete analysis.

### Water Temperature

Water temperature governs the rate at which compounds dissolve. Higher temperatures increase solubility and extraction speed; lower temperatures slow extraction and alter which compound classes are preferentially extracted. The SCA standard range for most hot-brew methods is 90–96 °C.

- Under-extracted: increase temperature 2–3 °C
- Over-extracted: decrease temperature 2–3 °C

See [Water Temperature](../water/water-temperature.md) for complete analysis.

### Brew Time

Brew time is the duration of contact between water and coffee grounds. Longer contact time generally produces higher extraction yield, though the relationship is not linear — early extraction is rapid, while later extraction slows as the concentration gradient narrows. Brew time is often the consequence of other variables (grind size, technique, pressure) rather than an independently set parameter, particularly in espresso. See [Extraction Time](extraction-time.md).

### Coffee Dose

Dose is the mass of coffee used in a brew. It primarily affects strength (TDS concentration) rather than extraction yield. Increasing dose with constant water volume produces a stronger, more concentrated brew at approximately the same extraction percentage.

- Weak coffee (correctly extracted): increase dose or reduce water volume
- Strong coffee (correctly extracted): decrease dose or increase water volume

### Water Volume and Brew Ratio

Brew ratio — the proportion of coffee to water, typically expressed as 1:N — primarily affects strength. A higher ratio (more water per gram of coffee) produces a weaker brew; a lower ratio produces a stronger brew. Standard ratios: espresso approximately 1:2–1:2.5; filter coffee approximately 1:15–1:17. See [Brew Ratio](brew-ratio.md).

### Agitation

Agitation — stirring, pouring technique, turbulence, or mechanical action — increases extraction uniformity and rate by renewing contact between fresh water and coffee grounds. In espresso, pressure provides the primary agitation; in pour-over, pouring technique determines agitation; in immersion methods, an initial stir improves saturation.

## Secondary Variables

These variables have significant but generally less direct impact on extraction:

- **Water quality:** Mineral composition and alkalinity affect compound solubility and perceived flavour; magnesium-rich water enhances extraction; excessive calcium carbonate mutes acidity. See [Water Quality](../coffee-brewing-water/water-quality.md).
- **Coffee freshness:** Fresh coffee contains CO₂ that can impede even water penetration; resting espresso 7–14 days post-roast and filter coffee 3–7 days improves consistency.
- **Roast level:** Light roasts are denser and harder to extract; dark roasts are more porous and extract more readily at equivalent grind settings.
- **Bean density:** High-altitude beans are denser and may require adjusted parameters compared to lower-grown coffees at the same roast level.
- **Pressure (espresso):** Standard extraction pressure is approximately 9 bar; pressure profiling machines vary pressure during extraction to manage extraction uniformity and flavour development.

## Variable Interactions

Variables do not act independently. Changing one typically requires compensatory adjustment of others to maintain target extraction yield:

**Grind size and time:** Finer grind → faster extraction → shorter brew time needed. Grinding finer without shortening time moves extraction towards over-extraction.

**Temperature and time:** Higher temperature → faster extraction → shorter time needed. These variables partially compensate for each other but produce different flavour profiles at the same extraction yield.

**Dose and strength versus extraction:** Dose and water volume affect strength (TDS) without materially changing extraction yield. Confusing a strength problem (weak or strong cup) with an extraction problem (sour or bitter cup) leads to incorrect variable adjustment.

## Adjustment Priority

When diagnosing and correcting extraction problems, adjustments are made in order of impact:

**Under-extracted (sour, thin):**
1. Grind finer (most impactful)
2. Increase temperature 2–3 °C
3. Extend brew time where the method permits
4. Increase agitation

**Over-extracted (bitter, harsh):**
1. Grind coarser (most impactful)
2. Decrease temperature 2–3 °C
3. Shorten brew time where the method permits
4. Reduce agitation

**Weak but correctly extracted (not sour):** Increase dose or reduce water volume.

**Strong but correctly extracted (not bitter):** Decrease dose or increase water volume.

Changing only one variable per brew session makes it possible to isolate the cause of any cup problem. Changing multiple variables simultaneously makes the cause of any change impossible to identify.

## Key Facts

- Six primary extraction variables: grind size, water temperature, brew time, dose, water volume, agitation — in approximate order of impact on extraction yield
- Grind size is the most powerful single variable; dose and water volume primarily affect strength (TDS), not extraction yield (the percentage extracted)
- Variables interact: grinding finer without adjusting time or temperature moves extraction beyond the target zone
- Distinguishing an extraction problem (sour/bitter) from a strength problem (weak/strong) determines which variable to adjust
- SCA target extraction yield for most methods: 18–22%; diagnosable from sensory evaluation and confirmed by refractometry

## Related Notes

- ../Maps of Content/Grind Size MOC
- [Water Temperature](../water/water-temperature.md)
- [Extraction Time](extraction-time.md)
- [Extraction Yield](extraction-yield.md)
- [Brew Ratio](brew-ratio.md)
- [Water Quality](../coffee-brewing-water/water-quality.md)
- [Brewing Control Chart](../coffee-brewing-science/brewing-control-chart.md)
- [Coffee Extraction Fundamentals MOC](../maps-of-content/coffee-extraction-fundamentals-moc.md)

## References

- [Specialty Coffee Association — Brewing Standards](https://sca.coffee/research)
- [Rao, S. (2015). *Everything But Espresso*. Scott Rao.](https://www.scottrao.com/books)
- [Hendon, C.H. et al. (2014). *Journal of Agricultural and Food Chemistry*. DOI: 10.1021/jf501687c](https://doi.org/10.1021/jf501687c)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-05-03 | Compliance review: fixed frontmatter (added coffee/* tags; removed non-coffee/* tags `extraction`, `brewing-science`, `variables`, `fundamentals`, `optimization`, `- 1`, `- 2`; removed `date_created` and `updated` fields); fixed path-prefixed wikilinks (`05_PUBLISHING/Atomic Notes/Grind Size` → `Grind Size`, `../Water Temperature` → `[Water Temperature](../water/water-temperature.md)`, `../Water Quality` → `[Water Quality](../coffee-brewing-water/water-quality.md)`, `05_PUBLISHING/Dictionary/Dictionary Atomic Notes/Brew Ratio` → `[Brew Ratio](brew-ratio.md)`); removed URL-style markdown links and trailing code fence; fixed "flavor" → "flavour", "channeling" → "channelling"; removed Fahrenheit temperatures; condensed from 620 lines to encyclopedic format; removed instructional step-by-step sections, second-person language, starred motivational text blocks, and Common Mistakes section; added metadata block, all required sections, copyright |

---

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
