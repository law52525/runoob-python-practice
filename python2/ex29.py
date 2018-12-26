import math

n = int(input("x > "))
print(int(math.log10(n)) + 1)
print(*(i for i in str(n)[::-1]))
