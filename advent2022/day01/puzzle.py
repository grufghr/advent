#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Solve Puzzle 2022 Day 01: Calorie Counting
"""
import os


def solve01(input_data):
    # part 01

    # create array of totals of each elf inventory
    inventory_totals = list(map(sum, input_data))

    # find largest elf inventory totals
    inventory_max = max(inventory_totals)
    return inventory_max


def solve02(input_data):
    # part 02

    # create array of totals of each elf inventory
    inventory_totals = list(map(sum, input_data))

    # sort inventory totals (largest first)
    inventory_totals_sorted = list(inventory_totals)
    inventory_totals_sorted.sort(reverse=True)

    # split top 3 into seperate list
    inventory_totals_top3 = inventory_totals_sorted[:3]

    # sum top 3 totals
    inventory_totals_top3_sum = sum(inventory_totals_top3)

    return inventory_totals_top3_sum


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, 'r') as filehandle:
        input_data_text = filehandle.read()

    # split data into list of lists (ints)
    inventory_text = [i.split("\n") for i in input_data_text.split("\n\n")]
    inventory = [list(map(int, i)) for i in inventory_text]

    return inventory


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - Total Calories strongest Elf = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - Total Calories top three Elves = {answer02}")
