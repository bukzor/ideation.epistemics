---
last-updated: "2026-07-26"
---

# Port comparison — chat / kb / agda

Part 3 of the plan in `../acs-counterfactual.md`: the thirteen core
points of `./abstract-core.md` run across the three ports, then the
stress findings adjudicated. This table is the porting-survival
measurement the core's validity rests on (core point 13 applied to
ACS itself).

## Survival table

| core point | ACS.chat | ACS.kb | ACS.agda |
|---|---|---|---|
| 1 payload as object | utterances | file bodies | λΠ deep embedding |
| 2 status lattice | 2 written cells (sigils), rest computed | read off fields + kind + path | explicit indexed datatype |
| 3 warranted membership | sigil discipline, attention-enforced | intake check | typing invariant |
| 4 dependency edges | in-dialogue citation | frontmatter paths | store edges |
| 5 versioned, last-wins | message order; dies with session, transported by core block | git history | indexed revisions, prior states first-class |
| 6 retraction cone | manual propagation | tombstone rename + link check | proved exact |
| 7 discharge ↑ / promote ↓ | natural in dialogue | recorded commits | transition rules + soundness proofs |
| 8 two strata | degenerate: checks run out-of-band | two disk regions + guard | object/meta law, native |
| 9 attack intake | strongest — any utterance contests | `contests:` claims | needs the spec amendment first |
| 10 degeneracy audit | visible but unmeasured | liveness report over git | unspecified |
| 11 self-application | ledger about the conversation itself | fleet teachings under own scheme | "ledger about your own build" |
| 12 query layer | at point of use, attention-priced | engine scripts | proved queries |
| 13 porting metric | — | `core.kb` citation measurement | — |

**Zero core points die in any port.** What varies is the *enforcement
grade*: operator attention → tooling → typechecker. The ports differ
not in what the kernel says but in who holds the ledger to it — the
same ascent `../ladder.md` describes, now visible as an enforcement
ladder.

## Per-port: strengthens / weakens / cannot express

- **ACS.chat** strengthens entry cost (a sigil), RN liveness, and
  attack intake — revision is what conversation *is*. It weakens
  persistence and cone exactness (both attention-bound). It cannot
  express durable certificates, history queries past the session, or
  the porting metric.
- **ACS.kb** strengthens persistence, mechanized propagation, and
  loading economics (views + attention banks). It weakens entry cost
  (a file and frontmatter vs a sigil) and transition soundness —
  guards and checks, not proofs; a session can still violate the
  strata discipline until a check catches it. It cannot express
  homogeneous certificate imports or proved-sound transitions.
- **ACS.agda** strengthens exactness across the board: proved cone,
  proved lattice laws, uniform foreign certificates. It weakens
  ergonomics and entry cost most, prose payloads enter only as opaque
  described objects, and it is unbuilt — every cell in its column is
  the spec's promise, not a measurement.

## Stress findings adjudicated

| finding | verdict |
|---|---|
| 1. `described` has no edges | **kernel change** — drift enters through the described door in *every* port (prose in chat, non-claim files in kb, opaque payloads in agda). Minimal fix: edges become legal at every status; warrant duties stay status-gated. |
| 2. multi-store scoping | **realization choice** — one repo per fleet keeps revision order total at kb weight; `../inquiry-scoped-layout.md` handles scope inside the store. Cross-store edges remain an open kernel question; until then, client-side import/symlink. |
| 3. loading economics | **realization choice** — each port prices queries in its own currency (attention, scripts, extraction); the only kernel-level constraint needed is the derived-cache discipline already in core §6. |
| 4. downgrade target | **kernel change** — spec amendment: the target is a port-fixed, recorded transition rule (core §6; ACS.kb fixed it as reopen-to-open). |

Add the two part-1 gaps — attack intake (core §9) and the degeneracy
audit (core §10) are forced by RN/IN but absent from the spec text —
and the counterfactual's net output for ACS is a **four-item spec
amendment list**: described-edges, downgrade rule, attack intake,
degeneracy audit.

## What the comparison establishes

The kernel is confirmed as *semantics*, not representation: the
lattice survives every port while being written down in none of the
file-based cells as an enum; the payload and checker parameterizations
absorb prose and shell scripts without bending. The kernel is
*incomplete* as spec'd: four amendments, all discovered by holding it
against a working system. And the ports are complements, not
rivals — chat for cheap live revision, kb for durable mechanized
weight, agda for proofs about the transition system itself — which is
the ladder thesis, now carrying a measurement as its warrant instead
of an analogy.
