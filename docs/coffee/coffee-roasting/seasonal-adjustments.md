---
tags: []
  - coffee/roasting
  - coffee/roasting/production
aliases:
  - Seasonal roast adjustments
  - Environmental roast compensation
---

# Seasonal Adjustments

**Tags:** #coffee/roasting #coffee/roasting/production
**Aliases:** Seasonal roast adjustments, Environmental roast compensation
**Related:** [Roasting MOC](../maps-of-content/roasting-moc.md) | [Profile Replication](profile-replication.md) | [Consecutive Batch Consistency](consecutive-batch-consistency.md) | [Bean Temperature Probes](../roasting-coffee-beans/bean-temperature-probes.md) | [Rate of Rise](rate-of-rise.md)
**Status:** ✅ Complete

---

## Overview

Seasonal adjustments in coffee roasting are deliberate changes made to roast profile parameters — most commonly charge temperature — to compensate for predictable changes in ambient environmental conditions across seasons. Temperature and humidity in the roastery change significantly between winter and summer, altering the thermal behaviour of the roasting drum and the incoming air supply. Without compensating adjustments, the same nominal profile settings (charge temperature, burner input, damper) will produce different RoR behaviour and different cup outcomes as conditions change. Seasonal adjustment is a routine part of production profile maintenance in roasteries operating in climates with pronounced seasonal temperature variation.

## How Ambient Conditions Affect the Roast

**Ambient temperature:**
- In winter (cold ambient temperature): the intake air drawn through the drum is colder than in summer; the drum environment loses more heat to the surrounding cold roastery structure; green coffee stored in an unheated roastery arrives colder to the drum
- Net effect: the early RoR (drying phase) is slower in winter; the roast takes longer to reach turning point and may have a slower rise through browning
- Correction: raise charge temperature by 3–8°C in winter relative to summer reference

**Ambient humidity:**
- Low humidity (dry conditions, common in winter or arid climates): the green coffee in storage loses moisture; green coffee that has dried from 12% to 10.5% moisture has less endothermic buffering in the drying phase; early RoR climbs faster
- Net effect: drier green coffee roasts "faster" through the drying phase and may reach first crack earlier than expected
- Correction: reduce charge temperature slightly for very dry conditions; or shorten the preheat period

**Combined effects:**
- In cold, dry conditions (typical winter): lower temperature slows the early roast; lower moisture speeds it — the effects partially cancel out but must still be tracked
- In hot, humid conditions (typical summer): higher ambient temperature accelerates early roast; higher moisture buffers it — again, effects partially offset

## Developing Seasonal Adjustment Values

Seasonal adjustments cannot be calculated from first principles for a given roastery — they must be determined empirically by:

1. **Tracking profile data across seasons:** Log charge temperature, turning point time and temperature, first crack start time, and DTR across multiple months. Systematic drift in these values signals that an adjustment is needed.

2. **Establishing seasonal compensation values:** Once the drift pattern is clear, determine the charge temperature adjustment required to return the profile to its summer reference performance. Common values: ±3–8°C depending on roaster type and climate severity.

3. **Documenting the compensation schedule:** Record the seasonal adjustment values alongside the base profile documentation; operators should know when and how much to adjust.

## Example Seasonal Adjustment Protocol

A roastery in Melbourne, Australia operating a 15 kg drum roaster:

| Season | Ambient temp range | Humidity | Charge temp adjustment |
| :--- | :--- | :--- | :--- |
| Summer (Dec–Feb) | 25–35°C | 50–70% RH | Base (0°C) |
| Autumn (Mar–May) | 15–25°C | 45–65% RH | −2°C |
| Winter (Jun–Aug) | 8–16°C | 40–55% RH | −5 to −8°C |
| Spring (Sep–Nov) | 15–25°C | 45–65% RH | −2 to −3°C |

In this protocol, "base" is the summer reference; winter charge temperatures are reduced relative to summer to compensate for the overall faster early-roast behaviour (colder ambient — slower drum, but the operator adjusts upward to compensate — actually, since colder ambient means less heat loss, adjust downward). Note: the direction of adjustment is roaster-specific and must be verified through observation.

## Other Sources of Environmental Drift

Beyond seasonal variation, similar adjustment logic applies to:
- **Time of day:** A roastery that warms significantly during a long session may require charge temperature adjustment for afternoon batches relative to morning batches
- **Lot transitions:** Transitioning to a new green coffee lot with different moisture or density requires profile adjustment even if the roast target is identical
- **Equipment maintenance:** Cleaning or replacing drum flights, relining a drum, or adjusting burner components can shift profile behaviour

## Key Facts

- Ambient temperature and humidity change across seasons and alter RoR behaviour at fixed profile settings
- Cold ambient → slower early drying/browning; correct by raising charge temperature or extending preheat
- Dry conditions → faster drying phase (less moisture buffer); correct by slightly reducing charge or monitoring more carefully
- Seasonal adjustment values (typically ±3–8°C on charge temperature) must be determined empirically per roaster through multi-month profile tracking
- Document seasonal adjustment values alongside base profile documentation; update when significant drift is confirmed

## Related Notes

- [Roasting MOC](../maps-of-content/roasting-moc.md)
- [Profile Replication](profile-replication.md)
- [Consecutive Batch Consistency](consecutive-batch-consistency.md)
- [Bean Temperature Probes](../roasting-coffee-beans/bean-temperature-probes.md)
- [Rate of Rise](rate-of-rise.md)
- [Moisture Loss](moisture-loss.md)

## References

- [Rao, S. (2014). *The Coffee Roaster's Companion* — Scott Rao](https://www.scottrao.com/the-coffee-roasters-companion)
- [Specialty Coffee Association — Roasting Production Standards](https://sca.coffee/research)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-04-27 | Note created |

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
