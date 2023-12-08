"""
Advent of Code - Test
"""
import unittest
import time

import advent2017.day01.puzzle as puzzle


# fmt: off
TEST_DATA = [
    ('tc01', 'part01', '1122',     3),
    ('tc02', 'part01', '1111',     4),
    ('tc03', 'part01', '1234',     0),
    ('tc04', 'part01', '91212129', 9),
    ('tc05', 'part01', '1212',     0),
    ('tc06', 'part01', '1221',     3),
    ('tc07', 'part01', '123425',   0),
    ('tc08', 'part01', '123123',   0),
    ('tc00', 'part01', '12131415', 0),

    ('tc01', 'part02', '1122',     0),
    ('tc02', 'part02', '1111',     4),
    ('tc03', 'part02', '1234',     0),
    ('tc04', 'part02', '91212129', 6),
    ('tc05', 'part02', '1212',     6),
    ('tc06', 'part02', '1221',     0),
    ('tc07', 'part02', '123425',   4),
    ('tc08', 'part02', '123123',   12),
    ('tc09', 'part02', '12131415', 4),

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
