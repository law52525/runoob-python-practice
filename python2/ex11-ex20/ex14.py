import math

n = int(input("n > "))
factor = []
for i in range(2, int(math.sqrt(n)) + 1):
    while not n % i:
        n = n // i
        factor.append(str(i))
print("*".join(factor))
