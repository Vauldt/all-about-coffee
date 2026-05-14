---
tags: []
  - coffee/roasting
  - coffee/roasting/thermodynamics
aliases:
  - Convective heat transfer coefficient
  - Roasting heat transfer
---

# Heat Transfer Coefficient

**Tags:** #coffee/roasting #coffee/roasting/thermodynamics
**Aliases:** Convective heat transfer coefficient, Roasting heat transfer
**Related:** [Roasting MOC](../maps-of-content/roasting-moc.md) | [Thermal Conductivity](thermal-conductivity.md) | [Heat Capacity](heat-capacity.md) | [Convection](convection.md) | [Conduction](conduction.md)
**Status:** ✅ Complete

---

## Overview

The heat transfer coefficient (h) is a physical parameter that quantifies the rate of heat exchange between a fluid (air or gas) and a solid surface (the coffee bean) per unit area per unit temperature difference. It is expressed in watts per square metre per kelvin (W/m²·K). In coffee roasting, the heat transfer coefficient governs how efficiently hot air in the drum delivers thermal energy to the surface of the coffee bean by convection. A higher heat transfer coefficient means more heat is delivered per degree of temperature difference between the air and the bean surface for a given contact area — producing faster bean heating and a steeper Rate of Rise.

## Factors Affecting the Heat Transfer Coefficient in Coffee Roasting

The convective heat transfer coefficient in a drum roaster depends on several variables:

**Air velocity:** Higher airflow velocity through the drum increases the turbulence of the boundary layer around each bean, reducing the thickness of the insulating stagnant air layer at the bean surface. This increases h. Increasing the damper opening (more airflow) generally increases convective heat transfer coefficient, within limits set by the fan and duct design.

**Air temperature:** The thermal properties of air change slightly with temperature; at higher temperatures, the heat transfer coefficient is marginally higher. This is a secondary effect compared to velocity.

**Bean surface geometry:** The size, shape, and surface texture of coffee beans affect how air flows around them. Larger beans (higher screen number) have a higher surface-area-to-volume ratio per unit of surface, but the boundary layer behaviour also changes with bean geometry.

**Drum agitation:** The rotating drum and flights tumble the bean mass, continuously exposing new bean surfaces to the hot airstream. Better agitation increases the effective heat transfer coefficient for the batch as a whole by minimising beans that remain in prolonged contact with one another (reducing conduction between cool beans).

## Practical Significance for Roasting

In practice, the heat transfer coefficient is not directly measured by roasters — it is an underlying parameter whose effects are observed through the Rate of Rise and the response of the roast profile to burner and damper adjustments:

- **High h:** Bean temperature rises quickly in response to gas and airflow input; sharp, responsive RoR
- **Low h:** Bean temperature responds more slowly; RoR is sluggish relative to heat input; the roast feels "unresponsive"

Differences in heat transfer coefficient between roaster models and design types partly explain why:
- A fluid bed roaster (high convection, very high h) requires significantly lower gas temperatures to achieve the same RoR as a drum roaster
- A drum roaster with high drum speed (more agitation) has a higher effective h than the same roaster at low drum speed
- A very full drum batch has lower effective h than a smaller batch, because beans are in contact with each other rather than the airstream

## Relationship to Roast Profile Design

Roasters do not calculate h directly, but understanding the concept helps explain:
- Why increasing airflow at a fixed gas setting can increase or decrease RoR depending on whether the air is hotter or cooler than the beans
- Why drum speed affects development consistency — lower drum speed reduces agitation, lowering effective h and potentially producing less even heat transfer across the bean mass
- Why different roaster designs require different profile parameters even for the same green coffee

## Key Facts

- Heat transfer coefficient (h) quantifies convective heat delivery from air to bean surface; units W/m²·K
- Higher h = faster, more responsive heat delivery; determined by air velocity, drum agitation, and bean geometry
- Fluid bed roasters have higher h than drum roasters; hence lower gas temperatures produce equivalent RoR
- Higher drum speed increases effective h by improving agitation and bean surface exposure
- Roasters do not measure h directly; its effects are seen in RoR responsiveness to damper and gas adjustments

## Related Notes

- [Roasting MOC](../maps-of-content/roasting-moc.md)
- [Thermal Conductivity](thermal-conductivity.md)
- [Heat Capacity](heat-capacity.md)
- [Convection](convection.md)
- [Conduction](conduction.md)
- [Rate of Rise](rate-of-rise.md)
- [Airflow Control](../roasting-coffee-beans/airflow-control.md)

## References

- [Rao, S. (2014). *The Coffee Roaster's Companion* — Scott Rao](https://www.scottrao.com/the-coffee-roasters-companion)
- [Incropera, F.P. et al. (2007). *Fundamentals of Heat and Mass Transfer*, 6th ed. — Wiley](https://www.wiley.com/en-us/Fundamentals+of+Heat+and+Mass+Transfer%2C+6th+Edition-p-9780471457282)
- [Specialty Coffee Association — Roasting Science and Thermodynamics](https://sca.coffee/research)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-04-27 | Note created |

---

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
