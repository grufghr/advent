"""
Advent of Code - Test
"""
import unittest
import time

import advent2015.day04.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer01 = [609043, 1048970]
    example_answer02 = [6742839, 5714438]

    answer01 = 254575
    answer02 = 1038736

    execution_time = 2.0

    def test_001_01_input_example(self):
        input_data = puzzle.load_data('input_example.txt')
        for tc, input_data_tc in puzzle.input_data_iter(input_data):
            answer01 = puzzle.solve01(input_data_tc)
            self.assertEqual(answer01, self.example_answer01[tc])

    def test_002_02_input_example(self):
        input_data = puzzle.load_data('input_example.txt')
        for tc, input_data_tc in puzzle.input_data_iter(input_data):
            answer02 = puzzle.solve02(input_data_tc)
            self.assertEqual(answer02, self.example_answer02[tc])

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
