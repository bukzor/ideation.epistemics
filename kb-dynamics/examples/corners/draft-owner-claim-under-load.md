---
verdicts:
  queue-empty: false
  no-load-bearing-on-proposed: true
  skeleton-right: false
  all-trusted: true
note: >
  The recorded bad state of confusions 1 and 2. Nothing is proposed, so
  every claim is trusted by its fold; the queue holds the draft, weighted
  by what rests on it; the skeleton is not right because a user claim's
  text is unread.
claims:
  shorthand:
    basis: user
    wording: draft
    grounds: []
    content: [1]
  reading:
    basis: derived
    wording: settled
    grounds: [shorthand]
    content: [2]
---

# A draft owner claim under load
