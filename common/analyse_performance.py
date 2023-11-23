#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Code Analysis
"""
import cProfile
import pstats
import io
from pstats import SortKey

import advent2015.day05.puzzle as puzzle

if __name__ == "__main__":
    input_data = puzzle.load_data("input.txt")

    pr = cProfile.Profile()
    pr.enable()

    # ... do something ...
    answer = puzzle.solve02(input_data)
    print(answer)

    pr.disable()
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
