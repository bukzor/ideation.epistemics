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

Declined: substrate first -- run the debt function on real ledgers,
attribute the debt by hand, adopt the rules the tally picks as must-read
entries, run two weeks, re-measure. Its parts survive as `PAYOUT_TEST`
and as the deferrals in `../rule-pricing.md`; its ordering does not.
What the sandbox buys is
that each flaw is found in seconds and fixed in a few lines, against
generated states rather than against ledgers the owner has to reload.
