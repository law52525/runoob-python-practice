from itertools import islice

n = 9
f = [1]
print(*islice((f[i + 1] for i in range(n) if not f.append(2 * f[i] + 2)), n - 1, None))
