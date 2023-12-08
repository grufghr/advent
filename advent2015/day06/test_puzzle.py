"""
Advent of Code - Test
"""
import unittest
import time

import advent2015.day06.puzzle as puzzle


# fmt: off
TEST_INPUT = [
    ('tc01', 'part01', 'input_example.txt', 998996),
    ('tc02', 'part01', 'input.txt',         543903),
    ('tc03', 'part02', 'input_example.txt', 1001996),
    ('tc04', 'part02', 'input.txt',         14687245),
]
EXECUTION_TIME = 1.0
# fmt: on


class PuzzleTest(unittest.TestCase):
    def test_puzzle(self):
        for name, part, input_data_file, expected_answer in TEST_INPUT:
            with self.subTest(name):
                input_data = puzzle.load_data(input_data_file)
                ts = time.time()
                if part == 'part01':
                    answer = puzzle.part01(input_data)
                elif part == 'part02':
                    answer = puzzle.part02(input_data)
                else:
                    raise Exception(f'unknown function {part}')
                ts = time.time() - ts
                self.assertEqual(answer, expected_answer, 'answer not expected')
                self.assertLess(ts, EXECUTION_TIME, f'part02 {ts:2.5f} secs')
