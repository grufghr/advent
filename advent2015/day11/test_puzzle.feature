Feature: AoC 2015 Day 11: Corporate Policy

  Background: Regression testing
    Given AoC puzzle
     Then validate test feature name

  @slow
  Scenario: part01 (execution time ~5 secs)
    Given input in file "input.txt"
     When solve part01
     Then expected answer = cqjxxyzz

  @slow
  Scenario: part02 (execution time ~5 secs)
    Given input "cqjxxyzz"
     When solve part02
     Then expected answer = cqkaabcc
