#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022 Day 15: Beacon Exclusion Zone
"""
import os
import re


LINE_SENSOR_READING = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+)\: closest beacon is at x=(-?\d+), y=(-?\d+)')


def solve01(sensor_data, row):
    al = [x - abs(row - y) + md for (x, y), md in sensor_data.items()]
    bl = [x + abs(row - y) - md for (x, y), md in sensor_data.items()]
    free_positons = max(al) - min(bl)
    return free_positons


def solve02(sensor_data):
    sensor_list = sensor_data.keys()

    acoeffs, bcoeffs = set(), set()
    for (x, y), md in sensor_data.items():
        acoeffs.add(y - x + md + 1)
        acoeffs.add(y - x - md - 1)
        bcoeffs.add(x + y + md + 1)
        bcoeffs.add(x + y - md - 1)

    beacon = None
    boundary = 4000000
    for a in acoeffs:
        for b in bcoeffs:
            p = ((b - a) // 2, (a + b) // 2)
            if all(0 < c < boundary for c in p):
                if all(manhatten_distance(p, t) > sensor_data[t] for t in sensor_list):
                    beacon = (p[0], p[1])

    frequency = (boundary * beacon[0]) + beacon[1]
    return frequency


def manhatten_distance(a, b):
    # manhatten distance between two points a(x,y) and b(x,y)
    md = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return md


def parse_data(input_data):
    sensor_text = input_data.splitlines()
    sensor_list = {}
    for sensor_reading in sensor_text:
        if match := LINE_SENSOR_READING.search(sensor_reading):
            loc_s = (int(match.group(1)), int(match.group(2)))
            loc_b = (int(match.group(3)), int(match.group(4)))
            sensor_list[loc_s] = manhatten_distance(loc_s, loc_b)
    return sensor_list


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data, 2000000)
    print(f'part01 - Positions without beacon = {answer01}')

    answer02 = solve02(input_data)
    print(f'part02 - Tuning frequency = {answer02}')
