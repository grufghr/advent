#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os


def solve(input_data_file):
    # read input data from file
    with open(input_data_file, 'r') as input_filehandle:
        test_case_list = input_filehandle.read().splitlines()

    # part 01
    marker_start_list = []

    MARKER_LEN = 4

    for datastream in test_case_list:
        for s in range(0, len(datastream) - 1):
            e = s + MARKER_LEN
            tm = datastream[s:e]
            if (len(set(tm)) == len(tm)):
                # print(e, tm, datastream)
                marker_start_list.append(e)
                break

    # part 02
    message_start_list = []

    MESSAGE_LEN = 14

    for datastream in test_case_list:
        for s in range(0, len(datastream) - 1):
            e = s + MESSAGE_LEN
            tm = datastream[s:e]
            if (len(set(tm)) == len(tm)):
                # print(e, tm, datastream)
                message_start_list.append(e)
                break

    # return results
    return (marker_start_list, message_start_list)


if __name__ == '__main__':
    input_data_file = os.path.join(
        os.path.dirname(__file__), 'input.txt')

    answers = solve(input_data_file)
    print(f"Start of marker = {answers[0]}")
    print(f"start of message = {answers[1]}")
