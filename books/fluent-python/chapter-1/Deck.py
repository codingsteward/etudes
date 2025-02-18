import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades hearts diamonds clubs'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, index):
        return self._cards[index]

    def __str__(self):
        return str(self._cards)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def card_value(card):
    rank_value = Deck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

deck = Deck()
len(deck)
print(deck)
for card in sorted(deck, key=card_value):
    print(card)
