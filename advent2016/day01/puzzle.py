#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2016
"""
import os
import re


INSTRUCTION_REGEX = re.compile(r"(L|R)(\d+)")


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

    # return results
    return (distance01, distance02)


def input_data_iter(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as input_filehandle:
        input_txt_list = input_filehandle.read().splitlines()

    for input_txt in input_txt_list:
        yield (input_txt)


if __name__ == '__main__':
    instruction_set = next(input_data_iter('input.txt'))

    answer = solve(instruction_set)

    print(f"Easter Bunny HQ = {answer[0]} blocks")
    print(f"first location you visit twice = {answer[1]} blocks")
