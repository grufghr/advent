#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Solve Puzzle
"""
import os
import math
from collections import deque
import numpy as np


def solve01(input_data):
    # part 01 - find local minimum in gridmap

    grid = np.array(input_data)
    lowest_height_list = []

    for ir in range(0, grid.shape[0]):
        for ic in range(0, grid.shape[1]):
            loc = (ir, ic)
            if all([grid[loc] < grid[t] for t in adjacent(grid, loc)]):
                lowest_height_list.append(grid[loc] + 1)

    risk_sum = sum(lowest_height_list)

    return risk_sum


def solve02(input_data):
    # part 02 - find basins in gridmap
    grid = np.array(input_data)
    lowest_loc_list = []

    for ir in range(0, grid.shape[0]):
        for ic in range(0, grid.shape[1]):
            loc = (ir, ic)
            if all([grid[loc] < grid[t] for t in adjacent(grid, loc)]):
                lowest_loc_list.append(loc)

    basin_size_list = [calc_basin_size(grid, loc) for loc in lowest_loc_list]
    basin_size_list = sorted(basin_size_list, reverse=True)

    largest3_product = math.prod(basin_size_list[:3])

    return largest3_product


def calc_basin_size(grid, loc_s):
    visited = set()
    q = deque([loc_s])

    while q:
        loc = q.popleft()

        visited.add(loc)

        # find more basin loc
        adj = adjacent(grid, loc)
        adj_basin = [x for x in adj if x not in visited and grid[x] != 9]
        q.extend(adj_basin)

    # TODO answer is = 911400
    return len(visited)


def adjacent(grid, loc):
    r, c = loc
    rm, cm = grid.shape

    adjacent = []
    if r > 0:
        adjacent.append((r - 1, c))
    if r + 1 < rm:
        adjacent.append((r + 1, c))
    if c > 0:
        adjacent.append((r, c - 1))
    if c + 1 < cm:
        adjacent.append((r, c + 1))
    return adjacent


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data_list = filehandle.read().splitlines()

    grid_list = [list(map(int, [*x])) for x in input_data_list]

    # 2d array of integer heights
    return grid_list


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - sum of risk levels = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - product of three largest basins = {answer02}")
