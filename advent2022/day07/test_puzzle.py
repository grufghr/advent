"""
Advent of Code - Test Case
"""
import unittest

import advent2022.day07.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 95437
    example_answer_part02 = 24933642

    answer_part01 = 1513699
    answer_part02 = 7991939

    def test_001_input_example(self):
        input_data = puzzle.input_data('input_example.txt')

        answer = puzzle.solve(input_data)
        answer_part01 = answer[0]
        self.assertEqual(answer_part01, self.example_answer_part01)

        answer_part02 = answer[1]
        self.assertEqual(answer_part02, self.example_answer_part02)

    def test_002_input(self):
        input_data = puzzle.input_data('input.txt')

        answer = puzzle.solve(input_data)
        answer_part01 = answer[0]
        self.assertEqual(answer_part01, self.answer_part01)

        answer_part02 = answer[1]
        self.assertEqual(answer_part02, self.answer_part02)
