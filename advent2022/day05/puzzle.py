#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os
import re
import copy


INSTRUCTION_REGEX = re.compile(r'move (\d+) from (\d+) to (\d+)')


def solve(input_data_file):
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

    # preseve copy of stack list for part 2
    stack_list_0 = copy.deepcopy(stack_list)

    # part 01

    # process instructions
    for instruction in instruction_list:
        instruction_parsed = INSTRUCTION_REGEX.search(instruction)

        move_count = int(instruction_parsed.group(1))
        stack_from_idx = int(instruction_parsed.group(2)) - 1
        stack_to_idx = int(instruction_parsed.group(3)) - 1

        for moves in range(move_count):
            crate = stack_list[stack_from_idx].pop()
            stack_list[stack_to_idx].extend(crate)

    # top of each stack
    top_of_stacks1 = ''
    for stack in stack_list:
        top_of_stacks1 += stack[-1]

    # part 02
    stack_list = copy.deepcopy(stack_list_0)

    # process instructions
    for instruction in instruction_list:
        instruction_parsed = INSTRUCTION_REGEX.search(instruction)

        move_count = int(instruction_parsed.group(1))
        stack_from_idx = int(instruction_parsed.group(2)) - 1
        stack_to_idx = int(instruction_parsed.group(3)) - 1

        stack_split_idx = len(stack_list[stack_from_idx]) - move_count

        stack_from = stack_list[stack_from_idx]

        stack_list[stack_to_idx].extend(stack_from[stack_split_idx:])
        stack_list[stack_from_idx] = stack_from[:stack_split_idx]

    # top of each stack
    top_of_stacks2 = ''
    for stack in stack_list:
        top_of_stacks2 += stack[-1]

    # return results
    return (top_of_stacks1, top_of_stacks2)


if __name__ == '__main__':
    input_data_file = os.path.join(
        os.path.dirname(__file__), 'input.txt')

    answers = solve(input_data_file)
    print(f"Crates at top of stacks with CrateMover 9000 = {answers[0]}")
    print(f"Crates at top of stacks with CrateMover 9001 = {answers[1]}")
