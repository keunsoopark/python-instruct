a, b, c, d, e, f = range(6)

N = [{b: 2, c: 1, d: 4, f: 1},
     {a: 4, d: 1, f: 4},
     {a: 1, b: 1, d: 2, e: 4},
     {a: 3, e: 2},
     {a: 3, b: 4, c: 1},
     {b: 1, c: 2, d: 4, e: 3}]

print(b in N[a])
print(len(N[f]))
print(N[a][b])


N = {'a': set('bcdf'),
     'b': set('adf'),
     'c': set('abde'),
     'd': set('ae'),
     'e': set('abc'),
     'f': set('bcde')}

print('b' in N['a'])
print(len(N['f']))
