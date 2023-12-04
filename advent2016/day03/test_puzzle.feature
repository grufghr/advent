Feature: AoC 2016 Day 03: Squares With Three Sides

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then expected answer = 4

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 869

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then expected answer = 7

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 1544
      And execution time < 1 secs
