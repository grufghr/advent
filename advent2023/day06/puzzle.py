#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 06: Wait For It
"""
import os
import re
import math


def part01(input_data):
    race_time, race_distance = input_data

    winning_ways = []
    # for each race calculate winning ways
    for r in range(0, len(race_time)):
        ww = calc_winning_ways(race_time[r], race_distance[r])
        winning_ways.append(ww)

    # calc product of winning ways
    winning_product = math.prod(winning_ways)
    return winning_product


def part02(input_data):
    race_time, race_distance = input_data
    # adjust input for bad kerning
    race_time = int(''.join(list(map(str, race_time))))
    race_distance = int(''.join(list(map(str, race_distance))))
    
    winning_ways = calc_winning_ways(race_time, race_distance)
    return winning_ways


def calc_winning_ways(race_time, race_distance):
    ww = 0
    # first and last distance travelled = 0 (not checked)
    for w in range(1, race_time):
        distance = w * (race_time - w)

        # if found first winning race
        # calculate total number of winning races (and break loop)
        if distance > race_distance:
            ww = race_time - (w * 2) + 1
            break
    return ww


def parse_data(input_data):
    for line_text in input_data.splitlines():
        if line_text.startswith('Time:'):
            race_time = list(map(int, re.findall(r'(\d+)', line_text)))
        elif line_text.startswith('Distance:'):
            race_distance = list(map(int, re.findall(r'(\d+)', line_text)))

    return (race_time, race_distance)


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - product of winning ways = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - winning ways = {answer02}')
