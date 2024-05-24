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
            elif bn == 7:
                pn, player = self.playerAddCard(pn, player, removed)
                self.judge(pn, bn, player, banker)
            elif bn <= 2:
                pn, player = self.playerAddCard(pn, player, removed)
                bn, banker = self.bankerAddCard(bn, banker, removed)
                self.judge(pn, bn, player, banker)
            else:
                pn, player = self.playerAddCard(pn, player, removed)
                x = self.addnum(player['cards'][-1])
                if (bn == 3 and x == 8) or (bn == 4 and x in (0, 1, 8, 9)) \
                    or (bn == 5 and x in (0, 1, 2, 3, 8, 9)) or (bn == 6 and x not in (6, 7)):
                    self.judge(pn, bn, player, banker)
                else:
                    bn, banker = self.bankerAddCard(bn, banker, removed)
                    self.judge(pn, bn, player, banker)

        self.usedcards.extend(removed)
        self.record.append((player, banker))
        # print(player, banker, sep='\n')
        # print('Removed:%s, Rest:%s' % (len(removed), len(self.cards)))
        # print(self.results)
        # print(self.record)

    def addnum(self, card):
        try:
            return int(card[0])
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
            if bn == 6:
                banker['issixwin'] = True
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
    x = 0
    while len(game.cards) > 20:
        game.play()
        x += 1
    p, b, t = game.results.count('P'), game.results.count('B'), game.results.count('T')
    print('Games Total:%s - %s - %s' % (x, len(game.results), len(game.record)))
    print('UsedCards:%s,  RestCards:%s' % (len(game.usedcards), len(game.cards)))
    print('Player:%s, Banker:%s, Tie:%s' % (p, b, t))
    print('Player:%.2f, Banker:%.2f, Tie:%.2f' % (p / x, b / x, t / x))
    sample = random.randint(0, 50)
    print('Samples:%s' % sample)
    print(game.results[sample])
    print(game.record[sample])