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
        for name, part, input_data, expected_answer in TEST_DATA:
            with self.subTest(name):
                ts = time.time()
                if part == 'policy01':
                    answer = puzzle.policy01(input_data)
                elif part == 'policy02':
                    answer = puzzle.policy02(input_data)
                elif part == 'part01':
                    answer = puzzle.solve01(input_data)
                elif part == 'part02':
                    answer = puzzle.solve02(input_data)
                else:
                    raise Exception(f'unknown function {part}')
                ts = time.time() - ts
                self.assertEqual(answer, expected_answer, 'answer not expected')
                self.assertLess(ts, EXECUTION_TIME, f'part02 {ts:2.5f} secs')
