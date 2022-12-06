#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021
"""
import os
import hashlib


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


def input_file(filename):
    input_txt_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_txt_file, 'r') as input_filehandle:
        input_txt_list = input_filehandle.read().splitlines()

    for input_txt in input_txt_list:
        yield (input_txt)


if __name__ == '__main__':
    for secret_key in input_file('input.txt'):
        answer = solve(secret_key, 5)
        print(f"part01 - lowest_positive_number = {answer}")

        answer = solve(secret_key, 6)
        print(f"part02 - lowest_positive_number = {answer}")
