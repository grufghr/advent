#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 Day 17: No Such Thing as Too Much
"""

import os
import itertools

EGGNOG_TOTAL = 150


def part01(input_data):
    container_list = input_data

    total_count = 0
    for L in range(1, len(container_list) + 1):
        combs = list(itertools.combinations(container_list, L))
        combs_size = list(map(sum, combs))
        count = combs_size.count(EGGNOG_TOTAL)
        total_count += count

    return total_count


def part02(input_data):
    container_list = input_data

    for L in range(1, len(container_list) + 1):
        combs = list(itertools.combinations(container_list, L))
        combs_size = list(map(sum, combs))
        count = combs_size.count(EGGNOG_TOTAL)
        if count > 0:
            break
    return count


def parse_data(input_data):
    container_list = [int(size) for size in input_data.splitlines()]
    return container_list


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input_example.txt')

    answer01 = part01(input_data)
    print(f'part01 answer = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 answer = {answer02}')
