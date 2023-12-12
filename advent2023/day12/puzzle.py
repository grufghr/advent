#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 12: Hot Springs
"""
import os
import re
from functools import cache


def part01(input_data):
    records = input_data

    arrange_count = 0
    for text, counts in records:
        arrange_count += calc_arrangement(text + '.', tuple(counts), 0, 0, 0)
    return arrange_count


def part02(input_data):
    records = input_data

    arrange_count = 0
    for text, counts in records:
        # unfold 5 times
        text_n = '?'.join([text] * 5)
        counts_n = counts * 5

        arrange_count += calc_arrangement(text_n + '.', tuple(counts_n), 0, 0, 0)

    return arrange_count


@cache
def calc_arrangement(text, counts, pos, current_count, countpos):
    # algorithm: recursive matching on combinations
    # algorithm: use memoize caching
    #
    # pos  = next character to be processed
    # current_count = pos current sequence of #
    # countpos = how many sequences of # have already finished beein identified
    if pos == len(text):
        if len(counts) == countpos:
            count_a = 1
        else:
            count_a = 0
    elif text[pos] == '#':
        count_a = calc_arrangement(text, counts, pos + 1, current_count + 1, countpos)
    elif text[pos] == '.' or countpos == len(counts):
        if countpos < len(counts) and current_count == counts[countpos]:
            count_a = calc_arrangement(text, counts, pos + 1, 0, countpos + 1)
        elif current_count == 0:
            count_a = calc_arrangement(text, counts, pos + 1, 0, countpos)
        else:
            count_a = 0
    else:
        hash_count = calc_arrangement(text, counts, pos + 1, current_count + 1, countpos)
        dot_count = 0
        if current_count == counts[countpos]:
            dot_count = calc_arrangement(text, counts, pos + 1, 0, countpos + 1)
        elif current_count == 0:
            dot_count = calc_arrangement(text, counts, pos + 1, 0, countpos)
        count_a = hash_count + dot_count

    return count_a


def parse_data(input_data):
    records = []
    for line_text in input_data.splitlines():
        # .??..??...?##. 1,1,3
        match = re.search(r'([\#\.\?]+) ((?:\d+,)+\d+)', line_text)
        if match:
            reading_text = match[1]
            reading_list = list(map(int, (match[2]).split(',')))
            records.append((reading_text, reading_list))
    return records


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - sum of arrangements = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - sum of arrangements (x5) = {answer02}')
