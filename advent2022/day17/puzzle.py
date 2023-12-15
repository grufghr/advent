#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022 Day 17: Pyroclastic Flow
"""
import os
from itertools import cycle

# fmt: off
ROCKS = (
    # ..####.
    (1, [30]),

    # ...#...
    # ..###..
    # ...#...
    (2, [8, 28, 8]),

    # ....#..
    # ....#..
    # ..###..
    (3, [4, 4, 28]),

    # ..#....
    # ..#....
    # ..#....
    # ..#....
    (4, [16, 16, 16, 16]),

    # ..##...
    # ..##...
    (5, [24, 24]),
)
GAP = [0] * 3
# fmt: on


def part01(input_data):
    tower_height = simulate(input_data, 2022)
    return tower_height


def part02(input_data):
    tower_height = simulate(input_data, 1000000000000)
    return tower_height


def simulate(jet_list, num_rocks):
    rock_cycle = cycle(ROCKS)
    jet_cycle = cycle(jet_list)

    tower = [127]  # base

    seen = dict()

    count_test = min(5000, num_rocks)
    for rock_count in range(count_test):
        rock_i, rock = next(rock_cycle)
        rock_size = len(rock)

        # add rock above tower (with gap)
        tower = rock + GAP + tower

        row = 0  # position of rock before fall
        falling = True
        while falling:
            jet_i, jet_dir = next(jet_cycle)

            # apply jet.dir (> or <)
            rock_n = None
            # hit edges?
            if jet_dir == '>' and all((b % 2) == 0 for b in rock):
                rock_n = [b >> 1 for b in rock]
            elif jet_dir == '<' and all(b < 64 for b in rock):
                rock_n = [b << 1 for b in rock]

            # if not edges is another rock blocking move
            if rock_n:
                # get tower top
                tower_n = tower[row : row + rock_size]
                # remove current rock from tower (using XOR) -> tower_n
                tower_n = list(map(lambda x, y: x ^ y, tower_n, rock))
                # determine if rock can move with jet (using AND) -> bock_m
                rock_m = list(map(lambda x, y: x & y, tower_n, rock_n))
                # move rock
                if not any(b for b in rock_m):
                    for r in range(0, rock_size):
                        tower[row + r] = tower[row + r] ^ rock[r]
                        tower[row + r] = tower[row + r] | rock_n[r]
                    rock = rock_n

            # can rock fall
            tower_n = tower[row : row + rock_size + 1]
            # remove current rock from tower (using XOR) -> tower_n
            tower_n = list(map(lambda x, y: x ^ y, tower_n, rock + [0]))
            # determine if rock can fall (using AND) -> rock_f
            rock_f = list(map(lambda x, y: x & y, tower_n, [0] + rock))

            # rock fall one row
            if not any(b for b in rock_f):
                # remove rock from tower
                for r in range(0, rock_size):
                    tower[row + r] = tower[row + r] ^ rock[r]
                # fall
                row += 1
                # add rock to tower (row lower)
                for r in range(0, rock_size):
                    tower[row + r] = tower[row + r] | rock[r]
            else:
                falling = False
        # end rock falling

        # remove empty rows
        tower = [r for r in tower if r != 0]
        height = len(tower) - 1  # -1 for base

        # check for repeating state
        state = (jet_i, rock_i, tuple(rock))
        if state in seen:
            rc_p, h_p = seen[state]
            rc_n = rock_count - rc_p
            hc_n = height - h_p
            diff = num_rocks - rock_count - 1
            more, remain = divmod(diff, rc_n)
            if remain == 0:
                return (hc_n * more) + height
        else:
            seen[state] = (rock_count, height)

    if count_test != 2022:
        print('Warning: May need to increase count test > ', count_test)
    return height


# def print_tower(tower):
#    for row in tower:
#        r = f'{row:07b}'
#        r = r.replace('1', '#')
#        r = r.replace('0', ' ')
#        print(f'|{r}|')
#    print('')


def parse_input(input_data):
    return list([(i, dir) for i, dir in enumerate(input_data)])


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read i[]nput data from file
    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_input(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - tower height (after 2022) = {answer01}')

    answer01 = part02(input_data)
    print(f'part02 - tower height (after 1000000000000)= {answer01}')
