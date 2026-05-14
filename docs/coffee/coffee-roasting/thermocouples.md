---
tags: []
  - coffee/roasting
  - coffee/equipment
  - coffee/equipment/roaster
aliases:
  - Thermocouple probes
  - K-type thermocouple
  - Coffee roasting thermocouples
---

# Thermocouples

**Tags:** #coffee/roasting #coffee/equipment #coffee/equipment/roaster
**Aliases:** Thermocouple probes, K-type thermocouple, Coffee roasting thermocouples
**Related:** [Roasting MOC](../maps-of-content/roasting-moc.md) | [Cropster](cropster.md) | [Artisan Software](../roasting-coffee-beans/artisan-software.md) | [Rate of Rise](rate-of-rise.md) | [Roast Profile](roast-profile.md) | [Data Logging Software](data-logging-software.md)
**Status:** ✅ Complete

---

## Overview

Thermocouples are temperature-sensing devices that measure temperature by detecting the voltage difference produced when two dissimilar metals are joined at a junction. In coffee roasting, thermocouples are the standard instrument for measuring bean temperature (the probe inserted into the bean mass) and environmental temperature (the drum air temperature probe), providing the real-time data that feeds roast logging software such as Artisan and Cropster. The accuracy, placement, and responsiveness of thermocouples directly affect the reliability of roast profile data — a poorly positioned or damaged probe produces readings that cannot be used for accurate profile replication.

## How Thermocouples Work

A thermocouple consists of two wires of different metals joined at one end (the measuring junction) and connected to a measurement instrument at the other end (the reference junction). When the measuring junction is at a different temperature from the reference junction, a small voltage (the Seebeck voltage) is generated proportional to the temperature difference. The measurement instrument reads this voltage and converts it to a temperature reading using calibration tables specific to the metal combination.

The most common thermocouple type in coffee roasting is the **K-type** (chromel/alumel), which:

- Measures accurately from −200 °C to +1350 °C
- Is inexpensive and widely available
- Provides fast response and good sensitivity in the 100–300 °C range used in coffee roasting
- Is compatible with the data loggers and interfaces used by Artisan, Cropster, and most roaster manufacturers

## Probe Placement in Drum Roasters

Two thermocouple probes are standard in profiled drum roasting:

**Bean probe (BT — Bean Temperature):**
- Positioned to contact the tumbling bean mass inside the drum
- Measures the temperature of the beans directly (or, more precisely, the temperature at the bean mass surface in contact with the probe tip)
- This probe generates the primary curve used for roast profiling — the bean temperature curve (BT)
- Placement depth inside the drum affects the reading; probes that do not penetrate far enough into the bean mass read closer to air temperature

**Environmental probe (ET — Environmental Temperature):**
- Positioned in the drum air space, away from the bean mass
- Measures the temperature of the heated air environment inside the drum
- Used to calculate delta between air and bean temperatures, informing heat transfer dynamics
- Also used to track pre-charge drum temperature (charge temperature is typically taken from ET when it reads the empty drum)

## Thermocouple Response Time and Smoothing

Thermocouples have a thermal response time — the time it takes for the probe to reach equilibrium with the surrounding temperature. A fine-wire probe responds faster than a thick-mass probe. In roast logging software, the Rate of Rise (RoR) is derived from the rate of change of the BT curve; if the thermocouple has a slow response time, the RoR curve appears smooth but lags behind actual temperature changes. Artisan and Cropster apply RoR smoothing algorithms to reduce noise from fast thermocouples while maintaining responsiveness.

## Key Facts

- Thermocouples: temperature sensors generating voltage from two dissimilar metal junctions; voltage proportional to temperature
- K-type (chromel/alumel) is the standard type for coffee roasting equipment
- Two probes standard in profiled roasting: bean probe (BT) and environmental probe (ET)
- BT probe measures the bean mass temperature and generates the primary profile curve
- ET probe measures drum air temperature; used for charge temperature reference
- Compatible with Artisan and Cropster via USB data loggers (Phidgets and others)
- Response time affects RoR calculation; software smoothing algorithms compensate for probe lag

## Related Notes

- [Roasting MOC](../maps-of-content/roasting-moc.md)
- [Cropster](cropster.md)
- [Artisan Software](../roasting-coffee-beans/artisan-software.md)
- [Rate of Rise](rate-of-rise.md)
- [Roast Profile](roast-profile.md)
- [Data Logging Software](data-logging-software.md)
- [Charge Temperature](charge-temperature.md)

## References

- [Rao, S. (2014). *The Coffee Roaster's Companion* — Scott Rao](https://www.scottrao.com/the-coffee-roasters-companion)
- [Artisan Roast Logger — Hardware and Thermocouple Setup Guide](https://artisan-scope.org)
- [Specialty Coffee Association — Roasting Professional Certificate](https://sca.coffee/education/courses)
- [Phidgets — Data Loggers and Thermocouple Interfaces for Coffee Roasting](https://www.phidgets.com)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-04-27 | Note created |

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
