def n(i):
    return 10 if i == 1 else n(i - 1) + 2


print(n(5))
