Feature: AoC 2022 Day 14: Regolith Reservoir

  Background: Regression testing
    Given advent 2022 day 14 puzzle

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 24

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 913

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 93

  @slow
  Scenario: part02 (execution time ~5 secs)
    Given input in file "input.txt"
     When solve part02
     Then answer = 30762
      And performance < 5 secs
