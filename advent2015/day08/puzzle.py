#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 Day 08: Matchsticks
"""
import os
import re


def solve01(input_data):
    # part 01 - calc literal length vs memory length

    len_code = 0
    len_memory = 0

    for line in input_data:
        len_code += len(line)

        line_n = line
        line_n = re.sub(r"\"(.*)\"", r"\1", line_n)
        # only need string length so subsitute 'X'
        line_n = re.sub(r"\\x[0-9a-fA-F]{2}", "X", line_n)
        line_n = re.sub(r"(\\){2}", "X", line_n)
        line_n = re.sub(r"\\(.)", r"\1", line_n)

        len_memory += len(line_n)

    len_diff = len_code - len_memory

    return len_diff


def solve02(input_data):
    # part 02 - calc literal length vs encode length

    len_code = 0
    len_escaped = 0

    for line in input_data:
        len_code += len(line)

        line_n = re.escape(line)
        line_n = re.sub('"', '\\"', line_n)
        line_n = '"' + line_n + '"'
        # print(line, "->", line_n)

        len_escaped += len(line_n)

    len_diff = len_escaped - len_code

    return len_diff


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
    print(f"part01 - difference literal - memory length = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - difference encoded - literal length = {answer02}")
