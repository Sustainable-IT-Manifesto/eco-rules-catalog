# Contributing

1. Update `master.json`
2. Run:

```bash
python tools/update_rules.py --catalog master.json --categories ontology/categories.json --families ontology/families.json --write --fill-system-layer --normalize-ontology
python tools/validate_ontology.py --in master.json --require-ontology
python tools/validate_catalog.py --catalog master.json --categories ontology/categories.json --families ontology/families.json
python generate_human_catalog.py --in master.json --out eco_catalog_human --examples-dir examples
```
