"""
Advent of Code - Test
"""
import unittest
import time

import advent2015.day14.puzzle as puzzle


class PuzzleTest(unittest.TestCase):
    example_data_01 = (1000, 1120)
    example_data_02 = (1000, 689)

    input_data_01 = (2503, 2696)
    input_data_02 = (2503, 1084)

    execution_time = 1.0

    def test_001_example_01(self):
        input_data = puzzle.load_data('input_example.txt')
        answer01 = puzzle.solve01(input_data, self.example_data_01[0])
        self.assertEqual(answer01, self.example_data_01[1])

    def test_002_solve_01(self):
        input_data = puzzle.load_data('input.txt')
        answer01 = puzzle.solve01(input_data, self.input_data_01[0])
        self.assertEqual(answer01, self.input_data_01[1])

    def test_003_example_02(self):
        input_data = puzzle.load_data('input_example.txt')
        answer02 = puzzle.solve02(input_data, self.example_data_02[0])
        self.assertEqual(answer02, self.example_data_02[1])

    def test_004_solve_02(self):
        input_data = puzzle.load_data('input.txt')
        ts = time.time()
        answer02 = puzzle.solve02(input_data, self.input_data_02[0])
        t = time.time() - ts
        self.assertEqual(answer02, self.input_data_02[1])
        self.assertLess(t, self.execution_time, f'part02 {t:2.5f} secs')
        print(f'execution_time {t:2.5f} secs')
