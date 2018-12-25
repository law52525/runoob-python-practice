import math


def is_perfect_number(n):
    factor = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if not n % i:
            factor.append(i)
            factor.append(n // i)
    return n == sum(factor) - n


print(*filter(is_perfect_number, range(2, 1000 + 1)))
