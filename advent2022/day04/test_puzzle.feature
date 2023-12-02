Feature: AoC 2022 Day 04: Camp Cleanup

  Background: Regression testing
    Given advent 2022 day 04 puzzle

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 2

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 413

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 4

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 806
      And performance < 1 secs
