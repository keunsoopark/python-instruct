# The simplest way of removing duplicates in list
def remove_dup(l1):
    return list(set(l1))


def intersection(l1, l2):
    return list(set(l1) & set(l2))


def union(l1, l2):
    return list(set(l1).union(set(l2)))


def test_sets_operations_with_lists():
    l1 = [1, 2, 3, 4, 5, 5, 9, 11, 11, 15]
    l2 = [4, 5, 6, 8, 7]
    l3 = []
    assert(remove_dup(l1) == [1, 2, 3, 4, 5, 9, 11, 15])
    assert(intersection(l1, l2) == [4, 5])
    assert(union(l1, l2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15])
    assert(remove_dup(l3) == l3)
    assert(intersection(l3, l2) == l3)
    assert(sorted(union(l3, l2)) == sorted(l2))
    print("test done")


if __name__ == "__main__":
    test_sets_operations_with_lists()


