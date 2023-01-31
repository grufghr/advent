#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Visualisation
"""
from matplotlib import pyplot
import matplotlib as mpl

import puzzle

# Visualisations
# make a color map of fixed colors
COLOR_MAP1 = mpl.colors.LinearSegmentedColormap.from_list('height_gradient_map',
                                                          ['green', 'blue',
                                                              'white'],
                                                          256)
COLOR_MAP2 = mpl.colors.LinearSegmentedColormap.from_list('height_gradient_map',
                                                          ['white', 'black'],
                                                          256)


if __name__ == '__main__':
    input_data = puzzle.input_data('input.txt')

    grid_map = puzzle.GridMap([list(map(puzzle.convert_height, i))
                               for i in input_data.split("\n")])

    fig, map1 = pyplot.subplots(1, 1)
    fig.suptitle('Grid Maps')

    m1 = map1.imshow(grid_map.height_map,
                     interpolation='nearest',
                     cmap=COLOR_MAP1)
    map1.set_title('Height Map')
    map1.axis('off')

    pyplot.colorbar(m1, cmap=COLOR_MAP1, orientation='horizontal')
    pyplot.show()
