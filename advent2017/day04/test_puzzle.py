"""
Advent of Code - Test
"""
import unittest
import time

import advent2017.day04.puzzle as puzzle


class PuzzleTest(unittest.TestCase):
    example_data_01 = [
        ('aa bb cc dd ee', True),
        ('aa bb cc dd aa', False),
        ('aa bb cc dd aaa', True),
    ]
    example_data_02 = [
        ('abcde fghij', True),
        ('abcde xyz ecdab', False),
        ('a ab abc abd abf abj', True),
        ('iiii oiii ooii oooi oooo', True),
        ('oiii ioii iioi iiio', False),
    ]

    answer01 = 325
    answer02 = 119

    execution_time = 1.0

    def test_001_example_01(self):
        for input_data, expected_result in self.example_data_01:
            with self.subTest(input_data):
                result = puzzle.policy01(input_data)
                self.assertEqual(result, expected_result)

    def test_002_solve_01(self):
        input_data = puzzle.load_data('input.txt')
        answer01 = puzzle.solve01(input_data)
        self.assertEqual(answer01, self.answer01)

    def test_003_example_02(self):
        for input_data, expected_result in self.example_data_02:
            with self.subTest(input_data):
                result = puzzle.policy02(input_data)
                self.assertEqual(result, expected_result)

    def test_004_solve_02(self):
        input_data = puzzle.load_data('input.txt')
        ts = time.time()
        answer02 = puzzle.solve02(input_data)
        t = time.time() - ts
        self.assertEqual(answer02, self.answer02)
        self.assertLess(t, self.execution_time, f'part02 {t:2.5f} secs')
        print(f'execution_time {t:2.5f} secs')
