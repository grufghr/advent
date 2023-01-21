"""
Advent of Code - Test Case
"""
import unittest
import time

import advent2021.day05.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer01 = 5
    example_answer02 = 12

    answer01 = 6666
    answer02 = 19081

    execution_time = 1.0

    def test_001_input_example(self):
        input_data = puzzle.load_data('input_example.txt')

        answer01 = puzzle.solve01(input_data)
        self.assertEqual(answer01, self.example_answer01)

        answer02 = puzzle.solve02(input_data)
        self.assertEqual(answer02, self.example_answer02)

    def test_002_input(self):
        input_data = puzzle.load_data('input.txt')

        answer01 = puzzle.solve01(input_data)
        self.assertEqual(answer01, self.answer01)

        ts = time.time()
        answer02 = puzzle.solve02(input_data)
        t = time.time() - ts
        self.assertEqual(answer02, self.answer02)
        self.assertLess(t, self.execution_time, f"part02 {t:2.5f} secs")
        print(f"execution_time {t:2.5f} secs")
