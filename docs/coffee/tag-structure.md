# Tag Structure

Table of Contents  ← single root
│
├── Foundational Knowledge MOC  ← cross-cutting entry point (keep as special case)
│
├── DOMAIN 1: Plant Science & Varietals
│   ├── Coffee Botany and Varietals MOC  ← Tier 1 parent
│   │   ├── Coffee Plant Science MOC
│   │   ├── Coffee Breeding and Genetics MOC
│   │   ├── Coffee Variety Families MOC
│   │   └── Variety Characteristics and Evaluation MOC
│
├── DOMAIN 2: Origins & Geography
│   ├── Coffee Origins MOC  ← Tier 1 parent (merge Coffee Origin MOC into this)
│   │   ├── Terroir-by-Country MOC
│   │   ├── Origins & Terroir MOC
│   │   ├── Regional Coffee MOC
│   │   ├── Ethiopia MOC
│   │   │   └── Ethiopia Coffee Regions MOC
│   │   ├── Specialty Coffee Regions MOC
│   │   ├── Australia MOC
│   │   └── USA MOC
│
├── DOMAIN 3: Processing
│   ├── Coffee Processing MOC  ← Tier 1 parent (absorb Processing Methods MOC)
│
├── DOMAIN 4: Roasting & Flavour
│   ├── Roasting MOC  ← Tier 1 parent
│   │   ├── Roasting Methods MOC
│   │   └── Flavour Development MOC
│
├── DOMAIN 5: Brewing
│   ├── Brewing Methods MOC  ← Tier 1 parent
│   │   ├── Brewing Fundamentals MOC
│   │   ├── Espresso MOC
│   │   │   └── (espresso drinks handled via Coffee Drinks MOC)
│   │   ├── Hario V60 MOC
│   │   └── Extraction by Brewing Method MOC
│
├── DOMAIN 6: Extraction & Chemistry
│   ├── Coffee Extraction Fundamentals MOC  ← Tier 1 parent
│   │   ├── Extraction Optimization & Troubleshooting MOC
│   │   ├── Coffee Chemistry MOC
│   │   ├── Water MOC
│   │   └── Grind Size MOC
│
├── DOMAIN 7: Equipment
│   ├── Coffee Equipment MOC  ← Tier 1 parent
│   │   ├── Coffee Grinders MOC
│   │   │   ├── Grinder Technology & Performance MOC
│   │   │   └── Grinder Maintenance & Care MOC
│
├── DOMAIN 8: Sensory Science & Quality
│   ├── Sensory Science MOC  ← Tier 1 parent
│   │   ├── Coffee Tasting MOC
│   │   ├── Coffee Defects MOC
│   │   └── Quality Control MOC
│
├── DOMAIN 9: Coffee Drinks
│   ├── Coffee Drinks MOC  ← Tier 1 parent (clarify/consolidate with Coffee Based Drinks MOC)
│   │   ├── Regional Coffee Drinks MOC
│   │   └── Coffee Cocktails MOC
│
├── DOMAIN 10: History & The Specialty Coffee Movement
│   ├── Coffee History MOC  ← Tier 1 parent
│   └── Specialty Coffee MOC  ← Tier 1 parent (rename from "MoC")
│       ├── Specialty Coffee History MOC
│       ├── Specialty Coffee Pioneers MOC
│       ├── Specialty Coffee Principles MOC
│       ├── Specialty Coffee Institutions MOC
│       │   └── Specialty Coffee Association MOC
│       └── Specialty Coffee Regions MOC
│
└── DOMAIN 11: Professional Development & Education
    ├── Professional Development MOC  ← Tier 1 parent
    │   ├── Training and Education MOC
    │   ├── Barista Skills Development MOC
    │   ├── Workplace Skills MOC
    │   └── Coffee Education MOC

I'll read the Table of Contents file and then survey all the MOC files to understand the current structure.

I can see there are 60+ MOC files across several locations. Let me read the Table of Contents and then do a deeper survey of the MOC landscape.

Let me now read all the remaining MOC files to fully understand the landscape.

Now let me read the most problematic duplicate pairs directly to understand exactly what each covers.

Let me check a few more key MOCs that have unclear placement or structure issues.

Let me check a few more MOCs - particularly the specialty coffee cluster and the skills/professional development overlap.

I now have a thorough picture of the entire MOC landscape. Let me compile this into a comprehensive analysis.

Here is the full analysis.

---

## Table of Contents — Issues and Recommendations

### Critical Issues (broken links and missing content)

**1. `Skills Development MOC` does not exist.** The table lists it under Professional Development, but no such file exists anywhere in the vault. The likely intention was `[Barista Skills Development MOC](maps-of-content/barista-skills-development-moc.md)` or `[Training and Education MOC](maps-of-content/training-and-education-moc.md)`. Remove or replace this link.

**2. Broken path: `Barista/Barista Skills /Barista Skills Development MOC`** The path contains a trailing space in `Barista Skills /` and the full folder path is not how Obsidian resolves wikilinks. Replace with the plain `[Barista Skills Development MOC](maps-of-content/barista-skills-development-moc.md)`.

**3. Three entire domains are absent from the ToC:**

- **History** — `Coffee History MOC` exists and is well-formed but is nowhere in the ToC.
- **Specialty Coffee Movement** — `Specialty Coffee MoC` and its five well-structured children (History, Pioneers, Principles, Institutions, Regions) are entirely absent.
- **Foundational Knowledge** — `Foundational Knowledge MOC` appears only in the Related MOCs footer; it arguably deserves a proper domain row or an explicit note that it is the cross-cutting entry point.

**4. The opening paragraph says "10 subject domains."** With History and the Specialty Movement accounted for, there are at least 11. Update the count when the missing domains are added.

**5. `Maps of Content/Coffee Drinks MOC` uses a folder-qualified path.** No file named `Coffee Drinks MOC.md` exists inside `Maps of Content/`. The actual file is `Cafe Drinks/Coffee Drinks MOC.md`. Either move the file or correct the path.

---

### Structural Issues

**6. Duplicate-scope rows across multiple sections.** Several sections list two MOCs that currently call each other "companion" with no defined parent/child relationship. The ToC inadvertently exposes these unresolved duplicates as if they are intentionally distinct. See the full hierarchy proposal below for the recommended resolution.

|Section|Pair in ToC|Status|
|:--|:--|:--|
|Origin and Geography|`Coffee Origin MOC` + `Coffee Origins MOC`|Effectively the same scope|
|Processing|`Coffee Processing MOC` + `Processing Methods MOC`|Essentially identical|
|Equipment|`Water MOC` + `Water in Coffee MOC`|One is a 600-line encyclopaedic file; other is a concise MOC|
|Professional Development|`Professional Development MOC` + `Workplace Skills MOC` + `Training and Education MOC` + `Barista Skills Dev MOC`|Four MOCs with overlapping scope and no explicit parent|

**7. `Grind Size MOC` is missing from the Equipment section.** It exists, is well-structured, and `Navigation MOC` treats it as a popular article. It belongs in the Equipment section of the ToC alongside `Coffee Grinders MOC`.

**8. `Coffee Glossary MOC` is absent.** It exists in `Maps of Content/` but appears nowhere in the ToC. It should appear as a utility reference, either in its own row or in a footer alongside `Tag Index`.

---

### Formatting Issues

**9. Missing `created`/`updated` fields in frontmatter.** The ToC itself has `created: 2026-04-27` and `updated: 2026-05-04` — that is correct. However the frontmatter also lacks a primary content tag beyond `coffee/meta`. This is fine for a navigation file but worth noting.

**10. The `MOC` tag is present in frontmatter.** The vault rule (from memory) is that the `MOC` tag must never be added to any file, and should be removed when editing. The ToC currently carries `tags: [MOC, coffee/meta, meta/navigation]`. Remove `MOC` from the tags list on next edit.

---

## MOC Inventory: Duplicates, Orphans, and Structural Problems

### True Duplicate Pairs (same scope, same articles)

|Primary (keep)|Duplicate (consolidate)|Action|
|:--|:--|:--|
|`Coffee Processing MOC.md`|`Processing Methods MOC.md`|The Processing MOC is marginally better — longer, includes the green coffee section. Merge the Regional Traditions section from Processing Methods MOC into Coffee Processing MOC, then redirect Processing Methods MOC via alias.|
|`Water MOC.md`|`Water in Coffee MOC.md`|Water MOC is correctly structured. Water in Coffee MOC is 600+ lines of encyclopaedic content — it violates the MOC rule (no primary content) and has hundreds of placeholder links. Demote it or strip it to a proper MOC shell.|
|`Professional Development MOC.md`|`Professional Development MOC 1.md`|The `1` suffix is an auto-increment artefact. Confirm content and delete the duplicate.|
|`Training and Education MOC.md`|`Training and Education MOC 1.md`|Same — delete the numbered duplicate after confirming content.|

### Near-Duplicate Pairs (overlapping scope, unclear distinction)

|MOC A|MOC B|Recommended resolution|
|:--|:--|:--|
|`Coffee Origin MOC`|`Coffee Origins MOC`|**Merge.** A is terroir-framework focused; B is geography/country-index focused. Neither distinction is strong enough to justify two MOCs. Merge into one `Coffee Origins MOC` with a Terroir section and a By-Country section. The `Terroir-by-Country MOC` and `Origins & Terroir MOC` can then be sub-MOCs.|
|`Roasting MOC`|`Roasting Methods MOC`|**Define hierarchy.** Roasting MOC = parent. Roasting Methods MOC = child covering equipment and heat-transfer types. Add explicit "Child MOCs" section to Roasting MOC.|
|`Specialty Coffee MoC`|`Specialty Coffee Principles MOC` + 4 siblings|**Already well-structured** — `Specialty Coffee MoC` correctly lists 5 child MOCs. The issue is this cluster is invisible in the ToC. Add a single "Specialty Coffee Movement" row to the ToC pointing to `Specialty Coffee MoC`.|

### Naming Inconsistencies

- `Specialty Coffee MoC.md` — lowercase "o" in MoC is inconsistent with vault naming standard. Rename to `Specialty Coffee MOC.md`.
- `Coffee Drink Recipes MOC.md` (double space) in `Cafe Drinks/Coffee Based Drinks/` — file naming error.
- `Coffee Equipment MOC.md` lives inside `Coffee Equipment/Coffee Equipment /` — double-folder with extra space, making it unreachable via standard wikilinks.

### MOC Tag Violation

`Specialty Coffee MoC.md` carries `tags: [MOC, coffee/specialty-coffee]`. The `MOC` tag must be removed. The ToC also has it (noted above).

### Missing `created`/`updated` Frontmatter

These MOC files are missing the required date fields:

- `Coffee Origin MOC.md`
- `Coffee Origins MOC.md`
- `Coffee Processing MOC.md`
- `Processing Methods MOC.md`
- `Water MOC.md`
- `Navigation MOC.md`
- `Coffee Tasting MOC.md`
- `Foundational Knowledge MOC.md`
- `Professional Development MOC.md` (and several others — all pre-date the `created`/`updated` requirement)

---

## Proposed MOC Hierarchy

The vault currently has no explicit tier system — all 60+ MOCs are effectively siblings. The hierarchy below proposes three tiers. The ToC should reflect Tier 1 only; each Tier 1 MOC's Deep Dives table lists its Tier 2 children; Tier 2 MOCs list Tier 3.

```
Table of Contents  ← single root
│
├── Foundational Knowledge MOC  ← cross-cutting entry point (keep as special case)
│
├── DOMAIN 1: Plant Science & Varietals
│   ├── Coffee Botany and Varietals MOC  ← Tier 1 parent
│   │   ├── Coffee Plant Science MOC
│   │   ├── Coffee Breeding and Genetics MOC
│   │   ├── Coffee Variety Families MOC
│   │   └── Variety Characteristics and Evaluation MOC
│
├── DOMAIN 2: Origins & Geography
│   ├── Coffee Origins MOC  ← Tier 1 parent (merge Coffee Origin MOC into this)
│   │   ├── Terroir-by-Country MOC
│   │   ├── Origins & Terroir MOC
│   │   ├── Regional Coffee MOC
│   │   ├── Ethiopia MOC
│   │   │   └── Ethiopia Coffee Regions MOC
│   │   ├── Specialty Coffee Regions MOC
│   │   ├── Australia MOC
│   │   └── USA MOC
│
├── DOMAIN 3: Processing
│   ├── Coffee Processing MOC  ← Tier 1 parent (absorb Processing Methods MOC)
│
├── DOMAIN 4: Roasting & Flavour
│   ├── Roasting MOC  ← Tier 1 parent
│   │   ├── Roasting Methods MOC
│   │   └── Flavour Development MOC
│
├── DOMAIN 5: Brewing
│   ├── Brewing Methods MOC  ← Tier 1 parent
│   │   ├── Brewing Fundamentals MOC
│   │   ├── Espresso MOC
│   │   │   └── (espresso drinks handled via Coffee Drinks MOC)
│   │   ├── Hario V60 MOC
│   │   └── Extraction by Brewing Method MOC
│
├── DOMAIN 6: Extraction & Chemistry
│   ├── Coffee Extraction Fundamentals MOC  ← Tier 1 parent
│   │   ├── Extraction Optimization & Troubleshooting MOC
│   │   ├── Coffee Chemistry MOC
│   │   ├── Water MOC
│   │   └── Grind Size MOC
│
├── DOMAIN 7: Equipment
│   ├── Coffee Equipment MOC  ← Tier 1 parent
│   │   ├── Coffee Grinders MOC
│   │   │   ├── Grinder Technology & Performance MOC
│   │   │   └── Grinder Maintenance & Care MOC
│
├── DOMAIN 8: Sensory Science & Quality
│   ├── Sensory Science MOC  ← Tier 1 parent
│   │   ├── Coffee Tasting MOC
│   │   ├── Coffee Defects MOC
│   │   └── Quality Control MOC
│
├── DOMAIN 9: Coffee Drinks
│   ├── Coffee Drinks MOC  ← Tier 1 parent (clarify/consolidate with Coffee Based Drinks MOC)
│   │   ├── Regional Coffee Drinks MOC
│   │   └── Coffee Cocktails MOC
│
├── DOMAIN 10: History & The Specialty Coffee Movement
│   ├── Coffee History MOC  ← Tier 1 parent
│   └── Specialty Coffee MOC  ← Tier 1 parent (rename from "MoC")
│       ├── Specialty Coffee History MOC
│       ├── Specialty Coffee Pioneers MOC
│       ├── Specialty Coffee Principles MOC
│       ├── Specialty Coffee Institutions MOC
│       │   └── Specialty Coffee Association MOC
│       └── Specialty Coffee Regions MOC
│
└── DOMAIN 11: Professional Development & Education
    ├── Professional Development MOC  ← Tier 1 parent
    │   ├── Training and Education MOC
    │   ├── Barista Skills Development MOC
    │   ├── Workplace Skills MOC
    │   └── Coffee Education MOC
```

---

## Priority Action List

**Immediate (broken links / missing content):**

1. Remove `Skills Development MOC` from the ToC — it does not exist
2. Fix `Barista/Barista Skills /Barista Skills Development MOC` → `[Barista Skills Development MOC](maps-of-content/barista-skills-development-moc.md)`
3. Add a "History & Specialty Coffee Movement" domain row to the ToC linking to `Coffee History MOC` and `Specialty Coffee MOC`
4. Remove the `MOC` tag from the ToC and from `Specialty Coffee MoC.md`

**Short-term (duplicate resolution):** 5. Delete `Professional Development MOC 1.md` and `Training and Education MOC 1.md` (numbered duplicates) 6. Merge `Coffee Origin MOC` into `Coffee Origins MOC` (or vice versa — pick one and delete the other) 7. Merge the Regional Traditions section from `Processing Methods MOC` into `Coffee Processing MOC`, then delete or redirect `Processing Methods MOC` 8. Demote `Water in Coffee MOC` — either restructure it as a proper MOC (no encyclopaedic content) or replace it with a pointer alias to `Water MOC`

**Medium-term (hierarchy establishment):** 9. Rename `Specialty Coffee MoC.md` → `Specialty Coffee MOC.md` 10. Add `created`/`updated` dates to all MOCs missing them 11. Add explicit "Child MOCs" or "Sub-MOC" callout to each Tier 1 parent MOC so the hierarchy is navigable 12. Move out-of-folder MOCs (`Barista/`, `Botany/`, `Coffee Equipment/`, etc.) to `Maps of Content/`, or document the folder structure as intentional in the ToC