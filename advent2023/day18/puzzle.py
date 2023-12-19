#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 18: Lavaduct Lagoon
"""
import os
import re
from collections import namedtuple

# datatypes
Instruction = namedtuple('Instruction', ['dir', 'd', 'color'])
Coord = namedtuple('Coord', ['r', 'c'])

# static lookups
DIFF_MAP = {'R': Coord(0, 1), 'D': Coord(1, 0), 'L': Coord(0, -1), 'U': Coord(-1, 0)}
DIR_MAP = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}


def part01(input_data):
    dig_instructions = input_data
    total_area = calc_area(dig_instructions)
    return total_area


def part02(input_data):
    dig_instructions = input_data

    # swap color instruction into direction & distance
    dig_n = []
    for i in dig_instructions:
        dig_n.append(Instruction(DIR_MAP[i.color[5]], int(i.color[:5], 16), None))

    total_area = calc_area(dig_n)
    return total_area


def calc_area(dig_instructions):
    pos = Coord(0, 0)
    edge = 0
    area = 0
    for i in dig_instructions:
        diff = DIFF_MAP[i.dir]
        pos_d = Coord(diff.r * i.d, diff.c * i.d)
        pos = Coord(pos.r + pos_d.r, pos.c + pos_d.c)

        edge += i.d
        area += pos.c * pos_d.r

    total_area = area + (edge // 2) + 1
    return total_area


def parse_data(input_data):
    dig_instructions = []
    for line_text in input_data.splitlines():
        # R 6 (#70c710)
        i = re.match(r'(?P<dir>[R|D|L|U]) (?P<d>\d+) \(#(?P<color>[\da-f]+)\)', line_text).groupdict()
        i['d'] = int(i['d'])
        dig_instructions.append(Instruction(**i))
    return dig_instructions


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - cubic meters of lava = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - cubic meters of lava = {answer02}')
