---
tags: []
  - coffee/roasting
  - coffee/roasting/profile
aliases:
  - RoR
  - Rate of rise roasting
  - Bean temperature rate of rise
---

# Rate of Rise

**Tags:** #coffee/roasting #coffee/roasting/profile
**Aliases:** RoR, Rate of rise roasting, Bean temperature rate of rise
**Related:** [Roasting MOC](../maps-of-content/roasting-moc.md) | [Development Time Ratio](development-time-ratio.md) | [First Crack](../roasting-coffee-beans/first-crack.md) | [Roast Profile](roast-profile.md) | [Charge Temperature](charge-temperature.md)
**Status:** ✅ Complete

---

## Overview

Rate of Rise (RoR) is the speed at which bean temperature increases during a coffee roast, measured in degrees per minute (°C/min or °F/min). It is the primary real-time control variable available to a roaster during a roast and the central diagnostic metric used to evaluate whether a roast is progressing according to plan. A declining RoR profile — in which the rate of temperature increase slows progressively from charge to drop — is the widely accepted standard for quality roasting, reflecting controlled heat transfer that avoids baking, scorching, or underdevelopment. Roasters read RoR through logging software such as Cropster or Artisan, which plot bean temperature and its derivative (RoR) as real-time curves throughout the roast.

## What Rate of Rise Measures

RoR is mathematically the first derivative of the bean temperature curve with respect to time:

```
RoR = ΔT / Δt   (°C per minute)
```

At any moment in the roast, RoR describes how quickly the beans are gaining heat. A high RoR means beans are heating rapidly; a low RoR means heating has slowed; a RoR of zero means bean temperature has plateaued; a negative RoR (a "crash") means beans are cooling, which is highly undesirable before the intended drop.

## Typical RoR Curve Shape

A well-structured roast follows a characteristic RoR trajectory:

| Phase | Typical RoR | What Is Happening |
| :--- | :--- | :--- |
| Charge to Turning Point | Negative, then rising sharply | Cold beans absorb heat; temperature initially drops then climbs |
| Early drying phase | 8–12 °C/min | Beans heating rapidly; moisture evaporating |
| Mid-roast | 5–8 °C/min | Sustained heat input; Maillard reactions beginning |
| Approaching first crack | 3–6 °C/min | Rate declining; exothermic reactions beginning |
| Development phase | 2–4 °C/min | Controlled, declining rate; critical flavour development |
| Drop | Controlled drop at planned DTR | Roast terminated before RoR crashes or plateaus |

The key principle is **monotonic decline**: RoR should fall steadily throughout the roast without flattening or reversing. A flattening RoR (often called a "stall") is associated with baked flavours — flat, cereal-like, lacking sweetness. A crashing RoR before drop produces underdevelopment. A RoR that climbs before first crack risks tipping or scorching.

## RoR and Flavour Development

The RoR profile directly influences flavour outcomes because it controls the rate of chemical reactions during roasting:

- **Too-high RoR through first crack:** Rapid heat input drives fast Maillard reactions and caramelisation; can produce a harsh, sharp, unintegrated acidity and under-ripe fruit notes
- **Declining RoR through development:** Allows the reactions initiated at first crack to complete in a controlled manner, integrating acidity, sweetness, and body into a coherent whole
- **Stalling RoR (plateau):** Extended dwell at a fixed temperature drives baking reactions; sweetness degrades; the cup becomes flat and hollow
- **RoR crash before drop:** Rapid heat loss from the beans mid-roast indicates the roaster has removed too much heat input; associated with underdevelopment and grassy or peanut-like flavours

## Controlling RoR

Roasters adjust RoR through two primary inputs:

**Gas (heat input):** Increasing gas pressure raises the rate of heat input to the drum and beans, pushing RoR up. Decreasing gas lowers heat input, allowing RoR to decline.

**Airflow:** Increasing airflow through the drum removes heat from the roasting environment, effectively reducing RoR. Reducing airflow retains heat and maintains or raises RoR.

The interaction between gas and airflow — and the thermal inertia of the roasting drum — means that changes in RoR lag behind adjustments by 30–60 seconds, requiring anticipatory control rather than reactive adjustment.

## RoR Analysis Software

Real-time RoR tracking requires data logging software connected to the roaster's temperature probes. The two most widely used platforms are:

- **[Cropster](https://www.cropster.com):** Industry-standard commercial platform; cloud-based; used by most large specialty roasters for profile storage, roast comparison, and green coffee tracking
- **[Artisan](https://artisan-scope.org):** Free, open-source roast logging software; widely used by smaller roasters and home roasters; supports most commercial data logger interfaces

Both platforms display real-time bean temperature and RoR curves simultaneously, enabling roasters to compare live roasts against saved reference profiles and make informed adjustments.

## Common RoR Problems and Corrections

| Problem | RoR Symptom | Likely Cause | Correction |
| :--- | :--- | :--- | :--- |
| Baked roast | RoR plateau during development | Insufficient heat input; low gas or excess airflow | Increase gas before development phase |
| Scorched roast | Spike in early RoR | Charge temperature too high; excessive initial gas | Lower charge temperature; reduce opening gas |
| Underdevelopment | RoR crash before first crack | Heat removed too quickly | Reduce airflow reduction rate; maintain gas input |
| Runaway roast | RoR fails to decline | Insufficient airflow; excess gas input | Increase airflow; reduce gas after midpoint |

## Key Facts

- RoR is measured in °C/min (or °F/min) and is the first derivative of the bean temperature curve
- Optimal profile: continuously declining from charge to drop with no plateaux or reversals
- A stalling RoR is the most common cause of baked, flat cup profiles
- Changes in gas or airflow affect RoR with a lag of 30–60 seconds due to drum thermal inertia
- Tracked in real time via Cropster or Artisan software connected to bean temperature probes
- RoR at first crack is typically 3–6 °C/min in a well-structured roast; development phase RoR typically 2–4 °C/min

## Related Notes

- [Roasting MOC](../maps-of-content/roasting-moc.md)
- [Development Time Ratio](development-time-ratio.md)
- [First Crack](../roasting-coffee-beans/first-crack.md)
- [Charge Temperature](charge-temperature.md)
- [Roast Profile](roast-profile.md)
- [Cropster](cropster.md)
- [Artisan Software](../roasting-coffee-beans/artisan-software.md)

## References

- [Rao, S. (2014). *The Coffee Roaster's Companion* — Scott Rao](https://www.scottrao.com/the-coffee-roasters-companion)
- [Artisan Roast Logging Software — Documentation and guides](https://artisan-scope.org)
- [Cropster — Rate of Rise explainer](https://www.cropster.com/blog/rate-of-rise-coffee-roasting/)
- [Specialty Coffee Association — Roasting Foundations Course](https://sca.coffee/education/courses)
- [Sivetz, M. & Foote, H.E. (1963). *Coffee Processing Technology* — AVI Publishing](https://archive.org/details/coffeeprocessin00sive)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-04-27 | Note created |

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
