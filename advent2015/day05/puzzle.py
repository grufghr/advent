#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015
"""
import os

VOWELS = 'aeiou'
PAIR_LIST = ['ab', 'cd', 'pq', 'xy']


def solve_part01(input_data_list):
    nice_count = 0

    for text in input_data_list:
        # rule 1 - vowels_count >= 3
        vowel_count = len([c for c in text if c in VOWELS])
        # rule 2 - duplicate pairs (e.g. aa, bb, cc)
        has_duplicate = False
        for i in range(1, len(text)):
            p = i - 1
            if text[p] == text[i]:
                has_duplicate = True
                break
        # rule 3 - contains pair from exlude PAIR_LIST
        has_pair = False
        for pair in PAIR_LIST:
            if pair in text:
                has_pair = True
                break

        if (vowel_count >= 3) and has_duplicate and not has_pair:
            nice_count += 1

    return nice_count


def solve_part02(input_data_list):
    nice_count = 0

    for text in input_data_list:

        # rule 1 - non-overlapping duplicate pairs (e.g. ...xy...xy...), but not 'aaa'
        has_duplicate = False
        for i in range(1, len(text)):
            dup = text[(i - 1):(i + 1)]
            if text.find(dup, (i + 1)) > 0:
                has_duplicate = True
                break

        # rule 2 - has 'repeater' (xyx, efe, aaa, etc.)
        has_repeater = False
        for i in range(2, len(text)):
            p = i - 2
            if text[p] == text[i]:
                has_repeater = True
                break

        if has_duplicate and has_repeater:
            nice_count += 1

    return nice_count


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, 'r') as filehandle:
        input_data_list = filehandle.readlines()

    return input_data_list


if __name__ == '__main__':
    input_data = input_data('input.txt')

    answer = solve_part01(input_data)
    print(f"part01 - Nice string count = {answer}")

    answer = solve_part02(input_data)
    print(f"part02 - Nice string count = {answer}")
