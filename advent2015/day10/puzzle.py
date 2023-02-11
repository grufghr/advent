#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 Day 10: Elves Look, Elves Say
"""
import os
import re

LS_REGEX = re.compile(r'(1+|2+|3+|4+|5+|6+|7+|8+|9+|0+)')


def solve01(input_data):
    number = input_data
    for step in range(0, 40):
        number_n = ''
        for match in LS_REGEX.findall(number):
            seq = str(len(match)) + match[0]
            number_n = number_n + seq
        number = number_n
    return len(number)


def solve02(input_data):
    number = input_data
    for step in range(0, 50):
        number_n = ''
        for match in LS_REGEX.findall(number):
            seq = str(len(match)) + match[0]
            number_n = number_n + seq
        number = number_n
    return len(number)


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, 'r') as input_filehandle:
        input_data_text = input_filehandle.read()

    return input_data_text


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - look-and-say after 40 iteratons = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - look-and-say after 50 iteratons = {answer02}")
