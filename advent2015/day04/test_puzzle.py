"""
Advent of Code - Test Case
"""
import unittest

import advent2015.day04.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = [609043, 1048970]
    example_answer_part02 = [6742839, 5714438]

    answer_part01 = 254575
    answer_part02 = 1038736

    def test_input_example(self):
        for test_case, input_text in enumerate(puzzle.input_data_iter('input_example.txt')):

            answer01 = puzzle.solve(input_text, 5)
            self.assertEqual(answer01, self.example_answer_part01[test_case])

            answer02 = puzzle.solve(input_text, 6)
            self.assertEqual(answer02, self.example_answer_part02[test_case])

    def test_input(self):
        input_text = next(puzzle.input_data_iter('input.txt'))

        answer01 = puzzle.solve(input_text, 5)
        self.assertEqual(answer01, self.answer_part01)

        answer02 = puzzle.solve(input_text, 6)
        self.assertEqual(answer02, self.answer_part02)
