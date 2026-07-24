#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = ["pyyaml"]
# ///
"""
An executable statement of RN's retraction invariant, for discourse graphs.

Born out of ideation.epistemics (2026-07-24). {TL, RN} says a retracted
claim's dependents must be revisited -- re-derived, retracted in turn, or
restated without the lost support (drop the edge). Nothing in
`Skill(llm-discourse-graph)` enforces that; the instruction lives in prose,
which is the failure mode `mechanism-over-exhortation` was written about.
This is the invariant in runnable form.

It is deliberately NOT a census. An earlier draft reported how much of
{TL, RN} each graph populates; that was discarded as circular -- adoption is
caused in part by design quality, so usage frequency cannot tell you what to
build (`claims.kb/incumbent-design-is-evidence-not-canon.md`). What remains
is a defect check and a design diagnostic, neither of which asks how popular
anything is.

- **Violation (exit 1)**: a live node still pointing at a retracted one.
  Found a real instance on first run: a deduction in template.python-project
  still concluding a retracted claim.

- **Diagnostic**: `depends:` edges bucketed by target collection. The field
  is documented as context ("without implying support or refutation") but is
  also written claim -> claim as genuine support. A propagation walker cannot
  separate the two from the data, so the counts size an ambiguity the new
  design has to resolve by typing the edge.

Written against today's vocabulary, which is being re-derived from the axioms
(`questions.kb/how-should-repo-weight-absorb-tl-rn.md`). The invariant is what
survives that; the field names are not expected to.

    ./warrant_audit.py [PATH]
"""

import sys
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

import yaml

EDGE_FIELDS = (
    "depends",
    "premises",
    "conclusion",
    "candidate-resolutions",
    "related",
    "broader",
    "narrower",
    "why",
)
RETRACTED = "retracted"


@dataclass(frozen=True)
class Node:
    path: Path
    collection: str
    frontmatter: dict

    @property
    def status(self) -> str | None:
        status = self.frontmatter.get("status")
        return status if isinstance(status, str) else None

    def edges(self, fields: Iterable[str] = EDGE_FIELDS) -> list[tuple[str, Path | None]]:
        """(field, resolved-target) per edge; None when nothing resolves."""
        found = []
        for field in fields:
            value = self.frontmatter.get(field)
            targets = [value] if isinstance(value, str) else value
            if not isinstance(targets, list):
                continue
            for target in targets:
                if isinstance(target, str):
                    found.append((field, resolve_edge(self.path, target)))
        return found


def resolve_edge(source: Path, target: str) -> Path | None:
    """Resolve an edge under both live path conventions.

    File-relative (`../claims.kb/x.md`) is current, per the discourse-graph
    ADR that superseded lexical scoping. Older graphs still write
    collection-relative edges (`claims.kb/x.md` from a sibling collection),
    resolved by walking up. Both are in service across the fleet, so both
    are tried -- file-relative first, since it is unambiguous.
    """
    direct = (source.parent / target).resolve()
    if direct.exists():
        return direct
    if target.startswith(("./", "../")):
        return None
    for ancestor in source.parents:
        candidate = (ancestor / target).resolve()
        if candidate.exists():
            return candidate
    return None


def extract_frontmatter(text: str) -> dict:
    """Parse leading YAML frontmatter; {} when absent or not a mapping."""
    if not text.startswith("---"):
        return {}
    lines = text.split("\n")
    end = next((i for i, line in enumerate(lines[1:], 1) if line.rstrip() == "---"), None)
    if end is None:
        return {}
    parsed = yaml.safe_load("\n".join(lines[1:end]))
    return parsed if isinstance(parsed, dict) else {}


def collection_of(path: Path) -> str:
    """Nearest enclosing *.kb/ directory name, or 'root' for loose files."""
    for parent in path.parents:
        if parent.name.endswith(".kb"):
            return parent.name.removesuffix(".kb")
    return "root"


def load_nodes(root: Path) -> list[Node]:
    nodes = []
    for path in sorted(root.rglob("*.md")):
        if path.name == "CLAUDE.md" or ".git" in path.parts:
            continue
        frontmatter = extract_frontmatter(path.read_text(encoding="utf-8"))
        if frontmatter:
            nodes.append(Node(path.resolve(), collection_of(path), frontmatter))
    return nodes


def depends_by_target(nodes: list[Node]) -> dict[str, int]:
    """Bucket `depends:` edges by target collection: the overload measure."""
    counts: dict[str, int] = {}
    for node in nodes:
        for _, target in node.edges(("depends",)):
            name = collection_of(target) if target is not None else "(unresolved)"
            counts[name] = counts.get(name, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))


def unpropagated_retractions(nodes: list[Node]) -> list[tuple[Node, str, Node]]:
    """Live nodes still pointing at a retracted one -- RP violations."""
    by_path = {node.path: node for node in nodes}
    violations = []
    for node in nodes:
        if node.status == RETRACTED:
            continue
        for field, target in node.edges():
            target_node = by_path.get(target) if target is not None else None
            if target_node is not None and target_node.status == RETRACTED:
                violations.append((node, field, target_node))
    return violations


def render_report(nodes: list[Node], root: Path) -> tuple[str, int]:
    violations = unpropagated_retractions(nodes)
    out = [f"=== warrant audit: {root} ===", "", "edge typing (`depends:` by target)"]

    buckets = depends_by_target(nodes)
    for name, count in buckets.items():
        out.append(f"  -> {name:<19} {count:>4}")
    if not buckets:
        out.append("  (none)")
    if len(buckets) > 1:
        out.append("  => mixes context and support; the new design must type this edge")

    out += ["", "retraction propagation (RN)"]
    if violations:
        out.append(f"  ❌ {len(violations)} unpropagated retraction(s):")
        for node, field, target in violations:
            source = node.path.relative_to(root)
            dead = target.path.relative_to(root)
            out.append(f"     {source}  --{field}-->  {dead}  [retracted]")
    else:
        retracted = sum(1 for node in nodes if node.status == RETRACTED)
        out.append(f"  ✅ clean ({retracted} retracted node(s), no live dependents)")

    out.append("")
    return "\n".join(out), (1 if violations else 0)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    assert root.is_dir(), root
    nodes = load_nodes(root)
    report, code = render_report(nodes, root)
    print(report)
    return code


if __name__ == "__main__":
    sys.exit(main())
