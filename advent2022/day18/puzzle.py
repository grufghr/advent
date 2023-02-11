#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022 Day 18: Boiling Boulders
"""
import os
from collections import deque
import numpy as np

SPACE = 0
CUBE = 1
FLOOD = 2


def floodfill(matrix, start_coords):

    q = deque()
    q.append(start_coords)
    while q:
        cube_coords = q.popleft()
        x, y, z = cube_coords

        if matrix[cube_coords] == SPACE:
            matrix[cube_coords] = FLOOD
            if x > 0:
                q.append((x - 1, y, z))
            if x < matrix.shape[0] - 1:
                q.append((x + 1, y, z))
            if y > 0:
                q.append((x, y - 1, z))
            if y < matrix.shape[1] - 1:
                q.append((x, y + 1, z))
            if z > 0:
                q.append((x, y, z - 1))
            if z < matrix.shape[2] - 1:
                q.append((x, y, z + 1))


def calc_exposed_surface(cube_list):
    area = len(cube_list) * 6
    for i, cube_i in enumerate(cube_list[:-1]):
        for cube_j in cube_list[i + 1:]:

            adjacent = sum(
                list(map(lambda i: abs(i[0] - i[1]), zip(cube_i, cube_j))))
            if adjacent == 1:
                area -= 2
    return area


def solve01(cube_list):
    # part 01 - total area exposed

    exposed_surface = calc_exposed_surface(cube_list)

    return exposed_surface


def solve02(cube_list):
    # part 02 - deduct trapped space

    # create 3d array
    x, y, z = zip(*cube_list)
    size = (max(x) + 1, max(y) + 1, max(z) + 1)
    origin = (min(x), min(y), min(z))
    if len([i for i in list(origin) if i < 0]) > 0:
        print(f"cubes exist in zero/negative space, origin = {origin}")
        print("floodfill may not work, need to offset cubes")
        exit()
    cube_np = np.zeros(size, dtype=int)
    cube_np[tuple(np.array(cube_list).T)] = CUBE

    # flood grid from origin
    floodfill(cube_np, (0, 0, 0))
    # replace remaing spaces with CUBE
    cube_np[cube_np == SPACE] = CUBE
    # replace flood with SPACE (is this required?)
    cube_np[cube_np == FLOOD] = SPACE

    # create list of cubes
    cube_list = np.argwhere(cube_np == CUBE)
    exposed_surface = calc_exposed_surface(cube_list)

    return exposed_surface


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, 'r') as input_filehandle:
        input_data_text_list = input_filehandle.read().splitlines()

    # parse input file
    cube_list = []
    for cube_text in input_data_text_list:
        cube = tuple([int(c) for c in cube_text.split(',')])
        cube_list.append(cube)

    return cube_list


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - scanned lava droplet surface area  = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - exterior surface area  = {answer02}")
