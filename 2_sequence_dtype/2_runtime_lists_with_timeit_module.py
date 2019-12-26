def tes1():
    l = []
    for i in range(1000):
        l = l + [i]


def tes2():
    l = []
    for i in range(1000):
        l.append(i)


def tes3():
    l = [i for i in range(1000)]


def tes4():
    l = list(range(1000))


if __name__ == "__main__":
    import timeit

    t1 = timeit.Timer("tes1()", "from __main__ import tes1")
    print("concat ", t1.timeit(number=1000), "milliseconds")
    t2 = timeit.Timer("tes2()", "from __main__ import tes2")
    print("append ", t2.timeit(number=1000), "milliseconds")
    t3 = timeit.Timer("tes3()", "from __main__ import tes3")
    print("comprehension ", t3.timeit(number=1000), "milliseconds")
    t4 = timeit.Timer("tes4()", "from __main__ import tes4")
    print("list range ", t4.timeit(number=1000), "milliseconds")
