import time


def sumOfN2(n):
    start = time.time()
    theSum = 0
    for i in range(1, n + 1):
        theSum = theSum + i
    end = time.time()
    return theSum, end - start


if __name__ == "__main__":
    n = 5
    print("Total: %d\t time: %10.7f sec" % sumOfN2(n))
    n = 200
    print("Total: %d\t time: %10.7f sec" % sumOfN2(n))
