"""
Advent of Code - Test
"""
import unittest
import time

import advent2015.day11.puzzle as puzzle


class PuzzleTest(unittest.TestCase):
    # fmt: off
    example_data_01 = [
        ("abcdefgh", "abcdffaa"),
        ("ghijklmn", "ghjaabcc")
    ]
    testdata_000 = [
        ("hijklmmn", False),
        ("abbceffg", False),
        ("abbcegjk", False),
        ("abcdffaa", True),
        ("ghjaabcc", True),
        ("cqjxxyzz", True),
        ("cqkaabcc", True),
    ]
    # fmt: on

    answer01 = 'cqjxxyzz'
    answer02 = 'cqkaabcc'

    execution_time = 5.0

    def test_000_is_valid(self):
        for input_data, expected_result in self.testdata_000:
            with self.subTest(input_data):
                result = puzzle.is_valid(input_data)
                self.assertEqual(result, expected_result)

    def test_001_example_01(self):
        for input_data, expected_result in self.example_data_01:
            with self.subTest(input_data):
                result = puzzle.solve01(input_data)
                self.assertEqual(result, expected_result)

    def test_002_solve_01(self):
        input_data = puzzle.load_data('input.txt')
        answer01 = puzzle.solve01(input_data)
        self.assertEqual(answer01, self.answer01)

    @unittest.skip('No examples for part02')
    def test_003_example_02(self):
        input_data = puzzle.load_data('input_example.txt')
        answer02 = puzzle.solve02(input_data)
        self.assertEqual(answer02, self.example_answer02)

    def test_004_solve_02(self):
        # note: answer01 used as input to part02
        input_data = self.answer01
        ts = time.time()
        answer02 = puzzle.solve02(input_data)
        t = time.time() - ts
        self.assertEqual(answer02, self.answer02)
        self.assertLess(t, self.execution_time, f'part02 {t:2.5f} secs')
        print(f'execution_time {t:2.5f} secs')
