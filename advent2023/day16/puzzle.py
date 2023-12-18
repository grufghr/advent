#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 16: The Floor Will Be Lava
"""
import os
from collections import deque
import numpy as np

DIR_E = (0, 1)
DIR_W = (0, -1)
DIR_N = (-1, 0)
DIR_S = (1, 0)


def part01(input_data):
    grid_map = input_data
    start = ((0, 0), DIR_E)
    energy_map = energise_grid(grid_map, start)
    energised_tiles = len(energy_map)
    return energised_tiles


def part02(input_data):
    grid_map = input_data
    grid_size = (max([r[0] for r in grid_map]), max([c[0] for c in grid_map]))

    tile_count_list = {}
    for r in range(grid_size[0] + 1):
        start = ((r, 0), DIR_E)
        energy_map = energise_grid(grid_map, start)
        tile_count_list[start] = len(energy_map)

        start = ((r, grid_size[1]), DIR_W)
        energy_map = energise_grid(grid_map, start)
        tile_count_list[start] = len(energy_map)

    for c in range(grid_size[1] + 1):
        start = ((0, c), DIR_S)
        energy_map = energise_grid(grid_map, start)
        tile_count_list[start] = len(energy_map)

        start = ((grid_size[0], c), DIR_N)
        energy_map = energise_grid(grid_map, start)
        tile_count_list[start] = len(energy_map)

    best_config = max(tile_count_list.values())
    return best_config


def energise_grid(grid_map, start):
    grid_size = (max([r[0] for r in grid_map]), max([c[0] for c in grid_map]))

    # to stop infinity loops
    limit_q = 2000

    energy_map = {}

    q = deque([start])
    while q and len(q) < limit_q:
        beam, direction = q.popleft()

        # beam left grid (ignore)
        if beam[0] < 0 or beam[1] < 0 or beam[0] > grid_size[0] or beam[1] > grid_size[1]:
            continue

        # add direction entered to tile
        if beam in energy_map:
            if direction in energy_map[beam]:
                # previously entered tile from this direction (ignore)
                continue
            else:
                energy_map[beam].add(direction)
        else:
            energy_map[beam] = set([direction])

        # move beam in direction
        if beam not in grid_map:
            q.append((tuple(np.add(beam, direction)), direction))
        elif grid_map[beam] == '-':
            if direction == DIR_E or direction == DIR_W:
                q.append((tuple(np.add(beam, direction)), direction))
            else:
                q.append((tuple(np.add(beam, DIR_E)), DIR_E))
                q.append((tuple(np.add(beam, DIR_W)), DIR_W))
        elif grid_map[beam] == '|':
            if direction == DIR_N or direction == DIR_S:
                q.append((tuple(np.add(beam, direction)), direction))
            else:
                q.append((tuple(np.add(beam, DIR_N)), DIR_N))
                q.append((tuple(np.add(beam, DIR_S)), DIR_S))
        elif grid_map[beam] == '/':
            if direction == DIR_N:
                q.append((tuple(np.add(beam, DIR_E)), DIR_E))
            elif direction == DIR_E:
                q.append((tuple(np.add(beam, DIR_N)), DIR_N))
            elif direction == DIR_S:
                q.append((tuple(np.add(beam, DIR_W)), DIR_W))
            elif direction == DIR_W:
                q.append((tuple(np.add(beam, DIR_S)), DIR_S))
        elif grid_map[beam] == '\\':
            if direction == DIR_N:
                q.append((tuple(np.add(beam, DIR_W)), DIR_W))
            elif direction == DIR_E:
                q.append((tuple(np.add(beam, DIR_S)), DIR_S))
            elif direction == DIR_S:
                q.append((tuple(np.add(beam, DIR_E)), DIR_E))
            elif direction == DIR_W:
                q.append((tuple(np.add(beam, DIR_N)), DIR_N))
    return energy_map


def parse_data(input_data):
    tile_map = {}
    for r, line_text in enumerate(input_data.splitlines()):
        for c, tile in enumerate(line_text):
            if tile != '.':
                coords = (r, c)
                tile_map[coords] = tile
    return tile_map


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - energised tiles, start (0,0) = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - energised tiles, best start = {answer02}')
