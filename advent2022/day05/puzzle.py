#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Solve Puzzle 2022 Day 05: Supply Stacks
"""
import os
import re
import copy


INSTRUCTION_REGEX = re.compile(r'move (\d+) from (\d+) to (\d+)')


def solve01(input_data):
    answer = solve(input_data[0], input_data[1], cratemover9000)
    return answer


def solve02(input_data):
    answer = solve(input_data[0], input_data[1], cratemover9001)
    return answer


def solve(stack_list_immutable, instruction_list, cratemover):

    # use copy of stack list (to avoid changes to input)
    stack_list = copy.deepcopy(stack_list_immutable)

    # process instructions
    for instruction in instruction_list:
        instruction_parsed = INSTRUCTION_REGEX.search(instruction)

        move_count = int(instruction_parsed.group(1))
        stack_from_idx = int(instruction_parsed.group(2)) - 1
        stack_to_idx = int(instruction_parsed.group(3)) - 1

        stack_from = stack_list[stack_from_idx]
        stack_to = stack_list[stack_to_idx]

        # move crates
        cratemover(move_count, stack_from, stack_to)

    # top of each stack
    top_crates = ''
    for stack in stack_list:
        top_crates += stack[-1]

    return top_crates


def cratemover9000(move_count, stack_from, stack_to):
    for moves in range(move_count):
        crate = stack_from.pop()
        stack_to.extend(crate)


def cratemover9001(move_count, stack_from, stack_to):
    split_idx = len(stack_from) - move_count
    crates = stack_from[split_idx:]
    stack_to.extend(crates)
    for moves in range(move_count):
        stack_from.pop()


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, 'r') as input_filehandle:
        input_data_text_list = input_filehandle.read().splitlines()

    input_data_text_list = list(filter(None, input_data_text_list))

    # parse instruction list
    instruction_list = [
        i for i in input_data_text_list if i.startswith('move')]

    # parse stack
    stack_list = list([])

    stack_text_list = reversed([i for i in input_data_text_list
                               if (i not in instruction_list)])
    # invert(reversed) stack so read heading line first
    # stack label is first item in each stack_list
    for line in stack_text_list:
        for i in range(1, len(line), 4):
            stack_idx = (i // 4)
            crate = line[i]
            if not crate.isspace():
                if (stack_idx > len(stack_list) - 1):
                    stack_list.append(list([crate]))
                else:
                    stack_list[stack_idx].append(crate)

    return (stack_list, instruction_list)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - Stack top Crates with CrateMover 9000 = {answer}")

    answer02 = solve02(input_data)
    print(f"part01 - Stack top Crates with CrateMover 9001 = {answer}")
