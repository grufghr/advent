#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021 Day 12: Passage Pathing
"""
import os
from collections import deque

START = "start"
END = "end"


def solve01(input_data):
    return traverse_caves(input_data, 1)


def solve02(input_data):
    return traverse_caves(input_data, 2)


def traverse_caves(cave_map, max_visits):
    path_count = 0

    q = deque([([START], False)])
    while q:
        path, already_max = q.pop()
        cave = path[-1]

        if cave == END:
            path_count += 1
        else:
            exits = cave_map[cave]
            for exit_n in exits:
                # skip going back to start cave
                if exit_n == START:
                    continue

                if exit_n == END or exit_n.isupper() or exit_n not in path:
                    path_n = path.copy()
                    path_n.append(exit_n)
                    q.append((path_n, already_max))
                elif not already_max and path.count(exit_n) < max_visits:
                    path_n = path.copy()
                    path_n.append(exit_n)
                    q.append((path_n, True))

    return path_count


def parse_input(input_data):
    graph = {}
    for edge_txt in input_data.splitlines():
        edge = tuple(edge_txt.split("-"))

        nodeA = edge[0]
        nodeB = edge[1]

        if nodeA in graph.keys():
            graph[nodeA].add(nodeB)
        else:
            graph[nodeA] = set([nodeB])

        if nodeB in graph.keys():
            graph[nodeB].add(nodeA)
        else:
            graph[nodeB] = set([nodeA])

    return graph


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, "r") as filehandle:
        input_data = filehandle.read()

    return parse_input(input_data)


if __name__ == "__main__":
    input_data = load_data("input.txt")

    answer01 = solve01(input_data)
    print(f"part01 - paths through cave system = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - paths through cave system = {answer02}")
