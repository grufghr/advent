#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 Day 02: I Was Told There Would Be No Math
"""
import os
import pandas as pd
import numpy as np


def solve01(dimension_pd):
    # part 01
    dimension_pd[3], dimension_pd[4] = np.sort(
        dimension_pd, axis=1)[:, :2].T
    dimension_pd['paper'] = dimension_pd.apply(lambda col:
                                               (2 * col[0] * col[1]) +
                                               (2 * col[1] * col[2]) +
                                               (2 * col[0] * col[2]) +
                                               (col[3] * col[4]),
                                               axis=1)

    wrapping_paper_total = dimension_pd['paper'].sum()

    return wrapping_paper_total


def solve02(dimension_pd):
    # part 02
    dimension_pd[3], dimension_pd[4] = np.sort(
        dimension_pd, axis=1)[:, :2].T

    dimension_pd['ribbon'] = dimension_pd.apply(lambda col:
                                                (2 * (col[3] + col[4])) +
                                                (col[0] * col[1] * col[2]),
                                                axis=1)

    ribbon_total = dimension_pd['ribbon'].sum()

    return ribbon_total


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    dimension_pd = pd.read_csv(input_data_file, header=None, delimiter='x')

    return dimension_pd


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - Wrapping paper required = {answer01} sq feet")

    answer02 = solve02(input_data)
    print(f"part02 - Ribbon required = {answer02} feet")
