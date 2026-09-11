"""Debt: a vector over the state, one component per kind of rot.

Every rotten claim contributes one plus what rests on it, so a leaf counts
at the lowest priority and never zero (`COMPONENTS`, `LEAF_EXEMPT`). The
weight across components is the owner's and is not set here.
"""

from collections.abc import Collection, Mapping
from typing import Literal, assert_never

from .model import ClaimId, State

Component = Literal["proposed-basis", "non-atomic", "duplicate", "wording", "stale"]
COMPONENTS: tuple[Component, ...] = (
    "proposed-basis",
    "non-atomic",
    "duplicate",
    "wording",
    "stale",
)
Debt = Mapping[Component, int]

EffectiveBasis = Literal["stipulated", "certified", "proposed"]
WEAKEST_FIRST: tuple[EffectiveBasis, ...] = ("proposed", "certified", "stipulated")


def dependents(state: State) -> Mapping[ClaimId, frozenset[ClaimId]]:
    """Transitive dependents of each claim: everything whose grounds reach it."""
    direct: dict[ClaimId, set[ClaimId]] = {claim_id: set() for claim_id in state}
    for claim_id, claim in state.items():
        for ground in claim.grounds:
            direct.setdefault(ground, set()).add(claim_id)

    def reach(claim_id: ClaimId, seen: frozenset[ClaimId]) -> frozenset[ClaimId]:
        found = seen
        for dependent in direct[claim_id] - seen:
            found = reach(dependent, found | {dependent})
        return found

    return {claim_id: reach(claim_id, frozenset()) for claim_id in direct}


def load(state: State, claim_id: ClaimId) -> int:
    return len(dependents(state)[claim_id])


def weakest(bases: Collection[EffectiveBasis]) -> EffectiveBasis:
    for basis in WEAKEST_FIRST:
        if basis in bases:
            return basis
    raise AssertionError(bases)


def effective_basis(state: State, claim_id: ClaimId) -> EffectiveBasis:
    """The fold over the grounds: as trustworthy as the weakest ground.

    Stops at `user` and `evidence`. A derived claim with no grounds, a claim
    missing from the state, and a claim in its own ancestry are all
    unwarranted, hence proposed.
    """

    def fold(claim_id: ClaimId, ancestry: frozenset[ClaimId]) -> EffectiveBasis:
        if claim_id in ancestry or claim_id not in state:
            return "proposed"
        claim = state[claim_id]
        match claim.basis:
            case "user":
                return "stipulated"
            case "evidence":
                return "certified"
            case "proposed" | "question":
                return "proposed"
            case "derived":
                if not claim.grounds:
                    return "proposed"
                else:
                    folded: set[EffectiveBasis] = {
                        fold(ground, ancestry | {claim_id}) for ground in claim.grounds
                    }
                    return weakest(folded)
            case _:
                assert_never(claim.basis)

    return fold(claim_id, frozenset())


def contribution(state: State, claim_id: ClaimId) -> int:
    return 1 + load(state, claim_id)


def debt(state: State) -> Debt:
    seen_content: dict[frozenset[int], ClaimId] = {}
    duplicates: list[ClaimId] = []
    for claim_id, claim in state.items():
        if claim.content in seen_content:
            duplicates.append(claim_id)
        else:
            seen_content[claim.content] = claim_id
    return {
        "proposed-basis": sum(
            contribution(state, claim_id)
            for claim_id in state
            if effective_basis(state, claim_id) == "proposed"
        ),
        "non-atomic": sum(
            contribution(state, claim_id)
            for claim_id, claim in state.items()
            if len(claim.content) > 1
        ),
        "duplicate": sum(contribution(state, claim_id) for claim_id in duplicates),
        "wording": sum(
            contribution(state, claim_id)
            for claim_id, claim in state.items()
            if claim.wording == "draft"
        ),
        # Staleness compares a claim against rulings newer than it, which needs
        # the move log; a constant until a property demands it.
        "stale": 0,
    }
