"""
Advent of Code - Performance test
"""
import unittest
import time

import advent2015.day02.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    time_part01 = 1.0
    time_part02 = 1.0

    def test_performance(self):
        input_data = puzzle.input_data('input.txt')

        ts = time.time()
        puzzle.solve(input_data)
        t = time.time() - ts
        self.assertLess(t, self.time_part01, f"part01 {t:2.5f} secs")

        ts = time.time()
        puzzle.solve(input_data)
        t = time.time() - ts
        self.assertLess(t, self.time_part02, f"part02 {t:2.5f} secs")
