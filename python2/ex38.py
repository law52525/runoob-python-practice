import numpy as np

a = np.array(list(map(int, (input() for i in range(3 * 3))))).reshape(3, 3)
print(sum(a.diagonal()))
