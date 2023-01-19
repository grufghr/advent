"""
Advent of Code - Performance test
"""
import unittest
import time

import advent2022.day12.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    execution_time = 7.0

    def test_performance(self):
        input_data = puzzle.input_data('input.txt')

        ts = time.time()
        puzzle.solve(input_data)
        t = time.time() - ts
        print(f"execution_time {t:2.5f} secs")
        self.assertLess(t, self.execution_time, f"part01&02 {t:2.5f} secs")
