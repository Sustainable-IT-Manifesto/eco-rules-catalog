#!/usr/bin/env python3
import argparse, json, sys
from copy import deepcopy
from pathlib import Path

EXPECTED_KEYS = ['resource_impacts','mechanisms','system_layers','detection_methods','remediation_patterns']
LAYER_TO_SYSTEM_LAYER = {'code':'code','runtime':'platform','platform':'platform','data':'data','network':'network','architecture':'architecture','ai':'ai','ai/ml':'ai','ml':'ai','organizational':'organization','org':'organization','process':'process','service':'service','application':'application','infrastructure':'infrastructure'}
ALIASES = {'CPU':'cpu','Memory':'memory','Network':'network','Storage':'storage','Energy':'energy','Latency':'latency','Infrastructure Cost':'infrastructure_cost','Developer Time':'developer_time','Static Analysis':'static_analysis','Runtime Profiling':'runtime_profiling','Query Analysis':'query_analysis','Network Trace Analysis':'network_trace_analysis','Log Pattern Detection':'log_pattern_detection','CI Pipeline Inspection':'ci_pipeline_inspection','Infrastructure Right-Sizing':'infrastructure_right_sizing','Event-Driven Design':'event_driven_design'}
LEVELS = {'none','low','medium','high','critical'}


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f: return json.load(f)

def dump_json(obj): return json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + '\n'

def norm_value(x, aliases=True):
    if not isinstance(x, str): return x
    v = x.strip()
    return ALIASES.get(v, v.strip().lower().replace(' ', '_')) if aliases else v

def norm_list(lst, aliases=True):
    out, seen = [], set()
    for x in lst or []:
        if not isinstance(x, str): continue
        v = norm_value(x, aliases)
        if v and v not in seen:
            seen.add(v); out.append(v)
    return sorted(out)

def normalize_level_map(obj):
    if not isinstance(obj, dict): return obj
    out = {}
    for k, v in obj.items():
        if isinstance(v, str):
            lv = v.strip().lower()
            out[k] = lv if lv in LEVELS else v
        else:
            out[k] = v
    return out

def normalize(catalog, create_missing=False, apply_aliases=True, fill_system_layer=False, create_missing_keys=False):
    rules = catalog.get('rules', [])
    if not isinstance(rules, list): raise ValueError("catalog['rules'] must be a list")
    changed, issues = False, []
    for rule in rules:
        ontology = rule.get('ontology')
        if ontology is None:
            if create_missing:
                rule['ontology'] = {}; ontology = rule['ontology']; changed = True
            else: continue
        if not isinstance(ontology, dict):
            issues.append(f"{rule.get('id','UNKNOWN')}: ontology not an object"); continue
        if fill_system_layer and isinstance(rule.get('layer'), str):
            mapped = LAYER_TO_SYSTEM_LAYER.get(rule['layer'].strip().lower(), rule['layer'].strip().lower())
            if not ontology.get('system_layers'):
                ontology['system_layers'] = [mapped]; changed = True
        if create_missing_keys:
            for k in EXPECTED_KEYS:
                if k not in ontology: ontology[k] = []; changed = True
        for k in EXPECTED_KEYS:
            if k in ontology and isinstance(ontology[k], list):
                before = list(ontology[k]); ontology[k] = norm_list(ontology[k], apply_aliases)
                changed = changed or before != ontology[k]
        # v0.4.0 structured metadata: preserve object shape, normalize only known level maps.
        if 'cost_dimensions' in rule:
            before = deepcopy(rule['cost_dimensions']); rule['cost_dimensions'] = normalize_level_map(rule['cost_dimensions'])
            changed = changed or before != rule['cost_dimensions']
        if 'runtime_evidence' in rule and isinstance(rule['runtime_evidence'], list):
            before = list(rule['runtime_evidence']); rule['runtime_evidence'] = norm_list(rule['runtime_evidence'], False)
            changed = changed or before != rule['runtime_evidence']
    return catalog, changed, issues

def main():
    ap=argparse.ArgumentParser(description='Normalize ontology arrays while preserving v0.4.0 structured metadata.')
    ap.add_argument('--in', dest='in_path', required=True); ap.add_argument('--write', action='store_true'); ap.add_argument('--check', action='store_true')
    ap.add_argument('--no-aliases', action='store_true'); ap.add_argument('--create-missing', action='store_true'); ap.add_argument('--create-missing-keys', action='store_true'); ap.add_argument('--fill-system-layer', action='store_true')
    args=ap.parse_args()
    if args.write and args.check: print('ERROR: --write and --check are mutually exclusive'); return 2
    original=load_json(args.in_path)
    normalized, changed, issues = normalize(deepcopy(original), args.create_missing, not args.no_aliases, args.fill_system_layer, args.create_missing_keys)
    if issues:
        print('Notes:'); [print('- '+i) for i in issues]
    if args.check:
        if dump_json(original) != dump_json(normalized): print('Normalization would make changes.'); return 1
        print('OK: No normalization changes needed.'); return 0
    if args.write:
        Path(args.in_path).write_text(dump_json(normalized), encoding='utf-8') if changed else None
        print('Wrote normalized catalog to {}'.format(args.in_path) if changed else 'No changes needed.')
    else: sys.stdout.write(dump_json(normalized))
    return 0
if __name__ == '__main__': raise SystemExit(main())
