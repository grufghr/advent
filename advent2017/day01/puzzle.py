#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2017 Day 01: Inverse Captcha
"""
import os


def part01(input_data):
    digit_sum = 0
    digit = input_data[-1]
    for digit_n in input_data:
        if digit == digit_n:
            digit_sum += int(digit_n)
        digit = digit_n
    return digit_sum


def part02(input_data):
    digit_sum = 0
    idx = len(input_data) // 2
    for digit_n in input_data:
        if input_data[idx] == digit_n:
            digit_sum += int(digit_n)
        idx += 1
        if idx >= len(input_data):
            idx = 0
    return digit_sum


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return input_data


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - captcha solution = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - captcha solution = {answer02}')
