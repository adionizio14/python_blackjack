# Andrew Dionizio
# CSC 340 Applied Combinatorics
# 12/15/2023

"""
Problem Statement:
Develop an interactive and informative Blackjack application that not only allows users to play the popular casino
card game with customizable deck options but also provides real-time probability assessments at crucial stages of the
game. The application should give the player accurate probabilities for specific outcomes, including the likelihood
of obtaining a perfect hand (21) or a favorable hand (18-21) before the initial deal. After the cards are dealt,
it would also give the chances of getting 21, going over 21 or getting a favorable hand (18-21) if the user decides
to hit. The goal is to create a program using topics we went over in class while also combining it with a real-world
application, like a casino game. This program was designed primarily to showcase the math included and not the actual
blackjack gameplay. In a regular game, the user does not have access to the cards and their counts. For example,
when the cards are dealt the dealer has a “hidden” card, but when we calculate the probability, that card is taken
into account.
"""

import sys
from random import randint
import probability as prob


# python class called blackjack
class Blackjack:

    def __init__(self, num_decks):

        """
        This function initializes the game. It sets the dealer's and player's
        cards to None, and sets the deck strings and values. It also sets the
        deck count to 4 for each card.
        """

        self.dealer_cards = None
        self.player_cards = None
        self.player_total = 0
        self.dealer_total = 0
        self.tie_total = 0
        self.win_total = 0
        self.lost_total = 0
        self.num_decks = num_decks
        self.deck_strings = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen",
                             "king", "ace"]
        self.deck_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        self.deck_count = []

    def start_game(self):

        """
        This function starts the game. It asks the player if they want to play,
        and if they do, it calls the deal_cards function. If they don't, it
        thanks them for playing and exits the program.
        """

        self.fill_deck()

        while True:

            print()
            print("Welcome to Blackjack!")
            print("You are playing with " + str(self.num_decks) + " deck(s).")
            print()
            self.print_starting_probabilities()
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

    def fill_deck(self):
        """
        This function fills the deck with the correct number of cards based on the number of decks
        """
        self.deck_count = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        for i in range(0, 13):
            self.deck_count[i] = self.num_decks * 4

    def deal_cards(self):

        """
        This function deals the cards to the player and dealer, like a real
        game of blackjack, player first, then dealer. It then calls the player's turn. Before
        dealing the cards, it checks if the deck has been used more than 70% and if it has, it shuffles the deck.
        """
        self.check_deck()
        self.player_cards = []
        self.dealer_cards = []
        self.player_cards.append(self.draw_card())
        self.dealer_cards.append(self.draw_card())
        self.player_cards.append(self.draw_card())
        self.dealer_cards.append(self.draw_card())
        self.print_player_cards()
        self.print_dealer_cards()
        self.player_turn()

    def check_deck(self):
        """
        This function checks if the deck has been used more than 70% and if it has, it shuffles the deck
        """

        total_start_cards = 52 * self.num_decks
        cards_dealt = total_start_cards - sum(self.deck_count)

        if cards_dealt >= (total_start_cards * 0.7):
            print("Shuffling deck...")
            self.fill_deck()

    @staticmethod
    def check_for_ace_and_adjust(cards, total):

        """
        Check if the player has an Ace and is over 21. If true, adjust the value of the Ace to 1.
        """
        if 12 in cards and total > 21:
            print("Ace found")
            total -= 10

        return total

    def draw_card(self):

        """
        This function draws a random card from the deck that still has cards left and returns its value
        """

        non_zero_totals = []
        for i in range(0, len(self.deck_count)):
            if self.deck_count[i] > 0:
                non_zero_totals.append(i)

        card_index = non_zero_totals[randint(0, len(non_zero_totals) - 1)]

        self.deck_count[card_index] -= 1

        return card_index

    def print_player_cards(self):

        """
        This function prints the cards in the player's hand
        """

        print("Your cards are:")
        self.player_total = 0
        for card in self.player_cards:
            print(self.deck_strings[card], end=" ")
            self.player_total += self.deck_values[card]
        print()
        self.player_total = self.check_for_ace_and_adjust(self.player_cards, self.player_total)
        print("Your total is: " + str(self.player_total))
        print()

    def print_dealer_cards(self):

        """
        This function prints the dealer's cards. The second card is hidden.
        """

        print("The dealer's cards are:")
        print(self.deck_strings[self.dealer_cards[0]], end=" ")
        print("hidden")
        print()

    def player_turn(self):

        """
        This function is the player's turn. The player can hit or stand.
        If the player hits, they draw a card and their hand is printed.
        If the player stands, it is the dealer's turn. It also prints the
        probabilities of getting a blackjack or good hand if the player hits.
        """

        while True:

            if self.player_total == 21:
                self.dealer_turn()

            prob.blackjack(self.deck_count, self.player_total, self.deck_values, self.num_decks)
            prob.good_hand(self.deck_count, self.player_total, self.deck_values, self.num_decks)
            prob.over_21(self.deck_count, self.player_total, self.deck_values, self.num_decks)
            print()

            print("Would you like to hit or stand? (h/s)")

            choice = input()
            print()

            if choice == "h":
                self.player_cards.append(self.draw_card())
                self.print_player_cards()
                if self.player_total > 21:
                    print("You lose!")
                    self.lost_total += 1
                    self.end_prompt()
                    break
                elif self.player_total == 21:
                    self.dealer_turn()
            elif choice == "s":
                self.dealer_turn()
                print("Dealer turn")
                break
            else:
                print("Invalid input, please try again.")
            print()

    def dealer_turn(self):

        """
        This function is the dealer's turn. The dealer will hit until their hand
        is greater than or equal to 17. If the dealer busts, the player wins.
        If the dealer's hand is greater than or equal to 17, the compare function
        is called.
        """

        self.print_dealer_cards_on_turn()
        while True:
            if self.dealer_total < 17:
                self.dealer_cards.append(self.draw_card())
                self.print_dealer_cards_on_turn()
                if self.dealer_total > 21:
                    print("You win!")
                    self.win_total += 1
                    self.end_prompt()
                    break
            else:
                self.compare()
                break

    def print_dealer_cards_on_turn(self):

        """
        This function prints the dealer's cards during their turn. The hidden card is
        revealed. And the dealer's total is printed.
        """

        print("The dealer's cards are:")
        self.dealer_total = 0
        for card in self.dealer_cards:
            print(self.deck_strings[card], end=" ")
            self.dealer_total += self.deck_values[card]
        print()
        self.dealer_total = self.check_for_ace_and_adjust(self.dealer_cards, self.dealer_total)
        print("The dealer's total is: " + str(self.dealer_total))
        print()

    def compare(self):

        """
        This function compares the player's and dealer's hands and determines
        who wins. If the player's hand is greater than the dealer's, the player
        wins. If the dealer's hand is greater than the player's, the dealer wins.
        If the hands are equal, the player and dealer tie.
        """

        if self.player_total > self.dealer_total:
            print("You win!")
            self.win_total += 1
        elif self.player_total < self.dealer_total:
            print("You lose!")
            self.lost_total += 1
        else:
            print("You push")
            self.tie_total += 1

        self.end_prompt()

    def end_prompt(self):

        """
        This function is called when the game is over. It asks the player
        if they want to play again. If they do, the deal_cards function is called.
        The deck is not reset, so the cards that were drawn are not put back in
        the deck.
        """

        print()
        self.print_starting_probabilities()
        print("Would you like to play again? (y/n)")
        print("Wins: " + str(self.win_total) + " Losses: " + str(self.lost_total) + " Ties: " + str(self.tie_total))
        print()
        play = input()
        print()
        if play == "y":
            self.deal_cards()
        elif play == "n":
            print("Thanks for playing!")
            exit(1)
        else:
            print("Invalid input, please try again.")

    def print_starting_probabilities(self):
        """
        This function prints the probabilities of getting a blackjack on the first hand and a good initial hand
        """
        blackjack = prob.first_hand_blackjack(self.deck_count)
        initial_hand = prob.good_initial_hand(self.deck_count)
        print("The probability of getting a blackjack on the first hand is: " + str(blackjack) + "%")
        print("The probability of getting a good initial hand is: " + str(initial_hand) + "%")
        print()


decks = int(sys.argv[1])
game = Blackjack(decks)
game.start_game()
