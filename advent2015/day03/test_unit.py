"""
Advent of Code - Test
"""
import unittest
import time

import advent2015.day03.puzzle as puzzle


# fmt: off
TEST_DATA = [
    ('tc01', 'part01', '>',          2),
    ('tc02', 'part01', '^>v<',       4),
    ('tc03', 'part01', '^v^v^v^v^v', 2),
    ('tc04', 'part01', '^v',         2),

    ('tc01', 'part02', '>',          2),
    ('tc02', 'part02', '^>v<',       3),
    ('tc03', 'part02', '^v^v^v^v^v', 11),
    ('tc04', 'part02', '^v',         3),
]
EXECUTION_TIME = 1.0
# fmt: on


class PuzzleUnit(unittest.TestCase):
    def test_unit(self):
        for name, part, input_data, expected_answer in TEST_DATA:
            with self.subTest(name):
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
