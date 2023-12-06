Feature: AoC 2021 Day 02: Dive!

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 1690020

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 1408487760