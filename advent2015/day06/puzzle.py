#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Solve Puzzle 2015 Day 06: Probably a Fire Hazard
"""
import os
import re
import numpy as np


LIGHT_INSTRUCTIONS_REGEX = re.compile(
    r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")


def solve01(input_data):
    answer = solve(input_data)
    return answer[0]


def solve02(input_data):
    answer = solve(input_data)
    return answer[1]


def solve(instruction_list):

    light_grid01 = np.zeros((1000, 1000), dtype=bool)
    light_grid02 = np.zeros((1000, 1000), dtype=int)

    # process instruction list
    for instruction, coord_s, coord_e in instruction_list:
        sr, sc = coord_s
        er, ec = coord_e
        ec = ec + 1
        er = er + 1

        if instruction == "turn on":
            light_grid01[sr:er, sc:ec] = True
            light_grid02[sr:er, sc:ec] = light_grid02[sr:er, sc:ec] + 1
        elif instruction == "turn off":
            light_grid01[sr:er, sc:ec] = False
            light_grid02[sr:er, sc:ec] = light_grid02[sr:er, sc:ec] - 1
            light_grid02[light_grid02 < 0] = 0
        elif instruction == "toggle":
            light_grid01[sr:er, sc:ec] = ~light_grid01[sr:er, sc:ec]
            light_grid02[sr:er, sc:ec] = light_grid02[sr:er, sc:ec] + 2
        else:
            exit(f"unknown instruction '{instruction}'")

    lights_on = np.count_nonzero(light_grid01)
    brightness_sum = np.sum(light_grid02)

    return (lights_on, brightness_sum)


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.readlines()

    # parse instruction list
    instruction_list = []
    for line_text in input_data:
        match_b = LIGHT_INSTRUCTIONS_REGEX.search(line_text)
        instruction, sr, sc, er, ec = match_b.groups()
        instruction_list.append(
            (instruction, (int(sr), int(sc)), (int(er), int(ec))))
    return instruction_list


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - lights on = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - brightness sum = {answer02}")
