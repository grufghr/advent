Feature: AoC 2022 Day 14: Regolith Reservoir

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 24

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 913

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 93

  @slow
  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 30762
