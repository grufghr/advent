"""
Advent of Code - Test
"""
import unittest
import time

import advent2015.day10.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer01 = 82350
    example_answer02 = 1166642

    answer01 = 360154
    answer02 = 5103798

    execution_time = 7.0

    def test_001_01_input_example(self):
        input_data = puzzle.load_data('input_example.txt')
        answer01 = puzzle.solve01(input_data)
        self.assertEqual(answer01, self.example_answer01)

    def test_002_02_input_example(self):
        input_data = puzzle.load_data('input_example.txt')
        answer02 = puzzle.solve02(input_data)
        self.assertEqual(answer02, self.example_answer02)

    def test_003_01_input(self):
        input_data = puzzle.load_data('input.txt')
        answer01 = puzzle.solve01(input_data)
        self.assertEqual(answer01, self.answer01)

    def test_004_02_input(self):
        input_data = puzzle.load_data('input.txt')
        ts = time.time()
        answer02 = puzzle.solve02(input_data)
        t = time.time() - ts
        self.assertEqual(answer02, self.answer02)
        self.assertLess(t, self.execution_time, f"part02 {t:2.5f} secs")
        print(f"execution_time {t:2.5f} secs")
