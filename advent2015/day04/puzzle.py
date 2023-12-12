#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 Day 04: The Ideal Stocking Stuffer
"""
import os
import hashlib


def part01(input_data):
    answer = solve(input_data, 5)
    return answer


def part02(input_data):
    answer = solve(input_data, 6)
    return answer


def solve(input_text, n):
    n_zeroes = '0' * n

    for n in range(100000000):
        text = input_text + str(n)
        hash_text = str(hashlib.md5(text.encode('utf-8')).hexdigest())
        if hash_text.startswith(n_zeroes):
            break
    return n


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return input_data


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - lowest_positive_number = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - lowest_positive_number = {answer02}')
