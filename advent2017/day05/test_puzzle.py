"""
Advent of Code - Test
"""
import unittest
import time

import advent2017.day05.puzzle as puzzle


# fmt: off
TEST_INPUT = [
    ('tc01', 'part01', 'input_example.txt', 5),
    ('tc02', 'part01', 'input.txt',         378980),
    ('tc03', 'part02', 'input_example.txt', 10),
    ('tc04', 'part02', 'input.txt',         26889114),
]
EXECUTION_TIME = 15.0
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
