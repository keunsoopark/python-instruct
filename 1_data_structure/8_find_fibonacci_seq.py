# find nth number in Fibonacci sequence

# time complexity = O(n)
def find_fibonacci_seq_iter(n):
    if n < 2:
        return n
    first, second = 0, 1
    for i in range(n):
        first, second = second, first + second

    return first


# time complexity = O(2^n)
def find_fibonacci_seq_rec(n):
    if n < 2:
        return n
    return find_fibonacci_seq_rec(n - 1) + find_fibonacci_seq_rec(n - 2)


def test_find_fib():
    n = 10
    assert (find_fibonacci_seq_iter(n) == 55)
    assert (find_fibonacci_seq_rec(n) == 55)


if __name__ == "__main__":
    test_find_fib()
