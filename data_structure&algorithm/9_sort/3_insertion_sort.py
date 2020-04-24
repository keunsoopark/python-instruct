def insertion_sort_kp(seq):
    length = len(seq)
    for i in range(length-1):
        if seq[i+1] < seq[i]:
            seq[i], seq[i+1] = seq[i+1], seq[i]
            for j in range(i, 0, -1):
                if seq[j] < seq[j-1]:
                    seq[j], seq[j-1] = seq[j-1], seq[j]
    return seq


def insertion_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq


def insertion_sort_rec(seq, i=None):
    if i is None:
        i = len(seq) - 1
    if i == 0:
        return seq

    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1

    insertion_sort_rec(seq, i=i-1)
    return seq


def test_insertion_sort():
    seq = [11, 3, 28, 43, 9, 4]
    assert(insertion_sort_kp(seq) == sorted(seq))
    assert(insertion_sort(seq) == sorted(seq))
    assert(insertion_sort_rec(seq) == sorted(seq))


if __name__ == "__main__":
    test_insertion_sort()
