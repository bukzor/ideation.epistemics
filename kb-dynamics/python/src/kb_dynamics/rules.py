"""Rules gate moves. The set is a candidate (`CANDIDATE_RULES`); the harness shows which have effect."""

from collections.abc import Callable, Iterable
from dataclasses import dataclass

from .model import State
from .moves import SettleWording, Step, Stipulate


@dataclass(frozen=True)
class Rule:
    name: str
    permits: Callable[[State, Step], bool]


def only_the_owner_settles_wording(state: State, step: Step) -> bool:
    return step.actor == "owner" or not isinstance(step.move, SettleWording)


def only_the_owner_stipulates(state: State, step: Step) -> bool:
    return step.actor == "owner" or not isinstance(step.move, Stipulate)


RULES: tuple[Rule, ...] = (
    Rule("only the owner settles wording", only_the_owner_settles_wording),
    Rule("only the owner stipulates", only_the_owner_stipulates),
)


def permitted(rules: Iterable[Rule], state: State, step: Step) -> bool:
    return all(rule.permits(state, step) for rule in rules)
