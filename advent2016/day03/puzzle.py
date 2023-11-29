#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2016 Day 03: Squares With Three Sides
"""
import os


def is_triangle(edge_list):
    longest = max(edge_list)
    edge_list.sort()
    shortest = edge_list[0:2]
    return sum(shortest) > longest


def solve01(edges_text_list):
    # part 01 - count triangles by row
    triangle_count = 0
    for edges in edges_text_list:
        # convert all array elements to int
        edge_list = list(map(int, list(edges.split())))
        if is_triangle(edge_list):
            triangle_count += 1

    return triangle_count


def solve02(edges_text_list):
    # part 02 - count triangles by col
    triangle_count = 0
    step = 3
    end = len(edges_text_list)
    for i in range(0, end, step):
        # read lines in three at a time producing array
        # create 1d array of ['a b c', 'e f g', 'h i j']
        edge_text_list = edges_text_list[i : i + step]
        # create 2d array of [['a', 'b', 'c'], ['e', 'f', 'g'], ['h', 'i', 'j']]
        edge_list = list(map(lambda x: x.split(), edge_text_list))
        # convert all 2d array elements to int
        edge_list = [list(map(int, x)) for x in edge_list]
        # transpose 2d array => [['a', 'e', 'h'], ['b', 'f', 'i'], ['c', 'g', 'j']]
        edge_list_transpose = list(map(list, zip(*edge_list)))
        # map is_triangle onto list
        triangle_list = list(map(is_triangle, edge_list_transpose))
        # count True(=1) in triangle list
        triangle_count += sum(triangle_list)

    return triangle_count


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

    answer01 = solve01(input_data)
    print(f'part01 - triangle count = {answer01}')

    answer02 = solve02(input_data)
    print(f'part02 - triangle count = {answer02}')
