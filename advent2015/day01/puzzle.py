#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Solve Puzzle 2015 Day 01: Not Quite Lisp
"""
import os


def solve01(input_data):
    answer = solve(input_data)
    return answer[0]


def solve02(input_data):
    answer = solve(input_data)
    return answer[1]


def solve(instruction_set):
    # part 01 - start on floor 0
    floor = 0
    # part 02 - step moved into based
    basement_step = 0

    for step, instruction in enumerate(instruction_set):
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1
        else:
            exit(f"Unknown instructions {instruction}")

        if (basement_step == 0) & (floor < 0):
            basement_step = step + 1

    return (floor, basement_step)


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as input_filehandle:
        input_data = input_filehandle.read()

    return input_data


def input_data_iter(input_data):
    for tc, input_data_tc in enumerate(input_data.splitlines()):
        yield tc, input_data_tc


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - Santa ends on floor = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - Santa enters basement on instruction step = {answer02}")
