#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 Day 04: The Ideal Stocking Stuffer
"""
import os
import hashlib


def solve01(input_data):
    answer = solve(input_data, 5)
    return answer


def solve02(input_data):
    answer = solve(input_data, 6)
    return answer


def solve(input_text, n):
    lowest_positive_number = 0
    n_zeroes = '0' * n

    found = False
    while (not found) and (lowest_positive_number < 99999999):
        lowest_positive_number += 1

        text = input_text + str(lowest_positive_number)

        hash_text = str(hashlib.md5(text.encode('utf-8')).hexdigest())
        if (hash_text.startswith(n_zeroes)):
            found = True

    return lowest_positive_number


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return input_data


def input_data_iter(input_data):
    for tc, input_data_tc in enumerate(input_data.splitlines()):
        yield tc, input_data_tc


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - lowest_positive_number = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - lowest_positive_number = {answer02}")
