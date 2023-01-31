#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Solve Puzzle 2022 Day 15: Beacon Exclusion Zone
"""
import os
import re


LINE_SENSOR_READING = re.compile(
    r'Sensor at x=(-?\d+), y=(-?\d+)\: closest beacon is at x=(-?\d+), y=(-?\d+)')


def manhatten_distance(a, b):
    # manhatten distance between two points a(x,y) and b(x,y)
    x = max(a[0], b[0]) - min(a[0], b[0])
    y = max(a[1], b[1]) - min(a[1], b[1])
    # print('md', a, b, x + y)
    return x + y


def manhatten_x(y, d):
    # find x where manhatten distance known i.e. x = d - y
    return d - y


def merge_overlaps(tup_list):
    if len(tup_list) == 0:
        return []

    tup_list.sort(key=lambda item: item[0])
    lol = [list(tup) for tup in tup_list]

    merged_list = [lol[0]]
    for tup_c in lol:
        tup_p = merged_list[-1]
        if (tup_p[1] + 1) >= tup_c[0]:
            tup_p[1] = max(tup_p[1], tup_c[1])
        else:
            merged_list.append(tup_c)
    return [(item[0], item[1]) for item in merged_list]


def split_intervals(tup_list, interval_list):
    if len(interval_list) == 0:
        return tup_list

    tup_list.sort(key=lambda item: item[0])
    interval_list.sort()

    split_list = []
    x = interval_list.pop(0)
    for tup_c in tup_list:
        tup_n = tup_c
        while tup_n[0] <= x <= tup_n[1]:
            tup_n = split_tuple(tup_n, x)
            # extend result with all but last [:-1]
            split_list.extend(tup_n[:-1])
            if (len(interval_list) > 0):
                x = interval_list.pop(0)
            # while loop to check split last [-1]
            tup_n = tup_n[-1]
        split_list.append(tup_n)  # add last tup_n

    return split_list


def split_tuple(tup, x):
    result = []
    tup_l = (tup[0], x - 1)
    tup_r = (x + 1, tup[1])
    if tup_l[0] <= tup_l[1]:
        result.append(tup_l)
    if tup_r[0] <= tup_r[1]:
        result.append(tup_r)
    return result


def solve01(input_data):
    answer = solve(input_data, 2000000)
    return answer


def solve02(input_data):
    answer = solve(input_data, 2000000)
    return answer


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

    # find manhatten distances
    known_list = []
    for sensor, beacon in zip(sensor_list, beacon_list):

        dist_sb = manhatten_distance(sensor, beacon)
        dist_sr = manhatten_distance(sensor, (sensor[0], check_row))

        # ignore sensors too far away from check_row
        if (dist_sr > dist_sb):
            continue

        y = max(check_row, sensor[1]) - min(check_row, sensor[1])
        x = manhatten_x(y, dist_sb)
        # print(f"s={sensor}, b={beacon}, sb={dist_sb}, sr={dist_sr} x={x} y={y}")
        known_x_slice = (sensor[0] - x, sensor[0] + x)

        known_list.append(known_x_slice)

    known_list.sort(key=lambda item: item[0])
    # print(check_row, 'known_list', known_list)

    # merge overlapping knowns
    known_list_merged = merge_overlaps(known_list)
    # print(check_row, 'merged', known_list_merged)

    # split by beacons
    beacon_split = [b[0] for b in beacon_list if b[1] == check_row]
    beacon_split = list(set(beacon_split))  # remove duplicates
    # print(check_row, 'beacon_split', beacon_split)
    known_list_split = split_intervals(known_list_merged, beacon_split)

    # split by sensors
    sensor_split = [s[0] for s in sensor_list if s[1] == check_row]
    known_list_split = split_intervals(known_list_split, sensor_split)
    # print(check_row, 'sensor_split', known_list_split)

    free_positions = sum([((t[1] - t[0]) + 1) for t in known_list_split])
    # print(free_positions)

    return free_positions


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, 'r') as input_filehandle:
        input_data_text_list = input_filehandle.read().splitlines()

    return input_data_text_list


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - Positions without beacon = {answer01}")
