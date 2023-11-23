#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2017 Day 02: Corruption Checksum
"""
import os


def solve01(input_data):
    checksum_total = 0
    for row in input_data:
        checksum = max(row) - min(row)
        checksum_total += checksum
    return checksum_total


def solve02(input_data):
    checksum_total = 0
    for row in input_data:
        checksum_list = [
            int(x / y) for x in row for y in row if x % y == 0 and int(x // y) != 1
        ]
        if len(checksum_list) > 1:
            exit(f"more than one value in {row} is evenly divisble")
        checksum_total += checksum_list[0]
    return checksum_total


def parse_data(input_data):
    input_data = input_data.splitlines()
    return [list(map(int, x.split())) for x in input_data]


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, "r") as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == "__main__":
    input_data = load_data("input.txt")

    answer01 = solve01(input_data)
    print(f"part01 - checksum total = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - checksum total = {answer02}")
