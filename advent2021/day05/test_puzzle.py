"""
Advent of Code - Test Case
"""
import unittest

import advent2021.day05.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 5
    example_answer_part02 = 12

    answer_part01 = 6666
    answer_part02 = 19081

    def test_001_input_example(self):
        input_data = puzzle.input_data('input_example.txt')

        answer_part01 = puzzle.solve(input_data)
        self.assertEqual(answer_part01, self.example_answer_part01)

        answer_part02 = puzzle.solve(input_data, True)
        self.assertEqual(answer_part02, self.example_answer_part02)

    def test_002_input(self):
        input_data = puzzle.input_data('input.txt')

        answer_part01 = puzzle.solve(input_data)
        self.assertEqual(answer_part01, self.answer_part01)

        answer_part02 = puzzle.solve(input_data, True)
        self.assertEqual(answer_part02, self.answer_part02)
