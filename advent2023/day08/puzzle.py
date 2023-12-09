#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2023 Day 08: Haunted Wasteland
"""
import os
import re
import math
from collections import deque


def part01(input_data):
    navigation, network_map = input_data
    step_count = traverse_network('AAA', navigation, network_map)
    return step_count


def part02(input_data):
    navigation, network_map = input_data

    node_list = network_map.keys()
    pos_list = [x for x in node_list if x[2:3] == 'A']

    end_counts = []
    for pos in pos_list:
        step_count = traverse_network(pos, navigation, network_map)
        end_counts.append(step_count)

    lcm = math.lcm(*end_counts)
    return lcm


def traverse_network(pos, navigation, network_map):
    step_count = 0

    q = deque(navigation)
    while q and step_count < 25000:
        move = q.popleft()
        q.append(move)
        step_count += 1
        pos = network_map[pos][move]

        if pos[2:3] == 'Z':
            return step_count
    return None


def parse_data(input_data):
    input_data = input_data.splitlines()
    navigation = input_data[0]
    navigation = list(map(int, list(navigation.replace('L', '0').replace('R', '1'))))

    network_map = {}
    for line_text in input_data[2:]:
        # AAA = (BBB, CCC)
        pos, left, right = re.findall(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)', line_text)[0]
        network_map[pos] = (left, right)

    return (navigation, network_map)


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - steps to end = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - steps to end = {answer02}')
