#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os
import hashlib


def solve01(door_id):
    # part 01 - calculate door password
    door_pwd = ''

    lowest_positive_number = 0
    n_zeroes = '00000'
    idx = 0

    while (idx < 8) and (lowest_positive_number < 99999999):
        lowest_positive_number += 1

        text = door_id + str(lowest_positive_number)

        hash_text = str(hashlib.md5(text.encode('utf-8')).hexdigest())
        if (hash_text.startswith(n_zeroes)):
            door_pwd = door_pwd + hash_text[5:6]
            idx += 1
            # print(door_pwd)

    return door_pwd


def solve02(door_id):
    # part 02 - calculate door password
    door_pwd = '--------'

    lowest_positive_number = 0
    n_zeroes = '00000'
    idx = 0

    while (idx < 8) and (lowest_positive_number < 99999999):
        lowest_positive_number += 1

        text = door_id + str(lowest_positive_number)

        hash_text = str(hashlib.md5(text.encode('utf-8')).hexdigest())
        if (hash_text.startswith(n_zeroes)):
            pos = hash_text[5:6]
            if pos in '01234567':
                pos = int(pos)
                if door_pwd[pos] == '-':
                    door_pwd = door_pwd[0:pos] + \
                        hash_text[6:7] + door_pwd[pos + 1:]
                    idx += 1
                    # print(door_pwd)

    return door_pwd


def input_data_iter(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as input_filehandle:
        input_txt_list = input_filehandle.read().splitlines()

    for input_txt in input_txt_list:
        yield (input_txt)


if __name__ == '__main__':
    door_id = next(input_data_iter('input.txt'))

    answer = solve01(door_id)
    print(f"part01 - door password = {answer}")

    answer = solve02(door_id)
    print(f"part02 - door password = {answer}")
