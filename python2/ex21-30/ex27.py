def my_print(i, s):
    if i == len(s):
        return
    my_print(i + 1, s)
    print(s[i])


my_print(0, input("str > "))
