class Num:
    nNum = 1

    def inc(self):
        self.nNum += 1
        print('nNum = {}'.format(self.nNum))


if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print('The num = {}'.format(nNum))
        inst.inc()
