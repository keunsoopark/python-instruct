from heap import Heap


def heap_sort2_kp(seq):
    h = Heap(seq)
    result = [h.extract_max() for i in range(len(seq))]
    result.reverse()
    return result


def heap_sort2(seq):
    s = list(seq)
    heap = Heap(s)
    res = []
    for _ in range(len(s)):
        res.insert(0, heap.extract_max())
    return res


def test_heap_sort2():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    sorted_seq = sorted(seq)

    assert(heap_sort2(seq) == sorted_seq)
    # assert(heap_sort2_kp(seq) == sorted(seq))
    assert(heap_sort2_kp(seq) == sorted_seq)


if __name__ == "__main__":
    test_heap_sort2()