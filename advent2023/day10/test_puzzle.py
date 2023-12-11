"""
Advent of Code - Test
"""
import unittest
import time

import advent2023.day10.puzzle as puzzle


# fmt: off
TEST_INPUT = [
    ('tc01', 'part01', 'input_example.txt', 4),
    ('tc02', 'part01', 'input.txt',         6640),
    ('tc03', 'part02', 'input_example.txt', 1),
    ('tc04', 'part02', 'input.txt',         411),

    ('tc05', 'part01', 'input_exampleA.txt', 8),
    ('tc06', 'part01', 'input_exampleB.txt', 23),
    ('tc07', 'part01', 'input_exampleC.txt', 70),
    ('tc08', 'part01', 'input_exampleD.txt', 80),

    ('tc09', 'part02', 'input_exampleA.txt', 1),
    ('tc10', 'part02', 'input_exampleB.txt', 4),
    ('tc11', 'part02', 'input_exampleC.txt', 8),
    ('tc12', 'part02', 'input_exampleD.txt', 10),
]
EXECUTION_TIME = 1.0
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
