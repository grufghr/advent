#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 Day 15: Science for Hungry People
"""
import os
import re
import math


def part01(input_data):
    recipe = input_data

    ingredient_count = len(recipe)
    best_score = 0
    for mixture in mixture_iter(ingredient_count, 100):
        cookie_score = calc_cookie_score(mixture, recipe)
        if cookie_score > best_score:
            best_score = cookie_score
    return best_score


def part02(input_data):
    recipe = input_data

    ingredient_count = len(recipe)
    best_score = 0
    for mixture in mixture_iter(ingredient_count, 100):
        if calc_calories(mixture, recipe) != 500:
            continue
        cookie_score = calc_cookie_score(mixture, recipe)
        if cookie_score > best_score:
            best_score = cookie_score
    return best_score


def mixture_iter(n, total):
    start = total if n == 1 else 0
    for i in range(start, total + 1):
        left = total - i
        if n - 1:
            for y in mixture_iter(n - 1, left):
                yield [i] + y
        else:
            yield [i]


def calc_cookie_score(ingredients, recipe):
    score = [0, 0, 0, 0]
    for i, j in enumerate(ingredients):
        for s in range(4):
            score[s] += j * recipe[i][s]

    if any([x < 0 for x in score]):
        return 0
    score = math.prod(score)
    return score


def calc_calories(ingredients, recipe):
    calories = 0
    for i, j in enumerate(ingredients):
        calories += j * recipe[i][4]
    return calories


def parse_data(input_data):
    recipe = []
    for line_text in input_data.splitlines():
        # Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
        ingredient, props = line_text.split(':')
        props = list(map(int, list(re.findall(r'(-?\d+)', line_text))))
        recipe.append(props)
    return recipe


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    with open(input_data_file, 'r') as filehandle:
        input_data = filehandle.read()

    return parse_data(input_data)


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = part01(input_data)
    print(f'part01 - best score = {answer01}')

    answer02 = part02(input_data)
    print(f'part02 - best score = {answer02}')
