#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Solve Puzzle 2019 Day 01: The Tyranny of the Rocket Equation
"""
import os


def solve01(input_data):
    # part 01 - calculate fuel required for all modules
    fuel_tot = 0
    for mass in input_data:
        fuel = (mass // 3) - 2
        fuel_tot += fuel
    return fuel_tot


def solve02(input_data):
    # part 02 - calculate fuel required for all modules (including fuel)
    fuel_tot = 0
    for mass_m in input_data:
        # fuel required for module
        fuel_m = (mass_m // 3) - 2
        fuel_tot += fuel_m

        # fuel required for fuel
        mass_f = fuel_m
        while mass_f > 0:
            mass_f = (mass_f // 3) - 2
            if mass_f > 0:
                fuel_tot += mass_f

    return fuel_tot


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as input_filehandle:
        input_data_text_list = input_filehandle.read().splitlines()

    input_data = [int(x) for x in input_data_text_list]
    return input_data


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - fuel needs = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - fuel needs (including fuel needs) = {answer02}")
