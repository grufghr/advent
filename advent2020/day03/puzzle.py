#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2020 Day 03: Toboggan Trajectory
"""

import os
import math
from collections import namedtuple

Position = namedtuple('Pos', 'x y')


def part01(input_data):
    # part 01 - count tree encounters
    gradient = (3, 1)
    tree_count = calc_tree_count(input_data, *gradient)

    return tree_count


def part02(input_data):
    # part 02 - product of trees on slopes
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_count_list = []
    for gradient in slopes:
        tc = calc_tree_count(input_data, *gradient)
        tree_count_list.append(tc)
    product = math.prod(tree_count_list)
    return product


def calc_tree_count(input_data, g_x, g_y):
    # calc grid size
    x_max = max([x for x, y in input_data]) + 1
    y_max = max([y for x, y in input_data]) + 1

    # start pos
    pos = Position(0, 0)
    tree_count = 0

    # toboggan slope unitl reach bottom (y_max)
    while pos.y < y_max:
        if pos in input_data:
            tree_count += 1
        # repeats over x axis (hence % x_max)
        x_n = (pos.x + g_x) % x_max
        y_n = pos.y + g_y
        pos = Position(x_n, y_n)

    # encountered trees
    return tree_count


def parse_data(input_data):
    tree_list = []
    for y, line in enumerate(input_data.splitlines()):
        for x, grid in enumerate(line):
            if grid == '#':
                tree = (x, y)
                tree_list.append(tree)

    # list of tuples (x,y) representing tree positions on slope
    return tree_list


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - trees encountered = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - product of trees on slope = {answer02}')
