"""The ladder's second rung: a uniform random agent, as hypothesis strategies.

`agent_steps(state)` draws one agent move against a live state, so a
sequence is drawn interactively and shrinks. `agent_runs(rules)` draws a
whole run from a recorded state under the rules.
"""

from collections.abc import Iterable, Mapping

from hypothesis import strategies as st

from kb_dynamics.examples import load_bad_states, load_corners, load_good_states
from kb_dynamics.harness import run
from kb_dynamics.model import Basis, Claim, ClaimId, State, Sufficiency, Wording
from kb_dynamics.moves import Add, Merge, Retract, SettleWording, Split, Step, Stipulate
from kb_dynamics.rules import Rule

STATES: Mapping[str, State] = {
    example.path.stem: example.state
    for example in [*load_bad_states(), *load_good_states(), *load_corners()]
}

ATOMS = st.integers(0, 4)
NEW_IDS = st.integers(0, 5).map(lambda i: f"new-{i}")
AGENT_BASES: tuple[Basis, ...] = ("proposed", "derived", "evidence", "question", "user")
WORDINGS: tuple[Wording, ...] = ("draft", "settled")
SUFFICIENCIES: tuple[Sufficiency, ...] = ("entails", "motivates")


def claims(ids: Iterable[ClaimId]) -> st.SearchStrategy[Claim]:
    ids = tuple(ids)
    grounds = (
        st.frozensets(st.sampled_from(ids)) if ids else st.just(frozenset[ClaimId]())
    )
    return st.builds(
        Claim,
        basis=st.sampled_from(AGENT_BASES),
        wording=st.sampled_from(WORDINGS),
        grounds=grounds,
        content=st.frozensets(ATOMS, min_size=1, max_size=2),
        sufficiency=st.sampled_from(SUFFICIENCIES),
    )


def agent_steps(state: State) -> st.SearchStrategy[Step]:
    ids = tuple(sorted(state))
    adds = st.builds(Add, NEW_IDS, claims(ids))
    if not ids:
        return adds.map(lambda move: Step("agent", move))
    existing = st.sampled_from(ids)
    moves: st.SearchStrategy[
        Add | Stipulate | SettleWording | Split | Merge | Retract
    ] = st.one_of(
        adds,
        st.builds(Stipulate, existing),
        st.builds(SettleWording, existing),
        st.builds(Retract, existing),
        st.builds(Merge, existing, existing),
        st.builds(Split, existing, NEW_IDS, NEW_IDS, st.frozensets(ATOMS, min_size=1)),
    )
    return moves.map(lambda move: Step("agent", move))


@st.composite
def agent_runs(
    draw: st.DrawFn, rules: Iterable[Rule]
) -> tuple[str, State, tuple[Step, ...], State]:
    """A recorded state, the log of permitted agent moves drawn against it, and the result."""
    name = draw(st.sampled_from(sorted(STATES)))
    attempts = draw(st.integers(0, 8))
    initial = STATES[name]
    final, log = run(initial, lambda state: draw(agent_steps(state)), rules, attempts)
    return name, initial, log, final
