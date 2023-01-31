#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Solve Puzzle 2021 Day 11: Dumbo Octopus
"""
import os
import numpy as np


def solve01(input_data):
    # part 01 - count flashes for 100 steps

    grid = np.array(input_data)
    flash_count = 0

    for step in range(0, 100):
        # increase energy
        grid += 1

        # count flashes (and adjacent flashes)
        flash_count += update_grid_flash(grid)

    return flash_count


def solve02(input_data):
    # part 02 - step all octopuses flash

    grid = np.array(input_data)
    step = 1

    while (step < 250):
        # increase energy
        grid += 1

        # count flashes (and adjacent flashes)
        flash_count = update_grid_flash(grid)

        if flash_count == grid.size:
            return step

        step += 1

    return None


def update_grid_flash(grid):
    flash_count = 0

    # flash where energy greater than 9
    flash_list = list(zip(*np.where(grid > 9)))
    flash_count += len(flash_list)

    # flash adjacent octopuses
    while len(flash_list) > 0:
        for flash in flash_list:
            # if flash set energy to large negative so doesn't flash again
            grid[flash] = -999
            # increase adjacent engery +1
            for adj in get_adjacent(grid, flash):
                grid[adj] += 1
        # any new flashes?
        flash_list = list(zip(*np.where(grid > 9)))
        flash_count += len(flash_list)

    # reset flashed energey to zero
    grid[grid < 0] = 0

    return flash_count


ADJ_MATRIX = [(-1, -1), (0, -1), (1, -1), (-1, 0),
              (1, 0), (-1, 1), (0, 1), (1, 1)]


def get_adjacent(grid, loc):
    adj = [tuple(sum(x) for x in zip(loc, adj)) for adj in ADJ_MATRIX]
    adj = [x for x in adj if within_boundary(x, grid)]
    return adj


def within_boundary(x, grid):
    if x[0] < 0:
        return False
    elif x[0] >= grid.shape[0]:
        return False
    elif x[1] < 0:
        return False
    elif x[1] >= grid.shape[1]:
        return False
    return True


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data_list = filehandle.read().splitlines()

    grid_list = [list(map(int, [*x])) for x in input_data_list]

    # 2d array of integers
    return grid_list


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - flash count = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - step all octopuses flash = {answer02}")
