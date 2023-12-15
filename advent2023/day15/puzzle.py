#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 15: Lens Library
"""
import os


def part01(input_data):
    init_seq = input_data
    hash_sum = sum(list(map(calc_hash, init_seq)))
    return hash_sum


def part02(input_data):
    init_seq = input_data

    boxes = [None] * 256
    for step in init_seq:
        # step is add label=focal_len
        if '=' in step:
            label, focal_len = step.split('=')
            box_num = calc_hash(label)
            focal_len = int(focal_len)

            if boxes[box_num]:
                boxes[box_num][label] = focal_len
            else:
                boxes[box_num] = {label: focal_len}
        # step is remove label-
        else:
            label, _ = step.split('-')
            box_num = calc_hash(label)
            if boxes[box_num]:
                if label in boxes[box_num]:
                    boxes[box_num].pop(label)

    # trim boxes to those that contain lens
    boxes = [(i + 1, b) for i, b in enumerate(boxes) if b]

    # calculate focus power
    focus_power = 0
    for box, lens_dict in boxes:
        for slot, label in enumerate(lens_dict, 1):
            focus_power += box * slot * lens_dict[label]

    return focus_power


def calc_hash(text):
    h = 0
    for c in list(text):
        h = ((h + ord(c)) * 17) % 256
    return h


def parse_data(input_data):
    return input_data.split(',')


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - tbc = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - tbc = {answer02}')
