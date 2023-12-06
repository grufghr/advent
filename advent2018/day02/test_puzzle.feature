Feature: AoC 2018 Day 02: Inventory Management System

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example_01.txt"
     When solve part01
     Then expected part01 answer = 12

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 7163

  Scenario: part02 example
    Given input in file "input_example_02.txt"
     When solve part02
     Then expected part02 answer = fgij

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = ighfbyijnoumxjlxevacpwqtr
