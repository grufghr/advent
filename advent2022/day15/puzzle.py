#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os
import re
import numpy as np
from matplotlib import pyplot
import matplotlib as mpl

COLOR_MAP = mpl.colors.LinearSegmentedColormap.from_list('height_gradient_map',
                                                         ['yellow', 'white',
                                                          'green', 'red'],
                                                         256)

LINE_SENSOR_READING = re.compile(
    r'Sensor at x=(-?\d+), y=(-?\d+)\: closest beacon is at x=(-?\d+), y=(-?\d+)')

BEACON = 3  # 'B'
SENSOR = 2  # 'S'
GRID_KNOWN = 1  # '#'
GRID_UNKNOWN = 0  # '.'


def visualise(known_map):
    # find boundaries (only for numpy visualisation?)
    border = 0
    known_x = [item[0][0] for item in [loc for loc in known_map]]
    known_y = [item[0][1] for item in [loc for loc in known_map]]
    offset_r = min(known_y) - border
    offset_c = min(known_x) - border
    size_r = max(known_y) - offset_r + 1 + (border * 2)
    size_c = max(known_x) - offset_c + 1 + (border * 2)

    array_np = np.array([[GRID_UNKNOWN] * size_c for i in range(size_r)])
    for k in known_map:
        loc = (k[0][1] - offset_r, k[0][0] - offset_c)
        array_np[loc] = k[1]

    fig, grid_plot = pyplot.subplots(1, 1)
    fig.suptitle('Grid Maps')

    grid = grid_plot.imshow(array_np,
                            interpolation='nearest',
                            cmap=COLOR_MAP)
    grid_plot.set_title('Height Map')
    grid_plot.axis('off')

    pyplot.colorbar(grid, cmap=COLOR_MAP, orientation='horizontal')
    pyplot.show()


def distance_manhatten(a, b):
    x = max(a[0], b[0]) - min(a[0], b[0])
    y = max(a[1], b[1]) - min(a[1], b[1])
    return x + y


def solve(sensor_text_list, check_row):

    # process input file
    beacon_list = []
    sensor_list = []
    for sensor_reading in sensor_text_list:
        if match := LINE_SENSOR_READING.search(sensor_reading):
            loc_s = (int(match.group(1)), int(match.group(2)))
            sensor_list.append(loc_s)
            loc_b = (int(match.group(3)), int(match.group(4)))
            beacon_list.append(loc_b)

    # part 01 find all spaces (i.e. without beacon)
    known_map = []
    for sensor, beacon in zip(sensor_list, beacon_list):
        known_map.append((sensor, SENSOR))

        if (beacon not in [item[0] for item in known_map]):
            known_map.append((beacon, BEACON))

        dist_m = distance_manhatten(sensor, beacon)
        print(sensor, beacon, dist_m)
        range_x = range(sensor[0] - dist_m, sensor[0] + dist_m + 1)
        range_y = range(sensor[1] - dist_m - 1, sensor[1] + dist_m + 1)
        for x in range_x:
            for y in range_y:
                dist_k = distance_manhatten(sensor, (x, y))
                if (dist_k <= dist_m):
                    if (x, y) in beacon_list:
                        continue
                    if (x, y) in sensor_list:
                        continue
                    if (x, y) not in [item[0] for item in known_map]:
                        known_map.append(((x, y), GRID_KNOWN))

    visualise(known_map)

    grid_clear = len([item for item in known_map if (
        (item[0][1] == check_row) and (item[1] == GRID_KNOWN))])

    return grid_clear


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, 'r') as input_filehandle:
        input_data_text_list = input_filehandle.read().splitlines()

    return input_data_text_list


if __name__ == '__main__':
    input_data = input_data('input_example.txt')

    row = 10
    answer = solve(input_data, row)
    print(f"part01 - For row={row} positions without beacon = {answer}")
