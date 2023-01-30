#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Solve Puzzle
"""
import os


def solve01(input_data):
    digit_sum = 0
    digit = input_data[-1]
    for digit_n in input_data:
        if digit == digit_n:
            digit_sum += int(digit_n)
        digit = digit_n
    return digit_sum


def solve02(input_data):
    digit_sum = 0
    idx = len(input_data) // 2
    for digit_n in input_data:
        if input_data[idx] == digit_n:
            digit_sum += int(digit_n)
        idx += 1
        if idx >= len(input_data):
            idx = 0
    return digit_sum


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as input_filehandle:
        input_data = input_filehandle.read()

    return input_data


def input_data_iter(input_data):
    for tc, input_data_tc in enumerate(input_data.splitlines()):
        yield tc, input_data_tc


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - captcha solution = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - captcha solution = {answer02}")
