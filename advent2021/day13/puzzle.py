#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021 Day 13: Transparent Origami
"""
import os
import re
from operator import itemgetter

COORD_REGEX = re.compile(r'^(\d+),(\d+)')
FOLD_REGEX = re.compile(r'^fold along (x|y)=(\d+)')


def solve01(grid, fold_list):
    # only process first instruction to fold paper
    axis, fold = fold_list[0]
    grid = _fold_paper(grid, axis, fold)

    dots = len(grid)
    return dots


def solve02(grid, fold_list):
    # complete all paper fold instructions
    for axis, fold in fold_list:
        grid = _fold_paper(grid, axis, fold)

    code = _get_code(grid)
    return code


def _fold_paper(grid, axis, fold):
    grid_n = set()
    if axis == 'x':
        for x, y in grid:
            if x > fold:
                x = fold - (x - fold)
            grid_n.add((x, y))
    else:
        for x, y in grid:
            if y > fold:
                y = fold - (y - fold)
            grid_n.add((x, y))

    return grid_n


def _get_code(grid):
    mx = max(grid, key=itemgetter(0))[0] + 1
    my = max(grid, key=itemgetter(1))[1] + 1

    code = []
    for j in range(0, my):
        row = ''
        for i in range(0, mx):
            if (i, j) in grid:
                row += '#'
            else:
                row += '.'
        code.append(row)
    return code


def _print_code(msg):
    for row in msg:
        print(row)


def parse_input(input_data):
    grid_list = []
    fold_list = []
    for instruction in input_data.splitlines():
        if match_m := COORD_REGEX.search(instruction):
            x, y = match_m.group(1), match_m.group(2)
            grid_list.append((int(x), int(y)))
        elif match_m := FOLD_REGEX.search(instruction):
            axis, d = match_m.group(1), match_m.group(2)
            fold_list.append((axis, int(d)))

    return (grid_list, fold_list)


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_input(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(*input_data)
    print(f'part01 - dots after first folder = {answer01}')

    answer02 = solve02(*input_data)
    print('part02 - code =')
    _print_code(answer02)
