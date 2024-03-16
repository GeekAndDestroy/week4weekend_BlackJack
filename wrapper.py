import random

class Card():
    def __init__(self, suit, face, value, is_ace):
        self.suit = suit
        self.face = face
        self.value = value
        self.is_ace = is_ace

    suites = ('c', 'h', 's', 'd')
    values = (3, 4, 5, 6, 7, 8, 9, 'j', 'q', 'k', 'a')


class Deck():
    pass
    

class Hand():
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def clear_cards(self):
        self.cards.clear()

    def get_value(self):
        hand = 0
        has_ace = False

        for card in self.cards:
            hand += card.value
            if card.is_ace:
                has_ace = True

        if hand > 21 and has_ace:
            for card in self.cards:
                if hand >21:
                    if card.is_ace:
                        hand -= 10


    def show_hand(self):


class Player():
    pass


class BlackJack():
    pass