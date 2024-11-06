#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 Day 19: Medicine for Rudolph
"""

import os
import re

REGEX = re.compile(r'(\w+) => (\w+)')


def part01(input_data):
    # find distinct molecules using replacement
    rep_list, mol = input_data
    mol_gen = set()
    for rep in rep_list:
        for match in re.finditer(rep[0], mol):
            mol_n = ''.join([mol[: match.start(0)], rep[1], mol[match.end(0) :]])
            mol_gen.add(mol_n)
    return len(mol_gen)


def part02(input_data):
    # find how many steps by reducing back to election
    rep_list, mol = input_data

    step = 0
    step_limit = 250

    # greedy replacement - use longest t1 in (t0, t1)
    # ToDO Use CYK algorithm
    rep_list.sort(key=lambda t: len(t[1]))
    while mol != 'e' and step < step_limit:
        for rep in rep_list:
            if rep[1] in mol:
                mol = mol.replace(rep[1], rep[0], 1)
                step = step + 1
        mol = mol.replace('ee', 'e')
    return step


def parse_data(input_data):
    rep_list = []
    for line_text in input_data.splitlines():
        if ' => ' in line_text:
            rep = line_text.split()
            rep_list.append(tuple([rep[0], rep[-1]]))
        elif line_text:
            mol = line_text
    return (rep_list, mol)


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 answer = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 answer = {answer02}')
