Feature: AoC 2016 Day 02: Bathroom Security

  Background: Regression testing
    Given AoC puzzle
     Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 1985

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 12578

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 5DB3

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 516DD