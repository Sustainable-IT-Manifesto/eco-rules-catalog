#!/usr/bin/env python3
import argparse, json, os
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / 'registry.json'
EXPECTED_KEYS = ['resource_impacts','mechanisms','system_layers','detection_methods','remediation_patterns','lifecycle_stage']
OBJECT_KEYS = ['cost_dimensions','amplification','temporal_behavior']
LIST_KEYS = ['runtime_evidence']


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f: return json.load(f)

def _is_list_of_strings(x):
    return isinstance(x, list) and all(isinstance(i, str) and i.strip() for i in x)

def _ensure_dir(path):
    d = os.path.dirname(os.path.abspath(path))
    if d and not os.path.isdir(d): os.makedirs(d)

def validate(catalog, registry, require_ontology=False, strict=False):
    rules = catalog.get('rules', []) if isinstance(catalog, dict) else catalog
    if not isinstance(rules, list): raise ValueError("catalog['rules'] must be a list")
    canon = {
        'resource_impacts': set(registry.get('resource_impacts', [])),
        'system_layers': set(registry.get('system_layers', [])),
        'detection_methods': set(registry.get('detection_methods', [])),
        'remediation_patterns': set(registry.get('remediation_patterns', [])),
    }
    errors, warnings = [], []
    def err(rid,msg): errors.append({'rule_id':rid,'message':msg})
    def warn(rid,msg): warnings.append({'rule_id':rid,'message':msg})
    for rule in rules:
        rid = rule.get('id', 'UNKNOWN')
        ontology = rule.get('ontology')
        if ontology is None:
            (err if require_ontology else warn)(rid, 'Missing ontology block')
            continue
        if not isinstance(ontology, dict):
            err(rid, 'Ontology must be an object/dict'); continue
        unknown = sorted(k for k in ontology if k not in EXPECTED_KEYS and k not in ('category','family','category_code','family_code'))
        if unknown: warn(rid, 'Unknown ontology keys: ' + ', '.join(unknown))
        for key, allowed in canon.items():
            if key not in ontology:
                (err if strict else warn)(rid, f'Missing ontology key: {key}')
                continue
            val = ontology.get(key)
            if not _is_list_of_strings(val):
                err(rid, f"Ontology key '{key}' must be a list of non-empty strings"); continue
            for item in val:
                if allowed and item not in allowed:
                    err(rid, f"Invalid vocab for '{key}': '{item}'")
        if 'lifecycle_stage' in ontology and ontology['lifecycle_stage'] not in registry.get('lifecycle_stages', []):
            err(rid, f"Invalid lifecycle_stage: {ontology['lifecycle_stage']!r}")
        # v0.4.0 metadata lives at rule top level, not ontology, but validate shape here for convenience.
        for key in OBJECT_KEYS:
            if key in rule and not isinstance(rule[key], dict): err(rid, f'{key} must be an object')
        if 'runtime_evidence' in rule and not _is_list_of_strings(rule['runtime_evidence']):
            err(rid, 'runtime_evidence must be a list of non-empty strings')
    return rules, errors, warnings


def main():
    ap = argparse.ArgumentParser(description='Validate ontology vocabularies and v0.4.0 metadata shape.')
    ap.add_argument('--in', dest='in_path', required=True)
    ap.add_argument('--registry', default=str(DEFAULT_REGISTRY))
    ap.add_argument('--require-ontology', action='store_true')
    ap.add_argument('--strict', action='store_true')
    ap.add_argument('--json-report')
    args = ap.parse_args()
    try:
        catalog = load_json(args.in_path); registry = load_json(args.registry)
        rules, errors, warnings = validate(catalog, registry, args.require_ontology, args.strict)
    except Exception as e:
        print('ERROR: {}'.format(e)); return 2
    print('\nEco Rules Ontology Validation')
    print('Input: {}'.format(args.in_path)); print('Rules: {}'.format(len(rules)))
    print('Errors: {}'.format(len(errors))); print('Warnings: {}'.format(len(warnings))); print('')
    if errors:
        print('Errors:'); [print('- {}: {}'.format(e['rule_id'], e['message'])) for e in errors[:200]]; print('')
    if warnings:
        print('Warnings:'); [print('- {}: {}'.format(w['rule_id'], w['message'])) for w in warnings[:200]]; print('')
    if args.json_report:
        _ensure_dir(args.json_report)
        with open(args.json_report,'w',encoding='utf-8') as f:
            json.dump({'generated_at':datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),'input':args.in_path,'rule_count':len(rules),'errors':errors,'warnings':warnings}, f, indent=2)
    return 1 if errors else 0

if __name__ == '__main__':
    raise SystemExit(main())
