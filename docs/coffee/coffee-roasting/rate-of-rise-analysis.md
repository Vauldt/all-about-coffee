---
tags: []
  - coffee/roasting
  - coffee/roasting/profile
aliases:
  - RoR analysis
  - Analysing Rate of Rise
---

# Rate of Rise Analysis

**Tags:** #coffee/roasting #coffee/roasting/profile
**Aliases:** RoR analysis, Analysing Rate of Rise
**Related:** [Roasting MOC](../maps-of-content/roasting-moc.md) | [Rate of Rise](rate-of-rise.md) | [Development Time Ratio](development-time-ratio.md) | [Artisan Software](../roasting-coffee-beans/artisan-software.md) | [Cropster](cropster.md)
**Status:** ✅ Complete

---

## Overview

Rate of Rise (RoR) analysis is the practice of examining the RoR curve — the derivative of the bean temperature (BT) curve over time — to assess, diagnose, and refine a roast profile. While the absolute temperature curve shows where the roast is, the RoR curve shows how fast it is getting there, and the shape of this curve is a primary indicator of profile quality. Scott Rao's work establishing the declining RoR model as a quality reference has made RoR analysis a central skill in specialty roasting; understanding how to read the RoR curve is fundamental to diagnosing baked, underdeveloped, crashed, or well-executed roasts.

## Reading the RoR Curve

The RoR curve is typically displayed in profile software (Artisan, Cropster) in degrees Celsius per minute (°C/min) on a secondary y-axis overlaid on the BT curve. Key features:

**Initial RoR after charge:** The RoR begins very high after green coffee is charged into the hot drum — sometimes 20–30°C/min or more — then falls rapidly as the cold bean mass absorbs heat and the drum cools. This initial spike is not meaningful for profile analysis.

**Turning point:** The BT reaches its minimum (the turning point) when the RoR passes through zero. After the turning point, RoR is positive and the bean temperature rises continuously.

**Post-turning-point RoR peak:** In a well-managed declining RoR profile, the RoR peaks relatively early (often in the first 1–3 minutes after turning point) and then declines continuously through the rest of the roast.

**Browning phase RoR:** A smooth, declining RoR through the 155–190°C zone indicates controlled energy delivery. A flat or rising RoR in this zone indicates too much energy and potential scorching or rushed browning.

**First crack RoR:** At first crack, the exothermic reaction temporarily reduces the apparent RoR (the bean releases heat, reducing the temperature difference between bean and heat source). A well-managed profile shows a brief, controlled RoR dip at first crack without crashing to zero or below.

**Development phase RoR:** Post-first-crack, a controlled declining RoR (typically 3–8°C/min depending on roaster and target) is the standard for specialty profiles. The RoR should continue declining gently to drop.

## The Declining RoR Model

The declining RoR model — where the RoR consistently decreases from its post-turning-point peak to drop without plateauing or rising — is the most widely adopted quality framework in specialty roasting. Its rationale:

- A declining RoR means the bean is absorbing heat at a decreasing rate; the bean is "catching up" to its environment rather than being driven harder as temperature rises
- Flat or rising RoR indicates the roaster is applying increasing energy relative to bean temperature, which risks development imbalance (scorching at high temps, baking at lower temps)
- The crash-and-flick pattern (RoR falls sharply near first crack then rises) is a particularly notable defect in RoR shape, associated with reactive overcorrection and uneven development

## Diagnosing Problems from RoR

| RoR pattern | Diagnosis | Cup symptom |
| :--- | :--- | :--- |
| Rising RoR through browning | Excessive heat; runaway heating | Possible scorching; harsh bitterness |
| Flat RoR through browning | Insufficient heat; baking risk | Flat, bread-like, no sweetness |
| Sharp RoR crash pre-first-crack | Excessive heat reduction anticipating crack | Stalled development; underdevelopment |
| Flick (rise) after first crack | Reactive overcorrection; crash-and-flick | Uneven development; sour-baked combination |
| RoR approaching zero in development | Prolonged low-temperature soak | Baked character; flat, dull cup |
| Smooth declining RoR throughout | Well-managed declining profile | Clean development; balance of origin and roast |

## Comparing RoR Curves Across Batches

RoR analysis is most powerful when comparing curves across multiple batches:
- Overlaying RoR curves for batches of the same green coffee allows identification of batch-to-batch inconsistency
- Environmental changes (ambient temperature, humidity), batch weight variation, or equipment wear all shift the RoR curve; analysis identifies these before they become chronic quality problems
- Profile logging software (Artisan, Cropster) facilitates automatic RoR comparison across sessions

## Limitations of RoR Analysis

- RoR curves are sensitive to probe placement and response time; noisy or slow probes produce jagged or delayed RoR readings
- RoR is a derivative — small fluctuations in the BT reading are amplified in the RoR; smoothing in software reduces noise but can obscure real events
- RoR analysis must be contextualised with the absolute temperature curve, DTR, and cup result — RoR shape alone does not fully determine cup quality

## Key Facts

- RoR analysis reads the derivative of the BT curve to assess how rapidly and evenly heat is being delivered to the bean mass
- The declining RoR model (continuously decreasing from post-turning-point peak to drop) is the dominant quality framework in specialty roasting
- Key diagnostic patterns: rising RoR (excess heat), flat RoR (baking), crash-and-flick (reactive overcorrection), RoR approaching zero in development (baking)
- Most valuable when comparing across batches; overlaying curves identifies systematic variation from environmental or equipment factors
- RoR curves are noisy — probe quality, smoothing settings, and data logging rate all affect readability

## Related Notes

- [Roasting MOC](../maps-of-content/roasting-moc.md)
- [Rate of Rise](rate-of-rise.md)
- [Development Time Ratio](development-time-ratio.md)
- [Declining Rate Profiles](declining-rate-profiles.md)
- [Crash and Flick](crash-and-flick.md)
- [Baked Roasts](../roasting-coffee-beans/baked-roasts.md)
- [Artisan Software](../roasting-coffee-beans/artisan-software.md)
- [Cropster](cropster.md)

## References

- [Rao, S. (2014). *The Coffee Roaster's Companion* — Scott Rao](https://www.scottrao.com/the-coffee-roasters-companion)
- [Artisan Software — Roast Profile Analysis Documentation](https://artisan-scope.org)
- [Cropster — RoR and Profile Analytics](https://www.cropster.com)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-04-27 | Note created |

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
