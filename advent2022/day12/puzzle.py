#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021
"""
from matplotlib import pyplot
import matplotlib as mpl
import os
import numpy as np

# Visualisations
# make a color map of fixed colors
COLOR_MAP1 = mpl.colors.LinearSegmentedColormap.from_list('height_gradient_map',
                                                          ['green', 'blue',
                                                              'white'],
                                                          256)
COLOR_MAP2 = mpl.colors.LinearSegmentedColormap.from_list('height_gradient_map',
                                                          ['white', 'black'],
                                                          256)

DEAD_END = 999


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

    def distance_map_init(self, loc_s):
        # create and initialise distance map
        self.distance_map = np.zeros(self.height_map.shape, dtype=int,)
        self.distance_map[:] = DEAD_END
        self.distance_map[loc_s] = 0

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

        self.distance_map_init(loc_s)

        q = []  # queue of locations & distances
        q.append((loc_s, 0))  # initial with start location

        # walk map to find shortest distance
        while len(q) > 0:
            loc_c, distance_c = q.pop()

            for loc_n in self.next_moves(loc_c):
                distance_n = distance_c + 1
                if (self.distance_map[loc_n] > distance_n):
                    self.distance_map[loc_n] = distance_n
                    q.append((loc_n, distance_n))

        return self.distance_map[self.end]

    def visualise(self):
        fig, (map1, map2) = pyplot.subplots(1, 2)
        fig.suptitle('Grid Maps')

        m1 = map1.imshow(self.height_map,
                         interpolation='nearest',
                         cmap=COLOR_MAP1)
        map1.set_title('Height Map')
        map1.axis('off')

        m2 = map2.imshow(self.distance_map,
                         interpolation='nearest',
                         cmap=COLOR_MAP2)
        map2.set_title('Distance Map')
        map2.axis('off')

        pyplot.colorbar(m1, cmap=COLOR_MAP1, orientation='horizontal')
        pyplot.colorbar(m2, cmap=COLOR_MAP2, orientation='horizontal')
        pyplot.show()


def convert_height(hc):
    if hc == 'S':
        return 0
    elif hc == 'E':
        return ord('z') - ord('a') + 2
    else:
        return ord(hc) - ord('a') + 1


def solve(height_map_text):

    # convert map into 2d array on heights (int)
    grid_map = GridMap([list(map(convert_height, i))
                        for i in height_map_text.split("\n")])

    # part 01

    part01 = grid_map.calc_distance_to_end()
    # grid_map.visualise()

    # part 02

    # Brute force starting place
    # need to revisit calc_distance_to_end
    hm = grid_map.height_map

    # produce map with levels 1 & 2
    level = 1
    lm = np.where(hm <= (level + 1), hm, 0)

    # Create filter for dead-ends
    for ir, ic in np.ndindex(lm.shape):
        if lm[ir, ic] != level:
            continue
        if (ir > 0) and (lm[ir - 1, ic] == (level + 1)):
            continue
        if (ic > 0) and (lm[ir, ic - 1] == (level + 1)):
            continue
        if (ir < (lm.shape[0] - 1)) and (lm[ir + 1, ic] == (level + 1)):
            continue
        if (ic < (lm.shape[1] - 1)) and (lm[ir, ic + 1] == (level + 1)):
            continue
        lm[ir, ic] = 0
    lm = np.where(lm == level, lm, 0)

    # All possible start places
    possible_s = list(zip(*np.where(lm == 1)))

    # Find shortest distance to end for all possible stating places
    loc_s = None
    distance_s = DEAD_END
    for loc_n in possible_s:
        distance_n = grid_map.calc_distance_to_end(loc_n)
        if distance_n < distance_s:
            distance_s = distance_n
            loc_s = loc_n
        # print(f"distance starting at {loc_n} took {distance_n}")

    # print(f"Shortest distance starts at {loc_s} took {distance_s}")

    part02 = distance_s
    # grid_map.visualise()

    # return results
    return (part01, part02)


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, 'r') as filehandle:
        input_data_text = filehandle.read()

    return input_data_text


if __name__ == '__main__':
    input_data = input_data('input.txt')

    answer = solve(input_data)
    print(f"part01 - Path reaches the goal in {answer[0]} move.\n")
    print(f"part02 - Shortest path from elevation 'a' is {answer[1]} move.\n")
