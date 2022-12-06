#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os
import pandas as pd
import numpy as np


def solve(dimension_pd):

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

    # part 02
    dimension_pd['ribbon'] = dimension_pd.apply(lambda col:
                                                (2 * (col[3] + col[4])) +
                                                (col[0] * col[1] * col[2]),
                                                axis=1)

    ribbon_total = dimension_pd['ribbon'].sum()

    # print(dimension_pd)

    # return results
    return (wrapping_paper_total, ribbon_total)


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    dimension_pd = pd.read_csv(input_data_file, header=None, delimiter='x')

    return dimension_pd


if __name__ == '__main__':
    input_data = input_data('input.txt')
    answer = solve(input_data)
    print(f"Wrapping paper required = {answer[0]} sq feet")
    print(f"Ribbon required = {answer[1]} feet")
