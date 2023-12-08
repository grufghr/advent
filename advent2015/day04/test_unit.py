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
EXECUTION_TIME = 15.0
# fmt: on


class PuzzleUnit(unittest.TestCase):
    def test_unit(self):
        for name, part, input_data, expected_answer in TEST_DATA:
            with self.subTest(name):
                ts = time.time()
                if part == 'part01':
                    answer = puzzle.solve01(input_data)
                elif part == 'part02':
                    answer = puzzle.solve02(input_data)
                else:
                    raise Exception(f'unknown function {part}')
                ts = time.time() - ts
                self.assertEqual(answer, expected_answer, 'answer not expected')
                self.assertLess(ts, EXECUTION_TIME, f'part02 {ts:2.5f} secs')
