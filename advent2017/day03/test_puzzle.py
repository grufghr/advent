"""
Advent of Code - Test
"""
import unittest
import time

import advent2017.day03.puzzle as puzzle


class PuzzleTest(unittest.TestCase):
    example_data = [(1, 0), (12, 3), (23, 2), (1024, 31)]

    puzzle_input = 368078

    answer01 = 371
    answer02 = 369601

    execution_time = 1.0

    def test_001_examples(self):
        for input_data, expected_result in self.example_data:
            with self.subTest(input_data):
                result = puzzle.solve01(input_data)
                self.assertEqual(result, expected_result)

    def test_002_01_input(self):
        answer02 = puzzle.solve02(self.puzzle_input)
        self.assertEqual(answer02, self.answer02)


    def test_003_02_input(self):
        ts = time.time()
        answer02 = puzzle.solve02(self.puzzle_input)
        t = time.time() - ts
        self.assertEqual(answer02, self.answer02)
        self.assertLess(t, self.execution_time, f"part02 {t:2.5f} secs")
        print(f"execution_time {t:2.5f} secs")
