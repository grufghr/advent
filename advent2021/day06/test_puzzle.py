"""
Advent of Code - Test Case
"""
import unittest

import advent2021.day06.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 5934
    example_answer_part02 = 26984457539

    answer_part01 = 380243
    answer_part02 = 1708791884591

    def test_001_input_example(self):
        input_data = puzzle.parse_data(puzzle.load_data('input_example.txt'))

        answer = puzzle.solve(input_data, 80)
        self.assertEqual(answer, self.example_answer_part01)

        answer = puzzle.solve(input_data, 256)
        self.assertEqual(answer, self.example_answer_part02)

    def test_002_input(self):
        input_data = puzzle.parse_data(puzzle.load_data('input.txt'))

        answer = puzzle.solve(input_data, 80)
        self.assertEqual(answer, self.answer_part01)

        answer = puzzle.solve(input_data, 256)
        self.assertEqual(answer, self.answer_part02)
