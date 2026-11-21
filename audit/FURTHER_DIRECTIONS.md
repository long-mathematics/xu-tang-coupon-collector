# Further directions and limits

The fixed-parameter completion theorem, its moments and late point process
are proved in the canonical paper. The items below are separate research
questions, not hidden hypotheses in that proof.

## Quantitative convergence

The proof takes the population limit first at fixed fluid time and then
sends that time to infinity. A rate would require estimates uniform in a
growing entrance time: concentration, the gamma-array approximation and the
amplitude error would need to be balanced together. The clock lemma already
gives a quantitative error conditional on a sparse state, but this alone is
not a quantitative final Gumbel bound. Doumas–Spektor already treat refined
one-copy asymptotics, so any proposed new rate should be compared with that
work rather than presented as new for every parameter choice.

## Growing target multiplicity or batch size

The gamma extreme-value calculation uses a fixed integer shape. Growing
`m` changes its tail and centering; growing batch sizes change the rate
constants and fluid estimates. Neither follows by substituting a sequence
into a theorem proved for fixed parameters. Growing multiplicity for the
ordinary single-draw collector has its own literature, including the 2026
Castro–Marinho preprint listed in the literature review. The interacting
greedy extension would require new uniform arguments.

## Nonuniform coupon probabilities

Uniform sampling makes the histogram sufficient and gives equal per-type
rates within a load class. Unequal probabilities remove this symmetry.
Independent comparison clocks would have different rates, with completion
extremes driven by the distribution of rare types. A theorem would need
explicit assumptions on that distribution and a new amplitude analysis.
Classical nonuniform coupon results do not automatically cover greedy
choice from several offers.

## Moving histogram fluctuations

The original all-layer stability program is stronger than what is needed
to locate the last completions. It may be useful for mesoscopic statistics,
but the common-interval stopping and nonlinear remainder estimates still
need a separate complete proof before any such theorem is claimed. A
square-root estimate with a logarithmic buffer is not a normal CLT.

## Certified finite computation

The exact histogram recursion implemented here is practical for small
parameters. Its state count still grows combinatorially. The paper's
sparse-state gamma bound can provide boundary values for a truncated
recursion with a rigorous additive error. Designing and benchmarking that
truncated solver, selecting a cost/error tradeoff and improving the constant
would be useful computational follow-up. The current exact calculator does
not implement this truncation and does not claim a new complexity bound.
