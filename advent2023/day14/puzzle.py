#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 14: Parabolic Reflector Dish
"""
import os


def calc_size(dish):
    return (max([p[0] for p in dish.keys()]), max([p[1] for p in dish.keys()]))
    

def calc_weight(dish_size, rocks):
    return sum([dish_size[0] - r[0] + 1 for r in rocks])
    

def calc_state(dish_size, rocks):
    return sum([((r[1] * (dish_size[0] + 1)) + r[0]) for r in rocks])

def part01(input_data):
    dish = input_data
    dish_size = calc_size(dish)
    rocks = set(k for k, t in dish.items() if t == 'O')
    cubes = set(k for k, t in dish.items() if t == '#')

    rocks = tilt(rocks, cubes, 'N', dish_size)
    weight = calc_weight(dish_size, rocks)

    return weight


def part02(input_data):
    dish = input_data
    dish_size = calc_size(dish)
    rocks = set(k for k, t in dish.items() if t == 'O')
    cubes = set(k for k, t in dish.items() if t == '#')

    tilt_cycle = ['N', 'W', 'S', 'E']

    #print('Starting position:')
    #print_dish(dish_size, rocks, cubes)

    count = 0
    count_test = 500
    seen = dict()
    seq = []
    while count < count_test:
        count += 1

        # spin cycle
        for direction in tilt_cycle:
            rocks = tilt(rocks, cubes, direction, dish_size)

        
        # seen[state] = (occurence, first seen, weight)
        state = calc_state(dish_size, rocks)
        if state in seen:
            occ, first, weight = seen[state]
            seen[state] = (occ + 1, first, weight)

            if occ > 1:
                mp = len(seq) // 2
                s1 = seq[:mp]
                s2 = seq[mp:]
                if s1 == s2:
                    seq = s1
                    break
        else:
            weight = calc_weight(dish_size, rocks)

            # reset sequence
            seq = []
            seen[state] = (0, count, weight)
        
        # append state to sequence
        seq.append(state)

    # extrapolate cycle count
    count_ex = 1000000000
    
    # repeating sequence starts
    seq_start = max([c[1] for c in seen.values()])
    
    seq_pos = (count_ex - seq_start) % len(seq)
    weight = seen[seq[seq_pos]][2]
    
    return weight


def tilt(rocks, cubes, direction, dish_size):
    
    rock_roll = True
    while rock_roll:
        rock_roll = False
        rocks_n = dict()
        for pos in rocks:
            if direction == 'N':
                pos_n = (pos[0] - 1 if pos[0] > 1 else pos[0], pos[1])
            elif direction == 'W':
                pos_n = (pos[0], pos[1] - 1 if pos[1] > 1 else pos[1])
            elif direction == 'S':
                pos_n = (pos[0] + 1 if pos[0] < dish_size[0] else pos[0], pos[1])
            elif direction == 'E':
                pos_n = (pos[0], pos[1] + 1 if pos[1] < dish_size[1] else pos[1])

            if pos_n not in cubes and pos_n not in rocks:
                rock_roll = True
                rocks_n[pos_n] = True
            else:
                rocks_n[pos] = False
        rocks = rocks_n

    return list(rocks.keys())


def print_dish(dish_size, rocks, cubes):
    for r in range(1, dish_size[0] + 1):
        row = []
        for c in range(1, dish_size[1] + 1):
            if (r, c) in rocks:
                row.append('O')
            elif (r, c) in cubes:
                row.append('#')
            else:
                row.append('.')
        print(''.join(row))
    #print("check rocks", len(rocks))
    #print(rocks)
    #print(dish_size)

def parse_data(input_data):
    dish = {}
    for r, line_text in enumerate(input_data.splitlines()):
        for c, t in enumerate(line_text):
            if t != '.':
                # origin (1, 1)
                dish[(r + 1, c + 1)] = t
    return dish


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input_example.txt')

    answer01 = part01(input_data)
    print(f'part01 - north beam load = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - north beam load = {answer02}')
