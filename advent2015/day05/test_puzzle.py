"""
Advent of Code - Test Case
"""
import unittest

import advent2015.day05.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 2
    example_answer_part02 = 2

    answer_part01 = 238
    answer_part02 = 69

    def test_input_example(self):
        input_text = puzzle.input_data('input_example.txt')

        answer01 = puzzle.solve_part01(input_text)
        self.assertEqual(answer01, self.example_answer_part01)

        answer02 = puzzle.solve_part02(input_text)
        self.assertEqual(answer02, self.example_answer_part02)

    def test_input(self):
        input_text = puzzle.input_data('input.txt')

        answer01 = puzzle.solve_part01(input_text)
        self.assertEqual(answer01, self.answer_part01)

        answer02 = puzzle.solve_part02(input_text)
        self.assertEqual(answer02, self.answer_part02)
