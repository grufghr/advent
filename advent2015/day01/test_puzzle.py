"""
Advent of Code - Test Case
"""
import unittest

import advent2015.day01.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = [0, 0, 3, 3, 3, -1, -1, -3, -3, -1, -1]
    example_answer_part02 = [0, 0, 0, 0, 1, 3, 1, 1, 1, 1, 5]

    answer_part01 = 280
    answer_part02 = 1797

    def test_input_example(self):
        for test_case, input_text in enumerate(puzzle.input_data_iter('input_example.txt')):

            answer = puzzle.solve(input_text)
            answer01 = answer[0]
            self.assertEqual(answer01, self.example_answer_part01[test_case])

            answer02 = answer[1]
            self.assertEqual(answer02, self.example_answer_part02[test_case])

    def test_input(self):
        input_text = next(puzzle.input_data_iter('input.txt'))

        answer = puzzle.solve(input_text)
        answer01 = answer[0]
        self.assertEqual(answer01, self.answer_part01)

        answer02 = answer[1]
        self.assertEqual(answer02, self.answer_part02)
