Feature: AoC 2016 Day 02: Bathroom Security

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 1985

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 12578

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 5DB3

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 516DD
      And execution time < 1 secs
