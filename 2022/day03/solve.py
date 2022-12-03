#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022
"""


def calc_priority(c):
    return (ord(c) - ord('a') + 1) if c.islower() else (ord(c) - ord('A') + 27)


def chunk_list(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def solve():
    # read in data file
    rucksack_file = open('rucksack.txt', 'r')
    rucksack_data = rucksack_file.read().splitlines()

    # part 01
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

    print(priority_list_sum)

    # part 02
    badge_list = []
    for group in chunk_list(rucksack_data, 3):
        badge = list(set(group[0]).intersection(
            group[1]).intersection(group[2]))
        badge_list.extend(badge)

    badge_priority_list = [calc_priority(b) for b in badge_list]
    badge_priority_list_sum = sum(badge_priority_list)
    print(badge_priority_list_sum)


if __name__ == '__main__':
    solve()
