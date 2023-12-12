#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 Day 16: Aunt Sue
"""
import os
import re

MFCSAM_OUTPUT = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


def part01(input_data):
    sue_list = input_data
    gift_from = None
    for sue_num, sue in enumerate(sue_list):
        match = []
        for k, v in MFCSAM_OUTPUT.items():
            if k not in sue:
                match.append(True)
            elif sue[k] == v:
                match.append(True)
            else:
                match.append(False)

        if all(match):
            gift_from = sue_num + 1
            break

    return gift_from


def part02(input_data):
    sue_list = input_data
    gift_from = None
    for sue_num, sue in enumerate(sue_list):
        match = []
        for k, v in MFCSAM_OUTPUT.items():
            if k not in sue:
                match.append(True)
            elif k in ('cats', 'trees') and sue[k] > v:
                match.append(True)
            elif k in ('pomeranians', 'goldfish') and sue[k] < v:
                match.append(True)
            elif sue[k] == v:
                match.append(True)
            else:
                match.append(False)

        if all(match):
            gift_from = sue_num + 1
            # do not break find another match

    return gift_from


def parse_data(input_data):
    sue_list = []
    for line_text in input_data.splitlines():
        # Sue 2: akitas: 10, perfumes: 10, children: 5
        cat_list = list(re.findall(r'([a-z]+): (\d+)', line_text))
        cat_dict = {k: int(v) for k, v in cat_list}
        sue_list.append(cat_dict)
    return sue_list


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - gift from sue = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - gift from sue = {answer02}')
