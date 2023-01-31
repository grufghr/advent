#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Solve Puzzle 2016 Day 02: Bathroom Security
"""
import os
import numpy as np
from operator import add


KEYPAD01 = np.array([['1', '2', '3'],
                     ['4', '5', '6'],
                     ['7', '8', '9'],
                     ])

KEYPAD02 = np.array([[' ', ' ', '1', ' ', ' '],
                     [' ', '2', '3', '4', ' '],
                     ['5', '6', '7', '8', '9'],
                     [' ', 'A', 'B', 'C', ' '],
                     [' ', ' ', 'D', ' ', ' '],
                     ])

INSTR = {"U": (-1, 0),
         "D": (1, 0),
         "L": (0, -1),
         "R": (0, 1),
         }


def solve01(input_data):
    start_pos = (1, 1)

    answer = solve(input_data, start_pos, KEYPAD01)
    return answer


def solve02(input_data):
    start_pos = (2, 0)
    answer = solve(input_data, start_pos, KEYPAD02)
    return answer


def solve(instruction_text_list, pos, keypad):

    keypad_size_r = len(keypad) - 1
    keypad_size_c = len(keypad[0]) - 1
    code_list = []

    for code_instruction in instruction_text_list:
        for move in code_instruction:
            pos_n = tuple(map(add, pos, INSTR[move]))
            pos_n = (max(0, min(pos_n[0], keypad_size_r)),
                     max(0, min(pos_n[1], keypad_size_c)))
            if keypad[pos_n] != ' ':
                pos = pos_n

        code_list.append(keypad[pos])

    code = ''.join([str(x) for x in code_list])

    return code


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as input_filehandle:
        input_data = input_filehandle.read().splitlines()

    return input_data


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - bathroom code = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - bathroom code = {answer02}")
