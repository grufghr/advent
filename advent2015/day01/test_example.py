#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021 - Test Case
"""
import os
import unittest

import advent2015.day01.puzzle as puzzle


class ExampleTest(unittest.TestCase):

    def test_solve(self):
        input_data_file = os.path.join(
            os.path.dirname(__file__), 'input_example.txt')

        answers = puzzle.solve(input_data_file)

        self.assertEqual(answers[0][0], 0)
        self.assertEqual(answers[0][1], 0)
        self.assertEqual(answers[0][2], 3)
        self.assertEqual(answers[0][3], 3)
        self.assertEqual(answers[0][4], 3)
        self.assertEqual(answers[0][5], -1)
        self.assertEqual(answers[0][6], -1)
        self.assertEqual(answers[0][7], -3)
        self.assertEqual(answers[0][8], -3)

        self.assertEqual(answers[1][9], 1)
        self.assertEqual(answers[1][10], 5)

        self.assertEqual(len(answers[0]), 11)


if __name__ == '__main__':
    unittest.main()
