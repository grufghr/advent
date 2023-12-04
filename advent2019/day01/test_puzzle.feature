Feature: AoC 2019 Day 01: The Tyranny of the Rocket Equation
  
  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01 examples
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 34241
  
  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then answer = 3448043

  Scenario: part02 examples
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 51316

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then answer = 5169198
      And execution time < 1 secs
