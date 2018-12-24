from itertools import permutations

a = [1, 2, 3, 4]
p = 0
for i in permutations("1234", 2):
    p += 1
    print(*i)

print(p)
