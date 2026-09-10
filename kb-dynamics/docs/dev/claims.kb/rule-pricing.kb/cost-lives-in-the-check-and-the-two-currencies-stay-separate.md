---
label: CHECK_SETS_COST
standing: agent
why:
  - a-rule-record-separates-check-from-trigger.md
  - ../imported-terms.kb/load-event.md
  - ../imported-terms.kb/weekly-cost.md
---

# Cost lives in the check, not the trigger, and the two currencies stay separate

A check is either mechanical -- code over the state: referential
integrity, exact duplicates, leaf questions, graph-candidate
near-duplicates -- or judgment, where an agent reads and decides. That
bit sets tokens per firing: mechanical is near zero, judgment is the
token size of the check's scope. Part of rule design is pushing checks
toward mechanical, and the record carries the flag.

- Token cost is load events per period times tokens per load event
  (`IMPORTED_LOAD_EVENT`, `IMPORTED_WEEKLY_COST`): the trigger sets the
  rate, the scope sets the size.
- Owner cost is surfaces per period times the context the owner must
  load to act -- the token size of the subgraph needed to judge what was
  surfaced, which is the wall of text quantified.
- The exchange rate between the two is set by the owner and never
  derived.

What made "always scan for near-duplicates" expensive was never the
trigger; it was an order-n-squared judgment check. A constant trigger
paired with a constant-time mechanical check is unremarkable. This
corrects the first reading, which had rejected the constant trigger as
unbounded.
