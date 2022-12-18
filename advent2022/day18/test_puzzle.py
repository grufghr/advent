"""
Advent of Code - Test Case
"""
import unittest

import advent2022.day18.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 64
    example_answer_part02 = 58

    answer_part01 = 3364
    answer_part02 = 2006

    def test_input_example(self):
        input_data = puzzle.input_data('input_example.txt')

        answer = puzzle.solve(input_data)
        self.assertEqual(answer[0], self.example_answer_part01)

        self.assertEqual(answer[1], self.example_answer_part02)

    def test_input(self):
        input_data = puzzle.input_data('input.txt')

        answer = puzzle.solve(input_data)
        self.assertEqual(answer[0], self.answer_part01)

        self.assertEqual(answer[1], self.answer_part02)
