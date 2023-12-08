"""
Advent of Code - Test
"""
import unittest
import time

import advent2015.day11.puzzle as puzzle


# fmt: off
TEST_DATA = [
    ('tc01', 'part01', 'abcdefgh', 'abcdffaa'),
    ('tc02', 'part01', 'ghijklmn', 'ghjaabcc'),
    ('tc03', 'part02', 'cqjxjnds', 'cqjxxyzz'),
    ('tc04', 'part02', 'cqjxxyzz', 'cqkaabcc'),

    ('tc01', 'is_valid', 'hijklmmn', False),
    ('tc01', 'is_valid', 'abbceffg', False),
    ('tc01', 'is_valid', 'abbcegjk', False),
    ('tc01', 'is_valid', 'abcdffaa', True),
    ('tc01', 'is_valid', 'ghjaabcc', True),
    ('tc01', 'is_valid', 'cqjxxyzz', True),
    ('tc01', 'is_valid', 'cqkaabcc', True),

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
