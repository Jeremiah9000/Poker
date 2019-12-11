import random


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        value_name = ""
        suit_name = ""
        values = dict(zip(range(13), ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']))
        suits = dict(zip(range(4), ['Spades', 'Diamonds', 'Clubs', 'Herts']))

        for key in values:
            if self.value ==  key:
                value_name = values[key]
        for key in suits:
            if self.suit == key:
                suit_name = suits[key]
        return value_name + " of " + suit_name


class StandardDeck(list):
    def __init__(self):
        super().__init__()
        suits = list(range(4))
        values = list(range(13))
        for value in values:
            for suit in suits:
                self.append(Card(value, suit))

    def shuffle(self):
        random.shuffle(self)
        print("deck shuffled")

    def deal(self, location):
        location.cards.append(self.pop(0))


deck = StandardDeck()
