Feature: AoC 2023 Day 02: Cube Conundrum

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 8

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 2716

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 2286

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 72227
      And execution time < 1 secs
