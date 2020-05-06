import random


def quick_select_kp(seq, k, start=None, end=None, kth_value=None):
    start = start or 0
    end = end or len(seq) - 1

    if kth_value is None:
        kth_value = -1

    if start < end:
        ipivot = _partition(seq, start, end)
        if ipivot == len(seq) - k:
            kth_value = seq[ipivot]
            return seq, kth_value
        _, kth_value = quick_select_kp(seq, k, start, ipivot - 1, kth_value)
        _, kth_value = quick_select_kp(seq, k, ipivot + 1, end, kth_value)

    return seq, kth_value


def _partition(seq, start, end):
    pivot = seq[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and seq[left] <= pivot:
            left += 1
        while left <= right and pivot <= seq[right]:
            right -= 1
        if right < left:
            done = True
        else:
            seq[left], seq[right] = seq[right], seq[left]
    seq[start], seq[right] = seq[right], seq[start]

    return right


def swap(seq, x, y):
    seq[x], seq[y] = seq[y], seq[x]


def quick_select(seq, k, left=None, right=None):
    left = left or 0
    right = right or len(seq) - 1
    ipivot = random.randint(left, right)
    pivot = seq[ipivot]

    # Move pivot out of the sorting range
    swap(seq, ipivot, right)
    swapIndex, i = left, left
    while i < right:
        if seq[i] < pivot:
            swap(seq, i, swapIndex)
            swapIndex += 1
        i += 1

    # Determine the location of pivot
    swap(seq, right, swapIndex)

    # Check the location of pivot
    rank = len(seq) - swapIndex
    if k == rank:
        return seq[swapIndex]
    elif k < rank:
        return quick_select(seq, k, left=swapIndex+1, right=right)
    else:
        return quick_select(seq, k, left=left, right=swapIndex-1)


def find_k_largest_seq_quickselect(seq, k):
    # Find k-th largest value
    seq, kth_largest = quick_select_kp(seq, k)
    # Store k-th largest value
    result = []
    for item in seq:
        if item >= kth_largest:
            result.append(item)

    return result


if __name__ == "__main__":
    seq = [8, 10, 4, 5, 1, 8, 9, 11, 5]
    k = 3
    print(find_k_largest_seq_quickselect(seq, k))
