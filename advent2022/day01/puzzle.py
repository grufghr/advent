#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os


def solve(inventory_file_text):
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


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, 'r') as filehandle:
        input_data_text = filehandle.read()

    return input_data_text


if __name__ == '__main__':
    input_data = input_data('input.txt')

    answer = solve(input_data)
    print(f"Total Calories Elf carrying the most Calories = {answer[0]}")
    print(f"Total Calories top three Elves are carrying = {answer[1]}")
