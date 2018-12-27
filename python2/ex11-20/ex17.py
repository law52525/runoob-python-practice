from string import ascii_letters, digits

s = input("str > ")
a = len(list(filter(lambda c: c in ascii_letters, s)))
b = len(list(filter(lambda c: c == ' ', s)))
d = len(list(filter(lambda c: c in digits, s)))
print(a, b, d, len(s) - a - b - d)
