"""
Advent of Code - Test
"""
import unittest
import time

import advent2018.day02.puzzle as puzzle


class PuzzleTest(unittest.TestCase):
    example_answer01 = 12
    example_answer02 = 'fgij'

    answer01 = 7163
    answer02 = 'ighfbyijnoumxjlxevacpwqtr'

    execution_time = 1.0

    def test_001_example_01(self):
        input_data = puzzle.load_data('input_example01.txt')
        answer01 = puzzle.solve01(input_data)
        self.assertEqual(answer01, self.example_answer01)

    def test_002_solve_01(self):
        input_data = puzzle.load_data('input.txt')
        answer01 = puzzle.solve01(input_data)
        self.assertEqual(answer01, self.answer01)

    def test_003_example_02(self):
        input_data = puzzle.load_data('input_example02.txt')
        answer02 = puzzle.solve02(input_data)
        self.assertEqual(answer02, self.example_answer02)

    def test_004_solve_02(self):
        input_data = puzzle.load_data('input.txt')
        ts = time.time()
        answer02 = puzzle.solve02(input_data)
        t = time.time() - ts
        self.assertEqual(answer02, self.answer02)
        self.assertLess(t, self.execution_time, f'part02 {t:2.5f} secs')
        print(f'execution_time {t:2.5f} secs')
