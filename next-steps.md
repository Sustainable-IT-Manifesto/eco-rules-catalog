Here’s a **GitHub Pages–hosted rules website** that works well for a catalog like yours, supports search, and can auto-publish from `main`.

I’m going to recommend **MkDocs + Material** because it’s:

* static (perfect for GitHub Pages)
* searchable
* clean nav
* easy to automate
* friendly to Markdown

Below is a complete, drop-in site skeleton + a build step that can publish your generated `eco_catalog_human/` content.

---

## Repo layout

Put the website in `docs-site/` and publish from it:

```
/master.json
/generate_human_catalog.py
/requirements.txt
/tools/validate_ontology.py
/tools/normalize_ontology.py

/eco_catalog_human/          # generated rule docs (your existing output)

/docs-site/
  mkdocs.yml
  requirements.txt
  docs/
    index.md
    catalog.md
    ontology.md
    contributing.md
    assets/
      logo.svg (optional)
```

During deploy, we’ll **copy `eco_catalog_human/` into `docs-site/docs/catalog/`** so it becomes part of the site.

---

# 1) `docs-site/mkdocs.yml`

```yaml
site_name: Eco Rules Catalog
site_description: Human-readable documentation for the Eco Rules Catalog
site_url: https://<YOUR_GITHUB_USERNAME>.github.io/<YOUR_REPO>/
repo_url: https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO>
edit_uri: edit/main/docs-site/docs/

theme:
  name: material
  features:
    - navigation.instant
    - navigation.sections
    - navigation.expand
    - navigation.path
    - toc.follow
    - search.highlight
    - search.share
  palette:
    scheme: default

markdown_extensions:
  - tables
  - toc:
      permalink: true
  - fenced_code
  - admonition
  - footnotes

plugins:
  - search

nav:
  - Home: index.md
  - Catalog:
      - Overview: catalog.md
      - Browse Rules: catalog/index.md
  - Ontology: ontology.md
  - Contributing: contributing.md
```

Notes:

* `catalog/index.md` will be generated from your `eco_catalog_human/index.md` (we’ll copy it).

---

# 2) `docs-site/requirements.txt`

```txt
mkdocs==1.6.0
mkdocs-material==9.5.28
```

(Keep this separate from your catalog generator requirements.)

---

# 3) Website pages

### `docs-site/docs/index.md`

```md
# Eco Rules Catalog

A structured catalog of software inefficiency patterns that waste compute, energy, network bandwidth, memory, and engineering time.

This site is the human-readable documentation for the Eco Rules Catalog.

## What you’ll find here

- A browsable catalog organized by **Family → Layer → Tier**
- Per-rule pages with **summary, rationale, raw impact/detection/remediation**, and optional **examples**
- Ontology documentation that standardizes classification

## Quick links

- [Browse the catalog](catalog/index.md)
- [Ontology](ontology.md)
- [Contributing](contributing.md)
```

### `docs-site/docs/catalog.md`

````md
# Catalog Overview

The catalog is stored in `master.json` (machine-readable) and rendered into Markdown for humans.

## Structure

Rules are organized by:

- **Family** (technology ecosystem)
- **Layer** (where the inefficiency occurs)
- **Tier** (complexity / maturity)

## Generating the catalog

From the repo root:

```bash
python generate_human_catalog.py --in master.json --out eco_catalog_human
````

Examples can be added in `examples/<RULE_ID>.md` and included during generation.

````

### `docs-site/docs/ontology.md`

```md
# Ontology

The ontology standardizes how rules describe:

- Resource impacts
- Mechanisms
- System layers
- Detection methods
- Remediation patterns

These controlled vocabularies enable consistent analysis and reporting.

See `docs/ontology/` in the repository for the full specification.
````

### `docs-site/docs/contributing.md`

````md
# Contributing

Contributions are welcome.

## Adding or updating rules

1. Update `master.json`
2. Normalize:
   ```bash
   python tools/normalize_ontology.py --in master.json --write --fill-system-layer
````

3. Validate:

   ```bash
   python tools/validate_ontology.py --in master.json --require-ontology
   ```
4. Regenerate docs:

   ```bash
   python generate_human_catalog.py --in master.json --out eco_catalog_human --examples-dir examples
   ```

## Adding examples

Add files:

* `examples/<RULE_ID>.md`

Use:

* `## Bad`
* `## Better`

````

---

# 4) GitHub Actions: build + publish to GitHub Pages

Create: `.github/workflows/pages.yml`

```yaml
name: Publish Rules Site

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      # 1) Generate the human catalog from master.json
      - name: Install catalog generator deps
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Generate catalog markdown
        run: |
          if [ -d "examples" ]; then
            python generate_human_catalog.py --in master.json --out eco_catalog_human --examples-dir examples
          else
            python generate_human_catalog.py --in master.json --out eco_catalog_human
          fi

      # 2) Build MkDocs site
      - name: Install site deps
        run: |
          pip install -r docs-site/requirements.txt

      - name: Sync generated catalog into site
        run: |
          rm -rf docs-site/docs/catalog
          mkdir -p docs-site/docs/catalog
          cp -R eco_catalog_human/* docs-site/docs/catalog/

      - name: Build site
        run: |
          mkdocs build -f docs-site/mkdocs.yml -d site

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: site

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy
        id: deployment
        uses: actions/deploy-pages@v4
````

---

# 5) GitHub Pages settings

In your repo:

**Settings → Pages**

* Source: **GitHub Actions**

That’s it.

---

## Optional polish (worth doing)

### A) Put your catalog version in the site header

MkDocs supports `extra` metadata you can inject; if you want, I can show a tiny script step that reads `catalog_version` from `master.json` and sets it in `mkdocs.yml`.

### B) “Rule index” landing page

Your generated `eco_catalog_human/index.md` already has a table. That becomes `catalog/index.md` and is searchable.

### C) Custom domain

If you later want `rules.makingsoftwaregreener.com`, GitHub Pages supports it.

---

## If you want, I can also add

* a “search by tags/mechanism/resource” page generated from JSON (not just MkDocs search)
* an “ontology browser” page
* a versioned site (`/v1/`, `/v2/`) so you can keep stable releases

Say the word and I’ll give you the exact generator + site pages for those.
