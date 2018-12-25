for i in range(1, 85):
    if not 168 % i:
        j = 168 // i
        if not (i + j) % 2 and not (i - j) % 2 and i > j:
            a = ((i - j) // 2) ** 2 - 100
            print(a)
