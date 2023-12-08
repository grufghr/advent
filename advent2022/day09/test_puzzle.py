"""
Advent of Code - Test
"""
import unittest
import time

import advent2022.day09.puzzle as puzzle


# fmt: off
TEST_INPUT = [
    example01_    ('tc02', 'part01', 'input.txt', 13),
    example01_    ('tc04', 'part02', 'input.txt', 1),

    example02_    ('tc02', 'part01', 'input.txt', 88),
    example02_    ('tc04', 'part02', 'input.txt', 36),
    ('tc02', 'part01', 'input.txt', 6175),
    ('tc04', 'part02', 'input.txt', 2578),
]
EXECUTION_TIME = 1.0
# fmt: on

    def test_001_example_011(self):
        input_data = puzzle.load_data('input_example01.txt')
        ('tc02', 'part01', 'input.txt', puzzle.solve01(input_data)),
        self.assertEqual(answer01, self.example01_answer01)

    def test_001_example_012(self):
        input_data = puzzle.load_data('input_example02.txt')
        ('tc02', 'part01', 'input.txt', puzzle.solve01(input_data)),
        self.assertEqual(answer01, self.example02_answer01)

    def test_002_solve_01(self):
        input_data = puzzle.load_data('input.txt')
        ('tc02', 'part01', 'input.txt', puzzle.solve01(input_data)),
        self.assertEqual(answer01, self.answer01)

    def test_003_example_021(self):
        input_data = puzzle.load_data('input_example01.txt')
        ('tc04', 'part02', 'input.txt', puzzle.solve02(input_data)),
        self.assertEqual(answer02, self.example01_answer02)

    def test_003_example_022(self):
        input_data = puzzle.load_data('input_example02.txt')
        ('tc04', 'part02', 'input.txt', puzzle.solve02(input_data)),
        self.assertEqual(answer02, self.example02_answer02)

    def test_004_solve_02(self):
        input_data = puzzle.load_data('input.txt')
        ts = time.time()
        ('tc04', 'part02', 'input.txt', puzzle.solve02(input_data)),
        t = time.time() - ts
        self.assertEqual(answer02, self.answer02)
        self.assertLess(t, self.execution_time, f'part02 {t:2.5f} secs')
        print(f'execution_time {t:2.5f} secs')
