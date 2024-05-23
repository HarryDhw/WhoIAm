import random

class Baccarat:
    def __init__(self) -> None:
        self.results = []
        self.usedcards = []
        self.record = []

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
        self.usedcards.extend(removed)
        print(self.usedcards)
        print('Removed:%s, Rest:%s' % (n + 1, len(self.cards)))

    def play(self):
        player = {'cards':[], 'amount':0, 'win':False, 'double':False}
        banker = {'cards':[], 'amount':0, 'win':False, 'double':False, 'issixwin':False}
        removed = [self.cards.pop() for _ in range(4)]
        a, b, c, d = removed
        player['cards'] = [a, c]
        banker['cards'] = [b, d]
        player['double'] = a[0] == c[0]
        banker['double'] = b[0] == d[0]

        pn, bn = 0, 0
        for card in player['cards']:
            pn += self.addnum(card)
            pn = pn % 10
        for card in banker['cards']:
            bn += self.addnum(card)
            bn = bn % 10

        if (pn >= 8 or bn >= 8) or (pn >= 6 and bn >= 6):
            self.judge(pn, bn, player, banker)
        else:
            if pn >= 6:
                bn, banker = self.bankerAddCard(bn, banker, removed)
                self.judge(pn, bn, player, banker)

        self.usedcards.extend(removed)
        self.record.append((player, banker))
        print(player, banker, sep='\n')
        print('Removed:%s, Rest:%s' % (len(removed), len(self.cards)))
        print(self.results)
        print(self.record)

    def addnum(self, card):
        try:
            n = card[0] / 1
            return n
        except:
            return 0
        
    def judge(self, pn, bn, player, banker):
        player['amount'] = pn
        banker['amount'] = bn
        if pn > bn:
            self.results.append('P')
            player['win'] = True
        elif pn < bn:
            self.results.append('B')
            banker['win'] = True
        else:
            self.results.append('T')

    def playerAddCard(self, pn, player, removed):
        card = self.cards.pop()
        removed.append(card)
        player['cards'].append(card)
        pn += self.addnum(card)
        pn %= 10
        return pn, player
    
    def bankerAddCard(self, bn, banker, removed):
        card = self.cards.pop()
        removed.append(card)
        banker['cards'].append(card)
        bn += self.addnum(card)
        bn %= 10
        return bn, banker



if __name__ == '__main__':
    game = Baccarat()
    game.makecards()
    game.ready()
    game.play()