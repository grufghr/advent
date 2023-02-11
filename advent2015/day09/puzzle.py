#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 Day 09: All in a Single Night
"""
import os
import re
from collections import deque


LINE_REGEX = re.compile(r"([a-zA-Z]+) to ([a-zA-Z]+) = (\d+)")


def solve01(input_data):
    # part 01 - sortest path between two points (visit all once only)

    path_all = find_all_paths(input_data)
    shortest_path = path_all[0]
    shortest_distance = shortest_path[0]
    return shortest_distance


def solve02(input_data):
    # part 02 - longest path between two points (visit all once only)

    path_all = find_all_paths(input_data)
    longest_path = path_all[-1]
    longest_distance = longest_path[0]
    return longest_distance


def find_all_paths(distances):

    # print(distances)
    locations_all = set(distances.keys())
    path_all = []

    q = deque([([x], 0) for x in locations_all])
    while q:
        path, distance = q.popleft()
        loc_a = path[-1]
        # print("qpop", path, visited, distance)
        # print("loc_a", loc_a)

        if set(path) != locations_all:
            loc_b_list = list(distances[loc_a].keys())
            for loc_b in loc_b_list:
                if loc_b not in path:
                    path_n = path.copy()
                    path_n.append(loc_b)
                    distance_n = distance + distances[loc_a][loc_b]

                    q.append((path_n, distance_n))
        else:
            path_all.append((distance, path))

    path_all.sort()
    return path_all


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.readlines()

    # parse instruction list
    distances = dict()
    for line_text in input_data:
        match_b = LINE_REGEX.search(line_text)
        loc_a, loc_b, distance = match_b.groups()

        if loc_a not in distances.keys():
            distances[loc_a] = {}
        distances[loc_a][loc_b] = int(distance)
        if loc_b not in distances.keys():
            distances[loc_b] = {}
        distances[loc_b][loc_a] = int(distance)

    return distances


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - shortest route distance = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - longest route distance = {answer02}")
