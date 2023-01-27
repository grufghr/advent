#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os
import re
from collections import deque

TYPE1_REGEX = re.compile(r"^(\d+|[a-z]+) -> ([a-z]+)")
TYPE2_REGEX = re.compile(r"^(NOT) (\d+|[a-z]+) -> ([a-z]+)")
TYPE3_REGEX = re.compile(
    r"^(\d+|[a-z]+) (AND|OR|LSHIFT|RSHIFT) (\d+|[a-z]+) -> ([a-z]+)")


def solve01(input_data):
    # part 01 - find wire 'a' signal

    signals = solve_signals(input_data)
    return signals['a']


def solve02(input_data):
    # part 02 - replace 'b' with 'a' part 01 and recalculate

    signals = solve_signals(input_data)

    instructions_map = {k: v for (k, v) in input_data}
    instructions_map['b'] = ('=', signals['a'], 0)
    input_data_n = [(k, v) for k, v in instructions_map.items()]

    signals = solve_signals(input_data_n)
    return signals['a']


def solve_signals(input_data):

    instructions = input_data
    signals = {}

    q = deque(instructions)
    while q:
        wire, (op, a, b) = q.popleft()

        if not isinstance(a, int):
            if a.isdigit():
                a = int(a)
            elif a in signals.keys():
                a = signals[a]

        if not isinstance(b, int):
            if b.isdigit():
                b = int(b)
            elif b in signals.keys():
                b = signals[b]

        if isinstance(a, int) and isinstance(b, int):
            if op == '=':
                signals[wire] = int(a)
            elif op == 'AND':
                signals[wire] = a & b
            elif op == 'OR':
                signals[wire] = a | b
            elif op == 'NOT':
                signals[wire] = ~a & 65535
            elif op == 'RSHIFT':
                signals[wire] = a >> b
            elif op == 'LSHIFT':
                signals[wire] = a << b
            else:
                exit(f"unknown op {op}")
        else:
            q.append((wire, (op, a, b)))

    return signals


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read i[]nput data from file
    with open(input_data_file, 'r') as input_filehandle:
        input_data_text_list = input_filehandle.read().splitlines()

    # parse input file
    instruction_list = []
    for instruction in input_data_text_list:
        if match_m := TYPE1_REGEX.search(instruction):
            instr = (match_m.group(2), ('=',
                                        match_m.group(1),
                                        0))
            instruction_list.append(instr)
        elif match_m := TYPE2_REGEX.search(instruction):
            instr = (match_m.group(3), (match_m.group(1),
                                        match_m.group(2),
                                        0))
            instruction_list.append(instr)
        elif match_m := TYPE3_REGEX.search(instruction):
            instr = (match_m.group(4), (match_m.group(2),
                                        match_m.group(1),
                                        match_m.group(3)))
            instruction_list.append(instr)
        else:
            exit(f"unknown instruction '{instruction}'")

    return instruction_list


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - a = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - a = {answer02}")
