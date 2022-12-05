#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021 - Test Case
"""
import os
import unittest

import advent2015.day03.puzzle as puzzle


class ExampleTest(unittest.TestCase):

    def test_solve(self):
        input_data_file = os.path.join(
            os.path.dirname(__file__), 'input_example.txt')

        answers = puzzle.solve(input_data_file)

        self.assertEqual(answers[0][0], 2)
        self.assertEqual(answers[0][1], 4)
        self.assertEqual(answers[0][2], 2)
        self.assertEqual(answers[0][3], 2)

        self.assertEqual(len(answers[0]), 4)

        self.assertEqual(answers[1][0], 2)
        self.assertEqual(answers[1][1], 3)
        self.assertEqual(answers[1][2], 11)
        self.assertEqual(answers[1][3], 3)

        self.assertEqual(len(answers[1]), 4)


if __name__ == '__main__':
    unittest.main()
