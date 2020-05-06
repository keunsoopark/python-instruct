import heapq


def find_N_largest_items_seq(seq, N):
    return heapq.nlargest(N, seq)


def find_N_smallest_items_seq(seq, N):
    return heapq.nsmallest(N, seq)


def find_smallest_items_seq_heap(seq):
    return heapq.nsmallest(1, seq)[0]


def find_smallest_items_seq(seq):
    return min(seq)


def find_N_smallest_items_seq_sorted(seq, N):
    return sorted(seq)[:N]


def find_N_largest_items_seq_sorted(seq, N):
    return sorted(seq)[len(seq)-N:]


def test_find_N_largest_smallest_items_seq():
    seq = [1, 3, 2, 8, 6, 10, 9]
    N = 3
    assert(find_N_largest_items_seq(seq, N) == [10, 9, 8])
    assert(find_N_smallest_items_seq(seq, N) == [1, 2, 3])
    assert(find_smallest_items_seq_heap(seq) == 1)
    assert(find_smallest_items_seq(seq) == 1)
    assert(find_N_smallest_items_seq_sorted(seq, N) == [1, 2, 3])
    assert(find_N_largest_items_seq_sorted(seq, N) == [8, 9, 10])


if __name__ == "__main__":
    test_find_N_largest_smallest_items_seq()
