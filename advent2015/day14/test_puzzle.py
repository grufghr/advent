"""
Advent of Code - Test
"""
import unittest
import time

import advent2015.day14.puzzle as puzzle


# fmt: off
TEST_INPUT = [
    ('tc01', 'part01', 'input_example.txt', 1120),
    ('tc02', 'part01', 'input.txt',         2696),
    ('tc03', 'part02', 'input_example.txt', 689),
    ('tc04', 'part02', 'input.txt',         1084),
]
EXECUTION_TIME = 7.0
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
