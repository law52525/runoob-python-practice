a = [1, 2, 3]
b = a[:]
c = b.copy()

a.append(4)
print(a, b)
b.append(4)
print(a, b, c)
