#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021
"""
import os


def solve01(command_list):
    # part 01 -
    horizontal = 0
    depth = 0

    for (direction, unit) in command_list:
        if direction == 'forward':
            horizontal += unit
        elif direction == 'down':
            depth += unit
        elif direction == 'up':
            depth -= unit

    distance = horizontal * depth

    return distance


def solve02(command_list):
    # part 02 -
    aim = 0
    horizontal = 0
    depth = 0

    for (direction, unit) in command_list:
        if direction == 'forward':
            horizontal += unit
            depth += (aim * unit)
        elif direction == 'down':
            aim += unit
        elif direction == 'up':
            aim -= unit

    distance = horizontal * depth

    return distance


def parse_data(input_data):
    command_list = []
    for command in input_data.split('\n'):
        direction, unit = command.split(' ')
        command_list.append((direction, int(unit)))
    return command_list


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - Final horizontal position * final depth = {answer01}")
    answer02 = solve02(input_data)
    print(f"part02 - Final horizontal position * final depth = {answer02}")