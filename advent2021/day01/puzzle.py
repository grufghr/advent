#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Solve Puzzle
"""
import os
import numpy as np


def solve01(sonar_depth_np):
    # part 01 -

    # find the difference between consecutive elements
    sonar_depth_delta = np.diff(sonar_depth_np)

    # count positive delta
    sonar_depth_increase_count = len(
        list(filter(lambda x: (x > 0), sonar_depth_delta)))

    return sonar_depth_increase_count


def solve02(sonar_depth_np):
    # part 02 -

    # rolling sum of 3 consecutive elements in list
    sonar_depth_data_conseq3 = np.convolve(
        sonar_depth_np, np.ones(3), mode='valid')
    sonar_depth_data_conseq3_delta = np.diff(sonar_depth_data_conseq3)

    # count positive delta
    sonar_depth_increase_count_conseq3 = len(
        list(filter(lambda x: (x > 0), sonar_depth_data_conseq3_delta)))

    return sonar_depth_increase_count_conseq3


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    sonar_depth_np = np.loadtxt(input_data_file)

    return sonar_depth_np


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - Measurements larger than previous = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - Sums larger than previous (3 sliding) = {answer02}")
