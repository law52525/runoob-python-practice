turn1 = 10000
turn2 = 100

profit = int(input("> ")) / turn1
award = 0

arr = (100, 60, 40, 20, 10, 0)
rat = (1, 1.5, 3, 5, 7.5, 10)

for i in range(len(arr)):
    if profit > arr[i]:
        t = (profit - arr[i]) * rat[i] * turn2
        award += t
        profit = arr[i]
        print(t)

print(award)
