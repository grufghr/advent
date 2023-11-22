"""
Advent of Code - Test
"""
import unittest
import time

import advent2016.day01.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer01 = [5, 2, 12, 8]
    example_answer02 = [None, None, None, 4]

    answer01 = 242
    answer02 = 150

    execution_time = 1.0

    def test_001_example_01(self):
        input_data = puzzle.load_data('input_example.txt')
        for tc, input_data_tc in puzzle.input_data_iter(input_data):
            answer01 = puzzle.solve01(input_data_tc)
            self.assertEqual(answer01, self.example_answer01[tc])

    def test_002_solve_01(self):
        input_data = puzzle.load_data('input.txt')
        answer01 = puzzle.solve01(input_data)
        self.assertEqual(answer01, self.answer01)

    def test_003_example_02(self):
        input_data = puzzle.load_data('input_example.txt')
        for tc, input_data_tc in puzzle.input_data_iter(input_data):
            answer02 = puzzle.solve02(input_data_tc)
            self.assertEqual(answer02, self.example_answer02[tc])

    def test_004_solve_02(self):
        input_data = puzzle.load_data('input.txt')
        ts = time.time()
        answer02 = puzzle.solve02(input_data)
        t = time.time() - ts
        self.assertEqual(answer02, self.answer02)
        self.assertLess(t, self.execution_time, f"part02 {t:2.5f} secs")
        print(f"execution_time {t:2.5f} secs")
