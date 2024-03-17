import random
import time

class Card():
    def __init__(self, suit, face, value, is_ace):
        self.suit = suit
        self.face = face
        self.value = value
        self.is_ace = is_ace

   
        
    def show_card(self):
    
        face_str = f'║ {self.face:<5}      ║'
        face_str2 = f'║      {self.face:>5} ║'

        visual = [
                '  ╔════════════╗',
                f'  {face_str}',
                '  ║            ║',
                '  ║            ║',
                f'  ║     {self.suit:^3}    ║',
                '  ║            ║',
                '  ║            ║',
                '  ║            ║',
                f'  {face_str2}',
                '  ╚════════════╝'
            ]

        for line in visual:
            print(line)

    def hidden_card(self):
        return [
            '  ╔════════════╗',
            '  ║░░░░░░░░░░░░║',
            '  ║░░░░░░░░░░░░║',
            '  ║░░░░░░░░░░░░║',
            '  ║░░░░░░░░░░░░║',
            '  ║░░░░░░░░░░░░║',
            '  ║░░░░░░░░░░░░║',
            '  ║░░░░░░░░░░░░║',
            '  ║░░░░░░░░░░░░║',
            '  ╚════════════╝'
        ]

    
class Deck():
    def __init__(self, num_decks=1):
        self.deck = []
        # self.suits = ("Spades", "Hearts","Clubs", "Diamonds")
        self.suits = ("\u2664", "\u2661","\u2667", "\u2662")
        self.faces = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
        self.value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.num_decks = num_decks
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

    def show_hand(self, hidden= False):
        for i, card in enumerate(self.cards):
            if hidden and i == 0:
                
                for line in card.hidden_card():
                    print(line)
            else:
                card.show_card()


class Player():
    def __init__(self, name):
        self.name = name    
        self.hand = Hand()


class Dealer():
    def __init__(self):
        self.hand = Hand()

    def deal_initial_cards(self, player, deck):
        for _ in range(2):
            card = deck.draw()
            player.hand.add_card(card)
        card = deck.draw()
        self.hand.add_card(card)


class BlackJack():
    def __init__(self):
        self.player = None
        self.dealer = Dealer()
        self.deck = Deck()
        self.total_score = {'Player': 0, 'Dealer': 0}

    def start_game(self):
        print("Welcome to Blackjack!\n")
        name = input("Please enter your name: ")
        self.player = Player(name)
        num_decks = int(input("How many decks would you like to use? "))
        self.deck.num_decks = num_decks
        while True:
            self.deck.build()
            self.deck.shuffle()
            self.play_round()
            self.display_results()
            if not self.play_again():
                break
        self.display_final_results()

    def play_round(self):
        print("\nStarting new round...")
        self.initial_deal()
        if self.player.hand.get_value() == 21:
            pass
        else:
            self.player_turn()
            # if self.player.hand.get_value() <= 21:
            self.dealer_turn()
        self.determine_winner()
        self.player.hand.clear_cards()
        self.dealer.hand.clear_cards()

    def initial_deal(self):
        # Clear hands before dealing new cards
        self.player.hand.clear_cards()
        self.dealer.hand.clear_cards()
        # Deal one card to the player
        card = self.deck.draw()
        self.player.hand.add_card(card)
        # Deal one card to the dealer (hidden)
        card = self.deck.draw()
        self.dealer.hand.add_card(card)
        # Deal one more card to the player
        card = self.deck.draw()
        self.player.hand.add_card(card)
        # Deal one more card to the dealer
        card = self.deck.draw()
        self.dealer.hand.add_card(card)
        self.show_initial_hands()

    def show_initial_hands(self):
        print(f"\n{self.player.name}'s Hand:")
        self.player.hand.show_hand()
        print(f"\nDealer's Hand:")
        self.dealer.hand.show_hand(hidden=True)

    def player_turn(self):
        if self.player.hand.get_value() == 21:
                print("Blackjack! You win!")
                return
        while True:
            if self.player.hand.get_value() == 21:
                print("Blackjack!")
                break
            action = input("Would you like to hit or stand? (h/s): ").lower()
            if action == 'h':
                self.hit(self.player)
                if self.player.hand.get_value() > 21:
                    print("Bust!")  #Dealer wins.
                    break
                elif len(self.player.hand.cards) == 5:
                    print("You have 5 cards. You can't hit again.")
                    break
            elif action == 's':
                break
            else:
                print("Invalid input. Please enter 'h' to hit or 's' to stand.")

    def hit(self, player):
        card = self.deck.draw()
        player.hand.add_card(card)
        print(f"\n{player.name} hits!")
        card.show_card()
        print(f"Total value of hand: {player.hand.get_value()}")

    def dealer_turn(self):
        print("\nDealer's Turn:")
        self.dealer.hand.show_hand()
        while self.dealer.hand.get_value() < 17:
            card = self.deck.draw()
            self.dealer.hand.add_card(card)
            card.show_card()
            print(f"Total value of dealer's hand: {self.dealer.hand.get_value()}")
        if self.dealer.hand.get_value() > 21:
            print("Dealer busts!")

    def determine_winner(self):
        player_score = self.player.hand.get_value()
        dealer_score = self.dealer.hand.get_value()
        if player_score > dealer_score and player_score <= 21 and dealer_score <= 21:
            print("You win!")
            self.total_score['Player'] += 1
        elif player_score <= 21 and dealer_score > 21:
            print("You win!")
            self.total_score['Player'] += 1
        elif player_score < dealer_score and dealer_score <= 21:
            print("Dealer wins!")
            self.total_score['Dealer'] += 1
        elif dealer_score <= 21 and player_score > 21:
            print("Dealer wins!")
            self.total_score['Dealer'] += 1
        elif player_score > 21 and dealer_score > 21:
            print("Dealer wins!")
            self.total_score['Dealer'] += 1
        else:
            print("It's a tie!")

    def play_again(self):
        while True:
            choice = input("\nWould you like to play again? (y/n): ").lower()
            if choice == 'y':
                return True
            elif choice == 'n':
                return False
            else:
                print("Invalid input. Please enter 'y' to play again or 'n' to quit.")

    def display_results(self):
        print("\nCurrent Results:")
        print(f"{self.player.name}: {self.total_score['Player']} wins")
        print(f"Dealer: {self.total_score['Dealer']} wins")


    def display_final_results(self):
        print("\nFinal Results:")
        print(f"{self.player.name}: {self.total_score['Player']} wins")
        print(f"Dealer: {self.total_score['Dealer']} wins")


# Start the game
blackjack_game = BlackJack()
blackjack_game.start_game()


