#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
try:
    import jsonschema
except ImportError:
    print('ERROR: jsonschema is required. Install with: pip install jsonschema'); sys.exit(2)
ROOT = Path(__file__).resolve().parents[1]

def load_json(path: Path):
    with path.open('r', encoding='utf-8') as fh: return json.load(fh)

def main() -> int:
    ap=argparse.ArgumentParser(description='Validate registry.json against schema-registry.json and internal references.')
    ap.add_argument('--registry', default=str(ROOT/'catalog'/'registry.json'))
    ap.add_argument('--schema', default=str(ROOT/'catalog'/'schema'/'schema-registry.json'))
    args=ap.parse_args()
    registry=load_json(Path(args.registry)); schema=load_json(Path(args.schema))
    jsonschema.validate(registry, schema)
    categories=registry['categories']; families=registry['families']; statuses=set(registry['statuses']); errors=[]
    for code,item in categories.items():
        if item['status'] not in statuses: errors.append(f"category {code}: invalid status {item['status']!r}")
    for code,item in families.items():
        if item['status'] not in statuses: errors.append(f"family {code}: invalid status {item['status']!r}")
        if item['category_code'] not in categories: errors.append(f"family {code}: unknown category_code {item['category_code']!r}")
    if errors:
        for e in errors: print(f'ERROR: {e}')
        return 1
    print(f'OK: registry valid ({len(categories)} categories, {len(families)} families)')
    return 0
if __name__ == '__main__': raise SystemExit(main())
