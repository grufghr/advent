#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2020 Day 02: Password Philosophy
"""
import os
import re


POLICY_REGEX = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]*)")


def solve01(input_data):
    # part 01 - count valid lines
    valid_tot = 0
    for line in input_data:
        regex_match = POLICY_REGEX.search(line)
        min_count, max_count, letter, pwd = regex_match.groups()

        c = pwd.count(letter)
        if c >= int(min_count) and c <= int(max_count):
            valid_tot += 1

    return valid_tot


def solve02(input_data):
    # part 02 - count valid lines
    valid_tot = 0
    for line in input_data:
        regex_match = POLICY_REGEX.search(line)
        pos_a, pos_b, letter, pwd = regex_match.groups()

        a = (pwd[int(pos_a) - 1] == letter)
        b = (pwd[int(pos_b) - 1] == letter)
        if (a and not b) or (not a and b):
            valid_tot += 1

    return valid_tot


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as input_filehandle:
        input_data = input_filehandle.read().splitlines()

    return input_data


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - valid lines = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - valid lines = {answer02}")
