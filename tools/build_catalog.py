#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def find_rules_dir(root: Path, explicit: str | None = None) -> Path:
    candidates = []
    if explicit:
        candidates.append(root / explicit)
    candidates.extend([root / 'catalog' / 'rules', root / 'rules'])
    for path in candidates:
        if path.exists() and path.is_dir():
            return path
    raise FileNotFoundError('Could not find rules directory. Tried: ' + ', '.join(str(p) for p in candidates))


def iter_rules(rules_dir: Path):
    for path in sorted(rules_dir.rglob('*.json')):
        yield path, load_json(path)


def infer_version(root: Path, base_catalog_path: Path | None, explicit_version: str | None) -> str:
    if explicit_version:
        return explicit_version
    for candidate in [base_catalog_path, root / 'catalog' / 'master.json', root / 'master.json', root / 'catalog' / 'registry.json', root / 'registry.json']:
        if candidate and candidate.exists():
            data = load_json(candidate)
            if isinstance(data, dict):
                return data.get('catalog_version') or data.get('version') or '0.4.0'
    return '0.4.0'


def build_catalog(input_root: Path, output_path: Path, base_catalog_path: Path | None = None, rules_dir_arg: str | None = None, version: str | None = None) -> int:
    rules_dir = find_rules_dir(input_root, rules_dir_arg)
    rules = []
    for path, rule in iter_rules(rules_dir):
        if isinstance(rule, dict):
            rule.setdefault('_source_file', str(path.relative_to(input_root)).replace('\\','/'))
            rules.append(rule)
    rules.sort(key=lambda r: r.get('id',''))

    catalog = {
        'catalog_version': infer_version(input_root, base_catalog_path, version),
        'generated_at': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        'license': 'See LICENSE',
        'publisher': {'name': 'Sustainable IT Manifesto Foundation', 'short_name': 'SITM'},
        'rule_id_namespace': 'ECO',
        'rules': rules,
        'tags': []
    }
    if base_catalog_path and base_catalog_path.exists():
        base = load_json(base_catalog_path)
        for key in ('catalog_version','license','publisher','rule_id_namespace','tags'):
            if key in base:
                catalog[key] = base[key]
    if version:
        catalog['catalog_version'] = version
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open('w', encoding='utf-8') as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False, sort_keys=False)
        f.write('\n')
    return len(rules)


def main() -> int:
    ap = argparse.ArgumentParser(description='Build master.json from rules/** or catalog/rules/**')
    ap.add_argument('--root', default='.', help='Repo root')
    ap.add_argument('--rules-dir', default=None, help='Rules directory relative to root')
    ap.add_argument('--base-catalog', default='catalog/master.json', help='Optional metadata source')
    ap.add_argument('--out', default='catalog/master.json', help='Output catalog path')
    ap.add_argument('--version', default=None, help='Override catalog_version')
    args = ap.parse_args()
    root = Path(args.root).resolve()
    base = root / args.base_catalog if args.base_catalog else None
    count = build_catalog(root, root / args.out, base, args.rules_dir, args.version)
    print(f'Built catalog with {count} rules -> {args.out}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
