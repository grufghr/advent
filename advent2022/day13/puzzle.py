#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os
import json
from functools import cmp_to_key


def check_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if (left < right):
            # print(f"- Left side is smaller, so inputs are in the right order")
            return True
        if (right < left):
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
        exit(f"do something with {type(left)} {type(right)}")
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


def solve(packet_pair_text_list):

    # create list from first and second line in every three lines
    pair_l_lol = [json.loads(t) for t in packet_pair_text_list[0::3]]
    pair_r_lol = [json.loads(t) for t in packet_pair_text_list[1::3]]
    # ignore third line

    # Part 01 - Test Comparator
    correct_pair_idx = []
    pair_idx = 0
    for pair_l, pair_r in zip(pair_l_lol, pair_r_lol):
        pair_idx += 1
        # print(f"== Pair {pair_idx} ==")
        if check_order(pair_l, pair_r):
            correct_pair_idx.append(pair_idx)

    correct_pair_idx_sum = sum(correct_pair_idx)

    # Part 02 - Use Comparator to find decoder key in message

    decoder_key_start = [[2]]
    decoder_key_end = [[6]]

    # use previous list instead of parsing input
    complete_list = pair_l_lol + pair_r_lol + \
        [decoder_key_start] + [decoder_key_end]

    # Create a sort comparator and sort list
    key = cmp_to_key(check_order_comparator(check_order))
    complete_list_sorted = sorted(complete_list, key=key)

    # find start & end decoder key
    decoder_key_sidx = complete_list_sorted.index(decoder_key_start) + 1
    decoder_key_eidx = complete_list_sorted.index(decoder_key_end) + 1

    # calculate decoder key
    decoder_key = decoder_key_sidx * decoder_key_eidx

    return (correct_pair_idx_sum, decoder_key)


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, 'r') as input_filehandle:
        input_data_text_list = input_filehandle.read().splitlines()

    return input_data_text_list


if __name__ == '__main__':
    input_data = input_data('input.txt')

    answer = solve(input_data)
    print(f"part01 = sum of the indices of correct pairs = {answer[0]}")

    print(f"part02 = distress signal decoder key = {answer[1]}")
