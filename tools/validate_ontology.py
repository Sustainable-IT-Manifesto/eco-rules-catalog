#!/usr/bin/env python3
"""
validate_ontology.py

Validate Eco Rules "ontology" blocks in master.json against canonical vocab.

Python: 3.6+

Usage:
  python tools/validate_ontology.py --in master.json
  python tools/validate_ontology.py --in master.json --require-ontology
  python tools/validate_ontology.py --in master.json --strict
  python tools/validate_ontology.py --in master.json --json-report build/ontology_report.json

Exit codes:
  0 = OK (no errors; warnings allowed)
  1 = Errors found
  2 = Invalid input / runtime error
"""

import argparse
import json
import os
import sys
from datetime import datetime

CANON = {
    "resource_impacts": {
        "CPU",
        "Memory",
        "Network",
        "Storage",
        "Energy",
        "Latency",
        "Infrastructure Cost",
        "Developer Time",
    },
    "mechanisms": {
        "Redundant Computation",
        "Excessive Allocation",
        "Inefficient Data Structures",
        "Serialization Overhead",
        "Network Amplification",
        "Polling",
        "Cache Misuse",
        "Unbounded Growth",
        "Resource Contention",
        "Over-Provisioning",
    },
    "system_layers": {
        "Code",
        "Runtime",
        "Data",
        "Network",
        "Architecture",
        "AI/ML",
        "Organizational",
    },
    "detection_methods": {
        "Static Analysis",
        "Runtime Profiling",
        "Query Analysis",
        "Network Trace Analysis",
        "Log Pattern Detection",
        "CI Pipeline Inspection",
    },
    "remediation_patterns": {
        "Algorithmic Improvement",
        "Resource Reuse",
        "Caching",
        "Batching",
        "Event-Driven Design",
        "Data Reduction",
        "Infrastructure Right-Sizing",
    },
}

EXPECTED_KEYS = [
    "resource_impacts",
    "mechanisms",
    "system_layers",
    "detection_methods",
    "remediation_patterns",
]


def _load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _is_list_of_strings(x):
    if not isinstance(x, list):
        return False
    for item in x:
        if not isinstance(item, str):
            return False
        if item.strip() == "":
            return False
    return True


def _ensure_dir(path):
    d = os.path.dirname(os.path.abspath(path))
    if d and not os.path.isdir(d):
        os.makedirs(d)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_path", required=True, help="Path to master.json")
    ap.add_argument("--require-ontology", action="store_true",
                    help="Treat missing ontology blocks as errors")
    ap.add_argument("--strict", action="store_true",
                    help="Treat warnings as errors (e.g., empty lists, missing keys)")
    ap.add_argument("--json-report", dest="json_report", default=None,
                    help="Optional path to write JSON report")
    args = ap.parse_args()

    try:
        catalog = _load_json(args.in_path)
    except Exception as e:
        print("ERROR: failed to read JSON: {}".format(e))
        return 2

    rules = catalog.get("rules", [])
    if not isinstance(rules, list):
        print("ERROR: catalog['rules'] must be a list")
        return 2

    errors = []
    warnings = []

    def add_error(rule_id, msg):
        errors.append({"rule_id": rule_id, "message": msg})

    def add_warning(rule_id, msg):
        warnings.append({"rule_id": rule_id, "message": msg})

    for rule in rules:
        rule_id = rule.get("id", "UNKNOWN")

        ontology = rule.get("ontology", None)
        if ontology is None:
            if args.require_ontology:
                add_error(rule_id, "Missing ontology block")
            else:
                add_warning(rule_id, "Missing ontology block")
            continue

        if not isinstance(ontology, dict):
            add_error(rule_id, "Ontology must be an object/dict")
            continue

        # Unknown keys
        unknown_keys = sorted([k for k in ontology.keys() if k not in EXPECTED_KEYS])
        if unknown_keys:
            add_warning(rule_id, "Unknown ontology keys: {}".format(", ".join(unknown_keys)))

        # Missing expected keys
        missing_keys = [k for k in EXPECTED_KEYS if k not in ontology]
        if missing_keys:
            msg = "Missing ontology keys: {}".format(", ".join(missing_keys))
            if args.strict:
                add_error(rule_id, msg)
            else:
                add_warning(rule_id, msg)

        # Validate each expected key
        for key in EXPECTED_KEYS:
            if key not in ontology:
                continue

            val = ontology.get(key)

            if val is None:
                msg = "Ontology key '{}' is null".format(key)
                if args.strict:
                    add_error(rule_id, msg)
                else:
                    add_warning(rule_id, msg)
                continue

            if not _is_list_of_strings(val):
                add_error(rule_id, "Ontology key '{}' must be a list of non-empty strings".format(key))
                continue

            if len(val) == 0:
                msg = "Ontology key '{}' is an empty list".format(key)
                if args.strict:
                    add_error(rule_id, msg)
                else:
                    add_warning(rule_id, msg)
                continue

            allowed = CANON.get(key, set())
            for item in val:
                if item not in allowed:
                    add_error(
                        rule_id,
                        "Invalid vocab for '{}': '{}' (allowed: {})".format(
                            key, item, "; ".join(sorted(list(allowed)))
                        ),
                    )

    # Summarize
    print("")
    print("Eco Rules Ontology Validation")
    print("Input: {}".format(args.in_path))
    print("Rules: {}".format(len(rules)))
    print("Errors: {}".format(len(errors)))
    print("Warnings: {}".format(len(warnings)))
    print("")

    # Print up to a reasonable number (avoid spam)
    max_list = 200

    if errors:
        print("Errors:")
        for e in errors[:max_list]:
            print("- {}: {}".format(e["rule_id"], e["message"]))
        if len(errors) > max_list:
            print("  ...and {} more".format(len(errors) - max_list))
        print("")

    if warnings:
        print("Warnings:")
        for w in warnings[:max_list]:
            print("- {}: {}".format(w["rule_id"], w["message"]))
        if len(warnings) > max_list:
            print("  ...and {} more".format(len(warnings) - max_list))
        print("")

    # JSON report
    if args.json_report:
        report = {
            "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "input": args.in_path,
            "rule_count": len(rules),
            "errors": errors,
            "warnings": warnings,
            "strict": bool(args.strict),
            "require_ontology": bool(args.require_ontology),
        }
        _ensure_dir(args.json_report)
        with open(args.json_report, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2, sort_keys=True)
        print("Wrote JSON report: {}".format(args.json_report))
        print("")

    # Exit codes
    if errors:
        return 1
    if args.strict and warnings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
