def get_rounds(number):
    return [number,number+1,number+2]


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    if number in rounds:
        return True
    return False
    


def card_average(hand):
    result = 0
    counter = 0
    for i in hand:
        result = result + i
        counter = counter + 1
    return (result/counter)


def approx_average_is_average(hand):
    average_like = (hand[0] + hand[-1])/2
    median = hand[int(len(hand)/2 - 0.5)]
    if average_like == card_average(hand) or median == card_average(hand):
        return True
    return False


def average_even_is_average_odd(hand):
    average_even = 0 
    average_odd = 0
    counter_even = 0
    counter_odd = 0
    for i in range(len(hand)):
        if i%2 == 0 :
            average_even = average_even + hand[i]
            counter_even = counter_even + 1
        else : 
            average_odd = average_odd + hand[i]
            counter_odd = counter_odd + 1
    average_even = average_even / counter_even
    average_odd = average_odd / counter_odd
    if average_even == average_odd :
        return True
    return False


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
