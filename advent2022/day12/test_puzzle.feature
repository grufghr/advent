Feature: AoC 2022 Day 12: Hill Climbing Algorithm

  Background: Regression testing
    Given advent 2022 day 12 puzzle

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 31

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 456

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 29

  @slow
  Scenario: part02 (execution time ~5 secs)
    Given input in file "input.txt"
     When solve part02
     Then answer = 454
      And performance < 5 secs
