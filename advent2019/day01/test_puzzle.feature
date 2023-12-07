Feature: AoC 2019 Day 01: The Tyranny of the Rocket Equation

  Background: Regression testing
    Given AoC puzzle
      Then correct test feature name

  Scenario: part01 example
    Given input in file "input_example.txt"
     When solve part01
     Then expected part01 answer = 34241

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected part01 answer = 3448043

  Scenario: part02 example
    Given input in file "input_example.txt"
     When solve part02
     Then expected part02 answer = 51316

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected part02 answer = 5169198
