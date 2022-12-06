#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021
"""
import os


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

    # return results
    return (floor, basement_step)


def input_data_iter(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as input_filehandle:
        input_txt_list = input_filehandle.read().splitlines()

    for input_txt in input_txt_list:
        yield (input_txt)


if __name__ == '__main__':
    instruction_set = next(input_data_iter('input.txt'))

    answer = solve(instruction_set)

    print(f"Santa ends on floor = {answer[0]}")
    print(f"Santa enters basement on instruction step = {answer[1]}")
