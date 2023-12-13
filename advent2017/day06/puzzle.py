#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2017 Day 06: Memory Reallocation
"""
import os


def part01(input_data):
    cycle = solve(input_data)[0]
    return cycle


def part02(input_data):
    loop_size = solve(input_data)[1]
    return loop_size


def solve(memory):
    history = {}
    # use tuple of list as memory key
    memory_key = tuple(memory)

    cycle = 0
    while memory_key not in history and cycle < 20000:
        # store memory_key & cycle seen
        history[memory_key] = cycle
        cycle += 1

        # find index of max memory block
        max_mem = max(memory)
        max_idx = memory.index(max_mem)

        # add largest memory bolck to other blocks
        memory[max_idx] = 0
        while max_mem > 0:
            max_idx = (max_idx + 1) % len(memory)
            memory[max_idx] += 1
            max_mem -= 1

        # define memory key
        memory_key = tuple(memory)

    loop_size = len(history) - history[memory_key]
    return cycle, loop_size


def parse_data(input_data):
    memory = [int(i) for i in input_data.split()]
    return memory


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - infinite loop detected cycle = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - infinite loop size = {answer02}')
