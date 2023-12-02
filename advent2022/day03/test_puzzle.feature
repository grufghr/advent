Feature: AoC 2022 Day 03: Rucksack Reorganization

  Background: Regression testing
    Given advent 2022 day 03 puzzle

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 157

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 8243

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 70

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 2631
      And performance < 1 seconds
