from random import shuffle

# TODO: write the game of Blackjack

RANKS = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '%s of %s' % (self.rank, self.suit)

    def __repr__(self):
        return self.__str__()


class Deck(object):
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        shuffle(self.cards)

    def get_card(self):
        return self.cards.pop()


