"""
Advent of Code - Test Case
"""
import unittest

import advent2022.day06.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = [7, 5, 6, 10, 11]
    example_answer_part02 = [19, 23, 23, 29, 26]

    answer_part01 = 1531
    answer_part02 = 2518

    def test_001_input_example(self):
        for test_case, input_text in enumerate(puzzle.input_data_iter('input_example.txt')):

            answer01 = puzzle.solve(input_text, 4)
            self.assertEqual(answer01, self.example_answer_part01[test_case])

            answer02 = puzzle.solve(input_text, 14)
            self.assertEqual(answer02, self.example_answer_part02[test_case])

    def test_002_input(self):
        input_text = next(puzzle.input_data_iter('input.txt'))

        answer01 = puzzle.solve(input_text, 4)
        self.assertEqual(answer01, self.answer_part01)

        answer02 = puzzle.solve(input_text, 14)
        self.assertEqual(answer02, self.answer_part02)
