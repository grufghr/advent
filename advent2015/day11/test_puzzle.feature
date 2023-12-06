Feature: AoC 2015 Day 11: Corporate Policy

  Background: Regression testing
    Given AoC puzzle
      Then validate test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = abcdffaa

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = cqjxxyzz

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = abcdffaa

  @slow
  Scenario: part02
    Given input "cqjxxyzz"
     When solve part02
     Then expected part02 answer = cqkaabcc
