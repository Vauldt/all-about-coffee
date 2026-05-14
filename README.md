# Matthew's Knowledge Site

A [MkDocs](https://www.mkdocs.org/) site using the [Material](https://squidfunk.github.io/mkdocs-material/) theme. The content is authored as plain Markdown (Obsidian-compatible) under `docs/`.

## Quick start

```bash
# 1. Create and activate a virtualenv (recommended)
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Serve locally with live-reload (http://127.0.0.1:8000)
mkdocs serve

# 4. Build the static site into ./site
mkdocs build --strict

# 5. (Optional) Deploy to GitHub Pages
# mkdocs gh-deploy --force
```

## Project layout

```
matthew-mkdocs-site/
├── mkdocs.yml           # Site config, theme, nav, extensions
├── requirements.txt     # Python deps (mkdocs, material, plugins)
├── docs/
│   ├── index.md
│   ├── getting-started.md
│   ├── knowledge-architecture.md
│   ├── coffee/
│   │   └── index.md
│   └── traffic-operations/
│       └── index.md
└── README.md
```

## Authoring notes

- Write Markdown files anywhere under `docs/`. Folders become navigation sections (manually listed in `mkdocs.yml` `nav:` for now).
- Use `index.md` inside any folder to define that section's landing page (enabled by `navigation.indexes`).
- Frontmatter `tags:` are indexed by the `tags` plugin and surfaced on a tags page.
- Admonitions, footnotes, def-lists, tabbed blocks, task lists, code highlighting, and Mermaid diagrams are all enabled — see `docs/getting-started.md` for examples.

## Optional plugins

`requirements.txt` installs a few extra plugins that are **not** enabled by default. To turn one on, add it under `plugins:` in `mkdocs.yml`, for example:

```yaml
plugins:
  - search
  - tags
  - glightbox
  - awesome-pages
  - git-revision-date-localized:
      enable_creation_date: true
  - minify:
      minify_html: true
```

## License

Content © Matthew Clairmont. Site generated with MkDocs Material (BSD-2-Clause).
