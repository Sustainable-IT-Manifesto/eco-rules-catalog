#!/usr/bin/env python3
import argparse, json, sys
from copy import deepcopy

EXPECTED_KEYS = ["resource_impacts","mechanisms","system_layers","detection_methods","remediation_patterns"]
ALIAS_MAP = {
    "InfraCost": "Infrastructure Cost",
    "InfrastructureCost": "Infrastructure Cost",
    "Cost": "Infrastructure Cost",
    "DevTime": "Developer Time",
    "DeveloperTime": "Developer Time",
    "Dev Time": "Developer Time",
    "AI": "AI/ML",
    "ML": "AI/ML",
    "Org": "Organizational",
    "Profiling": "Runtime Profiling",
    "Static": "Static Analysis",
    "Logs": "Log Pattern Detection",
    "CI": "CI Pipeline Inspection",
    "Right Sizing": "Infrastructure Right-Sizing",
    "Rightsizing": "Infrastructure Right-Sizing",
    "Event Driven Design": "Event-Driven Design",
}
LAYER_TO_SYSTEM_LAYER = {
    "code":"Code","runtime":"Runtime","data":"Data","network":"Network",
    "architecture":"Architecture","ai":"AI/ML","ai/ml":"AI/ML","ml":"AI/ML",
    "organizational":"Organizational","org":"Organizational"
}

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def dump_json(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n"

def _norm_item(s, apply_aliases):
    if not isinstance(s, str):
        return s
    v = s.strip()
    if apply_aliases and v in ALIAS_MAP:
        v = ALIAS_MAP[v]
    return v

def _norm_list(lst, apply_aliases):
    out, seen = [], set()
    for x in lst:
        if not isinstance(x, str):
            continue
        v = _norm_item(x, apply_aliases)
        if not v:
            continue
        if v not in seen:
            seen.add(v)
            out.append(v)
    out.sort()
    return out

def normalize(catalog, create_missing=False, apply_aliases=True, fill_system_layer=False, create_missing_keys=False):
    rules = catalog.get("rules", [])
    if not isinstance(rules, list):
        raise ValueError("catalog['rules'] must be a list")
    changed = False
    issues = []
    for rule in rules:
        ontology = rule.get("ontology")
        if ontology is None:
            if create_missing:
                rule["ontology"] = {}
                ontology = rule["ontology"]
                changed = True
            else:
                continue
        if not isinstance(ontology, dict):
            issues.append("{}: ontology not an object".format(rule.get("id","UNKNOWN")))
            continue
        if fill_system_layer:
            raw_layer = rule.get("layer")
            if isinstance(raw_layer, str):
                mapped = LAYER_TO_SYSTEM_LAYER.get(raw_layer.strip().lower())
                if mapped:
                    cur = ontology.get("system_layers")
                    if not cur or not isinstance(cur, list) or len(cur) == 0:
                        ontology["system_layers"] = [mapped]
                        changed = True
        if create_missing_keys:
            for k in EXPECTED_KEYS:
                if k not in ontology:
                    ontology[k] = []
                    changed = True
        for k in EXPECTED_KEYS:
            if k in ontology and isinstance(ontology.get(k), list):
                before = list(ontology[k])
                ontology[k] = _norm_list(ontology[k], apply_aliases)
                if before != ontology[k]:
                    changed = True
    return catalog, changed, issues

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_path", required=True)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--no-aliases", action="store_true")
    ap.add_argument("--create-missing", action="store_true")
    ap.add_argument("--create-missing-keys", action="store_true")
    ap.add_argument("--fill-system-layer", action="store_true")
    args = ap.parse_args()
    if args.write and args.check:
        print("ERROR: --write and --check are mutually exclusive")
        return 2
    try:
        original = load_json(args.in_path)
        normalized_obj, changed, issues = normalize(
            deepcopy(original),
            create_missing=args.create_missing,
            apply_aliases=(not args.no_aliases),
            fill_system_layer=args.fill_system_layer,
            create_missing_keys=args.create_missing_keys,
        )
        original_text = dump_json(original)
        normalized_text = dump_json(normalized_obj)
        if issues:
            print("Notes:")
            for i in issues:
                print("- {}".format(i))
        if args.check:
            if original_text != normalized_text:
                print("Normalization would make changes.")
                return 1
            print("OK: No normalization changes needed.")
            return 0
        if args.write:
            if original_text != normalized_text:
                with open(args.in_path, "w", encoding="utf-8") as f:
                    f.write(normalized_text)
                print("Wrote normalized catalog to {}".format(args.in_path))
            else:
                print("No changes needed.")
            return 0
        sys.stdout.write(normalized_text)
        return 0
    except Exception as e:
        print("ERROR: {}".format(e))
        return 2

if __name__ == "__main__":
    sys.exit(main())
