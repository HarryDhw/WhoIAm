import random

class Dice:
    def __init__(self):
        self.dice = list(range(1, 7))

    def show(self):
        print(random.choice(self.dice))

mydice = Dice()



if __name__ == '__main__':
    mydice.show()