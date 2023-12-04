Feature: AoC 2018 Day 02: Inventory Management System

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example01.txt"
     When solve part01
     Then expected answer = 12

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 7163

  Scenario: part02 examples
    Given example input in file "input_example02.txt"
     When solve part02
     Then expected answer = fgij

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = ighfbyijnoumxjlxevacpwqtr
      And execution time < 1 secs
