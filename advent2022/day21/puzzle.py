#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022 Day 21: Monkey Math
"""
import os
import re
import collections

MONKEY_REGEX = re.compile(r'([a-z]{4}): (.*)')
MONKEY_JOB_REGEX = re.compile(r'(?:(\d+)|([a-z]{4}) ([\+\-\*\/]) ([a-z]{4}))')


def calc_yell(a, op, b):
    if op == '+':
        yell = a + b
    elif op == '-':
        yell = a - b
    elif op == '*':
        yell = a * b
    elif op == '/':
        yell = a / b
    return int(yell)


def inverse_calc(name, a, op, b):
    r = None
    if not isinstance(a, int):
        if op == '+':
            r = (a, (name, '-', b))
        elif op == '-':
            r = (a, (name, '+', b))
        elif op == '*':
            r = (a, (name, '/', b))
        elif op == '/':
            r = (a, (name, '*', b))
    elif not isinstance(b, int):
        if op == '+':
            r = (b, (name, '-', a))
        elif op == '-':
            r = (b, (a, '-', name))
        elif op == '*':
            r = (b, (name, '/', a))
        elif op == '/':
            r = (b, (a, '/', name))

    # input(f"Inverse {name} = ({a} {op} {b}) -> {r}")
    return r


def solve01(input_data):
    # part 01 - determine what root monkey yells
    monkey_calc = [(k, v) for k, v in input_data[0].items()]
    monkey_yell = input_data[1].copy()

    # evaluate monkey equations
    q = collections.deque(monkey_calc)
    while q:
        name, calc = q.popleft()
        a, op, b = calc

        if a in monkey_yell:
            a = monkey_yell[a]
        if b in monkey_yell:
            b = monkey_yell[b]

        if isinstance(a, int) and isinstance(b, int):
            monkey_yell[name] = calc_yell(a, op, b)
        else:
            q.append((name, (a, op, b)))

    return monkey_yell['root']


def solve02(input_data):
    # part 02 - reversed,  determine what 'humn' shouts to solve root equation (a = b)
    monkey_calc = input_data[0]
    monkey_yell = input_data[1]

    # correct root monkey operation
    root_a, root_op, root_b = monkey_calc['root']
    monkey_calc['root'] = (root_a, '=', root_b)
    monkey_calc = [(k, v) for k, v in monkey_calc.items()]
    # remove humn from monkey_yell
    del monkey_yell['humn']

    # evaluate monkey equations
    q = collections.deque(monkey_calc)
    while q:
        name, calc = q.popleft()
        a, op, b = calc

        if a in monkey_yell:
            a = monkey_yell[a]
        if b in monkey_yell:
            b = monkey_yell[b]

        if op == '=':
            if isinstance(a, int) and not isinstance(b, int):
                monkey_yell[b] = int(a)
            elif isinstance(b, int) and not isinstance(a, int):
                monkey_yell[a] = int(b)
            else:
                q.append((name, (a, op, b)))
            continue

        if isinstance(a, int) and isinstance(b, int):
            monkey_yell[name] = calc_yell(a, op, b)
            continue
        elif name in monkey_yell:
            calc_n = inverse_calc(name, a, op, b)
            q.append(calc_n)
            continue

        # wait to resolve a and/or b
        q.append((name, (a, op, b)))

    return monkey_yell['humn']


def parse_data(input_data):
    # parse input file
    monkey_calc = {}
    monkey_yell = {}
    for monkey_line in input_data.splitlines():
        match_m = MONKEY_REGEX.search(monkey_line)
        monkey_name, monkey_job_text = match_m.groups()

        match_j = MONKEY_JOB_REGEX.search(monkey_job_text)
        monkey_job = match_j.groups()

        # part 01
        if monkey_job[0] is None:
            monkey_calc[monkey_name] = (monkey_job[1], monkey_job[2], monkey_job[3])
        else:
            monkey_yell[monkey_name] = int(monkey_job[0])

    return (monkey_calc, monkey_yell)


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read i[]nput data from file
    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f'part01 - root yells = {answer01}')

    answer02 = solve02(input_data)
    print(f'part02 - humn yells = {answer02}')
