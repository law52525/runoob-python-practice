f = [0, 1]
print([f[i] for i in range(2, int(input("x > ")) + 1) if not f.append(f[i - 1] + f[i - 2])][-1])
