"""
Advent of Code - Test Case
"""
import unittest

import advent2022.day21.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example1_answer_part01 = 152
    example1_answer_part02 = 301

    example2_answer_part01 = 34
    example2_answer_part02 = 19

    answer_part01 = 21120928600114
    answer_part02 = 3453748220116

    def test_001_input_example1(self):
        input_data = puzzle.input_data('input_example1.txt')

        answer = puzzle.solve(input_data)
        self.assertEqual(answer[0], self.example1_answer_part01)
        self.assertEqual(answer[1], self.example1_answer_part02)

    def test_002_input_example2(self):
        input_data = puzzle.input_data('input_example2.txt')

        answer = puzzle.solve(input_data)
        self.assertEqual(answer[0], self.example2_answer_part01)
        self.assertEqual(answer[1], self.example2_answer_part02)

    def test_003_input(self):
        input_data = puzzle.input_data('input.txt')

        answer = puzzle.solve(input_data)
        self.assertEqual(answer[0], self.answer_part01)
        self.assertEqual(answer[1], self.answer_part02)
