#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021
"""
import os


def solve(input_data):

    # part 01
    command_data_list = []
    for command in input_data.split('\n'):
        direction, unit = command.split(' ')
        command_data_list.append((direction, int(unit)))

    horizontal = 0
    depth = 0

    for (direction, unit) in command_data_list:
        if direction == 'forward':
            horizontal += unit
        elif direction == 'down':
            depth += unit
        elif direction == 'up':
            depth -= unit

    distance1 = horizontal * depth

    # part 02
    aim = 0
    horizontal = 0
    depth = 0

    for (direction, unit) in command_data_list:
        if direction == 'forward':
            horizontal += unit
            depth += (aim * unit)
        elif direction == 'down':
            aim += unit
        elif direction == 'up':
            aim -= unit

    distance2 = horizontal * depth

    # return results
    return (distance1, distance2)


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, 'r') as command_file:
        command_file_text = command_file.read()

    return command_file_text


if __name__ == '__main__':
    input_data = input_data('input.txt')

    answer = solve(input_data)
    print(f"part 01 - Final horizontal position * final depth = {answer[0]}.")
    print(f"part 02 - Final horizontal position * final depth = {answer[1]}.")
