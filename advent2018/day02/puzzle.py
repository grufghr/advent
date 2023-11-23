#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2018 Day 02: Inventory Management System
"""
import os
from collections import Counter


def solve01(input_data):
    # part 01 - box id list checksum
    valid_2 = 0
    valid_3 = 0
    for line in input_data:
        res = Counter(line)
        valid_2 += 1 if 2 in res.values() else 0
        valid_3 += 1 if 3 in res.values() else 0

    checksum = valid_2 * valid_3
    return checksum


def solve02(input_data):
    # part 02 - common letters of closest box ids
    closest = 0
    common = None
    for sx, line_a in enumerate(input_data[:-1]):
        for line_b in input_data[sx + 1 :]:
            count = sum(1 for a, b in zip(line_a, line_b) if a == b)
            if count > closest:
                closest = count
                common = (line_a, line_b)

    common_list = [a for a, b in zip(*common) if a == b]
    common_str = "".join(common_list)
    return common_str


def parse_data(input_data):
    return input_data.splitlines()


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, "r") as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == "__main__":
    input_data = load_data("input.txt")

    answer01 = solve01(input_data)
    print(f"part01 - box id list checksum = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - common letters of closest box ids = {answer02}")
