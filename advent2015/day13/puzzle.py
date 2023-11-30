#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 Day 13: Knights of the Dinner Table
"""
import os
import re
import itertools

INPUT_REGEX = re.compile(r'(.*) would (gain|lose) (\d+) happiness units by sitting next to (.*)\.')


def solve01(input_data):
    guest_pref = input_data

    # create table layout permutations
    guests = list(set([x[0] for x in guest_pref]))
    table_size = len(guests)
    table_layouts = [list(g) for g in itertools.permutations(guests)]

    # calculate change in happines with each table layout permutation
    table_happiness = []
    for layout in table_layouts:
        change = 0
        for idx, guest in enumerate(layout):
            keyL = (guest, layout[(idx - 1)])
            keyR = (guest, layout[(idx + 1) % table_size])
            guest_change = guest_pref[keyL] + guest_pref[keyR]
            change += guest_change
        table_happiness.append(change)

    return max(table_happiness)


def solve02(input_data):
    guest_pref = input_data.copy()

    # add myself to guest list
    guests = list(set([x[0] for x in guest_pref]))
    for g in guests:
        guest_pref[('#me', g)] = 0
        guest_pref[(g, '#me')] = 0

    return solve01(guest_pref)


def parse_data(input_data):
    guest_pref = {}
    for line_text in input_data.splitlines():
        match_m = re.findall(INPUT_REGEX, line_text)[0]
        if match_m[1] == 'gain':
            happiness = int(match_m[2])
        else:
            happiness = int(match_m[2]) * -1
        guest_key = (match_m[0], match_m[3])
        guest_pref[guest_key] = happiness

    # guest preferences
    return guest_pref


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f'part01 - total change in happiness = {answer01}')

    answer02 = solve02(input_data)
    print(f'part02 - total change in happiness (with #me) = {answer02}')
