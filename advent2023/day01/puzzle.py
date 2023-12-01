#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 01: Trebuchet?!
"""
import os
import re

NUM_WORDS = {
    'one': 'one1one',
    'two': 'two2two',
    'three': 'three3three',
    'four': 'four4four',
    'five': 'five5',
    'six': 'six6six',
    'seven': 'seven7seven',
    'eight': 'eight8eight',
    'nine': 'nine9nine',
}


def solve01(input_text):
    calibration_list = []

    for input_line in input_text.splitlines():
        c_numbers = re.findall(r'\d', input_line)
        calibiration = c_numbers[0] + c_numbers[-1]
        calibration_list.append(int(calibiration))

    return sum(calibration_list)


def solve02(input_text):
    # replace all numers
    for word, word_r in NUM_WORDS.items():
        input_text = input_text.replace(word, word_r)

    return solve01(input_text)


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return input_data


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f'part01 - calibration values sum = {answer01}')

    answer02 = solve02(input_data)
    print(f'part02 - calibration values sum = {answer02}')
