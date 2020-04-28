from bisect import bisect

if __name__ == "__main__":
    l = [0, 3, 4, 5]
    assert(bisect(l, 5) == 4)
