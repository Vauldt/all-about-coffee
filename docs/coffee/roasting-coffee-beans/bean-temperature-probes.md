---
tags: []
  - coffee/roasting
  - coffee/roasting/equipment
aliases:
  - Bean probe
  - BT probe
  - Roaster temperature probe
---

# Bean Temperature Probes

**Tags:** #coffee/roasting #coffee/roasting/equipment
**Aliases:** Bean probe, BT probe, Roaster temperature probe
**Related:** [Roasting MOC](../maps-of-content/roasting-moc.md) | [Thermocouples](../coffee-roasting/thermocouples.md) | [Rate of Rise](../coffee-roasting/rate-of-rise.md) | [Drop Temperature](../coffee-roasting/drop-temperature.md) | [Artisan Software](artisan-software.md)
**Status:** ✅ Complete

---

## Overview

Bean temperature probes — also called bean probes or BT probes — are temperature sensors positioned inside the roasting drum that measure the temperature of the coffee bean mass during roasting. Together with the environmental temperature (ET) probe, which measures the drum air temperature, the bean probe is one of the two primary data inputs for roast profile monitoring and logging. The BT reading drives the Rate of Rise (RoR) curve in profile software, and the BT reading at drop defines the Drop Temperature for each batch. Understanding what bean probes actually measure — and their limitations — is essential for interpreting roast profile data correctly.

## What Bean Probes Measure

Despite the name, bean temperature probes do not measure the internal temperature of individual coffee beans. They measure the temperature of the thermocouple junction, which is surrounded by the tumbling bean mass inside the drum. The probe reading is therefore:

- **A surface temperature:** The probe junction reads the temperature of beans and hot air contacting it, not the bean core temperature
- **A mass average:** The reading reflects the average temperature of the beans and gas in the immediate vicinity of the probe
- **A lagging indicator:** Due to thermal mass, the probe response to changes in bean or gas temperature is delayed; faster temperature changes are under-represented in the probe reading

This means:
- The RoR (rate of temperature rise) calculated from BT is a smoothed, lagging representation of actual heat delivery rate
- First crack may begin at a slightly lower actual bean core temperature than the BT reading suggests, because the probe reads surface and gas temperature
- The absolute BT number is roaster-specific and not directly comparable between different roasters without calibration

## Physical Characteristics of Bean Probes

Most commercial and prosumer roasters use thermocouple-based bean probes, typically:
- **Type K thermocouple:** The most common; accurate over the full range of roasting temperatures (0–1,000°C); see [Thermocouples](../coffee-roasting/thermocouples.md)
- **Probe diameter:** 1–4 mm; thinner probes have faster response time but are more fragile
- **Probe placement:** The probe tip is positioned in the centre of the drum's tumbling bean mass zone; exact positioning varies by roaster model
- **Connection:** Via a thermocouple port on the roaster control panel, which connects to a data logger (built-in or external, such as Phidgets)

## BT vs ET Probes

Commercial roasters typically have two probes:

| Probe | Measures | Common abbreviation | Use |
| :--- | :--- | :--- | :--- |
| Bean temperature probe | Temperature of bean mass (and surrounding gas) | BT | Primary RoR tracking; Drop Temperature reference |
| Environmental temperature probe | Temperature of gas/air in drum environment | ET | Charge temperature setting; heat transfer assessment |

The difference between ET and BT — the ET-BT delta — changes across the roast:
- At charge, ET is much higher than BT (drum is hot; beans are cold)
- Delta narrows as beans absorb heat through the roast
- At drop, ET and BT may be within a few degrees of each other in a well-managed roast

The ET-BT delta can serve as a proxy for the rate of heat transfer from the drum to the bean mass; a narrowing delta indicates diminishing temperature driving force, useful for monitoring development intensity.

## Probe Placement and Calibration

**Probe placement significantly affects readings.** A probe positioned closer to the drum wall reads higher temperatures (more radiant and conductive heat from the drum); a probe positioned more centrally in the bean mass reads closer to actual bean surface temperature. Different roaster models position probes differently, which is a key reason BT numbers are not directly transferable between roasters.

**Calibration:** Bean probes should be verified for accuracy periodically using an ice-water bath (0°C reference) or a boiling water bath (100°C adjusted for altitude). A probe reading 5°C high throughout the roast will produce a systematic error in Drop Temperature and RoR reference targets.

## Reading BT Data in Profile Software

In roast profile software (Artisan, Cropster), the BT channel generates:
- **BT curve:** Temperature vs. time; the primary visual reference for roast progress
- **RoR (derivative of BT):** Rate of change of BT over time, typically in °C per minute
- **Turning point:** The minimum BT value after charge, where the curve inflects upward
- **Drop temperature:** The BT reading at the moment beans are discharged from the drum

These data points form the basis for profile comparison, batch consistency tracking, and profile refinement across the bean temperature trace.

## Key Facts

- Bean probes measure the temperature of the bean mass surface and surrounding gas, not the internal bean temperature; readings are a lagging, surface-weighted average
- Type K thermocouples are standard; probe diameter affects response speed
- BT numbers are roaster-specific; do not compare absolute values between different roaster models without calibration
- The ET-BT delta narrows across the roast as the bean mass absorbs heat; useful as a qualitative heat transfer indicator
- Calibrate probes periodically; a systematic offset error affects Drop Temperature targets and RoR reference curves

## Related Notes

- [Roasting MOC](../maps-of-content/roasting-moc.md)
- [Thermocouples](../coffee-roasting/thermocouples.md)
- [Rate of Rise](../coffee-roasting/rate-of-rise.md)
- [Drop Temperature](../coffee-roasting/drop-temperature.md)
- [Artisan Software](artisan-software.md)
- [Cropster](../coffee-roasting/cropster.md)
- [Roast Logging](../coffee-roasting/roast-logging.md)

## References

- [Rao, S. (2014). *The Coffee Roaster's Companion* — Scott Rao](https://www.scottrao.com/the-coffee-roasters-companion)
- [Artisan Software — Thermocouple and Probe Setup Documentation](https://artisan-scope.org)
- [Cropster — Data Logging and Probe Integration](https://www.cropster.com)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-04-27 | Note created |

---

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
