---
label: SANDBOX_FIRST
standing: user
authority: chat.md#L498
why:
  - ../harness.kb/the-agent-is-replaced-by-a-generator-not-modeled.md
---

# The sandbox comes before the substrate

The harness is built before the debt function is run against real
ledgers, before any schema migration, and before any move table is
enforced on disk.

> [!@bukzor] chat.md#L498
> That seems a lot of work for something that seems likely I'll find a flaw and re-do, repeatedly.
> This was the aim of the schematic simulation, I think.

This overrules the sequence proposed just before it (chat.md#L468 to
chat.md#L492): debt function on real data first, attribution by hand,
rules as must-read entries, two weeks, re-measure. That sequence's
residue survives as `PAYOUT_TEST` and as the deferrals in
`../rule-pricing.md`; its ordering does not. What the sandbox buys is
that each flaw is found in seconds and fixed in a few lines, against
generated states rather than against ledgers the owner has to reload.
