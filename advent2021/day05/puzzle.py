#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021
"""
import os
import numpy as np


def solve01(coord_np):
    return solve(coord_np)


def solve02(coord_np):
    return solve(coord_np, True)


def solve(coord_np, include_diag=False):

    # create map of zeros
    num_r = max([*coord_np['sr'], *coord_np['er']]) + 1
    num_c = max([*coord_np['sc'], *coord_np['ec']]) + 1
    map_shape = (num_r, num_c)

    vent_map_np = np.asarray(np.zeros(map_shape, dtype=int))

    # process coordinates
    for coord in coord_np:
        sc = min(coord[0], coord[2])
        ec = max(coord[0], coord[2])
        sr = min(coord[1], coord[3])
        er = max(coord[1], coord[3])

        # part 01 & 02
        if sr == er:
            vent_map_np[sr, sc:ec + 1] += 1
        elif sc == ec:
            vent_map_np[sr:er + 1, sc] += 1

        # part 02 -
        if include_diag and (sr != er) and (sc != ec):
            r = coord[1]
            c = coord[0]
            vent_map_np[r][c] += 1
            while (r != coord[3]) and (c != coord[2]):
                if (r < coord[3]):
                    r += 1
                else:
                    r -= 1

                if (c < coord[2]):
                    c += 1
                else:
                    c -= 1
                vent_map_np[r][c] += 1

    num_overlapping_vents = len(np.where(vent_map_np > 1)[0])

    return num_overlapping_vents


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    dt = [('sr', np.int64), ('sc', np.int64),
          ('er', np.int64), ('ec', np.int64)]
    coord_np = np.fromregex(
        input_data_file, r'(\d+)\,(\d+) \-\> (\d+)\,(\d+)', dtype=dt)

    return coord_np


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - Overlapping air vents = {answer}")

    answer01 = solve02(input_data)
    print(f"part02 - Overlapping air vents (diagonals included) = {answer}")
