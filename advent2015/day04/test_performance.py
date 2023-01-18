"""
Advent of Code - Performance test
"""
import unittest
import time

import advent2015.day04.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    time_part01 = 1.0
    time_part02 = 1.5

    def test_performance(self):
        input_data = next(puzzle.input_data_iter('input.txt'))

        ts = time.time()
        puzzle.solve(input_data, 5)
        t = time.time() - ts
        self.assertLess(t, self.time_part01, f"part01 {t:2.5f} secs")

        ts = time.time()
        puzzle.solve(input_data, 6)
        t = time.time() - ts
        self.assertLess(t, self.time_part02, f"part02 {t:2.5f} secs")
