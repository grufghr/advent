#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os
import numpy as np


class Board:
    def __init__(self, board):
        self.board = np.array(board)
        self.shape = self.board.shape
        self.match = np.zeros(self.shape)
        self.done = False

    def dab(self, num):
        board_flat = self.board.flatten()
        board_match_num = np.where(board_flat == num)
        np.put(board_flat, board_match_num, 0)
        self.board = np.reshape(board_flat, self.shape)

        match_flat = self.match.flatten()
        np.put(match_flat, board_match_num, True)
        self.match = np.reshape(match_flat, self.shape)

    def check_house(self):
        axis0 = np.sum(self.match, axis=0)
        win0 = any(i >= self.shape[0] for i in axis0)
        axis1 = np.sum(self.match, axis=1)
        win1 = any(i >= self.shape[1] for i in axis1)
        return win0 or win1

    def score(self, num):
        return np.sum(self.board) * num

    def __repr__(self):
        return self.board.__repr__()


def solve(input_data_file):
    # read input data from file
    with open(input_data_file, 'r') as bingo_file:
        bingo_number_text = bingo_file.readline()
        bingo_file.readline()  # skip line
        board_text = bingo_file.readlines()

    # parse input data file
    board_count = board_text.count('\n') + 1
    board_np = np.genfromtxt(input_data_file, dtype=int, skip_header=2)
    board_np = np.array(np.array_split(board_np, board_count))

    # create list of boards
    board_list = []
    for b in board_np:
        board = Board(b)
        board_list.append(board)

    bingo_number_list = [int(n) for n in bingo_number_text.split(',')]
    # print(bingo_number_list)

    # part 01 & 02

    # play bingo
    winner_score = None
    for num in bingo_number_list:
        for board in board_list:
            if not board.done:
                board.dab(num)
                if board.check_house():
                    if not winner_score:
                        winner_score = board.score(num)
                    else:
                        last_winner_score = board.score(num)
                    board.done = True

    # return results
    return (winner_score, last_winner_score)


if __name__ == '__main__':
    input_data_file = os.path.join(
        os.path.dirname(__file__), 'input.txt')

    answers = solve(input_data_file)
    print(f"Winning bingo card score = {answers[0]}.")
    print(f"Last winning card score = {answers[1]}.")
