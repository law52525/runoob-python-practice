num = 2


def auto_func():
    num = 1
    print('internal block num = {}'.format(num))
    num += 1


for i in range(3):
    print('The num = {}'.format(num))
    num += 1
    auto_func()
