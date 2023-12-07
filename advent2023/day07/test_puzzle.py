"""
Advent of Code - Test
"""
import unittest
import time

import advent2023.day07.puzzle as puzzle

# fmt: off
TEST_DATA = [
    ('tc01', 'part01', 'input_example.txt', 6440),
    ('tc02', 'part01', 'input.txt',         250232501),
    ('tc03', 'part02', 'input_example.txt', 5905),
    ('tc04', 'part02', 'input.txt',         249138943),
]
EXECUTION_TIME = 1.0
# fmt: on


class PuzzleTest(unittest.TestCase):
    def test_advent2023_day07(self):
        for name, part, input_data_file, expected_answer in TEST_DATA:
            with self.subTest(name):
                input_data = puzzle.load_data(input_data_file)
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
