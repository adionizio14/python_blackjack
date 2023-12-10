from math import comb


def first_hand_blackjack(deck):
    """
    This function calculates the probability of getting a blackjack on the first hand
    of a game of blackjack. It is calculated by adding the probabilities of all the different combinations to get
    a blackjack on the first hand.
    """
    ten_value_totals = deck[8] + deck[9] + deck[10] + deck[11]
    ace_value_totals = deck[12]

    ten_ace_prob = (ace_value_totals / sum(deck)) * (ten_value_totals / (sum(deck) - 1))
    ace_ten_prob = (ten_value_totals / sum(deck)) * (ace_value_totals / (sum(deck) - 1))

    return round((ten_ace_prob + ace_ten_prob) * 100, 2)


def good_initial_hand(deck):
    """
    This function calculates the probability of getting a good initial hand on the first hand of a game of blackjack.
    A good initial hand is defined as a hand with a value of 18 or higher.
    """
    prob_blackjack = first_hand_blackjack(deck)
    prob_20 = first_hand_20(deck)
    prob_19 = first_hand_19(deck)
    prob_18 = first_hand_18(deck)

    return round(prob_blackjack + prob_20 + prob_19 + prob_18, 2)


def first_hand_20(deck):
    """
    This function calculates the probability of getting a 20 on the first hand of a game of blackjack. It is calculated
    by adding the different probabilities of the all the different combinations to get a 20 on the first hand.
    """

    ace_value_totals = deck[12]
    nine_value_totals = deck[7]
    ten_value_totals = deck[8] + deck[9] + deck[10] + deck[11]

    ace_nine_prob = (ace_value_totals / sum(deck)) * (nine_value_totals / (sum(deck) - 1))
    nine_ace_prob = (nine_value_totals / sum(deck)) * (ace_value_totals / (sum(deck) - 1))
    ten_ten_prob = (comb(ten_value_totals, 2)) / comb(sum(deck), 2)

    return round((ace_nine_prob + nine_ace_prob + ten_ten_prob) * 100, 2)


def first_hand_19(deck):
    """
    This function calculates the probability of getting a 19 on the first hand of a game of blackjack. It is calculated
    by adding the different probabilities of the all the different combinations to get a 19 on the first hand.
    """
    ace_value_totals = deck[12]
    eight_value_totals = deck[6]
    nine_value_totals = deck[7]
    ten_value_totals = deck[8] + deck[9] + deck[10] + deck[11]

    ace_eight_prob = (ace_value_totals / sum(deck)) * (eight_value_totals / (sum(deck) - 1))
    eight_ace_prob = (eight_value_totals / sum(deck)) * (ace_value_totals / (sum(deck) - 1))
    nine_ten_prob = (nine_value_totals / sum(deck)) * (ten_value_totals / (sum(deck) - 1))
    ten_nine_prob = (ten_value_totals / sum(deck)) * (nine_value_totals / (sum(deck) - 1))

    return round((ace_eight_prob + eight_ace_prob + nine_ten_prob + ten_nine_prob) * 100, 2)


def first_hand_18(deck):
    """
    This function calculates the probability of getting a 18 on the first hand of a game of blackjack. It is calculated
    by adding the different probabilities of the all the different combinations to get a 18 on the first hand.
    """

    ace_value_totals = deck[12]
    seven_value_totals = deck[5]
    eight_value_totals = deck[6]
    nine_value_totals = deck[7]
    ten_value_totals = deck[8] + deck[9] + deck[10] + deck[11]

    ace_seven_prob = (ace_value_totals / sum(deck)) * (seven_value_totals / (sum(deck) - 1))
    seven_ace_prob = (seven_value_totals / sum(deck)) * (ace_value_totals / (sum(deck) - 1))
    nine_nine_prob = (comb(nine_value_totals, 2)) / comb(sum(deck), 2)
    ten_eight_prob = (ten_value_totals / sum(deck)) * (eight_value_totals / (sum(deck) - 1))
    eight_ten_prob = (eight_value_totals / sum(deck)) * (ten_value_totals / (sum(deck) - 1))

    return round((ace_seven_prob + seven_ace_prob + nine_nine_prob + ten_eight_prob + eight_ten_prob) * 100, 2)


def blackjack(deck, player_total, deck_values, num_decks):
    """
    This function calculates the probability of getting a blackjack after the first hand has been dealt. It is
    calculated by first getting the card needed to get a blackjack, then calculating the probability of getting it
    using the prob_of_certain_card function.
    """
    card_to_draw = 21 - player_total

    if card_to_draw > 11:
        print("There is no card in the deck that can give you a blackjack")
        return
    elif card_to_draw == 1:
        card_to_draw = 11

    prob = prob_of_certain_card(deck, card_to_draw, deck_values, num_decks)

    print("The probability of getting a blackjack if you hit is: " + str(round(prob * 100, 2)) + "%")


def prob_of_certain_card(deck, card_to_draw, deck_values, num_decks):
    """
    this function calculates the probability of drawing a certain card from the deck. It is calculated by dividing the
    number of cards of that type in the deck by the total number of cards in the deck. Depending on the card, the
    probability is calculated differently.
    """
    ten_value_totals = deck[8] + deck[9] + deck[10] + deck[11]
    index = 0
    for i in range(0, len(deck_values)):
        if deck_values[i] == card_to_draw:
            index = i
            break

    num_total_cards_drawn = (52 * num_decks) - sum(deck)
    num_card_needed_drawn = (4 * num_decks) - deck[index]
    num_10_drawn = (16 * num_decks) - ten_value_totals

    if card_to_draw == 10:
        prob = ((16 * num_decks) - num_10_drawn) / ((52 * num_decks) - num_total_cards_drawn)
    else:
        prob = ((4 * num_decks) - num_card_needed_drawn) / ((52 * num_decks) - num_total_cards_drawn)

    return prob


def good_hand(deck, player_total, deck_values, num_decks):
    """
    This function calculates the probability of getting a good hand after the first hand has been dealt. It is
    calculated by first getting the cards needed to get a good hand in an array,
    then calculating the probability of getting them
    """
    if player_total >= 18:
        print("You already have a good hand")
        return

    cards_to_draw = [18 - player_total, 19 - player_total, 20 - player_total, 21 - player_total]
    total_prob = 0

    for card in cards_to_draw:
        if card > 11:
            continue
        elif card == 1:
            card = 11

        prob = prob_of_certain_card(deck, card, deck_values, num_decks)
        total_prob += prob

    print("The probability of getting a good hand if you hit is: " + str(round(total_prob * 100, 2)) + "%")


def over_21(deck, player_total, deck_values, num_decks):
    """
    This function calculates the probability of going over 21 after the first hand has been dealt. It is
    calculated by first getting the cards needed to go over 21 in an array,
    then calculating the probability of getting them using the prob_of_certain_card function.
    """

    if player_total <= 11:
        print("You are safe from going over 21")
        return

    over = 21 - player_total
    over_list = []

    for i in range(2, 11):
        if i > over:
            over_list.append(i)

    total_prob = 0
    for card in over_list:
        prob = prob_of_certain_card(deck, card, deck_values, num_decks)
        total_prob += prob

    print("The probability of going over 21 if you hit is: " + str(round(total_prob * 100, 2)) + "%")
