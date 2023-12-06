Feature: AoC 2015 Day 10: Elves Look, Elves Say

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 360154

  @slow
  Scenario: part02 (execution time ~7 secs)
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 5103798
