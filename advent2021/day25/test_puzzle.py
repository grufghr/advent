"""
Advent of Code - Test Case
"""
import unittest

import advent2021.day25.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 58

    answer_part01 = 532

    def test_input_example(self):
        input_data = puzzle.input_data('input_example.txt')

        answer = puzzle.solve(input_data)
        self.assertEqual(answer, self.example_answer_part01)

        # no part 02

    def test_input(self):
        input_data = puzzle.input_data('input.txt')

        answer = puzzle.solve(input_data)
        self.assertEqual(answer, self.answer_part01)

        # no part 02
