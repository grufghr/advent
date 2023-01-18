"""
Advent of Code - Performance test
"""
import unittest
import time

import advent2016.day05.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    execution_time = 40.0

    @unittest.skip("ToDo performance fix")
    def test_performance(self):
        # input_data = next(puzzle.input_data_iter('input.txt'))

        ts = time.time()
        puzzle.solve01('aecefkir')
        t = time.time() - ts
        print(f"execution_time {t:2.5f} secs")
        self.assertLess(t, self.execution_time, f"part02 {t:2.5f} secs")

        ts = time.time()
        puzzle.solve02('aecefkir')
        t = time.time() - ts
        print(f"execution_time {t:2.5f} secs")
        self.assertLess(t, self.execution_time, f"part02 {t:2.5f} secs")
