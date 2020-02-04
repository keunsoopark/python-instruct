def permutation_kp(val):
    if len(val) < 2:
        return [val]
    acc = []
    for c in val:
        acc += [c + elem for elem in permutation_kp(val.replace(c, ""))]
    return acc


# answer from the book
import itertools


def perm(s):
    if len(s) < 2:
        return s
    res = []
    for i, c in enumerate(s):
        for cc in perm(s[:i] + s[i + 1:]):
            res.append(c + cc)
    return res


# as expected, this method outperform all the others.
def perm2(s):
    res = itertools.permutations(s)
    return ["".join(i) for i in res]


# 10_combination.py
def combination(s):
    if len(s) < 2:
        return s
    res = []
    for i, c in enumerate(s):
        res.append(c)
        for cc in perm(s[:i] + s[i + 1:]):
            res.append(cc)
            res.append(c + cc)
    return res


if __name__ == "__main__":
    val = "0123"
    print(permutation_kp(val))
    print(len(permutation_kp(val)))
    print(perm(val))
    print(len(perm(val)))
    print(perm2(val))
    print(len(perm2(val)))
    print(combination(val))
    print(len(combination(val)))

    import timeit, functools  # functools is required to pass argument to function in timeit world.

    t1 = timeit.Timer(functools.partial(permutation_kp, val))
    print("reversing_words_sentence_logic_kp ", t1.timeit(number=1000), "milliseconds")
    t2 = timeit.Timer(functools.partial(perm, val))
    print("reversing_words_sentence_logic_kp ", t2.timeit(number=1000), "milliseconds")
    t3 = timeit.Timer(functools.partial(perm2, val))
    print("reversing_words_sentence_logic_kp ", t3.timeit(number=1000), "milliseconds")
