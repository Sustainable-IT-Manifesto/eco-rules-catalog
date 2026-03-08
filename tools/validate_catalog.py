#!/usr/bin/env python3
"""
Cross-registry validator for the Eco Rules Catalog.
"""

import argparse
import json
import re
import sys
from collections import Counter

VALID_SEVERITIES = {
    "note", "info", "warning", "error",
    "low", "medium", "high", "critical"
}

VALID_LAYERS = {
    "Code", "Runtime", "Data", "Network",
    "Architecture", "AI/ML", "Organizational"
}

PRIMARY_ID_RE = re.compile(r"^ECO-[A-Z]{3}-[A-Z0-9]{2,8}-\d{3}$")
LEGACY_ID_RE = re.compile(r"^ECO-[A-Z0-9]+-\d{3}$")


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_category_lookup(categories):
    by_name = {}
    by_code = {}
    for item in categories:
        if item.get("name"):
            by_name[item["name"]] = item
        if item.get("code"):
            by_code[item["code"]] = item
    return by_name, by_code


def build_family_lookup(families):
    by_name = {}
    by_code = {}
    for item in families:
        if item.get("name"):
            by_name[item["name"]] = item
        if item.get("code"):
            by_code[item["code"]] = item
    return by_name, by_code


def extract_sequence(rule):
    for candidate in (rule.get("legacy_id"), rule.get("id")):
        if not isinstance(candidate, str):
            continue
        parts = candidate.split("-")
        if not parts:
            continue
        seq = parts[-1]
        if re.match(r"^\d+$", seq):
            return seq
    return None


def derive_primary_id(rule):
    seq = extract_sequence(rule)
    category_code = rule.get("category_code")
    family_code = rule.get("family_code")
    if not seq or not category_code or not family_code:
        return None
    return "ECO-{}-{}-{}".format(category_code, family_code, seq)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", required=True)
    ap.add_argument("--categories", required=True)
    ap.add_argument("--families", required=True)
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    try:
        catalog = load_json(args.catalog)
        categories = load_json(args.categories)
        families = load_json(args.families)
    except Exception as e:
        print("ERROR: failed to load input files: {}".format(e))
        return 2

    rules = catalog.get("rules")
    if not isinstance(rules, list):
        print("ERROR: catalog['rules'] must be a list")
        return 2

    category_by_name, category_by_code = build_category_lookup(categories)
    family_by_name, family_by_code = build_family_lookup(families)

    errors = []
    warnings = []

    def add_error(rule_id, msg):
        errors.append({"rule_id": rule_id, "message": msg})

    def add_warning(rule_id, msg):
        warnings.append({"rule_id": rule_id, "message": msg})

    # Registry uniqueness
    for name, count in Counter([x.get("name") for x in categories if x.get("name")]).items():
        if count > 1:
            add_error("__registry__", "Duplicate category name: {}".format(name))

    for code, count in Counter([x.get("code") for x in categories if x.get("code")]).items():
        if count > 1:
            add_error("__registry__", "Duplicate category code: {}".format(code))

    for name, count in Counter([x.get("name") for x in families if x.get("name")]).items():
        if count > 1:
            add_error("__registry__", "Duplicate family name: {}".format(name))

    for code, count in Counter([x.get("code") for x in families if x.get("code")]).items():
        if count > 1:
            add_error("__registry__", "Duplicate family code: {}".format(code))

    # Family must point to known category
    for fam in families:
        fam_name = fam.get("name", "UNKNOWN")
        fam_category = fam.get("category")
        if fam_category not in category_by_name:
            add_error("__registry__", "Family '{}' references unknown category '{}'".format(
                fam_name, fam_category
            ))

    # Rule uniqueness
    for rid, count in Counter([r.get("id") for r in rules if r.get("id")]).items():
        if count > 1:
            add_error("__catalog__", "Duplicate rule id: {}".format(rid))

    for cid, count in Counter([r.get("canonical_id") for r in rules if r.get("canonical_id")]).items():
        if count > 1:
            add_error("__catalog__", "Duplicate canonical_id: {}".format(cid))

    # Cross-registry validation
    for rule in rules:
        rid = rule.get("id", "UNKNOWN")

        category = rule.get("category")
        category_code = rule.get("category_code")
        family = rule.get("family")
        family_code = rule.get("family_code")
        canonical_id = rule.get("canonical_id")
        legacy_id = rule.get("legacy_id")

        if not category:
            add_error(rid, "Missing category")
        elif category not in category_by_name:
            add_error(rid, "Unknown category '{}'".format(category))

        if not family:
            add_error(rid, "Missing family")
        elif family not in family_by_name:
            add_error(rid, "Unknown family '{}'".format(family))

        if category in category_by_name:
            expected_category_code = category_by_name[category]["code"]
            if category_code != expected_category_code:
                add_error(rid, "category_code mismatch: expected '{}', found '{}'".format(
                    expected_category_code, category_code
                ))

        if family in family_by_name:
            expected_family_code = family_by_name[family]["code"]
            expected_family_category = family_by_name[family]["category"]

            if family_code != expected_family_code:
                add_error(rid, "family_code mismatch: expected '{}', found '{}'".format(
                    expected_family_code, family_code
                ))

            if category and expected_family_category != category:
                add_error(rid, "Family/category mismatch: family '{}' belongs to '{}', but rule category is '{}'".format(
                    family, expected_family_category, category
                ))

        if not isinstance(rid, str) or not PRIMARY_ID_RE.match(rid):
            add_error(rid, "Primary id must match ECO-<CATEGORY_CODE>-<FAMILY_CODE>-<SEQ>, found '{}'".format(rid))

        if legacy_id is not None:
            if not isinstance(legacy_id, str) or not LEGACY_ID_RE.match(legacy_id):
                add_warning(rid, "legacy_id does not look like a legacy ECO id: '{}'".format(legacy_id))

        expected_primary_id = derive_primary_id(rule)
        if expected_primary_id:
            if rid != expected_primary_id:
                add_error(rid, "id mismatch: expected '{}', found '{}'".format(
                    expected_primary_id, rid
                ))
        else:
            add_warning(rid, "Could not derive expected primary id")

        if canonical_id != rid:
            add_error(rid, "canonical_id mismatch: expected '{}', found '{}'".format(
                rid, canonical_id
            ))

        if args.strict:
            tier = rule.get("tier")
            if not isinstance(tier, int):
                add_error(rid, "tier must be an integer")
            elif tier < 1 or tier > 4:
                add_error(rid, "tier must be between 1 and 4")

            severity = rule.get("severity")
            if severity and severity not in VALID_SEVERITIES:
                add_error(rid, "Unknown severity '{}'".format(severity))

            layer = rule.get("layer")
            if layer and layer not in VALID_LAYERS:
                add_warning(rid, "Layer '{}' is not in canonical layer vocab".format(layer))

    print("")
    print("Eco Rules Catalog Validation")
    print("Catalog: {}".format(args.catalog))
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

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
