Feature: AoC 2022 Day 09: Rope Bridge

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 1

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 6175

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 36

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 2578
