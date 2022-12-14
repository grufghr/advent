"""
Advent of Code - Test Case
"""
import unittest

import advent2022.day09.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 13
    example_answer_part02 = 1

    example02_answer_part01 = 88
    example02_answer_part02 = 36

    answer_part01 = 6175
    answer_part02 = 2578

    def test_input_example(self):
        input_data = puzzle.input_data('input_example.txt')

        answer_part01 = puzzle.solve(input_data)
        self.assertEqual(answer_part01, self.example_answer_part01)

        answer_part02 = puzzle.solve(input_data, 10)
        self.assertEqual(answer_part02, self.example_answer_part02)

    def test_input_example02(self):
        input_data = puzzle.input_data('input_exampleB.txt')

        answer_part01 = puzzle.solve(input_data)
        self.assertEqual(answer_part01, self.example02_answer_part01)

        answer_part02 = puzzle.solve(input_data, 10)
        self.assertEqual(answer_part02, self.example02_answer_part02)

    def test_input(self):
        input_data = puzzle.input_data('input.txt')

        answer_part01 = puzzle.solve(input_data)
        self.assertEqual(answer_part01, self.answer_part01)

        answer_part02 = puzzle.solve(input_data, 10)
        self.assertEqual(answer_part02, self.answer_part02)
