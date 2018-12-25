h = 100
n = 10
s = h

for i in range(10 - 1):
    h /= 2
    s += h * 2
    if i == 8:
        print(h / 2)
print(s)
