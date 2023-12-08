#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022 Day 04: Camp Cleanup
"""
import os
import pandas as pd


def part01(input_data):
    answer = solve(input_data)
    return answer[0]


def part02(input_data):
    answer = solve(input_data)
    return answer[1]


def solve(rosta_pd):
    # part 01
    rosta_pd[2] = rosta_pd[0].map(lambda x: x.split('-'))
    rosta_pd[3] = rosta_pd[1].map(lambda x: x.split('-'))
    rosta_pd[4] = rosta_pd[2].map(lambda x: set(range(int(x[0]), int(x[1]) + 1)))
    rosta_pd[5] = rosta_pd[3].map(lambda x: set(range(int(x[0]), int(x[1]) + 1)))
    rosta_pd[6] = rosta_pd.apply(lambda row: set(row[4]).intersection(row[5]), axis=1)
    rosta_pd[7] = rosta_pd.apply(lambda row: (set(row[6]) == set(row[4])) or (set(row[6]) == set(row[5])), axis=1)

    counts = rosta_pd[7].value_counts()
    contained_pairs = int(counts[True])

    # part 02
    rosta_pd[8] = rosta_pd.apply(lambda row: (len(set(row[6])) != 0), axis=1)
    counts = rosta_pd[8].value_counts()
    overlapping_pairs = int(counts[True])

    # print(rosta_pd)
    return (contained_pairs, overlapping_pairs)


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    rosta_pd = pd.read_csv(input_data_file, header=None)

    return rosta_pd


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - Wholly container pairs = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - Overlapping assignment pairs = {answer02}')
