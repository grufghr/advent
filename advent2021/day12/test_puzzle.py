"""
Advent of Code - Test
"""
import unittest
import time

import advent2021.day12.puzzle as puzzle


class PuzzleTest(unittest.TestCase):
    example_01 = [
        ("input_example01.txt", 10),
        ("input_example02.txt", 19),
        ("input_example03.txt", 226),
    ]
    example_02 = [
        ("input_example01.txt", 36),
        ("input_example02.txt", 103),
        ("input_example03.txt", 3509),
    ]

    answer01 = 5212
    answer02 = 134862

    execution_time = 1.0

    def test_001_example_01(self):
        for input_file, expected_result in self.example_01:
            with self.subTest(input_file):
                input_data = puzzle.load_data(input_file)
                result = puzzle.solve01(input_data)
                self.assertEqual(result, expected_result)

    def test_002_solve_01(self):
        input_data = puzzle.load_data("input.txt")
        answer01 = puzzle.solve01(input_data)
        self.assertEqual(answer01, self.answer01)

    def test_003_example_02(self):
        for input_file, expected_result in self.example_02:
            with self.subTest(input_file):
                input_data = puzzle.load_data(input_file)
                result = puzzle.solve02(input_data)
                self.assertEqual(result, expected_result)

    def test_004_solve_02(self):
        input_data = puzzle.load_data("input.txt")
        ts = time.time()
        answer02 = puzzle.solve02(input_data)
        t = time.time() - ts
        self.assertEqual(answer02, self.answer02)
        self.assertLess(t, self.execution_time, f"part02 {t:2.5f} secs")
        print(f"execution_time {t:2.5f} secs")
