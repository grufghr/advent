#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Solve Puzzle 2020 Day 01: Report Repair
"""
import os
from itertools import product


def solve01(input_data):
    # part 01 - find the 2 entries that sum to 2020
    # pairs = [(x, y) for x, y in product(input_data, repeat=2) if x + y == 2020]
    for a, b in product(input_data, repeat=2):
        if a + b == 2020:
            return a * b
    return None


def solve02(input_data):
    # part 02 - find the 3 entries that sum to 2020
    for a, b, c in product(input_data, repeat=3):
        if a + b + c == 2020:
            return a * b * c
    return None


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as input_filehandle:
        input_data_text_list = input_filehandle.readlines()

    input_data = [int(x) for x in input_data_text_list]
    return input_data


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - product of 2 entries sum to 2020 = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - product of 3 entries sum to 2020 = {answer02}")
