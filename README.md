# Extremes and Moments in Greedy Coupon Collection

Christopher D. Long

A replacement proof of the fixed-parameter completion results for the
Xu–Tang coupon collector, with moment and point-process refinements.
At each trial, sample a batch of uniformly distributed coupon types and
keep one least-collected type. The target is a fixed number of complete sets.

- [Canonical paper (PDF)](paper/extremes_and_moments_in_greedy_coupon_collection.pdf)
- [LaTeX source](paper/extremes_and_moments_in_greedy_coupon_collection.tex)
- [Proof audit (PDF)](notes/xu_tang_proof_audit.pdf)
- [Audit record](audit/AUDIT.md), [literature review](audit/REFERENCES.md),
  and [further directions](audit/FURTHER_DIRECTIONS.md)
- [Adversarial review of the replacement proof](audit/ADVERSARIAL_REVIEW.md)

## Main result

For a fixed batch size `g` and fixed target multiplicity `m`, let `T_n`
be the number of trials to finish, and put

```text
B_n = log n + (m−1) log log n
a_g = exp(−γ − ψ(1/g) − log g)
λ   = a_g / (m−1)!
```

Then `g T_n/n − B_n` converges to a Gumbel variable shifted by `log λ`,
with convergence of every fixed absolute moment. In particular,

```text
E T_n   = (n/g) [B_n + log λ + γ + o(1)]
Var T_n = (n/g)² [π²/6 + o(1)].
```

The centered completion times of individual types converge to a Poisson
point process with intensity `λ exp(−y) dy`. The paper also identifies the
joint law, covariance matrix and independent limiting gaps of the last
finitely many completions, with convergence of all mixed polynomial moments.

The theorem covers both sampling conventions (with or without replacement),
any fixed bounded random batch law with positive mean, and independent
holding whose activation probability may tend to zero. The paper gives the
amplitude integral for the random-batch model and a finite sparse-state
mean approximation with an explicit error bound.

## Proof and status

The earlier long proof assemblies are replaced by fixed-time fluid
concentration followed by a simultaneous comparison with independent gamma
clocks. The clock error is controlled in every fixed `L^p` norm by the
unfinished fraction. Explicit extreme-value tails supply the moment control
that was conditional in the older drafts. A separate moving-histogram
fluctuation program is not needed for these completion results and is not
claimed here.

This is a research manuscript with a complete written proof for its stated
fixed-parameter theorem. It has received an analytical and computational
audit, not independent peer review or proof-assistant verification.
No arXiv identifier is assigned to this manuscript here.

A subsequent adversarial pass made the clock construction valid explicitly
on all entrance states, separated centered moment bounds from weak
convergence, and quantified the point-process transfer. It also clarified
the holding corollary's scope. The review includes direct batch enumeration,
exact clock paths and counterexamples to unjustified weakenings of the
hypotheses. It is a second pass by the same assistant, not a separate
referee's assessment.

The one-copy greedy result is already covered by
[Doumas and Spektor (2026)](https://arxiv.org/abs/2607.01463), and classical
single-draw point-process results by
[Ilienko (2019)](https://arxiv.org/abs/1904.12954).
The literature review, checked on 2026-11-21, found no matching prior
resolution of the arbitrary fixed-copy greedy result. This is a bounded
search conclusion, not a guarantee of priority. See the
[claim-by-claim comparison](audit/REFERENCES.md).

## Build and verify

Requires Python 3, `latexmk`, a LaTeX installation with the standard AMS,
geometry, hyperref and Latin Modern packages, and Poppler (`pdftotext`,
`pdfinfo`). On Debian/Ubuntu:

```sh
sudo apt-get install latexmk texlive-latex-extra texlive-fonts-recommended lmodern poppler-utils
make verify
make pdf
make check
```

`make verify` uses exact rational arithmetic and exhaustive finite examples
to check transition rates, the exact mean/variance recursion and clock
bounds. It also checks explicit amplitude values and one-copy benchmarks.
These checks supplement the proof; they do not prove an asymptotic theorem.
The adversarial checks use directly enumerated batch generators to verify
pathwise clock identities and exact sparse-state mean bounds, including a
dense-state counterexample to dropping the sparsity assumption.
`make check` rebuilds both PDFs, rejects unresolved references and overfull
boxes, and compares their extracted text with the committed PDFs.

For exact finite mean and variance calculations:

```sh
python3 scripts/exact_moments.py 5 2 --g 2
python3 scripts/exact_moments.py 5 2 --g 2 --replacement
python3 scripts/exact_moments.py 5 2 --weights 1/4,1/4,1/2
```

The last command assigns probabilities to batch sizes 0, 1 and 2.
The histogram recursion has combinatorially many states and is intended for
small instances. Its state compression is due to Xu and Tang; it is not
claimed as a new exact algorithm.

## Repository conventions

The canonical LaTeX and PDF share a stable title-based basename without
draft, date, journal or version suffixes. Author attribution is retained;
submission contact blocks and correspondence are excluded. Original local
sources are preserved outside this repository; their fingerprints are in
[the provenance record](audit/source_fingerprints.json).

Both PDFs are tracked. Build products and caches are ignored. Changes to
mathematical claims must update the proof, the audit record and the PDF.
