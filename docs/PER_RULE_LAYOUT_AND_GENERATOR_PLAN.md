# Per-rule layout and generator update

This patch adds a source-oriented layout for the Eco Rules Catalog.

## What changed

- Added `catalog/rules/<CATEGORY_CODE>/<FAMILY_CODE>/<RULE_ID>.json`
- Added `tools/split_catalog.py` to split an existing bundled catalog into per-rule source files
- Added `tools/build_catalog.py` to rebuild `catalog/master.json`
- Added `tools/generate_human_catalog_v2.py` to render the human catalog from either per-rule files or a bundled catalog

## Why this matters

This makes rule review, contribution, governance, and release management much easier.

Instead of editing one large file, contributors can update a single rule in isolation.

## Recommended workflow

1. Edit a single rule file under `catalog/rules/...`
2. Run validation
3. Rebuild `catalog/master.json`
4. Regenerate the human catalog
5. Commit both source and generated outputs if desired

## Suggested commands

```bash
python tools/build_catalog.py --root . --base-catalog master.json --out catalog/master.json
python tools/generate_human_catalog_v2.py --root . --out eco_catalog_human_v2 --registry catalog/registry.json
```

## Notes

The v2 human generator prefers normalized Option A fields:

- `category_code`
- `family_code`
- lowercase machine values for `layer`
- lowercase machine values for `ontology.system_layers`

It still falls back to legacy fields where possible.
