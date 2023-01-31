#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Solve Puzzle 2021 Day 10: Syntax Scoring
"""
import os
from collections import deque

CHUNK_MAP = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
CHAR_OPEN = CHUNK_MAP.keys()
CHAR_CLOSE = CHUNK_MAP.values()

SCORE_TABLE_01 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

SCORE_TABLE_02 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def solve01(input_data):
    # part 01 - calc syntax error score

    error_count = dict.fromkeys(CHAR_CLOSE, 0)

    for line in input_data:
        q = deque([])
        for nc in line:
            if nc in CHAR_OPEN:
                q.append(nc)
            else:
                oc = q.pop()
                if nc != CHUNK_MAP[oc]:
                    # print(f"{oc} not match {nc}")
                    error_count[nc] += 1
                    # stop processing line when error encountered
                    break

    lista = list(error_count.values())
    listb = list(SCORE_TABLE_01.values())
    error_score = sum([a * b for a, b in zip(lista, listb)])
    return error_score


def solve02(input_data):
    # part 02 - complete uncorrupted incomplete lines

    correct_scores = []

    for line in input_data:
        q = deque([])

        # process open closing pairs (drop corrupted)
        corrupted = False
        for nc in line:
            if nc in CHAR_OPEN:
                q.append(nc)
            else:
                oc = q.pop()

                if nc != CHUNK_MAP[oc]:
                    # stop processing line when error encountered
                    corrupted = True
                    break

        if corrupted:
            # next line
            continue

        # correct missing closing chunk
        line_close = []
        while q:
            oc = q.pop()
            line_close.append(CHUNK_MAP[oc])

        # calculate line score
        line_score = 0
        for cc in line_close:
            line_score = (line_score * 5) + SCORE_TABLE_02[cc]

        correct_scores.append(line_score)

    # find middle score
    correct_scores.sort()
    middle_score = correct_scores[(len(correct_scores) // 2)]

    return middle_score


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data_list = filehandle.read().splitlines()

    return input_data_list


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - syntax error score = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - middle correct score = {answer02}")
