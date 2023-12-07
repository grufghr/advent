Feature: AoC 2021 Day 12: Passage Pathing

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 226

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 5212

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 3509

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 134862
