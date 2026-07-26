#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = ["pyyaml"]
# ///
"""Re-runnable check certifying `claims.kb/path-conflates-type-and-topic.md`.

The claim: a node's type and its topic share one path component, so
`collection_of()` -- "nearest enclosing *.kb/" -- reports the elaboration
scope rather than the collection for every node living inside one. Type
detection thus fails exactly at the recursion `inquiry-scoped-layout.md`
wants more of.

The check: assert the conflation on real nodes here, plus a control. The
control matters -- an unelaborated node still reports correctly, which is
what makes this specific to elaboration rather than general breakage, and
what makes the defect invisible in a flat graph.

    ./certify_type_topic_conflation.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from warrant_audit import collection_of  # noqa: E402

REALM = Path(__file__).parent.parent

# node, the collection it belongs to, what collection_of says instead
CONFLATED = (
    (
        "sources.kb/knot-theory-chat.kb/glossary.kb/ACS--agda-claim-system.md",
        "sources",
        "glossary",
    ),
    ("background.kb/prior-art.kb/atms-tms.md", "background", "prior-art"),
)

# node, the collection it belongs to -- and reports, having no elaboration
CONTROL = (("claims.kb/two-base-statuses-not-four.md", "claims"),)


def main() -> int:
    rc = 0
    for relative, belongs_to, reported in CONFLATED:
        path = REALM / relative
        if not path.exists():
            print(f"  MISSING {relative}", file=sys.stderr)
            rc = 1
            continue
        actual = collection_of(path)
        if actual == reported and actual != belongs_to:
            print(f"  ok      {relative}: in {belongs_to}.kb, reports {actual!r}")
        else:
            print(
                f"  FAIL    {relative}: expected {reported!r}, got {actual!r}",
                file=sys.stderr,
            )
            rc = 1

    for relative, belongs_to in CONTROL:
        path = REALM / relative
        actual = collection_of(path)
        if actual == belongs_to:
            print(f"  ok      {relative}: control reports {actual!r}")
        else:
            print(
                f"  FAIL    {relative}: control expected {belongs_to!r}, got {actual!r}",
                file=sys.stderr,
            )
            rc = 1

    if rc:
        print("FAIL: conflation not as claimed", file=sys.stderr)
    else:
        print(f"PASS: {len(CONFLATED)} node(s) report their elaboration scope, not their collection")
    return rc


if __name__ == "__main__":
    sys.exit(main())
