#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 03: Gear Ratios
"""
import os
import re
import math


def solve01(schematic):
    # create coords of symbols
    symbol_list = []
    for r, row in enumerate(schematic):
        for c, col in enumerate(row):
            if not col.isdigit() and not col == '.':
                symbol_list.append((r, c))

    # find numbers in schematic
    part_list = []
    for r, row in enumerate(schematic):
        for nums in re.finditer(r'(\d+)', row):
            box = ((r - 1, nums.start() - 1), (r + 1, nums.end()))

            # check if symbol adjacent
            for symbol in symbol_list:
                inside_r = box[0][0] <= symbol[0] <= box[1][0]
                inside_c = box[0][1] <= symbol[1] <= box[1][1]
                # if symbol adjacent to part append to list
                if inside_r and inside_c:
                    part_list.append(int(nums[0]))

    part_sum = sum(part_list)
    return part_sum


def solve02(schematic):
    # create coords of gears
    gears_list = []
    for r, row in enumerate(schematic):
        for c, col in enumerate(row):
            if col == '*':
                gears_list.append((r, c))

    # find numbers in schematic
    gears_dict = {}
    for r, row in enumerate(schematic):
        for nums in re.finditer(r'(\d+)', row):
            box = ((r - 1, nums.start() - 1), (r + 1, nums.end()))

            # check if symbol adjacent
            for symbol in gears_list:
                inside_r = box[0][0] <= symbol[0] <= box[1][0]
                inside_c = box[0][1] <= symbol[1] <= box[1][1]
                # if symbol adjacent to part append to list
                if inside_r and inside_c:
                    if symbol not in gears_dict.keys():
                        gears_dict[symbol] = [int(nums[0])]
                    else:
                        gears_dict[symbol].append(int(nums[0]))

    # find gear ratio (product where two numbers are adjecent to *)
    ratio_list = [math.prod(p) for p in gears_dict.values() if len(p) == 2]

    # sum of ratios
    ratio_sum = sum(ratio_list)
    return ratio_sum


def parse_data(input_data):
    schematic = []
    for line_text in input_data.splitlines():
        schematic.append(line_text)
    return schematic


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f'part01 - part numbers sum = {answer01}')

    answer02 = solve02(input_data)
    print(f'part02 - gear ratio sum = {answer02}')
