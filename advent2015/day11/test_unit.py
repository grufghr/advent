"""
Advent of Code - Test
"""
import unittest
import time

import advent2015.day11.puzzle as puzzle


# fmt: off
TEST_DATA = [
    ('tc01', 'isvalid', 'hijklmmn', False),
    ('tc01', 'isvalid', 'abbceffg', False),
    ('tc01', 'isvalid', 'abbcegjk', False),
    ('tc01', 'isvalid', 'abcdffaa', True),
    ('tc01', 'isvalid', 'ghjaabcc', True),
    ('tc01', 'isvalid', 'cqjxxyzz', True),
    ('tc01', 'isvalid', 'cqkaabcc', True),

    ('tc01', 'part01', 'abcdefgh', 'abcdffaa'),
    ('tc02', 'part01', 'ghijklmn', 'ghjaabcc'),
    ('tc03', 'part02', 'cqjxjnds', 'cqjxxyzz'),
    ('tc04', 'part02', 'cqjxxyzz', 'cqkaabcc'),
]
EXECUTION_TIME = 15.0
# fmt: on


class PuzzleUnit(unittest.TestCase):
    def test_unit(self):
        for name, part, input_data, expected_answer in TEST_DATA:
            with self.subTest(name):
                ts = time.time()
                if part == 'isvalid':
                    answer = puzzle.is_valid(input_data)
                elif part == 'part01':
                    answer = puzzle.solve01(input_data)
                elif part == 'part02':
                    answer = puzzle.solve02(input_data)
                else:
                    raise Exception(f'unknown function {part}')
                ts = time.time() - ts
                self.assertEqual(answer, expected_answer, 'answer not expected')
                self.assertLess(ts, EXECUTION_TIME, f'part02 {ts:2.5f} secs')
