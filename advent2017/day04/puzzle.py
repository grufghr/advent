#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2017 Day 04: High-Entropy Passphrases
"""
import os


def solve01(input_data):
    valid_count = 0
    for passphrase in input_data:
        if policy01(passphrase):
            valid_count = valid_count + 1
    return valid_count


def solve02(input_data):
    valid_count = 0
    for passphrase in input_data:
        if policy01(passphrase) and policy02(passphrase):
            valid_count = valid_count + 1
    return valid_count


def policy01(passphrase):
    passphrase_words = passphrase.split()
    if len(passphrase_words) == len(set(passphrase_words)):
        return True
    return False

def policy02(passphrase):
    passphrase_words = passphrase.split()
    passphrase_sorted = list(map(lambda x: ''.join(sorted(x)), passphrase_words))
    if len(passphrase_sorted) == len(set(passphrase_sorted)):
        return True
    return False

def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, "r") as filehandle:
        passphrase_data = filehandle.read().splitlines()

    return passphrase_data


if __name__ == "__main__":
    input_data = load_data("input.txt")

    answer01 = solve01(input_data)
    print(f"part01 - valid passphrases (policy 01) = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - valid passphrases (policy 01 & 02) = {answer02}")
