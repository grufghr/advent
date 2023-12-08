"""
Advent of Code - Test
"""
import unittest
import time

import advent2022.day21.puzzle as puzzle


# fmt: off
TEST_INPUT = [
    ('tc01', 'part01', 'input_example.txt',   34),
    ('tc02', 'part01', 'input.txt',           21120928600114),
    ('tc03', 'part02', 'input_example.txt',   19),
    ('tc04', 'part02', 'input.txt',           3453748220116),
    
    ('tc05', 'part01', 'input_example01.txt', 152),
    ('tc06', 'part02', 'input_example01.txt', 301),
]
EXECUTION_TIME = 1.0
# fmt: on


class PuzzleTest(unittest.TestCase):
    def test_puzzle(self):
        for name, part, input_data_file, expected_answer in TEST_INPUT:
            with self.subTest(name):
                input_data = puzzle.load_data(input_data_file)
                ts = time.time()
                if part == 'part01':
                    answer = puzzle.part01(input_data)
                elif part == 'part02':
                    answer = puzzle.part02(input_data)
                else:
                    raise Exception(f'unknown function {part}')
                ts = time.time() - ts
                self.assertEqual(answer, expected_answer, 'answer not expected')
                self.assertLess(ts, EXECUTION_TIME, f'part02 {ts:2.5f} secs')
