"""
Advent of Code - Test Case
"""
import unittest

import advent2015.day04.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answers_part01 = [609043, 1048970]
    example_answers_part02 = [6742839, 5714438]

    answer_part01 = 254575
    answer_part02 = 1038736

    def test_input_example(self):
        for test_case, input_text in enumerate(puzzle.input_file('input_example.txt')):

            answer = puzzle.solve(input_text, 5)
            self.assertEqual(answer, self.example_answers_part01[test_case])

            answer = puzzle.solve(input_text, 6)
            self.assertEqual(answer, self.example_answers_part02[test_case])

    def test_input(self):
        input_text = next(puzzle.input_file('input.txt'))

        answer = puzzle.solve(input_text, 5)
        self.assertEqual(answer, self.answer_part01)

        answer = puzzle.solve(input_text, 6)
        self.assertEqual(answer, self.answer_part02)

