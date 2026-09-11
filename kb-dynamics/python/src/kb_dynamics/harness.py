"""Run a generator against the rules from a state, keeping the log."""

from collections.abc import Callable, Iterable

from .model import State
from .moves import Step
from .rules import Rule, permitted
from .transition import Reject, transition

Generator = Callable[[State], Step | None]


def run(
    initial: State, generate: Generator, rules: Iterable[Rule], steps: int
) -> tuple[State, tuple[Step, ...]]:
    """Apply up to `steps` permitted moves; stop at the first the rules or the table refuse."""
    rules = tuple(rules)
    state = initial
    log: list[Step] = []
    for _ in range(steps):
        step = generate(state)
        if step is None or not permitted(rules, state, step):
            break
        after = transition(state, step)
        if isinstance(after, Reject):
            break
        log.append(step)
        state = after
    return state, tuple(log)
