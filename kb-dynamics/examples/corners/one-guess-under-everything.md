---
verdicts:
  queue-empty: false
  skeleton-right: false
  all-trusted: false
note: >
  One agent guess with ten derivations chained on it. The queue is one
  item of weight eleven; no claim is trusted, since every fold reaches
  the guess. One ruling repays the whole chain.
claims:
  guess: {basis: proposed, wording: settled, grounds: [], content: [0]}
  d1: {basis: derived, wording: settled, grounds: [guess], content: [1]}
  d2: {basis: derived, wording: settled, grounds: [d1], content: [2]}
  d3: {basis: derived, wording: settled, grounds: [d2], content: [3]}
  d4: {basis: derived, wording: settled, grounds: [d3], content: [4]}
  d5: {basis: derived, wording: settled, grounds: [d4], content: [5]}
  d6: {basis: derived, wording: settled, grounds: [d5], content: [6]}
  d7: {basis: derived, wording: settled, grounds: [d6], content: [7]}
  d8: {basis: derived, wording: settled, grounds: [d7], content: [8]}
  d9: {basis: derived, wording: settled, grounds: [d8], content: [9]}
  d10: {basis: derived, wording: settled, grounds: [d9], content: [10]}
---

# One guess under everything
