#!/usr/bin/env python3
import argparse, json, os
from collections import Counter

CANON_KEYS = ["resource_impacts","mechanisms","system_layers","detection_methods","remediation_patterns"]

def ensure_dir(path):
    d = os.path.dirname(os.path.abspath(path))
    if d and not os.path.isdir(d):
        os.makedirs(d)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_path", required=True)
    ap.add_argument("--out", dest="out_path", required=True)
    args = ap.parse_args()

    with open(args.in_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    rules = catalog.get("rules", [])
    items = []
    facets = {k: Counter() for k in (["category","family","layer","tier","severity"] + CANON_KEYS)}

    for r in rules:
        entry = {
            "id": r.get("id",""),
            "canonical_id": r.get("canonical_id",""),
            "title": r.get("title",""),
            "summary": r.get("summary",""),
            "category": r.get("category","Uncategorized"),
            "family": r.get("family","Uncategorized"),
            "layer": r.get("layer","Uncategorized"),
            "tier": r.get("tier",None),
            "severity": r.get("severity",""),
            "ontology": {k: (r.get("ontology",{}).get(k,[]) if isinstance(r.get("ontology",{}).get(k,[]), list) else []) for k in CANON_KEYS}
        }
        items.append(entry)
        facets["category"][entry["category"]] += 1
        facets["family"][entry["family"]] += 1
        facets["layer"][entry["layer"]] += 1
        if entry["tier"] is not None:
            facets["tier"][str(entry["tier"])] += 1
        if entry["severity"]:
            facets["severity"][entry["severity"]] += 1
        for k in CANON_KEYS:
            for v in entry["ontology"][k]:
                facets[k][v] += 1

    payload = {
        "catalog_version": catalog.get("catalog_version",""),
        "rule_count": len(items),
        "rules": items,
        "facets": {k: dict(v.most_common()) for k, v in facets.items()}
    }
    ensure_dir(args.out_path)
    with open(args.out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2, sort_keys=True)

if __name__ == "__main__":
    main()
