---
title: "Triangle Tests"
tags: [coffee/tasting]
status: Draft
aliases: []
related: []
---

# Triangle Tests

A triangle test is a discrimination test used in sensory evaluation to determine whether two samples are perceptibly different. It is one of the most widely used methods in food and beverage quality control, and in coffee it is applied across roasting, blending, green buying, and panel training.

---

## How It Works

The triangle test presents an assessor with **three samples**: two are identical and one is different. The assessor's task is simply to identify which sample is the odd one out — without knowing in advance which sample is different or in which position it appears.

**Key principles:**
- Samples are presented simultaneously (not sequentially)
- Sample order is randomised and balanced across the panel
- The assessor must make a choice — guessing is permitted and expected
- No descriptive feedback is required (though it is useful to collect it)

**Probability of correct identification by chance:** 1 in 3 (33.3%). This is fundamental to the statistical analysis — because there is always a 1-in-3 chance of being correct by guessing, a larger panel or more trials are needed to achieve statistical significance.

---

## When to Use a Triangle Test

Triangle tests answer one question: **are these two samples perceptibly different?**

They do not indicate which is preferred, or describe how the samples differ. They are the right tool when:

- Testing whether a process change (new water, adjusted roast profile, new green lot) has changed the cup
- Verifying that two lots from different suppliers are interchangeable
- Checking that a reformulated blend still tastes the same as the original
- Training panellists to detect differences — or screening candidates for panel sensitivity
- Validating that equipment changes (new grinder, new batch brewer) have not altered output

---

## Sample Preparation

Rigorous preparation is essential — any unintentional differences in preparation (grind, dose, water temperature, timing) could produce a false positive result.

**Requirements:**
- Identical brew parameters for all three samples
- Same coffee weight, grind setting, water temperature, contact time, and vessel
- Samples prepared and presented at the same temperature
- Cups labelled with random three-digit codes (not letters or sequential numbers — these introduce bias)
- Presentation order balanced: the six possible orderings (AAB, ABA, BAA, ABB, BAB, BBA) should appear in equal proportions across the panel

**Palate cleansing:** Provide water and plain crackers or bread between samples. Assessors should cleanse between each of the three cups.

---

## Statistical Analysis

Because 1 in 3 people will guess correctly, a single correct response means nothing. The triangle test becomes meaningful when a sufficient number of assessors identify the correct sample to exceed what chance alone would predict.

### The Binomial Model

Results follow a **binomial distribution** with p = 1/3. Reference tables (or software) are used to determine the minimum number of correct responses required for statistical significance at a given panel size and confidence level.

**Commonly used significance levels:**
- **α = 0.05** (95% confidence) — standard for most quality control applications
- **α = 0.01** (99% confidence) — used when consequences of a false positive are high

### Minimum Correct Responses Required

The table below shows the minimum number of correct responses needed to conclude a perceptible difference exists at the 5% significance level:

| Panel Size | Min. Correct for p < 0.05 | Min. Correct for p < 0.01 |
|---|---|---|
| 10 | 7 | 8 |
| 15 | 8 | 10 |
| 20 | 10 | 12 |
| 24 | 11 | 13 |
| 30 | 13 | 15 |
| 40 | 16 | 19 |

*Source: ISO 4120:2021 — Sensory analysis: Methodology — Triangle test*

If the number of correct responses meets or exceeds the threshold, the conclusion is that the two samples are **perceptibly different** at the stated confidence level. If it falls below the threshold, the test is inconclusive — not a proof that the samples are identical.

### Inconclusive Results

An inconclusive result (too few correct responses) does not prove the samples are the same. It means the panel could not reliably tell them apart. This distinction matters: in quality control, a test that fails to reach significance may simply mean the panel was too small, or the difference is below the threshold of detection for that panel.

---

## Interpreting Results in Coffee Contexts

### Positive Result (Difference Detected)

The samples are perceptibly different. Next steps:
- Run a preference test or descriptive analysis to characterise the difference
- Investigate the source of the difference (process, ingredient, equipment)
- Decide whether the difference is acceptable for the intended use

### Negative Result (No Difference Detected)

The panel could not tell the samples apart. This supports (but does not prove) interchangeability. Useful for:
- Confirming a supplier substitution is transparent to tasters
- Validating a process change has not altered the cup
- Establishing baseline sensitivity of a panel

---

## Triangle Tests in Coffee Quality Control

### Roasting QC

Compare today's roast batch against a certified reference sample of the same coffee. If the triangle test detects no difference, the roast is consistent with the benchmark. If a difference is detected, the roast parameters should be reviewed.

### Green Coffee Buying

Compare a sample lot against a reference or a competing offer. A positive result confirms they are not equivalent; a negative result supports substitution.

### Blend Consistency

When a component coffee in a blend is replaced, triangle testing the finished blend confirms whether the substitution is detectable. This is particularly important for house espresso blends sold under a consistent brand identity.

### Panel Training

Triangle tests with deliberately different samples (different roast levels, different processing methods) calibrate panellists and identify individuals with high discrimination ability. Panel candidates who consistently perform above chance across repeated triangle tests are strong candidates for trained sensory panels.

---

## Variations on the Triangle Test

**Duo-trio test:** The assessor is given a reference sample and two unknowns; they identify which unknown matches the reference. Easier than the triangle test (1 in 2 chance of guessing correctly) but requires more samples for equivalent statistical power.

**Same-different test:** The assessor receives two samples and states whether they are the same or different. Useful when three-sample presentation is impractical.

**Tetrad test:** Four samples (two of each type) in random order; the assessor groups them into two matching pairs. More statistically powerful than the triangle test for the same number of assessors — increasingly used in professional sensory applications.

---

## Practical Guidance

- **Run enough assessors.** With 10 or fewer assessors, the triangle test has low statistical power. 20–30 is a practical target for reliable results.
- **Randomise rigorously.** Use a randomisation table or software to assign sample codes and presentation order.
- **Do not tell assessors which type of difference to look for.** This primes them and inflates correct response rates.
- **Collect qualitative notes.** Even though the task is only to identify the odd sample, asking assessors to describe how it differs builds useful descriptive data at no extra cost.
- **Repeat for reliability.** A single triangle test is a snapshot. Consistent results across multiple sessions on different days increase confidence.

---

## Related Topics

- Calibration Sessions — Aligning panel responses to shared standards
- Blind Tasting — Unbiased evaluation methodology
- [Production Cupping](../coffee-roasting/production-cupping.md) — QC cupping in roasting environments
- [SCA Cupping Protocol](sca-cupping-protocol.md) — Industry standard evaluation method
- [Sensory Science MOC](../maps-of-content/sensory-science-moc.md) — Overview of sensory science

---

_Part of 05_PUBLISHING/Homepage/Coffeepedia - The comprehensive coffee knowledge vault_
