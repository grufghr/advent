"""
Advent of Code - Test Case
"""
import unittest

import advent2022.day11.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 10605
    example_answer_part02 = 2713310158

    answer_part01 = 56595
    answer_part02 = 15693274740

    def test_001_input_example(self):
        input_data = puzzle.input_data('input_example.txt')

        answer_part01 = puzzle.solve(input_data, 20)
        self.assertEqual(answer_part01, self.example_answer_part01)

        answer_part02 = puzzle.solve(input_data, 10000, True)
        self.assertEqual(answer_part02, self.example_answer_part02)

    def test_002_input(self):
        input_data = puzzle.input_data('input.txt')

        answer_part01 = puzzle.solve(input_data, 20)
        self.assertEqual(answer_part01, self.answer_part01)

        answer_part02 = puzzle.solve(input_data, 10000, True)
        self.assertEqual(answer_part02, self.answer_part02)
