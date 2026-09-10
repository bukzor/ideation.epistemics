---
label: REPLAY
standing: agent
why:
  - a-rule-record-separates-check-from-trigger.md
  - benefit-is-attributed-from-real-debt-not-argued.md
---

# When triggers are code and transcripts are kept, firings and attribution are replayed, not instrumented

Firings per period is `count(trigger(prefix) for prefix in transcript
prefixes)`: exact, no agent involved. Attribution is replay too: for
each debt item, find the turn it entered, evaluate the trigger on the
context at that turn, run the check on the state at that turn. For
mechanical checks that is exact; for judgment checks it needs the agent,
on one real historical snapshot, bounded and cheap. Marginal benefit
given an adopted set is a set difference on findings across the replay.

The pipeline for a proposed guidance change is then: write it as
(trigger, check, mode), replay against transcripts and ledger history,
read off cost and marginal benefit. The inputs that cannot be mechanized
are the owner's: debt weight per component and the exchange rate.

Deferred: build when the hand tally of `ATTRIBUTION` stops scaling, or
rules are proposed faster than they can be attributed by hand. The
vocabulary has already paid out on paper.
