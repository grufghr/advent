#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021 Day 04: Giant Squid
"""
import os
import numpy as np


class Board:
    def __init__(self, board):
        self.board = np.array(board)
        self.shape = self.board.shape
        self.match = np.zeros(self.shape)
        self.done = False

    # TODO - improve performance function
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


def part01(input_data):
    answers = solve(input_data[0], input_data[1])
    return int(answers[0])


def part02(input_data):
    answers = solve(input_data[0], input_data[1])
    return int(answers[1])


def solve(bingo_number_list, board_np):
    # create list of boards
    board_list = []
    for b in board_np:
        board = Board(b)
        board_list.append(board)

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

    return (winner_score, last_winner_score)


def parse_data(input_data):
    input_data = input_data.splitlines()
    bingo_number_text = input_data.pop(0)
    bingo_number_list = [int(n) for n in bingo_number_text.split(',')]

    board_text_list = list(filter(None, input_data))
    board_array = [list(map(int, i.split())) for i in board_text_list]

    board_count = len(board_array) // len(board_array[0])
    board_np = np.array(board_array)
    board_np = np.array(np.array_split(board_np, board_count))

    return (bingo_number_list, board_np)


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - Winning bingo card score = {answer01}.')

    answer02 = part02(input_data)
    print(f'part02 - Last winning card score = {answer02}.')
