"""
Advent of Code - Test Case
"""
import unittest

import advent2016.day01.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = [5, 2, 12, 8]
    example_answer_part02 = [None, None, None, 4]

    answer_part01 = 242
    answer_part02 = 150

    def test_001_input_example(self):
        for test_case, input_text in enumerate(puzzle.input_data_iter('input_example.txt')):

            answer = puzzle.solve(input_text)
            answer01 = answer[0]
            self.assertEqual(answer01, self.example_answer_part01[test_case])

            answer02 = answer[1]
            self.assertEqual(answer02, self.example_answer_part02[test_case])

    def test_002_input(self):
        input_text = next(puzzle.input_data_iter('input.txt'))

        answer = puzzle.solve(input_text)
        answer01 = answer[0]
        self.assertEqual(answer01, self.answer_part01)

        answer02 = answer[1]
        self.assertEqual(answer02, self.answer_part02)
