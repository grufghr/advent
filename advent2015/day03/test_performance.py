"""
Advent of Code - Performance test
"""
import unittest
import time

import advent2015.day03.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    execution_time = 1.0

    def test_performance(self):
        input_data = next(puzzle.input_data_iter('input.txt'))

        ts = time.time()
        puzzle.solve(input_data, 2)
        t = time.time() - ts
        print(f"execution_time {t:2.5f} secs")
        self.assertLess(t, self.execution_time, f"part02 {t:2.5f} secs")