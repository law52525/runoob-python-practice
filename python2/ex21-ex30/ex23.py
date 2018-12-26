n = 7


def my_print(is_re):
    a = reversed(range(1, n, 2)) if is_re else range(1, n, 2)
    for i in a:
        yield i


f = lambda i: (n - i) // 2 * " " + i * "*" + "\n"
print(''.join(f(i) for i in my_print(False)) + n * "*")
print(''.join(f(i) for i in my_print(True)), end='')
