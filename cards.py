import random
from values_suits import (
    VALUES
   ,SUITS)

class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        value_name = ""
        suit_name = ""
        values_dict = dict(zip(range(len(VALUES)), VALUES))
        suits_dict = dict(zip(range(len(SUITS)), SUITS))

        for key in values_dict:
            if self.value ==  key:
                value_name = values_dict[key]
        for key in suits_dict:
            if self.suit == key:
                suit_name = suits_dict[key]
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