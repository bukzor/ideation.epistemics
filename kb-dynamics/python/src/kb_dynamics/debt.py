"""Debt: a vector over the state, one component per kind of rot.

Every rotten claim contributes one plus what rests on it, so a leaf counts
at the lowest priority and never zero (`COMPONENTS`, `LEAF_EXEMPT`). The
weight across components is the owner's and is not set here.
"""

from collections.abc import Collection, Iterator, Mapping
from dataclasses import dataclass
from typing import Literal, assert_never

from .model import ClaimId, State

Component = Literal["proposed-basis", "non-atomic", "duplicate", "wording", "conflict"]
COMPONENTS: tuple[Component, ...] = (
    "proposed-basis",
    "non-atomic",
    "duplicate",
    "wording",
    "conflict",
)
Debt = Mapping[Component, int]

EffectiveBasis = Literal["stipulated", "certified", "proposed"]
WEAKEST_FIRST: tuple[EffectiveBasis, ...] = ("proposed", "certified", "stipulated")


@dataclass(frozen=True)
class Item:
    """One thing the owner can rule on: a claim, the rot it carries, and its contribution."""

    claim: ClaimId
    component: Component
    contribution: int


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

    Stops at `user` and `evidence`. A derived claim with no grounds, one whose
    grounds only motivate it, a claim missing from the state, and a claim in
    its own ancestry are all unwarranted, hence proposed.
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
                if not claim.grounds or claim.sufficiency == "motivates":
                    return "proposed"
                else:
                    folded: set[EffectiveBasis] = {
                        fold(ground, ancestry | {claim_id}) for ground in claim.grounds
                    }
                    return weakest(folded)
            case _:
                assert_never(claim.basis)

    return fold(claim_id, frozenset())


def proposed_roots(state: State) -> Iterator[ClaimId]:
    """Claims where proposedness enters: effectively proposed with no proposed ground.

    A ruling on the root repays everything that folds to it, so the root is
    the queue item and its dependents are its weight, not items of their own.
    A claim in a cycle has only proposed grounds and no root below it, so
    every member of a cycle is a root.
    """
    reach = dependents(state)
    for claim_id, claim in state.items():
        if effective_basis(state, claim_id) != "proposed":
            continue
        elif claim_id in reach[claim_id]:
            yield claim_id
        elif not any(
            effective_basis(state, ground) == "proposed" for ground in claim.grounds
        ):
            yield claim_id


def duplicates(state: State) -> Iterator[ClaimId]:
    """Every claim after the first with the same content, in state order."""
    seen: set[frozenset[int]] = set()
    for claim_id, claim in state.items():
        if claim.content in seen:
            yield claim_id
        else:
            seen.add(claim.content)


def rot(state: State) -> tuple[Item, ...]:
    """Every (claim, component) the state is rotten at, with its contribution."""
    by_component: Mapping[Component, Collection[ClaimId]] = {
        "proposed-basis": tuple(proposed_roots(state)),
        "non-atomic": tuple(c for c, claim in state.items() if len(claim.content) > 1),
        "duplicate": tuple(duplicates(state)),
        "wording": tuple(c for c, claim in state.items() if claim.wording == "draft"),
        # A conflict is a set of claims that cannot all stand (`CONFLICT`); the
        # state carries no relation between contents yet, so none is found.
        "conflict": (),
    }
    weight = dependents(state)
    return tuple(
        Item(claim_id, component, 1 + len(weight[claim_id]))
        for component in COMPONENTS
        for claim_id in by_component[component]
    )


def debt(state: State) -> Debt:
    items = rot(state)
    return {
        component: sum(
            item.contribution for item in items if item.component == component
        )
        for component in COMPONENTS
    }


def queue(state: State) -> tuple[Item, ...]:
    """The owner's review, highest contribution first (`QUEUE`); leaves come last."""
    return tuple(sorted(rot(state), key=lambda item: (-item.contribution, item.claim)))
