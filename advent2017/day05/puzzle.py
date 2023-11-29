#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2017 Day 05: A Maze of Twisty Trampolines, All Alike
"""
import os


def solve01(input_data):
    instructions = input_data.copy()
    pos = 0
    step = 0
    while pos >= 0 and pos < len(instructions):
        step += 1
        jump = instructions[pos]
        instructions[pos] += 1
        pos += jump
    return step


def solve02(input_data):
    instructions = input_data.copy()
    pos = 0
    step = 0
    while pos >= 0 and pos < len(instructions):
        step += 1
        jump = instructions[pos]
        if jump >= 3:
            instructions[pos] -= 1
        else:
            instructions[pos] += 1
        pos += jump
    return step


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, 'r') as filehandle:
        input_data = [int(line.rstrip()) for line in filehandle]

    return input_data


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f'part01 - steps to exit = {answer01}')

    answer02 = solve02(input_data)
    print(f'part02 - steps to exit = {answer02}')
