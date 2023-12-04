#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2017 Day 03: Spiral Memory
"""
import os
from itertools import count


def solve01(input_data):
    mem_pos = int(input_data)
    coords = walk_spiral(mem_pos)
    manhatten_dist = sum(list(map(abs, coords)))
    return manhatten_dist


def solve02(input_data):
    mem_pos = int(input_data)
    for s in sum_spiral():
        if s > mem_pos:
            return s


def sum_spiral():
    grid = {(0, 0): 1}
    i, j = 0, 0
    for s in count(1, 2):
        for ds, di, dj in [(0, 1, 0), (0, 0, -1), (1, -1, 0), (1, 0, 1)]:
            for _ in range(s + ds):
                i += di
                j += dj
                grid[i, j] = sum(grid.get((k, l), 0) for k in range(i - 1, i + 2) for l in range(j - 1, j + 2))
                yield grid[i, j]


def walk_spiral(target):
    target
    d = 1
    m = 1
    x = 0
    y = 0
    square = 1

    while square <= target:
        while 2 * x * d < m:
            if square == target:
                return (x, y)
            x = x + d
            square = square + 1
        while 2 * y * d < m:
            if square == target:
                return (x, y)
            y = y + d
            square = square + 1
        d = -1 * d
        m = m + 1
    return None


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return int(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f'part01 - manhatten distance for memory location {input_data} = {answer01}')

    answer02 = solve02(input_data)
    print(f'part02 - first value that is larger than puzzle input = {answer02}')
