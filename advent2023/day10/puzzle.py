#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 10: Pipe Maze
"""
import os
from collections import deque


def part01(input_data):
    field = input_data

    start = get_start(field)
    pipes = get_pipes_distance(field, start)
    distance = max(pipes.values())

    return distance


def part02(input_data):
    field = input_data

    # find pipes
    start = get_start(field)
    pipes = get_pipes_distance(field, start)
    pipes = set(pipes.keys())

    # If you shoot a ray in any direction from the pixel
    # and it crosses the boundary an odd number of times, it's inside.
    # but if it crosses an even number of times, it's outside.
    # Works for all enclosed shapes, even self-intersecting and non-convex ones.
    enclosed = 0
    rmax = len(field)
    cmax = len(field[0])
    for r in range(rmax):
        for c in range(cmax):
            if (r, c) in pipes:
                continue

            crosses = 0
            r2 = r
            c2 = c
            while r2 < rmax and c2 < cmax:
                f2 = field[r2][c2]
                if (r2, c2) in pipes and f2 != 'L' and f2 != '7':
                    crosses += 1
                r2 += 1
                c2 += 1

            if crosses % 2 == 1:
                enclosed += 1
                # field[r][c] = 'I'
            # else:
            # field[r][c] = 'O'

    return enclosed


def get_start(field):
    for r in range(len(field)):
        for c in range(len(field[0])):
            if field[r][c] == 'S':
                return (r, c)
    return None


def get_pipes_distance(field, start):
    d = 0
    visited = {}
    q = deque([(start, 0)])
    while q and d < 10000:
        pos, d = q.popleft()
        if pos not in visited.keys():
            visited[pos] = d
            d += 1

            exits = get_exits(field, pos[0], pos[1])
            q.append((exits[0], d))
            q.append((exits[1], d))
    return visited


def get_exits(field, r, c):
    if field[r][c] == '|' or field[r][c] == 'S':
        if exit_n(field, r, c) and exit_s(field, r, c):
            return ((r - 1, c), (r + 1, c))
    if field[r][c] == 'L' or field[r][c] == 'S':
        if exit_n(field, r, c) and exit_e(field, r, c):
            return ((r - 1, c), (r, c + 1))
    if field[r][c] == 'F' or field[r][c] == 'S':
        if exit_s(field, r, c) and exit_e(field, r, c):
            return ((r + 1, c), (r, c + 1))
    if field[r][c] == '7' or field[r][c] == 'S':
        if exit_s(field, r, c) and exit_w(field, r, c):
            return ((r + 1, c), (r, c - 1))
    if field[r][c] == 'J' or field[r][c] == 'S':
        if exit_n(field, r, c) and exit_w(field, r, c):
            return ((r - 1, c), (r, c - 1))
    if field[r][c] == '-' or field[r][c] == 'S':
        if exit_w(field, r, c) and exit_e(field, r, c):
            return ((r, c - 1), (r, c + 1))
    return None


def exit_n(field, r, c):
    if r <= 0:
        return False
    return field[r - 1][c] in ('7', 'F', '|', 'S')


def exit_e(field, r, c):
    if c >= (len(field[0]) - 1):
        return False
    return field[r][c + 1] in ('7', 'J', '-', 'S')


def exit_s(field, r, c):
    if r >= (len(field) - 1):
        return False
    return field[r + 1][c] in ('L', 'J', '|', 'S')


def exit_w(field, r, c):
    if c <= 0:
        return False
    return field[r][c - 1] in ('L', 'F', '-', 'S')


def parse_data(input_data):
    field = []
    for line_text in input_data.splitlines():
        field_line = [x for x in line_text]
        field.append(field_line)

    return field


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - furthest distance from start = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - enclosed tiles = {answer02}')
