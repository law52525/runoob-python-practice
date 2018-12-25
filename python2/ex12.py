import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if not n % i:
            return False
    return True


print(*filter(is_prime, range(101, 200 + 1)))
