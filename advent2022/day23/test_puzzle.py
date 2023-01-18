"""
Advent of Code - Test Case
"""
import unittest

import advent2022.day23.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 110
    example_answer_part02 = 20

    answer_part01 = 4218
    answer_part02 = 976

    def test_001_input_example1(self):
        input_data = puzzle.input_data('input_example.txt')

        answer = puzzle.solve(input_data, 10)
        self.assertEqual(answer[0], self.example_answer_part01)

        answer = puzzle.solve(input_data, 25)
        self.assertEqual(answer[1], self.example_answer_part02)

    def test_002_input(self):
        input_data = puzzle.input_data('input.txt')

        answer = puzzle.solve(input_data, 10)
        self.assertEqual(answer[0], self.answer_part01)

        answer = puzzle.solve(input_data, 1000)
        self.assertEqual(answer[1], self.answer_part02)
