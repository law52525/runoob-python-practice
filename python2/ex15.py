s = int(input("s > "))
interval = {90: "A", 60: "B", 0: "C"}

for k, v in interval.items():
    if s >= k:
        print(v)
        break
