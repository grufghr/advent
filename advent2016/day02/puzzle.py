#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
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


def solve(instruction_text_list):

    # parse input file
    code_list01 = []
    code_list02 = []

    pos01 = (1, 1)
    pos02 = (2, 0)

    for code_instruction in instruction_text_list:
        for move in code_instruction:
            pos01_n = tuple(map(add, pos01, INSTR[move]))
            pos01_n = (max(0, min(pos01_n[0], 2)),
                       max(0, min(pos01_n[1], 2)))
            pos01 = pos01_n

            pos02_n = tuple(map(add, pos02, INSTR[move]))
            pos02_n = (max(0, min(pos02_n[0], 4)),
                       max(0, min(pos02_n[1], 4)))

            if KEYPAD02[pos02_n] != ' ':
                pos02 = pos02_n

        code_list01.append(KEYPAD01[pos01])
        code_list02.append(KEYPAD02[pos02])

    # part 01 - code for KEYPAD 01
    code01 = ''.join([str(x) for x in code_list01])

    # part 02 - code for KEYPAD 02
    code02 = ''.join([str(x) for x in code_list02])

    return (code01, code02)


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, 'r') as input_filehandle:
        input_data_text_list = input_filehandle.read().splitlines()

    return input_data_text_list


if __name__ == '__main__':
    input_data = input_data('input.txt')

    answer = solve(input_data)
    print(f"part01 - bathroom code = {answer[0]}")

    print(f"part02 - bathroom code = {answer[1]}")
