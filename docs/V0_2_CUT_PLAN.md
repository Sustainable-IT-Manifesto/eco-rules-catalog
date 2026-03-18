# Eco Rules Catalog v0.2 Cut Plan (Option A)

## Decision locked
- Rules carry `category_code` and `family_code` as canonical values.
- Human-readable `category` and `family` remain for docs and readability, but are normalized from the registry.
- IDs are derived and validated as `ECO-{CATEGORY_CODE}-{FAMILY_CODE}-{SEQUENCE}`.
- Ontology values are normalized to lowercase machine values.

## Migration sequence
1. Add `catalog/registry.json` and validate it in CI.
2. Replace the existing rule schema with the v2 schema in this pack.
3. Run `tools/migrate_rules.py master.json migrated/master.v0_2.json --report migrated/report.json`.
4. Review migration errors, especially family/category mismatches.
5. Run `tools/validate_rules_v2.py migrated/master.v0_2.json`.
6. Freeze `master.json` as generated output only.
7. Move source rules into per-rule files under `catalog/rules/`.
8. Publish docs to GitHub Pages and machine artifacts in GitHub Releases.

## What will break
- Existing schema validation based on title-cased layers.
- Any tooling that assumes IDs look like `ECO-PY-001`.
- Any tooling that infers category from free text instead of registry codes.

## What gets better
- No more silent family/category drift.
- Clear migration path from legacy IDs.
- Cleaner docs generation.
- Stronger API contract.
- Easier external integrations and certification alignment.

## Recommended short-term policy
- Treat unresolved category/family as build-breaking errors.
- Treat missing remediation examples as warnings until v1.0.
- Keep `legacy_id` during the migration window.
