from functools import reduce

n = 20
f = [1, 1]
print(reduce(lambda x, y: x + y, (f[i] / f[i - 1] for i in range(2, n + 2) if not f.append(f[i - 1] + f[i - 2]))))
