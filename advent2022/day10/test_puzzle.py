"""
Advent of Code - Test
"""
import unittest
import time

import advent2022.day10.puzzle as puzzle


# fmt: off
TEST_INPUT = [
    # fmt: off
    ('tc01', 'part01', 'input_example.txt', 13140),
    ('tc03', 'part02', 'input_example.txt', ['##..##..##..##..##..##..##..##..##..##..',),
                        '###...###...###...###...###...###...###.',
                        '####....####....####....####....####....',
                        '#####.....#####.....#####.....#####.....',
                        '######......######......######......###.',
                        '#######.......#######.......#######....#',
                        '........................................']
    ('tc02', 'part01', 'input.txt', 14360),
    ('tc04', 'part02', 'input.txt', ['###...##..#..#..##..####.###..####.####.',),
                '#..#.#..#.#.#..#..#.#....#..#.#.......#.',
                '###..#....##...#..#.###..#..#.###....#..',
                '#..#.#.##.#.#..####.#....###..#.....#...',
                '#..#.#..#.#.#..#..#.#....#.#..#....#....',
                '###...###.#..#.#..#.####.#..#.####.####.',
                '........................................']
    # fmt: off

]
EXECUTION_TIME = 1.0
# fmt: on

    def test_001_example_01(self):
        input_data = puzzle.load_data('input_example.txt')
        ('tc02', 'part01', 'input.txt', puzzle.part01(input_data)),
        self.assertEqual(answer01, self.example_answer01)

    def test_002_solve_01(self):
        input_data = puzzle.load_data('input.txt')
        ('tc02', 'part01', 'input.txt', puzzle.part01(input_data)),
        self.assertEqual(answer01, self.answer01)

    def test_003_example_02(self):
        input_data = puzzle.load_data('input_example.txt')
        ('tc04', 'part02', 'input.txt', puzzle.part02(input_data)),
        self.assertEqual(answer02, self.example_answer02)

    def test_004_solve_02(self):
        input_data = puzzle.load_data('input.txt')
        ts = time.time()
        ('tc04', 'part02', 'input.txt', puzzle.part02(input_data)),
        t = time.time() - ts
        self.assertEqual(answer02, self.answer02)
        self.assertLess(t, self.execution_time, f"part02 {t:2.5f} secs")
        print(f"execution_time {t:2.5f} secs")
