#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 Day 14: Reindeer Olympics
"""
import os
import re

INPUT_REGEX = re.compile(r'(.*) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.')


def solve01(input_data, seconds):
    reindeer_stats = input_data

    reindeer_dist = []
    for r, stats_r in reindeer_stats.items():
        dist = calc_dist(stats_r, int(seconds))
        reindeer_dist.append(dist)

    # max distance returned by a reindeer
    return max(reindeer_dist)


def solve02(input_data, seconds):
    reindeer_stats = input_data

    reindeer_dist = {r: 0 for r in reindeer_stats.keys()}
    reindeer_score = {r: 0 for r in reindeer_stats.keys()}

    for s in range(1, int(seconds)):
        for r, stats_r in reindeer_stats.items():
            reindeer_dist[r] = calc_dist(stats_r, s)

        max_dist = max(reindeer_dist.values())
        reindeer_lead = [r for r, d in reindeer_dist.items() if d == max_dist]
        for r in reindeer_lead:
            reindeer_score[r] += 1

    # max score by reindeer
    max_score = max(reindeer_score.values())
    return max_score


def calc_dist(stats_r, seconds):
    cycle_t = stats_r[1] + stats_r[2]
    cycles_d = seconds // cycle_t
    cycles_m = seconds % cycle_t
    dist_d = (stats_r[0] * stats_r[1]) * cycles_d

    if cycles_m > stats_r[1]:
        dist_m = stats_r[0] * stats_r[1]
    else:
        dist_m = stats_r[0] * cycles_m
    dist = dist_d + dist_m
    return dist


def parse_data(input_data):
    reindeer_stats = {}
    for line_text in input_data.splitlines():
        match_m = re.findall(INPUT_REGEX, line_text)[0]
        reindeer_stats[match_m[0]] = (int(match_m[1]), int(match_m[2]), int(match_m[3]))

    # reindeer stats
    return reindeer_stats


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data, 2503)
    print(f'part01 - winning reindeer traveled = {answer01}')

    answer02 = solve02(input_data, 2503)
    print(f'part02 - winning reindeer score = {answer02}')
