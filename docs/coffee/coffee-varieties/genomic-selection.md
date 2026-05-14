---
tags: []
  - coffee/varieties
  - coffee/varieties/breeding
aliases:
  - Genomic selection coffee
  - GS coffee breeding
  - Genome-wide selection
---

# Genomic Selection

**Tags:** #coffee/varieties #coffee/varieties/breeding
**Aliases:** Genomic selection coffee, GS coffee breeding, Genome-wide selection
**Related:** [Coffee Breeding and Genetics MOC](../maps-of-content/coffee-breeding-and-genetics-moc.md) | [Marker-Assisted Selection](marker-assisted-selection.md) | [Planned Crossing](planned-crossing.md) | [Breeding for Cup Quality](breeding-for-cup-quality.md) | [Arabica](arabica.md)
**Status:** ✅ Complete

---

## Overview

Genomic selection (GS) is an advanced plant breeding methodology that uses genome-wide molecular marker data — typically tens of thousands to millions of single nucleotide polymorphisms (SNPs) distributed across the entire genome — combined with phenotypic data from a training population to predict the breeding value of untested individuals. Unlike marker-assisted selection (MAS), which uses a small number of markers linked to specific known genes, genomic selection does not require prior knowledge of individual gene locations; instead, it uses statistical models trained on whole-genome marker profiles and measured performance data to generate a **genomic estimated breeding value (GEBV)** for any individual that has been genotyped. In coffee, genomic selection is at the research and early-implementation stage, with the potential to significantly accelerate the improvement of complex traits such as cup quality and yield that involve many genes acting together.

## How Genomic Selection Differs from Marker-Assisted Selection

| Feature | Marker-Assisted Selection (MAS) | Genomic Selection (GS) |
| :--- | :--- | :--- |
| Markers used | Small number (10–100) | Tens of thousands to millions (genome-wide) |
| Target traits | Simply-inherited (single gene); specific known QTL | Both simple and complex (polygenic) traits |
| Requires known gene location? | Yes — markers must be linked to target trait | No — statistical model captures genome-wide effects |
| Training data required? | No (markers directly linked to trait) | Yes — training population with both markers and phenotypes |
| Prediction basis | Known gene-marker association | Statistical model of whole-genome × phenotype relationships |
| Applications in coffee | Disease resistance transfer (SH3, CBD resistance) | Cup quality, yield, climate adaptation prediction |

## The Genomic Selection Process

### 1. Training Population

A set of genetically diverse individuals is phenotyped (carefully measured for the traits of interest — cup quality scores, yield, disease response) and genotyped (genome-wide SNP profiling). This training population captures the relationship between genome variation and phenotypic variation.

### 2. Statistical Model Training

A genomic prediction model is fitted to the training data — typically using statistical approaches such as GBLUP (genomic best linear unbiased prediction), LASSO, or random forest. The model estimates the contribution of each SNP (or small chromosomal region) to the trait, distributed across the whole genome.

### 3. Prediction of New Individuals

New individuals are genotyped (but not necessarily phenotyped). The trained model predicts each individual's GEBV — an estimate of its breeding value for the target trait — based on its genome-wide marker profile.

### 4. Selection

Breeders select individuals with the highest predicted GEBVs for crossing or propagation, without requiring extensive phenotyping of every candidate.

## Applications to Coffee

### Cup Quality

Cup quality is a complex polygenic trait influenced by hundreds or thousands of gene variants interacting with the environment. MAS is poorly suited to cup quality improvement because no small number of markers captures its genetic basis. Genomic selection is theoretically better suited:

- A training population of diverse genotypes with cupping scores and SNP data can be used to train a prediction model
- New breeding lines can be ranked by predicted cup quality based on genome markers alone — avoiding the cost of producing, roasting, and cupping every breeding line before selection

### Yield

Yield is similarly polygenic and environment-dependent. Genomic prediction for yield across diverse environments (multi-environment trials) is an active area of research.

### Disease Resistance (Complex)

While major resistance genes can be tracked by MAS, partial (quantitative) disease resistance — which is more durable than single-gene resistance — is polygenic and better suited to genomic selection approaches.

## Status in Coffee Breeding

As of the mid-2020s, genomic selection in coffee is primarily at the research stage:

- World Coffee Research and partner institutions (CIRAD, CATIE, national programmes) have begun developing training populations and prediction models for *C. arabica*
- The allotetraploid genome of *C. arabica* presents computational and statistical challenges compared to diploid crops (more complex SNP calling and population structure)
- Cost of high-density genotyping per plant, while declining rapidly, remains a limiting factor for large-scale implementation in breeding programmes in lower-income producing countries
- Prediction accuracy for complex traits such as cup quality is still being validated across diverse genetic backgrounds and environments

## Key Facts

- Genomic selection uses genome-wide SNP data and statistical models trained on phenotype-genotype relationships to predict breeding values without prior knowledge of specific gene locations
- Unlike MAS, genomic selection can target complex polygenic traits such as cup quality and yield — where no small number of markers captures the genetic basis
- The process requires a training population of individuals with both genome-wide markers and measured phenotypes; subsequent candidates need only genotyping
- Coffee genomic selection is at the research and early-implementation stage; challenges include the allotetraploid genome complexity, genotyping cost, and training population size requirements
- World Coffee Research and CIRAD are leading development of genomic prediction tools for Arabica improvement

## Related Notes

- [Coffee Breeding and Genetics MOC](../maps-of-content/coffee-breeding-and-genetics-moc.md)
- [Marker-Assisted Selection](marker-assisted-selection.md)
- [Planned Crossing](planned-crossing.md)
- [Breeding for Cup Quality](breeding-for-cup-quality.md)
- [Arabica](arabica.md)

## References

- [World Coffee Research — Genomic Selection Research Programme](https://worldcoffeeresearch.org)
- [CIRAD — Coffee Genomics and Molecular Breeding](https://www.cirad.fr)
- [Meuwissen, T.H.E., Hayes, B.J. & Goddard, M.E. (2001). Prediction of total genetic value using genome-wide dense marker maps — *Genetics* 157: 1819–1829](https://www.genetics.org)
- [Crossa, J. et al. (2017). Genomic selection in plant breeding — *Crop Science* 57: 1271–1296](https://acsess.onlinelibrary.wiley.com)

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-04-27 | Note created |

---

This article is part of **[All-About-Coffee.com](http://All-About-Coffee.com)** - The comprehensive coffee knowledgebase.

Copyright © Matthew Clairmont 2026
