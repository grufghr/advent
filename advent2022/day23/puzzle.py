#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os
import operator


dirs = {"N": [(0, -1), (1, -1), (-1, -1)],
        "S": [(0, 1), (1, 1,), (-1, 1)],
        "W": [(-1, 0), (-1, 1), (-1, -1)],
        "E": [(1, 0), (1, 1), (1, -1)]}
direction_all = set(dirs["N"] + dirs["S"] + dirs["W"] + dirs["E"])


def add(t1, t2):
    return tuple(map(operator.add, t1, t2))


def visualise(grove_map):
    x_vals = [x for x, y in grove_map]
    y_vals = [y for x, y in grove_map]

    for y in range(min(y_vals) - 1, max(y_vals) + 1):
        line = ''
        for x in range(min(x_vals) - 1, max(x_vals) + 1):
            if (x, y) in grove_map:
                line += '#'
            else:
                line += '.'
        print(line)


def solve(grove_map_list, max_rounds):

    direction_order = ["N", "S", "W", "E"]

    # parse input
    grove_map = []
    for y, line in enumerate(grove_map_list):
        for x, pos in enumerate(line):
            if pos == '#':
                elf = (x, y)
                grove_map.append(elf)

    # visualise(grove_map)

    # part 01 - move elves for 10 rounds

    round_num = 0
    movement = True
    while round_num < max_rounds and movement:
        round_num += 1
        print("round ", round_num)

        # 1st part of round
        moves = {}
        for idx, elf in enumerate(grove_map):
            if not any(add(elf, direction) in grove_map for direction in direction_all):
                # elf does need to move
                continue

            for diro in direction_order:
                if not any(add(elf, direction) in grove_map for direction in dirs[diro]):
                    elf_p = add(elf, dirs[diro][0])
                    if elf_p not in moves.keys():
                        moves[elf_p] = idx
                    else:
                        # duplicate => set value to None
                        moves[elf_p] = None
                    break

        # rotate direction order queue
        direction_order.append(direction_order.pop(0))

        # 2nd part of round
        movement = False
        for elf_p, idx in moves.items():
            if idx is not None:
                grove_map[idx] = elf_p
                movement = True

        # visualise(grove_map)

    x_vals = [x for x, y in grove_map]
    y_vals = [y for x, y in grove_map]
    grid_size = (max(x_vals) - min(x_vals) + 1) * \
        (max(y_vals) - min(y_vals) + 1)

    empty_grids = grid_size - len(grove_map)

    return (empty_grids, round_num)


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read i[]nput data from file
    with open(input_data_file, 'r') as input_filehandle:
        input_data_text_list = input_filehandle.read().splitlines()

    return input_data_text_list


if __name__ == '__main__':
    input_data = input_data('input.txt')

    answer = solve(input_data, 10)
    print(f"part01 - empty ground = {answer[0]}")

    answer = solve(input_data, 1500)
    print(f"part02 - round nothing moved = {answer[1]}")
