#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022
"""
import os
import numpy as np


class Board:
    def __init__(self):
        self.board = np.zeros((5, 5), dtype=int)
        self.match = np.zeros((5, 5))

    def number_called(self, number):
        if number in self.board:
            indices = np.where(self.board == called_number)
            self.marked[indices[0], indices[1]] = 1

    def house(self):
        return self.marked.all(axis=0).any() or self.marked.all(axis=1).any()


def solve(input_data_file):
    # read input data from file
    with open(input_data_file, 'r') as bingo_file:
        bingo_number_text = bingo_file.readline()
        bingo_file.readline()  # skip line
        boards_text = bingo_file.readlines()

    boards_count = boards_text.count('\n') + 1
    boards_np = np.genfromtxt(input_data_file, dtype=int, skip_header=2)
    boards_np = np.array(np.array_split(boards_np, boards_count))

    match_np = np.zeros(boards_np.shape)

    # parse input data file
    bingo_number_list = [int(n) for n in bingo_number_text.split(',')]

    # part 01
    print(bingo_number_list)

    # part 02
    # return results
    return (None, None)


if __name__ == '__main__':
    input_data_file = os.path.join(
        os.path.dirname(__file__), 'input_example.txt')

    answers = solve(input_data_file)
    print(f"part1 = {answers[0]}.")
    print(f"part2 = {answers[1]}.")
