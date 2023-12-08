"""
Advent of Code - Test
"""
import unittest
import time

import advent2015.day01.puzzle as puzzle


# fmt: off
TEST_DATA = [
    ('tc01', 'part01', '(())',    0),
    ('tc02', 'part01', '()()',    0),
    ('tc03', 'part01', '(((',     3),
    ('tc04', 'part01', '(()(()(', 3),
    ('tc05', 'part01', '))(((((', 3),
    ('tc06', 'part01', '())',     -1),
    ('tc07', 'part01', '))(',     -1),
    ('tc08', 'part01', ')))',     -3),
    ('tc09', 'part01', ')())())', -3),
    ('tc10', 'part01', ')',       -1),
    ('tc11', 'part01', '()())',   -1),

    ('tc01', 'part02', '(())',    0),
    ('tc02', 'part02', '()()',    0),
    ('tc03', 'part02', '(((',     0),
    ('tc04', 'part02', '(()(()(', 0),
    ('tc05', 'part02', '))(((((', 1),
    ('tc06', 'part02', '())',     3),
    ('tc07', 'part02', '))(',     1),
    ('tc08', 'part02', ')))',     1),
    ('tc09', 'part02', ')())())', 1),
    ('tc10', 'part02', ')',       1),
    ('tc11', 'part02', '()())',   5),
]
EXECUTION_TIME = 1.0
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
