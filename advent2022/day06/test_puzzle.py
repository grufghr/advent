#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code - Test Case
"""
import os
import unittest

import advent2022.day06.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    def test_input_example(self):
        input_data_file = os.path.join(
            os.path.dirname(__file__), 'input_example.txt')

        answers = puzzle.solve(input_data_file)

        self.assertEqual(answers[0][0], 7)
        self.assertEqual(answers[0][1], 5)
        self.assertEqual(answers[0][2], 6)
        self.assertEqual(answers[0][3], 10)
        self.assertEqual(answers[0][4], 11)

        self.assertEqual(len(answers[0]), 5)

        self.assertEqual(answers[1][0], 19)
        self.assertEqual(answers[1][1], 23)
        self.assertEqual(answers[1][2], 23)
        self.assertEqual(answers[1][3], 29)
        self.assertEqual(answers[1][4], 26)

        self.assertEqual(len(answers[1]), 5)
