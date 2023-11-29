#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022 Day 10: Cathode-Ray Tube
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


def solve01(input_data):
    answer = solve(input_data)
    return answer[0]


def solve02(input_data):
    answer = solve(input_data)
    return answer[1]


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

    answer01 = solve01(input_data)
    print(f'part01 - sum of signal strengths = {answer01}')

    answer02 = '\n'.join(solve02(input_data))
    print(f'part02 - crt = \n{answer02}')
