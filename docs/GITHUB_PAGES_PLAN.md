# GitHub Pages Recommendation

Yes. GitHub Pages makes sense for the Eco Rules Catalog.

## Use GitHub Pages for

- Human-facing documentation
- Taxonomy, ontology, and philosophy pages
- Contribution guidance
- Changelog and release notes
- A browsable rendered catalog

## Do not use GitHub Pages for

- The canonical machine-readable catalog by itself
- Release artifact distribution by itself
- Dynamic APIs

## Recommended split

- GitHub repository: source of truth
- GitHub Releases: versioned artifacts such as `master.json`, schema bundles, and checksums
- GitHub Pages: public standard website for SITM

## Recommended stack

- MkDocs Material
- GitHub Actions
- GitHub Pages deployment from Actions
