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
        face_str = f'║ {self.face:<5} ║'

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
    def __init__(self, num_decks):
        self.deck = []
        # self.suits = ("Spades", "Hearts","Clubs", "Diamonds")
        self.suits = ("\u2664", "\u2661","\u2667", "\u2662")
        self.faces = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
        self.value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.num_decks = 1
        self.build()

    def build(self):
        num_decks = self.num_decks
        while num_decks:
            for suit in self.suits:
                for i in range(len(self.faces)):
                    is_ace = False
                    if i == 12:
                        is_ace = True
                    card = Card(suit, self.faces[i], self.value[i], is_ace) 
                    self.deck.append(card)
            num_decks -=1

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()
    
    def deck_reset(self):
        self.deck = []
        self.build()
    

class Hand():
    def __init__(self):
        self.cards = []

    def add_card(self):
        self.cards.append(Deck.draw())

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
    def __init__(self, name):
        self.name = name    
        self.hand = Hand()

    def hit(self, card):
        
        pass

    def stand(self):
        # Implement logic for player standing
        pass


class Dealer():
    def __init__(self):
        self.hand = Hand()

    def deal_initial_cards(self, player):
        # Implement logic for dealing initial cards
        pass

    def play(self):
        # Implement logic for dealer's actions
        pass


class BlackJack():
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.dealer = Dealer()
        self.deck = Deck()

    def start_game(self):
        #shuffle deck
        self.deck.shuffle()
        #deal cards
        #display initial hands
        pass

    def player_turn(self):
        #allow player to hit or stand
        #If playere busts, end game
        #continue until player stands or busts
        pass

    def dealer_turn(self):
        #after player's turn
        #hit until value is 17 or higher
        pass

    def determine_winner(self):
        # compare player and dealer's hands top determine winner or tie(tie:dealer wins)
        pass


    def reset_game(self):
        ##clear hands and rebuild/shuffle deck
        pass