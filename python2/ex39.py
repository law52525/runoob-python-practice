import numpy as np

n = int(input("x > "))
a = np.array([1, 4, 6, 9, 13, 16, 19, 28, 40, 100])
a = np.insert(a, np.searchsorted(a, n), n)
print(a)
