"""
Advent of Code - Test Case
"""
import unittest

import advent2021.day07.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 37
    example_answer_part02 = 168

    answer_part01 = 323647
    answer_part02 = 87640209

    def test_001_input_example(self):
        input_data = puzzle.load_data('input_example.txt')

        answer = puzzle.solve01(input_data)
        self.assertEqual(answer, self.example_answer_part01)

        answer = puzzle.solve02(input_data)
        self.assertEqual(answer, self.example_answer_part02)

    def test_002_input(self):
        input_data = puzzle.load_data('input.txt')

        answer = puzzle.solve01(input_data)
        self.assertEqual(answer, self.answer_part01)

        answer = puzzle.solve02(input_data)
        self.assertEqual(answer, self.answer_part02)
