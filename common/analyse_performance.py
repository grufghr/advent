#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Code Analysis
"""

import cProfile
import pstats
import io
from pstats import SortKey

import puzzle


def performance(func):
    pr = cProfile.Profile()
    pr.enable()

    # ... do something ...
    answer = func(input_data)
    pr.disable()
    print(f'{func} {answer=}')

    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())


if __name__ == '__main__':
    input_data = puzzle.load_data('input.txt')

    performance(puzzle.part01)
    performance(puzzle.part02)
