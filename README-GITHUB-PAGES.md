# GitHub Pages Jungle Theme

This vault did not already contain a GitHub Pages build system, so these files add a lightweight Jekyll setup with a jungle-inspired palette. Jekyll is a better fit than MkDocs here because the Markdown notes already live at the repository root.

## Files added

- `_config.yml` configures Jekyll for the vault.
- `_layouts/default.html` defines the shared page layout.
- `assets/css/style.scss` defines the jungle palette and reading theme.
- `assets/images/jungle-coffee-mark.svg` provides the site logo and favicon.
- `.github/workflows/pages.yml` builds and deploys the site to GitHub Pages.

## Palette

- Canopy green: `#0f3d2e`
- Deep canopy: `#08251c`
- Leaf green: `#1f6b45`
- Fern accent: `#78a557`
- Moss highlight: `#b8c67a`
- Bark brown: `#5b4633`
- Earth brown: `#8a6846`
- Parchment surface: `#f4efd9`
- Mist surface: `#dfe8d2`
- Coffee cherry accent: `#9f3f2f`
- Amber highlight: `#d49b49`

## How to use

1. Commit these files to the repository.
2. In GitHub, go to **Settings → Pages**.
3. Set **Build and deployment** to **GitHub Actions**.
4. Push to `main` or `master`, or run the workflow manually.

For a local preview, install Jekyll and run:

```bash
bundle exec jekyll serve
```
