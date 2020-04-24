from collections import defaultdict


def count_sort_dict_kp(a):
    b = [-1] * len(a)
    c = [0] * (max(a) - min(a) + 1)

    for i in range(len(a)):
        c[a[i]] += 1

    for i in range(len(c)-1):
        c[i+1] += c[i]

    for i in range(len(a), 0, -1):
        b[c[a[i-1]] - 1] = a[i-1]
        c[a[i-1]] -= 1

    return b


def count_sort_dict(a):
    b, c = [], defaultdict(list)
    for x in a:
        c[x].append(x)

    for k in range(min(c), max(c) + 1):
        b.extend(c[k])

    return b


def test_count_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
    assert(count_sort_dict_kp(seq) == sorted(seq))
    assert(count_sort_dict(seq) == sorted(seq))


if __name__ == "__main__":
    test_count_sort()
