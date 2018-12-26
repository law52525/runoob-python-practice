for i in range(1, 10):
    for j in range(1, i+1):
        print("{:2d} *{:2d} ={:3d}".format(i, j, i * j), end=' ')
    print()
