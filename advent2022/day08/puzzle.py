#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os
import numpy as np


def calc_score(outlook, height):
    score = 0
    if len(outlook) == 0:
        score = 1
    else:
        hidden = np.any(outlook >= height)
        if hidden:
            blocked_distance = np.asarray(np.where(outlook >= height))
            score = blocked_distance[0][0] + 1
        else:
            score = len(outlook)
    return (not hidden), score


def solve(tree_map_np):

    # process terminal output
    num_r = tree_map_np.shape[0]
    num_c = tree_map_np.shape[1]

    # part 01 & 02
    visible_tree_np = np.ones(tree_map_np.shape)
    # set internal tree (i.e. except boundary) to all hidden
    visible_tree_np[1:num_r - 1, 1:num_c - 1] = 0

    scenic_score_np = np.zeros(tree_map_np.shape)

    for r in range(1, num_r - 1):
        for c in range(1, num_c - 1):
            height = tree_map_np[r][c]

            outlook_n = np.flip(np.array(tree_map_np[:, c][0:r]))
            view_n, score_n = calc_score(outlook_n, height)

            outlook_e = np.array(tree_map_np[r, :][c + 1:num_c])
            view_e, score_e = calc_score(outlook_e, height)

            outlook_s = np.array(tree_map_np[:, c][r + 1:num_r])
            view_s, score_s = calc_score(outlook_s, height)

            outlook_w = np.flip(np.array(tree_map_np[r, :][0:c]))
            view_w, score_w = calc_score(outlook_w, height)

            visible_tree_np[r][c] = view_n or view_e or view_s or view_w
            scenic_score_np[r][c] = score_n * score_e * score_s * score_w

    visible_trees = np.count_nonzero(visible_tree_np)
    highest_scenic_score = int(np.amax(scenic_score_np))

    # return results
    return (visible_trees, highest_scenic_score)


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    input_data = np.genfromtxt(input_data_file, dtype=int, delimiter=1)

    return input_data


if __name__ == '__main__':
    input_data = input_data('input.txt')

    answer = solve(input_data)
    print(f"Total visible trees = {answer[0]}")

    print(f"Highest scenic score = {answer[1]}")
