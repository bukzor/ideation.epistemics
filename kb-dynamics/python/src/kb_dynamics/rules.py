"""Rules gate moves. The set is a candidate (`CANDIDATE_RULES`); the harness shows which have effect.

These are the default standing license: what a move with no license of
its own may do. A licensed move passes every rule here.
"""

from collections.abc import Callable, Iterable
from dataclasses import dataclass

from .model import State
from .moves import Add, Merge, Retract, SettleWording, Step, Stipulate, licensed


@dataclass(frozen=True)
class Rule:
    name: str
    permits: Callable[[State, Step], bool]


def owner_only_changes_need_owner_authority(state: State, step: Step) -> bool:
    """Settling wording, stipulating or adding as user, and retracting or dropping a user claim."""
    move = step.move
    if licensed(step):
        return True
    elif isinstance(move, (SettleWording, Stipulate)):
        return False
    elif isinstance(move, Add):
        return move.claim.basis != "user" and move.claim.wording == "draft"
    elif isinstance(move, Retract):
        return move.claim_id not in state or state[move.claim_id].basis != "user"
    elif isinstance(move, Merge):
        return move.drop not in state or state[move.drop].basis != "user"
    else:
        return True


def unlicensed_merges_preserve_content(state: State, step: Step) -> bool:
    """`AGENT_REDUCTIONS`: the unasked merge is of claims that say one thing (`DUPLICATE`)."""
    move = step.move
    if licensed(step) or not isinstance(move, Merge):
        return True
    elif move.keep not in state or move.drop not in state:
        return True
    else:
        return state[move.keep].content == state[move.drop].content


RULES: tuple[Rule, ...] = (
    Rule(
        "owner-only changes need owner authority",
        owner_only_changes_need_owner_authority,
    ),
    Rule("unlicensed merges preserve content", unlicensed_merges_preserve_content),
)


def permitted(rules: Iterable[Rule], state: State, step: Step) -> bool:
    return all(rule.permits(state, step) for rule in rules)
