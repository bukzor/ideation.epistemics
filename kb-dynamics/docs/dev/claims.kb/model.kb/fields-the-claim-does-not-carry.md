---
label: FIELDS_NOT_CARRIED
standing: agent
why:
  - effective-basis-is-computed-from-grounds-not-stored.md
---

# Fields the claim does not carry

The claim carries no author, no timestamp, no confidence number, and no
stored groundedness:

- author -- git blame has it.
- timestamps -- git has them.
- a confidence number -- false precision.
- groundedness as a stored value -- computed from the grounds
  (`EFFECTIVE_BASIS`).

The test for admitting a field is `NEXT_ACTION_TEST`; none of these
changes a next action that the grounds and the two fields of
`BASIS_WORDING` do not already determine.
