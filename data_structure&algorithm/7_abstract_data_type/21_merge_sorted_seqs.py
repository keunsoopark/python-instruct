import heapq


def merge_sorted_seqs(seq1, seq2):
    return list(heapq.merge(seq1, seq2))


def test_merge_sorted_seq():
    seq1 = [1, 2, 3, 8, 9, 10]
    seq2 = [2, 3, 4, 5, 6, 7, 9]
    seq3 = seq1 + seq2
    assert(merge_sorted_seqs(seq1, seq2) == sorted(seq3))


if __name__ == "__main__":
    test_merge_sorted_seq()
