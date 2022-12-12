#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os
import re

COMMAND_ADDX = re.compile(r'addx (\d+|-\d+)')


def update_test_signal(cycle, x):
    test_cycle = 20 + (40 * ((cycle + 20 - 1) // 40))
    if cycle == test_cycle:
        return cycle * x
    return None


def update_crt(crt, cycle, x):
    c = (cycle - 1) % 40
    if (c >= (x - 1)) and (c <= (x + 1)):
        r = cycle // 40
        crt[r][c] = '#'
    return crt


def solve(instruction_list):

    x = 1
    cycle = 0

    # part 01
    signal_strength_list = []

    # part 02
    crt = [['.'] * 40 for i in range(7)]

    # process input file
    for instruction in instruction_list:

        if instruction == 'noop':
            cycle += 1
            if signal_strength := update_test_signal(cycle, x):
                signal_strength_list.append(signal_strength)
            crt = update_crt(crt, cycle, x)

        if match := COMMAND_ADDX.search(instruction):
            cycle += 1
            if signal_strength := update_test_signal(cycle, x):
                signal_strength_list.append(signal_strength)
            crt = update_crt(crt, cycle, x)

            cycle += 1
            if signal_strength := update_test_signal(cycle, x):
                signal_strength_list.append(signal_strength)
            crt = update_crt(crt, cycle, x)

            x += int(match.group(1))

    # part 01
    # print(sum(signal_strength_list))
    sum_signal_strength = sum(signal_strength_list)

    # part 02
    crt = [''.join(row) for row in crt]
    # print('\n'.join(crt))
    return (sum_signal_strength, crt)


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, 'r') as input_filehandle:
        input_data_text_list = input_filehandle.read().splitlines()

    return input_data_text_list


if __name__ == '__main__':
    input_data = input_data('input.txt')

    answer = solve(input_data)
    print(f"part01 - sum of signal strengths = {answer[0]}")

    answer_part02 = '\n'.join(answer[1])
    print(f"part02 - crt = \n{answer_part02}")
