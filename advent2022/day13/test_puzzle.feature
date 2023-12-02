Feature: AoC 2022 Day 13: Distress Signal

  Background: Regression testing
    Given advent 2022 day 13 puzzle

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 13

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 5806

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 140

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 23600
      And performance < 1 secs
