#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 Day 18: Like a GIF For Your Yard
"""

import os


def part01(input_data):
    grid = input_data
    lights_on = run_cycles(grid, 100)
    return lights_on


def part02(input_data):
    grid = input_data
    lights_on = run_cycles(grid, 100, True)
    return lights_on


def run_cycles(grid, cycles, corners_on=False):
    max_x = max([p[0] for p in grid])
    max_y = max([p[1] for p in grid])

    if corners_on:
        corners = {(0, 0), (0, max_y), (max_x, 0), (max_x, max_y)}
    else:
        corners = set()

    grid = grid.union(corners)

    for c in range(cycles):
        grid_n = set()
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                neighbour_count = len(grid.intersection(neighbours(x, y)))
                if ((x, y) in grid) and (2 <= neighbour_count <= 3):
                    grid_n.add((x, y))
                if ((x, y) not in grid) and (neighbour_count == 3):
                    grid_n.add((x, y))

        grid = grid_n.union(corners)

    return len(grid)


def neighbours(px, py):
    neighbour_list = {
        (px - 1, py - 1),
        (px - 1, py),
        (px - 1, py + 1),
        #
        (px, py - 1),
        # (px, py),
        (px, py + 1),
        #
        (px + 1, py - 1),
        (px + 1, py),
        (px + 1, py + 1),
    }
    return neighbour_list


def parse_data(input_data):
    lights = set()
    for y, line in enumerate(input_data.splitlines()):
        for x, char in enumerate(line.strip()):
            if char == '#':
                lights.add((x, y))
    return lights


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - lights on after cycles = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - lights on after cycles = {answer02}')
