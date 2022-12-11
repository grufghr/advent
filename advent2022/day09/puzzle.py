#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
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
        exit(f"unknown instruction {move}")
    head = (hr, hc)
    return head


def move_rope(head, rope):
    # print(f"b rope   {rope  }")
    rope_n = [head]
    knot_p = head
    for k, knot in enumerate(rope[1:]):
        distance_between_knots = math.dist(knot_p, knot)
        (r, c) = knot
        while (distance_between_knots > SQRT2):
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

    # return results
    return positions_tail_visited


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, 'r') as input_filehandle:
        input_data_text_list = input_filehandle.read().splitlines()

    return input_data_text_list


if __name__ == '__main__':
    input_data = input_data('input.txt')

    answer = solve(input_data)
    print(f"part01 - Positions tail visited = {answer}")

    answer = solve(input_data, 10)
    print(f"part02 - Positions tail visited = {answer}")
