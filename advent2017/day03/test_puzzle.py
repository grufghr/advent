"""
Advent of Code - Test
"""
import unittest
import time

import advent2017.day03.puzzle as puzzle


class PuzzleTest(unittest.TestCase):
    example_testdata01 = [(1, 0), (12, 3), (23, 2), (1024, 31)]

    answer01 = 371
    answer02 = 369601

    execution_time = 1.0

    def test_001_example_01(self):
        for input_data, expected_result in self.example_testdata01:
            with self.subTest(input_data):
                result = puzzle.solve01(input_data)
                self.assertEqual(result, expected_result)

    def test_002_solve_01(self):
        input_data = puzzle.load_data('input.txt')
        answer01 = puzzle.solve01(input_data)
        self.assertEqual(answer01, self.answer01)

    def test_003_example_02(self):
        pass

    def test_004_solve_02(self):
        input_data = puzzle.load_data('input.txt')
        ts = time.time()
        answer02 = puzzle.solve02(input_data)
        t = time.time() - ts
        self.assertEqual(answer02, self.answer02)
        self.assertLess(t, self.execution_time, f'part02 {t:2.5f} secs')
        print(f'execution_time {t:2.5f} secs')
