#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2020 Day 04: Passport Processing
"""

import os
import re

VALID_KEYS_NO_CID = set({'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'})
EYE_COLOURS = set({'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'})


def part01(input_data):
    # part 01 - validate passport keys
    valid = [validate_keys(passport_data) for passport_data in input_data]
    return valid.count(True)


def part02(input_data):
    # part 02 - validate passport data
    valid_count = 0
    for passport_data in input_data:
        valid_passport = validate_keys(passport_data)
        if valid_passport:
            valid_passport = validate_data(passport_data)
        if valid_passport:
            valid_count += 1
    return valid_count


def validate_keys(passport_data):
    keys = set(passport_data.keys())
    valid = VALID_KEYS_NO_CID.issubset(keys)
    return valid


def validate_data(passport_data):
    for key, val in passport_data.items():
        match key:
            case 'byr':
                if len(val) != 4:
                    return False
                year = int(val)
                if (year < 1920) or (year > 2002):
                    return False
            case 'iyr':
                if len(val) != 4:
                    return False
                year = int(val)
                if (year < 2010) or (year > 2020):
                    return False
            case 'eyr':
                if len(val) != 4:
                    return False
                year = int(val)
                if (year < 2020) or (year > 2030):
                    return False
            case 'hgt':
                match = re.search(r'(\d{2,3})(cm|in)', val)
                if not match:
                    return False
                hgt = int(match.group(1))
                unit = match.group(2)
                if unit == 'cm':
                    if hgt < 150 or hgt > 193:
                        return False
                elif unit == 'in':
                    if hgt < 59 or hgt > 76:
                        return False
                else:
                    print(f'unknown hgt unit {val}')
            case 'hcl':
                match = re.search(r'^#(\d|[a-f]){6}$', val)
                if not match:
                    return False
            case 'ecl':
                if val not in EYE_COLOURS:
                    return False
            case 'pid':
                match = re.search(r'^\d{9}$', val)
                if not match:
                    return False
            case 'cid':
                # ignore
                pass
            case _:
                print(f'unknown key {key}')
                return False
    return True


def parse_data(input_data):
    lines_grouped = input_data.split('\n\n')
    passport_data = [txt.replace('\n', ' ') for txt in lines_grouped]
    passport_list = []
    for passport_text in passport_data:
        pd = {kv.split(':')[0]: kv.split(':')[1] for kv in passport_text.split()}
        passport_list.append(pd)
    return passport_list


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 answer = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 answer = {answer02}')
