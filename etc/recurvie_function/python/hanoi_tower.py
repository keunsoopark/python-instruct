def hanoi(num, n_from, to, other):
    if num == 0: return
    print("num: {}, from: {}, other: {}, to: {}".format(num, n_from, to, other))
    hanoi(num - 1, n_from, other, to)
    hanoi(num - 1, other, to, n_from)


hanoi(4, 0, 1, 2)
