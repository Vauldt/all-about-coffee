# Coffeepedia

A [MkDocs](https://www.mkdocs.org/) site using the [Material](https://squidfunk.github.io/mkdocs-material/) theme. The content is a publishing-oriented import of the Coffeepedia Obsidian vault, converted into MkDocs-friendly Markdown under `docs/coffee/`.

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
mkdocs build

# 5. Verify the production build
mkdocs build --strict
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
│   ├── coffee/            # Imported Coffeepedia vault pages
│   └── assets/coffee/     # Imported coffee assets
├── .github/workflows/
│   └── deploy-pages.yml # GitHub Pages deployment workflow
└── README.md
```

## Coffee vault import

- Imported from the curated `AllAboutCoffee` branch of the Obsidian vault.
- Excluded private/non-publishing folders: daily journals, inbox captures, templates, trash, `.obsidian`, `.claude`, and `.git`.
- Converted Obsidian wikilinks such as `[[Coffee Extraction|extraction]]` into Markdown links where a unique target could be resolved.
- Slugified folders and filenames for stable web URLs.
- Generated lightweight `index.md` pages for folders so large sections are browsable.
- Removed the original traffic-operations sample content.

This import builds successfully with `mkdocs build --strict`.

## Updating from Obsidian

`scripts/sync_coffee_vault.py` is the single command for refreshing the
site from Matthew's local Obsidian vault. It imports Markdown + assets,
slugifies paths, converts Obsidian wikilinks and embeds where uniquely
resolvable, generates folder index pages, cleans up known broken
references, and (optionally) runs a strict build and pushes the result.

```bash
# Default vault path: /Users/chris/Obsidian Vaults/Coffee/AllAboutCoffee
python3 scripts/sync_coffee_vault.py

# Preview locally with live reload
mkdocs serve

# Strict production build (same check CI runs)
mkdocs build --strict

# Full local update -> strict build -> commit -> push to origin
python3 scripts/sync_coffee_vault.py --push

# Override the vault location if needed
python3 scripts/sync_coffee_vault.py \
    --vault-path "/Users/chris/Obsidian Vaults/Coffee/AllAboutCoffee"

# Sync without running the strict build (faster iteration)
python3 scripts/sync_coffee_vault.py --no-build
```

Equivalent `make` targets are provided for convenience:

```bash
make sync          # Sync vault + strict build
make sync-no-build # Sync only, no build
make sync-push     # Sync, strict build, commit, push
make serve         # Live preview
make strict        # mkdocs build --strict
```

The script rewrites everything under `docs/coffee/` and
`docs/assets/coffee/` on each run, so do not hand-edit those folders —
edit notes in the Obsidian vault and re-run the sync.

## GitHub Pages deployment

The repository includes `.github/workflows/deploy-pages.yml`, which publishes the site with GitHub Actions.

### First-time setup

1. Create a GitHub repository for this project.
2. Push this folder to the repository, preferably on the `main` branch.
3. In GitHub, open **Settings → Pages**.
4. Set **Build and deployment → Source** to **GitHub Actions**.
5. Push to `main`, or run the workflow manually from **Actions → Deploy Coffeepedia to GitHub Pages → Run workflow**.

The workflow:

- installs dependencies from `requirements.txt`
- runs `mkdocs build --strict`
- uploads the generated `site/` directory
- deploys it to GitHub Pages

If you know the final repository URL, set `site_url` in `mkdocs.yml` to the GitHub Pages address, for example:

```yaml
site_url: https://USERNAME.github.io/REPOSITORY/
```

## Authoring notes

- Write Markdown files anywhere under `docs/`. The curated top-level navigation is listed in `mkdocs.yml`; the full coffee vault remains searchable without putting every note into every page sidebar.
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
