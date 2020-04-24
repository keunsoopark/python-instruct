def selection_sort_kp(seq):
    length = len(seq)
    for i in range(length-1):
        min_elem = seq[i]
        for j in range(i+1, length):
            if seq[j] < min_elem:
                min_elem = seq[j]
        seq[i] = min_elem

    return seq


def selection_sort(seq):
    length = len(seq)
    for i in range(length-1):
        min_j = i
        for j in range(i+1, length):
            if seq[j] < seq[min_j]:
                min_j = j
        seq[i], seq[min_j] = seq[min_j], seq[i]

    return seq


def test_selection_sort():
    seq = [11, 3, 28, 43, 9, 4]
    assert(selection_sort_kp(seq) == sorted(seq))
    assert(selection_sort(seq) == sorted(seq))


if __name__ == "__main__":
    test_selection_sort()
    