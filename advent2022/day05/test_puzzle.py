"""
Advent of Code - Test Case
"""
import unittest

import advent2022.day05.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 'CMZ'
    example_answer_part02 = 'MCD'

    answer_part01 = 'FZCMJCRHZ'
    answer_part02 = 'JSDHQMZGF'

    def test_input_example(self):
        input_data = puzzle.input_data('input_example.txt')

        answer_part01 = puzzle.solve(
            input_data[0], input_data[1], puzzle.cratemover9000)
        self.assertEqual(answer_part01, self.example_answer_part01)

        answer_part02 = puzzle.solve(
            input_data[0], input_data[1], puzzle.cratemover9001)
        self.assertEqual(answer_part02, self.example_answer_part02)

    def test_input(self):
        input_data = puzzle.input_data('input.txt')

        answer_part01 = puzzle.solve(
            input_data[0], input_data[1], puzzle.cratemover9000)
        self.assertEqual(answer_part01, self.answer_part01)

        answer_part02 = puzzle.solve(
            input_data[0], input_data[1], puzzle.cratemover9001)
        self.assertEqual(answer_part02, self.answer_part02)
