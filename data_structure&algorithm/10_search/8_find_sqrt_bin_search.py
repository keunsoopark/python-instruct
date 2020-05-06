def find_sqrt_bin_search_kp(n, error=0.001):
    mid = n / 2
    step_size = 0.1
    plus_dir = True
    while step_size > error:
        if abs(mid * mid - n) < error:
            return mid
        elif mid * mid > n:
            mid = mid - step_size
            if plus_dir:
                step_size /= 2
            plus_dir = False
        else:
            mid = mid + step_size
            if not plus_dir:
                step_size /= 2
            plus_dir = True
    return mid


def find_sqrt_bin_search(n, error=0.001):
    lower = n < 1 and n or 1
    upper = n < 1 and 1 or n
    mid = lower + (upper - lower) / 2.0
    square = mid * mid
    while abs(square - n) > error:
        if square < n:
            lower = mid
        else:
            upper = mid
        mid = lower + (upper - lower) / 2.0
        square = mid * mid
    return mid


if __name__ == "__main__":
    a = 2
    b = 9
    import math
    print(math.sqrt(a))
    print(find_sqrt_bin_search_kp(a))
    print(find_sqrt_bin_search(a))
    print(math.sqrt(b))
    print(find_sqrt_bin_search_kp(b))
    print(find_sqrt_bin_search(b))
