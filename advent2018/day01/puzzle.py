#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2018 Day 01: Chronal Calibration
"""
import os
from itertools import cycle


def solve01(input_data):
    freq = sum(input_data)
    return freq


def solve02(input_data):
    freq = 0
    freq_list = set([freq])
    for change in cycle(input_data):
        freq += change
        if freq in freq_list:
            return freq
        freq_list.add(freq)
    return None


def parse_data(input_data):
    return [int(x) for x in input_data]


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, "r") as filehandle:
        input_data = filehandle.read().splitlines()

    return parse_data(input_data)


if __name__ == "__main__":
    input_data = load_data("input.txt")

    answer01 = solve01(input_data)
    print(f"part01 - resulting frequency = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - first frequency reached twice = {answer02}")
