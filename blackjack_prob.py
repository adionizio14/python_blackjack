# python class called blackjack
from random import randint


class Blackjack:

    def __init__(self):

        # All the deck values, strings, and counts
        self.dealer_cards = None
        self.player_cards = None
        self.deck_strings = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen",
                             "king", "ace"]
        self.deck_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        self.deck_count = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

    def start_game(self):
        # This is the main game loop
        while True:
            # This is the main game loop
            print("Welcome to Blackjack!")
            print("Would you like to play? (y/n)")
            play = input()
            print()
            if play == "y":
                self.deal_cards()
            elif play == "n":
                print("Thanks for playing!")
                break
            else:
                print("Invalid input, please try again.")
            print()

    def deal_cards(self):
        # This function deals the cards to the player and dealer
        self.player_cards = []
        self.dealer_cards = []
        self.player_cards.append(self.draw_card())
        self.dealer_cards.append(self.draw_card())
        self.player_cards.append(self.draw_card())
        self.dealer_cards.append(self.draw_card())
        self.print_player_cards()
        self.print_dealer_cards()
        self.player_turn()

    def draw_card(self):
        # This function draws a card from the deck
        while True:
            card = randint(0, 12)
            if self.deck_count[card] > 0:
                self.deck_count[card] -= 1
                return self.deck_values[card]

    def print_player_cards(self):
        # This function prints the cards in the player's handy
        print("Your cards are:")
        for card in self.player_cards:
            print(self.deck_strings[self.deck_values.index(card)], end=" ")
        print()
        print("Your total is: " + str(sum(self.player_cards)))
        print()

    def print_dealer_cards(self):
        # This function prints the cards in the dealer's hand
        print("The dealer's cards are:")
        print(self.deck_strings[self.deck_values.index(self.dealer_cards[0])], end=" ")
        print("hidden")
        print()

    def player_turn(self):
        # This function is the player's turn
        while True:
            print("Would you like to hit or stand? (h/s)")
            choice = input()
            print()
            if choice == "h":
                self.player_cards.append(self.draw_card())
                self.print_player_cards()
                if sum(self.player_cards) > 21:
                    self.lose()
                    break
            elif choice == "s":
                self.dealer_turn()
                print("Dealer turn")
                break
            else:
                print("Invalid input, please try again.")
            print()

    def lose(self):
        # This function is called when the player loses
        print("You lose!")
        print()

        print("Would you like to play again? (y/n)")
        play = input()
        print()
        if play == "y":
            self.deal_cards()
        elif play == "n":
            print("Thanks for playing!")
        else:
            print("Invalid input, please try again.")

    def dealer_turn(self):
        # This function is the dealer's turn
        self.print_dealer_cards_on_turn()
        while True:
            if sum(self.dealer_cards) < 17:
                self.dealer_cards.append(self.draw_card())
                self.print_dealer_cards_on_turn()
                if sum(self.dealer_cards) > 21:
                    self.win()
                    break
            else:
                self.compare()
                break

    def print_dealer_cards_on_turn(self):
        # This function prints the cards in the dealer's hand
        print("The dealer's cards are:")
        for card in self.dealer_cards:
            print(self.deck_strings[self.deck_values.index(card)], end=" ")
        print()
        print("The dealer's total is: " + str(sum(self.dealer_cards)))
        print()

    def win(self):
        # This function is called when the player wins
        print("You win!")
        print()

        print("Would you like to play again? (y/n)")
        play = input()
        print()
        if play == "y":
            self.deal_cards()
        elif play == "n":
            print("Thanks for playing!")
        else:
            print("Invalid input, please try again.")

    def compare(self):
        # This function compares the player's and dealer's hands
        if sum(self.player_cards) > sum(self.dealer_cards):
            self.win()
        elif sum(self.player_cards) < sum(self.dealer_cards):
            self.lose()
        else:
            self.tie()

    def tie(self):
        # This function is called when the player and dealer tie
        print("You pushed!")
        print()

        print("Would you like to play again? (y/n)")
        play = input()
        print()
        if play == "y":
            self.deal_cards()
        elif play == "n":
            print("Thanks for playing!")
        else:
            print("Invalid input, please try again.")


game = Blackjack()
game.start_game()
