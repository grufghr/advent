#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os


def solve(datastream, marker_len):
    marker_start = None

    for s in range(0, len(datastream) - 1):
        e = s + marker_len
        text_marker = datastream[s:e]
        if (len(set(text_marker)) == len(text_marker)):
            # print(e, text_marker, datastream)
            marker_start = e
            break

    # return results
    return marker_start


def input_data_iter(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as input_filehandle:
        input_txt_list = input_filehandle.read().splitlines()

    for input_txt in input_txt_list:
        yield (input_txt)


if __name__ == '__main__':
    instruction_set = next(input_data_iter('input.txt'))

    answer = solve(instruction_set, 4)
    print(f"Start of marker = {answer}")

    answer = solve(instruction_set, 14)
    print(f"Start of message = {answer}")
