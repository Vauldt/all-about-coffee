---
tags: []
  - coffee/roasting
  - coffee/roasting/production
aliases:
  - Roast data logging
  - Profile logging
  - Roast record keeping
---

# Roast Logging

**Tags:** #coffee/roasting #coffee/roasting/production
**Aliases:** Roast data logging, Profile logging, Roast record keeping
**Related:** [Roasting MOC](../maps-of-content/roasting-moc.md) | [Roast Profile](roast-profile.md) | [Cropster](cropster.md) | [Artisan Software](../roasting-coffee-beans/artisan-software.md) | [Rate of Rise](rate-of-rise.md) | [Development Time Ratio](development-time-ratio.md)
**Status:** ✅ Complete

---

## Overview

Roast logging is the systematic recording of roast parameters — temperature curves, time markers, gas and airflow settings, and batch metadata — for every roast batch. It is the foundational practice enabling roast profile replication, quality control, and batch-to-batch consistency in specialty coffee production. Without logged data, roasters cannot identify the specific conditions that produced a given cup outcome, diagnose the source of batch variation, or replicate a successful profile on subsequent batches. Roast logging ranges from hand-written paper records to fully automated digital logging via software platforms (Artisan, Cropster) that capture continuous temperature and Rate of Rise data from thermocouple-equipped roasters.

## What Is Logged

A complete roast log typically records:

| Data Type | Examples |
| :--- | :--- |
| Batch metadata | Date, operator, green coffee lot, batch weight, target roast level |
| Temperature curves | Bean temperature (BT) and environmental temperature (ET) at regular intervals |
| Rate of Rise | Calculated from BT curve; logged continuously |
| Phase markers | Charge time/temperature, turning point time/temperature, first crack start/end, drop time/temperature |
| Derived metrics | Development Time Ratio, total roast time, weight loss (roast yield) |
| Equipment settings | Gas settings at each phase, airflow/damper positions, drum speed |
| Post-roast notes | Roast colour (Agtron), cupping score, observations |

## Digital Versus Paper Logging

**Digital logging (Artisan, Cropster):**
- Continuous temperature and RoR data captured automatically from thermocouple probes
- Phase markers entered by operator at the moment of each event
- Post-roast metrics calculated automatically (DTR, turning point, drop temperature)
- Searchable profile library allows comparison across sessions
- Artisan: free, local storage, single-roaster focus
- Cropster: paid subscription, cloud storage, multi-user access, inventory integration

**Paper logging:**
- Operator records temperature at regular intervals (typically every 30 seconds) by reading the gauge
- Less accurate than continuous digital logging; operator attention divided between recording and roast management
- Lower cost but loses the RoR curve and fine-grained temperature data
- Sufficient for basic consistency tracking but inadequate for detailed profile analysis

## Roast Logging for Consistency

The primary value of roast logging in production is enabling reproducibility. When a roast produces a desirable cup, the log records every parameter that contributed to that outcome. On subsequent batches of the same green coffee, the roaster can compare the live profile against the reference log and make real-time adjustments to stay on-curve.

Key consistency metrics extracted from logs:

- **Charge temperature:** Must match within ±2–3 °C for consistent turning points
- **Turning point temperature and time:** Diagnostic of charge consistency
- **First crack start time:** Consistency within ±20–30 seconds batch-to-batch indicates good profile control
- **Development Time Ratio:** Must be consistent for consistent cup outcome at equivalent drop temperatures
- **Total roast time:** Changes indicate batch size, green coffee moisture, or energy input variation

## Roast Logging and Quality Control

Production roasters link roast logs to cupping records — assigning SCA scores or sensory descriptors to each logged batch. This linkage reveals which profile parameters correlate with which cup outcomes for a specific green coffee, building a calibrated understanding of how roast variables affect the final beverage. Over time, logged data builds the institutional knowledge that allows a roasting operation to train new staff, maintain consistency across multiple operators, and diagnose quality deviations.

## Key Facts

- Roast logging: systematic recording of roast parameters for every batch to enable replication and quality control
- Logs capture: temperature curves, RoR, phase markers, batch metadata, equipment settings, post-roast notes
- Digital logging (Artisan, Cropster) provides continuous, automated data capture superior to paper records
- Key consistency metrics: charge temperature, turning point, first crack timing, DTR, total roast time
- Linking roast logs to cupping scores builds calibrated profile–cup quality understanding
- Essential practice for specialty production roasting at any scale

## Related Notes

- [Roasting MOC](../maps-of-content/roasting-moc.md)
- [Roast Profile](roast-profile.md)
- [Cropster](cropster.md)
- [Artisan Software](../roasting-coffee-beans/artisan-software.md)
- [Rate of Rise](rate-of-rise.md)
- [Development Time Ratio](development-time-ratio.md)
- [Charge Temperature](charge-temperature.md)

## References

- [Rao, S. (2014). *The Coffee Roaster's Companion* — Scott Rao](https://www.scottrao.com/the-coffee-roasters-companion)
- [Cropster — Roast logging and production management documentation](https://www.cropster.com)
- [Artisan Roast Logger — Profile logging guide](https://artisan-scope.org)
- [Specialty Coffee Association — Roasting Professional Certificate](https://sca.coffee/education/courses)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-04-27 | Note created |

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
