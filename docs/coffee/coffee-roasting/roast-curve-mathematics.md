---
tags: []
  - coffee/roasting
  - coffee/roasting/profile
aliases:
  - Roast profile mathematics
  - Mathematical analysis of roast curves
---

# Roast Curve Mathematics

**Tags:** #coffee/roasting #coffee/roasting/profile
**Aliases:** Roast profile mathematics, Mathematical analysis of roast curves
**Related:** [Roasting MOC](../maps-of-content/roasting-moc.md) | [Rate of Rise](rate-of-rise.md) | [Development Time Ratio](development-time-ratio.md) | [Artisan Software](../roasting-coffee-beans/artisan-software.md) | [Predictive Modelling](predictive-modelling.md)
**Status:** ✅ Complete

---

## Overview

Roast curve mathematics refers to the quantitative analysis of roast profile data — the numerical and statistical operations applied to time-temperature curves, their derivatives (Rate of Rise), and derived metrics (DTR, turning point, development time) to characterise, compare, and optimise roast profiles. As digital data logging has made roast curves routinely available in specialty coffee, the tools of applied mathematics — calculus, statistics, curve fitting, and numerical analysis — have become relevant to roasters who want to move beyond visual intuition to systematic, quantifiable profile assessment.

## Key Mathematical Concepts in Roast Curve Analysis

### Derivative: Rate of Rise

The Rate of Rise (RoR) is the mathematical derivative of the bean temperature (BT) curve with respect to time:

**RoR = dBT/dt (°C per minute)**

In practice, because BT is measured at discrete time intervals (typically every 1–5 seconds), the derivative is approximated numerically:

**RoR(t) ≈ [BT(t + Δt) − BT(t − Δt)] / (2Δt)**

This finite difference approximation introduces noise from probe measurement variation — a primary reason RoR curves appear jagged in raw form. Smoothing algorithms (moving averages, Gaussian filters, or Savitzky-Golay filters) are applied in software to produce a readable, noise-reduced RoR curve.

### Integral: Area Under the Curve

The integral of the RoR curve over a time interval gives the total temperature change over that interval:

**∫ RoR dt = ΔBT**

This relationship is used implicitly when roasters speak of "energy delivered" to the bean in a phase — the area under the RoR curve is proportional to the total temperature rise during that phase.

### Development Time Ratio (DTR)

A ratio that quantifies the proportion of total roast time spent in post-first-crack development:

**DTR (%) = (Development phase time / Total roast time) × 100**

DTR is a simple arithmetic ratio; however, its implications derive from the reaction kinetics relationships between time and temperature (see [Reaction Rates](reaction-rates.md)).

### Turning Point Detection

The turning point (TP) is defined as the minimum of the BT curve — the point at which RoR = 0 and transitions from negative to positive. Mathematically:

**TP = argmin(BT) for t > t_charge**

Or equivalently, the time at which RoR crosses zero (from negative to positive) after charging.

### Curve Fitting and Reference Comparison

Profile software can fit mathematical functions to reference profile curves and measure deviation of current batches from the reference:
- A least-squares fit between current BT and reference BT curves provides a quantitative consistency score
- The root mean square error (RMSE) between current and reference RoR curves quantifies how closely the current profile followed the intended shape

### Decline Rate of RoR

In the declining RoR model, the RoR decreases from its post-TP peak to drop. The rate of decline can be characterised by a linear or exponential model:

- **Linear decline:** RoR(t) = RoR_max − k × t (where k is the decline rate in °C/min²)
- **Exponential decline:** RoR(t) = RoR_max × e^(−kt)

Comparing the decline rate of RoR across batches provides a quantitative measure of profile shape consistency beyond simply comparing the DTR or drop temperature.

## Practical Applications

- **Batch comparison:** Numerically comparing DTR, total roast time, and turning point across multiple batches quantifies consistency more rigorously than visual inspection
- **Profile optimisation:** Expressing the relationship between profile parameters (DTR, drop temperature) and cup score numerically enables regression-based optimisation
- **RoR shape scoring:** Quantifying the degree to which a profile conforms to a declining RoR shape (vs. flat or rising) provides an objective "profile quality score" that can be automated in software

## Key Facts

- RoR is the derivative of the BT curve (dBT/dt); calculated numerically using finite differences; smoothed by software to reduce noise
- DTR = development phase time / total roast time × 100; a simple ratio with profound quality implications from reaction kinetics
- Turning point = minimum of BT curve; mathematically equivalent to zero-crossing of RoR (negative to positive)
- Curve fitting (least-squares) and RMSE allow quantitative comparison of current batch profiles against reference profiles
- Declining RoR can be characterised by a linear or exponential decay model; tracking decline rate quantifies profile shape consistency

## Related Notes

- [Roasting MOC](../maps-of-content/roasting-moc.md)
- [Rate of Rise](rate-of-rise.md)
- [Development Time Ratio](development-time-ratio.md)
- [Artisan Software](../roasting-coffee-beans/artisan-software.md)
- [Predictive Modelling](predictive-modelling.md)
- [Statistical Process Control](statistical-process-control.md)

## References

- [Rao, S. (2014). *The Coffee Roaster's Companion* — Scott Rao](https://www.scottrao.com/the-coffee-roasters-companion)
- [Artisan Software — Mathematical Analysis Features](https://artisan-scope.org)
- [Specialty Coffee Association — Data and Analytics in Roasting](https://sca.coffee/research)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-04-27 | Note created |

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
