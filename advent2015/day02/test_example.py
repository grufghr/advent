#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021 - Test Case
"""
import os
import unittest

import advent2015.day02.puzzle as puzzle

class ExampleTest(unittest.TestCase):

    def test_solve(self):
        input_data_file = os.path.join(
            os.path.dirname(__file__), 'input_example.txt')

        answers = puzzle.solve(input_data_file)

        self.assertEqual(answers[0], 101)
        self.assertEqual(answers[1], 48)


if __name__ == '__main__':
    unittest.main()
