from typing import List

seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]


def merge_sort_list(seq: List):
    if len(seq) < 2:
        return seq

    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]
    if len(left) > 1:
        left = merge_sort_list(left)
    if len(right) > 1:
        right = merge_sort_list(right)

    # print("seq:", seq)
    # print("left:", left)
    # print("right:", right)

    res = []
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()

    # print("res:", res)
    # print("return:", (left or right) + res)
    # print()

    return (left or right) + res


def merge_sort_sep(seq):
    if len(seq) < 2:
        return seq

    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]
    if len(left) > 1:
        left = merge_sort_sep(left)
    if len(right) > 1:
        right = merge_sort_sep(right)

    return merge(left, right)


def merge(left, right):
    if not left or not right:
        return left or right

    res = []
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()

    return (left or right) + res


def merge_files(list_files):
    result = []
    final = []
    for filename in list_files:
        aux = []
        with open(filename, "r") as file:
            for line in file:
                aux.append(int(line))
        result.append(aux)
    final.extend(result.pop())

    for l in result:
        final = merge(l, final)

    return final


def merge_sort_linked_list_kp(seq: List):
    pass


def test_merge_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    seq_sorted = sorted(seq)

    assert(merge_sort_list(seq) == seq_sorted)
    assert(merge_sort_sep(seq) == seq_sorted)

    list_files = ["a.dat", "b.dat", "c.dat"]
    l_sorted = [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8]
    assert(merge_files(list_files) == seq_sorted)
    # assert(merge_sort_linked_list_kp(seq) == seq_sorted)


if __name__ == "__main__":
    test_merge_sort()
