"""
Advent of Code - Test Case
"""
import unittest
import time

import advent2021.day25.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer01 = 58
    example_answer02 = None

    answer01 = 532
    answer02 = None

    execution_time = 20.0

    def test_001_input_example(self):
        input_data = puzzle.load_data('input_example.txt')

        answer01 = puzzle.solve01(input_data)
        self.assertEqual(answer01, self.example_answer01)

        # no part 02
        # answer02 = puzzle.solve02(input_data)
        # self.assertEqual(answer02, self.example_answer02)

    def test_002_input(self):
        input_data = puzzle.load_data('input.txt')

        # no part 02
        # answer01 = puzzle.solve01(input_data)
        # self.assertEqual(answer01, self.answer01)

        # no part 02 - timing part 01
        ts = time.time()
        answer01 = puzzle.solve01(input_data)
        t = time.time() - ts
        self.assertEqual(answer01, self.answer01)
        self.assertLess(t, self.execution_time, f"part02 {t:2.5f} secs")
        print(f"execution_time {t:2.5f} secs")
