#!/usr/bin/env python3
"""
normalize_ontology.py

Normalize Eco Rules "ontology" blocks in master.json:
- strip whitespace
- dedupe
- sort for stable diffs
- optional alias normalization
- optional auto-fill system_layers from existing "layer" field
- optional auto-create missing ontology keys

Python: 3.6+

Usage:
  # Write changes in-place
  python tools/normalize_ontology.py --in master.json --write

  # Print normalized JSON to stdout
  python tools/normalize_ontology.py --in master.json

  # Fail if changes would be made (CI)
  python tools/normalize_ontology.py --in master.json --check

  # Auto-create missing ontology blocks + keys
  python tools/normalize_ontology.py --in master.json --write --create-missing

  # Fill ontology.system_layers from rule.layer
  python tools/normalize_ontology.py --in master.json --write --fill-system-layer

Exit codes:
  0 = OK (no changes in --check, or successful write)
  1 = Changes would be made (only in --check)
  2 = Invalid input / runtime error
"""

import argparse
import json
import sys
from copy import deepcopy

EXPECTED_KEYS = [
    "resource_impacts",
    "mechanisms",
    "system_layers",
    "detection_methods",
    "remediation_patterns",
]

# Canonical vocab values (for alias mapping only; validator enforces exact membership)
ALIAS_MAP = {
    # Resource impacts
    "InfraCost": "Infrastructure Cost",
    "InfrastructureCost": "Infrastructure Cost",
    "Cost": "Infrastructure Cost",
    "DevTime": "Developer Time",
    "DeveloperTime": "Developer Time",
    "Dev Time": "Developer Time",

    # Layers
    "AI": "AI/ML",
    "ML": "AI/ML",
    "Org": "Organizational",

    # Detection
    "Profiling": "Runtime Profiling",
    "Static": "Static Analysis",
    "Logs": "Log Pattern Detection",
    "CI": "CI Pipeline Inspection",

    # Remediation
    "Right Sizing": "Infrastructure Right-Sizing",
    "Rightsizing": "Infrastructure Right-Sizing",
    "Event Driven Design": "Event-Driven Design",
}

# Map existing rule.layer strings into canonical SystemLayer values
LAYER_TO_SYSTEM_LAYER = {
    "code": "Code",
    "runtime": "Runtime",
    "data": "Data",
    "network": "Network",
    "architecture": "Architecture",
    "ai": "AI/ML",
    "ml": "AI/ML",
    "ai/ml": "AI/ML",
    "organizational": "Organizational",
    "org": "Organizational",
}

def _load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def _dump_json(obj):
    # Stable formatting for git
    return json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n"

def _norm_item(s, apply_aliases):
    if not isinstance(s, str):
        return s
    v = s.strip()
    if apply_aliases and v in ALIAS_MAP:
        v = ALIAS_MAP[v]
    return v

def _norm_list(lst, apply_aliases):
    # Strip, alias, dedupe, sort
    out = []
    seen = set()
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

def _ensure_ontology(rule, create_missing):
    if "ontology" not in rule or rule["ontology"] is None:
        if create_missing:
            rule["ontology"] = {}
        else:
            return None
    if not isinstance(rule["ontology"], dict):
        # Don't try to fix non-dicts silently
        return None
    return rule["ontology"]

def _fill_system_layer(rule, ontology):
    # Derive from rule.layer if missing/empty
    raw_layer = rule.get("layer")
    if not raw_layer or not isinstance(raw_layer, str):
        return
    key = raw_layer.strip().lower()
    mapped = LAYER_TO_SYSTEM_LAYER.get(key)
    if not mapped:
        return
    cur = ontology.get("system_layers")
    if not cur or not isinstance(cur, list) or len(cur) == 0:
        ontology["system_layers"] = [mapped]

def normalize(catalog, create_missing=False, apply_aliases=True, fill_system_layer=False, create_missing_keys=False):
    rules = catalog.get("rules", [])
    if not isinstance(rules, list):
        raise ValueError("catalog['rules'] must be a list")

    changed = False
    issues = []

    for rule in rules:
        rid = rule.get("id", "UNKNOWN")

        ontology = _ensure_ontology(rule, create_missing=create_missing)
        if ontology is None:
            # can't normalize (missing or wrong type); leave to validator
            continue

        if fill_system_layer:
            before = deepcopy(ontology.get("system_layers"))
            _fill_system_layer(rule, ontology)
            after = ontology.get("system_layers")
            if before != after:
                changed = True

        # Create missing keys as empty lists (optional)
        if create_missing_keys:
            for k in EXPECTED_KEYS:
                if k not in ontology:
                    ontology[k] = []
                    changed = True

        # Normalize each expected list key if present
        for k in EXPECTED_KEYS:
            if k not in ontology:
                continue
            v = ontology.get(k)
            if v is None:
                # leave None as-is unless create_missing_keys forced list
                continue
            if isinstance(v, list):
                before = list(v)
                ontology[k] = _norm_list(v, apply_aliases=apply_aliases)
                if before != ontology[k]:
                    changed = True
            else:
                # Wrong type; track but don't rewrite (validator should fail)
                issues.append("{}: ontology.{} not a list".format(rid, k))

    return catalog, changed, issues

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_path", required=True, help="Path to master.json")
    ap.add_argument("--write", action="store_true", help="Write normalized JSON back to file")
    ap.add_argument("--check", action="store_true", help="Fail if normalization would change the file")
    ap.add_argument("--no-aliases", action="store_true", help="Disable alias normalization")
    ap.add_argument("--create-missing", action="store_true", help="Create missing ontology blocks as empty dicts")
    ap.add_argument("--create-missing-keys", action="store_true", help="Create missing ontology keys as empty lists")
    ap.add_argument("--fill-system-layer", action="store_true", help="Populate ontology.system_layers from rule.layer when missing/empty")
    args = ap.parse_args()

    if args.write and args.check:
        print("ERROR: --write and --check are mutually exclusive")
        return 2

    try:
        original = _load_json(args.in_path)
    except Exception as e:
        print("ERROR: failed to read JSON: {}".format(e))
        return 2

    original_text = _dump_json(original)

    try:
        normalized_obj, changed, issues = normalize(
            deepcopy(original),
            create_missing=args.create_missing,
            apply_aliases=(not args.no_aliases),
            fill_system_layer=args.fill_system_layer,
            create_missing_keys=args.create_missing_keys,
        )
    except Exception as e:
        print("ERROR: normalization failed: {}".format(e))
        return 2

    normalized_text = _dump_json(normalized_obj)

    if issues:
        print("Notes:")
        for i in issues[:200]:
            print("- {}".format(i))
        if len(issues) > 200:
            print("  ...and {} more".format(len(issues) - 200))
        print("")

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

    # default: print to stdout
    sys.stdout.write(normalized_text)
    return 0

if __name__ == "__main__":
    sys.exit(main())
