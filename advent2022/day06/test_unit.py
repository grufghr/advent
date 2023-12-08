"""
Advent of Code - Test
"""
import unittest
import time

import advent2022.day06.puzzle as puzzle


# fmt: off
TEST_DATA = [
    ('tc01', 'part01', 'mjqjpqmgbljsphdztnvjfqwrcgsmlb',    7),
    ('tc02', 'part01', 'bvwbjplbgvbhsrlpgdmjqwftvncz',      5),
    ('tc03', 'part01', 'nppdvjthqldpwncqszvftbrmjlhg',      6),
    ('tc04', 'part01', 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
    ('tc05', 'part01', 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',  11),

    ('tc01', 'part02', 'mjqjpqmgbljsphdztnvjfqwrcgsmlb',    19),
    ('tc02', 'part02', 'bvwbjplbgvbhsrlpgdmjqwftvncz',      23),
    ('tc03', 'part02', 'nppdvjthqldpwncqszvftbrmjlhg',      23),
    ('tc04', 'part02', 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
    ('tc05', 'part02', 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',  26),
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
