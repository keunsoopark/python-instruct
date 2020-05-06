
def quick_sort_cache(seq):
    # Use cache
    if len(seq) < 2:
        return seq
    ipivot = len(seq) // 2
    pivot = seq[ipivot]

    before = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    after = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]

    # print("seq", seq)
    # print("pivot", pivot)
    # print("before", before)
    # print("after", after)
    # print()

    return quick_sort_cache(before) + [pivot] + quick_sort_cache(after)


def quick_sort_cache_devided(seq):
    # Same as quick_sort_cache, but divided into two functions
    if len(seq) < 2:
        return seq
    before, pivot, after = _partition_devided(seq)
    return quick_sort_cache_devided(before) + [pivot] + quick_sort_cache_devided(after)


def _partition_devided(seq):
    pivot, seq = seq[0], seq[1:]
    before = [x for x in seq if x <= pivot]
    after = [x for x in seq if x > pivot]
    return before, pivot, after


# https://gmlwjd9405.github.io/2018/05/10/algorithm-quick-sort.html
def quick_sort(seq, start, end):
    # Without using cache
    if start < end:
        ipivot = _partition(seq, start, end)
        quick_sort(seq, start, ipivot - 1)
        quick_sort(seq, ipivot + 1, end)
    return seq


def _partition(seq, start, end):
    pivot = seq[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and seq[left] <= pivot:
            left += 1
        while left <= right and pivot <= seq[right]:
            right -= 1
        if right < left:
            done = True
        else:
            seq[left], seq[right] = seq[right], seq[left]
    seq[start], seq[right] = seq[right], seq[start]     # "right" should be used cuz "left" and "right" are crossed each other already.
    print(right, seq)

    return right


def quick_sort_kp(seq):
    ipivot = len(seq) // 2
    pivot = seq[ipivot]
    for i in range(len(seq)):
        if i < ipivot:
            if seq[i] > pivot:
                pass
    pass


def test_quick_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]

    assert(quick_sort_cache(seq) == sorted(seq))
    assert(quick_sort_cache_devided(seq) == sorted(seq))
    assert(quick_sort(seq, 0, len(seq)-1) == sorted(seq))

    # assert(quick_sort_kp(seq) == sorted(seq))


if __name__ == "__main__":
    test_quick_sort()
