---
title: Getting Started
description: Run, edit, and extend the site locally.
tags:
  - how-to
  - reference
---

# Getting Started

This page covers the day-to-day workflow: running the site locally, adding pages, and using the Markdown features that are turned on.

## Local commands

```bash
# one-time
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# every session
mkdocs serve            # live-reload at http://127.0.0.1:8000
mkdocs build --strict   # produce ./site, fail on warnings
```

!!! note "Why `--strict`?"
    Strict mode turns warnings (broken links, orphaned pages, missing nav entries) into build failures. Catch them locally instead of in production.

## Adding a page

1. Create a Markdown file under `docs/`, e.g. `docs/coffee/v60-recipe.md`.
2. Add a frontmatter block:

    ```yaml
    ---
    title: V60 Recipe
    description: A repeatable 1:16 V60 method.
    tags:
      - coffee
      - how-to
    ---
    ```

3. Link it from a parent page **or** add it to `nav:` in `mkdocs.yml`.
4. Run `mkdocs serve` and verify the link, the TOC, and any cross-references render.

## Markdown features enabled

### Admonitions

!!! warning "Heads up"
    Admonitions support `note`, `tip`, `warning`, `danger`, `info`, `example`, `quote`, and more.

??? example "Collapsible details"
    Use `???` for collapsed-by-default, `???+` for expanded-by-default.

### Code blocks with highlighting & annotations

```python title="brew.py" linenums="1" hl_lines="3"
def brew(dose_g, ratio=16):
    water_g = dose_g * ratio  # (1)!
    return water_g
```

1. Inline annotation — click the marker in the rendered page.

### Tabs

=== "Pour-over"
    - Dose: 15 g
    - Water: 240 g
    - Time: 2:30–3:00

=== "Espresso"
    - Dose: 18 g
    - Yield: 36 g
    - Time: 25–30 s

### Tables

| Method     | Ratio | Grind   |
| ---------- | ----- | ------- |
| V60        | 1:16  | Medium  |
| AeroPress  | 1:14  | Med-fine|
| Espresso   | 1:2   | Fine    |

### Task lists

- [x] Scaffold the site
- [x] Add starter content
- [ ] Migrate Obsidian vault sections
- [ ] Wire up CI build

### Footnotes & definitions

Pour-over is a percolation method[^perc].

[^perc]: Water moves through a bed of grounds once, by gravity, without prolonged immersion.

Percolation
:   A brewing process where water passes through coffee grounds a single time.

Immersion
:   A brewing process where grounds steep in water before separation.

### Keys & inline highlights

Press ++ctrl+k++ to focus the search box. Inline code like `mkdocs serve` and ==highlighted text== are supported.

### Mermaid diagrams

```mermaid
flowchart LR
    A[Obsidian vault] --> B[Curate & tag]
    B --> C[Promote to docs/]
    C --> D[mkdocs build]
    D --> E[Published site]
```

## Troubleshooting

- **`Config value 'plugins'` error:** the plugin is listed in `mkdocs.yml` but not installed. Run `pip install -r requirements.txt`.
- **Broken link warnings under `--strict`:** check the relative path; MkDocs resolves links relative to the source file, not the URL.
- **Search not finding a page:** make sure it's reachable from `nav:` or linked from another page. Orphan pages aren't indexed in some configurations.
