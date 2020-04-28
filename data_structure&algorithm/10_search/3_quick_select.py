"""
    Sequential search for non-sorted list
"""


def quick_select_cache(seq, k):
    if len(seq) < 2:
        return seq
    ipivot = len(seq) // 2
    pivot = seq[ipivot]

    before = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    after = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]

    m = len(before)
    if k == m:
        return pivot
    elif k < m:
        return quick_select_cache(before, k)
    else:
        return quick_select_cache(after, k)


def quick_select(seq, k, left=None, right=None):
    left = left or 0
    right = right or len(seq) - 1
    ipivot = len(seq) // 2
    pivot = seq[ipivot]

    # Move pivot to outside of the sort range
    _swap(seq, ipivot, right)
    swapIndex, i = left, right
    while i < right:
        if pivot < seq[i]:
            _swap(seq, i, swapIndex)
            swapIndex += 1
        i += 1

    # Fix the pivot location
    _swap(seq, right, swapIndex)

    # Confirm pivot location
    rank = len(seq) - swapIndex
    if k == rank:
        return seq[swapIndex]
    elif k < rank:
        return quick_select(seq, k, swapIndex+1, right)
    else:
        return quick_select(seq, k, left, swapIndex-1)


def _swap(seq, x, y):
    seq[x], seq[y] = seq[y], seq[x]


if __name__ == "__main__":
    seq = [3, 7, 2, 1, 4, 6, 5, 10, 9, 11]
    k = len(seq) // 2
    print(sorted(seq))
    print(quick_select_cache(seq, k-1))
    print(quick_select(seq, k))

    import numpy
    print(numpy.median(seq))
