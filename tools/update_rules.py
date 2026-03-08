#!/usr/bin/env python3
"""
update_rules.py

Auto-update Eco Rules catalog fields from registry files.

What this script does:
- Loads master.json
- Loads ontology/categories.json
- Loads ontology/families.json
- Normalizes family names using aliases
- Infers family from legacy id if missing
- Backfills category from family if missing
- Backfills category_code from category
- Backfills family_code from family
- Renames id to ECO-<CATEGORY_CODE>-<FAMILY_CODE>-<SEQ>
- Preserves the old id in legacy_id
- Sets canonical_id to the new id
- Optionally fills ontology.system_layers from layer
- Optionally normalizes ontology lists
"""

import argparse
import copy
import json
import os
import re
import sys

LAYER_TO_SYSTEM_LAYER = {
    "code": "Code",
    "runtime": "Runtime",
    "data": "Data",
    "network": "Network",
    "architecture": "Architecture",
    "ai": "AI/ML",
    "ai/ml": "AI/ML",
    "ml": "AI/ML",
    "organizational": "Organizational",
    "org": "Organizational",
}

EXPECTED_ONTOLOGY_KEYS = [
    "resource_impacts",
    "mechanisms",
    "system_layers",
    "detection_methods",
    "remediation_patterns",
]

FAMILY_ALIASES = {
    # names / variants
    "AI": "AI",
    "ML": "AI",
    "Machine Learning": "AI",
    "Network": "Network",
    "Networking": "Network",
    "Data": "Data",
    "Storage": "Storage",
    "Concurrency": "Concurrency",
    "Architecture": "Architecture",
    "Architecture General": "Architecture General",
    "Operations": "Operations",
    "Operations General": "Operations General",
    "Infrastructure": "Infrastructure",
    "Org": "Organizational",
    "Organization": "Organizational",
    "Organizational": "Organizational",

    # code-style values found in rules
    "PY": "Python",
    "JS": "JavaScript",
    "JAVA": "Java",
    "SQL": "SQL",
    "HTTP": "HTTP",
    "NET": "Network",
    "DATA": "Data",
    "STO": "Storage",
    "CON": "Concurrency",
    "ARCH": "Architecture",
    "OPS": "Operations",
    "INF": "Infrastructure",
    "ORG": "Organizational",
    "PROC": "Process",
    "AI": "AI"
}

LEGACY_FAMILY_PREFIX_MAP = {
    "PY": "Python",
    "JS": "JavaScript",
    "JAVA": "Java",
    "SQL": "SQL",
    "HTTP": "HTTP",
    "AI": "AI",
    "NET": "Network",
    "DATA": "Data",
    "STO": "Storage",
    "CON": "Concurrency",
    "ARCH": "Architecture",
    "OPS": "Operations",
    "INF": "Infrastructure",
    "ORG": "Organizational",
    "PROC": "Process",
}


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def dump_json(data):
    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def ensure_parent_dir(path):
    parent = os.path.dirname(os.path.abspath(path))
    if parent and not os.path.isdir(parent):
        os.makedirs(parent)


def build_category_lookup(categories):
    return {c.get("name"): c for c in categories if c.get("name")}


def build_family_lookup(families):
    return {f.get("name"): f for f in families if f.get("name")}


def extract_sequence(rule):
    candidates = [rule.get("legacy_id"), rule.get("id")]
    for value in candidates:
        if not isinstance(value, str):
            continue
        parts = value.split("-")
        if not parts:
            continue
        seq = parts[-1]
        if re.match(r"^\d+$", seq):
            return seq
    return None


def infer_family_from_id(rule_id):
    if not isinstance(rule_id, str):
        return None
    parts = rule_id.split("-")
    if len(parts) < 3:
        return None
    prefix = parts[1]
    return LEGACY_FAMILY_PREFIX_MAP.get(prefix)


def normalize_family_name(family):
    if not isinstance(family, str):
        return family
    return FAMILY_ALIASES.get(family.strip(), family.strip())


def derive_new_id(rule):
    seq = extract_sequence(rule)
    category_code = rule.get("category_code")
    family_code = rule.get("family_code")

    if not seq or not category_code or not family_code:
        return None

    return "ECO-{}-{}-{}".format(category_code, family_code, seq)


def normalize_string_list(values):
    if not isinstance(values, list):
        return values

    out = []
    seen = set()

    for item in values:
        if not isinstance(item, str):
            continue

        value = item.strip()
        if not value:
            continue

        if value not in seen:
            seen.add(value)
            out.append(value)

    out.sort()
    return out


def maybe_fill_system_layer(rule):
    layer = rule.get("layer")
    if not isinstance(layer, str):
        return False

    mapped = LAYER_TO_SYSTEM_LAYER.get(layer.strip().lower())
    if not mapped:
        return False

    ontology = rule.setdefault("ontology", {})
    current = ontology.get("system_layers")

    if not current:
        ontology["system_layers"] = [mapped]
        return True

    if isinstance(current, list) and mapped not in current:
        current.append(mapped)
        ontology["system_layers"] = normalize_string_list(current)
        return True

    return False


def maybe_normalize_ontology(rule):
    ontology = rule.get("ontology")
    if not isinstance(ontology, dict):
        return False

    changed = False

    for key in EXPECTED_ONTOLOGY_KEYS:
        if key in ontology:
            normalized = normalize_string_list(ontology[key])
            if normalized != ontology[key]:
                ontology[key] = normalized
                changed = True

    return changed


def update_rule(rule, category_by_name, family_by_name, fill_system_layer=False, normalize_ontology=False):
    changes = []
    warnings = []
    rule = copy.deepcopy(rule)

    original_id = rule.get("id")
    family = rule.get("family")
    category = rule.get("category")

    # Normalize family name if present
    if family:
        normalized_family = normalize_family_name(family)
        if normalized_family != family:
            rule["family"] = normalized_family
            family = normalized_family
            changes.append("normalized family alias")

    # Infer family from legacy/current id if missing
    if not family:
        inferred_family = infer_family_from_id(rule.get("legacy_id") or rule.get("id"))
        if inferred_family:
            rule["family"] = inferred_family
            family = inferred_family
            changes.append("filled family from legacy id")

    # Backfill category from family registry if missing
    if not category and family in family_by_name:
        inferred_category = family_by_name[family].get("category")
        if inferred_category:
            rule["category"] = inferred_category
            category = inferred_category
            changes.append("filled category from family registry")

    # Fill category_code
    if category and category in category_by_name:
        expected_category_code = category_by_name[category].get("code")
        if expected_category_code and rule.get("category_code") != expected_category_code:
            rule["category_code"] = expected_category_code
            changes.append("set category_code")
    else:
        warnings.append("could not resolve category '{}' in registry".format(category))

    # Fill family_code
    if family and family in family_by_name:
        expected_family_code = family_by_name[family].get("code")
        if expected_family_code and rule.get("family_code") != expected_family_code:
            rule["family_code"] = expected_family_code
            changes.append("set family_code")
    else:
        warnings.append("could not resolve family '{}' in registry".format(family))

    # Derive new primary id
    new_id = derive_new_id(rule)
    if new_id:
        if original_id != new_id:
            if original_id and rule.get("legacy_id") != original_id:
                rule["legacy_id"] = original_id
                changes.append("set legacy_id")

            rule["id"] = new_id
            changes.append("renamed id '{}' -> '{}'".format(original_id, new_id))

        if rule.get("canonical_id") != new_id:
            rule["canonical_id"] = new_id
            changes.append("set canonical_id")
    else:
        warnings.append(
            "could not derive new id (category_code='{}', family_code='{}', sequence='{}')".format(
                rule.get("category_code"),
                rule.get("family_code"),
                extract_sequence(rule),
            )
        )

    if fill_system_layer:
        if maybe_fill_system_layer(rule):
            changes.append("filled ontology.system_layers from layer")

    if normalize_ontology:
        if maybe_normalize_ontology(rule):
            changes.append("normalized ontology lists")

    return rule, changes, warnings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", required=True, help="Path to master.json")
    ap.add_argument("--categories", required=True, help="Path to ontology/categories.json")
    ap.add_argument("--families", required=True, help="Path to ontology/families.json")
    ap.add_argument("--write", action="store_true", help="Write updates back to catalog file")
    ap.add_argument("--out", help="Write updated catalog to a different file")
    ap.add_argument("--fill-system-layer", action="store_true", help="Fill ontology.system_layers from rule.layer")
    ap.add_argument("--normalize-ontology", action="store_true", help="Trim/dedupe/sort ontology lists")
    ap.add_argument("--verbose", action="store_true", help="Print per-rule changes and warnings")
    args = ap.parse_args()

    if args.write and args.out:
        print("ERROR: use either --write or --out, not both")
        return 2

    try:
        catalog = load_json(args.catalog)
        categories = load_json(args.categories)
        families = load_json(args.families)
    except Exception as e:
        print("ERROR: failed to load input files: {}".format(e))
        return 2

    category_by_name = build_category_lookup(categories)
    family_by_name = build_family_lookup(families)

    rules = catalog.get("rules")
    if not isinstance(rules, list):
        print("ERROR: catalog['rules'] must be a list")
        return 2

    updated_rules = []
    total_changed = 0
    total_renamed = 0
    total_warnings = 0

    for rule in rules:
        old_id = rule.get("id", "UNKNOWN")
        updated_rule, changes, warnings = update_rule(
            rule,
            category_by_name=category_by_name,
            family_by_name=family_by_name,
            fill_system_layer=args.fill_system_layer,
            normalize_ontology=args.normalize_ontology,
        )
        updated_rules.append(updated_rule)

        if changes:
            total_changed += 1
        if updated_rule.get("id") != old_id:
            total_renamed += 1
        if warnings:
            total_warnings += 1

        if args.verbose:
            if changes:
                print("{}: {}".format(old_id, "; ".join(changes)))
            if warnings:
                print("{} WARNING: {}".format(old_id, "; ".join(warnings)))

    updated_catalog = copy.deepcopy(catalog)
    updated_catalog["rules"] = updated_rules

    output_text = dump_json(updated_catalog)

    if args.write:
        with open(args.catalog, "w", encoding="utf-8") as f:
            f.write(output_text)
        print("Updated catalog written to {}".format(args.catalog))
    elif args.out:
        ensure_parent_dir(args.out)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(output_text)
        print("Updated catalog written to {}".format(args.out))
    else:
        sys.stdout.write(output_text)

    print("Rules changed: {} of {}".format(total_changed, len(rules)))
    print("Rules renamed: {} of {}".format(total_renamed, len(rules)))
    print("Rules with warnings: {} of {}".format(total_warnings, len(rules)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
