#!/usr/bin/env python3
"""Finite exact identities and numerical benchmarks; not asymptotic proofs."""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product
from math import comb, exp, factorial, fsum, log, pi, sqrt
from exact_moments import avoidance, exact_moments


def check_enumeration():
    cases = 0
    for n in range(1, 7):
        for m in (1, 2, 3):
            for loads in combinations_with_replacement(range(m+1), n):
                for g in range(1, min(n, 3)+1):
                    for replacement in (False, True):
                        batches = list(product(range(n), repeat=g) if replacement
                                       else combinations(range(n), g))
                        counts = [0]*(m+1)
                        bin_prob = [F(0)]*n
                        for batch in batches:
                            low = min(loads[i] for i in batch)
                            counts[low] += 1
                            if low < m:
                                tied = {i for i in batch if loads[i] == low}
                                for i in tied:
                                    bin_prob[i] += F(1, len(tied)*len(batches))
                        weights = (F(0),)*g + (F(1),)
                        for j in range(m):
                            a = sum(v < j for v in loads)
                            b = sum(v <= j for v in loads)
                            expected = avoidance(n, a, weights, replacement)-avoidance(n, b, weights, replacement)
                            assert expected == F(counts[j], len(batches))
                            for i, load in enumerate(loads):
                                if load == j:
                                    assert bin_prob[i] == expected/(b-a)
                        cases += 1
    print(f'PASS: exhaustive batch enumeration and symmetric per-type rates in {cases} histogram/model cases.')


def check_rates():
    cases = 0
    for n in range(2, 31):
        laws = [(F(0),)*g+(F(1),) for g in range(1, min(n, 6)+1)]
        laws += [(F(1, 4), F(1, 4), F(1, 2))]
        for weights in laws:
            d = len(weights)-1
            mu = sum(j*w for j, w in enumerate(weights))
            alpha = (1-weights[0])/mu
            for replacement in (False, True):
                vals = [F(n, 1)/mu*(1-avoidance(n, k, weights, replacement)) for k in range(n+1)]
                for k in range(n):
                    inc = vals[k+1]-vals[k]
                    assert 0 <= inc <= 1
                    assert vals[k] >= alpha*k
                    if n >= 2*d and k+1 <= n/2:
                        assert inc >= 1-F(2*d*(k+1), n)
                    if not replacement:
                        formula = sum(F(j, 1)/mu*w*F(comb(n-k-1, j-1), comb(n-1, j-1))
                                      for j, w in enumerate(weights) if j and w and n-k >= j)
                        assert inc == formula
                cases += 1
    print(f'PASS: exact finite differences, global phase rates, and sparse clock bounds in {cases} cases.')


def check_moments():
    cases = 0
    for n in range(1, 8):
        for g in range(1, n+1):
            weights = (F(0),)*g+(F(1),)
            for replacement in (False, True):
                mean, var, _ = exact_moments(n, 1, weights, replacement)
                ps = [1-avoidance(n, k, weights, replacement) for k in range(1, n+1)]
                assert mean == sum(1/p for p in ps)
                assert var == sum((1-p)/(p*p) for p in ps)
                cases += 1
        for m in (1, 2, 3):
            mean, var, _ = exact_moments(n, m, (F(0),)*n+(F(1),))
            assert mean == n*m and var == 0
    for n, m, g in ((3, 2, 2), (5, 3, 2), (6, 2, 3)):
        base = (F(0),)*g+(F(1),)
        for replacement in (False, True):
            e, v, _ = exact_moments(n, m, base, replacement)
            for p in (F(1, 2), F(2, 3), F(1, 7)):
                held = (1-p,)+(F(0),)*(g-1)+(p,)
                eh, vh, _ = exact_moments(n, m, held, replacement)
                assert eh == e/p
                assert vh == (v+(1-p)*e)/(p*p)
                cases += 1
    print(f'PASS: {cases} exact mean/variance comparisons, deterministic full-choice cases, and holding identities.')


def check_constants():
    # Midpoint quadrature of the nonsingular amplitude integrand.
    def integrand(x, g):
        if g == 1:
            return 0.0
        # g/(1-(1-x)^g)-1/x, evaluated by factored polynomials.
        s = fsum((1-x)**j for j in range(g))
        numerator = fsum(fsum((1-x)**k for k in range(j)) for j in range(1, g))
        return numerator/s
    a = {}
    steps = 20000
    for g in (1, 2, 3):
        a[g] = exp(fsum(integrand((k+0.5)/steps, g) for k in range(steps))/steps)
    expected = {1:1.0, 2:2.0, 3:sqrt(3)*exp(pi/(2*sqrt(3)))}
    assert all(abs(a[g]-expected[g]) < 2e-8 for g in a)
    print('PASS: amplitude integrals agree numerically with a_1=1, a_2=2, a_3=sqrt(3) exp(pi/(2sqrt(3))).')
    gamma = 0.5772156649015329
    for g in (1, 2, 3):
        n = 200000
        ps = [1.0 - ((n-k)*(n-k-1)/(n*(n-1)) if g == 2 else
                    (n-k)*(n-k-1)*(n-k-2)/(n*(n-1)*(n-2)) if g == 3 else
                    (n-k)/n) for k in range(1, n+1)]
        shift = g/n*fsum(1/p for p in ps)-log(n)
        target = gamma+log(expected[g])
        variance = (g/n)**2*fsum((1-p)/(p*p) for p in ps)
        assert abs(shift-target) < 3e-4
        assert abs(variance-pi*pi/6) < 5e-4
        print(f'BENCHMARK: m=1, n={n}, g={g}: mean shift {shift:.9f} (limit {target:.9f}); scaled variance {variance:.9f}.')


if __name__ == '__main__':
    check_enumeration()
    check_rates()
    check_moments()
    check_constants()
