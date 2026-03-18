#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from datetime import datetime, timezone
from pathlib import Path

def load_json(path: Path):
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)

def iter_rules(rules_dir: Path):
    for path in sorted(rules_dir.rglob('*.json')):
        yield path, load_json(path)

def build_catalog(input_root: Path, output_path: Path, base_catalog_path: Path | None = None):
    rules_dir = input_root / 'catalog' / 'rules'
    rules = []
    for path, rule in iter_rules(rules_dir):
        rule.setdefault('_source_file', str(path.relative_to(input_root)).replace('\\','/'))
        rules.append(rule)
    rules.sort(key=lambda r: r.get('id',''))

    catalog = {
        'catalog_version': '0.2.0',
        'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'license': 'See LICENSE',
        'publisher': {
            'name': 'Sustainable IT Manifesto Foundation',
            'short_name': 'SITM'
        },
        'rule_id_namespace': 'ECO',
        'rules': rules,
        'tags': []
    }
    if base_catalog_path and base_catalog_path.exists():
        base = load_json(base_catalog_path)
        for key in ('catalog_version','license','publisher','rule_id_namespace','tags'):
            if key in base:
                catalog[key] = base[key]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open('w', encoding='utf-8') as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False, sort_keys=False)
        f.write('\n')
    return len(rules)


def main():
    ap = argparse.ArgumentParser(description='Build master.json from catalog/rules/**')
    ap.add_argument('--root', default='.', help='Repo root')
    ap.add_argument('--base-catalog', default='master.json', help='Optional metadata source')
    ap.add_argument('--out', default='catalog/master.json', help='Output catalog path')
    args = ap.parse_args()
    root = Path(args.root).resolve()
    count = build_catalog(root, root / args.out, root / args.base_catalog)
    print(f'Built catalog with {count} rules -> {args.out}')

if __name__ == '__main__':
    main()
