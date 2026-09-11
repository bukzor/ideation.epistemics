"""Rules gate moves. The set is a candidate (`CANDIDATE_RULES`); the harness shows which have effect."""

from collections.abc import Callable, Iterable
from dataclasses import dataclass

from .model import State
from .moves import Add, Merge, Retract, SettleWording, Step, Stipulate


@dataclass(frozen=True)
class Rule:
    name: str
    permits: Callable[[State, Step], bool]


def only_the_owner_settles_wording(state: State, step: Step) -> bool:
    return step.actor == "owner" or not isinstance(step.move, SettleWording)


def only_the_owner_stipulates(state: State, step: Step) -> bool:
    """Neither the stipulate move nor an add with `basis: user` is an agent's."""
    move = step.move
    if step.actor == "owner":
        return True
    elif isinstance(move, Stipulate):
        return False
    elif isinstance(move, Add):
        return move.claim.basis != "user"
    else:
        return True


def agents_never_retract_user_claims(state: State, step: Step) -> bool:
    """`PRUNE_GUARD`'s basis guard."""
    move = step.move
    return (
        step.actor == "owner"
        or not isinstance(move, Retract)
        or move.claim_id not in state
        or state[move.claim_id].basis != "user"
    )


def agents_merge_only_exact_duplicates(state: State, step: Step) -> bool:
    """`UNASKED_MOVES`: the unasked merge is of exact duplicates, and never drops a user claim."""
    move = step.move
    if step.actor == "owner" or not isinstance(move, Merge):
        return True
    elif move.keep not in state or move.drop not in state:
        return True
    else:
        return (
            state[move.drop].basis != "user"
            and state[move.keep].content == state[move.drop].content
        )


def agents_add_draft_wording_only(state: State, step: Step) -> bool:
    move = step.move
    return (
        step.actor == "owner"
        or not isinstance(move, Add)
        or move.claim.wording == "draft"
    )


RULES: tuple[Rule, ...] = (
    Rule("agents add draft wording only", agents_add_draft_wording_only),
    Rule("only the owner settles wording", only_the_owner_settles_wording),
    Rule("only the owner stipulates", only_the_owner_stipulates),
    Rule("agents never retract user claims", agents_never_retract_user_claims),
    Rule("agents merge only exact duplicates", agents_merge_only_exact_duplicates),
)


def permitted(rules: Iterable[Rule], state: State, step: Step) -> bool:
    return all(rule.permits(state, step) for rule in rules)
