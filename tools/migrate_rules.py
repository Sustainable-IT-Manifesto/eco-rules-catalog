#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path
from typing import Any

ID_RE = re.compile(r"^ECO-([A-Z0-9]+)(?:-([A-Z0-9]+))?-([0-9]{3})$")

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "catalog" / "registry.json"

LAYER_MAP = {
    "Code": "application",
    "Runtime": "platform",
    "Data": "data",
    "Network": "network",
    "Architecture": "service",
    "AI/ML": "application",
    "Organizational": "organization",
    "code": "application",
    "runtime": "platform",
    "data": "data",
    "network": "network",
    "architecture": "service",
    "ai/ml": "application",
    "organizational": "organization",
}

SYSTEM_LAYER_MAP = {
    "Code": "application",
    "Runtime": "platform",
    "Data": "data",
    "Network": "network",
    "Architecture": "service",
    "AI/ML": "application",
    "Organizational": "organization",
    "code": "application",
    "runtime": "platform",
    "data": "data",
    "network": "network",
    "architecture": "service",
    "ai/ml": "application",
    "organizational": "organization",
}

RESOURCE_IMPACT_MAP = {
    "CPU": "cpu",
    "Memory": "memory",
    "Network": "network",
    "Storage": "storage",
    "Energy": "energy",
    "Latency": "latency",
    "Infrastructure Cost": "infrastructure_cost",
    "Developer Time": "developer_time",
}

DETECTION_METHOD_MAP = {
    "Static Analysis": "static_analysis",
    "Runtime Profiling": "runtime_profiling",
    "Query Analysis": "query_analysis",
    "Network Trace Analysis": "network_trace_analysis",
    "Log Pattern Detection": "log_pattern_detection",
    "CI Pipeline Inspection": "ci_pipeline_inspection",
}

REMEDIATION_PATTERN_MAP = {
    "Algorithmic Improvement": "algorithmic_improvement",
    "Resource Reuse": "resource_reuse",
    "Caching": "caching",
    "Batching": "batching",
    "Event-Driven Design": "event_driven_design",
    "Data Reduction": "data_reduction",
    "Infrastructure Right-Sizing": "infrastructure_right_sizing",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def save_json(path: Path, payload: Any) -> None:
    with path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2)
        fh.write("\n")


def normalize_text(value: str | None) -> str | None:
    if value is None:
        return None
    return value.strip().lower()


class Registry:
    def __init__(self, data: dict[str, Any]):
        self.categories_by_code = data["categories"]
        self.families_by_code = data["families"]
        self.category_name_to_code = {}
        self.family_name_to_code = {}
        for code, item in self.categories_by_code.items():
            self.category_name_to_code[normalize_text(item["name"])] = code
            for alias in item.get("aliases", []):
                self.category_name_to_code[normalize_text(alias)] = code
        for code, item in self.families_by_code.items():
            self.family_name_to_code[normalize_text(item["name"])] = code
            for alias in item.get("aliases", []):
                self.family_name_to_code[normalize_text(alias)] = code

    def resolve_category_code(self, raw: str | None) -> str | None:
        if raw is None:
            return None
        if raw in self.categories_by_code:
            return raw
        return self.category_name_to_code.get(normalize_text(raw))

    def resolve_family_code(self, raw: str | None) -> str | None:
        if raw is None:
            return None
        if raw in self.families_by_code:
            return raw
        return self.family_name_to_code.get(normalize_text(raw))


def infer_sequence(rule: dict[str, Any]) -> int:
    if isinstance(rule.get("sequence"), int):
        return rule["sequence"]
    for key in ("canonical_id", "id", "legacy_id"):
        value = rule.get(key)
        if isinstance(value, str):
            m = ID_RE.match(value)
            if m:
                return int(m.group(3))
    raise ValueError(f"Unable to infer sequence for rule {rule.get('id')}")


def migrate_rule(rule: dict[str, Any], registry: Registry) -> dict[str, Any]:
    out = dict(rule)
    ontology = dict(rule.get("ontology", {}))
    sequence = infer_sequence(rule)

    category_code = registry.resolve_category_code(rule.get("category_code") or ontology.get("category_code") or rule.get("category"))
    family_code = registry.resolve_family_code(rule.get("family_code") or ontology.get("family_code") or rule.get("family"))

    if category_code is None:
        raise ValueError(f"Could not resolve category for {rule.get('id')}")
    if family_code is None:
        raise ValueError(f"Could not resolve family for {rule.get('id')}")

    expected_category = registry.families_by_code[family_code]["category_code"]
    if expected_category != category_code:
        raise ValueError(
            f"Family {family_code} belongs to category {expected_category}, not {category_code} for {rule.get('id')}"
        )

    canonical_id = f"ECO-{category_code}-{family_code}-{sequence:03d}"

    out["sequence"] = sequence
    out["category_code"] = category_code
    out["family_code"] = family_code
    out["category"] = registry.categories_by_code[category_code]["name"]
    out["family"] = registry.families_by_code[family_code]["name"]
    out["legacy_id"] = rule.get("legacy_id") or (rule.get("id") if rule.get("id") != canonical_id else None)
    out["id"] = canonical_id
    out["canonical_id"] = canonical_id

    old_layer = rule.get("layer")
    out["layer"] = LAYER_MAP.get(old_layer, normalize_text(old_layer) or "application")

    old_status = dict(rule.get("metadata", {})).get("status", "active")
    metadata = dict(rule.get("metadata", {}))
    metadata.setdefault("status", old_status)
    metadata.setdefault("version", "0.2.0")
    out["metadata"] = metadata

    ontology["category_code"] = category_code
    ontology["family_code"] = family_code
    ontology["system_layers"] = [SYSTEM_LAYER_MAP.get(x, normalize_text(x) or "application") for x in ontology.get("system_layers", [old_layer] if old_layer else ["application"])]
    if "resource_impacts" in ontology:
        ontology["resource_impacts"] = [RESOURCE_IMPACT_MAP.get(x, normalize_text(x)) for x in ontology["resource_impacts"]]
    if "detection_methods" in ontology:
        ontology["detection_methods"] = [DETECTION_METHOD_MAP.get(x, normalize_text(x)) for x in ontology["detection_methods"]]
    if "remediation_patterns" in ontology:
        ontology["remediation_patterns"] = [REMEDIATION_PATTERN_MAP.get(x, normalize_text(x)) for x in ontology["remediation_patterns"]]
    out["ontology"] = ontology

    remediation = dict(rule.get("remediation", {}))
    remediation.setdefault("examples", [])
    remediation.setdefault("guidance", remediation.get("guidance", ""))
    out["remediation"] = remediation

    return out


def iter_rules(payload: Any) -> tuple[list[dict[str, Any]], str]:
    if isinstance(payload, list):
        return payload, "list"
    if isinstance(payload, dict) and isinstance(payload.get("rules"), list):
        return payload["rules"], "wrapped"
    raise ValueError("Unsupported catalog shape. Expected list or {'rules': [...]}.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to current master.json")
    parser.add_argument("output", help="Path to write migrated master.json")
    parser.add_argument("--report", help="Optional path to write migration report JSON")
    args = parser.parse_args()

    registry = Registry(load_json(REGISTRY_PATH))
    payload = load_json(Path(args.input))
    rules, shape = iter_rules(payload)

    migrated = []
    report = {"migrated": 0, "errors": []}
    for rule in rules:
        try:
            migrated.append(migrate_rule(rule, registry))
            report["migrated"] += 1
        except Exception as exc:
            report["errors"].append({"rule_id": rule.get("id"), "error": str(exc)})

    if shape == "wrapped":
        payload["rules"] = migrated
        save_json(Path(args.output), payload)
    else:
        save_json(Path(args.output), migrated)

    if args.report:
        save_json(Path(args.report), report)

    print(f"Migrated {report['migrated']} rule(s)")
    if report["errors"]:
        print(f"Encountered {len(report['errors'])} error(s)")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
