"""
Advent of Code - Test
"""
import unittest
import time

import advent2015.day04.puzzle as puzzle


# fmt: off
TEST_DATA = [
    ('tc01', 'part01', 'abcdef',  609043),
    ('tc02', 'part01', 'pqrstuv', 1048970),

    ('tc03', 'part02', 'abcdef',  6742839),
    ('tc04', 'part02', 'pqrstuv', 5714438),
]
EXECUTION_TIME = 10.0
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
