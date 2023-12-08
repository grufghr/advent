#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021 Day 03: Binary Diagnostic
"""
import os
import numpy as np


def part01(input_data):
    diag_report_np = input_data

    (r_size, c_size) = diag_report_np.shape

    gamma_binary = ''
    epsilon_binary = ''
    for c in range(c_size):
        col = list(diag_report_np[:, c])
        counts = np.bincount(col)

        gamma_bit = '1' if counts[1] >= counts[0] else '0'
        epsilon_bit = '0' if counts[1] >= counts[0] else '1'

        gamma_binary += gamma_bit
        epsilon_binary += epsilon_bit

    gamma = int(gamma_binary, 2)
    epsilon = int(epsilon_binary, 2)

    power_consumption = gamma * epsilon

    return power_consumption


def part02(input_data):
    diag_report_np = input_data
    
    (r_size, c_size) = diag_report_np.shape

    ox_filter_list = diag_report_np.copy()
    co_filter_list = diag_report_np.copy()
    for c in range(c_size):
        if len(ox_filter_list) > 1:
            ox_counts = np.bincount(list(np.array(ox_filter_list)[:, c]))
            ox_bit = '1' if ox_counts[1] >= ox_counts[0] else '0'
            ox_filter_list_n = [row for row in ox_filter_list if row[c] == ox_bit]
            ox_filter_list = ox_filter_list_n.copy()

        if len(co_filter_list) > 1:
            co_counts = np.bincount(list(np.array(co_filter_list)[:, c]))
            co_bit = '0' if co_counts[1] >= co_counts[0] else '1'
            co_filter_list_n = [row for row in co_filter_list if row[c] == co_bit]
            co_filter_list = co_filter_list_n.copy()

    ox_filter_list = ox_filter_list[0]
    co_filter_list = co_filter_list[0]

    ox_rating = int(''.join(ox_filter_list), 2)
    co_rating = int(''.join(co_filter_list), 2)

    life_support_rating = ox_rating * co_rating

    return life_support_rating


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    diag_report_np = np.genfromtxt(input_data_file, delimiter=1, dtype=str)

    return diag_report_np


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - Power consumption = {answer01}')
    answer02 = part02(input_data)
    print(f'part02 - Life support rating = {answer02}')
