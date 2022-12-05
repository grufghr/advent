#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021
"""
import os
import numpy as np


def deliver_presents(instruction_set, delivery_num=1):

    # create basic 3x3 array (to start)
    present_np = np.zeros((3, 3), dtype=int)

    # all delivery people start at centre of present_np [r,c]
    pos = np.array([[1, 1]] * delivery_num)

    # each delivery person delivers present to first house
    present_np[1][1] += delivery_num

    # each delivery person moves according to instruction
    for i, instruction in enumerate(instruction_set):
        p = (i % delivery_num)
        if instruction == 'v':
            pos[p][0] += 1
        elif instruction == '^':
            pos[p][0] -= 1
        elif instruction == '>':
            pos[p][1] += 1
        elif instruction == '<':
            pos[p][1] -= 1
        else:
            exit(f"Unknown instructions {instruction}")

        # insert/append to present_np if delivery person is out of bounds
        shape = present_np.shape
        if (pos[p][0] > (shape[0] - 1)):
            zr = np.zeros((1, shape[1]), dtype=int)
            present_np = np.append(present_np, zr, axis=0)
        elif (pos[p][0] < 0):
            present_np = np.insert(present_np, 0, 0, axis=0)
            # adjust all delivery people (to account for insert)
            pos[:, 0] += 1
            pos[p][0] = 0
        elif (pos[p][1] > (shape[1] - 1)):
            zc = np.zeros((shape[0], 1), dtype=int)
            present_np = np.append(present_np, zc, axis=1)
        elif (pos[p][1] < 0):
            present_np = np.insert(present_np, 0, 0, axis=1)
            # adjust all delivery people (to account for insert)
            pos[:, 1] += 1
            pos[p][1] = 0

        # deliver present
        present_np[pos[p][0]][pos[p][1]] += 1

    house_count = np.count_nonzero(present_np)

    return house_count


def solve(input_data_file):
    # read input data from file
    with open(input_data_file, 'r') as instructions_file:
        instructions_data = instructions_file.read().splitlines()

    # part 01
    non_zero_count01 = []

    for idx, instruction_set in enumerate(instructions_data):
        count = deliver_presents(instruction_set)
        non_zero_count01.append(count)

    # part 02
    non_zero_count02 = []

    for idx, instruction_set in enumerate(instructions_data):
        count = deliver_presents(instruction_set, 2)
        non_zero_count02.append(count)

    # return results
    return (non_zero_count01, non_zero_count02)


if __name__ == '__main__':
    input_data_file = os.path.join(
        os.path.dirname(__file__), 'input.txt')

    answers = solve(input_data_file)
    print(f"Houses visited with santa = {answers[0]}")
    print(f"Houses visited with santa & robot = {answers[1]}")
