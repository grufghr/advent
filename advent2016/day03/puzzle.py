#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code
"""
import os


def is_triangle(edge_list):
    longest = max(edge_list)
    edge_list.sort()
    shortest = edge_list[0:2]
    return sum(shortest) > longest


def solve(edges_text_list):

    # part 01 - count triangles by row
    triangle_count01 = 0
    for edges in edges_text_list:
        # convert all array elements to int
        edge_list = list(map(int, list(edges.split())))
        if is_triangle(edge_list):
            triangle_count01 += 1

    # part 02 - count triangles by col
    triangle_count02 = 0
    step = 3
    end = len(edges_text_list)
    for i in range(0, end, step):
        # read lines in three at a time producing array
        # create 1d array of ['a b c', 'e f g', 'h i j']
        edge_text_list = edges_text_list[i:i + step]
        # create 2d array of [['a', 'b', 'c'], ['e', 'f', 'g'], ['h', 'i', 'j']]
        edge_list = list(map(lambda x: x.split(), edge_text_list))
        # convert all 2d array elements to int
        edge_list = [list(map(int, x)) for x in edge_list]
        # transpose 2d array => [['a', 'e', 'h'], ['b', 'f', 'i'], ['c', 'g', 'j']]
        edge_list_transpose = list(map(list, zip(*edge_list)))
        # map is_triangle onto list
        triangle_list = list(map(is_triangle, edge_list_transpose))
        # count True(=1) in triangle list
        triangle_count02 += sum(triangle_list)

    return (triangle_count01, triangle_count02)


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read input data from file
    with open(input_data_file, 'r') as input_filehandle:
        input_data_text_list = input_filehandle.read().splitlines()

    return input_data_text_list


if __name__ == '__main__':
    input_data = input_data('input_example.txt')

    answer = solve(input_data)
    print(f"part01 - triangle count = {answer[0]}")

    print(f"part02 - triangle count = {answer[1]}")
