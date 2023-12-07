#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 06: Wait For It
"""
import os
from collections import Counter
from functools import cmp_to_key

CARD_VALUES = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}


def solve01(input_data):
    total_winnings = solve(input_data, False)
    return total_winnings


def solve02(input_data):
    # replace Joker value
    CARD_VALUES['J'] = 0

    total_winnings = solve(input_data, True)
    return total_winnings


def solve(hand_list, wildcard):
    hand_type_list = []
    for hand, bid in hand_list:
        strength = calc_strength(hand, wildcard)
        hand_type_list.append((strength, hand, bid))

    hand_list_sorted = sorted(hand_type_list, key=cmp_to_key(hand_compare))

    total_winnings = 0
    for rank, x in enumerate(hand_list_sorted):
        total_winnings += x[2] * (rank + 1)

    return total_winnings


def calc_strength(hand, wildcard):
    if not wildcard or 'J' not in hand:
        return calc_hand(hand)

    best_type = calc_hand(hand)
    # find better type hand with Joker wildcards
    for wc in CARD_VALUES.keys():
        hand_n = hand.replace('J', wc)
        hand_type = calc_hand(hand_n)
        if hand_type > best_type:
            best_type = hand_type

    return best_type


def calc_hand(hand):
    count_dict = Counter(hand)
    count = list(count_dict.values())

    # Five of a kind
    if 5 in count:
        return 7
    # Four of a kind
    if 4 in count:
        return 6
    # Full House
    if all(x in count for x in [2, 3]):
        return 5
    # Three of a kind
    if 3 in count:
        return 4
    if 2 in count:
        # Two pair
        if count.count(2) == 2:
            return 3
        # One pair
        else:
            return 2
    # High card
    return 1


def hand_compare(a, b):
    # compare tuple (strength:int, hand:str)
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    else:
        list_a = [CARD_VALUES[x] for x in a[1]]
        list_b = [CARD_VALUES[x] for x in b[1]]
        for i, j in zip(list_a, list_b):
            if i < j:
                return -1
            elif i > j:
                return 1
    return 0


def parse_data(input_data):
    hand_list = []
    for line_text in input_data.splitlines():
        hand, bid = tuple(line_text.split(' '))
        hand_list.append((hand, int(bid)))

    return hand_list


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f'part01 - total winnings = {answer01}')

    answer02 = solve02(input_data)
    print(f'part02 - total winnings (wildcards) = {answer02}')
