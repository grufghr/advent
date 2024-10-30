#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2020 Day 04: Passport Processing
"""

import os


def part01(input_data):
    # part 01 - find highest seat id 
    seat_list = [get_seat_id(boarding_pass) for boarding_pass in input_data]
    return max(seat_list)


def part02(input_data):
    # part 02 - find seat
    seat_list = [get_seat_id(boarding_pass) for boarding_pass in input_data]
    seats_all = set(list(range(min(seat_list), max(seat_list) + 1)))
    seats_taken = set(seat_list)
    seat_id = list(seats_all.difference(seats_taken))
    return seat_id[0]


def get_seat_id(boarding_pass):
    row = list(range(0, 128))
    for ch in boarding_pass[:7]:
        hwp = len(row) // 2
        if ch == 'F':
            row = row[:hwp]
        elif ch == 'B':
            row = row[hwp:]
        else:
            print(f'unknown {ch=}')
    row = row[0]
    col = list(range(0, 8))
    for ch in boarding_pass[7:]:
        hwp = len(col) // 2
        if ch == 'L':
            col = col[:hwp]
        elif ch == 'R':
            col = col[hwp:]
        else:
            print(f'unknown {ch=}')
    col = col[0]
    seat_id = (row * 8) + col

    return seat_id


def parse_data(input_data):
    boardingpass_list = input_data.splitlines()
    return boardingpass_list


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - highest seat ID = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - my seat id = {answer02}')
