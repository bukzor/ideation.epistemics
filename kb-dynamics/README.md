# kb-dynamics

An executable model of a claim ledger under change: the moves an agent or
owner can make on it, the rules that gate those moves, and a debt function
the moves must not raise. The model is tested by property-based generation
and bounded enumeration, with the agent replaced by an operation generator
rather than modeled. Its origin is the captured chat under
`../docs/dev/chats/claude/Created=2026/09/09/14:14:39-05:00/`; the design
ledger at `docs/dev/claims.md` replaces that chat as the entry point.

Layout, as it fills in:

- `docs/dev/claims.md` -- the design ledger ([llm-claims-kb]). The
  `imported-terms` theory inside it is the only place a `why:` may leave
  this directory; `imported-terms.verify.py` beside it certifies that.
- `examples/` -- language-neutral bad states, good states, corners where
  the trust conditions disagree, and traces with provenance, consumed by
  every implementation.
- `python/` -- the first implementation. `transition`, `rules`, and `debt`
  stay pure and total so a later port is a translation.
- `lean/` -- the port, if the design ever stops changing.

Two rules the layout serves. Everything language-neutral lives at this
root. And the subpath stays independent of the sibling projects until a
deliberate reconciliation pass, which is why the outer vocabulary enters
through one theory and nowhere else.

[llm-claims-kb]: ../../bukzor-agent-skills/llm-claims-kb/SKILL.md
