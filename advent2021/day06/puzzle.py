#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os


def solve(fish_age_list, days):

    # part 01&02 - fish population after n days
    day = 0
    population_data = [fish_age_list.count(age) for age in range(0, 9)]

    while (day < days):
        day += 1

        population_data.append(population_data[0])
        fish_6 = population_data.pop(0)
        population_data[6] += fish_6

    # print(f"After  {day} day: population = {sum(population_data)}")
    fish_pop = sum(population_data)

    return fish_pop


def parse_data(input_data):
    fish_text_list = list(input_data.split(","))
    fish_age_list = list(map(int, fish_text_list))
    return fish_age_list


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as input_filehandle:
        input_data = input_filehandle.read()

    return input_data


if __name__ == '__main__':
    input_data = parse_data(load_data('input.txt'))

    answer = solve(input_data, 80)
    print(f"part01 - fish population after 80 days = {answer}")

    answer = solve(input_data, 256)
    print(f"part02 - fish population after 256 days = {answer}")
