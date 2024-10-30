#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2020 Day 06: Custom Customs
"""

import os


def part01(input_data):
    # part 01 - sum of counts for ANY questions answered yes
    count_list = []
    for group in input_data:
        yes = get_yes_set(group)
        count_list.append(len(yes))

    return sum(count_list)


def part02(input_data):
    # part 02 - sum of counts for ALL questions answered yes
    count_list = []
    for group in input_data:
        yes = get_yes_set(group)
        for person in group:
            ans = set(list(person))
            yes = yes.intersection(ans)
            if len(yes) == 0:
                break
        count_list.append(len(yes))
    return sum(count_list)


def get_yes_set(group):
    ans = [list(person) for person in group]
    # flatten list of list into set
    yes = set([x for xs in ans for x in xs])
    return yes


def parse_data(input_data):
    group_data = [g.split('\n') for g in input_data.split('\n\n')]
    return group_data


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - sum of counts = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - tbc = {answer02}')
