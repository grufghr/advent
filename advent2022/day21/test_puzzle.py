"""
Advent of Code - Test
"""
import unittest
import time

import advent2022.day21.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example1_answer01 = 152
    example1_answer02 = 301

    example2_answer01 = 34
    example2_answer02 = 19

    answer01 = 21120928600114
    answer02 = 3453748220116

    execution_time = 1.0

    def test_001_example_011(self):
        input_data = puzzle.load_data('input_example1.txt')
        answer01 = puzzle.solve01(input_data)
        self.assertEqual(answer01, self.example1_answer01)

    def test_001_example_012(self):
        input_data = puzzle.load_data('input_example2.txt')
        answer01 = puzzle.solve01(input_data)
        self.assertEqual(answer01, self.example2_answer01)

    def test_002_solve_01(self):
        input_data = puzzle.load_data('input.txt')
        answer01 = puzzle.solve01(input_data)
        self.assertEqual(answer01, self.answer01)

    def test_003_example_021(self):
        input_data = puzzle.load_data('input_example1.txt')
        answer02 = puzzle.solve02(input_data)
        self.assertEqual(answer02, self.example1_answer02)

    def test_003_example_022(self):
        input_data = puzzle.load_data('input_example2.txt')
        answer02 = puzzle.solve02(input_data)
        self.assertEqual(answer02, self.example2_answer02)

    def test_004_solve_02(self):
        input_data = puzzle.load_data('input.txt')
        ts = time.time()
        answer02 = puzzle.solve02(input_data)
        t = time.time() - ts
        self.assertEqual(answer02, self.answer02)
        self.assertLess(t, self.execution_time, f"part02 {t:2.5f} secs")
        print(f"execution_time {t:2.5f} secs")
