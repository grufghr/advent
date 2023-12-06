Feature: AoC 2015 Day 08: Matchsticks

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  Scenario: part01
    Given input in file "input.txt"
     When solve part01
     Then expected answer = 1371

  Scenario: part02
    Given input in file "input.txt"
     When solve part02
     Then expected answer = 2117
