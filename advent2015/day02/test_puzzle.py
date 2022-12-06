"""
Advent of Code - Test Case
"""
import unittest

import advent2015.day02.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 101
    example_answer_part02 = 48

    answer_part01 = 1586300
    answer_part02 = 3737498

    def test_input_example(self):
        input_data = puzzle.input_data('input_example.txt')

        answer = puzzle.solve(input_data)
        answer_part01 = answer[0]
        self.assertEqual(answer_part01, self.example_answer_part01)

        answer_part02 = answer[1]
        self.assertEqual(answer_part02, self.example_answer_part02)

    def test_input(self):
        input_data = puzzle.input_data('input.txt')

        answer = puzzle.solve(input_data)
        answer_part01 = answer[0]
        self.assertEqual(answer_part01, self.answer_part01)

        answer_part02 = answer[1]
        self.assertEqual(answer_part02, self.answer_part02)

