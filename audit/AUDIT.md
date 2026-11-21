# Mathematical and repository audit

Review date: 2026-11-21.

## Scope and provenance

The inspected local sources were the moving-tail synthesis, the
terminal-cloud synthesis and the Xu–Tang sections of the broader
terminal-defect framework. Their relative filenames and SHA-256 hashes are
recorded in `source_fingerprints.json`. Original sources were preserved
outside the new public repository.

Earlier research discussions were also reviewed. They describe later
integrating-factor, localization and hybrid lower-layer revisions, including
repairs that postdate the inspected local sources. Those discussions are
evidence of development history; the unavailable revised source files were
not treated as audited proofs. Private transcripts are not published here.

The old moving-tail synthesis retained a common-interval martingale
hypothesis. The terminal-cloud synthesis asserted a completion distribution
but retained an additional uniform-integrability hypothesis for the sharp
mean. The earlier sources therefore did not provide a complete unconditional
proof of all the results now stated in the canonical paper.

## Findings and repairs

The companion [proof audit](../notes/xu_tang_proof_audit.pdf) supplies the
equations and counterexamples behind these findings.

| Finding in the inspected proof assemblies | Resolution in the replacement |
| --- | --- |
| Row-specific martingale estimates end before the common interval needed by the bootstrap. | Use concentration only on each fixed fluid interval; no common growing interval is needed. |
| A top-row stopping time is substituted for an all-row stopping time without proving the needed variance bounds. | Remove the stopped moving-tail argument from the completion proof. |
| Tightness is strengthened to one fixed bound holding with probability tending to one. | Prove an explicit exponentially small fixed-time failure probability. |
| The count-decrement martingale sign is inconsistent in representation formulas. | State the convention correctly in the audit; derive the replacement directly from exact transition rates. |
| A logarithmic-power cushion from the envelope is omitted in a later use. | Do not use that envelope in the new proof. |
| A density-scale envelope is used to claim a square-root-scale quadratic remainder bound. | Exhibit the failed scale comparison; replace the nonlinear remainder analysis by an integrated clock error. |
| A barrier exponent is claimed to be of order `log n` where the allowed variance scale gives only constant order. | Record the invalid inference and reported later repair; avoid either envelope version in the replacement. |
| Smallness in probability and good-event conditional estimates are used for unconditional factorial moments. | Use bounded Laplace tests for laws and explicit gamma tails plus `L^p` comparison for moments. |
| The one-copy entrance convention is mixed with the general entrance formula. | One gamma argument covers every `m ≥ 1`. |
| A singleton atom of a Poisson law is used as a continuity set. | Use a continuity interval or the discrete topology. |
| Stopping at a variance threshold can include an overshoot. | Supply a correct predictable-truncation martingale lemma. |
| A buffered square-root bound is described in language suggestive of a normal CLT. | Make no moving-histogram normal-limit claim. |

These are defects in arguments or interfaces, not counterexamples to the
fixed-parameter completion theorem.

## Replacement proof checked

1. **Exact chain.** The class transition rate is the difference of two
   avoidance probabilities. Histogram transitions do not depend on the tie
   rule. Under symmetric ties the rate of each unfinished type is at most
   one and at least `1 − C K/n` when `K` types remain and `n ≥ 2d`.
2. **Fixed time.** A bounded-jump martingale inequality and Gronwall give
   exponential concentration around a finite triangular ODE on each fixed
   interval. Separation of the base equation identifies the amplitude;
   variation of constants gives every deterministic layer's leading term.
3. **Sparse state.** Independent Poisson drivers give independent residual
   gamma clocks. Every actual remaining time lies between its gamma clock
   and that clock plus a common error. The error is bounded by
   `(2C/n) sum G_i`, hence is `O(K/n)` in each fixed `L^p` norm.
4. **Extremes.** Conditional Laplace products identify the Poisson limit.
   Explicit upper and lower tails control all moments of the largest fixed
   number of points. Lower gamma shapes contribute no points in this window.
5. **Transfer.** First take the population limit at fixed entrance time,
   then send that entrance time to infinity. The common error tends to zero
   in `L^p`. Exponentially rare bad entrance states are controlled by coarse
   global completion moments.
6. **Discrete time.** An independent exponential clock and a maximal moment
   estimate change every completion time by an error tending to zero in
   every fixed `L^p` norm after scaling. The same method treats independent
   geometric holding clocks uniformly in their activation probability.
7. **Consequences.** Gamma and beta identities give the explicit means,
   covariances and independent limiting gaps. A truncation argument handles
   the unbounded interval used for the unfinished-type count.

The common error controls all individual completion times at once. This
supplies the point-process result as well as the maximum. The fixed-time
argument resolves the prior moment hypothesis without claiming the older,
stronger moving-tail fluctuation program.

## Strengthenings and boundaries

Proved here: the completion law for each fixed target multiplicity; the
linear-order mean correction; leading variance; every fixed moment; joint
late order statistics and gaps; the completion point process; both sampling
conventions; fixed bounded random batches; additional holding; deterministic
layer amplitudes; and a finite sparse-state mean error bound.

Not asserted: parameters growing with population size, nonuniform coupon
probabilities, a moving-histogram CLT, or a quantitative Gumbel convergence
rate. See [further directions](FURTHER_DIRECTIONS.md). Known special cases
are credited in [the literature review](REFERENCES.md), particularly the
one-copy greedy and ordinary single-draw results.

## Computational and document validation

`make verify` checks exhaustive finite batches against the transition
formulas, exact finite differences and sparse rate bounds, and independent
exact mean/variance calculations. It includes deterministic full-choice
instances, holding identities, amplitude values and large one-copy
benchmarks. The captured record is [verification.txt](verification.txt).

`make pdf` and `make check` build both documents, check labels and citations,
reject unresolved LaTeX diagnostics and overfull boxes, scan source/PDF
metadata for submission contact information, and compare committed PDF text
with a fresh build. All pages were rendered and visually inspected.

These are analytical and computational checks, not a proof-assistant
verification or independent referee report. Exact finite calculations do not
establish the asymptotic theorem by themselves.

## Editorial and repository changes

- Replaced duplicated component assemblies with one canonical manuscript
  and one short audit note.
- Used stable title-based LaTeX/PDF names and retained author attribution.
- Removed submission-specific front matter from the public presentation;
  no personal addresses, correspondence or private source archives are
  included.
- Added an exact finite mean/variance calculator, reproducible builds,
  automated checks, citation metadata and maintenance instructions.
- Preserved originals outside the repository and recorded their hashes.
- Did not submit the manuscript to arXiv. No verified arXiv record for this
  manuscript was located in the reviewed material; the Xu–Tang arXiv record
  cited in the bibliography belongs to their original 2010 preprint.
