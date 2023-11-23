#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022 Day 20: Grove Positioning System
"""
import os
from itertools import cycle


def solve01(input_data):
    # part 01 - decrypt file (number list)
    return decrypt(input_data, 1, 1)


def solve02(input_data):
    # part 02 - decrypt file (number list) using decryption key
    return decrypt(input_data, 811589153, 10)


def decrypt(encrypted, dec_key, mix_repeat):
    decrypted = [(x * dec_key, i) for i, x in enumerate(encrypted)]
    cyc = cycle(decrypted.copy())
    lm = len(decrypted) - 1

    for _ in range(len(encrypted) * mix_repeat):
        curr = next(cyc)
        idx_old = decrypted.index(curr)
        decrypted.remove(curr)
        idx_new = (idx_old + curr[0] + lm) % lm
        decrypted.insert(idx_new, curr)

    zero_tuple = (0, encrypted.index(0))
    zero_tuple_idx = decrypted.index(zero_tuple)
    grove_coords = [
        decrypted[(zero_tuple_idx + i) % len(encrypted)][0] for i in [1000, 2000, 3000]
    ]
    grove_coords_sum = sum(grove_coords)
    return grove_coords_sum


def parse_data(input_data):
    return [int(x) for x in input_data]


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, "r") as input_filehandle:
        input_data = input_filehandle.read().splitlines()

    return parse_data(input_data)


if __name__ == "__main__":
    input_data = load_data("input.txt")

    answer01 = solve01(input_data)
    print(f"part01 - grove coordinates sum = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - answer = {answer02}")
