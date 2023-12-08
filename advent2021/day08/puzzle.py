#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021 Day 08: Seven Segment Search
"""
import os
import re

SEGMENT_REGEX = re.compile(r'([a-g]+)')


def part01(input_data):
    # part 01 - count number of times 1, 4, 7 or 8 appear in output_value
    total_unique_count = 0

    for signal in input_data:
        patterns_ov = signal[10:]
        unique_count = sum([unique_num(x) for x in patterns_ov])
        total_unique_count += unique_count

    return total_unique_count


def part02(input_data):
    # part 02 - determine output values

    value_list = []
    for signal in input_data:
        value = calc_output_value(signal)
        value_list.append(value)

    output_value_sum = sum(value_list)
    return output_value_sum


def unique_num(x):
    return len(x) in [2, 4, 3, 7]


def calc_output_value(patterns):
    patterns_ov = patterns[10:]

    digit = {}

    digit[1] = flatten([x for x in patterns if len(x) == 2])
    digit[7] = flatten([x for x in patterns if len(x) == 3])
    digit[4] = flatten([x for x in patterns if len(x) == 4])
    digit[8] = flatten([x for x in patterns if len(x) == 7])

    A = digit[7] - digit[1]
    BD = digit[4] - digit[1]
    AEG = digit[8] - digit[4]
    EG = AEG - A
    CF = digit[1]

    patterns_235 = [x for x in patterns if len(x) == 5]
    patterns_069 = [x for x in patterns if len(x) == 6]

    digit[2] = flatten([x for x in patterns_235 if EG.issubset(x)])
    digit[3] = flatten([x for x in patterns_235 if CF.issubset(x)])

    CD = digit[2] - AEG
    D = BD & CD
    B = BD - CD
    C = CD - D
    ABCD = A | B | C | D

    digit[9] = flatten([x for x in patterns_069 if ABCD.issubset(x)])
    digit[0] = flatten([x for x in patterns_069 if not D.issubset(x)])
    digit[6] = flatten([x for x in patterns_069 if not C.issubset(x)])
    digit[5] = flatten([x for x in patterns_235 if not C.issubset(x)])

    # invert (swap k,v) digit dict
    digit_decode = dict((hash_v(v), k) for k, v in digit.items())

    output_value_list = [str(digit_decode[x]) for x in patterns_ov]
    output_value = int(''.join(output_value_list))

    return output_value


def hash_v(v):
    return ''.join(sorted(''.join(v)))


def flatten(lol):
    return set([x for sublist in lol for x in sublist])


def parse_data(input_data):
    segment_list = []
    # segment = signal_patten (x10) | output_value (4 digit)
    for segment_line in input_data.splitlines():
        match_list = SEGMENT_REGEX.findall(segment_line)
        patterns = [''.join(sorted(x)) for x in match_list]
        segment_list.append(patterns)

    return segment_list


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - times 1, 4, 7, or 8 appear in segments = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - output value sum = {answer02}')
