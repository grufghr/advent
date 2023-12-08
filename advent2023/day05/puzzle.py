#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 05: If You Give A Seed A Fertilizer
"""
import os
import re
import math
from itertools import islice


def part01(input_data):
    seeds, almanac = input_data

    location_min = math.inf
    # for each seed find location is less than location_min
    for seed in seeds:
        loc = find_location(seed, almanac)
        location_min = min(location_min, loc)

    return location_min


def part02(input_data):
    seeds, almanac = input_data

    # range search all ranges to find closest match
    seeds_local = local_search(seeds, almanac)
    # seeds local = [(s1, 1), (s2, 2)]

    # find lowest location in seeds_local
    seeds_batch = batched(seeds_local, 2)

    # find local min in range
    location_min = math.inf
    for seed_r in seeds_batch:
        # create list of seeds from range
        seed_list = list(range(seed_r[0], seed_r[0] + seed_r[1]))

        # for each seed find location is less than location_min
        for seed in seed_list:
            loc_m = find_location(seed, almanac)
            if loc_m < location_min:
                location_min = loc_m

    return location_min


def local_search(seeds, almanac):
    # check boundaries of each range to find local heuristic search

    range_n = find_local_min(seeds, almanac)
    inf_loop = 1000

    # repeat while left range length > 1
    while range_n[1] > 1:
        # infinite loop checker
        inf_loop -= 1
        if inf_loop <= 0:
            raise Exception('potential infinite loop')

        # split range at mid point, creating two sublists
        mp = range_n[1] // 2
        range_a = (range_n[0], mp)
        # note: mp + 1 to cater for odd length
        range_b = (range_n[0] + mp, mp + 1)
        seeds_n = list(range_a) + list(range_b)

        range_n = find_local_min(seeds_n, almanac)

    # should have list of [s1, 1, s2, 2]
    # which represent 3 seeds, one of which produces lowest location
    return seeds_n


def find_local_min(seeds, almanac):
    # seeds = [s1, l1, s2, l2, s3, l3 ...]
    # given list of ranges starting at s1, s2, s3 ...
    #   and having length r1, l2, l3 ...
    # find range with has lowest location

    # batch list of seeds -> [(s1, l1), (s2, l2)]
    seed_ranges = batched(seeds, 2)

    # find seed range with lowest location
    loc_min = math.inf
    seed_min = None
    for seed in seed_ranges:
        # check local range start (s)
        loc = find_location(seed[0], almanac)
        if loc < loc_min:
            loc_min = loc
            seed_min = seed

        # check local range end (s + l)
        loc = find_location(seed[0] + seed[1], almanac)
        if loc < loc_min:
            loc_min = loc
            seed_min = seed

    return seed_min


def find_location(seed, almanac):
    # given seed find location

    # start with loc = seed
    loc = seed

    # iterate over pages of almanac
    for page, almanac_row in almanac.items():
        loc_n = loc

        # iterate over rows on almanac page
        for destination, source, rl in almanac_row:
            # if match rowing
            if source <= loc <= (source + rl):
                loc_n = destination + (loc - source)
                break

        # next location (use same value if not changed)
        loc = loc_n
    return loc


def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    # implemented in python 3.12
    if n < 1:
        raise ValueError('n must be at least one')
    batched_list = []
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        batched_list.append(batch)
    return batched_list


def parse_data(input_data):
    almanac = {}
    key = 'seeds'
    for line_text in input_data.splitlines():
        if line_text.startswith('seeds: '):
            seeds = list(map(int, re.findall(r'(\d+)', line_text)))
        elif match := re.findall(r'(.*) map:', line_text):
            key = match[0]
            almanac[key] = []
        elif line_text:
            range_list = tuple(list(map(int, re.findall(r'(\d+)', line_text))))
            almanac[key].append(range_list)
    return (seeds, almanac)


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - lowest location = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - lowest location = {answer02}')
