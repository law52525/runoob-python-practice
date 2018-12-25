print(*filter(lambda n: sum(map(lambda x: int(x) ** 3, str(n))) == n, range(100, 1000)))
