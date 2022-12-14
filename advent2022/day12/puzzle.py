#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021
"""
from matplotlib import pyplot
import matplotlib as mpl
import os
import numpy as np

# visualisation
# make a color map of fixed colors
COLOR_MAP1 = mpl.colors.LinearSegmentedColormap.from_list('height_gradient_map',
                                                          ['green', 'blue',
                                                              'white'],
                                                          256)
COLOR_MAP2 = mpl.colors.LinearSegmentedColormap.from_list('height_gradient_map',
                                                          ['red', 'orange',
                                                              'yellow'],
                                                          256)


class GridMap():

    def __init__(self, height_map_array):
        self.height_map = np.array(height_map_array)

        self.bounds_n, self.bounds_w = (0, 0)
        self.bounds_s, self.bounds_e = self.height_map.shape

        # find start location (r,c)
        s = np.where(self.height_map == np.min(self.height_map))
        sl = list(zip(s[0], s[1]))
        self.start = sl[0]

        # find end location (r,c)
        e = np.where(self.height_map == np.max(self.height_map))
        se = list(zip(e[0], e[1]))
        self.end = se[0]

        # create and initialise
        self.distance_map = np.zeros(self.height_map.shape, dtype=int,)
        # number bigger than possible number of steps
        self.distance_map[:] = ((self.bounds_s + 1) * (self.bounds_e + 1)) ^ 2
        self.distance_map[self.start] = 0

    def next_steps(self, loc_c):
        r, c = loc_c
        steps = []
        # check N
        if r > self.bounds_n:
            loc_n = (r - 1, c)
            if self.valid_move(loc_c, loc_n):
                steps.append(loc_n)
        # check E
        if (c + 1) < self.bounds_e:
            loc_n = (r, c + 1)
            if self.valid_move(loc_c, loc_n):
                steps.append(loc_n)
        # check S
        if (r + 1) < self.bounds_s:
            loc_n = (r + 1, c)
            if self.valid_move(loc_c, loc_n):
                steps.append(loc_n)
        # check W
        if c > self.bounds_w:
            loc_n = (r, c - 1)
            if self.valid_move(loc_c, loc_n):
                steps.append(loc_n)
        return steps

    def valid_move(self, loc_c, loc_n):
        h_diff = self.height_map[loc_n] - self.height_map[loc_c]
        if h_diff <= 1:
            return True
        return False

    def calc_distance_to_end(self):

        q = []  # queue of locations & distances
        q.append((self.start, 0))  # initial with start location

        # walk map to find shortest distance
        while len(q) > 0:
            loc_c, distance_c = q.pop()
            if self.distance_map[loc_c] != distance_c:
                continue
            for loc_n in self.next_steps(loc_c):
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

    shortest_distance = grid_map.calc_distance_to_end()

    # grid_map.visualise()

    # return results
    return shortest_distance


def input_data(filename):
    input_data_file = os.path.join(os.path.dirname(__file__), filename)

    # read in data file
    with open(input_data_file, 'r') as filehandle:
        input_data_text = filehandle.read()

    return input_data_text


if __name__ == '__main__':
    input_data = input_data('input_example.txt')

    answer = solve(input_data)
    print(f"path reaches the goal in {answer} steps.\n")
