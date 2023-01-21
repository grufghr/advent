#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021
"""
import os
import math


def solve01(input_data):
    def calc_cost(x, i):
        return abs(x - i)

    return solve(input_data, calc_cost)


def solve02(input_data):
    def calc_cost(x, i):
        n = abs(x - i)
        return int((n * (n + 1)) / 2)
    return solve(input_data, calc_cost)


def solve(pos_list, cost_func):

    # part 01 - find best position
    s = min(pos_list)
    e = max(pos_list) + 1
    min_cost = math.inf
    for i in range(s, e):
        diff = [cost_func(x, i) for x in pos_list]
        cost = sum(diff)
        min_cost = min(min_cost, cost)

    return min_cost


def parse_data(input_data):
    pos_text_list = list(input_data.split(","))
    pos_list = list(map(int, pos_text_list))
    return pos_list


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = input_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - least fuel to align = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - least fuel to align = {answer02}")
