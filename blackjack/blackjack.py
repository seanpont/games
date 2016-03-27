from random import shuffle

RANKS = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
PLAYS = {0: 'stay', 1: 'hit', 2: 'double down'}


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '%s of %s' % (self.rank, self.suit)

    def __repr__(self):
        return self.__str__()

    def value(self):
        return 11 if self.ace() else 10 if self.face_card() else self.rank

    def values(self):
        return (1, 11) if self.ace() else (10,) if self.face_card() else (self.rank,)

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
        >>> Hand(Card(3, 'Clubs')).value()
        3
        >>> Hand(Card(3, 'Clubs'), Card('Ace', 'Diamonds')).value()
        14
        >>> Hand(Card(3, 'Clubs'), Card('Ace', 'Diamonds'), Card('Ace', 'Hearts')).value()
        15
        >>> Hand(Card(3, 'Clubs'), Card('Ace', 'Diamonds'), Card('Ace', 'Hearts'), Card(8, 'Spades')).value()
        13
        >>> Hand(Card(9, 'Clubs'), Card('Ace', 'Diamonds'), Card('Ace', 'Hearts'), Card(10, 'Spades')).value()
        21
        >>> Hand(Card(10, 'Clubs'), Card('Ace', 'Diamonds'), Card('Ace', 'Hearts'), Card(10, 'Spades')).value()
        -1
        >>> Hand(Card('Ace', 'Spades'), Card('King', 'Spades')).value()
        21
        """
        values = self.values()
        return -1 if not values else values[-1]

    def values(self):
        """
        >>> Hand(Card('Ace', 'Clubs'), Card('Ace', 'Diamonds')).values()
        (2, 12)
        >>> Hand(Card('Ace', 'Clubs'), Card(2, 'Diamonds')).values()
        (3, 13)
        >>> Hand(Card('Ace', 'Clubs'), Card(2, 'Diamonds'), Card(3, 'Hearts')).values()
        (6, 16)
        >>> Hand(Card('Ace', 'Clubs'), Card(2, 'Diamonds'), Card(3, 'Hearts'), Card(10, 'Clubs')).values()
        (16,)
        """
        values = 0,
        for card in self.cards:
            values = tuple((v + x for v in values for x in card.values() if v + x <= 21))
        return tuple(sorted(set(values)))

    def add_card(self, card):
        self.cards.append(card)

    def compare(self, dealer_hand, bet):
        if self.blackjack():
            return 0 if dealer_hand.blackjack() else bet * 3 / 2
        elif self.bust():
            return -bet
        else:
            return bet if self.value() > dealer_hand.value() else -bet if self.value() < dealer_hand.value() else 0

    def blackjack(self):
        return len(self.cards) == 2 and self.has_ace() and self.has_face_card()

    def has_ace(self):
        return any((card.ace() for card in self.cards))

    def has_face_card(self):
        return any((card.face_card() for card in self.cards))

    def bust(self):
        return self.value() == -1

    def __str__(self):
        return (self.value(), self.cards).__str__()

    def __repr__(self):
        return self.__str__()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.chips = 0
        self.hand = None

    def deal(self, *cards):
        self.hand = Hand(*cards)

    def bet(self):
        return 2

    def add_chips(self, chips):
        self.chips += chips

    def play(self, dealer_card):
        """
        return one of:
            0: stay,
            1: hit,
            2: double down
        :param dealer_card: Card
        :return: str
        """
        return 1 if self.hand.value() < 17 else 0

    def __str__(self):
        return (self.name, self.chips, self.hand).__str__()


class CmdLinePlayer(Player):
    def play(self, dealer_card):
        return int(raw_input('%s: Stay (0), Hit (1), or Double Down (2)?: ' % self.name))

    def add_chips(self, chips):
        super(CmdLinePlayer, self).add_chips(chips)
        print '%s %s' % (self.name, 'won!' if chips > 0 else 'pushed' if chips == 0 else 'lost :(')


class AdvancedPlayer(Player):
    def hit(self, dealer_card):
        """ http://www.blackjackclassroom.com/wp-content/uploads/2009/12/single-deck-basic-strategy.png """
        #                  2  3  4  5  6  7  8  9  10 A
        return {(11, 21): (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                (10, 20): (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                (9, 19):  (0, 0, 0, 0, 2, 0, 0, 0, 0, 0),
                (8, 18):  (0, 2, 2, 2, 2, 0, 0, 1, 1, 0),
                (7, 17):  (2, 2, 2, 2, 2, 1, 1, 1, 1, 1),
                (6, 16):  (1, 1, 2, 2, 2, 1, 1, 1, 1, 1),
                (5, 15):  (1, 1, 2, 2, 2, 1, 1, 1, 1, 1),
                (4, 14):  (1, 1, 2, 2, 2, 1, 1, 1, 1, 1),
                (3, 13):  (1, 1, 2, 2, 2, 1, 1, 1, 1, 1),
                (2, 12):  (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                (21,):    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                (20,):    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                (19,):    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                (18,):    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                (17,):    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                (16,):    (0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
                (15,):    (0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
                (14,):    (0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
                (13,):    (0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
                (12,):    (1, 1, 0, 0, 0, 1, 1, 1, 1, 1),
                (11,):    (2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
                (10,):    (2, 2, 2, 2, 2, 2, 2, 2, 1, 1),
                (9,):     (2, 2, 2, 2, 2, 1, 1, 1, 1, 1),
                (8,):     (1, 1, 1, 2, 2, 1, 1, 1, 1, 1),
                (7,):     (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                (6,):     (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                (5,):     (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                (4,):     (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                }[self.hand.values()][dealer_card.value() - 2]


class Blackjack(object):
    def __init__(self, dealer, players):
        self.dealer = dealer
        self.players = players

    def play_hand(self):
        deck = Deck()

        # Collect bets
        bets = [player.bet() for player in self.players]

        # Deal players
        for player in self.players:
            player.deal(deck.get_card(), deck.get_card())

        # Deal Dealer
        self.dealer.deal(deck.get_card())
        dealer_card = self.dealer.hand.cards[0]

        # Service players
        for i, player in enumerate(self.players):
            self.render("%s's turn" % player.name)
            while not player.hand.bust():
                play = player.quiz(dealer_card)
                if play in (1, 2):  # hit or double down
                    card = deck.get_card()
                    player.hand.add_card(card)
                    self.render("%s drew a %s" % (player.name, card))
                if play == 2:
                    bets[i] *= 2
                if play in (0, 2):  # stay or double down
                    break

        # Service Dealer
        self.dealer.deal(deck.get_card())
        while not self.dealer.hand.bust() and self.dealer.quiz(None):
            self.dealer.hand.add_card(deck.get_card())

        self.render("Dealer has played")

        # Collect
        for bet, player in zip(bets, self.players):
            exchanged = player.hand.compare(self.dealer.hand, bet)
            player.add_chips(exchanged)
            self.dealer.add_chips(-exchanged)

    def __str__(self):
        return '%s\n' % self.dealer + '\n'.join(map(str, self.players))

    def render(self, state):
        pass


class CmdLineBlackjack(Blackjack):
    def render(self, state):
        print '\n%s\n%s\n' % (state, self)


def simulate_play(rounds):
    print 'Simulating %s rounds of Blackjack' % rounds
    blackjack = Blackjack(Player('Dealer'),
                          (Player('Basic'), AdvancedPlayer('Advanced')))
    for _ in xrange(rounds):
        blackjack.play_hand()

    print blackjack


def cmd_line_play(rounds):
    num_players = int(raw_input("Number of players: "))
    players = [CmdLinePlayer(raw_input("Player %s name: " % i))
               for i in range(num_players)]
    dealer = Player('Dealer')
    blackjack = CmdLineBlackjack(dealer, players)
    for _ in xrange(rounds):
        print '\n============================'
        blackjack.play_hand()


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    import argparse

    parser = argparse.ArgumentParser(description='Play Blackjack.')
    parser.add_argument('--cmd', dest='cmd', action='store_const',
                        const=True, default=False,
                        help='Command Line Version')
    parser.add_argument('--rounds', help='Number of rounds', type=int,
                        default=10000)

    args = parser.parse_args()
    if args.cmd:
        cmd_line_play(args.rounds)
    else:
        simulate_play(args.rounds)
