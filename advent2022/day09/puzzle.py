#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022 Day 09: Rope Bridge
"""
import os
import math

SQRT2 = math.sqrt(2)


def move_head(head, direction):
    (hr, hc) = head
    if direction == 'R':
        hc = hc + 1
    elif direction == 'L':
        hc = hc - 1
    elif direction == 'U':
        hr = hr - 1
    elif direction == 'D':
        hr = hr + 1
    else:
        exit(f'unknown instruction {direction}')
    head = (hr, hc)
    return head


def move_rope(head, rope):
    # print(f"b rope   {rope  }")
    rope_n = [head]
    knot_p = head
    for k, knot in enumerate(rope[1:]):
        distance_between_knots = math.dist(knot_p, knot)
        (r, c) = knot
        while distance_between_knots > SQRT2:
            # print(f"{knot_p} -> {k} ({r},{c}) = {distance_between_knots}")
            if knot_p[0] > knot[0]:
                r = r + 1
            elif knot_p[0] < knot[0]:
                r = r - 1
            if knot_p[1] > knot[1]:
                c = c + 1
            elif knot_p[1] < knot[1]:
                c = c - 1
            distance_between_knots = math.dist(knot_p, (r, c))

        knot_p = (r, c)
        rope_n.append(knot_p)

    # print(f"a rope_n {rope_n}")
    return rope_n


def part01(input_data):
    answer = solve(input_data, 2)
    return answer


def part02(input_data):
    answer = solve(input_data, 10)
    return answer


def solve(instruction_list, rope_knots=2):
    head = (0, 0)
    rope = [head] * rope_knots
    tail = (0, 0)

    head_pos = [tuple(head)]
    tail_pos = [tuple(tail)]

    for instruction in instruction_list:
        direction, steps = instruction.split(' ', 1)
        # print(f"move {direction} for {steps} steps")

        for s in range(int(steps)):
            head = move_head(head, direction)
            rope = move_rope(head, rope)
            tail = rope[-1]

            tail_pos.append(tuple(tail))
            head_pos.append(tuple(head))

    positions_tail_visited = len(set(tail_pos))

    return positions_tail_visited


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

    answer01 = part01(input_data)
    print(f'part01 - Positions tail visited = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - Positions tail visited = {answer02}')
