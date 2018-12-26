from functools import reduce

n, a = input("n a > ").split(' ')
print(reduce(lambda x, y: x + y, (int(i * a) for i in range(1, int(n) + 1))))
