Feature: AoC 2023 Day 03: Gear Ratios

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 4361

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 520019

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 467835

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 75519888
      And execution time < 1 secs
