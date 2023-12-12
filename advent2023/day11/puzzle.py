#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 11: Cosmic Expansion
"""
import os


def part01(input_data):
    galaxy_map = expand_galaxy(input_data, 1)
    distances = shortest_distance(galaxy_map)
    return sum(distances)


def part02(input_data):
    galaxy_map = expand_galaxy(input_data, 999999)
    distances = shortest_distance(galaxy_map)
    return sum(distances)


def expand_galaxy(galaxy_map, expansion):
    # expand galaxy map
    rows = [x[0] for x in galaxy_map]
    cols = [x[1] for x in galaxy_map]
    rmax = max(rows)
    cmax = max(cols)

    # work from largest to smallest increase if > empty row
    for r in range(rmax, 0, -1):
        if r not in rows:
            rows = [x + expansion if x > r else x for x in rows]
    for c in range(cmax, 0, -1):
        if c not in cols:
            cols = [x + expansion if x > c else x for x in cols]

    return list(zip(rows, cols))


def shortest_distance(galaxy_map):
    # find shortest distance between pairs
    distances = []
    gc = len(galaxy_map)
    for i in range(gc - 1):
        for j in range(i + 1, gc):
            distances.append(man_dist(galaxy_map[i], galaxy_map[j]))
    return distances


def man_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def parse_data(input_data):
    galaxy_map = []
    for r, line_text in enumerate(input_data.splitlines()):
        for c, reading in enumerate([*line_text]):
            if reading == '#':
                galaxy_map.append((r, c))
    return galaxy_map


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - furthest distance from start = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - sum of shortest distances = {answer02}')
