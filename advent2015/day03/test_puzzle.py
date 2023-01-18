"""
Advent of Code - Test Case
"""
import unittest

import advent2015.day03.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = [2, 4, 2, 2]
    example_answer_part02 = [2, 3, 11, 3]

    answer_part01 = 2081
    answer_part02 = 2341

    def test_001_input_example(self):
        for test_case, input_text in enumerate(puzzle.input_data_iter('input_example.txt')):

            answer01 = puzzle.solve(input_text)
            self.assertEqual(answer01, self.example_answer_part01[test_case])

            answer02 = puzzle.solve(input_text, 2)
            self.assertEqual(answer02, self.example_answer_part02[test_case])

    def test_002_input(self):
        input_text = next(puzzle.input_data_iter('input.txt'))

        answer01 = puzzle.solve(input_text)
        self.assertEqual(answer01, self.answer_part01)

        answer02 = puzzle.solve(input_text, 2)
        self.assertEqual(answer02, self.answer_part02)
