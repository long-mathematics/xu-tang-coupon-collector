#!/usr/bin/env python3
"""Adversarial finite checks using enumerated batches and exact arithmetic.

The rate oracle does not use the paper's avoidance-probability formula.
Deterministic internal thresholds check pathwise identities, not the
distributional theorem or independence of the random exponential drivers.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
from math import comb, factorial
from random import Random


@lru_cache(None)
def rates(n, m, residual, weights, replacement):
    """Enumerate the original offer-and-tie rule for each labelled type."""
    mu = sum(j*w for j, w in enumerate(weights))
    loads = tuple(m-r for r in residual) + (m,)*(n-len(residual))
    answer = [F(0) for _ in residual]
    for j, weight in enumerate(weights):
        if not j or not weight:
            continue
        batches = product(range(n), repeat=j) if replacement else combinations(range(n), j)
        count = n**j if replacement else comb(n, j)
        for batch in batches:
            low = min(loads[i] for i in batch)
            if low == m:
                continue
            tied = {i for i in batch if loads[i] == low}
            probability = weight / (count*len(tied))
            for i in tied:
                answer[i] += F(n)/mu*probability
    return tuple(answer)


def run_clocks(n, m, quota, weights, replacement, increments):
    """Run internal thresholds through enumerated state-dependent rates."""
    residual = list(quota)
    thresholds = [tuple(sum(row[:j+1]) for j in range(len(row))) for row in increments]
    internal = [F(0) for _ in quota]
    finish = [None for _ in quota]
    time = area = F(0)
    for _ in range(sum(quota)):
        q = rates(n, m, tuple(residual), weights, replacement)
        assert all(0 <= qi <= 1 for qi in q)
        candidates = []
        for i, ri in enumerate(residual):
            if ri and q[i]:
                distance = thresholds[i][quota[i]-ri]-internal[i]
                assert distance >= 0
                candidates.append((distance/q[i], i))
        assert candidates, 'The chain cannot become trapped before completion'
        dt, winner = min(candidates)
        area += sum(ri > 0 for ri in residual)*dt
        time += dt
        for i in range(len(quota)):
            internal[i] += q[i]*dt
        assert internal[winner] == thresholds[winner][quota[winner]-residual[winner]]
        residual[winner] -= 1
        if not residual[winner]:
            finish[winner] = time
    gamma = tuple(row[-1] for row in thresholds)
    assert tuple(internal) == gamma, 'Every terminal internal time equals its fixed threshold'
    assert area == sum(finish), 'Integrated unfinished population equals sum of residual times'
    assert all(ri >= gi for ri, gi in zip(finish, gamma))
    return finish, gamma, area


@lru_cache(None)
def continuous_mean(n, m, residual, weights, replacement):
    if not any(residual):
        return F(0)
    q = rates(n, m, residual, weights, replacement)
    total = sum(q)
    future = F(0)
    for i, qi in enumerate(q):
        if qi:
            nxt = list(residual)
            nxt[i] -= 1
            future += qi*continuous_mean(n, m, tuple(nxt), weights, replacement)
    return (1+future)/total


def gamma_max_mean(quota):
    """Integrate the independent gamma survival function exactly."""
    answer = F(0)
    for size in range(1, len(quota)+1):
        for subset in combinations(quota, size):
            polynomial = [F(1)]
            for r in subset:
                factor = [F(1, factorial(j)) for j in range(r)]
                nxt = [F(0)]*(len(polynomial)+len(factor)-1)
                for j, a in enumerate(polynomial):
                    for k, b in enumerate(factor):
                        nxt[j+k] += a*b
                polynomial = nxt
            integral = sum(a*F(factorial(j), size**(j+1))
                           for j, a in enumerate(polynomial))
            answer += (-1)**(size+1)*integral
    return answer


def main():
    random = Random(20261121)
    models = [
        (8, 3, (1, 3), (F(0), F(1))),
        (16, 3, (1, 3), (F(0), F(0), F(1))),
        (16, 3, (3, 3), (F(0), F(0), F(1))),
        (24, 3, (1, 2, 3), (F(1, 3), F(1, 3), F(1, 3))),
        (24, 3, (2, 3), (F(0), F(0), F(0), F(1))),
        (16, 3, (1, 3), (F(999, 1000), F(0), F(1, 1000))),
    ]
    path_cases = mean_cases = 0
    for n, m, quota, weights in models:
        d = len(weights)-1
        constant = 2*d
        assert n >= 2*d and F(len(quota), n) <= min(F(1, 2), F(1, 2*constant))
        for replacement in (False, True):
            for trial in range(80):
                increments = [[F(random.randint(1, 997), random.randint(1, 991))
                               for _ in range(r)] for r in quota]
                # Exercise very uneven thresholds, not just typical clocks.
                increments[0][0] *= (F(1, 10**6), F(10**6), F(1))[trial % 3]
                finish, gamma, area = run_clocks(n, m, quota, weights, replacement, increments)
                delta = F(constant, n)*area
                assert all(ri <= 2*gi for ri, gi in zip(finish, gamma))
                assert max(ri-gi for ri, gi in zip(finish, gamma)) <= delta
                assert delta <= F(2*constant, n)*sum(gamma)
                path_cases += 1
            actual = continuous_mean(n, m, quota, weights, replacement)
            ideal = gamma_max_mean(quota)
            assert 0 <= actual-ideal <= F(2*constant, n)*sum(quota)
            mean_cases += 1
    print(f'PASS: {path_cases} exact clock paths from directly enumerated batch generators, including extreme thresholds.')
    print(f'PASS: {mean_cases} exact sparse-state mean bounds against independently integrated gamma maxima.')

    # n >= 2d holds, but sparsity fails: a higher-load type initially has rate 0.
    dense = (4, 2, (1, 2, 2, 2), (F(0), F(0), F(1)), False)
    increments = [[F(1, 1000)], [F(1), F(1)], [F(2), F(1)], [F(3), F(1)]]
    assert rates(*dense)[0] == 0
    finish, gamma, _ = run_clocks(*dense, increments)
    assert finish[0] > 2*gamma[0]
    print('PASS: dense-state counterexample rejects R_i <= 2 G_i without sparsity; the general clock construction still completes.')


if __name__ == '__main__':
    main()
