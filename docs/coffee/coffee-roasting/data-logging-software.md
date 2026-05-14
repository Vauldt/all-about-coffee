---
tags: []
  - coffee/roasting
  - coffee/roasting/equipment
aliases:
  - Roast data logging
  - Coffee roasting software
---

# Data Logging Software

**Tags:** #coffee/roasting #coffee/roasting/equipment
**Aliases:** Roast data logging, Coffee roasting software
**Related:** [Roasting MOC](../maps-of-content/roasting-moc.md) | [Artisan Software](../roasting-coffee-beans/artisan-software.md) | [Cropster](cropster.md) | [Bean Temperature Probes](../roasting-coffee-beans/bean-temperature-probes.md) | [Profile Documentation](profile-documentation.md)
**Status:** ✅ Complete

---

## Overview

Data logging software in coffee roasting refers to computer applications that connect to temperature sensors (thermocouples) and other instrumentation on a roasting machine, recording real-time data — bean temperature (BT), environmental temperature (ET), Rate of Rise (RoR), burner input, and damper position — and displaying this data as visual curves for the operator to monitor and act on during roasting. Data logging software is the tool that transforms the roasting process from a sensory and judgement-based craft into a data-informed, reproducible science. It enables profile documentation, batch comparison, overlay-based replication, and the export of roast data for analysis.

## Primary Data Logging Functions

**Real-time monitoring:** BT, ET, and RoR are graphed in real time against time, giving the operator a visual representation of roast progress to compare against a reference profile.

**Reference overlay:** Most roasting software allows one or more reference profiles (from previous batches) to be overlaid on the current batch in real time, enabling the operator to see whether the current batch is running ahead of or behind the reference at every point.

**Alarm and annotation:** Operators can mark events (turning point, first crack, first crack end, drop) during the roast; some software triggers alarms at defined temperatures or times.

**Profile storage and retrieval:** Every completed roast is saved with its full data record (time-series temperature data, events, metadata) and can be retrieved for comparison, analysis, or reporting.

**RoR calculation and smoothing:** RoR is mathematically derived from the BT curve (derivative); software applies smoothing algorithms to reduce probe noise and present a readable RoR trace.

**Report generation:** Summary reports, production logs, and session summaries can be exported in PDF or spreadsheet format for quality records.

## Major Data Logging Software Platforms

| Software | Type | Cost | Key features |
| :--- | :--- | :--- | :--- |
| Artisan | Open-source desktop app | Free | Full profile logging, overlay, RoR; highly configurable; compatible with a wide range of hardware via Phidgets, Modbus, and serial interfaces |
| Cropster | Cloud-based SaaS | Subscription | Integrates roast logging with inventory, production planning, cupping, and ordering; real-time cloud sync; professional operations focus |
| RoastLog | Cloud-based | Subscription | Similar to Cropster; smaller market presence |
| Ikawa app | Device-specific | Free with device | Controls and logs Ikawa sample roaster profiles; highly precise for small batches |
| Probat Profile | Proprietary | Included with equipment | Probat roaster-specific; integrated hardware/software |

## Hardware Requirements

Data logging software connects to the roaster via:
- **Phidgets USB modules:** Common with Artisan; connect Type K thermocouples to a computer via USB; widely compatible
- **Modbus protocol:** Used by many commercial roasters for direct hardware integration with logging software
- **VINT hubs (Phidgets):** More recent Phidgets architecture; supports multiple sensors
- **Direct serial connection:** Some older roasters use RS-232 serial data output for direct connection

## Data-Informed Roasting vs. Instrument-Dependent Roasting

Data logging is a tool, not a replacement for roasting skill and sensory evaluation:
- A roaster who only watches the screen and does not attend to the sensory cues (aroma, first crack sound, visual observation) may miss critical real-time information that software cannot capture
- Conversely, a roaster who roasts entirely by feel without data logging cannot reproducibly replicate profiles or diagnose causes of quality variation
- Best practice integrates both: data logging for documentation, reproducibility, and trend analysis; direct observation for in-the-moment process management

## Key Facts

- Data logging software records BT, ET, RoR, and operator inputs in real time for monitoring and documentation
- Reference overlay — displaying the current batch against a saved reference — is the primary replication tool
- Artisan (free, open-source) and Cropster (commercial SaaS) are the dominant platforms in specialty coffee
- Hardware: Phidgets USB modules with Type K thermocouples is the most common Artisan setup; commercial roasters often use Modbus integration
- Data logging is a tool for reproducibility and diagnosis; sensory attention to the roast remains essential alongside the software

## Related Notes

- [Roasting MOC](../maps-of-content/roasting-moc.md)
- [Artisan Software](../roasting-coffee-beans/artisan-software.md)
- [Cropster](cropster.md)
- [Bean Temperature Probes](../roasting-coffee-beans/bean-temperature-probes.md)
- [Thermocouples](thermocouples.md)
- [Profile Documentation](profile-documentation.md)
- [Roast Logging](roast-logging.md)

## References

- [Artisan Software — Documentation and User Guide](https://artisan-scope.org)
- [Cropster — Roastery Platform](https://www.cropster.com)
- [Phidgets — Thermocouple Interface Hardware](https://www.phidgets.com)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-04-27 | Note created |

---

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
