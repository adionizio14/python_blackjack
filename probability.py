from math import comb


def first_hand_blackjack(deck):
    """
    This function calculates the probability of getting a blackjack on the first hand
    of a game of blackjack. It is calculated by multiplying the number of ten value cards and the number of aces
    in the deck and dividing that by the total number of combinations of two cards in the deck.
    """
    ten_value_totals = deck[8] + deck[9] + deck[10] + deck[11]
    ace_value_totals = deck[12]

    ten_ace_prob = (ace_value_totals/sum(deck)) * (ten_value_totals/(sum(deck)-1))
    ace_ten_prob = (ten_value_totals/sum(deck)) * (ace_value_totals/(sum(deck)-1))

    return round((ten_ace_prob + ace_ten_prob) * 100, 2)


def good_initial_hand(deck):
    prob_blackjack = first_hand_blackjack(deck)
    prob_20 = first_hand_20(deck)
    prob_19 = first_hand_19(deck)
    prob_18 = first_hand_18(deck)

    return round(prob_blackjack + prob_20 + prob_19 + prob_18, 2)


def first_hand_20(deck):
    """
    This function calculates the probability of getting a 20 on the first hand of a game of blackjack.
    """

    ace_value_totals = deck[12]
    nine_value_totals = deck[7]
    ten_value_totals = deck[8] + deck[9] + deck[10] + deck[11]

    ace_nine_prob = (ace_value_totals/sum(deck)) * (nine_value_totals/(sum(deck)-1))
    nine_ace_prob = (nine_value_totals/sum(deck)) * (ace_value_totals/(sum(deck)-1))
    ten_ten_prob = (comb(ten_value_totals, 2)) / comb(sum(deck), 2)

    return round((ace_nine_prob + nine_ace_prob + ten_ten_prob) * 100, 2)


def first_hand_19(deck):
    """
    This function calculates the probability of getting a 19 on the first hand of a game of blackjack.
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
    This function calculates the probability of getting a 18 on the first hand of a game of blackjack.
    """

    ace_value_totals = deck[12]
    seven_value_totals = deck[5]
    eight_value_totals = deck[6]
    nine_value_totals = deck[7]
    ten_value_totals = deck[8] + deck[9] + deck[10] + deck[11]

    ace_seven_prob = (ace_value_totals / sum(deck)) * (seven_value_totals / (sum(deck) - 1))
    seven_ace_prob = (seven_value_totals / sum(deck)) * (ace_value_totals / (sum(deck) - 1))
    nine_eight_prob = (comb(nine_value_totals, 2)) / comb(sum(deck), 2)
    ten_eight_prob = (ten_value_totals / sum(deck)) * (eight_value_totals / (sum(deck) - 1))
    eight_ten_prob = (eight_value_totals / sum(deck)) * (ten_value_totals / (sum(deck) - 1))

    return round((ace_seven_prob + seven_ace_prob + nine_eight_prob + ten_eight_prob + eight_ten_prob) * 100, 2)

def blackjack(deck, player_total):
    """
    This function calculates the probability of getting a blackjack after the first hand has been dealt.
    """
    card_to_draw = 21 - player_total

    pass
