---
tags: []
  - coffee/roasting
  - coffee/roasting/quality
aliases:
  - SPC in roasting
  - Control charts in roasting
---

# Statistical Process Control

**Tags:** #coffee/roasting #coffee/roasting/quality
**Aliases:** SPC in roasting, Control charts in roasting
**Related:** [Roasting MOC](../maps-of-content/roasting-moc.md) | [Profile Documentation](profile-documentation.md) | [Consecutive Batch Consistency](consecutive-batch-consistency.md) | [Yield Calculation](yield-calculation.md) | [Cropster](cropster.md)
**Status:** ✅ Complete

---

## Overview

Statistical Process Control (SPC) is a quality management methodology that uses statistical methods to monitor and control a production process, distinguishing between normal process variation (common cause) and unusual variation that signals a process problem (special cause). In coffee roasting, SPC provides a rigorous framework for tracking key batch parameters — Drop Temperature, DTR, yield, first crack timing, total roast time — and identifying when the roasting process is drifting outside acceptable limits before it produces out-of-specification batches that fail cupping. While full SPC implementation is most common in large-volume commercial roasting operations, the underlying principles are applicable at any production scale.

## Core SPC Concepts

**Common cause variation:** Natural, inherent variation in the process — the small batch-to-batch fluctuations in RoR, DTR, or yield that occur even when the process is well-managed and in control. Common cause variation is expected and should fall within defined control limits.

**Special cause variation:** Unusual variation caused by a specific, identifiable factor — a change in green coffee moisture, a burner component failure, an operator error, an environmental shift — that is not part of the normal process distribution. Special cause variation signals that the process is out of control and investigation is required.

**Control charts:** The primary SPC tool; a graph of a measured parameter (e.g., Drop Temperature) over sequential batches, with:
- **Centre line:** The process mean (average value across historical batches)
- **Upper Control Limit (UCL):** Mean + 3 standard deviations
- **Lower Control Limit (LCL):** Mean − 3 standard deviations
- **Warning lines:** Mean ± 2 standard deviations (inner limits)

A batch that plots outside the UCL or LCL, or shows a systematic trend (e.g., seven consecutive batches above the centre line), signals a special cause requiring investigation.

## Applying SPC to Coffee Roasting

Key parameters to track on control charts for a consistently roasted production lot:

| Parameter | Control chart type | Typical UCL/LCL range |
| :--- | :--- | :--- |
| Drop temperature | Individual X / moving range | ±4°C from mean |
| DTR | Individual X / moving range | ±3% from mean |
| Total roast time | Individual X / moving range | ±45 seconds from mean |
| Yield | Individual X / moving range | ±2% from mean |
| First crack start time | Individual X / moving range | ±30 seconds from mean |

Control limit values should be calculated from actual process data (a minimum of 20–30 consecutive batches on the same lot and profile) rather than assumed.

## SPC in Practice at Different Scales

**Small specialty roastery:** Full control charts may be impractical with the small number of batches produced per lot. However, tracking key parameters in a simple run chart (sequential plot without formal control limits) still reveals trends, batch-to-batch drift, and outliers visually.

**Medium roastery (50–200 kg/week):** With sufficient batch volume to calculate meaningful statistics, formal control charts per lot are practical. Crop rotation (transitioning from one crop year to the next) is a key special cause event requiring chart reset.

**Large commercial roastery:** Full SPC implementation including automated control chart generation from roast software data is standard practice. Triggers defined out-of-specification (OOS) batches for hold and reinspection before dispatch.

## Benefits of SPC in Roasting

- **Early warning:** Identifies process drift before it produces failed batches; investigation and correction can occur before customer-facing quality impact
- **Separates noise from signal:** Normal variation is expected and does not require action; SPC distinguishes signal (special cause) from noise (common cause), preventing over-correction
- **Objective evidence:** Provides documented, statistical evidence of process performance for quality audits, certification, and wholesale customer reporting
- **Continuous improvement baseline:** Enables tracking of the effect of intentional profile or equipment changes against a statistical baseline

## Key Facts

- SPC distinguishes common cause variation (expected, in-control fluctuation) from special cause variation (process problem requiring investigation)
- Control charts plot key parameters over sequential batches with UCL/LCL at ±3 standard deviations from the mean
- Track: Drop Temperature, DTR, total roast time, yield, first crack timing — all key batch consistency indicators
- Formal SPC is most practical in medium-to-large operations; run charts (sequential plots without formal limits) provide partial benefit at smaller scales
- Calculate control limits from at least 20–30 consecutive historical batches on the same lot and profile

## Related Notes

- [Roasting MOC](../maps-of-content/roasting-moc.md)
- [Profile Documentation](profile-documentation.md)
- [Consecutive Batch Consistency](consecutive-batch-consistency.md)
- [Yield Calculation](yield-calculation.md)
- [Cropster](cropster.md)
- [Production Cupping](production-cupping.md)

## References

- [Rao, S. (2014). *The Coffee Roaster's Companion* — Scott Rao](https://www.scottrao.com/the-coffee-roasters-companion)
- [Montgomery, D.C. (2020). *Introduction to Statistical Quality Control*, 8th ed. — Wiley](https://www.wiley.com/en-us/Introduction+to+Statistical+Quality+Control%2C+8th+Edition-p-9781119399308)
- [Specialty Coffee Association — Quality Systems in Roastery Production](https://sca.coffee/research)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-04-27 | Note created |

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
