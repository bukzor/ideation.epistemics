# `likelihood` removed from claims and deductions

**Applied.** Property dropped from this realm's `claims.jsonschema.yaml`
and `deductions.jsonschema.yaml`, and the field stripped from every
node carrying it.

**Why.** TL asks what *warrants* a claim, not how sure anyone feels.
Those are different axes, and only one of them gates anything: a
`certified:` claim is different in kind from an unchecked one, whereas
`likelihood: 0.7` and `likelihood: 0.6` differ in no way any tool or
reader acts on. Under field presence the open cell is already the
default, so likelihood was a second, uncalibrated representation of
"not sure" sitting beside the real one.

**The one real use found, and where it went.** `prior-art.jsonschema.
yaml` carried `likelihood: 0.7` glossed as "inherits the chat source's
0.7 until independently verified against the actual literature." That
is not a confidence — it is an open obligation with a named discharge
route, hand-rolled. The new scheme says it directly: no field means
open, `certified:` when the literature check is actually run. The
derivation absorbing its own best counterexample is the strongest
evidence I have that it reaches.

**What to check.** Whether you ever made a decision from a likelihood
number. If yes, this removed something load-bearing and I did not see
it.

**Reverse by.** Re-adding the property to both schemas. No node depends
on its absence.
