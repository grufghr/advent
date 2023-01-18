"""
Advent of Code - Test Case
"""
import unittest

import advent2022.day13.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 13
    example_answer_part02 = 140

    answer_part01 = 5806
    answer_part02 = 23600

    def test_001_input_example(self):
        input_data = puzzle.input_data('input_example.txt')

        answer = puzzle.solve(input_data)
        self.assertEqual(answer[0], self.example_answer_part01)

        self.assertEqual(answer[1], self.example_answer_part02)

    def test_002_input(self):
        input_data = puzzle.input_data('input.txt')

        answer = puzzle.solve(input_data)
        self.assertEqual(answer[0], self.answer_part01)

        self.assertEqual(answer[1], self.answer_part02)
