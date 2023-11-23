#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022 Day 11: Monkey in the Middle
"""
import os
import re
import math

LINE_MONKEY = re.compile(r'Monkey (\d+):')
LINE_STARTING_ITEM = re.compile(r'Starting items:')
LINE_NUMBER_LIST = re.compile(r'(\d+)')
LINE_OPERATION = re.compile(r'Operation: new = (.+) (.+) (.+)')
LINE_TEST = re.compile(r'Test: divisible by (\d+)')
LINE_IF = re.compile(r'If (true|false): throw to monkey (\d+)')


def solve01(input_data):
    answer = solve(input_data, 20)
    return answer


def solve02(input_data):
    answer = solve(input_data, 10000, True)
    return answer


def solve(note_list, rounds_to_complete=20, manage_worry_level=False):

    monkey = None
    m_items = {}
    m_ops = {}
    m_div = {}
    m_target_true = {}
    m_target_false = {}
    m_inspect_count = {}

    # process input file
    for note in note_list:
        if match := LINE_MONKEY.search(note):
            monkey = int(match.group(1))
            m_inspect_count[monkey] = 0

            # print(f"Monkey {monkey}")
        elif match := LINE_STARTING_ITEM.search(note):
            m_items[monkey] = [int(x) for x in LINE_NUMBER_LIST.findall(note)]
            # print(f"  Starting items: {m_items[monkey]}")
        elif match := LINE_OPERATION.search(note):
            m_ops[monkey] = tuple(match.groups())
            # print(f"  Operation: new = {m_ops[monkey]}")
        elif match := LINE_TEST.search(note):
            m_div[monkey] = int(match.group(1))
            # print(f"  Test: divisible by { m_div[monkey]}")
        elif match := LINE_IF.search(note):
            condition = True if match.group(1) == 'true' else False
            if condition:
                m_target_true[monkey] = int(match.group(2))
            else:
                m_target_false[monkey] = int(match.group(2))
            # print(f"    If {condition}: throw to monkey {m_target}")
        elif not note:
            continue
        else:
            print("do something with ", note)

    mod_factor = math.prod([d for d in m_div.values()])

    round = 1
    while (round <= rounds_to_complete):
        for monkey in m_items.keys():
            # print(f"Monkey {monkey}:")
            for item in m_items[monkey]:
                worry_level = int(item)
                m_inspect_count[monkey] += 1
                # print(f"  Monkey inspects an item with a worry level of {worry_level}.")

                if m_ops[monkey][0] == 'old':
                    a = worry_level
                else:
                    a = int(m_ops[monkey][0])

                if m_ops[monkey][2] == 'old':
                    b = worry_level
                else:
                    b = int(m_ops[monkey][2])

                if m_ops[monkey][1] == '+':
                    worry_level_n = a + b
                elif m_ops[monkey][1] == '*':
                    worry_level_n = a * b
                else:
                    exit("unknown op ", m_ops[monkey][1])

                # print(f"    Worry level is {a} {m_ops[monkey][1]} {b} = {worry_level_n}")

                if manage_worry_level:
                    worry_level_n = worry_level_n % mod_factor
                    # print(f"    Worry level is % by {mod_factor} to keep worry level manageable at {worry_level_n}.")
                else:
                    worry_level_n = worry_level_n // 3
                    # print(f"    Monkey gets bored with item. Worry level is divided by 3 to {worry_level_n}.")

                test = ((worry_level_n % m_div[monkey]) == 0)
                # test_str = 'is' if test else 'is not'
                # print(f"    Current worry level {test_str} divisible by {m_div[monkey]}.")

                if test:
                    m_target = m_target_true[monkey]
                else:
                    m_target = m_target_false[monkey]
                # print(f"    Item with worry level {worry_level_n} is thrown to monkey {m_target}.")

                m_items[m_target].append(worry_level_n)

            m_items[monkey] = []

        # if (round == 1) or (round == 20) or (round % 100) == 0:
        #     print(f"After round {round}, the monkeys are " +
        #           "holding items with these worry levels:")
        #     # for k, v in m_items.items():
        #     #     print(f"Monkey {k}: {v}")
        #     for k, v in m_inspect_count.items():
        #         print(f"Monkey {k} inpsected items {v} times.")

        round += 1

    m_inspect_count_sorted = sorted(m_inspect_count.values(), reverse=True)
    # print(m_inspect_count_sorted)
    m_business = m_inspect_count_sorted[0] * m_inspect_count_sorted[1]
    # print(m_business)
    return m_business


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read().splitlines()

    return input_data


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - level of monkey business after 20 rounds = {answer01}")

    answer02 = solve02(input_data)
    print(f"part02 - level of monkey business after 10000 rounds = {answer02}")
