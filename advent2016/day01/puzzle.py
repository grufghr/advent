#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2016 Day 01: No Time for a Taxicab
"""
import os
import re


INSTRUCTION_REGEX = re.compile(r"(L|R)(\d+)")


def solve01(input_data):
    answer = solve(input_data)
    return answer[0]


def solve02(input_data):
    answer = solve(input_data)
    return answer[1]


def solve(instruction_text):

    # part 01 - start at 0,0 facing North
    pos = (0, 0)
    compass = ['N', 'E', 'S', 'W']
    # compass = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # part 02
    visited = set()
    visited.add(pos)
    bunny_hq = None

    instruction_list = [x.strip() for x in instruction_text.split(',')]
    for instruction in instruction_list:
        match_i = INSTRUCTION_REGEX.search(instruction)
        direction, steps = match_i.groups()
        steps = int(steps)

        if direction == 'L':
            compass = compass[1:] + list(compass[0])
        elif direction == 'R':
            compass = list(compass[-1]) + compass[:-1]

        for s in range(0, steps):

            if compass[0] == 'N':
                pos = (pos[0], pos[1] - 1)
            elif compass[0] == 'E':
                pos = (pos[0] + 1, pos[1])
            elif compass[0] == 'S':
                pos = (pos[0], pos[1] + 1)
            elif compass[0] == 'W':
                pos = (pos[0] - 1, pos[1])

            if not bunny_hq:
                if pos not in visited:
                    visited.add(pos)
                else:
                    bunny_hq = pos

    distance01 = sum([abs(x) for x in list(pos)])

    if bunny_hq:
        distance02 = sum([abs(x) for x in list(bunny_hq)])
    else:
        distance02 = None

    return (distance01, distance02)


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return input_data


def input_data_iter(input_data):
    for tc, test_input_data in enumerate(input_data.splitlines()):
        yield tc, test_input_data


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - Easter Bunny HQ = {answer01} blocks")

    answer02 = solve02(input_data)
    print(f"part02 - First location visited twice = {answer02} blocks")
