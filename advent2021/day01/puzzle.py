#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021
"""
import os
import numpy as np


def solve(input_data_file):
    # read in data file
    sonar_depth_data = np.loadtxt(input_data_file)

    # part 01

    # find the difference between consecutive elements
    sonar_depth_delta = np.diff(sonar_depth_data)

    # count positive delta
    sonar_depth_increase_count = len(
        list(filter(lambda x: (x > 0), sonar_depth_delta)))

    # part 02

    # rolling sum of 3 consecutive elements in list
    sonar_depth_data_conseq3 = np.convolve(
        sonar_depth_data, np.ones(3), mode='valid')
    sonar_depth_data_conseq3_delta = np.diff(sonar_depth_data_conseq3)

    # count positive delta
    sonar_depth_increase_count_conseq3 = len(
        list(filter(lambda x: (x > 0), sonar_depth_data_conseq3_delta)))

    # return results
    return (sonar_depth_increase_count, sonar_depth_increase_count_conseq3)


if __name__ == '__main__':
    input_data_file = os.path.join(os.path.dirname(__file__), 'input.txt')

    answers = solve(input_data_file)
    print(f"Measurements larger than the previous measurement = {answers[0]}")
    print(f"Sums larger than previous (with 3 sliding) = {answers[1]}")
