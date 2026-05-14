---
date_created: 2026-03-21
updated: 2026-03-23
---

# Measuring Coffee Extraction

Extraction can be quantified using two key metrics: Total Dissolved Solids (TDS) and Extraction Yield (EY). Understanding these measurements allows for precision, consistency, and troubleshooting.

## Total Dissolved Solids (TDS)

### Definition

**TDS** is the concentration of dissolved coffee compounds in the final beverage, expressed as a percentage.

### What It Measures

TDS tells you how **strong** or **concentrated** your coffee is—how much dissolved coffee is in your cup, not how much you extracted from the beans.

### Example

- **1.28% TDS** means 1.28 grams of dissolved coffee per 100 grams of brewed coffee
- **1.50% TDS** is stronger (more concentrated)
- **1.00% TDS** is weaker (more diluted)

### Ideal TDS Ranges

- **Espresso:** 8-12% TDS (very concentrated)
- **Filter coffee (pour-over, drip):** 1.15-1.45% TDS
- **French press:** 1.20-1.50% TDS
- **Cold brew concentrate:** 3-6% TDS (diluted before drinking)
- **Cold brew ready-to-drink:** 1.0-1.5% TDS

### How to Measure TDS

**Refractometer method** (most common):
1. Use a digital refractometer (VST, Atago, DiFluid)
2. Brew coffee and let sample cool to room temperature
3. Place small sample on refractometer sensor
4. Device measures how dissolved solids refract light
5. Displays TDS percentage directly

**Important:** Coffee must be at room temperature for accurate reading. Hot coffee will give falsely high readings.

**Cost:** Refractometers range from $100 (DiFluid) to $700+ (VST Lab Coffee III)

## Extraction Yield (EY)

### Definition

**Extraction Yield** is the percentage of the coffee's original mass that has been dissolved into the beverage.

### What It Measures

EY tells you how **thoroughly** you extracted the coffee beans—what percentage of the soluble compounds you successfully dissolved.

### Formula

For percolation methods (pour-over, espresso, drip):

**EY = (TDS × Beverage Weight) / Coffee Dose × 100%**

Where:
- **TDS** = Total dissolved solids (%)
- **Beverage Weight** = Final weight of brewed coffee (grams)
- **Coffee Dose** = Weight of dry coffee used (grams)

### Example Calculation

**Brewing parameters:**
- Coffee dose: 20g
- Water used: 320g
- Beverage weight: 300g (some water absorbed by grounds)
- TDS measured: 1.35%

**Calculation:**
```
EY = (1.35 × 300) / 20 × 100%
EY = 405 / 20 × 100%
EY = 20.25%
```

**Result:** 20.25% extraction yield (in ideal range)

### Ideal Extraction Yield Ranges

- **Target range:** 18-22% for most brewing methods
- **Under-extracted:** < 18% (sour, salty, weak flavors)
- **Over-extracted:** > 22% (bitter, astringent, harsh)
- **Specialty standards (SCA):** 18-22% with 1.15-1.35% TDS

**Note:** These are guidelines, not absolute rules. Personal preference and specific coffee beans may call for different targets.

### Why Beverage Weight Matters

Notice that beverage weight ≠ water weight. Some water is retained by the coffee grounds (typically 1.5-2× the coffee dose).

**Example:**
- 20g coffee + 320g water
- Retained water: ~30-40g (stays in spent grounds)
- Beverage weight: ~280-290g (actual drinkable coffee)

Always weigh the final beverage, don't just use the water weight.

## Relationship Between TDS and Extraction Yield

TDS and EY are **related but independent variables**:

- **TDS** measures **strength** (concentration in cup)
- **EY** measures **thoroughness** (how much extracted from beans)

### Four Scenarios

| Extraction Yield | TDS (Strength) | Result |
|-----------------|----------------|--------|
| High EY (22%) | High TDS (1.45%) | Strong, fully extracted - may be bitter |
| High EY (22%) | Low TDS (1.10%) | Weak but fully extracted - thin but not sour |
| Low EY (16%) | High TDS (1.40%) | Strong but under-extracted - concentrated sourness |
| Low EY (16%) | Low TDS (1.05%) | Weak and under-extracted - watery and sour |

**Key insight:** You can adjust strength (TDS) independently of extraction (EY) by changing brew ratio while keeping other variables constant.

## The Brewing Control Chart

First developed by E.E. Lockhart in the 1950s, the Brewing Control Chart maps TDS (vertical axis) against Extraction Yield (horizontal axis):

**Zones:**
- **Ideal zone:** 18-22% EY, 1.15-1.35% TDS (center "sweet spot")
- **Under-extracted:** < 18% EY (left side - sour/underdeveloped)
- **Over-extracted:** > 22% EY (right side - bitter/harsh)
- **Weak:** Low TDS (bottom - thin/watery)
- **Strong:** High TDS (top - heavy/intense)

Modern apps and calculators (Coffee Extraction Calculator, VST CoffeeTools) use this chart to help dial in recipes.

## Practical Measurement Workflow

### Basic Workflow (No Refractometer)

1. **Brew coffee** with known dose and water amount
2. **Taste critically** for balance
3. **Adjust based on taste:**
   - Sour/salty → Grind finer, increase temp, or brew longer (increase EY)
   - Bitter/astringent → Grind coarser, decrease temp, or brew shorter (decrease EY)
   - Weak/thin → Increase dose or decrease water (increase TDS)
   - Too strong → Decrease dose or increase water (decrease TDS)

### Advanced Workflow (With Refractometer)

1. **Brew coffee** with known parameters
2. **Weigh dose, water used, and final beverage** precisely
3. **Measure TDS** with refractometer
4. **Calculate EY** using formula
5. **Plot on brewing chart** or use app
6. **Adjust recipe:**
   - Move EY: Change grind, temp, or time
   - Move TDS: Change brew ratio (dose:water)
7. **Iterate** until you reach desired zone

## Common Measurement Mistakes

### Mistake 1: Using Water Weight Instead of Beverage Weight

**Wrong:** EY = (TDS × Water Used) / Dose  
**Correct:** EY = (TDS × Final Beverage Weight) / Dose

Always account for water retention in grounds (~1.5-2× coffee weight).

### Mistake 2: Measuring Hot Coffee TDS

**Problem:** Temperature affects refractometer accuracy  
**Solution:** Let coffee cool to room temperature (20-25°C) before measuring, or use temperature compensation if available

### Mistake 3: Not Stirring Sample

**Problem:** Coffee can stratify, with different TDS at top vs. bottom  
**Solution:** Stir brewed coffee thoroughly before taking sample

### Mistake 4: Assuming TDS = Extraction

**Problem:** Confusing strength with extraction  
**Clarification:** TDS is one input to calculate EY, not the same thing

### Mistake 5: Treating Numbers as Absolutes

**Problem:** Chasing "perfect numbers" instead of flavor  
**Reminder:** 18-22% and 1.15-1.35% are guidelines for typical specialty coffee, not universal laws. Dark roasts, light roasts, and personal preference can all justify different targets.

## Alternative: Taste-Based Evaluation

You don't need a refractometer to make excellent coffee. Experienced tasters can identify extraction level by flavor:

**Under-extracted indicators:**
- Sour, sharp acidity (like unripe fruit)
- Salty notes
- Thin, watery body
- Grassy or vegetal flavors
- Short finish
- Lack of sweetness

**Balanced extraction indicators:**
- Bright but balanced acidity
- Clear sweetness
- Defined flavor notes
- Good body and mouthfeel
- Pleasant, lingering finish
- Complexity

**Over-extracted indicators:**
- Dominant bitterness
- Astringency (dry, puckering sensation)
- Harsh, unpleasant finish
- Muddy or indistinct flavors
- Flat, lifeless acidity
- Heavy, coating mouthfeel

## Modern Tools

### Refractometers

- **VST Lab Coffee III** - Industry standard, very accurate ($700+)
- **Atago** - Excellent accuracy, professional choice ($500-600)
- **DiFluid R2 Extract** - Budget-friendly, Bluetooth app integration ($100-150)

### Apps and Calculators

- **VST CoffeeTools** - iOS app with brewing control chart
- **Blossom Coffee** - Free web calculator
- **MoccaMaster App** - Tracks brews and TDS over time
- **Decent Espresso** - Integrated refractometer and software (espresso-focused)

## When to Measure vs. When to Taste

**Use measurement when:**
- Dialing in a new coffee or recipe
- Achieving consistency across multiple locations/baristas
- Troubleshooting persistent problems
- Communicating recipes precisely
- Competition or professional contexts

**Trust taste when:**
- You have calibrated palate and experience
- Making small adjustments to familiar recipe
- Personal home brewing (consistency less critical)
- Equipment doesn't justify refractometer cost
- You're getting consistently delicious results

## Related Topics

- [Coffee Extraction Definition](../coffee-brewing/coffee-extraction-definition.md) - What extraction means
- ../Coffee Extraction - Variables - How to control EY and TDS
- ../Coffee Extraction - Troubleshooting - Using measurements to fix problems
- Brewing-Control-Chart - Lockhart's framework
- Refractometer-Guide - Detailed measurement techniques

---

*Measurement gives you a common language and diagnostic power, but taste is always the final judge. Use TDS and extraction yield as tools for understanding and communication, not as substitutes for developing your palate. The best brewers combine precise measurement with sensory evaluation to achieve both consistency and excellence.*
