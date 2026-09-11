#!/usr/bin/env -S uv run
"""Certify MINUTIAE: most open questions in the fleet's ledgers are leaves.

Passes when, over every ledger under the owner's repos except this one
and except git worktree copies, at least half of the `standing: open`
claims have no dependents. Prints the tally either way; exit status is 1
on failure.
"""

import sys
from collections.abc import Iterable
from pathlib import Path

from llm_claims_kb.grounding import Grounding, grounding
from llm_claims_kb.ledger import ledger_roots, read_ledger

HERE = Path(__file__).resolve()
SUBPATH = HERE.parents[4]  # problem.kb -> claims.kb -> dev -> docs -> kb-dynamics
FLEET = (Path.home() / "repo/github.com/bukzor", Path.home() / "claude")


def in_worktree(path: Path) -> bool:
    """A linked git worktree has `.git` as a file; its ledgers are copies."""
    return any((parent / ".git").is_file() for parent in (path, *path.parents))


def open_claims(roots: Iterable[Path]) -> tuple[Grounding, ...]:
    """Every open-standing claim in the given ledgers, this subpath excluded."""
    return tuple(
        record
        for root in roots
        if not root.resolve().is_relative_to(SUBPATH) and not in_worktree(root)
        for record in grounding(read_ledger(root))
        if record.standing == "open"
    )


def leaf_share(records: tuple[Grounding, ...]) -> tuple[int, int]:
    """(leaves, total): how many open claims nothing rests on."""
    return sum(1 for r in records if r.rests_on_it == 0), len(records)


def main() -> None:
    roots = [root for under in FLEET for root in ledger_roots(under)]
    leaves, total = leaf_share(open_claims(roots))
    print(f"open questions: {total}, leaves: {leaves}, ledgers: {len(roots)}")
    sys.exit(0 if total and leaves * 2 >= total else 1)


if __name__ == "__main__":
    main()
