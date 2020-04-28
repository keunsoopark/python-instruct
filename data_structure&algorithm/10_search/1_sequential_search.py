"""
    Sequential search for non-sorted list
    
    As return is True:
        Best: O(1), average: O(n/2), worst: O(n)
    As return is False:
        O(n)
"""


def sequential_search(seq, n):
    for value in seq:
        if value == n:
            return True
    return False


def test_sequential_search():
    seq = [1, 5, 6, 8, 3]
    n1 = 5
    n2 = 7
    assert (sequential_search(seq, n1) is True)
    assert (sequential_search(seq, n2) is False)


if __name__ == "__main__":
    test_sequential_search()
