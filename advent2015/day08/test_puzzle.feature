Feature: AoC 2015 Day 08: Matchsticks

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 12

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 1371

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 19

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 2117
