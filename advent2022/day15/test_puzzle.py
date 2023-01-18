"""
Advent of Code - Test Case
"""
import unittest

import advent2022.day15.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = 26
    example_answer_part02 = 56000011

    answer_part01 = 5716881
    answer_part02 = 0

    def test_001_input_example(self):
        input_data = puzzle.input_data('input_example.txt')

        answer = puzzle.solve(input_data, 10)
        self.assertEqual(answer, self.example_answer_part01)

        #answer = puzzle.solve(input_data, True, False)
        #self.assertEqual(answer, self.example_answer_part02)

    def test_002_input(self):
        input_data = puzzle.input_data('input.txt')

        answer = puzzle.solve(input_data, 2000000)
        self.assertEqual(answer, self.answer_part01)

        #answer = puzzle.solve(input_data, True, False)
        #self.assertEqual(answer, self.answer_part02)
