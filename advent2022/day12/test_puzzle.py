"""
Advent of Code - Test Case
"""
import unittest

import advent2022.day12.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 31
    example_answer_part02 = 29

    answer_part01 = 456
    answer_part02 = 454

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
