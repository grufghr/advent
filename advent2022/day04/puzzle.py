#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022
"""
import os
import pandas as pd


def solve(input_data_file):
    # read input data from file
    rosta_pd = pd.read_csv(input_data_file, header=None)

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

    print(rosta_pd)
    # return results
    return (contained_pairs, overlapping_pairs)


if __name__ == '__main__':
    input_data_file = os.path.join(
        os.path.dirname(__file__), 'input.txt')

    answers = solve(input_data_file)
    print(f"Wholly container pairs = {answers[0]}")
    print(f"Overlapping assignment pairs = {answers[1]}")
