a, b, c, d, e, f = range(6)

N = [[b, c, d, f],
     [a, d, f],
     [a, b, d, e],
     [a, e],
     [a, b, c],
     [b, c, d, e]]

print(b in N[a])    # a = 0

print(b in N[b])    # b is not in {a, d, f}

len(N[f])           # len({b, c, d, e} = 4
