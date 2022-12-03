#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022
"""
import os


def solve(input_data_file):
    # read input data from file
    with open(input_data_file, 'r') as inventory_file:
        inventory_file_text = inventory_file.read()

    # part 01

    # split data into list of lists (ints)
    inventory_text = [i.split("\n") for i in inventory_file_text.split("\n\n")]
    inventory = [list(map(int, i)) for i in inventory_text]

    # create array of totals of each elf inventory
    inventory_totals = list(map(sum, inventory))

    # find largest elf inventory totals
    inventory_max = max(inventory_totals)

    # part 02

    # sort inventory totals (largest first)
    inventory_totals_sorted = list(inventory_totals)
    inventory_totals_sorted.sort(reverse=True)

    # split top 3 into seperate list
    inventory_totals_top3 = inventory_totals_sorted[:3]

    # sum top 3 totals
    inventory_totals_top3_sum = sum(inventory_totals_top3)

    # return results
    return (inventory_max, inventory_totals_top3_sum)


if __name__ == '__main__':
    input_data_file = os.path.join(os.path.dirname(__file__), 'input.txt')

    answers = solve(input_data_file)
    print(f"Total Calories Elf carrying the most Calories = {answers[0]}")
    print(f"Total Calories top three Elves are carrying = {answers[1]}")
