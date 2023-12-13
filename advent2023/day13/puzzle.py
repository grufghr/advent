#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 13: Point of Incidence
"""
import os
from itertools import groupby


def part01(input_data):
    patterns = input_data
    return solve(patterns, False)


def part02(input_data):
    patterns = input_data
    return solve(patterns, True)


def solve(patterns, check_smudge):
    # find all mirror positions (and add them together)
    row_sum = 0
    col_sum = 0
    for pattern in patterns:
        # find mirror axis
        axis = find_mirror_axis(pattern, check_smudge)
        if axis:
            row_sum += axis
        else:
            # transpose patterns 90 degress and find mirror row (equivalent to mirror on vertical axis)
            p_t = [''.join(s) for s in zip(*pattern)]
            axis = find_mirror_axis(p_t, check_smudge)
            col_sum += axis

    summary = (row_sum * 100) + col_sum
    return summary


def find_mirror_axis(pattern, check_smudge):
    mp = None  # no mirror point
    lenp = len(pattern)
    for x in range(1, lenp):
        # convert pattern into two strings (s1, s2) at mirror point p
        p1 = pattern[:x]
        p1.reverse()
        p2 = pattern[x:]
        mx = min(len(p1), len(p2))
        s1 = ''.join(p1[:mx])
        s2 = ''.join(p2[:mx])

        # check if mirror reflections matach
        if check_smudge:
            if match_with_smudge(s1, s2):
                mp = x
                break
        elif s1 == s2:
            mp = x
            break

    return mp


def match_with_smudge(s1, s2):
    # s1 == s2 if same except exactly 1 character difference
    matched = sum([1 for a, b in zip(s1, s2) if a != b]) == 1
    return matched


def parse_data(input_data):
    pattern = []
    for line_text in input_data.splitlines():
        pattern.append(line_text)

    pattern_list = [list(g) for k, g in groupby(pattern, key=lambda x: x == '') if not k]

    return pattern_list


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - mirror summary = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - mirror summary (with 1 smudge) = {answer02}')
