#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 02: Cube Conundrum
"""
import os
import re
import math


POSSIBLE = {'red': 12, 'green': 13, 'blue': 14}


def part01(input_data):
    game_stats = input_data
    # for each game create merged with maximum count
    game_max = max_stats(game_stats)

    # create a list of games whe count <= POSSIBLE
    game_possible = []
    for game_num, game in game_max.items():
        if all([count <= POSSIBLE[color] for color, count in game.items()]):
            game_possible.append(int(game_num))

    game_sum = sum(game_possible)
    return game_sum


def part02(input_data):
    game_stats = input_data
    # for each game create merged with maximum count
    game_max = max_stats(game_stats)

    game_power_list = []
    for game in game_max.values():
        count_list = list(game.values())
        game_power_list.append(math.prod(count_list))

    game_sum = sum(game_power_list)
    return game_sum


def max_stats(game_stats):
    game_max = {}
    for game_num, game in game_stats.items():
        dict1 = {}
        for dict2 in game:
            for key in dict2:
                if key not in dict1 or dict2[key] > dict1[key]:
                    dict1[key] = dict2[key]
        game_max[game_num] = dict1
    return game_max


def parse_data(input_data):
    game_stats = {}
    ## Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    for line_text in input_data.splitlines():
        game_num = re.findall(r'Game (\d+):', line_text)[0]
        game_stats[game_num] = [parse2(t) for t in parse1(line_text)]
    return game_stats


def parse1(text):
    r1 = str(text.split(':')[1])
    r2 = r1.split(';')
    return r2


def parse2(text):
    r1 = re.findall(r'(\d+) (red|green|blue)', text)
    r2 = {color: int(count) for (count, color) in r1}
    return r2


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - sum of possible games = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - sum of the powers = {answer02}')
