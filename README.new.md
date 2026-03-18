# Eco Rules Catalog Option A Migration Pack

This pack contains the stricter, code-first migration artifacts for the Eco Rules Catalog.

Included:
- `catalog/registry.json`
- `catalog/schema/schema-rule.json`
- `catalog/schema/schema-registry.json`
- `tools/validate_registry.py`
- `tools/validate_rules_v2.py`
- `tools/migrate_rules.py`
- `docs/V0_2_CUT_PLAN.md`

## Expected next step
Run the migration script against the current `master.json`, then validate the migrated output.
