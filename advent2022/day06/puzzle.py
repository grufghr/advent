#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022 Day 06: Tuning Trouble
"""
import os


def solve01(input_data):
    answer = solve(input_data, 4)
    return answer


def solve02(input_data):
    answer = solve(input_data, 14)
    return answer


def solve(datastream, marker_len):
    marker_start = None

    for s in range(0, len(datastream) - 1):
        e = s + marker_len
        text_marker = datastream[s:e]
        if len(set(text_marker)) == len(text_marker):
            # print(e, text_marker, datastream)
            marker_start = e
            break

    return marker_start


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return input_data


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f'part01 - Start of marker = {answer01}')

    answer02 = solve02(input_data)
    print(f'part02 - Start of message = {answer02}')
