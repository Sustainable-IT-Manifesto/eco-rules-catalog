from __future__ import annotations

import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "catalog" / "master.json"
OUT_DIR = ROOT / "docs" / "catalog"

LAYER_ORDER = ["ai", "architecture", "code", "data", "network", "process"]

LAYER_LABELS = {
    "ai": "AI",
    "architecture": "Architecture",
    "code": "Code",
    "data": "Data",
    "network": "Network",
    "process": "Process",
}


def load_catalog() -> dict:
    with MASTER.open("r", encoding="utf-8") as f:
        return json.load(f)


def get_rules(catalog: dict) -> list[dict]:
    rules = catalog.get("rules", [])
    return sorted(rules, key=lambda r: r.get("id", ""))


def ensure_out_dir() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "layers").mkdir(parents=True, exist_ok=True)


def category_name(rule: dict) -> str:
    category_code = rule.get("category_code", "")
    ontology = rule.get("ontology", {})
    category = ontology.get("category")
    if category:
        return str(category)
    return str(category_code)


def family_name(rule: dict) -> str:
    family_code = rule.get("family_code", "")
    ontology = rule.get("ontology", {})
    family = ontology.get("family")
    if family:
        return str(family)
    return str(family_code)


def summary_text(rule: dict) -> str:
    for key in ("summary", "description", "rationale"):
        value = rule.get(key)
        if value:
            text = " ".join(str(value).split())
            return text[:220] + ("…" if len(text) > 220 else "")
    return "No summary provided."


def rule_link(rule: dict) -> str:
    return f"{rule.get('id', 'UNKNOWN')}.md"


def render_rule(rule: dict) -> str:
    rid = rule.get("id", "UNKNOWN")
    name = rule.get("name") or rule.get("title") or rid
    description = rule.get("description") or rule.get("summary") or "No description provided."
    layer = rule.get("layer", "unknown")
    ontology = rule.get("ontology", {})
    system_layers = ontology.get("system_layers", [])
    category = category_name(rule)
    family = family_name(rule)

    impact = rule.get("impact", {})
    detection = rule.get("detection", {})
    remediation = rule.get("remediation", {})
    metadata = rule.get("metadata", {})

    lines = [
        f"# {rid}",
        "",
        f"**Name:** {name}",
        "",
        f"**Category:** {category}",
        "",
        f"**Family:** {family}",
        "",
        f"**Primary layer:** `{layer}`",
        "",
        f"**System layers:** {', '.join(f'`{x}`' for x in system_layers) if system_layers else 'None listed'}",
        "",
        "## Description",
        "",
        description,
        "",
    ]

    if impact:
        lines += ["## Impact", ""]
        for k, v in impact.items():
            lines.append(f"- **{k}:** {v}")
        lines.append("")

    if detection:
        lines += ["## Detection", ""]
        for k, v in detection.items():
            if isinstance(v, list):
                lines.append(f"- **{k}:**")
                for item in v:
                    lines.append(f"  - {item}")
            else:
                lines.append(f"- **{k}:** {v}")
        lines.append("")

    if remediation:
        lines += ["## Remediation", ""]
        for k, v in remediation.items():
            if isinstance(v, list):
                lines.append(f"- **{k}:**")
                for item in v:
                    lines.append(f"  - {item}")
            else:
                lines.append(f"- **{k}:** {v}")
        lines.append("")

    if metadata:
        lines += ["## Metadata", ""]
        for k, v in metadata.items():
            lines.append(f"- **{k}:** {v}")
        lines.append("")

    lines += [
        "## Navigation",
        "",
        "- [Back to Human Catalog](index.md)",
        "- [Back to Rule Browser](../rule-browser.md)",
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


def write_rule_pages(rules: list[dict]) -> None:
    for rule in rules:
        out = OUT_DIR / rule_link(rule)
        out.write_text(render_rule(rule), encoding="utf-8")


def render_catalog_index(rules: list[dict]) -> str:
    lines = [
        "# Eco Rules Catalog (Human Readable)",
        "",
        f"**Total rules:** {len(rules)}",
        "",
        "## Browse",
        "",
        "- [Rule Browser](../rule-browser.md)",
        "- [AI layer](layers/ai.md)",
        "- [Architecture layer](layers/architecture.md)",
        "- [Code layer](layers/code.md)",
        "- [Data layer](layers/data.md)",
        "- [Network layer](layers/network.md)",
        "- [Process layer](layers/process.md)",
        "",
        "## Rules",
        "",
    ]
    for rule in rules:
        rid = rule.get("id", "UNKNOWN")
        name = rule.get("name") or rule.get("title") or rid
        lines.append(f"- [{rid} — {name}]({rule_link(rule)})")
    lines.append("")
    return "\n".join(lines)


def group_by_layer(rules: list[dict]) -> dict[str, list[dict]]:
    groups = defaultdict(list)
    for rule in rules:
        layer = str(rule.get("layer", "")).strip().lower()
        groups[layer].append(rule)
    for layer in groups:
        groups[layer] = sorted(groups[layer], key=lambda r: r.get("id", ""))
    return groups


def render_layer_index(layer: str, rules: list[dict]) -> str:
    title = LAYER_LABELS.get(layer, layer.title())
    lines = [
        f"# {title} rules",
        "",
        f"**Total rules:** {len(rules)}",
        "",
        "- [Back to Human Catalog](../index.md)",
        "- [Back to Rule Browser](../../rule-browser.md)",
        "",
    ]

    if not rules:
        lines += ["No rules are currently listed for this layer.", ""]
        return "\n".join(lines)

    lines += [
        "## Rules",
        "",
    ]
    for rule in rules:
        rid = rule.get("id", "UNKNOWN")
        name = rule.get("name") or rule.get("title") or rid
        summary = summary_text(rule)
        lines.append(f"### [{rid} — {name}](../{rule_link(rule)})")
        lines.append("")
        lines.append(summary)
        lines.append("")
        lines.append(f"- Category: **{category_name(rule)}**")
        lines.append(f"- Family: **{family_name(rule)}**")
        lines.append("")
    return "\n".join(lines)


def write_layer_indexes(rules: list[dict]) -> None:
    groups = group_by_layer(rules)
    for layer in LAYER_ORDER:
        out = OUT_DIR / "layers" / f"{layer}.md"
        out.write_text(render_layer_index(layer, groups.get(layer, [])), encoding="utf-8")


def main() -> None:
    ensure_out_dir()
    catalog = load_catalog()
    rules = get_rules(catalog)

    write_rule_pages(rules)
    (OUT_DIR / "index.md").write_text(render_catalog_index(rules), encoding="utf-8")
    write_layer_indexes(rules)

    print(f"Generated {len(rules)} rule pages in {OUT_DIR}")
    print(f"Generated layer indexes in {OUT_DIR / 'layers'}")


if __name__ == "__main__":
    main()
