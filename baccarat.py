import random

class Baccarat:
    def __init__(self) -> None:
        pass

    def makecards(self):
        suits = ['Spade', 'Heart', 'Club', 'Diamond']
        numbers = list(range(1, 11)) + list('JQK')
        cards = []
        for suit in suits:
            for n in numbers:
                cards.append((n, suit))
        self.cards = cards * 8
        random.shuffle(self.cards)

    def makesure(self, card):
        return self.cards.count(card)
    
    def ready(self):
        card = self.cards.pop()
        try:
            n = int(card[0] / 1)
        except:
            n = 10
        removed = [card]
        for _ in range(n):
            removed.append(self.cards.pop())
        print(removed)
        print('Removed:%s, Rest:%s' % (n + 1, len(self.cards)))

    def play(self):
        player = {'cards':[], 'amount':0, 'win':False}
        banker = {'cards':[], 'amount':0, 'win':False}
        a, b, c, d = [self.cards.pop() for _ in range(4)]
        player['cards'] = [a, c]
        banker['cards'] = [b, d]
        pn, bn = 0, 0
        for card in player['cards']:
            try:
                pn += card[0]
            except:
                pn += 0
        for card in banker['cards']:
            try:
                bn += card[0]
            except:
                bn += 0
        player['amount'] = pn % 10
        banker['amount'] = bn % 10
        print(player, banker, sep='\n')
        print('Removed:%s, Rest:%s' % (4, len(self.cards)))


if __name__ == '__main__':
    game = Baccarat()
    game.makecards()
    game.ready()
    game.play()