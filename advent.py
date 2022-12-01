#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022
"""


def solve():
    # read in data file
    elf_inventory_file = open('elf_inventory.txt', 'r')
    elf_inventory_file_text = elf_inventory_file.read()

    # split data into list of lists (ints)
    elf_inventory_text = [i.split("\n")
                          for i in elf_inventory_file_text.split("\n\n")]
    elf_inventory = [list(map(int, i)) for i in elf_inventory_text]

    # create array of totals of each elf inventory
    elf_inventory_totals = list(map(sum, elf_inventory))

    # find largest elf inventory totals
    elf_inventory_max = max(elf_inventory_totals)
    print("Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?")
    print(f"Your puzzle answer was {elf_inventory_max}.\n")

if __name__ == '__main__':
    solve()
