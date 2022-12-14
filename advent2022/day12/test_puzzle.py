"""
Advent of Code - Test Case
"""
import unittest

import advent2022.day12.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 31
    example_answer_part02 = 0

    answer_part01 = 456
    answer_part02 = 0

    def test_input_example(self):
        input_data = puzzle.input_data('input_example.txt')

        answer_part01 = puzzle.solve(input_data)
        self.assertEqual(answer_part01, self.example_answer_part01)

        # answer_part02 = puzzle.solve(input_data, 10000, True)
        # self.assertEqual(answer_part02, self.example_answer_part02)

    def test_input(self):
        input_data = puzzle.input_data('input.txt')

        answer_part01 = puzzle.solve(input_data)
        self.assertEqual(answer_part01, self.answer_part01)

        #answer_part02 = puzzle.solve(input_data, 10000, True)
        #self.assertEqual(answer_part02, self.answer_part02)
