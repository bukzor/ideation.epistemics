#!/usr/bin/env -S uv run
"""Certify IMPORTED_TERMS: the one theory whose `why:` may leave the subpath.

Passes when every `why:` that resolves outside `kb-dynamics/` is carried by
a claim of this theory, every such link resolves to a file, the theory's
`ontology:` is exactly the words its claims are named for, and each outer
theory a claim cites still stipulates that word, and no import wears the
label of a claim it cites. One finding per line on
stderr; exit status is the number of findings, capped at 1.
"""

import sys
from pathlib import Path

from llm_claims_kb.ledger import Claim, Theory, cited_claim, read_ledger

LEDGER = Path(__file__).resolve().parent
THEORY = LEDGER / "imported-terms.kb"
SUBPATH = LEDGER.parents[2]  # claims.kb -> dev -> docs -> kb-dynamics


def word(claim: Claim) -> str:
    """The word a claim imports, read off its filename: `load-event` is "load event"."""
    return claim.stem.replace("-", " ")


def escapes(path: Path) -> bool:
    return not path.resolve().is_relative_to(SUBPATH)


def confinement(claims: tuple[Claim, ...]) -> list[str]:
    """Outward links carried by any claim outside the theory."""
    return [
        f"{claim.path}: cites outside the subpath from outside imported-terms: {cited.path}"
        for claim in claims
        if not claim.path.resolve().is_relative_to(THEORY)
        for cited in claim.why
        if escapes(cited.path)
    ]


def resolution(imports: tuple[Claim, ...]) -> list[str]:
    return [
        f"{claim.path}: outward link resolves to nothing: {cited.path}"
        for claim in imports
        for cited in claim.why
        if not cited.path.exists()
    ]


def ontology_matches(defining: Claim, imports: tuple[Claim, ...]) -> list[str]:
    stated, named = set(defining.ontology), {word(claim) for claim in imports}
    return [
        *(f"{defining.path}: ontology lists {w!r}, no claim imports it" for w in sorted(stated - named)),
        *(f"{THEORY}/{w.replace(' ', '-')}.md: imports {w!r}, ontology omits it" for w in sorted(named - stated)),
    ]


def still_stipulated(origin: Path, imports: tuple[Claim, ...]) -> list[str]:
    """An outer theory cited for a word must still list that word. A cited file
    that is no theory (a discourse-graph claim, say) stipulates nothing and is
    not asked."""
    findings: list[str] = []
    for claim in imports:
        cited = [cited_claim(origin, prior.path) for prior in claim.why]
        theories = [outer for outer in cited if outer is not None and outer.ontology]
        if theories and not any(word(claim) in outer.ontology for outer in theories):
            labels = [outer.label for outer in theories]
            findings.append(f"{claim.path}: no cited theory stipulates {word(claim)!r}: {labels}")
    return findings


def labels_distinct(origin: Path, imports: tuple[Claim, ...]) -> list[str]:
    """An import's label must differ from every outer claim it cites: once the
    paths are gone, labels are the only handle a reader has."""
    return [
        f"{claim.path}: label {claim.label} is also the cited outer claim's: {prior.path}"
        for claim in imports
        for prior in claim.why
        if (outer := cited_claim(origin, prior.path)) is not None
        and outer.label == claim.label
    ]


def theory_at(theories: tuple[Theory, ...], path: Path) -> Theory:
    return next(theory for theory in theories if theory.path.resolve() == path)


def main() -> int:
    ledger = read_ledger(LEDGER)
    theory = theory_at(ledger.theories, THEORY)
    assert theory.defining is not None, theory.path
    findings = [
        *confinement(ledger.claims),
        *resolution(theory.claims),
        *ontology_matches(theory.defining, theory.claims),
        *still_stipulated(ledger.origin, theory.claims),
        *labels_distinct(ledger.origin, theory.claims),
    ]
    for finding in findings:
        print(finding, file=sys.stderr)
    if not findings:
        outward = sum(escapes(cited.path) for claim in theory.claims for cited in claim.why)
        print(f"ok: {len(theory.claims)} imported terms, {outward} outward links, all confined")
    return min(len(findings), 1)


if __name__ == "__main__":
    sys.exit(main())
