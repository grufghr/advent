#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 Day 12: JSAbacusFramework.io
"""
import os
import re
import json
from collections import deque


def solve01(input_data):
    number_list = [int(x) for x in re.findall(r"(-?\d+)", input_data)]
    total = sum(number_list)
    return total


def solve02(input_data):
    accounts = json.loads(input_data)

    total = 0

    # note: use count to prevent infinite loop
    count = 0

    q = deque([accounts])
    while q and count < 3000:
        count += 1
    
        element = q.pop()
        if isinstance(element, dict):
            if "red" in element.keys():
                continue
            if "red" in element.values():
                continue
            for key, value in element.items():
                q.append(value)
        elif isinstance(element, list):
            for item in element:
                q.append(item)
        elif isinstance(element, int):
            total = total + element

    return total


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, "r") as filehandle:
        input_data = filehandle.read()

    return input_data


if __name__ == "__main__":
    input_data = load_data("input.txt")

    answer01 = solve01(input_data)
    print(f"part01 - sum of numbers = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - sum of numbers (without red) = {answer02}")
