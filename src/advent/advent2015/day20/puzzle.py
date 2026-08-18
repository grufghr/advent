"""
Advent of Code 2015 Day 20: Infinite Elves and Infinite Houses
"""

import os
from math import sqrt


def part01(input_data):
    presents = input_data

    h = 1
    while factor_sum01(h) < presents:
        h += 1

    return h


def part02(input_data):
    presents = input_data

    h = 1
    while factor_sum02(h) < presents:
        h += 1

    return h


def factor_sum01(n):
    # step reduces number of checks in list comphrehension for even numbers
    step = 2 if n % 2 else 1
    # find factors of N -> [(1, N), ....]
    f_list = [n // i for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0]
    # sum list (* 10)
    ps = sum(f_list) * 10
    return ps


def factor_sum02(n):
    # find factors of N -> [(1, N), ....]
    f_list = [n // i for i in range(1, 51) if n % i == 0]
    # sum list (* 11)
    ps = sum(f_list) * 11
    return ps


def parse_data(input_data):
    return int(input_data)


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 answer = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 answer = {answer02}')
