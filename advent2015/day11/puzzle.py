#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 Day 11: Corporate Policy
"""
import os
from itertools import groupby
from string import ascii_lowercase


def solve01(input_data):
    password = next_password(input_data)
    while not is_valid(password):
        password = next_password(password)
    return password


def solve02(input_data):
    return solve01(input_data)


def is_valid(password):
    # fmt: off
    # cannot contain i, o, l
    if len(set('iol') & set(password)) > 0:
        return False

    # must contain 3 sequential i.e. abc
    if not any([ascii_lowercase[n: n + 3] in password for n in range(24)]):
        return False

    # contains two non-overlapping pairs
    if sum([2 if len(list(group)) >= 4 else 1 for letter, group in groupby(password) if len(list(group)) >= 2]) < 2:
        return False

    # fmt: on
    return True


def next_password(password):
    if password == '':
        return ''
    elif password[-1] < 'z':
        return password[0:-1] + chr(ord(password[-1]) + 1)
    else:
        return next_password(password[:-1]) + 'a'


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return input_data


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f'part01 - santas next password = {answer01}')

    # note: pass part01 answer to part02
    answer02 = solve01(answer01)
    print(f'part02 - santas next password = {answer02}')
