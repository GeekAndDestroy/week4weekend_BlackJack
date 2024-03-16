import random
import time

class Card():
    def __init__(self, suit, face, value, is_ace):
        self.suit = suit
        self.face = face
        self.value = value
        self.is_ace = is_ace

    # def show_card(self):
    #     print(f"{self.face} of {self.suit}")
        
    def show_card(self):
        if self.face == '10':
            # Adjust spacing for '10' to fit in the card properly
            face_str = f'║ {self.face} ║'
        else:
            face_str = f'║ {self.face:<5} ║'

        if self.is_ace:
            visual = [
                '  ╔════════════╗',
                f'  {face_str}',
                '  ║            ║',
                '  ║            ║',
                f'  ║     {self.suit:^3}    ║',
                '  ║            ║',
                '  ║            ║',
                '  ║            ║',
                f'  {face_str}',
                '  ╚════════════╝'
            ]
        else:
            visual = [
                '  ╔════════════╗',
                f'  {face_str}',
                '  ║            ║',
                '  ║            ║',
                f'  ║     {self.suit:^3}    ║',
                '  ║            ║',
                '  ║            ║',
                '  ║            ║',
                f'  {face_str}',
                '  ╚════════════╝'
            ]

        for line in visual:
            print(line)

    def hidden_card(self):
        return [
            '   ╔════════════╗',
            '   ║░░░░░░░░░░░░║',
            '   ║░░░░░░░░░░░░║',
            '   ║░░░░░░░░░░░░║',
            '   ║░░░░░░░░░░░░║',
            '   ║░░░░░░░░░░░░║',
            '   ║░░░░░░░░░░░░║',
            '   ║░░░░░░░░░░░░║',
            '   ║░░░░░░░░░░░░║',
            '   ╚════════════╝'
            ],


class Deck():
    def __init__(self):
        self.deck = []
        self.suits = ('Clubs', 'Hearts', 'Spades', 'Diamonds')
        self.faces = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
        self.value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.build()

    def build(self):
        for suit in self.suits:
            for i in range(len(self.faces)):
                is_ace = False
                if i == 12:
                    is_ace = True
                card = Card(suit, self.faces[i], self.value[i], is_ace) 
                deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)
    

class Hand():
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def clear_cards(self):
        self.cards.clear()

    def get_value(self):
        hand_value = sum(card.value for card in self.cards)
        num_aces = sum(1 for card in self.cards if card.is_ace)

        while hand_value > 21 and num_aces > 0:
            hand_value -= 10  
            num_aces -= 1

        return hand_value


    def show_hand(self):
        for card in self.cards:
            card.show_card()


class Player():
    pass


class BlackJack():
    pass