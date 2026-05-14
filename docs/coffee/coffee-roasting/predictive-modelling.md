---
tags: []
  - coffee/roasting
  - coffee/roasting/profile
aliases:
  - Roast predictive modelling
  - Machine learning in roasting
---

# Predictive Modelling

**Tags:** #coffee/roasting #coffee/roasting/profile
**Aliases:** Roast predictive modelling, Machine learning in roasting
**Related:** [Roasting MOC](../maps-of-content/roasting-moc.md) | [Statistical Process Control](statistical-process-control.md) | [Data Logging Software](data-logging-software.md) | [Cropster](cropster.md) | [Profile Documentation](profile-documentation.md)
**Status:** ✅ Complete

---

## Overview

Predictive modelling in coffee roasting refers to the use of mathematical and computational methods to anticipate the future behaviour of a roast in progress, predict cup quality outcomes from roast profile data, or optimise roast profiles systematically rather than through intuitive trial and error. As the volume of digital roast profile data has expanded with the widespread adoption of data logging software, the application of statistical models, machine learning, and physics-based simulation to roasting has become an increasingly active area of research and commercial development in specialty and commercial coffee.

## Types of Predictive Modelling in Roasting

### Physics-Based Thermodynamic Modelling

Mathematical models derived from heat transfer principles can simulate the temperature trajectory of a coffee bean through the roasting process, given inputs such as:
- Green coffee physical properties (density, moisture, thermal conductivity, heat capacity)
- Drum environment conditions (air temperature, airflow velocity)
- Heat transfer coefficients for the specific roaster

These models predict BT and RoR curves from physical first principles, without requiring training data. They are primarily used in academic research and equipment design rather than by individual roasters, but they inform the engineering design of commercial roasters.

### Statistical Profile Models

Data-driven models derived from large roast databases:
- Correlation of profile parameters (charge temperature, DTR, drop temperature, total roast time) with cup score outcomes
- Regression models that predict drop temperature or DTR targets from green coffee properties (density, moisture, screen size) to generate starting profile recommendations
- Batch-to-batch consistency models that flag profiles deviating from the expected envelope for a given lot and roaster

**Cropster's "predictive guidance" features** are one commercial example: using historical batch data to suggest adjustments when a current batch is trending ahead of or behind the reference profile.

### Machine Learning Applications

Machine learning approaches applied to roast data include:
- **Classification models:** Classifying roasts as defective vs. non-defective from profile curve features (RoR shape, DTR, drop temperature) without cupping
- **Prediction of cup score:** Neural networks trained on roast profile data paired with cupping scores to predict expected cup quality of a new batch without cupping every batch
- **Green coffee characterisation:** Using near-infrared (NIR) spectroscopy data from green coffee to predict optimal roast parameters

Most machine learning applications in specialty roasting are at research or early commercial stage; full production-scale deployment is less common than in large commercial operations.

### Automated Profile Adjustment

Some commercial roaster systems combine real-time RoR data with predictive models to automatically adjust burner and damper settings in real time to maintain the roast on a reference profile curve:
- The system compares current BT and RoR to the reference at each time step
- Automated proportional-integral-derivative (PID) control makes small burner and damper adjustments to minimise deviation
- Reduces the manual skill requirement for profile replication; increases batch-to-batch consistency

**Cropster and Probat's integrated systems** offer automated profile following with varying degrees of closed-loop control.

## Limitations of Predictive Modelling

- All predictive models are approximations; real roasting is more complex than any current model captures fully
- Models trained on historical data perform best within the range of conditions represented in training data; they may fail when extrapolated to novel greens, new lots, or unusual environmental conditions
- Cup quality is the ultimate measure; predictive models can guide efficiency and consistency but do not replace sensory evaluation
- Physics-based models require precise green coffee property data that is not routinely measured in commercial operations

## Key Facts

- Predictive modelling in roasting includes physics-based thermodynamic simulation, statistical correlation models, and machine learning
- Commercial applications include profile following suggestions (Cropster), automated PID control, and green coffee property-to-profile mapping
- Machine learning for cup quality prediction from profile data is an active research area; full production-scale deployment is limited
- Automated profile following (closed-loop PID control of burner/damper from real-time RoR data) is commercially available in high-end roaster systems
- All predictive models supplement rather than replace sensory evaluation; cup quality is the ground truth

## Related Notes

- [Roasting MOC](../maps-of-content/roasting-moc.md)
- [Statistical Process Control](statistical-process-control.md)
- [Data Logging Software](data-logging-software.md)
- [Cropster](cropster.md)
- [Artisan Software](../roasting-coffee-beans/artisan-software.md)
- [Rate of Rise Analysis](rate-of-rise-analysis.md)

## References

- [Rao, S. (2014). *The Coffee Roaster's Companion* — Scott Rao](https://www.scottrao.com/the-coffee-roasters-companion)
- [Cropster — Intelligent Roasting and Profile Management](https://www.cropster.com)
- [Specialty Coffee Association — Technology and Innovation in Roasting](https://sca.coffee/research)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-04-27 | Note created |

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
