Feature: AoC 2021 Day 10: Syntax Scoring

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 339477

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 3049320156
