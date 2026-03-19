#!/usr/bin/env python3
"""Generate a human-readable catalog from per-rule files or a bundled catalog.

Prefers normalized Option A fields:
- category_code, family_code
- layer in lowercase machine values
- ontology.system_layers as lowercase machine values
"""
from __future__ import annotations
import argparse, json, os, re, shutil
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

LAYER_LABELS = {
    'data': 'Data',
    'network': 'Network',
    'code': 'Code',
    'architecture': 'Architecture',
    'ai': 'AI',
    'process': 'Process'
}

def slugify(s: str) -> str:
    s = (s or '').strip().lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return re.sub(r'-+', '-', s).strip('-') or 'item'

def safe(s: str) -> str:
    return re.sub(r'[^A-Za-z0-9._-]+', '_', s or 'UNKNOWN')

def load_json(path: Path):
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)

def load_registry(path: Path | None):
    return load_json(path) if path and path.exists() else {'categories':{}, 'families':{}}

def resolve_category_name(rule, registry):
    code = rule.get('category_code') or rule.get('ontology', {}).get('category_code')
    if code and code in registry.get('categories', {}):
        return registry['categories'][code].get('name', code)
    return rule.get('category', code or 'Unknown')

def resolve_family_name(rule, registry):
    code = rule.get('family_code') or rule.get('ontology', {}).get('family_code')
    if code and code in registry.get('families', {}):
        return registry['families'][code].get('name', code)
    return rule.get('family', code or 'Unknown')

def resolve_layer(rule):
    layer = rule.get('layer')
    if isinstance(layer, str) and layer:
        return LAYER_LABELS.get(layer, layer.title())
    olayers = rule.get('ontology', {}).get('system_layers', [])
    if olayers:
        return ', '.join(LAYER_LABELS.get(x, str(x).title()) for x in olayers)
    return 'Unknown'

def iter_rules(root: Path):
    rules_dir = root / 'catalog' / 'rules'
    if rules_dir.exists():
        for path in sorted(rules_dir.rglob('*.json')):
            yield load_json(path)
        return
    bundled = root / 'catalog' / 'master.json'
    if not bundled.exists():
        bundled = root / 'master.json'
    data = load_json(bundled)
    for rule in data.get('rules', []):
        yield rule

def render_rule(rule, registry):
    rid = rule.get('id', 'UNKNOWN')
    title = rule.get('title', '')
    category = resolve_category_name(rule, registry)
    family = resolve_family_name(rule, registry)
    layer = resolve_layer(rule)
    severity = rule.get('severity', '')
    tier = rule.get('tier', '')
    tags = rule.get('tags', [])
    parts = [f'# {rid} — {title}', '']
    meta = [
        f'- **Category:** {category} ({rule.get("category_code","?")})',
        f'- **Family:** {family} ({rule.get("family_code","?")})',
        f'- **Layer:** {layer}',
    ]
    if tier != '': meta.append(f'- **Tier:** {tier}')
    if severity: meta.append(f'- **Severity:** {severity}')
    if tags: meta.append(f'- **Tags:** {", ".join(tags)}')
    if rule.get('legacy_id'): meta.append(f'- **Legacy ID:** {rule["legacy_id"]}')
    parts.extend(meta)
    parts.append('')
    for section, key in [('Summary','summary'), ('Rationale','rationale')]:
        if rule.get(key):
            parts.extend([f'## {section}', '', str(rule[key]).strip(), ''])
    for section, key in [('Impact','impact'), ('Detection','detection'), ('Remediation','remediation'), ('Ontology','ontology')]:
        if rule.get(key):
            parts.extend([f'## {section}', '', '```json', json.dumps(rule[key], indent=2, ensure_ascii=False, sort_keys=True), '```', ''])
    return '\n'.join(parts).rstrip() + '\n'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--out', default='docs/catalog/')
    ap.add_argument('--registry', default='catalog/registry.json')
    args = ap.parse_args()
    root = Path(args.root).resolve()
    out = root / args.out
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    registry = load_registry(root / args.registry)
    rules = list(iter_rules(root))
    rules.sort(key=lambda r: r.get('id',''))
    by_cat = defaultdict(list)
    for r in rules:
        by_cat[r.get('category_code','UNC')].append(r)
    index = [
        '# Eco Rules Catalog (Human Readable)',
        '',
        f'**Generated at:** {datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}',
        f'**Total rules:** {len(rules)}',
        '',
        '## Categories',
        ''
    ]
    for cat_code in sorted(by_cat):
        cat_name = registry.get('categories', {}).get(cat_code, {}).get('name', cat_code)
        index.append(f'- [{cat_name} ({cat_code})](categories/{slugify(cat_code)}/index.md) ({len(by_cat[cat_code])} rules)')
    index += ['', '## Rule Index', '', '| ID | Title | Category | Family | Layer | Severity |', '|---|---|---|---|---|---|']
    for r in rules:
        cat = r.get('category_code','UNC')
        fam = r.get('family_code','GEN')
        rule_path = f'categories/{slugify(cat)}/families/{slugify(fam)}/{safe(r.get("id","UNKNOWN"))}.md'
        index.append(f'| [{r.get("id","")}]({rule_path}) | {r.get("title","")} | {resolve_category_name(r, registry)} | {resolve_family_name(r, registry)} | {resolve_layer(r)} | {r.get("severity","")} |')
    (out / 'index.md').write_text('\n'.join(index) + '\n', encoding='utf-8')
    for cat_code, cat_rules in by_cat.items():
        cat_dir = out / 'categories' / slugify(cat_code)
        (cat_dir / 'families').mkdir(parents=True, exist_ok=True)
        fam_groups = defaultdict(list)
        for r in cat_rules:
            fam_groups[r.get('family_code','GEN')].append(r)
        cat_name = registry.get('categories', {}).get(cat_code, {}).get('name', cat_code)
        cat_index = [f'# {cat_name} ({cat_code})', '', f'- [Back to catalog index](../../index.md)', '', '## Families', '']
        for fam_code, fam_rules in sorted(fam_groups.items()):
            fam_name = registry.get('families', {}).get(fam_code, {}).get('name', fam_code)
            cat_index.append(f'- [{fam_name} ({fam_code})](families/{slugify(fam_code)}/index.md) ({len(fam_rules)} rules)')
            fam_dir = cat_dir / 'families' / slugify(fam_code)
            fam_dir.mkdir(parents=True, exist_ok=True)
            fam_index = [f'# {fam_name} ({fam_code})', '', f'- [Back to {cat_name}](../../index.md)', '', '| ID | Title | Severity | Layer |', '|---|---|---|---|']
            for r in sorted(fam_rules, key=lambda x: x.get('id','')):
                fam_index.append(f'| [{r.get("id","")}]({safe(r.get("id","UNKNOWN"))}.md) | {r.get("title","")} | {r.get("severity","")} | {resolve_layer(r)} |')
                (fam_dir / f'{safe(r.get("id","UNKNOWN"))}.md').write_text(render_rule(r, registry), encoding='utf-8')
            (fam_dir / 'index.md').write_text('\n'.join(fam_index) + '\n', encoding='utf-8')
        (cat_dir / 'index.md').write_text('\n'.join(cat_index) + '\n', encoding='utf-8')
    print(f'Generated {len(rules)} rule pages -> {out}')

if __name__ == '__main__':
    main()
