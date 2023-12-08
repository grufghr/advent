"""
Advent of Code - Test
"""
import unittest
import time

import advent2017.day04.puzzle as puzzle


# fmt: off
TEST_DATA = [
    ('tc01', 'policy01', 'aa bb cc dd ee',           True),
    ('tc02', 'policy01', 'aa bb cc dd aa',           False),
    ('tc03', 'policy01', 'aa bb cc dd aaa',          True),

    ('tc01', 'policy02', 'abcde fghij',              True),
    ('tc02', 'policy02', 'abcde xyz ecdab',          False),
    ('tc03', 'policy02', 'a ab abc abd abf abj',     True),
    ('tc04', 'policy02', 'iiii oiii ooii oooi oooo', True),
    ('tc05', 'policy02', 'oiii ioii iioi iiio',      False),
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
