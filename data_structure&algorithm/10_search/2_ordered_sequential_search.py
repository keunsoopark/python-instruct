"""
    Sequential search for non-sorted list

    Only works as the input list is sorted.
    The same time complexity as the element is in the list or not
"""


def ordered_sequential_search(seq, n):
    for value in seq:
        if value > n:
            return False
        if value == n:
            return True
    return False


def test_ordered_sequential_search():
    seq = [1, 2, 4, 5, 6, 8, 10]
    seq = sorted(seq)
    n1 = 10
    n2 = 7
    assert(ordered_sequential_search(seq, n1) is True)
    assert(ordered_sequential_search(seq, n2) is False)


if __name__ == "__main__":
    test_ordered_sequential_search()
