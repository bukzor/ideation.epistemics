---
label: EXCHANGE_RATE
standing: user
authority:
  address: dfc18e9d
  words: human-attention is more expensive than llm-tokens (with some highly sensitive exchange rate -- perhaps useful to convert them both to dollars? I'd probably charge $150/hr, myself.)
  about: the exchange rate CHECK_SETS_COST leaves to the owner
why:
  - cost-lives-in-the-check-and-the-two-currencies-stay-separate.md
  - ../imported-terms.kb/weekly-cost.md
---

# Owner attention is dearer than tokens; both convert to dollars, the owner's hour at $150

The two currencies of `CHECK_SETS_COST` stay separate in the record and
meet in dollars when a rule is priced: tokens at their market price,
owner attention at the owner's own rate, initially $150 per hour. The
rate is highly sensitive and the owner's to set (`IMPORTED_WEEKLY_COST`);
what it fixes is only the direction, that a minute of the owner's
attention outweighs a great many tokens.

> [!@bukzor] dfc18e9d
> 2. human-attention is more expensive than llm-tokens (with some highly sensitive exchange rate -- perhaps useful to convert them both to dollars? I'd probably charge $150/hr, myself.)

Consequence: a rule that spends tokens to save owner attention is
cheap at almost any firing rate, and a rule that surfaces to the owner
is expensive at almost any rate. `OBJECTIVE` in `../debt.md` is what
the rate serves.
