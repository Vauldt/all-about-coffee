---
title: "Style Guide for This Vault"
tags: [coffee/education]
status: Draft
aliases: []
related: []
---

# Style Guide for This Vault

**Tags:** #meta/index #style-guide
**Related:** [Tag Index](tag-index.md) | All About Coffee — Map of Content (MOC)
**Purpose:** Defines the standards for writing, formatting, and structuring all notes in the Coffee Encyclopedia vault. Follow this guide when creating new notes or revising existing ones.

---

## Core Principles

1. **Consistency** — Every note should feel like it belongs to the same reference work
2. **Navigability** — Every note should link outward to at least two related notes
3. **Granularity** — One concept per note; split large topics into sub-notes rather than growing a single note indefinitely
4. **Progressive detail** — Lead with a plain-language overview before introducing technical depth
5. **Australian English** — Use Australian spelling throughout (e.g. *flavour*, *colour*, *organisation*, *recognised*)

---

## Note Architecture

Every encyclopedia entry should follow this structure in order:

~~~markdown
# Note Title

**Tags:** #coffee/[category]/[subcategory]
**Aliases:** [alternative names or spellings]
**Related:** Link 1 | Link 2 | Link 3
**Status:** 🌱 Stub / 🔄 In Progress / ✅ Complete

---

## Overview
[2–4 sentence plain-language summary of the topic. Write as if introducing
the concept to an intelligent reader with no prior coffee knowledge.]

## [Main Section 1]
[Detailed content]

## [Main Section 2]
[Detailed content]

## [Main Section 3]
[Detailed content]

## Key Facts
[Bullet-point summary of the most important figures, dates, or parameters
associated with this topic. Ideal for quick reference.]

## Related Notes
- Note A
- Note B
- Note C

## References
- [Source 1]
- [Source 2]

## Changelog
| Date | Change |
| :--- | :--- |
| YYYY-MM-DD | Note created |
~~~

---

## Frontmatter Fields

| Field | Required | Notes |
| :--- | :--- | :--- |
| `Tags` | ✅ Yes | Minimum one `#coffee/*` tag. See [Tag Index](tag-index.md) |
| `Aliases` | Recommended | Include common alternate names, abbreviations, non-English terms |
| `Related` | ✅ Yes | Minimum two wikilinks to closely related notes |
| `Status` | ✅ Yes | Use 🌱 / 🔄 / ✅ consistently |

---

## Heading Conventions

| Level | Use For |
| :--- | :--- |
| `#` H1 | Note title only — one per note |
| `##` H2 | Major sections (Overview, Key Facts, Related Notes, References, Changelog) |
| `###` H3 | Sub-sections within a major section |
| `####` H4 | Avoid where possible; split into a new note instead |

---

## Writing Style

### Voice and Tone
- Write in the **third person** — avoid "you" or "we"
- Use **active voice** where possible
- Be **precise but readable** — this is an encyclopedia, not an academic paper
- Avoid marketing language (e.g. "delicious", "amazing", "world-class")

### Terminology
- On first use of a technical term, briefly define it inline
  - ✅ *The mucilage — a sticky, pectin-rich layer surrounding the parchment — is removed during fermentation*
  - ❌ *The mucilage is removed during fermentation*
- Use the **SCA** (Specialty Coffee Association) as the reference standard for terminology where applicable
- Capitalise proper nouns: *Arabica*, *Robusta*, *Maillard reaction*, *Cup of Excellence*
- Do not capitalise generic descriptors: *espresso*, *filter coffee*, *green bean*

### Numbers and Units
- Spell out numbers one through nine; use numerals for 10 and above
- Always include units: **°C** for temperature, **%** for moisture and humidity, **g** for grams, **mL** for millilitres
- Use **metric units** exclusively
- Express ranges with an en dash: *10.5–12%*, *15–21°C*

### Dates
- Use ISO 8601 format in changelogs and frontmatter: **YYYY-MM-DD**
- Use day-month-year in prose: *21 March 2026*

---

## Tables

Use tables for:
- Comparative data (e.g. processing method comparison)
- Parameter ranges (e.g. storage conditions)
- Quick reference grids

Table formatting rules:
- Always include a header row
- Left-align text columns; right-align or centre numeric columns
- Keep cell content concise — link out to a dedicated note for detail

---

## Lists

- Use **bullet points** for unordered items with no hierarchy of importance
- Use **numbered lists** for sequential steps or ranked items
- Use **nested bullets** sparingly — maximum two levels of nesting
- End list items without a full stop unless the item is a complete sentence

---

## Links and Wikilinks

- Use `Wikilink` for all internal note references
- Use `Display Text` when the display text should differ from the note title
- Place inline wikilinks naturally within prose rather than clustering them at the end of a sentence
- External URLs should be placed in the **References** section, not inline in prose

---

## Code Blocks and Callouts

Use Obsidian callout blocks to highlight important information:

~~~markdown
> [!NOTE]
> Use for supplementary context that does not fit the main narrative.

> [!TIP]
> Use for practical advice, especially in brewing or storage notes.

> [!WARNING]
> Use for safety-critical or quality-critical parameters (e.g. moisture thresholds).

> [!IMPORTANT]
> Use for industry standards or certification requirements.
~~~

---

## Images and Diagrams

- Store all images in the `/Assets/Images/` folder
- Name images descriptively using kebab-case: `wet-processing-fermentation-tank.jpg`
- Always include alt text in image embeds:
  - `wet-processing-fermentation-tank`
- Diagrams and process flow charts are encouraged for processing and brewing notes

---

## Status Definitions

| Status | Emoji | Meaning |
| :--- | :--- | :--- |
| Stub | 🌱 | Note created, placeholder content only |
| In Progress | 🔄 | Actively being researched and written |
| Complete | ✅ | Fully written, fact-checked, and reviewed |

A note should only be marked ✅ Complete when:
- All major sections are populated
- At least two outbound wikilinks exist
- At least one reference source is listed
- Australian English spelling has been applied throughout

---

## Note Naming Conventions

| Rule | Example |
| :--- | :--- |
| Use title case for all note names | `Wet-Processed Green Coffee` |
| Include parenthetical clarifiers for ambiguous titles | `Honey Processing (Coffee)` |
| Use the most common English name as the primary title | `Gesha / Geisha Cultivar` |
| Avoid abbreviations in note titles | `Specialty Coffee Association (SCA)` not `SCA` |

---

## Templates

See Note Templates for ready-to-use templates for:
- Standard encyclopedia entry
- Origin / geography note
- Cultivar / variety note
- Equipment note
- Business and industry note

---

## Changelog

| Date | Change |
| :--- | :--- |
| 2026-03-21 | Style Guide created |