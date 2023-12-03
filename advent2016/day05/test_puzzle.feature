Feature: AoC 2016 Day 05: How About a Nice Game of Chess?

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  @slow
  Scenario: part01 examples (execution time ~20 secs)
    Given example input in file "input_example.txt"
     When solve part01
     Then answer = 18f47a30

  @slow
  Scenario: part01 (execution time ~20 secs)
    Given input in file "input.txt"
     When solve part01
     Then answer = f97c354d

  @slow
  Scenario: part02 examples (execution time ~20 secs)
    Given example input in file "input_example.txt"
     When solve part02
     Then answer = 05ace8e3

  @slow
  Scenario: part02 (execution time ~20 secs)
    Given input in file "input.txt"
     When solve part02
     Then answer = 863dde27
      And execution time < 50 secs
