# Adversarial review of the replacement proof

Date: 2026-11-21. Baseline: `3f7be97752f8e0b4b2a9d0f5bcceb75cb8649f9d`.
Scope: the new fixed-parameter theorem, particularly the gamma-clock
coupling, conditional laws, exceptional events and convergence of moments.

## Outcome and independence

No counterexample to the core coupling or completion theorem was found.
The proof needed several interfaces made explicit: construction outside the
sparse event, unconditional centered moment bounds and uniform control of
compact point counts in the second limit. The holding corollary's phrase
"every assertion above" was too broad and has been replaced by explicit
statements and scales. These repairs preserve the main theorem and its
centering constant.

This is a fresh derivation and adversarial second-pass review by the same
assistant, not an independent human or separate-agent referee report.
Independence of the computational checks means that their generator is
obtained from direct enumeration of batches and tie decisions, without
using the avoidance formula under review. Neither repeated agreement nor
finite computation certifies an asymptotic proof.

## Proof obligations and repairs

| Obligation | Adversarial question | Result and repair |
| --- | --- | --- |
| Exact process law | Do independent internal clocks really reproduce the interacting collector? | Yes. An explicit exponential race constructs the chain; memorylessness verifies each conditional transition rate. Null trials are integrated out. |
| Conditional independence | Are the gamma clocks independent after the entrance state is selected? | Yes, conditional on the full fixed-time history, because fresh drivers are independent of it. They are not claimed independent after conditioning on a future small-error event. |
| Dense exceptional states | Does the construction exist where the sparse lemma's hypotheses fail? | Yes. The total rate is positive in every unfinished state and finitely many increments remain. The construction is now established before sparsity is used. |
| Lost clock identity | Could dependence or a jump overshoot invalidate `R_i − G_i`? | No. Internal time is continuous and reaches the fixed terminal threshold exactly. Its lost time is the integral of `1 − q_i` until completion. |
| Common error | Is replacing an individual error by an integral over all unfinished types justified? | Yes, pathwise. The integrated population is exactly `sum R_i`, bounded by `2 sum G_i` under sparsity. |
| Clock moments | Is the constant uniform over entrance times and states? | Yes. Conditional gamma additivity gives an explicit gamma-ratio bound; Minkowski gives `C K/n` with no entrance-time dependence. |
| Bad-event moments | Is a high-probability estimate being mistaken for integrability? | No after the explicit repair: Cauchy–Schwarz combines unconditional coarse moments with an exponential failure probability. |
| Centering | Are bounded moments claimed for centered or uncentered completion times? | Centered. The vectors are now defined explicitly; uncentered moments are only `O((log n)^q)`. |
| Moment limits | Is an unjustified double-limit or uniform-integrability step hidden? | A simpler proof fixes one entrance time to bound every higher centered moment. Weak convergence is proved separately; truncation then gives all claimed moment limits. |
| Point-process transfer | Is fixed-entrance tightness sufficiently uniform for the later entrance limit? | The revision computes first moments of compact counts and gives an explicit Laplace error with bounded limiting intensity. |
| Holding | Does time change merely divide every finite moment by a power of the activation probability? | No. Exact means scale that way; finite variance has an extra term. The statement and proof now distinguish finite identities from asymptotic scaling. |

## Re-derived clock construction

After fixing the full history at deterministic time `b`, give each
unfinished type fresh independent rate-one exponential increments. Their
cumulative sums are internal thresholds. In each current state, advance
internal times at the exact per-type transition rates. The smallest ratio
of remaining internal distance to positive rate determines the next jump.

The memoryless property leaves independent exponential internal residuals
after every observed jump. Thus the next external jump has the desired
total rate and type probabilities. A rate can temporarily be zero; this
does not create a problem because the total rate is `F_n(K) > 0` until
completion. Exactly `sum r_i` increments remain. The construction therefore
works on dense states too, without invoking the sparse lower-rate bound.

For each type, its terminal internal threshold is `G_i ~ Gamma(r_i,1)`.
The actual residual time `R_i` is dependent on the other types. In a sparse
state, the rate remains between one half and one, and

```text
R_i − G_i = ∫[b,b+R_i] (1 − q_i(h)) dh
0 ≤ R_i − G_i ≤ Δ = (C/n) ∫[b,∞) K(h) dh
                    = (C/n) Σ R_i ≤ (2C/n) Σ G_i.
```

For `s = sum r_i > 0`, conditional independence gives

```text
E[Δ^p | F_b] ≤ (2C/n)^p Γ(s+p)/Γ(s).
```

The corresponding `L^p` root is at most
`(2C/n) K ||Gamma(m,1)||_p`, uniformly over starting histories.
The construction uses the symmetric tie rule; invariance of the histogram
law supplies the unlabelled conclusions for other allowed tie rules.

The standard random-time-change construction was cross-checked against
the primary account by Anderson and Kurtz,
[Continuous time Markov chain models for chemical reaction networks, §2](https://people.math.wisc.edu/~dfanderson/papers/SURVEY_AndKurtz.pdf).
The manuscript now includes its own finite-state argument rather than
relying on a representation name alone. The integrated error estimate is
then proved directly for this collector.

## Moment audit

At fixed entrance time, the conditional gamma upper tail holds for every
shape configuration. Negative extremes on a bad shape configuration are
bounded by `B_n − b = O(log n)`. Its exceptional probability is exponentially
small. Explicitly, the bad contribution to each gamma absolute moment is
bounded by `[(B_n − b)^p + C] P(bad)`.

For the actual-to-ideal discrepancy, Cauchy–Schwarz gives
`O_b((log n)^p exp(−a_b n/2))` on the bad entrance event. This does not
assume that the event is independent of completion time.

The revised passage to moments has two separate steps:

1. Prove centered joint weak convergence by taking the population limit at
   fixed entrance time, and then the entrance-time limit.
2. Fix one sufficiently large entrance time once and for all. The centered
   gamma moments and the `L^q` error imply bounded higher centered actual
   moments. For any desired power or polynomial degree, choose a strictly
   larger `q`. The tail inequality `E[|X|^p; |X| > R] ≤ R^(p−q) E|X|^q`
   gives uniform integrability and hence moment convergence.

For point processes, a direct gamma calculation supplies the limiting
expectation of the ideal count on an enlarged compact interval. This avoids
inferring a count moment from vague convergence. The explicit Laplace error
is bounded by `C δ_b/ε + λ_b M_I ω_φ(ε)`, with bounded `λ_b`.
The limits are taken in the order `n`, then `b`, then `ε ↓ 0`.

## Negative controls

- **Sparsity is necessary for the fast clock bound.** With `n=4`, batch
  size two and loads `(1,0,0,0)`, the first type's initial rate is zero.
  An early enough terminal internal threshold gives `R_1 > 2 G_1`.
  This satisfies `n ≥ 2d` but violates sparsity. The test checks that the
  general construction still finishes and that the stronger bound fails.
- **Weak convergence is insufficient for moments.** At entrance time zero, set all gamma shapes
  to zero with probability `1/log n`, and all to `m` otherwise. The limiting
  point process is unchanged, but the exceptional contribution to a centered
  `p`th absolute moment is `B_n^p/log n`, diverging when `p > 1`.
  The actual fixed-time concentration estimate excludes this example.
- **Holding does not simply rescale finite variance.** For a base process
  finishing in one deterministic trial, geometric activation has positive
  variance although the original variance is zero. The correct identity is
  `Var D^(p) = [Var D + (1−p) E D]/p²`; the extra term is asymptotically
  negligible only after the theorem's normalization.

## Other checked steps

The audit also checked the finite-difference rate bounds, ordered fluid
simplex, deterministic amplitude, gamma tail calculation, sorting
comparison, de-Poissonization through an independent random horizon,
beta–gamma covariance and spacing identities, and the unbounded-interval
truncation for unfinished counts. No change to those conclusions was needed.

Two minor formal corrections were made: the deterministic profile statement
now ranges over the layers defined in its ODE; the concentration proof
calls its exponential parameter a valid choice instead of an exact
optimizer. The ODE boundary calculation is indexed only where its terms
are defined.

## Verification and status

`scripts/verify_clocks.py` adds 960 exact rational threshold paths, 12 exact
sparse-state mean comparisons and the dense-state negative control. Its
generator comes from enumerating the original batch choices, including
duplicate offers and uniform ties. The independent-gamma mean is integrated
exactly by inclusion–exclusion and polynomial integration. Both sampling
conventions, random batches and a small positive activation probability are
included. The script is part of `make verify` and GitHub CI.

All existing finite checks also pass. Both PDFs are rebuilt and checked,
with visual review after the changes. The numerical records are in
`verification.txt` and `adversarial_verification.txt`.

After these repairs, no unresolved gap was identified in the stated
fixed-parameter theorem. This is a scoped audit judgment, not a claim that
every possible error has been excluded. Growing multiplicity, growing
batches, nonuniform sampling and moving-histogram normal limits remain
outside this proof. The manuscript has not received independent peer review.
