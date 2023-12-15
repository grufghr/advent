"""
Advent of Code - Test
"""
import unittest
import time

import advent2023.day15.puzzle as puzzle


# fmt: off
TEST_INPUT = [
    ('tc01', 'part01', 'input_example.txt', 1320),
    ('tc02', 'part01', 'input.txt',         516657),
    ('tc03', 'part02', 'input_example.txt', 145),
    ('tc04', 'part02', 'input.txt',         210906),
]
EXECUTION_TIME = 10.0
# fmt: on


class PuzzleTest(unittest.TestCase):
    def test_puzzle(self):
        for name, funcname, input_data_file, expected_answer in TEST_INPUT:
            with self.subTest(name):
                input_data = puzzle.load_data(input_data_file)
                func = getattr(puzzle, funcname)
                ts = time.time()
                answer = func(input_data)
                ts = time.time() - ts
                self.assertEqual(answer, expected_answer, 'answer not expected')
                self.assertLess(ts, EXECUTION_TIME, f'part02 {ts:2.5f} secs')
