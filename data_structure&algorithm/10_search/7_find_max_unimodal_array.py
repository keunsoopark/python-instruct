def find_max_unimodal_array_kp(A):
    if len(A) <= 2:
        return None
    low, high = 0, len(A)
    while low < high:
        mid = (low + high) // 2
        if A[mid-1] < A[mid] and A[mid+1] < A[mid]:
            return A[mid]
        elif A[mid-1] > A[mid]:
            high = mid
        elif A[mid+1] > A[mid]:
            low = mid
    return None


def find_max_unimodal_array(A):
    if len(A) <= 2:
        return None
    left = 0
    right = len(A) - 1
    while right > left + 1:
        mid = (left + right) // 2
        if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
            return A[mid]
        elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
            left = mid
        else:
            right = mid
    return None


def test_find_max_unimodal_array():
    seq = [1, 2, 5, 6, 7, 10, 12, 9, 8, 7, 6]
    assert(find_max_unimodal_array_kp(seq) == max(seq))
    assert(find_max_unimodal_array(seq) == max(seq))


if __name__ == "__main__":
    test_find_max_unimodal_array()
