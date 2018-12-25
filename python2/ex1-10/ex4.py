from datetime import datetime

b = datetime(*map(int, input("YY MM DD > ").split(' ')))
print((b - b.replace(month=1, day=1)).days + 1)
