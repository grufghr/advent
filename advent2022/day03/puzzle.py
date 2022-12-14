#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os


def calc_priority(c):
    return (ord(c) - ord('a') + 1) if c.islower() else (ord(c) - ord('A') + 27)


def chunk_list(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def solve(rucksack_data):

    common_list = []
    for rucksack in rucksack_data:
        compartment1 = rucksack[:len(rucksack) // 2]
        compartment2 = rucksack[len(rucksack) // 2:]
        common = ''.join(set(compartment1).intersection(compartment2))
        if len(common) > 1:
            exit("Should there be more than 1 common character?")

        common_list.append(common)

    priority_list = [calc_priority(c) for c in common_list]
    priority_list_sum = sum(priority_list)

    # part 02

    badge_list = []
    for group in chunk_list(rucksack_data, 3):
        badge = list(set(group[0]).intersection(
            group[1]).intersection(group[2]))
        badge_list.extend(badge)

    badge_priority_list = [calc_priority(c) for c in badge_list]
    badge_priority_list_sum = sum(badge_priority_list)

    # return results
    return (priority_list_sum, badge_priority_list_sum)


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, 'r') as filehandle:
        rucksack_data = filehandle.read().splitlines()

    return rucksack_data


if __name__ == '__main__':
    input_data = input_data('input.txt')

    answer = solve(input_data)
    print(f"Sum of the item priorities = {answer[0]}")
    print(f"Sum of the group badges item priorities = {answer[1]}")
