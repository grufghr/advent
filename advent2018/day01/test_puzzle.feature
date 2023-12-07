Feature: AoC 2018 Day 01: Chronal Calibration

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 0

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 599

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 6

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 81204
