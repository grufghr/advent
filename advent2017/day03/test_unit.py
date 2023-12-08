"""
Advent of Code - Test
"""
import unittest
import time

import advent2017.day03.puzzle as puzzle

# fmt: off
TEST_DATA = [
    ('tc01', 'part01', 1,    0),
    ('tc02', 'part01', 12,   3),
    ('tc03', 'part01', 23,   2),
    ('tc04', 'part01', 1024, 31),
]
EXECUTION_TIME = 1.0
# fmt: on


class PuzzleUnit(unittest.TestCase):
    def test_unit(self):
        for name, funcname, input_data, expected_answer in TEST_DATA:
            with self.subTest(name):
                func = getattr(puzzle, funcname)
                ts = time.time()
                answer = func(input_data)
                ts = time.time() - ts
                self.assertEqual(answer, expected_answer, 'answer not expected')
                self.assertLess(ts, EXECUTION_TIME, f'part02 {ts:2.5f} secs')
