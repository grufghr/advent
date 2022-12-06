#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021
"""
import os
import numpy as np


def solve(sonar_depth_np):
    # part 01

    # find the difference between consecutive elements
    sonar_depth_delta = np.diff(sonar_depth_np)

    # count positive delta
    sonar_depth_increase_count = len(
        list(filter(lambda x: (x > 0), sonar_depth_delta)))

    # part 02

    # rolling sum of 3 consecutive elements in list
    sonar_depth_data_conseq3 = np.convolve(
        sonar_depth_np, np.ones(3), mode='valid')
    sonar_depth_data_conseq3_delta = np.diff(sonar_depth_data_conseq3)

    # count positive delta
    sonar_depth_increase_count_conseq3 = len(
        list(filter(lambda x: (x > 0), sonar_depth_data_conseq3_delta)))

    # return results
    return (sonar_depth_increase_count, sonar_depth_increase_count_conseq3)


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file into numpy array
    sonar_depth_np = np.loadtxt(input_data_file)

    return sonar_depth_np


if __name__ == '__main__':
    input_data = input_data('input.txt')

    answer = solve(input_data)
    print(f"Measurements larger than the previous measurement = {answer[0]}")
    print(f"Sums larger than previous (with 3 sliding) = {answer[1]}")
