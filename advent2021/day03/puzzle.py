#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os
import numpy as np


def solve(input_data_file):
    # read in data file
    diag_report_data = np.genfromtxt(input_data_file, delimiter=1, dtype=str)
    (r_size, c_size) = diag_report_data.shape

    # part 01
    gamma_binary = ''
    epsilon_binary = ''
    for c in range(c_size):
        col = list(diag_report_data[:, c])
        counts = np.bincount(col)

        gamma_bit = ('1' if counts[1] >= counts[0] else '0')
        epsilon_bit = ('0' if counts[1] >= counts[0] else '1')

        gamma_binary += gamma_bit
        epsilon_binary += epsilon_bit

    gamma = int(gamma_binary, 2)
    epsilon = int(epsilon_binary, 2)

    power_consumption = gamma * epsilon

    # part 02
    ox_filter_list = diag_report_data.copy()
    co_filter_list = diag_report_data.copy()
    for c in range(c_size):
        if len(ox_filter_list) > 1:
            ox_counts = np.bincount(list(np.array(ox_filter_list)[:, c]))
            ox_bit = ('1' if ox_counts[1] >= ox_counts[0] else '0')
            ox_filter_list_n = [
                row for row in ox_filter_list if row[c] == ox_bit]
            ox_filter_list = ox_filter_list_n.copy()

        if len(co_filter_list) > 1:
            co_counts = np.bincount(list(np.array(co_filter_list)[:, c]))
            co_bit = ('0' if co_counts[1] >= co_counts[0] else '1')
            co_filter_list_n = [
                row for row in co_filter_list if row[c] == co_bit]
            co_filter_list = co_filter_list_n.copy()

    ox_filter_list = ox_filter_list[0]
    co_filter_list = co_filter_list[0]

    ox_rating = int(''.join(ox_filter_list), 2)
    co_rating = int(''.join(co_filter_list), 2)

    life_support_rating = ox_rating * co_rating

    # return results
    return (power_consumption, life_support_rating)


if __name__ == '__main__':
    input_data_file = os.path.join(os.path.dirname(__file__), 'input.txt')

    answers = solve(input_data_file)
    print(f"Power consumption = {answers[0]}.")
    print(f"Life support rating = {answers[1]}.")
