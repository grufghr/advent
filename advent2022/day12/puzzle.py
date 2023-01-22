#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Solve Puzzle
"""
import os
from collections import deque
import numpy as np


class GridMap():

    def __init__(self, height_map_array):
        self.height_map = np.array(height_map_array)

        self.bounds_n, self.bounds_w = (0, 0)
        self.bounds_s, self.bounds_e = self.height_map.shape

        self.start = self.find_start_loc()
        self.end = self.find_end_loc()

    def find_start_loc(self):
        # find start location (r,c)
        s = np.where(self.height_map == np.min(self.height_map))
        sl = list(zip(s[0], s[1]))
        start = sl[0]
        return start

    def find_end_loc(self):
        # find end location (r,c)
        e = np.where(self.height_map == np.max(self.height_map))
        el = list(zip(e[0], e[1]))
        end = el[0]
        return end

    def next_moves(self, loc_c):
        # find all valid next move (N,E,S,W)
        r, c = loc_c
        moves = []
        # check N
        if r > self.bounds_n:
            loc_n = (r - 1, c)
            if self.valid_move(loc_c, loc_n):
                moves.append(loc_n)
        # check E
        if (c + 1) < self.bounds_e:
            loc_n = (r, c + 1)
            if self.valid_move(loc_c, loc_n):
                moves.append(loc_n)
        # check S
        if (r + 1) < self.bounds_s:
            loc_n = (r + 1, c)
            if self.valid_move(loc_c, loc_n):
                moves.append(loc_n)
        # check W
        if c > self.bounds_w:
            loc_n = (r, c - 1)
            if self.valid_move(loc_c, loc_n):
                moves.append(loc_n)
        return moves

    # Valid move is up one step (or down as many as required)
    # Note: this may result in path jumping down into hole
    #       from end cannot be reached.
    def valid_move(self, loc_c, loc_n):
        h_diff = self.height_map[loc_n] - self.height_map[loc_c]
        if h_diff <= 1:
            return True
        return False

    # calculate shortest distance from start to end
    # Note: not completely accurate?
    def calc_distance_to_end(self, loc_s=None, loc_e=None):
        if not loc_s:
            loc_s = self.find_start_loc()

        if not loc_e:
            loc_e = self.find_end_loc()

        q = deque()  # queue of locations & distances
        q.append((loc_s, 0))  # initial with start location
        visited = set()

        # walk map to find shortest distance
        while q:
            loc_c, distance_c = q.popleft()

            if (loc_c not in visited):
                visited.add(loc_c)

                # reached end (stop searching)
                if loc_c == loc_e:
                    return distance_c

                # search next steps
                distance_n = distance_c + 1
                for loc_n in self.next_moves(loc_c):
                    q.append((loc_n, distance_n))

        return None


def convert_height(hc):
    if hc == 'S':
        return 0
    elif hc == 'E':
        return ord('z') - ord('a') + 2
    else:
        return ord(hc) - ord('a') + 1


def solve01(height_map_text):
    # part 01

    # convert map into 2d array on heights (int)
    grid_map = GridMap([list(map(convert_height, i))
                        for i in height_map_text.split("\n")])

    distance = grid_map.calc_distance_to_end()
    return distance


def solve02(height_map_text):
    # part 02

    # convert map into 2d array on heights (int)
    grid_map = GridMap([list(map(convert_height, i))
                        for i in height_map_text.split("\n")])

    # Brute force all possible start places
    hm = grid_map.height_map
    possible_s = list(zip(*np.where(hm == 1)))

    # Find shortest distance to end for all possible stating places
    distance_l = list()
    for loc_n in possible_s:
        distance_s = grid_map.calc_distance_to_end(loc_s=loc_n)
        if distance_s:
            distance_l.append(distance_s)
    distance_s = min(distance_l)

    return distance_s


def load_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, 'r') as filehandle:
        input_data_text = filehandle.read()

    return input_data_text


if __name__ == '__main__':
    input_data = load_data('input.txt')

    answer01 = solve01(input_data)
    print(f"part01 - Path reaches the goal in {answer01} move.\n")

    answer02 = solve02(input_data)
    print(f"part02 - Shortest path from elevation 'a' is {answer02} move.\n")
