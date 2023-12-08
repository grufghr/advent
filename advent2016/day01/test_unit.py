"""
Advent of Code - Test
"""
import unittest
import time

import advent2016.day01.puzzle as puzzle

# fmt: off
TEST_DATA = [
    ('tc01', 'part01', 'R2, L3',         5),
    ('tc02', 'part01', 'R2, R2, R2',     2),
    ('tc03', 'part01', 'R5, L5, R5, R3', 12),
    ('tc04', 'part01', 'R8, R4, R4, R8', 8),

    ('tc01', 'part02', 'R2, L3',         None),
    ('tc02', 'part02', 'R2, R2, R2',     None),
    ('tc03', 'part02', 'R5, L5, R5, R3', None),
    ('tc04', 'part02', 'R8, R4, R4, R8', 4),
]
EXECUTION_TIME = 15.0
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
