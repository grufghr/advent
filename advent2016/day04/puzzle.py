#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2016 Day 04: Security Through Obscurity
"""
import os
import re
from collections import Counter

ROOM_REGEX = re.compile(r'([a-z\-]+)(\d+)\[([a-z]+)\]')


def caeser_cypher(c, offset):
    x = ord(c) - ord('a')
    if 0 <= x <= ord('z'):
        return chr(((x + offset) % 26) + ord('a'))
    else:
        return ' '


def part01(input_data):
    answer = solve(input_data)
    return answer[0]


def part02(input_data):
    answer = solve(input_data)
    return answer[1]


def solve(encrypted_data_list):
    # part 01 - calculate sum of real room sectors
    sector_sum = 0
    # part 02 - find sector of "northpole object storage"
    northpole_sector = None

    for encrypted_data in encrypted_data_list:
        # print(encrypted_name)
        regex_match = ROOM_REGEX.search(encrypted_data)
        encrypted_name, sector, checksum = regex_match.groups()
        sector = int(sector)

        count_map = Counter(encrypted_name)
        count_list = [(k, v) for k, v in count_map.items() if k != '-']
        count_list = sorted(count_list, key=lambda x: (-x[1], x[0]))

        checksum_calc = ''.join([k for k, v in count_list])
        checksum_calc = checksum_calc[:5]

        # print(encrypted_name, sector, checksum, checksum_calc)
        if checksum == checksum_calc:
            sector_sum += sector

            room_name = ''.join([caeser_cypher(c, sector) for c in encrypted_name]).strip()

            if room_name == 'northpole object storage':
                # print(encrypted_name, sector, checksum, checksum_calc, room_name)
                northpole_sector = sector

    return (sector_sum, northpole_sector)


def parse_data(input_data):
    return input_data.splitlines()


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - real room sector sum  = {answer01}')

    answer02 = part01(input_data)
    print(f'part02 - northpole object storage sectore = {answer02}')
