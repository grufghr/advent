Feature: AoC 2015 Day 08: Matchsticks

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 12

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 1371

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 19

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 2117
      And execution time < 1 secs
