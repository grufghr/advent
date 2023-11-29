#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022 Day 13: Distress Signal
"""
import os
import json
from functools import cmp_to_key


def check_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            # print(f"- Left side is smaller, so inputs are in the right order")
            return True
        if right < left:
            # print(f"- Right side is smaller, so inputs are not in the right order")
            return False
    elif isinstance(left, list) and isinstance(right, list):
        for pair_l, pair_r in zip(left, right):
            c = check_order(pair_l, pair_r)
            if c is not None:
                return c
        if len(left) < len(right):
            # print(f"- Left side ran out of items, so inputs are in the right order")
            return True
        if len(right) < len(left):
            # print(f"- Right side ran out of items, so inputs are not in the right order")
            return False
    elif isinstance(left, int) and isinstance(right, list):
        left_n = [left]
        # print(f"- Mixed types; convert left to {left_n} and retry comparison")
        return check_order(left_n, right)
    elif isinstance(left, list) and isinstance(right, int):
        right_n = [right]
        # print(f"- Mixed types; convert right to {right_n} and retry comparison")
        return check_order(left, right_n)
    else:
        exit(f'do something with {type(left)} {type(right)}')
    return None


def check_order_comparator(check_order):
    def compare(left, right):
        if check_order(left, right):
            return -1
        elif check_order(right, left):
            return 1
        else:
            return 0

    return compare


def solve01(input_data):
    # Part 01 - Test Comparator

    # create list from first and second line in every three lines
    pair_l_lol = [json.loads(t) for t in input_data[0::3]]
    pair_r_lol = [json.loads(t) for t in input_data[1::3]]
    # ignore third line

    correct_pair_idx = []
    pair_idx = 0
    for pair_l, pair_r in zip(pair_l_lol, pair_r_lol):
        pair_idx += 1
        # print(f"== Pair {pair_idx} ==")
        if check_order(pair_l, pair_r):
            correct_pair_idx.append(pair_idx)

    correct_pair_idx_sum = sum(correct_pair_idx)

    return correct_pair_idx_sum


def solve02(input_data):
    # Part 02 - Use Comparator to find decoder key in message

    # create list from first and second line in every three lines
    pair_l_lol = [json.loads(t) for t in input_data[0::3]]
    pair_r_lol = [json.loads(t) for t in input_data[1::3]]
    # ignore third line

    decoder_key_start = [[2]]
    decoder_key_end = [[6]]

    # use previous list instead of parsing input
    complete_list = pair_l_lol + pair_r_lol + [decoder_key_start] + [decoder_key_end]

    # Create a sort comparator and sort list
    key = cmp_to_key(check_order_comparator(check_order))
    complete_list_sorted = sorted(complete_list, key=key)

    # find start & end decoder key
    decoder_key_sidx = complete_list_sorted.index(decoder_key_start) + 1
    decoder_key_eidx = complete_list_sorted.index(decoder_key_end) + 1

    # calculate decoder key
    decoder_key = decoder_key_sidx * decoder_key_eidx

    return decoder_key


def parse_data(input_data):
    return input_data.splitlines()


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f'part01 = sum of the indices of correct pairs = {answer01}')

    answer02 = solve02(input_data)
    print(f'part02 = distress signal decoder key = {answer02}')
