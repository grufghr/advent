#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2021 - Test Case
"""
import os
import unittest

import advent2021.day02.puzzle as puzzle


class PuzzleTest(unittest.TestCase):

    def test_input_example(self):
        input_data_file = os.path.join(
            os.path.dirname(__file__), 'input_example.txt')

        answers = puzzle.solve(input_data_file)

        self.assertEqual(answers[0], 150)
        self.assertEqual(answers[1], 900)
