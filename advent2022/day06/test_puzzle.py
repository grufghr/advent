"""
Advent of Code - Test
"""
import unittest
import time

import advent2022.day06.puzzle as puzzle


# fmt: off
TEST_INPUT = [
    ('tc01', 'part01', 'input_example.txt', [7, 5, 6, 10, 11]),
    ('tc03', 'part02', 'input_example.txt', [19, 23, 23, 29, 26]),
    ('tc02', 'part01', 'input.txt', 1531),
    ('tc04', 'part02', 'input.txt', 2518),
]
EXECUTION_TIME = 1.0
# fmt: on

    def _input_data_iter(self, input_data):
        for tc, input_data_tc in enumerate(input_data.splitlines()):
            yield tc, input_data_tc

    def test_001_example_01(self):
        input_data = puzzle.load_data('input_example_tc.txt')
        for tc, input_data_tc in self._input_data_iter(input_data):
            ('tc02', 'part01', 'input.txt', puzzle.part01(input_data_tc)),
            self.assertEqual(answer01, self.example_answer01[tc])

    def test_002_solve_01(self):
        input_data = puzzle.load_data('input.txt')
        ('tc02', 'part01', 'input.txt', puzzle.part01(input_data)),
        self.assertEqual(answer01, self.answer01)

    def test_003_example_02(self):
        input_data = puzzle.load_data('input_example_tc.txt')
        for tc, input_data_tc in self._input_data_iter(input_data):
            ('tc04', 'part02', 'input.txt', puzzle.part02(input_data_tc)),
            self.assertEqual(answer02, self.example_answer02[tc])

    def test_004_solve_02(self):
        input_data = puzzle.load_data('input.txt')
        ts = time.time()
        ('tc04', 'part02', 'input.txt', puzzle.part02(input_data)),
        t = time.time() - ts
        self.assertEqual(answer02, self.answer02)
        self.assertLess(t, self.execution_time, f'part02 {t:2.5f} secs')
        print(f'execution_time {t:2.5f} secs')
