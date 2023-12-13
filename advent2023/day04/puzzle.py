#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 04: Scratchcards
"""
import os
import re
import math
from collections import deque


def part01(input_data):
    card_list = input_data
    
    # calcuate total points on all cards
    total_points = 0
    for c, card, winning_nums in card_list:
        matches = len(winning_nums & card) - 1
        total_points += int(math.pow(2, matches))

    return total_points


def part02(input_data):
    card_list = input_data

    # calcuate number of cards at end (count)
    q = deque(card_list)
    count = 0
    while q and count < 10000000:
        c, card, winning_nums = q.pop()
        count += 1
        matches = len(winning_nums & card)
        # win number of cards matching
        if matches >= 1:
            q.extend(card_list[c : c + matches])
    return count


def parse_data(input_data):
    scratch_cards = []
    for line_text in input_data.splitlines():
        # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        line_items = re.split(':|\|', line_text)
        c = int(re.findall(r'(\d+)', line_items[0])[0])
        winning_nums = set(map(int, re.findall(r'(\d+)', line_items[1])))
        card = set(map(int, re.findall(r'(\d+)', line_items[2])))
        scratch_cards.append((c, card, winning_nums))
    return scratch_cards


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - total points = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - total scratchcards = {answer02}')
