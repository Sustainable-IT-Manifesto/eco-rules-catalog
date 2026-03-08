#!/usr/bin/env python3
import argparse, json, os, sys
from datetime import datetime

CANON = {
    "resource_impacts": {"CPU","Memory","Network","Storage","Energy","Latency","Infrastructure Cost","Developer Time"},
    "mechanisms": {"Redundant Computation","Excessive Allocation","Inefficient Data Structures","Serialization Overhead","Network Amplification","Polling","Cache Misuse","Unbounded Growth","Resource Contention","Over-Provisioning"},
    "system_layers": {"Code","Runtime","Data","Network","Architecture","AI/ML","Organizational"},
    "detection_methods": {"Static Analysis","Runtime Profiling","Query Analysis","Network Trace Analysis","Log Pattern Detection","CI Pipeline Inspection"},
    "remediation_patterns": {"Algorithmic Improvement","Resource Reuse","Caching","Batching","Event-Driven Design","Data Reduction","Infrastructure Right-Sizing"},
}
EXPECTED_KEYS = ["resource_impacts","mechanisms","system_layers","detection_methods","remediation_patterns"]

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def _is_list_of_strings(x):
    return isinstance(x, list) and all(isinstance(i, str) and i.strip() for i in x)

def _ensure_dir(path):
    d = os.path.dirname(os.path.abspath(path))
    if d and not os.path.isdir(d):
        os.makedirs(d)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_path", required=True)
    ap.add_argument("--require-ontology", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--json-report", dest="json_report")
    args = ap.parse_args()

    try:
        catalog = load_json(args.in_path)
    except Exception as e:
        print("ERROR: failed to read JSON: {}".format(e))
        return 2

    rules = catalog.get("rules", [])
    if not isinstance(rules, list):
        print("ERROR: catalog['rules'] must be a list")
        return 2

    errors, warnings = [], []
    def add_error(rule_id, msg): errors.append({"rule_id":rule_id,"message":msg})
    def add_warning(rule_id, msg): warnings.append({"rule_id":rule_id,"message":msg})

    for rule in rules:
        rid = rule.get("id", "UNKNOWN")
        ontology = rule.get("ontology")
        if ontology is None:
            if args.require_ontology: add_error(rid, "Missing ontology block")
            else: add_warning(rid, "Missing ontology block")
            continue
        if not isinstance(ontology, dict):
            add_error(rid, "Ontology must be an object/dict")
            continue
        unknown = sorted([k for k in ontology.keys() if k not in EXPECTED_KEYS])
        if unknown:
            add_warning(rid, "Unknown ontology keys: {}".format(", ".join(unknown)))
        missing = [k for k in EXPECTED_KEYS if k not in ontology]
        if missing:
            msg = "Missing ontology keys: {}".format(", ".join(missing))
            if args.strict: add_error(rid, msg)
            else: add_warning(rid, msg)
        for key in EXPECTED_KEYS:
            if key not in ontology:
                continue
            val = ontology.get(key)
            if val is None:
                if args.strict: add_error(rid, "Ontology key '{}' is null".format(key))
                else: add_warning(rid, "Ontology key '{}' is null".format(key))
                continue
            if not _is_list_of_strings(val):
                add_error(rid, "Ontology key '{}' must be a list of non-empty strings".format(key))
                continue
            if len(val) == 0:
                if args.strict: add_error(rid, "Ontology key '{}' is an empty list".format(key))
                else: add_warning(rid, "Ontology key '{}' is an empty list".format(key))
                continue
            allowed = CANON.get(key, set())
            for item in val:
                if item not in allowed:
                    add_error(rid, "Invalid vocab for '{}': '{}'".format(key, item))

    print("\nEco Rules Ontology Validation")
    print("Input: {}".format(args.in_path))
    print("Rules: {}".format(len(rules)))
    print("Errors: {}".format(len(errors)))
    print("Warnings: {}".format(len(warnings)))
    print("")
    if errors:
        print("Errors:")
        for e in errors[:200]:
            print("- {}: {}".format(e["rule_id"], e["message"]))
        print("")
    if warnings:
        print("Warnings:")
        for w in warnings[:200]:
            print("- {}: {}".format(w["rule_id"], w["message"]))
        print("")
    if args.json_report:
        report = {"generated_at":datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),"input":args.in_path,"rule_count":len(rules),"errors":errors,"warnings":warnings,"strict":bool(args.strict),"require_ontology":bool(args.require_ontology)}
        _ensure_dir(args.json_report)
        with open(args.json_report, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2, sort_keys=True)
    if errors:
        return 1
    if args.strict and warnings:
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
