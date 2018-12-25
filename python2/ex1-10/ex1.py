from itertools import permutations

a = [1, 2, 3, 4]
for i in permutations(a, 3):
    print(*i)
