"""
Advent of Code - Test
"""
import unittest
import time

import advent2021.day12.puzzle as puzzle


# fmt: off
TEST_INPUT = [
    ('tc01', 'part01', 'input_example.txt', 10),
    ('tc02', 'part01', 'input.txt',         5212),
    ('tc03', 'part02', 'input_example.txt', 36),
    ('tc04', 'part02', 'input.txt',         134862),

    ('tc01', 'part01', 'input_exampleA.txt', 226),
    ('tc02', 'part01', 'input_exampleB.txt', 19),
    ('tc03', 'part02', 'input_exampleA.txt', 3509),
    ('tc04', 'part02', 'input_exampleB.txt', 103),
]
EXECUTION_TIME = 15.0
# fmt: on


class PuzzleTest(unittest.TestCase):
    def test_puzzle(self):
        for name, funcname, input_data_file, expected_answer in TEST_INPUT:
            with self.subTest(name):
                input_data = puzzle.load_data(input_data_file)                
                func = getattr(puzzle, funcname)
                ts = time.time()
                answer = func(input_data)
                ts = time.time() - ts
                self.assertEqual(answer, expected_answer, 'answer not expected')
                self.assertLess(ts, EXECUTION_TIME, f'part02 {ts:2.5f} secs')
