#!/usr/bin/env python3
"""Exact histogram recursion, following Xu--Tang, extended to batch mixtures.

States count types at each capped load 0,...,m. This is a small-parameter
calculator: the number of states can be binomial(n+m,m).
"""
import argparse
from fractions import Fraction as F
from functools import lru_cache
from math import comb


def avoidance(n, k, weights, replacement=False):
    """Probability that a batch avoids a prescribed set of k types."""
    return sum(w * (F(n-k, n)**j if replacement else
                    F(comb(n-k, j), comb(n, j)) if n-k >= j else F(0))
               for j, w in enumerate(weights) if w)


def exact_moments(n, m, weights, replacement=False):
    weights = tuple(map(F, weights))
    if n < 1 or m < 1 or any(w < 0 for w in weights) or sum(weights) != 1:
        raise ValueError('Require n,m >= 1 and a probability vector')
    if not any(weights[1:]):
        raise ValueError('A positive batch size must have positive probability')
    if not replacement and any(weights[n+1:]):
        raise ValueError('Without replacement batch size cannot exceed n')

    @lru_cache(None)
    def solve(state):
        if state[-1] == n:
            return F(0), F(0)
        lower = 0
        transitions = []
        for j, count in enumerate(state[:-1]):
            if count:
                prob = avoidance(n, lower, weights, replacement) - avoidance(
                    n, lower+count, weights, replacement)
                nxt = list(state)
                nxt[j] -= 1
                nxt[j+1] += 1
                transitions.append((prob, solve(tuple(nxt))))
            lower += count
        move = sum(prob for prob, _ in transitions)
        mean = (1 + sum(prob*ms[0] for prob, ms in transitions)) / move
        second = (2*mean - 1 + sum(prob*ms[1] for prob, ms in transitions)) / move
        return mean, second

    mean, second = solve((n,) + (0,)*m)
    return mean, second-mean*mean, solve.cache_info().currsize


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('n', type=int)
    parser.add_argument('m', type=int)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--g', type=int, help='fixed positive batch size')
    group.add_argument('--weights', help='nonnegative rational weights for J=0,1,...; normalized automatically')
    parser.add_argument('--replacement', action='store_true')
    args = parser.parse_args()
    if args.g is not None:
        if args.g < 1:
            parser.error('--g must be positive')
        weights = [F(0)]*args.g + [F(1)]
    else:
        weights = list(map(F, args.weights.split(',')))
        if any(w < 0 for w in weights) or sum(weights) <= 0:
            parser.error('--weights must be nonnegative with positive sum')
        total = sum(weights)
        weights = [w/total for w in weights]
    mean, variance, states = exact_moments(args.n, args.m, weights, args.replacement)
    print(f'mean = {mean}\nmean (decimal) = {float(mean):.12g}')
    print(f'variance = {variance}\nvariance (decimal) = {float(variance):.12g}')
    print(f'states evaluated = {states}')


if __name__ == '__main__':
    main()
