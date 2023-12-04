Feature: AoC 2022 Day 12: Hill Climbing Algorithm

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 31

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 456

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 29

  @slow
  Scenario: part02 (execution time ~5 secs)
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 454
      And execution time < 5 secs
