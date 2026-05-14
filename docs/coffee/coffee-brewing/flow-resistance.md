---
tags: []
  - coffee/brewing
  - coffee/science
  - coffee/equipment
aliases:
  - Puck resistance
  - Coffee bed resistance
  - Hydraulic resistance espresso
---

# Flow Resistance

**Tags:** #coffee/brewing #coffee/science #coffee/equipment
**Aliases:** Puck resistance, Coffee bed resistance, Hydraulic resistance espresso
**Related:** [Espresso Pressure](../brewing/coffee-brewing-espresso/espresso-pressure.md) | [Flow Rate](flow-rate.md) | ../Maps of Content/Grind Size MOC | [Espresso MOC](../maps-of-content/espresso-moc.md) | [Pressure Brewing](pressure-brewing.md) | [Particle Uniformity](particle-uniformity.md)
**Status:** ✅ Complete

---

## Overview

Flow resistance is the opposition a coffee bed or filter offers to the passage of water under pressure. In espresso brewing, flow resistance is the primary mechanism that converts pump pressure into the controlled, slow flow rate required for espresso extraction — without sufficient resistance, water passes through the coffee too quickly to achieve adequate extraction. Flow resistance is determined by the coffee bed's physical properties (grind size, dose, tamp pressure, particle uniformity, and puck integrity) and is the key variable that baristas manipulate through grind adjustment to achieve target shot parameters. Understanding flow resistance is fundamental to diagnosing and resolving espresso extraction problems.

## Darcy's Law and Coffee Flow

Flow through a porous medium (such as a coffee puck) is described by **Darcy's Law**:

**Q = (k × A × ΔP) / (μ × L)**

Where:
- **Q** = volumetric flow rate (ml/s)
- **k** = permeability of the coffee bed (inversely related to resistance)
- **A** = cross-sectional area of the puck
- **ΔP** = pressure differential across the puck (pump pressure minus atmospheric)
- **μ** = dynamic viscosity of water
- **L** = thickness (depth) of the coffee puck

Practically: **Flow rate is proportional to pressure and inversely proportional to resistance**. A tighter, less permeable puck (higher resistance) at fixed pump pressure produces a slower flow rate; a looser puck produces a faster flow rate.

## Factors Determining Flow Resistance

### Grind Size

The most critical variable. Finer grinding produces smaller particles with more surface area and smaller interstitial spaces — dramatically increasing flow resistance. This is the primary adjustment baristas make to control shot time:
- **Too coarse** → low resistance → fast flow → under-extraction (short, thin, sour shots)
- **Too fine** → high resistance → very slow flow or no flow → over-extraction or choked shot

### Dose

More coffee mass in a fixed basket size increases puck depth (L in Darcy's law) and packing density — increasing resistance. A higher dose at the same grind will produce a slower shot.

### Tamp Pressure and Evenness

Tamping compresses the coffee bed, reducing interstitial space and increasing packing density. Consistent tamp pressure (typically 15–20 kg) is important for reproducibility — but variation in tamp pressure has less effect on resistance than grind size variation. Uneven tamping creates differential resistance zones that contribute to channelling.

### Particle Uniformity

A non-uniform grind (wide particle size distribution) creates a mixed-resistance bed — fine particles pack tightly and create high-resistance zones; coarse particles form low-resistance channels. The result is uneven flow and channelling, not predictably controlled resistance.

### Channelling

**Channelling** occurs when water finds a path of least resistance through the puck — either through a crack, a low-density area, or around the puck edge — and bypasses most of the coffee bed. Channelling dramatically reduces effective flow resistance in the channel while starving the rest of the puck of water. It produces:
- Fast, light, sour shots (under-extraction in most of the puck)
- Sometimes an initial normal time followed by a sudden "blond" fast tail
- Visible as uneven extraction on the puck after the shot

### Puck Integrity

Swelling, cracking, or deformation of the puck during pre-infusion or at the onset of full pressure can create channels and reduce resistance unpredictably. Techniques to maintain puck integrity:
- Pre-infusion (gentle initial pressure to saturate before full pressure)
- WDT distribution (break up internal clumps before tamping)
- Appropriate grind fineness (very fine grinds are more prone to channelling at puck edges)

## Flow Resistance and Shot Diagnosis

| Symptom | Flow resistance indication | Likely cause |
| :--- | :--- | :--- |
| Shot runs fast (< 20 sec for 36 g out from 18 g in) | Too low | Grind too coarse; under-dose |
| Shot runs slow (> 40 sec) | Too high | Grind too fine; over-dose; choking |
| Shot starts slow then speeds up | Channelling developing | Puck cracking; uneven distribution |
| Shot appears fast despite fine grind | Channelling | Uneven tamp; puck bypass |

## Key Facts

- Flow resistance is the property of the espresso puck that converts pump pressure into the controlled slow flow rate needed for extraction
- Described by Darcy's Law: flow rate is proportional to pressure and inversely proportional to puck resistance
- Grind size is the primary determinant of flow resistance — finer grinds dramatically increase resistance
- Dose, tamp pressure, and particle uniformity also affect resistance; channelling dramatically reduces effective resistance
- Target: approximately 25–35 seconds for a standard espresso shot (18 g in, 36 g out) at 9 bar pump pressure
- Channelling is the most common cause of unexpected fast shots or inconsistent extraction at a fixed grind setting

## Related Notes

- [Espresso Pressure](../brewing/coffee-brewing-espresso/espresso-pressure.md)
- [Flow Rate](flow-rate.md)
- ../Maps of Content/Grind Size MOC
- [Particle Uniformity](particle-uniformity.md)
- [WDT - Weiss Distribution Technique](../brewing/coffee-brewing-espresso/wdt-weiss-distribution-technique.md)
- [Espresso MOC](../maps-of-content/espresso-moc.md)

## References

- [Illy, A. & Viani, R. (eds.) (2005). *Espresso Coffee: The Science of Quality* (2nd ed.). Elsevier Academic Press.](https://www.elsevier.com/books/espresso-coffee/illy/978-0-12-370371-2)
- [Perger, M. — Barista Hustle: The Espresso Guide](https://www.baristahustle.com/learn/espresso)
- [Cameron, M. et al. (2020). Systematically improving espresso: Insights from mathematical modelling and experiment. *Matter*.](https://doi.org/10.1016/j.matt.2019.12.019)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-04-28 | Note created |

---

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
