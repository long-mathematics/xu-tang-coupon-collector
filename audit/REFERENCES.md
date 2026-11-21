# Literature review and claim comparison

Checked through 2026-11-21. This review distinguishes the sampling rule,
retention rule, target multiplicity and conclusion; similar titles do not
by themselves identify the same problem.

## Conclusion

The one-copy greedy problem is already covered by a July 2026 preprint.
The ordinary single-draw multiple-copy distribution and its point-process
version are also prior results. The canonical manuscript therefore makes
no general claim that Gumbel or Poisson limits for coupon collection are new.

No matching prior proof was found for the full result stated here for the
interacting greedy keep-one model with arbitrary fixed multiplicity,
including its sharp linear mean term and joint moment conclusions. No
matching result was found for the theorem's combined random-batch and
sampling extensions either. These are findings of the search described
below, not a proof that no other source exists. Literature claims should be
checked again before journal or arXiv submission.

## Closest sources

| Source | Model and result | Consequence for this manuscript |
| --- | --- | --- |
| Xu–Tang (2011) | Fixed distinct batch, keep a least-collected type, collect `m` complete sets; first two mean terms with `O(mn)` remainder and exact finite computation. | Original problem and exact histogram algorithm must be credited. |
| Doumas–Spektor (2026), Problem II | Same fixed distinct-batch greedy rule, **one** complete set; refined mean, Gumbel law and variance. | The one-copy law, sharp mean and variance are known; their centering constant equals ours. |
| Erdős–Rényi (1961) | Ordinary single-draw collection with fixed multiplicity. | The `g=1` limiting distribution is classical. |
| Ilienko (2019) | Point process of each type's fixed-order arrival in the ordinary collector. | The `g=1` point-process theorem is known, including multiple copies. |
| Schilling–Henze (2021) | Uniform group drawings; counts of types sampled fewer than a fixed number of times have Poisson limits. | Groups are recorded without the greedy keep-one retention rule; this is a related but different process. |
| Gast (2011) | Fluid approximations to hitting times for collections of identical component chains. | Related methodology; does not provide the interacting greedy completion theorem used here. |

### Xu and Tang

Weiyu Xu and Ao Kevin Tang, *A generalized coupon collector problem*,
Journal of Applied Probability 48 (2011), 1081–1094.
[DOI](https://doi.org/10.1239/jap/1324046020),
[arXiv:1010.5608](https://arxiv.org/abs/1010.5608),
[author-hosted paper](https://people.ece.cornell.edu/atang/pub/11/Coupon_collector.pdf).

The mean expansion is
`(n/g)[log n + (m−1) log log n] + O(mn)`.
The finite-state computation is already part of their contribution.
The arXiv record is their original preprint, first submitted in 2010; it
does not identify an arXiv submission of the present manuscript.
The primary paper and bibliographic record were inspected.

### Doumas and Spektor

Aristides V. Doumas and S. Spektor,
*Two Multi–Draw Coupon Collector models with different retention rules*,
arXiv:2607.01463, version 1, 2026-07-01.
[Record](https://arxiv.org/abs/2607.01463),
[full text](https://arxiv.org/html/2607.01463v1).

Problem II collects one complete set. Theorem 14 gives the mean expansion,
Theorem 20 the Gumbel law and Theorem 23 the variance asymptotics.
Equation (70) and Remark 15 identify

```text
C_g = ∫₀¹ [1/(1−(1−x)^g) − 1/(g x)] dx
    = [−ψ(1/g) − γ − log g]/g
    = (log a_g)/g.
```

Thus its one-copy centering agrees with this paper's. The introduction,
Problem II and the cited statements were read in the full primary text.
The present work does not supersede their finer one-copy expansions.

### Classical distribution and point-process results

Paul Erdős and Alfréd Rényi, *On a classical problem of probability theory*,
Magyar Tud. Akad. Mat. Kutató Int. Közl. 6 (1961), 215–220.
[Primary archive PDF](https://static.renyi.hu/renyi_cikkek/1961_on_a_classical_problem_of_probability_theory.pdf).
The original result and its fixed-multiplicity normalization were checked.

Andrii Ilienko, *Convergence of point processes associated with coupon
collector's and Dixie cup problems*, Electronic Communications in
Probability 24 (2019), paper 51, 9 pages.
[DOI](https://doi.org/10.1214/19-ECP263),
[arXiv:1904.12954](https://arxiv.org/abs/1904.12954).
The primary abstract explicitly concerns the point process of fixed-order
arrival times for all coupon types. The bibliographic record and abstract
were inspected; this is sufficient to establish overlap with the
ordinary single-draw special case, not a full audit of that paper's proof.

### Group drawings

Judith Schilling and Norbert Henze, *Two Poisson limit theorems for the
coupon collector's problem with group drawings*, Journal of Applied
Probability 58 (2021), 966–977.
[DOI and publisher abstract](https://doi.org/10.1017/jpr.2021.15).
The primary abstract concerns sampled subsets and the number of types
sampled at most `c−1` times. It does not describe choosing and keeping only
one least-collected type. The publisher abstract and metadata were
inspected; no claim of a full proof review is made.

### Fluid hitting times

Nicolas Gast, *Computing hitting times via fluid approximation: application
to the coupon collector problem*, arXiv:1107.3385 (2011).
[Primary record](https://arxiv.org/abs/1107.3385).
Its component-chain setting and stated mean approximation were checked.
The present paper derives its own concentration and extinction comparison
rather than assuming that a generic fluid limit determines the sharp
completion distribution.

## Recent and adjacent work screened

- Andrii Ilienko, *Limit theorems in the extended coupon collector's problem*,
  online 2026-08-11, journal issue 2027;
  [primary journal text](https://vmsta.org/journal/VMSTA/article/358/read),
  [earlier preprint arXiv:2002.00650](https://arxiv.org/abs/2002.00650).
  Its collector-and-younger-brothers setup uses successive copies of
  ordinary draws, not greedy choice from a batch. The later journal date
  does not make its underlying preprint a new 2026 result.
- Maria Eliza Castro and Rodrigo Marinho, *Cutoff profile for the coupon
  collector with many collections*,
  [arXiv:2610.33199](https://arxiv.org/abs/2610.33199), revised 2026-11-12.
  The primary abstract treats a growing number of collections for the
  ordinary collector. It is relevant to future growing-parameter work;
  it does not by itself settle the interacting greedy model.
- Siva Athreya, Satyaki Mukherjee and Soumendu Sundar Mukherjee,
  *On a Generalisation of the Coupon Collector Problem*,
  [DOI](https://doi.org/10.1007/s10959-025-01417-w).
  The super-coupon model records subsets from sampled batches; it is a
  different retention and coverage problem.
- Michael T. Goodrich, Michael Mitzenmacher, Wojciech Szpankowski and
  Jakub Turowski, *The Dynamic Double Coupon Collector Problem and its
  Applications to Randomized Alternation Algorithms*;
  [author-hosted paper](https://www.cs.purdue.edu/homes/spa/papers/double_hashing.pdf).
  The inspected model uses colored coupons and recoloring, not the
  least-collected keep-one process. Its title alone is not evidence that
  multiple greedy collections have been solved.

## Search method and limits

The search used the original title and author names, forward-citation
listings on the publisher page, references of the closest papers, and
combinations of the following terms:

```text
"Xu" "Tang" "coupon" "Gumbel"
"least-collected" "coupon" limit
"coupon collector" "multiple choices" "limiting distribution"
greedy coupon collection moments
coupon collector batch multiple copies Poisson point process
generalized coupon collector least collected sharp mean
```

Recent arXiv records, primary publisher pages and author-hosted papers were
checked to distinguish keep-one, keep-all, super-coupon, ordinary
multiple-copy and growing-parameter models. Search snippets and secondary
summaries were used only to locate primary sources. The level of inspection
of each closest source is stated above. The search cannot exclude unindexed
work, inaccessible theses or differently named results.

The manuscript's mathematical conclusion rests on its written proof.
Priority is a separate bibliographic question. A complete fixed-parameter
proof does not imply that every related extension is solved or new.
