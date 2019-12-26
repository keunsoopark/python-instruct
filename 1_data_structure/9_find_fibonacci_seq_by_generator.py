# find nth number in Fibonacci sequence with using generator


def fib_generator(n):
    if n < 2:
        yield n
    first, second = 0, 1
    seq = 0
    while seq < n:
        yield second
        first, second = second, first + second
        seq += 1


if __name__ == "__main__":
    for i in fib_generator(10):
        print(i)
