from binary_search import binary_search_iter


# Use set
def intersection_two_arrays_sets(seq1, seq2):
    return set(seq1).intersection(set(seq2))


# Use merge sort
def intersection_two_arrays_ms(seq1, seq2):
    res = []
    while seq1 and seq2:
        if seq1[-1] == seq2[-1]:
            res.append(seq1.pop())
            seq2.pop()
        elif seq1[-1] > seq2[-1]:
            seq1.pop()
        else:
            seq2.pop()
    res.reverse()
    return res


# Use binary search
def intersection_two_arrays_bs(seq1, seq2):
    if len(seq1) > len(seq2):
        seq, key = seq1, seq2
    else:
        seq, key = seq2, seq1

    intersec = []
    for item in key:
        if binary_search_iter(seq, item):
            intersec.append(item)

    return intersec


def test_intersection_two_arrays():
    seq1 = [1, 2, 3, 5, 7, 8]
    seq2 = [3, 5, 6]
    assert(set(intersection_two_arrays_sets(seq1, seq2)) == set([3, 5]))
    assert(intersection_two_arrays_bs(seq1, seq2) == [3, 5])
    assert(intersection_two_arrays_ms(seq1, seq2) == [3, 5])
