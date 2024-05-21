import random

class Dice:
    def __init__(self):
        self.dice = list(range(1, 7))

    def show(self):
        print(random.choices(self.dice, k=3))
        
    def makegames(self, n):
        arr = []
        for _ in range(n):
            dices = random.choices(self.dice, k=3)
            if len(set(dices)) == 1:
                arr.append([dices, 'other'])
            else:
                amount = sum(dices)
                if amount >= 11:
                    arr.append([dices, 'big'])
                else:
                    arr.append([dices, 'small'])
        self.sample = arr
        return self.sample
    
    def showdata(self, n):
        data = self.makegames(n)
        b, s, o = 0, 0, 0
        for i in data:
            if i[1] == 'big':
                b += 1
            elif i[1] == 'small':
                s += 1
            else:
                o += 1
        print('Big:%s  Small:%s  Other:%s  Total:%s' % (b, s, o, n))
        print('Big:%.2f  Small:%.2f  Other:%.2f' % (b / n, s / n, o / n))

mydice = Dice()



if __name__ == '__main__':
    mydice.showdata(1000)