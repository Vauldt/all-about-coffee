---
tags: [coffee/education]
 date_created: 2026-03-21
updated: 2026-03-23
---
# Tag Index

**Tags:** #meta/index  
**Purpose:** This entry codifies the master reference for all tags used across the All-About-Coffee Encyclopedia. This note is used to maintain consistency when tagging new notes.

---

## Tag Conventions

- Tags use **lowercase** with **hyphens** for multi-word terms (e.g. `#coffee/green-beans`)
- Tags use **forward slash `/`** for parent/child nesting
- Every note should have **at least one** `#coffee/*` tag and **one** `#meta/*` tag where applicable
- Avoid creating new top-level tags without updating this index first

---

## Full Tag Hierarchy

### `#coffee` — All Coffee Encyclopedia Notes

#### `/processing` — Cherry and Bean Processing Methods

| Tag | Use For |
| :--- | :--- |
| `#coffee/processing` | General processing overviews |
| `#coffee/processing/washed` | Wet/fully washed process |
| `#coffee/processing/natural` | Dry/natural process |
| `#coffee/processing/honey` | Honey/pulped natural process |
| `#coffee/processing/wet-hulled` | Giling basah / Sumatra method |
| `#coffee/processing/anaerobic` | Anaerobic fermentation methods |
| `#coffee/processing/experimental` | Novel or emerging processing techniques |

#### `/green-beans` — Raw, Unroasted Coffee

| Tag | Use For |
| :--- | :--- |
| `#coffee/green-beans` | General green bean topics |
| `#coffee/green-beans/grading` | Grading systems and defect classification |
| `#coffee/green-beans/defects` | Physical and cup defects |
| `#coffee/green-beans/moisture` | Moisture content and measurement |

#### `/production` — Farm and Mill-level Topics

| Tag | Use For |
| :--- | :--- |
| `#coffee/production` | General production overviews |
| `#coffee/production/harvesting` | Picking methods and selective harvesting |
| `#coffee/production/milling` | Wet and dry milling operations |
| `#coffee/production/sorting` | Density, colour, and size sorting |

#### `/storage` — Storage Conditions and Methods

| Tag | Use For |
| :--- | :--- |
| `#coffee/storage` | General storage principles |
| `#coffee/storage/green` | Green bean storage specifically |
| `#coffee/storage/roasted` | Roasted bean storage specifically |
| `#coffee/storage/transit` | Shipping and logistics moisture management |
| `#coffee/storage/packaging` | Bags, hermetic seals, GrainPro, vacuum |

#### `/cultivation` — Growing and Agronomy

| Tag | Use For |
| :--- | :--- |
| `#coffee/cultivation` | General agronomy and growing |
| `#coffee/cultivation/soil` | Soil types and requirements |
| `#coffee/cultivation/altitude` | Altitude and its effect on bean development |
| `#coffee/cultivation/climate` | Climate zones and seasonal patterns |
| `#coffee/cultivation/shade` | Shade-grown and agroforestry practices |

#### `/varieties` — Species, Varieties and Cultivars

| Tag | Use For |
| :--- | :--- |
| `#coffee/varieties` | General variety overviews |
| `#coffee/varieties/arabica` | Coffea arabica and its cultivars |
| `#coffee/varieties/robusta` | Coffea canephora / robusta |
| `#coffee/varieties/liberica` | Coffea liberica |
| `#coffee/varieties/cultivars` | Named cultivars (Bourbon, Typica, Gesha, etc.) |

#### `/geography` — Origins and Producing Regions

| Tag | Use For |
| :--- | :--- |
| `#coffee/geography` | General origin and terroir topics |
| `#coffee/geography/africa` | African producing countries |
| `#coffee/geography/americas` | Central and South American origins |
| `#coffee/geography/asia-pacific` | Asia-Pacific origins including PNG and Indonesia |
| `#coffee/geography/australia` | Australian specialty coffee production |

#### `/roasting` — Roast Profiles and Chemistry

| Tag | Use For |
| :--- | :--- |
| `#coffee/roasting` | General roasting topics |
| `#coffee/roasting/profiles` | Roast curves, development time, RoR |
| `#coffee/roasting/chemistry` | Maillard reaction, caramelisation, CO₂ degassing |
| `#coffee/roasting/defects` | Roast defects (scorching, tipping, underdevelopment) |
| `#coffee/roasting/equipment` | Roaster types and drum mechanics |

#### `/brewing` — Extraction Methods and Recipes

| Tag | Use For |
| :--- | :--- |
| `#coffee/brewing` | General brewing overviews |
| `#coffee/brewing/espresso` | Espresso extraction |
| `#coffee/brewing/filter` | Pour-over, batch brew, drip |
| `#coffee/brewing/immersion` | French press, AeroPress, cold brew |
| `#coffee/brewing/parameters` | Grind size, ratio, temperature, time |

#### `/tasting` — Sensory Evaluation and Cupping

| Tag | Use For |
| :--- | :--- |
| `#coffee/tasting` | General sensory and tasting notes |
| `#coffee/tasting/cupping` | Formal cupping protocols (SCA, CoE) |
| `#coffee/tasting/flavour-wheel` | SCA flavour wheel references |
| `#coffee/tasting/defects` | Cup defects and off-flavours |
| `#coffee/tasting/scoring` | Q-grading and scoring systems |

#### `/equipment` — Tools and Machinery

| Tag | Use For |
| :--- | :--- |
| `#coffee/equipment` | General equipment topics |
| `#coffee/equipment/grinders` | Burr grinders, grind consistency |
| `#coffee/equipment/espresso-machines` | Espresso machine types and mechanics |
| `#coffee/equipment/brew-devices` | Manual and automated brew devices |
| `#coffee/equipment/mill` | Wet and dry mill machinery |

#### `/business` — Industry, Trade and Commercial Topics

| Tag | Use For |
| :--- | :--- |
| `#coffee/business` | General industry and trade topics |
| `#coffee/business/supply-chain` | Farm to roaster logistics |
| `#coffee/business/certifications` | Fair Trade, Rainforest Alliance, Organic, CoE |
| `#coffee/business/pricing` | C-market, differentials, direct trade pricing |
| `#coffee/business/cafe-operations` | Cafe setup, workflow, staffing |
| `#coffee/business/wholesale` | Roaster-to-cafe wholesale relationships |

#### `/history` — Historical Context and Development

| Tag | Use For |
| :--- | :--- |
| `#coffee/history` | General coffee history |
| `#coffee/history/origins` | Yemeni and Ethiopian origins |
| `#coffee/history/trade` | Historical trade routes and colonialism |
| `#coffee/history/waves` | First, second, third and fourth wave movements |
| `#coffee/history/australia` | Australian coffee culture history |

---

### `#meta` — Vault Management Notes

| Tag | Use For |
| :--- | :--- |
| `#meta/index` | Index and reference notes (including this note) |
| `#meta/template` | Note templates |
| `#meta/moc` | Maps of Content (MOC) notes |
| `#meta/stub` | Incomplete notes that need expanding |
| `#meta/review` | Notes flagged for fact-checking or revision |

---

## Notes Using Each Tag

> Use a Dataview query to auto-populate this section:

~~~dataview
TABLE tags
FROM #coffee
SORT file.name ASC
~~~

---

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-03-21 | Initial tag index created |

---

Part of **All-About-Coffee.com** - The comprehensive coffee knowledgebase.

You can contact the editor:  
All_About_Coffee@icloud.com

Copyright © Matthew Clairmont 2026

---