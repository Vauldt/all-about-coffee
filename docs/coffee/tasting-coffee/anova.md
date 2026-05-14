---
tags: []
  - coffee/tasting
  - coffee/tasting/evaluation
aliases:
  - Analysis of Variance
  - ANOVA Coffee
---

# ANOVA

**Tags:** #coffee/tasting #coffee/tasting/evaluation
**Aliases:** Analysis of Variance, ANOVA Coffee
**Related:** [Sensory Science MOC](../maps-of-content/sensory-science-moc.md) | [Quality Control MOC](../maps-of-content/quality-control-moc.md) | [Cupping Protocol](../coffee-tasting/cupping-protocol.md) | Calibration Sessions
**Status:** 🔄 In Progress

---

## Overview

ANOVA (Analysis of Variance) is a statistical method used in coffee sensory science to compare means across multiple groups and determine whether differences are statistically significant. It is essential for Calibration Sessions, panel management, and interpreting cupping results where three or more groups must be compared simultaneously.

## What is ANOVA?

ANOVA tests whether the means of three or more groups differ significantly by:
1. Partitioning total variance into components
2. Comparing variance between groups to variance within groups
3. Calculating an F-statistic
4. Determining if differences are likely due to chance

**Null Hypothesis (H₀)**: All group means are equal
**Alternative Hypothesis (H₁)**: At least one group mean differs

## Why Use ANOVA in Coffee?

### Common Applications

**Comparing Coffees:**
- Do three different processing methods produce different cup scores?
- Is coffee from one region rated higher than others?
- Do roast levels affect sweetness scores differently?

**Evaluating Panels:**
- Do different judges score consistently?
- Is one panellist systematically higher or lower?
- Are there significant judge-by-coffee interactions?

**Quality Control:**
- Do production batches differ significantly?
- Has quality changed over time?
- Do different roasters produce equivalent results?

## Types of ANOVA

### One-Way ANOVA

**Design:**
- One independent variable (factor)
- Three or more groups or levels
- Tests main effect only

**Example:**
Comparing cup scores across four origins — Ethiopia, Kenya, Colombia, Brazil.

**Question:** Do origin group means differ?

### Two-Way ANOVA

**Design:**
- Two independent variables
- Tests main effects and interaction
- More complex but more informative

**Example:**
Testing effects of processing method (washed, natural, honey) and roast level (light, medium, dark) on acidity scoring.

**Questions:**
1. Main effect of processing?
2. Main effect of roast?
3. Interaction: does the processing effect depend on roast level?

### Repeated Measures ANOVA

**Design:**
- Same subjects measured multiple times
- Accounts for within-subject correlation
- Common in sensory panels

**Example:**
The same panel tastes five coffees at three different temperatures (hot, warm, cool).

**Controls for:** Individual judge differences

### Mixed-Design ANOVA

**Design:**
- Combines between-subjects and within-subjects factors
- Example: Different panels (between) rating the same coffees (within)

## ANOVA Assumptions

### Critical Assumptions

1. **Independence**: Observations are independent of each other
2. **Normality**: Data in each group are normally distributed
3. **Homogeneity of Variance**: Equal variance across groups (homoscedasticity)

Minor violations are often tolerable, especially with balanced designs. Severe violations warrant transformations or non-parametric alternatives.

### Checking Assumptions

**Normality:**
- Shapiro-Wilk test
- Q-Q plots
- Histograms

**Homogeneity:**
- Levene's test
- Bartlett's test
- Visual inspection of residuals

## Interpreting ANOVA Results

### F-Statistic

F = Variance Between Groups / Variance Within Groups

A large F indicates that between-group variance substantially exceeds within-group variance, suggesting the groups truly differ. A small F indicates differences likely attributable to chance.

### P-Value

**Significance Levels:**
- p < 0.05: Statistically significant at 5% level
- p < 0.01: Highly significant at 1% level
- p > 0.05: Not statistically significant

In a coffee context, a significant result indicates coffees or groups truly differ; a non-significant result indicates differences could be random variation.

### Effect Size

Statistical significance does not equal practical importance. With large samples, even trivial differences can be statistically significant. Effect size measures the magnitude of differences.

**Common Measures:**
- **Eta-squared (η²)**: Proportion of variance explained
- **Omega-squared (ω²)**: Less biased estimate
- **Cohen's f**: Standardised effect size

**Interpretation:**
- Small: η² ≈ 0.01
- Medium: η² ≈ 0.06
- Large: η² ≈ 0.14

## Post-Hoc Tests

ANOVA indicates that groups differ but not which specific pairs differ. Post-hoc tests address this.

### Common Post-Hoc Tests

**Tukey's HSD (Honestly Significant Difference):**
- Most widely used
- Controls family-wise error rate
- All pairwise comparisons
- Preferred for balanced designs

**Bonferroni Correction:**
- Conservative
- Adjusts p-value threshold
- Suitable when few comparisons are planned

**Scheffé's Test:**
- Most conservative
- Appropriate for complex comparisons
- Suitable for unplanned contrasts

**Dunnett's Test:**
- Compares all groups to one control
- Example: comparing four experimental coffees to a standard blend

## Practical Examples

### Example 1: Three Processing Methods

**Data:**
- 12 judges taste three coffees (washed, natural, honey)
- Each rates overall cup score on the 80–100 scale

**ANOVA Results:**
- F(2, 33) = 8.45, p = 0.001
- η² = 0.34

**Interpretation:**
- Processing method significantly affects cup score
- Processing explains 34% of variance (large effect)
- Post-hoc tests needed to determine which pairs differ

**Post-Hoc (Tukey's HSD):**
- Washed (86.2) vs. Natural (88.5): p = 0.04 (significant)
- Washed (86.2) vs. Honey (87.8): p = 0.15 (not significant)
- Natural (88.5) vs. Honey (87.8): p = 0.52 (not significant)

**Conclusion:** Natural process scores significantly higher than washed; honey is intermediate.

### Example 2: Judge Consistency

**Data:**
- 8 judges rate 10 coffees
- Testing whether judges score consistently

**Two-Way ANOVA:**
- Judge effect: F(7, 63) = 2.1, p = 0.06 (not significant)
- Coffee effect: F(9, 63) = 15.3, p < 0.001 (highly significant)
- Interaction: F(63, 560) = 1.2, p = 0.18 (not significant)

**Interpretation:**
- Judges are well-calibrated with no systematic differences
- Coffees differ significantly, as expected
- No judge-by-coffee interaction indicates good panel reliability

## ANOVA in Sensory Software

### Common Platforms

**XLSTAT:**
- Excel add-in with user-friendly sensory module
- Built-in post-hoc tests

**R Statistical Software:**
- Free and open-source
- Highly flexible; requires coding knowledge

**SPSS:**
- Comprehensive statistical package with point-and-click interface

### Automation in Quality Control

Automated ANOVA on daily batch cupping scores can flag significant deviations and track judge performance over time, reducing the manual workload of routine quality monitoring.

## Limitations and Considerations

### Sample Size

**Too small:** Underpowered (misses real differences); a minimum of five to 10 observations per group is typically needed.

**Too large:** Trivial differences become statistically significant; effect size must accompany p-values.

### Multiple Comparisons Problem

With 10 groups, 45 pairwise comparisons are possible. The probability of at least one false positive increases with the number of comparisons. Post-hoc adjustments (Bonferroni, Tukey) address this.

### Non-Normal Data

**Alternatives:**
- Kruskal-Wallis Test: non-parametric one-way ANOVA
- Friedman Test: non-parametric repeated measures
- Permutation Tests: randomisation-based inference
- Data transformation: log, square-root transforms

## Advanced Topics

### MANOVA (Multivariate ANOVA)

Tests effects on multiple dependent variables simultaneously — for example, testing effects on [Acidity](acidity.md), [Body](body.md), and [Sweetness](../coffee-tasting/sweetness.md) together. Controls Type I error across variables.

### ANCOVA (Analysis of Covariance)

Controls for continuous covariates — for example, controlling for bean density when comparing origins.

### Mixed Models

Used for complex designs with random effects, nested factors (judges within labs), unbalanced data, or repeated measures with missing data.

## Key Facts

- ANOVA compares means across three or more groups simultaneously using an F-statistic
- A significant result (p < 0.05) indicates at least one group mean differs, but post-hoc tests are needed to identify which pairs differ
- Effect size (η²) is as important as p-value — statistical significance does not imply practical importance
- Three critical assumptions are independence, normality, and homogeneity of variance
- Repeated measures ANOVA is the appropriate design for sensory panels tasting multiple samples

## Related Notes

- [Sensory Science MOC](../maps-of-content/sensory-science-moc.md)
- [Quality Control MOC](../maps-of-content/quality-control-moc.md)
- Calibration Sessions
- [Cupping Protocol](../coffee-tasting/cupping-protocol.md)
- Processing Methods MOC

## References

- [Montgomery, D.C., *Design and Analysis of Experiments*, 9th ed., Wiley, 2017](https://www.wiley.com/en-us/Design+and+Analysis+of+Experiments%2C+9th+Edition-p-9781119492443)
- [Field, A., *Discovering Statistics Using IBM SPSS*, 5th ed., SAGE, 2017](https://www.sagepub.com/en-gb/aus/discovering-statistics-using-ibm-spss-statistics/book257366)
- [Lawless, H.T. & Heymann, H., *Sensory Evaluation of Food*, 2nd ed., Springer, 2010](https://link.springer.com/book/10.1007/978-1-4419-6488-5)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-04-29 | Compliance review: added frontmatter, metadata block, Overview, Key Facts, Related Notes, References, Changelog; fixed ../wikilinks; removed path-based link; applied Australian English; added copyright notice |

---

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
