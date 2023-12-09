#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 09: Mirage Maintenance
"""
import os
import re


def part01(input_data):
    report = input_data
    total = sum(list([extrapolate_next(seq) for seq in report]))
    return total


def part02(input_data):
    report = input_data
    total = sum(list([extrapolate_prev(seq) for seq in report]))
    return total


def extrapolate_next(seq):
    rec = not all([x == 0 for x in seq])
    seq_diff = [b - a for a, b in zip(seq, seq[1:])]
    return seq[-1] + extrapolate_next(seq_diff) if rec else 0


def extrapolate_prev(seq):
    rec = not all([x == 0 for x in seq])
    seq_diff = [b - a for a, b in zip(seq, seq[1:])]
    return seq[0] - extrapolate_prev(seq_diff) if rec else 0


def parse_data(input_data):
    report = []
    for line_text in input_data.splitlines():
        sequence = list(map(int, re.findall(r'(-?\d+)', line_text)))
        report.append(sequence)

    return report


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - extrapolated sum = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - extrapolated sum = {answer02}')
