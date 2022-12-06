#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os
import pandas as pd


def solve(rosta_pd):

    # part 01
    rosta_pd[2] = rosta_pd[0].map(lambda x: x.split('-'))
    rosta_pd[3] = rosta_pd[1].map(lambda x: x.split('-'))
    rosta_pd[4] = rosta_pd[2].map(lambda x:
                                  set(range(int(x[0]), int(x[1]) + 1)))
    rosta_pd[5] = rosta_pd[3].map(lambda x:
                                  set(range(int(x[0]), int(x[1]) + 1)))
    rosta_pd[6] = rosta_pd.apply(lambda row:
                                 set(row[4]).intersection(row[5]),
                                 axis=1)
    rosta_pd[7] = rosta_pd.apply(lambda row:
                                 (set(row[6]) == set(row[4])) or (
                                     set(row[6]) == set(row[5])),
                                 axis=1)

    counts = rosta_pd[7].value_counts()
    contained_pairs = counts[True]

    # part 02
    rosta_pd[8] = rosta_pd.apply(lambda row: (len(set(row[6])) != 0), axis=1)
    counts = rosta_pd[8].value_counts()
    overlapping_pairs = counts[True]

    # print(rosta_pd)
    # return results
    return (contained_pairs, overlapping_pairs)


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    rosta_pd = pd.read_csv(input_data_file, header=None)

    return rosta_pd


if __name__ == '__main__':
    input_data = input_data('input.txt')

    answer = solve(input_data)
    print(f"Wholly container pairs = {answer[0]}")
    print(f"Overlapping assignment pairs = {answer[1]}")
