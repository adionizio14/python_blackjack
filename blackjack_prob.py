# Andrew Dionizio
# CSC 340 -

# python class called blackjack
from random import randint
import probability as prob


class Blackjack:

    def __init__(self):

        """
        This function initializes the game. It sets the dealer's and player's
        cards to None, and sets the deck strings and values. It also sets the
        deck count to 4 for each card.
        """

        self.dealer_cards = None
        self.player_cards = None
        self.player_total = 0
        self.dealer_total = 0
        self.deck_strings = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen",
                             "king", "ace"]
        self.deck_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        self.deck_count = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

    def start_game(self):

        """
        This function starts the game. It asks the player if they want to play,
        and if they do, it calls the deal_cards function. If they don't, it
        thanks them for playing and exits the program.
        """

        while True:

            print("Welcome to Blackjack!")
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

    def deal_cards(self):

        """
        This function deals the cards to the player and dealer, like a real
        game of blackjack, player first, then dealer. It then calls the player's turn.
        """
        # check if the deck is empty
        print(self.deck_count)
        if sum(self.deck_count) == 0:
            print("The deck is empty. Please restart the game.")
            return
        self.player_cards = []
        self.dealer_cards = []
        self.player_cards.append(self.draw_card())
        self.dealer_cards.append(self.draw_card())
        self.player_cards.append(self.draw_card())
        self.dealer_cards.append(self.draw_card())
        self.check_for_ace_and_adjust(self.player_cards, self.player_total)
        self.check_for_ace_and_adjust(self.dealer_cards, self.dealer_total)
        self.print_player_cards()
        self.print_dealer_cards()
        self.player_turn()

    @staticmethod
    def check_for_ace_and_adjust(cards, total):

        """
        Check if the player has an Ace and is over 21. If true, adjust the value of the Ace to 1.
        """
        if 12 in cards:
            print("Ace found")
            if total > 21:
                total -= 10

    def draw_card(self):

        """
        This function draws a card from the deck and returns its value
        """

        while True:
            card_index = randint(0, 12)
            if self.deck_count[card_index] > 0:
                self.deck_count[card_index] -= 1
                return card_index
            else:
                self.draw_card()

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
        If the player stands, it is the dealer's turn.
        """

        while True:

            print("Would you like to hit or stand? (h/s)")

            prob.blackjack(self.deck_count, self.player_total)

            choice = input()
            print()

            if self.player_total == 21:
                self.dealer_turn()

            if choice == "h":
                self.player_cards.append(self.draw_card())
                self.check_for_ace_and_adjust(self.player_cards, self.player_total)
                self.print_player_cards()
                if self.player_total > 21:
                    print("You lose!")
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
                self.check_for_ace_and_adjust(self.dealer_cards, self.dealer_total)
                self.print_dealer_cards_on_turn()
                if self.dealer_total > 21:
                    print("You win!")
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
        elif self.player_total < self.dealer_total:
            print("You lose!")
        else:
            print("You push")

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
        print()
        play = input()
        print()
        if play == "y":
            self.deal_cards()
        elif play == "n":
            print("Thanks for playing!")
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


game = Blackjack()
game.start_game()
