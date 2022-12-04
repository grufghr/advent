#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021
"""
import os


def solve(input_data_file):
    # read input data from file
    with open(input_data_file, 'r') as instructions_file:
        instructions_data = instructions_file.read().splitlines()

    # part 01
    result_floor = []
    result_basement = []

    for idx, instruction_set in enumerate(instructions_data):
        result_floor.append(0)
        result_basement.append(0)

        for i in range(len(instruction_set)):
            instruction = instruction_set[i]
            if instruction == '(':
                result_floor[idx] += 1
            elif instruction == ')':
                result_floor[idx] -= 1
            else:
                exit(f"Unknown instructions {instruction}")

            if (result_basement[idx] == 0) & (result_floor[idx] < 0):
                result_basement[idx] = i + 1

    # return results
    return (result_floor, result_basement)


if __name__ == '__main__':
    input_data_file = os.path.join(
        os.path.dirname(__file__), 'input.txt')

    answers = solve(input_data_file)
    print(f"Santa floor = {answers[0][0]}")
    print(f"Santa enters basement on instruction = {answers[1][0]}")
