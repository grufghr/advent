Feature: AoC 2022 Day 04: Camp Cleanup

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 2

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 413

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 4

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 806
      And execution time < 1 secs
