#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2019 Day 02: 1202 Program Alarm
"""
import os
from collections import deque


def solve01(input_data):
    program = input_data

    # replace 1202 error
    program[1] = 12
    program[2] = 2

    result = run_program(program)
    return result


def solve02(input_data):
    # add zeros to avoid index range exceptions
    program = input_data + ([0] * 100)

    for noun in range(100):
        for verb in range(100):
            # replace 1202 error
            program[1] = noun
            program[2] = verb
            result = run_program(program)
            if result == 19690720:
                return (100 * noun) + verb
    return None


def run_program(input_data):
    program = input_data.copy()

    q = deque(program)
    command = q.popleft()
    while command != 99:
        if command == 1:
            a = q.popleft()
            b = q.popleft()
            c = q.popleft()
            program[c] = program[a] + program[b]
        elif command == 2:
            a = q.popleft()
            b = q.popleft()
            c = q.popleft()
            program[c] = program[a] * program[b]
        command = q.popleft()
    return program[0]


def parse_data(input_data):
    input_data = input_data.split(',')
    return [int(x) for x in input_data]


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f'part01 - value at position 0 = {answer01}')

    answer02 = solve02(input_data)
    print(f'part02 - 100 * verb + noun = {answer02}')
