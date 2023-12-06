Feature: AoC 2016 Day 05: How About a Nice Game of Chess?

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  @slow
  Scenario: part01 (execution time ~20 secs)
    Given input in file "input.txt"
     When solve part01
     Then expected answer = f97c354d

  @slow
  Scenario: part02 (execution time ~20 secs)
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 863dde27
