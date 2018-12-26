from functools import reduce

n = 20
print(reduce(lambda x, y: x + y, (reduce(lambda x, y: x * y, (j for j in range(1, i + 1))) for i in range(1, n + 1))))
