"""
    Binary search - for sorted list

    O(logN)
"""


# recursive function
def binary_search_rec_kp(seq, target, low=None, high=None):
    low = low or 0
    high = high or len(seq)

    i_mid = len(seq) // 2
    mid_elem = seq[i_mid]

    if target == mid_elem:
        return (low + high) // 2
    elif target < mid_elem:
        return binary_search_rec_kp(seq[:i_mid], target, low, i_mid-1)
    else:
        return binary_search_rec_kp(seq[i_mid:], target, i_mid+1, high)


# loop
def binary_search_iter_kp(seq, target):
    high, low = len(seq), 0
    while True:
        i_mid = (low + high) // 2
        if target == seq[i_mid]:
            return i_mid
        elif target < seq[i_mid]:
            high = i_mid
        else:
            low = i_mid + 1


def binary_search_iter(seq, target):
    high, low = len(seq), 0
    while low < high:
        mid = (high + low) // 2
        if target == seq[mid]:
            return mid
        elif target < seq[mid]:
            high = mid
        else:
            low = mid + 1
    return None


def test_binary_search():
    seq = [1, 2, 5, 6, 7, 10, 12, 12, 14, 15]
    target = 6
    assert(binary_search_rec_kp(seq, target) == 3)
    assert(binary_search_iter(seq, target) == 3)
    assert(binary_search_iter_kp(seq, target) == 3)


if __name__ == "__main__":
    test_binary_search()
