from random import shuffle

RANKS = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.repr = (RANKS.index(rank), SUITS.index(suit))

    def __str__(self):
        return '%s of %s' % (self.rank, self.suit)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.repr.__lt__(other.repr)

    def value(self):
        """
        >>> Card(4, 'Hearts').value()
        4
        >>> Card('Ace', 'Hearts').value()
        11
        >>> Card('Jack', 'Hearts').value()
        10
        """
        return 11 if self.ace() else 10 if self.face_card() else self.rank

    def ace(self):
        return self.rank == 'Ace'

    def face_card(self):
        return self.rank in ('Jack', 'Queen', 'King')


class Deck(object):
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        shuffle(self.cards)

    def get_card(self):
        return self.cards.pop()


class Hand(object):
    def __init__(self, *cards):
        self.cards = list(cards)

    def value(self):
        """
        >>> h = Hand()
        >>> h.add_card(Card(3, 'Clubs'))
        >>> h.value()
        3
        >>> h.add_card(Card('Ace', 'Diamonds'))
        >>> h.value()
        14
        >>> h.add_card(Card('Ace', 'Hearts'))
        >>> h.value()
        15
        >>> h.add_card(Card(8, 'Spades'))
        >>> h.value()
        13
        >>> h.add_card(Card(8, 'Spades'))
        >>> h.value()
        21
        >>> h.add_card(Card(2, 'Spades'))
        >>> h.value()
        -1
        >>> h = Hand()
        >>> h.add_card(Card('Ace', 'Spades'))
        >>> h.add_card(Card('King', 'Spades'))
        >>> h.value()
        22
        """
        if self.blackjack():
            return 22
        values = [0]
        for card in self.cards:
            card_values = (1, 11) if card.ace() else (card.value(),)
            values = [v + x for v in values for x in card_values if v + x <= 21]
        return -1 if not values else sorted(values)[-1]

    def add_card(self, card):
        self.cards.append(card)

    def blackjack(self):
        cards = sorted(self.cards)
        return len(self.cards) == 2 and cards[0].ace() and cards[1].face_card()

    def bust(self):
        return self.value() == -1

    def __str__(self):
        return (self.value(), self.cards).__str__()

    def __repr__(self):
        return self.__str__()


class Player(object):
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = None

    def deal(self, *cards):
        self.hand = Hand(*cards)

    def bet(self):
        if self.chips < 2:
            raise Exception("Insufficient Funds")
        return 2

    def hit(self):
        return self.hand.value() <= 17

    def win(self, chips):
        self.chips += chips

    def push(self):
        pass

    def lose(self, chips):
        self.chips -= chips

    def __str__(self):
        return (self.name, self.chips, self.hand).__str__()


class BlackJack(object):
    def __init__(self, players):
        self.dealer = Player('Dealer', 0)
        self.players = players

    def play_hand(self):
        deck = Deck()
        dealer = self.dealer
        players = self.players

        # Collect bets
        bets = [player.bet() for player in players]

        # Deal Players
        for player in players:
            player.deal(deck.get_card(), deck.get_card())

        # Deal Dealer
        dealer.deal(deck.get_card())

        # Service Players
        for player in players:
            while not player.hand.bust() and player.hit():
                player.hand.add_card(deck.get_card())

        # Service Dealer
        dealer.deal(deck.get_card())
        while not dealer.hand.bust() and dealer.hit():
            dealer.hand.add_card(deck.get_card())

        # Collect
        for bet, player in zip(bets, players):
            if player.hand.bust() or player.hand.value() < dealer.hand.value():
                player.lose(bet)
                dealer.win(bet)
            elif player.hand.value() > dealer.hand.value():
                amount = bet * 3 / 2 if player.hand.blackjack() else bet
                player.win(amount)
                dealer.lose(amount)
            else:
                player.push()

    def __str__(self):
        return '\n'.join((str(p) for p in self.players)) + '\n%s' % self.dealer


def play():
    blackjack = BlackJack([
        Player('Sean', 100),
        Player('YiOu', 100)
    ])
    for _ in xrange(1000):
        blackjack.play_hand()
        print blackjack
        print


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    play()
