#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021 Day 25: Sea Cucumber
"""
import os
import numpy as np


def solve01(input_data):
    cucumber_grid = input_data

    # create new empty grid
    r_size, c_size = cucumber_grid.shape

    movement = True
    step = 0

    while movement and (step < 1000):
        movement = False

        cucumber_grid_n = cucumber_grid.copy()

        # east heard
        for r in range(r_size):
            for c in range(c_size):
                if cucumber_grid[r][c] == '>':
                    c_n = (c + 1) % c_size
                    if cucumber_grid[r][c_n] == '.':
                        cucumber_grid_n[r][c] = '.'
                        cucumber_grid_n[r][c_n] = '>'
                        movement = True
                    else:
                        cucumber_grid_n[r][c] = '>'

        cucumber_grid = cucumber_grid_n.copy()

        # south heard
        for r in range(r_size):
            for c in range(c_size):
                if cucumber_grid[r][c] == 'v':
                    r_n = (r + 1) % r_size
                    if cucumber_grid[r_n][c] == '.':
                        cucumber_grid_n[r][c] = '.'
                        cucumber_grid_n[r_n][c] = 'v'
                        movement = True
                    else:
                        cucumber_grid_n[r][c] = 'v'

        cucumber_grid = cucumber_grid_n.copy()
        step += 1

    return step


def parse_data(input_data):
    # parse data
    # split data into 2d array
    cucumber_map_text = [list(i) for i in input_data.splitlines()]
    # convert into numpy array
    cucumber_grid = np.array(cucumber_map_text)
    return cucumber_grid


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f'part01 - First step on which no sea cucumbers moved = {answer01}')
