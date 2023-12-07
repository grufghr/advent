Feature: AoC 2021 Day 10: Syntax Scoring

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 26397

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 339477

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 288957

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 3049320156
