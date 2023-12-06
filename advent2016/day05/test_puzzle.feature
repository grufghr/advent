Feature: AoC 2016 Day 05: How About a Nice Game of Chess?

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 18f47a30

  @slow
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = f97c354d

  @slow
  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 05ace8e3

  @slow
  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 863dde27
