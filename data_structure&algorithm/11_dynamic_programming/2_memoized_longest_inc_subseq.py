"""
    to.be.contiued...
"""

from bisect import bisect
from itertools import combinations
from functools import wraps

from benchmark import benchmark


s1 = [94, 8, 78, 22, 38, 79, 93, 8, 84, 39]


def naive_longest_inc_subseq(seq):
    # 1) Simple method
    for length in range(len(seq), 0, -1):
        for sub in combinations(seq, length):
            if list(sub) == sorted(sub):
                return len(sub)


def dp_longest_inc_subseq(seq):
    # 2) Dynamic programming
    L = [1] * len(seq)
    # res = []
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1 + L[pre])
    return max(L)


def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


def memoized_longest_inc_subseq(seq):
    # 3) Memoization
    pass


def longest_inc_bisec(seq):
    # 4) Binary search
    pass


@benchmark
def test_naive_longest_inc_subseq():
    print(naive_longest_inc_subseq(s1))


@benchmark
def test_dp_longest_inc_subseq():
    print(dp_longest_inc_subseq(s1))


@benchmark
def test_memoized_longest_inc_subseq():
    print(memoized_longest_inc_subseq(s1))


@benchmark
def test_longest_inc_bisec():
    print(longest_inc_bisec(s1))


if __name__ == "__main__":
    s1 = [94, 8, 78, 22, 38, 79, 93, 8, 84, 39]
    print(s1)
    test_naive_longest_inc_subseq()
    test_dp_longest_inc_subseq()
    test_memoized_longest_inc_subseq()
    test_longest_inc_bisec()
