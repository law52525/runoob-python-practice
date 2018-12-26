from itertools import permutations

print(*(i for i in "abc"))
print(" ".join(3 * ["|"]))
for p in permutations("xyz"):
    f = []
    for i, v in enumerate(p):
        if v == "x":
            f.append(i not in (0, 2))
        elif v == "z":
            f.append(i != 2)
        if len(f) == 2 and all(f):
            print(*p)
            break
