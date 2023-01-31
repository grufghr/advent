#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Solve Puzzle 2022 Day 02: Rock Paper Scissors
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


def solve01(strategy_data):
    # part 01
    startegy_scores_array = [calc_score_part01(row) for row in strategy_data]
    startegy_score = sum(startegy_scores_array)
    return startegy_score


def solve02(strategy_data):
    # part 02
    startegy_scores_array = [calc_score_part02(row) for row in strategy_data]
    startegy_score = sum(startegy_scores_array)

    return startegy_score


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    strategy_data = np.genfromtxt(input_data_file, dtype=str)

    return strategy_data


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - Rock-Paper-Scissors score = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - Rock-Paper-Scissors score = {answer02}")
