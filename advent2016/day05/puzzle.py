#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2016 Day 05: How About a Nice Game of Chess?
"""
import os
import hashlib


def part01(input_data):
    # part 01 - calculate door password
    door_id = input_data

    door_pwd = ''

    lowest_positive_number = 0
    n_zeroes = '00000'
    idx = 0

    while (idx < 8) and (lowest_positive_number < 99999999):
        lowest_positive_number += 1

        text = door_id + str(lowest_positive_number)

        hash_text = str(hashlib.md5(text.encode('utf-8')).hexdigest())
        if hash_text.startswith(n_zeroes):
            door_pwd = door_pwd + hash_text[5:6]
            idx += 1
            # print(door_pwd)

    return door_pwd


def part02(input_data):
    # part 02 - calculate door password
    door_id = input_data

    door_pwd = '--------'

    lowest_positive_number = 0
    n_zeroes = '00000'
    idx = 0

    while (idx < 8) and (lowest_positive_number < 99999999):
        lowest_positive_number += 1

        text = door_id + str(lowest_positive_number)

        hash_text = str(hashlib.md5(text.encode('utf-8')).hexdigest())
        if hash_text.startswith(n_zeroes):
            pos = hash_text[5:6]
            if pos in '01234567':
                pos = int(pos)
                if door_pwd[pos] == '-':
                    door_pwd = door_pwd[0:pos] + hash_text[6:7] + door_pwd[pos + 1 :]
                    idx += 1
                    # print(door_pwd)

    return door_pwd


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return input_data


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - door password = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - door password = {answer02}')
