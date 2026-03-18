#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

def main():
    ap = argparse.ArgumentParser(description='Split a bundled catalog into catalog/rules/<CAT>/<FAM>/<ID>.json')
    ap.add_argument('--catalog', default='master.json')
    ap.add_argument('--out-root', default='catalog/rules')
    args = ap.parse_args()
    with open(args.catalog, 'r', encoding='utf-8') as f:
        data = json.load(f)
    out_root = Path(args.out_root)
    count = 0
    for rule in data.get('rules', []):
        cat = rule.get('category_code', 'UNC')
        fam = rule.get('family_code', 'GEN')
        rid = rule.get('id', f'rule-{count:03d}')
        target = out_root / cat / fam / f'{rid}.json'
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('w', encoding='utf-8') as f:
            json.dump(rule, f, indent=2, ensure_ascii=False, sort_keys=True)
            f.write('\n')
        count += 1
    print(f'Wrote {count} rules to {out_root}')

if __name__ == '__main__':
    main()
