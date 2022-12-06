#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os
import numpy as np

ROCK = 1
PAPER = 2
SCISSORS = 3
LOSS = 0
DRAW = 3
WIN = 6


def calc_score_part01(r):
    score = 0
    if r[0] == 'A':
        if r[1] == 'X':
            score = score + DRAW + ROCK
        elif r[1] == 'Y':
            score = score + WIN + PAPER
        elif r[1] == 'Z':
            score = score + LOSS + SCISSORS
    elif r[0] == 'B':
        if r[1] == 'X':
            score = score + LOSS + ROCK
        elif r[1] == 'Y':
            score = score + DRAW + PAPER
        elif r[1] == 'Z':
            score = score + WIN + SCISSORS
    elif r[0] == 'C':
        if r[1] == 'X':
            score = score + WIN + ROCK
        elif r[1] == 'Y':
            score = score + LOSS + PAPER
        elif r[1] == 'Z':
            score = score + DRAW + SCISSORS
    return score


def calc_score_part02(r):
    score = 0
    if r[0] == 'A':
        if r[1] == 'X':
            score = score + LOSS + SCISSORS
        elif r[1] == 'Y':
            score = score + DRAW + ROCK
        elif r[1] == 'Z':
            score = score + WIN + PAPER
    elif r[0] == 'B':
        if r[1] == 'X':
            score = score + LOSS + ROCK
        elif r[1] == 'Y':
            score = score + DRAW + PAPER
        elif r[1] == 'Z':
            score = score + WIN + SCISSORS
    elif r[0] == 'C':
        if r[1] == 'X':
            score = score + LOSS + PAPER
        elif r[1] == 'Y':
            score = score + DRAW + SCISSORS
        elif r[1] == 'Z':
            score = score + WIN + ROCK
    return score


def solve(strategy_data):
    # part 01
    startegy1_scores_array = [calc_score_part01(row) for row in strategy_data]
    startegy1_score = sum(startegy1_scores_array)

    # part 02
    startegy2_scores_array = [calc_score_part02(row) for row in strategy_data]
    startegy2_score = sum(startegy2_scores_array)

    # return results
    return (startegy1_score, startegy2_score)


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    strategy_data = np.genfromtxt(input_data_file, dtype=str)

    return strategy_data


if __name__ == '__main__':
    input_data = input_data('input.txt')

    answer = solve(input_data)
    print(f"Rock-Paper-Scissors score with part 01 strategy = {answer[0]}")
    print(f"Rock-Paper-Scissors score with part 02 strategy = {answer[1]}")
