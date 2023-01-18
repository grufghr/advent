"""
Advent of Code - Test Case
"""
import unittest

import advent2016.day05.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    example_answer_part01 = ['18f47a30']
    example_answer_part02 = ['05ace8e3']

    answer_part01 = 'f97c354d'
    answer_part02 = '863dde27'

    def test_001_input_example(self):
        for test_case, input_data in enumerate(puzzle.input_data_iter('input_example.txt')):

            answer01 = puzzle.solve01(input_data)
            self.assertEqual(answer01, self.example_answer_part01[test_case])

            answer02 = puzzle.solve02(input_data)
            self.assertEqual(answer02, self.example_answer_part02[test_case])

    def test_002_input(self):
        input_data = next(puzzle.input_data_iter('input.txt'))

        answer01 = puzzle.solve01(input_data)
        self.assertEqual(answer01, self.answer_part01)

        answer02 = puzzle.solve02(input_data)
        self.assertEqual(answer02, self.answer_part02)
