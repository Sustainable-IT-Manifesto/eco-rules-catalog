# Repository Structure Proposal

This proposal keeps the current repository usable while introducing a cleaner center of gravity for SITM stewardship.

## Recommended shape

```text
.
├── catalog/
│   ├── registry.json
│   ├── schema/
│   │   └── schema-registry.json
│   ├── rules/
│   │   ├── CMP/
│   │   ├── DAT/
│   │   ├── NET/
│   │   ├── STO/
│   │   ├── CON/
│   │   ├── AIM/
│   │   ├── ARC/
│   │   ├── OPS/
│   │   ├── INF/
│   │   └── ORG/
│   ├── master.json
│   └── releases/
├── docs/
├── docs-site/
├── templates/
├── tools/
└── .github/workflows/
```

## Why this works

- `catalog/registry.json` becomes the single source of truth for category and family lookups.
- `catalog/rules/` makes single-rule changes reviewable.
- `master.json` becomes a generated artifact instead of a hand-edited bundle.
- `docs-site/` remains the public static site.
- `tools/` remains the build and validation layer.

## Migration path

1. Add `catalog/registry.json` and validate it in CI.
2. Keep the current `ontology/*.json` files for compatibility during migration.
3. Move new rules into `catalog/rules/<CATEGORY>/<FAMILY>/`.
4. Generate `master.json` from the per-rule files.
5. Retire duplicate registries once all tooling points at `catalog/registry.json`.
