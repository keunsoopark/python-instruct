import timeit


command = "x = 2 + 2"
print(command, "| time consumption:", timeit.timeit(command))

command = "x = sum(range(10))"
print(command, "| time consumption:", timeit.timeit(command))
