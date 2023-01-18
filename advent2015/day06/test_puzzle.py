"""
Advent of Code - Test Case
"""
import unittest

import advent2015.day06.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 998996
    example_answer_part02 = 1001996

    answer_part01 = 543903
    answer_part02 = 14687245

    def test_001_input_example(self):
        input_text = puzzle.input_data('input_example.txt')

        answer = puzzle.solve(input_text)
        self.assertEqual(answer[0], self.example_answer_part01)

        self.assertEqual(answer[1], self.example_answer_part02)

    def test_002_input(self):
        input_text = puzzle.input_data('input.txt')

        answer = puzzle.solve(input_text)
        self.assertEqual(answer[0], self.answer_part01)

        self.assertEqual(answer[1], self.answer_part02)
